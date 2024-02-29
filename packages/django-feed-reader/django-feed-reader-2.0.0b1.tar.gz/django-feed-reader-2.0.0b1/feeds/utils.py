from django.db.models import Q, F
from django.utils import timezone
from django.conf import settings


from feeds.models import Source, Enclosure, Post, Subscription

import feedparser as parser

import time
import datetime
import hashlib

import requests

import pyrfc3339
import json

import logging

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

VERIFY_HTTPS = True
if hasattr(settings, "FEEDS_VERIFY_HTTPS"):
    VERIFY_HTTPS = settings.FEEDS_VERIFY_HTTPS

KEEP_OLD_ENCLOSURES = False
if hasattr(settings, "FEEDS_KEEP_OLD_ENCLOSURES"):
    KEEP_OLD_ENCLOSURES = settings.FEEDS_KEEP_OLD_ENCLOSURES

SAVE_JSON = False
if hasattr(settings, "FEEDS_SAVE_JSON"):
    SAVE_JSON = settings.FEEDS_SAVE_JSON


class LogOutput(object):

    def __init__(self, log_level: int = logging.DEBUG):
        self.log_level = log_level

    # little class for when we have no outputter
    def write(self, strin: str):

        if strin.startswith("\n"):
            strin = strin[1:]

        if strin.endswith("\n"):
            strin = strin[:-1]

        logging.log(self.log_level, strin)


@receiver(post_delete)
def delete_subscriber(sender, instance, **kwargs):
    if sender == Subscription and instance.source is not None:
        instance.source.update_subscriber_count()


@receiver(post_save)
def save_subscriber(sender, instance, **kwargs):
    if sender == Subscription and instance.source is not None:
        instance.source.update_subscriber_count()


def _customize_sanitizer(fp):

    bad_attributes = [
        "align",
        "valign",
        "hspace",
        "width",
        "height"
    ]

    for item in bad_attributes:
        try:
            if item in fp.sanitizer._HTMLSanitizer.acceptable_attributes:
                fp.sanitizer._HTMLSanitizer.acceptable_attributes.remove(item)
        except Exception:
            logging.debug("Could not remove {}".format(item))


def get_agent(source_feed):

    agent = "{user_agent} (+{server}; Updater; {subs} subscribers)".format(user_agent=settings.FEEDS_USER_AGENT, server=settings.FEEDS_SERVER, subs=source_feed.subscriber_count)
    return agent


def fix_relative(html, url):

    """ this is fucking cheesy """
    try:
        base = "/".join(url.split("/")[:3])

        html = html.replace("src='//", "src='http://")
        html = html.replace('src="//', 'src="http://')

        html = html.replace("src='/", "src='%s/" % base)
        html = html.replace('src="/', 'src="%s/' % base)

        html = html.replace("href='//", "href='http://")
        html = html.replace('href="//', 'href="http://')

        html = html.replace("href='/", "href='%s/" % base)
        html = html.replace('href="/', 'href="%s/' % base)

    except Exception:
        pass

    return html


def update_feeds(max_feeds=3, output=LogOutput()):

    todo = Source.objects.filter(Q(due_poll__lt=timezone.now()) & Q(live=True))

    output.write("Queue size is {}".format(todo.count()))

    sources = todo.order_by("due_poll")[:max_feeds]

    output.write("\nProcessing %d\n\n" % sources.count())

    for src in sources:
        read_feed(src, output)


