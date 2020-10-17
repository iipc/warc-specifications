---
title: Zstandard Compression for WARC Files
status: proposed
version: 1.0
numbered: true
latest: true
version-of: warc-zstd
---

# Introduction *(informative)*

This specification defines a Zstandard-based format for compressed WARC files,
as an alternative to the GZIP-based format defined in [WARC/1.1 Annex D].

In general, Zstandard can produce significantly smaller files than GZIP while
also achieving faster compression and decompression. Zstandard also offers a
much wider range of compression levels, ranging from extremely fast compression
with a modest size reduction to extremely slow compression with a much better
reduction. For files containing many small records, Zstandard dictionaries can
be used reduce file size even further, while still permitting random access to
individual records.

## Words of caution

This specification is __experimental__ and __subject to change__.
Furthermore, the Zstandard format itself is __much less mature__ than GZIP. The
GZIP RFC was published in 1996; the Zstandard RFC was published in 2018\.
Before using Zstandard compression for archival, organizations should carefully
consider the risks of relying on such a young format.

# Normative references

\[RFC 8478\] Collet, Y. and Kucherawy, M. Zstandard Compression and the
application/zstd Media Type. October 2018. Available at:
<https://tools.ietf.org/html/rfc8478>

[RFC 8478]: https://tools.ietf.org/html/rfc8478
[RFC 8478 section 3.1.1]: https://tools.ietf.org/html/rfc8478#section-3.1.1
[RFC 8478 section 3.1.1.1.2]: https://tools.ietf.org/html/rfc8478#section-3.1.1.1.2
[RFC 8478 section 3.1.2]: https://tools.ietf.org/html/rfc8478#section-3.1.2
[RFC 8478 section 5]: https://tools.ietf.org/html/rfc8478#section-5
[RFC 8478 section 7]: https://tools.ietf.org/html/rfc8478#section-7

\[WARC/1.0\] <https://iipc.github.io/warc-specifications/specifications/warc-format/warc-1.0/>

\[WARC/1.1\] <https://iipc.github.io/warc-specifications/specifications/warc-format/warc-1.1/>

[WARC/1.1 Annex D]: https://iipc.github.io/warc-specifications/specifications/warc-format/warc-1.1/#annex-d-informative-compression-recommendations

# File identification

A Zstandard-compressed WARC file should have the customary ".zst" appended to
its name, making the complete suffix ".warc.zst".

Because a Zstandard-compressed WARC file must begin with either a Zstandard
frame or a dictionary frame, the first four bytes of the file will be either
`0x28 0xB5 0x2F 0xFD` or `0x5D 0x2A 0x4D 0x18`, respectively.

# File format

    warc-zst-file   = zstandard-frame *( zstandard-frame | extension-frame )
                        | dict-frame 1*( zstandard-frame | extension-frame )
    dict-frame      = <a skippable frame with a Magic_Number of 0x184D2A5D>
    zstandard-frame = <a Zstandard frame>
    extension-frame = <a skippable frame with a Magic_Number other than 0x184D2A5D>

A Zstandard-compressed WARC file consists of an optional dictionary frame
followed by one or more Zstandard frames, possibly with extension frames in
between. The file must begin with either a Zstandard frame or a dictionary
frame. If each Zstandard frame is decompressed and the results are concatenated
in order, the result will be a valid, uncompressed WARC file.

Each WARC record must correspond to one or more Zstandard frames in the
compressed file. If those frames are decompressed and the results are
concatenated in order, the result will be the original, uncompressed WARC
record. A single Zstandard frame __must not__ contain data from multiple WARC
records.

Like uncompressed WARC files, Zstandard-compressed WARC files must contain at
least one record.

## Dictionaries

If a Zstandard-compressed WARC file does not contain a dictionary frame, each
Zstandard frame in the file must be decompressed without a dictionary.

If a Zstandard-compressed WARC file does contain a dictionary frame, it must
follow the dictionary frame format described below. Each Zstandard frame in the
file must be decompressed using the decoded dictionary.

Encoders may use an arbitrary dictionary that follows the Zstandard dictionary
format. They should attempt to give a unique ID to each dictionary. For
example, they may use a random dictionary ID between 32,768 and 2,147,483,647.

