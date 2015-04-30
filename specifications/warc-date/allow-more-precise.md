---
title: Proposal to Revise the WARC Spec to Allow More Precise Values WARC-Date
status: proposed
---

* TOC
{:toc}

Current (2009) Spec
-------------------
> #### 5.4 WARC-Date (mandatory)
> 
> A 14-digit UTC timestamp formatted according to YYYY-MM-DDThh:mm:ssZ, described
> in the W3C profile of ISO8601 [W3CDTF]. The timestamp shall represent the
> instant that data capture for record creation began. Multiple records written
> as part of a single capture event (see section 5.7) shall use the same
> WARC-Date, even though the times of their writing will not be exactly
> synchronized.
> 
>     WARC-Date   = "WARC-Date" ":" w3c-iso8601
>     w3c-iso8601 = <YYYY-MM-DDThh:mm:ssZ>
> 
> All records shall have a WARC-Date field.


Proposed Revised Spec
---------------------
> #### 5.4 WARC-Date (mandatory)
> 
> A UTC timestamp as described in the W3C profile of ISO8601 [W3CDTF]. The
> timestamp shall represent the instant that data capture for record creation
> began. Multiple records written as part of a single capture event (see section
> 5.7) shall use the same WARC-Date, even though the times of their writing will
> not be exactly synchronized. WARC-Date shall be specified as a complete date
> plus hours, minutes and seconds, or as a complete date plus hours, minutes,
> seconds and a decimal fraction of a second. If WARC-Date includes a decimal
> fraction of a second, the decimal fraction of a second shall have a minimum of
> 1 digit and a maximum of 9 digits. WARC-Date should be specified with as
> much precision as is accurately known.
> 
>     WARC-Date   = "WARC-Date" ":" w3c-iso8601
>     w3c-iso8601 = <YYYY-MM-DDThh:mm:ss.sZ> | <YYYY-MM-DDThh:mm:ssZ>
>
> All records shall have a WARC-Date field.


Alternative Proposed Revised Spec (Not Preferred)
-------------------------------------------------
Not preferred because it's unclear what the correct behavior at replay time
should be, when a specific timestamp is requested and an approximate timestamp is
available. and implementing the correct behavior may be complex. In the absence
of specific known use cases, better not to force tools to tackle this
potentially hard problem. (Are there specific known use cases?)

> #### 5.4 WARC-Date (mandatory)
> 
> A UTC timestamp as described in the W3C profile of ISO8601 [W3CDTF]. The
> timestamp shall represent the instant that data capture for record creation
> began. Multiple records written as part of a single capture event (see section
> 5.7) shall use the same WARC-Date, even though the times of their writing will
> not be exactly synchronized. WARC-Date may be specified at any of the six
> levels of granularity described in [W3CDTF].  If WARC-Date includes a decimal
> fraction of a second, the decimal fraction of a second shall have a minimum of
> 1 digit and a maximum of 9 digits. WARC-Date should be specified with as
> much precision as is accurately known.
> 
>     WARC-Date   = "WARC-Date" ":" w3c-iso8601
>     w3c-iso8601 = w3c-iso8601-14+ | w3c-iso8601-14 | w3c-iso8601-12 | w3c-iso8601-10 | w3c-iso8601-8 | w3c-iso8601-6 | w3c-iso8601-4
>     w3c-iso8601-14+ = <YYYY-MM-DDThh:mm:ss.sZ>
>     w3c-iso8601-14  = <YYYY-MM-DDThh:mm:ssZ>
>     w3c-iso8601-12  = <YYYY-MM-DDThh:mmZ>
>     w3c-iso8601-8   = <YYYY-MM-DD>
>     w3c-iso8601-6   = <YYYY-MM>
>     w3c-iso8601-4   = <YYYY>
> 
> All records shall have a WARC-Date field.