def read_feed(source_feed, output=LogOutput()):

    old_interval = source_feed.interval

    was302 = False

    output.write("\n------------------------------\n")

    source_feed.last_polled = timezone.now()

    agent = get_agent(source_feed)

    headers = {"User-Agent": agent}  # identify ourselves

    feed_url = source_feed.feed_url
    if source_feed.is_cloudflare:  # Fuck you !

        if settings.FEEDS_CLOUDFLARE_WORKER:
            feed_url = "{}/read/?target={}".format(settings.FEEDS_CLOUDFLARE_WORKER, feed_url)

    if source_feed.etag:
        headers["If-None-Match"] = str(source_feed.etag)
    if source_feed.last_modified:
        headers["If-Modified-Since"] = str(source_feed.last_modified)

    output.write("\nFetching %s" % feed_url)

    ret = None
    try:
        ret = requests.get(feed_url, headers=headers, verify=VERIFY_HTTPS, allow_redirects=False, timeout=20)
        source_feed.status_code = ret.status_code
        source_feed.last_result = "Unhandled Case"
        output.write(str(ret))
    except Exception as ex:
        source_feed.last_result = ("Fetch error:" + str(ex))[:255]
        source_feed.status_code = 0
        output.write("\nFetch error: " + str(ex))

    if ret is None and source_feed.status_code == 1:  # er ??
        pass
    elif ret is None or source_feed.status_code == 0:
        source_feed.interval += 120
    elif ret.status_code < 200 or ret.status_code >= 500:
        # errors, impossible return codes
        source_feed.interval += 120
        source_feed.last_result = "Server error fetching feed (%d)" % ret.status_code
    elif ret.status_code == 404:
        # not found
        source_feed.interval += 120
        source_feed.last_result = "The feed could not be found"
    elif ret.status_code == 410:  # Gone
        source_feed.last_result = "Feed has gone away and says it isn't coming back."
        source_feed.live = False
    elif ret.status_code == 403:  # Forbidden
        if "Cloudflare" in ret.text or ("Server" in ret.headers and "cloudflare" in ret.headers["Server"]):
            source_feed.is_cloudflare = True
            source_feed.last_result = "Blocked by Cloudflare (grr)"
        else:
            source_feed.last_result = "Feed is no longer accessible."
            source_feed.live = False

    elif ret.status_code >= 400 and ret.status_code < 500:
        # treat as bad request
        source_feed.live = False
        source_feed.last_result = "Bad request (%d)" % ret.status_code
    elif ret.status_code == 304:
        # not modified
        source_feed.interval += 10
        source_feed.last_result = "Not modified"
        source_feed.last_success = timezone.now()

        if source_feed.last_success and (timezone.now() - source_feed.last_success).days > 7:
            source_feed.last_result = "Clearing etag/last modified due to lack of changes"
            source_feed.etag = None
            source_feed.last_modified = None

    elif ret.status_code == 301 or ret.status_code == 308:  # permenant redirect
        new_url = ""
        try:
            if "Location" in ret.headers:
                new_url = ret.headers["Location"]

                if new_url[0] == "/":
                    # find the domain from the feed

                    base = "/".join(source_feed.feed_url.split("/")[:3])

                    new_url = base + new_url

                source_feed.feed_url = new_url
                source_feed.last_result = "Moved"
                source_feed.save(update_fields=["feed_url", "last_result"])

            else:
                source_feed.last_result = "Feed has moved but no location provided"
        except Exception:
            output.write("\nError redirecting.")
            source_feed.last_result = ("Error redirecting feed to " + new_url)[:255]
            pass
    elif ret.status_code == 302 or ret.status_code == 303 or ret.status_code == 307:  # Temporary redirect
        new_url = ""
        was302 = True
        try:
            new_url = ret.headers["Location"]

            if new_url[0] == "/":
                # find the domain from the feed
                start = source_feed.feed_url[:8]
                end = source_feed.feed_url[8:]
                if end.find("/") >= 0:
                    end = end[:end.find("/")]

                new_url = start + end + new_url

            ret = requests.get(new_url, headers=headers, allow_redirects=True, timeout=20, verify=VERIFY_HTTPS)
            source_feed.status_code = ret.status_code
            source_feed.last_result = ("Temporary Redirect to " + new_url)[:255]

            if source_feed.last_302_url == new_url:
                # this is where we 302'd to last time
                td = timezone.now() - source_feed.last_302_start
                if td.days > 60:
                    source_feed.feed_url = new_url
                    source_feed.last_302_url = " "
                    source_feed.last_302_start = None
                    source_feed.last_result = ("Permanent Redirect to " + new_url)[:255]

                    source_feed.save(update_fields=["feed_url", "last_result", "last_302_url", "last_302_start"])

                else:
                    source_feed.last_result = ("Temporary Redirect to " + new_url + " since " + source_feed.last_302_start.strftime("%d %B"))[:255]

            else:
                source_feed.last_302_url = new_url
                source_feed.last_302_start = timezone.now()

                source_feed.last_result = ("Temporary Redirect to " + new_url + " since " + source_feed.last_302_start.strftime("%d %B"))[:255]

        except Exception as ex:
            source_feed.last_result = ("Failed Redirection to " + new_url + " " + str(ex))[:255]
            source_feed.interval += 60

    # NOT ELIF, WE HAVE TO START THE IF AGAIN TO COPE WTIH 302
    if ret and ret.status_code >= 200 and ret.status_code < 300:  # now we are not following redirects 302,303 and so forth are going to fail here, but what the hell :)

        # great!
        ok = True
        changed = False

        if was302:
            source_feed.etag = None
            source_feed.last_modified = None
        else:
            try:
                source_feed.etag = ret.headers["etag"]
            except Exception:
                source_feed.etag = None
            try:
                source_feed.last_modified = ret.headers["Last-Modified"]
            except Exception:
                source_feed.last_modified = None

        output.write("\netag:%s\nLast Mod:%s\n\n" % (source_feed.etag, source_feed.last_modified))

        content_type = "Not Set"
        if "Content-Type" in ret.headers:
            content_type = ret.headers["Content-Type"]

        (ok, changed) = import_feed(source_feed=source_feed, feed_body=ret.content, content_type=content_type, output=output)

        if ok and changed:
            source_feed.interval /= 2
            source_feed.last_result = " OK (updated)"  # and temporary redirects
            source_feed.last_change = timezone.now()

        elif ok:
            source_feed.last_result = " OK"
            source_feed.interval += 20  # we slow down feeds a little more that don't send headers we can use
        else:  # not OK
            source_feed.interval += 120

    if source_feed.interval < 60:
        source_feed.interval = 60  # no less than 1 hour
    if source_feed.interval > (60 * 24):
        source_feed.interval = (60 * 24)  # no more than a day

    output.write("\nUpdating source_feed.interval from %d to %d\n" % (old_interval, source_feed.interval))
    td = datetime.timedelta(minutes=source_feed.interval)
    source_feed.due_poll = timezone.now() + td
    source_feed.save(update_fields=[
                "due_poll", "interval", "last_result",
                "last_modified", "etag", "last_302_start",
                "last_302_url", "last_success", "live",
                "status_code", "max_index", "is_cloudflare",
                "last_change",
            ])


