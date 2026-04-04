---
title: WARC-Protocol
warc_extension_type: field
summary: network protocol(s) used when retrieving the included content
status: adopted
license: CC0 1.0
---

The WARC-Protocol field records the network protocol(s) used when retrieving the included content.

    WARC-Protocol = "WARC-Protocol" ":" protocol-id
    protocol-id = "dns"      ; DNS [RFC 1035]
                | "ftp"      ; FTP [RFC 959]
                | "gemini"   ; Gemini
                | "gopher"   ; Gopher [RFC 1436]
                | "http/0.9" ; HTTP/0.9
                | "http/1.0" ; HTTP/1.0 [RFC 1945]
                | "http/1.1" ; HTTP/1.1 [RFC 7230]
                | "h2"       ; HTTP/2 over TLS [RFC 7540]
                | "h2c"      ; HTTP/2 over cleartext TCP [RFC 7540]
                | "h3"       ; HTTP/3 [RFC 9114]
                | "quic/1"   ; QUIC version 1 [RFC 9000]
                | "quic/2"   ; QUIC version 2 [RFC 9369]
                | "spdy/1"   ; SPDY/1
                | "spdy/2"   ; SPDY/2
                | "spdy/3"   ; SPDY/3
                | "ssl/2"    ; SSLv2 aka SSL 0.2
                | "ssl/3"    ; SSLv3 aka SSL 3.0 [RFC 6101]
                | "tls/1.0"  ; TLS 1.0 [RFC 2246]
                | "tls/1.1"  ; TLS 1.1 [RFC 4336]
                | "tls/1.2"  ; TLS 1.2 [RFC 5246]
                | "tls/1.3"  ; TLS 1.3

The WARC-Protocol field may be repeated to indicate protocol layering. When multiple fields are written for layering, 
WARC writers should order them from higher-level to lower-level.

> **Example:**
> HTTP/1.1 layered over TLS 1.0 may be recorded as:
> 
>     WARC-Protocol: http/1.1
>     WARC-Protocol: tls/1.0

The field may be omitted when the protocol is unknown or can be determined unambiguously from the `WARC-Target-URI`, 
the `Content-Type`, and the record block per the rules in the section below

The WARC-Protocol field does not indicate the format of the record block and
is not a replacement for the Content-Type field.

> **Example:**
> A binary HTTP/2 message recorded using `application/http` text syntax:  
>
>     WARC-Type: response
>     WARC-Protocol: h2
>     Content-Type: application/http;msgtype=response
>     ...
>     
>     HTTP/1.1 200 OK
>     Content-Type: text/html
>     ... 

The WARC-Protocol field may be used in 'request', 'response', 'resource', 'metadata' and 'revisit' records, but shall 
not be used in 'warcinfo', 'conversion' or 'continuation' records.

## Determining the protocol in the absence of WARC-Protocol

| URI Scheme | Content-Type         | Header version | Protocol                      |
|------------|----------------------|----------------|-------------------------------|
| dns        | text/dns             |                | dns ; transport unknown       |
| ftp        |                      |                | ftp ; over cleartext TCP      |
| gemini     | application/gemini † |                | [gemini](https://gemini.circumlunar.space/docs/specification.html) ; over TLS #85          |
| gopher     | application/gopher † |                | gopher ; over cleartext TCP   |
| http       | application/http     | absent         | http/0.9 ; over cleartext TCP |
| http       | application/http     | "HTTP/1.0"     | http/1.0 ; over cleartext TCP |
| http       | application/http     | "HTTP/1.1"     | http/1.1 ; over cleartext TCP |
| https      | application/http     | "HTTP/1.0"     | http/1.0 ; over TLS           |
| https      | application/http     | "HTTP/1.1"     | http/1.1 ; over TLS           |

† Not a [registered media type](https://www.iana.org/assignments/media-types/media-types.xhtml) but has been used in the wild.

When the WARC-Protocol field is present it takes precedence over the rules in the table above.