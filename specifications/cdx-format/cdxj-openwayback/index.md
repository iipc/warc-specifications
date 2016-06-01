---
title: CDXJ OpenWayback File Format
type: specification
status: proposed
version: 1.0
---

# Preamble


This specification covers the CDXJ file format used by OpenWayback 3.0.0 (and later) to index web archive contents (notably in 
WARC and ARC files) and make them searchable via a resource resolution service.

The format builds on the CDX file format originally developed by the Internet Archive for the indexing behind the WaybackMachine. 
This specification build on it by simplifying the primary fields while adding a flexible JSON 'blob' to each resource, allowing 
high flexiblity in the inclusion of secondary data.

The use of a JSON in this manner is not novel. This specification is focused on enumarating the exact fields *outside* the JSON
and creating a list of the most common JSON fields for cross compatibility reasons.


# File Specification

Each file is a plain text file, UTF-8 encoded. It should end each line with Unix style newlines (U+000A).

A CDXJ file that has been sorted can be refered to as a CDXJ *index* as it is easily searchable.


## Header / Format Version

Each file should begin with a line declaring the file format and file format version. This line is preceeded with a bang symbol 
(`!` - U+0021) so that it automatically sorts to the front of the file.

Example:
```
!OpenWayback-CDXJ 1.0
```

This line may be repeated any number of times, as long as they are all sequential, starting from the first line of the file. 
The is to accomodate the merging of multiple CDXJ files that may be generated at different times.

It is permissible to mix minor version numbers (e.g. `1.0` and `1.1`) as minor versions are required to be backwards compatible.
In this scenario, parsing software should treat the entire file based on the highest observed version number.

It is not permissible to mix major version numbers (e.g. `1.0` and `2.0`) in the same file. It is understood that a bump in
the major version number indicates a change that is not backwards compatible. It is not possible to merge CDXJ files with 
different major version numbers.


## Resource Entries

Following the header lines, each additional line should represent exactly one resource in a web archive. Typically in a WARC or ARC file, although the exact storage of the resource is not defined by this specification.


# Field Specification

Each line is composed of five fields as described in the next capter. 

The fields are seperated by spaces (U+0020). Consequently, spaces may not appear in the fields, except for the last field (JSON blob). 

Additionally, only the last (JSON) field may begin with an opening curly brace (`{` - U+007B).

## Searchable URI

The first field is a searchable version of the URI that this resource refers to.

By *searchable*, we mean that the following transformations have been applied to it:

1. Canonicalization - See Appendix A
2. Sort-friendly URI Reordering Transform (SURT) - See Appendix B
3. The scheme is dropped from the SURT format

**Note:** While this is extremly simmilar to other CDX and CDXJ implementations, we note that a lot of them get the SURT format wrong. 
Most notably by omitting the starting parenthesis or dropping the trailing comma in the domain name.

E.g. in using OpenWayback 2's CDX server the URL `http://example.com/' would translate to:

```
com,example)/
```

The correct SURT transformation is:

```
(com,example,)/
```

Once you include the third step of dropping the scheme. 

The first field may not begin with a bang character (`!` - U+0021). As these are not allowed in URIs, this is unlikely to cause any issues.


## Timestamp

The second field is a timestamp. It should correspond to the WARC-Date timestamp as of WARC 1.1.

> A UTC timestamp as described in the W3C profile of ISO8601 [W3CDTF].
> The timestamp shall represent the instant that data capture for record
> creation began. Multiple records written as part of a single capture
> event (see section 5.7) shall use the same WARC-Date, even though the
> times of their writing will not be exactly synchronized. 
> 
> WARC-Date may be specified at any of the six levels of granularity
> described in [W3CDTF]. If WARC-Date includes a decimal fraction of a
> second, the decimal fraction of a second shall have a minimum of 1
> digit and a maximum of 9 digits. WARC-Date should be specified with as
> much precision as is accurately known. This document recommends no
> particular algorithm for access software to choose a record by date
> when an exact match is not available.

This is a notable departure from the original CDX format, that used a somewhat truncated timestamp (YYYYMMDDhhmmss). The level of accuracy
of the timestamp should match the accuracy that is available in the WARC (or other source material).

**Note:** All timestamps should be in UTC.


## Content Digest

The third field should contain a Base32 encoded SHA-1 digest of the contents of the URI or a simple dash (`-` - U+002D) if the URI refers 
to a record without a content block. The algorithm prefix (e.g. `sha1:`) often used where multiple hashing algorithms may be used, is
omitted in this case.

In the case of revisit records and continuation records (or others that rely on a second record to fully replay the content), this should
be the digest of the original/full content. Additional digests may be included in the JSON blob.

The choice of SHA-1 hashing algorithm is based on its extremly widespread usage in web archiving. As it is not practical to have a CDXJ 
with a mixture of digest from different algorithms here, we chose the most commonly used algorithm. Additional digests from other 
algorithms may be included in the JSON blob.


## Record Type

Indicates what type of record the current line refers to. This field is fully compatible with WARC 1.0 (ISO 28500) definition of 
WARC-Type (chapter 5.5 and chapter 6). 

For content not stored in WARCs, a reasonable equivalent should be chosen.

E.g. 

* **response** - Suitable for any record that contains the response from a server to a specific request (irrespective of protocol).
* **request** - Suitable for any record containing a request made to a server.
* **revisit** - Suitable for any record of a response from a server to a specific request, where the content body is equal to that of another record.


## JSON 


# Sorting File / Index


# Appendices 

## A - Canonicalization

Canonicalization is applied to URIs to remove trivial differences in the URIs that do not reflect that the URI reference different resources. Examples include removing session ID parameters, unneccessary port declerations (e.g. :80 when crawling HTTP).

OpenWayback implements its own canonicalization process. Typically, it will be applied to the searchable URIs in CDXJ files. You can, however, use any canonicalization scheme you care for (including none). You must simple ensure that the same canonicalization process is applied to the URIs when performing searches. Otherwise they may not match correctly.


## B - Sort-friendly URI Reordering Transform (SURT)

SURT is a transformation applied to URIs which makes their left-to-right representation better match the natural hierarchy of domain names.

A URI <scheme://domain.tld/path?query> has SURT form <scheme://(tld,domain,)/path?query>.

Conversion to SURT form also involves making all characters lowercase, and changing the 'https' scheme to 'http'. Further, the '/' after a URI authority component -- for example, the third slash in a regular HTTP URI -- will only appear in the SURT form if it appeared in the plain URI form. (This convention proves important when using real URIs as a shorthand for SURT prefixes, as described below.)
