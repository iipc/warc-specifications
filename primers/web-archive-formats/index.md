---
title: Introduction to web archive formats
type: primer
strand: warc-format
---

Archiving a URL
---------------

[hello-world.txt](./hello-world.txt)

What's in the WARC?
-------------------

[hello-world.warc](./hello-world.warc)

~~~
WARC-Type: warcinfo
WARC-Type: request
WARC-Type: response
WARC-Type: metadata
WARC-Type: resource
WARC-Type: resource
~~~

Finding individual records
--------------------------

    $ jwattools cdx hello-world.warc

or

    $ cdx-indexer hello-world.warc > hello-world.warc.cdx

which means we can pick out the response record like this:

    $ tail -c +1261 hello-world.warc | head -c 1085

~~~
WARC/1.0
WARC-Type: response
WARC-Record-ID: <urn:uuid:3C74F309-6B37-461C-B982-1B5C447C3C0E>
WARC-Warcinfo-ID: <urn:uuid:B8FDDD7C-DBB0-4EC4-BC7E-AA0B21749707>
WARC-Concurrent-To: <urn:uuid:8DCD2661-1B5A-445C-B4F4-2ACEB69A900B>
WARC-Target-URI: http://iipc.github.io/warc-specifications/primers/web-archive-formats/hello-world.txt
WARC-Date: 2015-07-08T21:55:13Z
WARC-IP-Address: 185.31.18.133
WARC-Block-Digest: sha1:3OMBZSE4IFAWD7XYWIYPAF575DHKSV4M
WARC-Payload-Digest: sha1:XMABAYFTCASBJ5QATNBILSXH6PSZEMG4
Content-Type: application/http;msgtype=response
Content-Length: 494

HTTP/1.1 200 OK
Server: GitHub.com
Content-Type: text/plain; charset=utf-8
Last-Modified: Wed, 08 Jul 2015 21:53:08 GMT
Access-Control-Allow-Origin: *
Expires: Wed, 08 Jul 2015 22:05:13 GMT
Cache-Control: max-age=600
Content-Length: 13
Accept-Ranges: bytes
Date: Wed, 08 Jul 2015 21:55:13 GMT
Via: 1.1 varnish
Age: 0
Connection: keep-alive
X-Served-By: cache-lcy1127-LCY
X-Cache: MISS
X-Cache-Hits: 0
X-Timer: S1436392513.648949,VS0,VE165
Vary: Accept-Encoding

Hello World

~~~

How playback works
------------------

CDX, sorted, search. Gets filename, offset.
grab WARC record
Modify as needed
Playback

Comparison with ARC files
-------------------------

...

Further Reading
---------------
For more information about the WARC format, see:

* [Web ARChive -- Wikipedia](http://en.wikipedia.org/wiki/Web_ARChive)
* [WARC -- File Formats Wiki](http://fileformats.archiveteam.org/wiki/WARC)
* [WARC, Web ARChive file format -- Sustainability of Digital Formats (Library of Congress)](http://www.digitalpreservation.gov/formats/fdd/fdd000236.shtml)


Appendix: Tools used
--------------------

This section outlines the tools and commands that were used to generate the example files.

### Making the WARC ###

To create a WARC, we used [wget](http://www.gnu.org/software/wget/):

    $ wget --warc-file hello-world http://iipc.github.io/warc-specifications/primers/web-archive-formats/hello-world.txt

...which created the compressed [hello-world.warc.gz](./hello-world.warc.gz) file. These special block-compressed files are often used directly, but in this primer, we uncompress it so we can see what's going on:

    $ gunzip hello-world.warc.gz

...leaving us with [hello-world.warc](./hello-world.warc).

### Making the CDX ###

To generate a content index (CDX) file, we have at least two options. There's [JWATTools](https://sbforge.org/display/JWAT/JWAT-Tools):

    $ jwattools cdx hello-world.warc

...(which created [cdx.unsorted.out](./cdx.unsorted.out)), or the ```cdx-indexer``` from [OpenWayback](https://github.com/iipc/openwayback):

    $ cdx-indexer hello-world.warc > hello-world.warc.cdx

...(which created [hello-world.warc.cdx](./hello-world.warc.cdx)).

### Extracting a WARC record ###

Once we've identified the offset and length of a particular record (in this case, an offset of 1260 bytes and a length of 1085 bytes), we can snip out an individual record like this:

    $ tail -c +1261 hello-world.warc | head -c 1085


### Making a Memento ###

To create an archived version of the page that could be played back properly, I used the Internet Archive's "Save" feature by going to this URL in my web browser: 

http://web.archive.org/save/http://iipc.github.io/warc-specifications/primers/web-archive-formats/hello-world.txt

...which created this snapshot:

http://web.archive.org/web/20150709104019/http://iipc.github.io/warc-specifications/primers/web-archive-formats/hello-world.txt

From here, we can use ```wget``` to look at what gets played back:

    $ wget --server-response http://web.archive.org/web/20150709104019/http://iipc.github.io/warc-specifications/primers/web-archive-formats/hello-world.txt

...giving:

~~~
  HTTP/1.0 200 OK
  Server: Tengine/2.1.0
  Date: Thu, 09 Jul 2015 10:41:38 GMT
  Content-Type: text/plain;charset=utf-8
  Content-Length: 13
  Set-Cookie: wayback_server=19; Domain=archive.org; Path=/; Expires=Sat, 08-Aug-15 10:41:38 GMT;
  Memento-Datetime: Thu, 09 Jul 2015 10:40:19 GMT
  Link: <http://iipc.github.io/warc-specifications/primers/web-archive-formats/hello-world.txt>; rel="original", <http://web.archive.org/web/timemap/link/http://iipc.github.io/warc-specifications/primers/web-archive-formats/hello-world.txt>; rel="timemap"; type="application/link-format", <http://web.archive.org/web/http://iipc.github.io/warc-specifications/primers/web-archive-formats/hello-world.txt>; rel="timegate", <http://web.archive.org/web/20150709104019/http://iipc.github.io/warc-specifications/primers/web-archive-formats/hello-world.txt>; rel="first last memento"; datetime="Thu, 09 Jul 2015 10:40:19 GMT"
  X-Archive-Orig-x-cache-hits: 0
  X-Archive-Orig-x-served-by: cache-sjc3122-SJC
  X-Archive-Orig-cache-control: max-age=600
  X-Archive-Orig-content-type: text/plain; charset=utf-8
  X-Archive-Orig-server: GitHub.com
  X-Archive-Orig-age: 0
  X-Archive-Orig-x-timer: S1436438419.302921,VS0,VE141
  X-Archive-Orig-access-control-allow-origin: *
  X-Archive-Orig-last-modified: Wed, 08 Jul 2015 22:33:03 GMT
  X-Archive-Orig-expires: Thu, 09 Jul 2015 10:50:19 GMT
  X-Archive-Orig-accept-ranges: bytes
  X-Archive-Orig-vary: Accept-Encoding
  X-Archive-Orig-connection: close
  X-Archive-Orig-date: Thu, 09 Jul 2015 10:40:19 GMT
  X-Archive-Orig-via: 1.1 varnish
  X-Archive-Orig-content-length: 13
  X-Archive-Orig-x-cache: MISS
  X-Archive-Wayback-Perf: {"IndexLoad":359,"IndexQueryTotal":359,"RobotsFetchTotal":1,"RobotsRedis":1,"RobotsTotal":1,"Total":371,"WArcResource":10}
  X-Archive-Playback: 1
  X-Page-Cache: MISS
~~~