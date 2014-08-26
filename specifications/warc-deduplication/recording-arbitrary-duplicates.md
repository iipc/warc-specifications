---
title: Proposal for Standardizing the Recording of Arbitrary Duplicates in WARC Files
status: adopted
---
International Internet Preservation Consortium<br/>
Harvesting Working Group

* TOC
{:toc}

Introduction
============

Periodic harvesting of material on the web is quite likely to produce datasets with some level of duplication. Across time, a given resource is not necessarily modified during the interval between one visit and the next. A company logo is one such example of a resource to remain unmodified several visits to come. Across space, resources at different locations possibly hold identical payloads. A photo that gains popularity on the web is one such example of payload to be duplicated at different locations, such as in media outlets, blogs, and social networks.

It is important that web archives be able to record varied use of the same content without necessarily storing it repeatedly.

Background
==========

The issue of time-based duplicates[^1], i.e. where the same URI contains the same data at different points in time, has been addressed for some time now. This was reflected when the WARC File Format specification was written, namely in the ‘revisit’ record (see further in Appendix A).

Such duplicates are easier to handle than spatial duplicates[^2], as it is implicit that the URI of original and duplicate is the same. There is a need to resolve the time of the original’s capture, but that can typically be done by seeking out the latest, non-revisit, record of the URL with a date prior to the revisit record in question. This makes it fairly easy for playback tools (e.g. the Wayback Machine) to deal with collections with time-based deduplication.

During the 2012 IIPC General Assembly, in the Harvesting Working Group meeting, a report on the amount of duplication in Bibliotheca Alexandrina's web archive suggested the 1-PB collection could be reduced by about 14 percent given full deduplication. The Internet Archive and the French Institut National de l'Audiovisuel (INA) both suggested possibly even higher rates of reduction through deduplication. It is clear that the current, limited ability to handle spatial duplicates is a serious issue.

While the WARC File Format does recognize the need for deduplication by providing for the 'revisit' record type, which "describes the revisitation of content already archived...for when benefits of reduced storage size or improved cross-referencing of material are desired,"[^3] it does not adequately address “spatial” duplicates.

Where content is identical, the specification provides for the 'identical-payload-digest'[^4] profile for 'revisit' records. Using this profile, WARC-Payload-Digest is the "value of the digest that was calculated on the payload," and WARC-Refers-To is optionally the record ID of the original record.

Keeping in mind that most playback tools use an index whereby a URI+timestamp are used to look up specific records, it is clear that the current specification does not make it easy to do “spatial” deduplication, especially as the dataset increases in size. It would be necessary to have, in addition to the usual index, either an index of digests or of WARC record IDs. Neither is typically the case.

The Proposal
============

Based on discussion at the HWG meeting at the 2013 GA, the HWG recommends that the IIPC adopt the following recommendation for extending the WARC File Format.

For WARC ‘revisit’ records with WARC-Profile set to ‘identical-payload-digest’[^5], the following fields should be viewed as strongly recommended:

**WARC-Refers-To-Target-URI**  
This value should be equal to the WARC-Target-URI in the WARC record that the current record is considered a duplicate of.

**WARC-Refers-To-Date**  
This value should be equal to the WARC-Date in the WARC record that the current record is considered a duplicate of.

Additionally, the use of fields specifying the actual WARC file name and offsets where the record can be found should be discouraged as it is potentially very brittle.

Along with adopting this as a formal recommendation, the IIPC should plan to have this incorporated into the WARC File Format specification when it is next reviewed.

The IIPC should also encourage members who are engaged in developing tools that interact with WARC files to implement this recommendation.

Possible Issue
==============

Does the standard allow adding new fields not covered by the standard? It is specified in clause 5.5 of the standard that it is possible to add "future-types”. The standard is however entirely silent on adding new header fields.

* * * * *

Appendix A
==========

What follows is an excerpt from the ISO 28500 WARC File Format specification, namely section 6.7.2.

6.7.2 Profile: Identical Payload Digest
---------------------------------------

This 'revisit' profile may be used whenever a subsequent consideration of a URI provides payload content which a strong digest function, such as SHA-1, indicates is identical to a previously recorded version.

To indicate this profile, use the URI:

         http://netpreserve.org/warc/0.18/revisit/identical-payload-digest

To report the payload digest used for comparison, a 'revisit' record using this profile shall include a WARC-Payload-Digest field, with a value of the digest that was calculated on the payload.

A 'revisit' record using this profile may have no record block, in which case a Content-Length of zero must be written. If a record block is present, it shall be interpreted the same as a 'response' record type for the same URI, but truncated to avoid storing the duplicate content. A WARC-Truncated header with reason 'length' shall be used for any identical-digest truncation.

For records using this profile, the payload is defined as the original payload content whose digest value was unchanged.

Using a WARC-Refers-To header to identify a specific prior record from which the matching content can be retrieved is recommended, to minimize the risk of misinterpreting the 'revisit' record.

* * * * *

[^1]: Also often reffered to as “URL based” duplicates

[^2]: Also often referred to as “URL agnostic” duplicates

[^3]: WARC File Format specification, section 6.7

[^4]: See Appendix A

[^5]: Formally: http://netpreserve.org/warc/1.0/revisit/identical-payload-digest. See further in Appendix A.