## Extension frames

An extension frame is a skippable frame, as defined in [RFC 8478 section
3.1.2], with a Magic\_Number other than `0x184D2A5D`. An arbitrary sequence of
extension frames may appear before or after any Zstandard frame, except that
the file may not begin with an extension frame.

This specification does not define the format or meaning of any extension
frame. This specification also does not define which WARC record an extension
frame should be associated with, if any. Decoders must ignore any extension
frames they do not recognize.

# Zstandard frames

Each Zstandard frame in a compressed WARC file must include the
Frame\_Content\_Size and Content\_Checksum fields, which are described in [RFC
8478 section 3.1.1].
If the file includes a dictionary, each Zstandard frame must also include the
Dictionary\_ID field, and its contents must match the Dictionary\_ID field in
the dictionary itself.

Whenever a decoder decompresses a frame in its entirety, it should check the
checksum of the decompressed data against the Content\_Checksum field to
determine whether data corruption has occurred.

Empty Zstandard frames are permissible, and will have a Frame\_Content\_Size of
zero.

Zstandard frames must use the standard format defined in [RFC 8478]; they
must not use any of the legacy Zstandard formats not described there.

# Dictionary frame format

A dictionary frame is a skippable frame, as defined in [RFC 8478 section
3.1.2], with a Magic\_Number of `0x184D2A5D`. The User\_Data field contains a
single dictionary which may optionally be compressed.

If the dictionary is not compressed, the User\_Data field will consist of a
single dictionary in the format given by [RFC 8478 section 5]. It will start
with the bytes `0x37 0xA4 0x30 0xEC`.

If the dictionary is compressed, the User\_Data field must consist of a single
Zstandard frame, starting with the bytes `0x28 0xB5 0x2F 0xFD`; skippable
frames are not allowed. The Zstandard frame must be compressed without a
dictionary, and the Frame\_Content\_Size and Content\_Checksum fields must be
present. When the frame is decompressed, the result must be a single dictionary
in the format given by [RFC 8478 section 5].

# Window and dictionary limits

Each Zstandard frame has a value called Window\_Size, described in [RFC 8478
section 3.1.1.1.2], which determines how much memory is needed to decode the
frame. Although the Zstandard format supports window sizes up to 16 exabytes,
sizes this large may be impractical for certain decoders. Memory requirements
are also affected by the size of the dictionary, if any. This specification
only requires decoders to support the following sizes:

- Window sizes up to 8,388,608 bytes (2<sup>23</sup> bytes) in all Zstandard
  frames, including Zstandard frames within dictionary frames.
- Compressed dictionary sizes up to 8,388,608 bytes (2<sup>23</sup> bytes).
  This refers to the size of the User\_Data field in the dictionary frame.
- Decompressed dictionary sizes up to 8,388,608 bytes (2<sup>23</sup> bytes).
  This refers to the size of the User\_Data field in the dictionary frame (when
  the dictionary is not compressed) or the result of decompressing the
  User\_Data field (when the dictionary is compressed).

Encoders are permitted to generate files that exceed these limits, but decoders
may choose to reject such files with a suitable error message.

# Security considerations

The security considerations for this format are a combination of those for WARC
and those for Zstandard. Users should consult [RFC 8478 section 7] for a
discussion of the latter.

When implementations support seeking to a record at an arbitrary position in
the file, they should also beware of positions provided by malicious sources,
which may point to falsified or invalid data.

# Implementation notes *(informative)*