def import_feed(source_feed, feed_body, content_type, output=LogOutput()):

    ok = False
    changed = False

    if "xml" in content_type or feed_body[0:1] == b"<":
        (ok, changed) = parse_feed_xml(source_feed, feed_body, output)
    elif "json" in content_type or feed_body[0:1] == b"{":
        (ok, changed) = parse_feed_json(source_feed, str(feed_body, "utf-8"), output)
    else:
        ok = False
        source_feed.last_result = "Unknown Feed Type: " + content_type

    if ok and changed:
        source_feed.last_result = " OK (updated)"  # and temporary redirects
        source_feed.last_change = timezone.now()

        idx = source_feed.max_index
        # give indices to posts based on created date
        posts = Post.objects.filter(Q(source=source_feed) & Q(index=0)).order_by("created")
        for p in posts:
            idx += 1
            p.index = idx
            p.save(update_fields=["index"])

        source_feed.max_index = idx

    return (ok, changed)


def make_guid(e_id, e_url, body):
    if is_valid_post_guid(e_id):
        return e_id
    elif is_valid_post_guid(e_url):
        return e_url
    else:
        return hash_body(body)


def hash_body(body):
    m = hashlib.md5()
    m.update(body.encode("utf-8"))
    return m.hexdigest()


def is_valid_post_guid(x):
    return (x is not None) and (len(x) <= Post.GUID_MAX_LENGTH)


