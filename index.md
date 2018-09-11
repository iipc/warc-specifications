---
title: Welcome
---

Introduction
------------

This site and the corresponding [GitHub repository](https://github.com/iipc/warc-specifications) are being used by IIPC members and other interested parties to track and improve various specifications and proposals relating to web archiving.

In particular, [the specification of the WARC format](./specifications/warc-format/warc-1.1/) is hosted here, and we will develop extensions and forthcoming versions of the specification on this site, using GitHub [issues](https://github.com/iipc/warc-specifications/issues) and [pull requests](https://github.com/iipc/warc-specifications/pulls).

We also intend to publish and develop appropriate guidelines for web archiving, covering areas where common practice should be encouraged prior to any attempt at formal standardisation, e.g. through ISO.

How to contribute
-----------------

We are in the early staged of working out how best to develop these standards and guidelines.

* Use GitHub to review the [open issues](https://github.com/iipc/warc-specifications/issues) or [add new issues or comments](https://github.com/iipc/warc-specifications/issues).
    * Use the issue tags to identify the specification the issue applies to. 
* Contribute modifications to site by editing the pages on GitHub and submitting pull requests.
    * Every page has icons at the top and bottom that let you view and edit that page on GitHub. 
* Get in touch!
    * Use the IIPC Members mailing list, or [openwayback-dev](https://groups.google.com/forum/#!forum/openwayback-dev) otherwise.
    * *PROPOSAL:* Set up a dedicated, public mailing list?


### Specifications ###

{% assign sorted_pages = site.pages | sort:"title" %}

<ul>
{% for page in sorted_pages %}
{% if page.status %}
<li><a href="{{ site.baseurl }}{{ page.url }}">{{ page.title }}{% if page.version %} {{ page.version }}{% endif %}</a> <span class="badge spec-badge-status-{{ page.status }}">{{ page.status }}</span></li>
{% endif %}
{% endfor %}
</ul>

Specification Status
--------------------

The possible statuses of the specifications are as follows:

Proposed
: Document is for review and discussion, may change.

Adopted
: IIPC members have adopted the proposal and it may eventually be incorporated into an official standard. Whether *de facto* or official, it represents current best practices.

Standard
: Has been incorporated into an offical standard.

