---
title: WARC-Cipher-Suite
warc_extension_type: field
summary: TLS cipher suite used when retrieving included content
status: adopted
license: CC0 1.0
---

The WARC-Cipher-Suite field contains the TLS cipher suite negotiated when retrieving the included content.
The value shall be the name of a cipher suite from the 'Description' column of the [IANA TLS Cipher Suites registry](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml#tls-parameters-4).

    WARC-Cipher-Suite = "WARC-Cipher-Suite" ":" cipher-suite
    cipher-suite      = <TLS cipher suite name per IANA registry>

> **Example**
>
>     WARC-Cipher-Suite: TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

The WARC-Cipher-Suite field may be used on 'metadata', 'response', 'resource', 'request', and 'revisit' records, but 
shall not be used on 'continuation', 'conversion' or 'warcinfo' records.