def parse_feed_xml(source_feed, feed_content, output):

    ok = True
    changed = False

    if source_feed.posts.all().count() == 0:
        is_first = True
    else:
        is_first = False

    # output.write(ret.content)
    try:

        _customize_sanitizer(parser)
        f = parser.parse(feed_content)  # need to start checking feed parser errors here
        entries = f['entries']
        if len(entries):
            source_feed.last_success = timezone.now()  # in case we start auto unsubscribing long dead feeds
        else:
            source_feed.last_result = "Feed is empty"
            ok = False

    except Exception:
        source_feed.last_result = "Feed Parse Error"
        entries = []
        ok = False

    source_feed.save(update_fields=["last_success", "last_result"])

    if ok:
        try:
            source_feed.name = f.feed.title
            source_feed.save(update_fields=["name"])
        except Exception as ex:
            output.write("\nUpdate name error:" + str(ex))
            pass

        try:
            source_feed.site_url = f.feed.link
            source_feed.save(update_fields=["site_url"])
        except Exception:
            pass

        try:
            source_feed.image_url = f.feed.image.href
            source_feed.save(update_fields=["image_url"])
        except Exception:
            pass

        # either of these is fine, prefer description over summary
        # also feedparser will give us itunes:summary etc if there
        try:
            source_feed.description = f.feed.summary
        except Exception:
            pass

        try:
            source_feed.description = f.feed.description
        except Exception:
            pass

        try:
            source_feed.save(update_fields=["description"])
        except Exception:
            pass

        # output.write(entries)
        entries.reverse()  # Entries are typically in reverse chronological order - put them in right order
        for e in entries:
            # we are going to take the longest
            body = ""

            if hasattr(e, "summary"):
                if len(e.summary) > len(body):
                    body = e.summary

            if hasattr(e, "summary_detail"):
                if len(e.summary_detail.value) >= len(body):
                    body = e.summary_detail.value

            if hasattr(e, "description"):
                if len(e.description) >= len(body):
                    body = e.description

            # This can be a content:encoded html body
            # but it can also be the alt-text of an an Enclosure
            if hasattr(e, "content"):
                for c in e.content:
                    if c.get("type", "") == "text/html" and len(c.get("value", "")) > len(body):
                        body = c.value

            body = fix_relative(body, source_feed.site_url)
            e_guid = getattr(e, 'guid', None)
            e_link = getattr(e, 'link', None)
            guid = make_guid(e_guid, e_link, body)
            try:
                p = Post.objects.filter(source=source_feed).filter(guid=guid)[0]
                output.write("EXISTING " + guid + "\n")

            except Exception:
                output.write("NEW " + guid + "\n")
                p = Post(index=0, body=" ", title="", guid=guid)
                p.found = timezone.now()
                changed = True

                try:
                    p.created = datetime.datetime.fromtimestamp(time.mktime(e.published_parsed)).replace(tzinfo=datetime.timezone.utc)
                except Exception:
                    try:
                        p.created = datetime.datetime.fromtimestamp(time.mktime(e.updated_parsed)).replace(tzinfo=datetime.timezone.utc)
                    except Exception as ex3:
                        output.write("CREATED ERROR:" + str(ex3))
                        p.created = timezone.now()

                p.source = source_feed
                p.save()

            if SAVE_JSON:
                p.json = e
                p.save(update_fields=["json"])

            try:
                p.title = e.title
                p.save(update_fields=["title"])
            except Exception as ex:
                output.write("Title error:" + str(ex))

            try:
                p.link = e.link
                p.save(update_fields=["link"])
            except Exception as ex:
                output.write("Link error:" + str(ex))

            try:
                p.image_url = e.image.href
                p.save(update_fields=["image_url"])
            except Exception:
                pass

            try:
                p.author = e.author
                p.save(update_fields=["author"])
            except Exception:
                p.author = ""

            try:
                p.body = body
                p.save(update_fields=["body"])
                # output.write(p.body)
            except Exception as ex:
                output.write(str(ex))
                output.write(p.body)

            try:
                seen_files = []

                post_files = e["enclosures"]
                non_dupes = []

                # find any files in media_content that aren't already declared as enclosures
                if "media_content" in e:
                    for ee in e["media_content"]:

                        # try and find a description for this.
                        # The way the feedparser works makes this difficult
                        # because it should be a child of ee but it isn't
                        # so while, I don't think this is right, it works most of the time
                        if len(e["media_content"]) == 1 and len(e.get("content", [])) == 1:
                            ee["description"] = e["content"][0].get("value")

                        found = False
                        for ff in post_files:
                            if ff["href"] == ee["url"]:
                                found = True
                                break
                        if not found:
                            non_dupes.append(ee)

                    post_files += non_dupes

                for ee in list(p.enclosures.all()):
                    # check existing enclosure is still there
                    found_enclosure = False
                    for pe in post_files:

                        href = "href"
                        if href not in pe:
                            href = "url"

                        length = "length"
                        if length not in pe:
                            length = "filesize"

                        if pe[href] == ee.href and ee.href not in seen_files:
                            found_enclosure = True

                            try:
                                ee.length = int(pe[length])
                            except Exception:
                                ee.length = 0

                            try:
                                type = pe["type"]
                            except Exception:
                                type = "unknown"

                            ee.type = type

                            if "medium" in pe:
                                ee.medium = pe["medium"]

                            if "description" in pe:
                                ee.description = pe["description"][:512]

                            ee.save()
                            break
                    if not found_enclosure:
                        if KEEP_OLD_ENCLOSURES:
                            ee.is_current = False
                            ee.save()
                        else:
                            ee.delete()
                    seen_files.append(ee.href)

                for pe in post_files:

                    href = "href"
                    if href not in pe:
                        href = "url"

                    length = "length"
                    if length not in pe:
                        length = "filesize"

                    try:
                        if pe[href] not in seen_files:

                            try:
                                length = int(pe[length])
                            except Exception:
                                length = 0

                            try:
                                type = pe["type"]
                            except Exception:
                                type = "audio/mpeg"

                            ee = Enclosure(post=p, href=pe[href], length=length, type=type)

                            if "medium" in pe:
                                ee.medium = pe["medium"]

                            if "description" in pe:
                                ee.description = pe["description"][:512]

                            ee.save()
                    except Exception:
                        pass
            except Exception as ex:
                if output:
                    output.write("No enclosures - " + str(ex))

        if SAVE_JSON:
            # Kill the entries
            f["entries"] = None
            source_feed.json = f
            source_feed.save(update_fields=["json"])

    if is_first and source_feed.posts.all().count() > 0:
        # If this is the first time we have parsed this
        # then see if it's paginated and go back through its history
        agent = get_agent(source_feed)
        headers = {"User-Agent": agent}  # identify ourselves
        keep_going = True
        while keep_going:
            keep_going = False  # assume were stopping unless we find a next link
            if hasattr(f.feed, 'links'):
                for link in f.feed.links:
                    if 'rel' in link and link['rel'] == "next":
                        ret = requests.get(link['href'], headers=headers, verify=VERIFY_HTTPS, allow_redirects=True, timeout=20)
                        (pok, pchanged) = parse_feed_xml(source_feed, ret.content, output)
                        # print(link['href'])
                        # print((pok, pchanged))
                        f = parser.parse(ret.content)  # rebase the loop on this feed version
                        keep_going = True

    return (ok, changed)