The initial discussion of this format can be found at [warc-specifications #53].
The dictionary frame format has been submitted to upstream zstd, along with
example code, at [zstd #2349], but that specification is not authoritative for
WARC files; the specification above must be used instead.

[warc-specifications #53]: https://github.com/iipc/warc-specifications/issues/53
[zstd #2349]: https://github.com/facebook/zstd/pull/2349

## Compression trade-offs

In general, the best compression results are achieved by using a single frame
for each record. However, there are other advantages to using multiple frames.
If a record uses multiple frames, they can potentially be compressed and
decompressed in parallel. Multiple frames may also be helpful when dealing with
huge records, too large to fit in memory.

Dictionaries are extremely helpful for tiny frames, but not very helpful for
huge frames. With a typical window size of 8MB, a dictionary will only help
with the first 8MB of uncompressed data in a frame.

Dictionaries will be most effective when they are tailored for the content of a
particular WARC file. For example, when crawling a specific website, a
dictionary can be generated from the first crawled set of records. The
dictionary can then be used for the rest of the WARC files produced by the
crawl.

Especially large window sizes may improve compression of especially large
frames, but they carry the risk that a decoder will reject the frame if the
window size is too large.

## Random access

As with GZIP, external indexes of Zstandard-compressed WARC file content may be
used to save each record's starting position in the file. An arbitrary record
can then be decoded by loading the dictionary (if any) from the start of the
file, then seeking to the known starting position and decoding Zstandard frames
until the record is complete.

## Encoding with libzstd

The simplest way to create a Zstandard-compressed WARC file is to call
`ZSTD_compress` separately on each record and concatenate the results. If
encoders use other functions from libzstd, they must take care to include the
Frame\_Content\_Size field in every frame, and to start a new frame for each
new record.

## Decoding with libzstd

Most of the functions in libzstd already ignore skippable frames and
concatenate decompressed Zstandard frames, so the only extra effort needed is
to load the dictionary.

The following code decompresses an entire WARC file. For simplicity, this code
assumes the entire compressed file has been loaded into memory, and some
error-handling code has been omitted.

```c
uint32_t readLE32(const uint8_t* src) {
    return (uint32_t)src[0]
         | (uint32_t)src[1] << 8
         | (uint32_t)src[2] << 16
         | (uint32_t)src[3] << 24;
}

size_t warc_zstd_decompress_file(uint8_t* dst, size_t dstCapacity,
                           const uint8_t* src, size_t srcSize) {
    ZSTD_DCtx* dctx = ZSTD_createDCtx();
    if (srcSize >= 8 && readLE32(src) == 0x184D2A5D) {
        // Dictionary frame.
        uint32_t dictSize = readLE32(src + 4);
        const uint8_t *dictData = src + 8;
        if (dictSize < 4 || dictSize + 8 > srcSize) {
            abort();
        }
        if (readLE32(dictData) == ZSTD_MAGIC_DICTIONARY) {
            // Uncompressed dictionary.
            ZSTD_DCtx_loadDictionary(dctx, dictData, dictSize);
        } else if (readLE32(dictData) == ZSTD_MAGICNUMBER) {
            // Compressed dictionary.
            unsigned long long bufferSize;
            bufferSize = ZSTD_getFrameContentSize(dictData, dictSize);
            uint8_t* buffer = malloc(bufferSize);
            size_t result = ZSTD_decompress(buffer, bufferSize, dictData, dictSize);
            ZSTD_DCtx_loadDictionary(dctx, buffer, result);
            free(buffer);
        } else {
            abort();
        }
    }
    size_t result = ZSTD_decompressDCtx(dctx, dst, dstCapacity, src, srcSize);
    ZSTD_freeDCtx(dctx);
    return result;
}
```

## Combining files

Two Zstandard-compressed WARC files without dictionaries can be concatenated to
form a valid file. However, if either file contains a dictionary, the files
__cannot__ be concatenated in this way.

Two files that use identical dictionaries can be combined by removing the
dictionary frame from the second file, then concatenating them.

In other cases, files can only be combined by decompressing and recompressing
them to use the same dictionary.

## Multiple dictionaries

It may be desirable to use different dictionaries for different types of
content. For example, one dictionary for records containing HTML, and another
for records containing PNG images. This can be accomplished by creating
separate WARC files for each dictionary.

## Extension frames

Extension frames could be used to add padding, or to prefix each record with
its compressed size so records can easily be skipped. They could also be used
to add a seek table for random access within a single record, perhaps using a
variant of the [Zstandard Seekable Format].

Extension frames are prohibited at the beginning of the file in order to
simplify the process of checking whether a file is Zstandard-compressed. If
necessary, a zero-length Zstandard frame can be used at the beginning of the
file, followed by an extension frame.

[Zstandard Seekable Format]: https://github.com/facebook/zstd/blob/dev/contrib/seekable_format/zstd_seekable_compression_format.md
