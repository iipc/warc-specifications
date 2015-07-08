---
title: Introduction to web archive formats
type: primer
strand: warc-format
---

[hello-world.txt](./hello-world.txt)

    wget --warc-file hello-world http://iipc.github.io/warc-specifications/primers/web-archive-formats/hello-world.txt

    gunzip hello-world.warc.gz

[hello-world.warc](./hello-world.warc)

    jwattools cdx hello-world.warc

    tail -c +1261 hello-world.warc | head -c 1120

```    
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



WARC/1.0
WARC-Type: metadata
...
```


WARC-Type: warcinfo
WARC-Type: request
WARC-Type: response
WARC-Type: metadata
WARC-Type: resource
WARC-Type: resource


For introductory information about the WARC format, see:

* [Web ARChive -- Wikipedia](http://en.wikipedia.org/wiki/Web_ARChive)
* [WARC -- File Formats Wiki](http://fileformats.archiveteam.org/wiki/WARC)
* [WARC, Web ARChive file format -- Sustainability of Digital Formats (Library of Congress)](http://www.digitalpreservation.gov/formats/fdd/fdd000236.shtml)

**TODO:** include copies of earlier versions?

