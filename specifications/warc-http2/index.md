---
title: WARC Extensions for HTTP/2
status: proposed
latest: true
version-of: warc-http2
version: 0.1
---

[HTTP/2] defines a new binary protocol which is semantically highly compatible
with HTTP/1 but adds new transport features such as header compression, request
multiplexing and server push.

[HTTP/2]: https://tools.ietf.org/html/rfc7540

Backwards compatiblity dictates that HTTP/2 servers be able to serve the same
content over HTTP/1 so current practice when crawling is to make all requests
over HTTP/1. However browser-based archiving tools may not have control over
protocol negotiation and therefore may have no choice but to deal with content
that was delivered via HTTP/2. It may also be desirable for crawlers to be able
to make use of HTTP/2 for performance reasons.

As HTTP/2 allows connection multiplexing and is typically encrypted with TLS
we cannot simply store the bytes received from the TCP stream as we do with
HTTP/1. Tools that are browser-based or use a HTTP/2 code library may have 
ready access to decoded headers but not to the raw protocol bytes. Finally, 
storing only the binary H2 protocol would pose a compatiblity problem for
WARC reading tools that only understand HTTP/1.1 and increase the complexity
of reading WARC files.

Therefore this document proposes a mechanism for storing HTTP/2 requests and
responses in their semantically equivalent HTTP/1.1 form and defines an
extension WARC header field recording the original protocol version.

Future versions of these extensions may specify how extra HTTP/2-specific
information may be optionally encoded in extension fields or metadata records.
This version however does not. Anyone with a use case for storing
HTTP/2-specific information is encouraged to join the discussion or even submit
a proposal via the [warc-specifications Github project].

[warc-specifications Github project]: https://github.com/iipc/warc-specifications

# WARC-Original-Protocol field definition

The WARC-Original-Protocol field denotes that the protocol messages in the
record block was originally encoded using a different protocol.

    WARC-Original-Protocol = "WARC-Original-Protocol" ":" protocol-id
    protocol-id = "h2"   ; HTTP/2 over TLS
                | "h2c"  ; HTTP/2 over cleartext TCP

The WARC-Original-Protocol field should not be used when the record block
contains the original protocol and the protocol can be determined from the
value of the WARC record's Content-Type field.

The WARC-Original-Protocol field may be used in 'request', 'response',
'resource' and 'metadata' records and shall not be used in 'warcinfo',
'conversion' and 'continuation' records.

# Encoding HTTP/2 messages as HTTP/1.1

When the decoded header information for HTTP/2 requests and responses is
available they should be formatted WARC 'request' and 'response' records
with the header encoded as HTTP/1.1. When header information is unavailable a
'resource' record should instead be used.

In all three record types the fact the exchange originally occurred via HTTP/2
should be recorded by including a WARC-Original-Protocol field with the values
"h2" for HTTP/2 over TLS or "h2c" for HTTP/2 of cleartext TCP.

Example request record:

    WARC/1.1
    WARC-Record-ID: <urn:uuid:a6aadb41-1b2f-46e0-9e94-74339cbc9875>
    WARC-Type: request
    WARC-Date: 2018-07-12T16:44:13.123Z
    WARC-Target-URI: https://example.org/
    WARC-Original-Protocol: h2
    Conent-Length: 75
    Content-Type: application/http;msgtype=request

    GET / HTTP/1.1
    host: example.org
    user-agent: example/1.0
    accept: */*

Example response record:

    WARC/1.1
    WARC-Record-ID: <urn:uuid:5269bd38-547a-4f77-a285-8d30ec6e0b54>
    WARC-Type: response
    WARC-Date: 2018-07-12T16:44:13.123Z
    WARC-Target-URI: https://example.org/
    WARC-Original-Protocol: h2
    WARC-IP-Address: 192.0.2.1
    Conent-Length: 12131
    Content-Type: application/http;msgtype=response

    HTTP/1.1 200 
    server: Apache
    content-type: text/html;charset=UTF-8
    cache-control: max-age=43200
    expires: Thu, 12 Jul 2018 16:44:26 GMT
    date: Thu, 12 Jul 2018 04:44:26 GMT
    content-length: 11930

    [text/html payload follows]

Example resource record:

    WARC/1.1
    WARC-Record-ID: <urn:uuid:5269bd38-547a-4f77-a285-8d30ec6e0b54>
    WARC-Type: resource
    WARC-Date: 2018-07-12T16:44:13.123Z
    WARC-Target-URI: https://example.org/
    WARC-Original-Protocol: h2
    Content-Length: 12131
    Content-Type: text/html;charset=UTF-8
    
    [text/html payload follows]

## Handling of reason phrases in HTTP responses
 
HTTP/2 does not define a way to carry the HTTP/1 reason phrase in response
messages. The reason-phrase field is mandatory in HTTP/1.1 responses but may
be an empty string. Therefore the status line must be written with a trailing
space:

    "HTTP/1.1" SP status-code SP CRLF

## Non-standard HTTP/2 textual representations

Some tools (notably curl) for debugging purposes display a non-standard textual
representation of HTTP/2 formatted similar to HTTP/1 but with a version number
of "HTTP/2":

    GET / HTTP/2
    Host: example.org
    User-Agent: curl/7.59.0
    Accept: */*

This is not a valid HTTP message and for interoperability programs writing
WARC files must not write records like this. Programs translating WARC/2
messages to HTTP/1.1 should write messages which obey grammar defined in
[RFC 7230]. The original protocol version should instead be indicated using the
WARC-Original-Protocol field defined above. 

[RFC 7230]: https://tools.ietf.org/html/rfc7230
