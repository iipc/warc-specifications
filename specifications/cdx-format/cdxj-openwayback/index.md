---
title: CDXJ OpenWayback File Format
type: specification
status: draft
version: 1.0
---

# 1. Preamble


This specification covers the CDXJ file format used by OpenWayback 3.0.0 (and later) to index web archive contents (notably in 
WARC and ARC files) and make them searchable via a resource resolution service.

The format builds on the CDX file format originally developed by the Internet Archive for the indexing behind the WaybackMachine. 
This specification build on it by simplifying the primary fields while adding a flexible JSON 'blob' to each resource, allowing 
high flexiblity in the inclusion of secondary data.

The use of a JSON in this manner is not novel. This specification is focused on enumarating the exact fields *outside* the JSON
and creating a list of the most common JSON fields for cross compatibility reasons.


# 2. File Specification

Each file is a plain text file, UTF-8 encoded. It should end each line with Unix style newlines (`LF`).

A CDXJ file that has been sorted can be refered to as a CDXJ *index* as it is easily searchable.


## 2.1 Header / Format Version

Each file should begin with a line declaring the file format and file format version. This line is preceeded with a bang symbol 
(`!`) so that it automatically sorts to the front of the file.

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


## 2.2 Resource Entries

Following the header lines, each additional line should represent exactly one resource in a web archive. Typically in a WARC or ARC file, although the exact storage of the resource is not defined by this specification.


# 3. Field Specification

Each line is composed of five fields as described in the next capter. 

The fields are seperated by spaces (U+0020). Consequently, spaces may not appear in the fields, except for the last field (JSON blob). 

Additionally, only the last (JSON) field may begin with an opening curly brace (`{`).

## 3.1 Searchable URI

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

Once in include the third stop of dropping the scheme. 


## 3.2 Timestamp


## 3.3 Content Digest


## 3.4 Record Type


## 3.5 JSON 


# 4 Sorting File / Index


# Appendices 

## A - Canonicalization

Canonicalization is applied to URIs to remove trivial differences in the URIs that do not reflect that the URI reference different resources. Examples include removing session ID parameters, unneccessary port declerations (e.g. :80 when crawling HTTP).

OpenWayback implements its own canonicalization process. Typically, it will be applied to the searchable URIs in CDXJ files. You can, however, use any canonicalization scheme you care for (including none). You must simple ensure that the same canonicalization process is applied to the URIs when performing searches. Otherwise they may not match correctly.


## B - Sort-friendly URI Reordering Transform (SURT)

SURT is a transformation applied to URIs which makes their left-to-right representation better match the natural hierarchy of domain names.

A URI <scheme://domain.tld/path?query> has SURT form <scheme://(tld,domain,)/path?query>.

Conversion to SURT form also involves making all characters lowercase, and changing the 'https' scheme to 'http'. Further, the '/' after a URI authority component -- for example, the third slash in a regular HTTP URI -- will only appear in the SURT form if it appeared in the plain URI form. (This convention proves important when using real URIs as a shorthand for SURT prefixes, as described below.)