def parse_feed_json(source_feed, feed_content, output):

    ok = True
    changed = False

    try:
        f = json.loads(feed_content)
        entries = f['items']
        if len(entries):
            source_feed.last_success = timezone.now()  # in case we start auto unsubscribing long dead feeds
        else:
            source_feed.last_result = "Feed is empty"
            source_feed.interval += 120
            ok = False

        source_feed.save(update_fields=["last_success", "last_result"])

    except Exception:
        source_feed.last_result = "Feed Parse Error"
        entries = []
        source_feed.interval += 120
        ok = False

    if ok:

        if "expired" in f and f["expired"]:
            # This feed says it is done
            # TODO: permanently disable
            # for now source_feed.interval to max
            source_feed.interval = (24*3*60)
            source_feed.last_result = "This feed has expired"
            return (False, False, source_feed.interval)

        try:
            source_feed.site_url = f["home_page_url"]
            source_feed.name = f["title"]

            source_feed.save(update_fields=["site_url", "title"])

        except Exception:
            pass

        try:
            if "description" in f:
                _customize_sanitizer(parser)
                source_feed.description = parser.sanitizer._sanitize_html(f["description"], "utf-8", 'text/html')
                source_feed.save(update_fields=["description"])
        except Exception:
            pass

        try:
            _customize_sanitizer(parser)
            source_feed.name = parser.sanitizer._sanitize_html(source_feed.name, "utf-8", 'text/html')
            source_feed.save(update_fields=["name"])

        except Exception:
            pass

        try:
            if "icon" in f:
                source_feed.image_url = f["icon"]
                source_feed.save(update_fields=["icon"])
        except Exception:
            pass

        # output.write(entries)
        entries.reverse()  # Entries are typically in reverse chronological order - put them in right order
        for e in entries:
            body = " "
            if "content_text" in e:
                body = e["content_text"]
            if "content_html" in e:
                body = e["content_html"]  # prefer html over text

            body = fix_relative(body, source_feed.site_url)

            e_id = e.get("id", None)
            e_url = e.get("url", None)
            guid = make_guid(e_id, e_url, body)

            try:
                p = Post.objects.filter(source=source_feed).filter(guid=guid)[0]
                output.write("EXISTING " + guid + "\n")

            except Exception:
                output.write("NEW " + guid + "\n")
                p = Post(index=0, body=' ')
                p.found = timezone.now()
                changed = True
                p.source = source_feed

            try:
                title = e["title"]
            except Exception:
                title = ""

            # borrow the RSS parser's sanitizer
            _customize_sanitizer(parser)
            body = parser.sanitizer._sanitize_html(body, "utf-8", 'text/html')  # TODO: validate charset ??
            _customize_sanitizer(parser)
            title = parser.sanitizer._sanitize_html(title, "utf-8", 'text/html')  # TODO: validate charset ??
            # no other fields are ever marked as |safe in the templates

            if "banner_image" in e:
                p.image_url = e["banner_image"]

            if "image" in e:
                p.image_url = e["image"]

            try:
                p.link = e["url"]
            except Exception:
                p.link = ''

            p.title = title

            try:
                p.created = pyrfc3339.parse(e["date_published"])
            except Exception:
                output.write("CREATED ERROR")
                p.created = timezone.now()

            p.guid = guid
            try:
                p.author = e["author"]
            except Exception:
                p.author = ""

            if SAVE_JSON:
                p.json = e

            p.save()

            try:
                seen_files = []
                for ee in list(p.enclosures.all()):
                    # check existing enclosure is still there
                    found_enclosure = False
                    if "attachments" in e:
                        for pe in e["attachments"]:

                            if pe["url"] == ee.href and ee.href not in seen_files:
                                found_enclosure = True

                                try:
                                    ee.length = int(pe["size_in_bytes"])
                                except Exception:
                                    ee.length = 0

                                try:
                                    type = pe["mime_type"]
                                except Exception:
                                    type = "audio/mpeg"  # we are assuming podcasts here but that's probably not safe

                                ee.type = type
                                ee.save()
                                break
                    if not found_enclosure:
                        if KEEP_OLD_ENCLOSURES:
                            ee.is_current = False
                            ee.save()
                        else:
                            ee.delete()
                    seen_files.append(ee.href)

                if "attachments" in e:
                    for pe in e["attachments"]:

                        try:
                            if pe["url"] not in seen_files:

                                try:
                                    length = int(pe["size_in_bytes"])
                                except Exception:
                                    length = 0

                                try:
                                    type = pe["mime_type"]
                                except Exception:
                                    type = "audio/mpeg"

                                ee = Enclosure(post=p, href=pe["url"], length=length, type=type)
                                ee.save()
                        except Exception:
                            pass
            except Exception as ex:
                if output:
                    output.write("No enclosures - " + str(ex))

            try:
                p.body = body
                p.save()
                # output.write(p.body)
            except Exception as ex:
                output.write(str(ex))
                output.write(p.body)

        if SAVE_JSON:
            f['items'] = []
            source_feed.json = f
            source_feed.save(update_fields=["json"])

    return (ok, changed)


