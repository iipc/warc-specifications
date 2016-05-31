---
title: CDXJ OpenWayback File Format
type: specification
status: draft
version: 1
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

Each file is a plain text file, UTF-8 encoded. It should end each line with Unix style newlines (`LF`).

A CDXJ file that has been sorted can be refered to as a CDXJ *index* as it is easily searchable.


## Header

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


# Field Specification


# Sorting / Index




