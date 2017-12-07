---
title: The WARC Format Errata
type: errata
status: proposed
version: 1.0
numbered: true
errata-for: warc-format
---

The following errors will be corrected at the next revision of the
standard.

URI and Record ID BNF Grammar
=============================

Section 4, grammar definition 2, line 32 currently reads:

    uri            = "<" <'URI' per RFC3986> ">"

It should read:

    record-id      = "<" uri ">"
    uri            = <'URI' per RFC3986>

- - -

The grammar definition in section 5.7 currently reads:

    WARC-Concurrent-To = "WARC-Concurrent-To" ":" uri

It should read:

    WARC-Concurrent-To = "WARC-Concurrent-To" ":" record-id

- - -

The grammar definition in section 5.11 currently reads:

    WARC-Refers-To = "WARC-Refers-To" ":" uri

It should read:

    WARC-Refers-To = "WARC-Refers-To" ":" record-id

- - -

The grammar defintion in section 5.14 currently reads:

    WARC-Warcinfo-ID = "WARC-Warcinfo-ID" ":" uri

It should read:

    WARC-Warcinfo-ID = "WARC-Warcinfo-ID" ":" record-id

- - -

The grammar definition in section 5.20 currently reads:

    WARC-Segment-Origin-ID = "WARC-Segment-Origin-ID" ":" uri

It should read:

    WARC-Segment-Origin-ID = "WARC-Segment-Origin-ID" ":" record-id
