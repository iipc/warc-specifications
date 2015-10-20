---
title: Minutes of the WARC revision workshop
redirect_from: "specifications/warc-format/meetings/2015-05-01-IIPC-GA-WARC-Meeting-Minutes.html"
---

During the General Assembly of the IIPC in Stanford, a workshop has been
held on the revision process.

The goals of this workshop were to:

-          present the current status of the WARC standard;
-          present the revision process;
-          identify, discuss and prioritize revision needs;
-          set up an organization and agenda for further work.

Please look powerpoint presented during the workshop for information on
the WARC standard and its revision process; on the IIPC
website: <http://netpreserve.org/sites/default/files/attachments/2015_IIPC-GA_Slides_17b_Oury.pptx>.

# Discussions & Decisions #

We propose here a short summary of the discussion and decisions that
have been taken during the workshop:

---

**1) Modification: the next version of the WARC standard should
be minor, thus named WARC 1.1**

---

**[2) Clarification: scope of the standard ](https://github.com/iipc/warc-specifications/issues/8)**

**Issue:** the introduction and the scope of the standard mostly
acknowledges use cases related to web archiving. However, some
institutions are using WARC format to store other kinds of digital
content.

**Decision:** the introduction and the scope should state more precisely
that WARC originated from web archiving community but should also
acknowledge its use in other communities.

**Action: **Clément Oury to propose a formulation.

---

**3) Clarification: validity of a WARC file / a WARC record with unknown field (s).**

**Issue:** In 6.1 “WARC record types/General”, it is written “Because
new record types that extend the WARC format may be defined in future
standards, WARC processing software shall skip records of unknown
type”.

However, it is not explained if a known record type with new named
fields should be valid; and should be processed by WARC reading or
validating tools.

**Decision:** it should be stated that it is allowed to add new named
fields, as well as new records types. However, it is strongly
recommended to discuss the utility and the relevance of these new named
fields within the right forum (e.g. the IIPC for web archiving) and to
inform the maintenance body of the standard (currently the ISSN
International Centre). 

New named field that are considered relevant and mature by a large
community of WARC users should be added in the next revision of the WARC
standard.

Besides, the sentence “Because new record types that extend the WARC
format may be defined in future standards…” should be replaced by
“Because new record types that extend the WARC format may be defined
in **future versions of the standard**…”.

**Action:** Clément Oury to propose a formulation.

---

**4) Augmentation: add new named fields for deduplication**

**Issue:** the issue has been identified and describe by the IIPC
harvesting working, which has proposed a
solution: *<http://iipc.github.io/warc-specifications/specifications/warc-deduplication/recording-arbitrary-duplicates-1.0/>*

**Decision:** the preconisation from the HWG should be written in the
standard.

**Action:** Kristinn Sigurðsson (??) to include the preconisation in the
standard.

---

**5) Augmentation: propose a specific profile for the management of
diffs in the revisit records.**

**Issue:** revisit records may be used to store the diffs of a
deduplication process. A new profile should be proposed that takes this
case into account.

**Decision:** a paragraph should be written that describes this new
profile, as chapter 6.7.4. of the standard.

Besides, in the sentence (p. 4): “All 'warcinfo', 'metadata' and
'revisit' records shall not have a payload”, the revisit records should
not be listed (NB from Clément: not sure about that: is the diff a
“payload” or a “block” of the record? If the HTTP protocole response is
included, the diff should be considered a payload).

**Action:** Andy Jackson from BL, Eld Zierau from KB and Kristinn
Sigurðsson from NL of Iceland to propose a formulation.

---

**6) Modification: allow for more precise timestamps for WARC-date
field**

**Issue:** The current standard (5.4) states that “The WARC-Date is a
14-digit UTC time-stamp formatted as YYYY-MM-DDThh:mm:ssZ, and shall
conform to the W3C profile of ISO 8601, i.e. 
[W3CDTF
]”.

It may happen that similar URLs are crawled at the same second, hence
generating a problem of duplicates. 

**Decision:** It looks necessary to allow for more precise timestamp,
below the level of the second.

**Action:** **Noah Lewitt** from Internet Archive to propose a
formulation.

---

**7) [Clarification: security issues](https://github.com/iipc/warc-specifications/issues/12)**

**Issue:** It is written in the WARC standards (8.3): “Security
considerations: The WARC record syntax poses no direct risk to computers
and networks. Implementers need to be aware of source authority and
trustworthiness of information structured in WARC. Readers and writers
subject themselves to all the risks that accompany normal operation of
data processing services (e.g. message length errors, buffer overflow
attacks)”.

This sentence looks misleading: it should not mean that it is impossible
to address security issues in WARC, but that it has been decided that it
should not be part of the standard.

**Decision:** This should be more clearly explained.

**Action: Jack Cushman from *Perma.cc* ** to propose a formulation.

---

**8)      [Augmentation: storing the “rendered target” in WARC record](https://github.com/iipc/warc-specifications/issues/13)**

**Issue:** some robots store “rendered target” along with files archived
on the web, i.e. screenshots of these files. A precise way to record
them should be proposed in the standard, as there is a consensus in the
community.

**Decision:** Propose a way to record rendered target either in the
standard or as an appendix (NB from Clément: I would probably favour the
second solution).

**Action:** **Andy Jackson from BL ** to propose something.

---

**9) [Augmentation: how to render AJAX interactions in WARC](https://github.com/iipc/warc-specifications/issues/14)**

**Issue:** it is necessary to have a common way of rendering AJAX
interactions in WARC. 

**Decision:** Propose a way to record rendering files either in the
standard or as an appendix (NB from Clément: I would probably vote for
the second solution).

**Action:** someone from LOCKSS (who??) to propose something.

---

**10) [Modification: support of HTTP 2.X protocol in WARC format.](https://github.com/iipc/warc-specifications/issues/15)**

**Issue:** nothing is said on the HTTP 2 protocol, which could give the
impression that WARC files cannot harvest documents in HTTP2.

**Decision:** few sentences on the handling of HTTP 2.X protocol should
be written.

**Action:** Kristinn Sigurðsson  to propose a formulation **and give an
example.**

---

**11) [Augmentation: specification of the WAT format.](https://github.com/iipc/warc-specifications/issues/16)**

**Issue:** WAT (Web Archive Transformation) is a “profile” of WARC
format intended to store web archive metadata, notably for data mining
processes
(see*https://webarchive.jira.com/wiki/display/Iresearch/Web+Archive+Transformation+%28WAT%29+Specification,+Utilities,+and+Usage+Overview*).
 Proposing the WAT format as an official (even though not prescriptive)
specification of the WARC format would give it more authority and would
allow more confidence in its maintenance.

**Decision:** Propose a specification of the WAT format as an
(informative) appendix of the standard. Ensure that the specification
may be freely available online. 

**Action: Vinay Goel from** Internet Archive to propose a specification,
with comments from WAT users such as **Andy Jackson from BL or Sara
Aubry from BnF**. Find a place to host the WAT specification (e.g. on
BnF website, as traditional host of the WARC standard draft?). 

 