def test_feed(source, cache=False, output=LogOutput()):

    headers = {"User-Agent": get_agent(source)}  # identify ourselves and also stop our requests getting picked up by any cache

    if cache:
        if source.etag:
            headers["If-None-Match"] = str(source.etag)
        if source.last_modified:
            headers["If-Modified-Since"] = str(source.last_modified)
    else:
        headers["Cache-Control"] = "no-cache,max-age=0"
        headers["Pragma"] = "no-cache"

    output.write("\n" + str(headers))

    ret = requests.get(source.feed_url, headers=headers, allow_redirects=False, verify=VERIFY_HTTPS, timeout=20)

    output.write("\n\n")

    output.write(str(ret))

    output.write("\n\n")

    output.write(ret.text)


def get_subscription_list_for_user(user):

    subs_list = list(Subscription.objects.filter(Q(user=user) & Q(parent=None)).order_by("-is_river", "name"))

    return subs_list


def get_unread_subscription_list_for_user(user):

    to_read = list(Subscription.objects.filter(Q(user=user) & (Q(source=None) | Q(is_river=True) | Q(last_read__lt=F('source__max_index')))).order_by("-is_river", "name"))

    subs_list = []
    groups = {}

    for sub in to_read:
        if sub.source is None:
            # This is a group add it to the group list for later
            groups[sub.id] = sub
            sub._unread_count = 0
        if sub.parent_id is None:
            subs_list.append(sub)

    for sub in to_read:
        if sub.parent_id:
            # This is inside a group, all we do is add its count to the group it is in (assuming its not a group)
            if sub.parent_id in groups and sub.source_id is not None:
                grp = groups[sub.parent_id]
                grp._unread_count += sub.unread_count

    while len(groups.keys()) > 0:
        for key in list(groups.keys()):
            folder = groups[key]
            found = False
            for kk in list(groups.keys()):
                vv = groups[kk]
                if vv.parent_id == folder.id:
                    # then this folder has subfolders still inside the
                    # dictionary
                    found = True
                    break
            if not found:
                # This folder does not have any children
                if folder.parent_id is not None:
                    parent = groups[folder.parent_id]
                    parent._unread_count += folder._unread_count
                groups.pop(folder.id)

    return subs_list
