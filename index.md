---
title: Welcome
---

Introduction
------------

This site and the corresponding [GitHub repository](https://github.com/iipc/warc-specifications) are being used by IIPC members and other interested parties to track and improve various specifications and proposals relating to web archiving.

In particular, [the specification of the WARC format](./specifications/warc-format/) is hosted here, and we will develop the forthcoming 1.1 version of the specification on this site, using GitHub [issues](https://github.com/iipc/warc-specifications/issues) and [pull requests](https://github.com/iipc/warc-specifications/pulls).

We also intend to publish and develop appropriate guidelines for web archiving, covering areas where common practice should be encouraged prior to any attempt at formal standardisation, e.g. through ISO.

How to contribute
-----------------

We are in the early staged of working out how best to develop these standards and guidelines.

* Use GitHub to open issues you wish to raise.
* Contribute modifications to site by editing the pages on GitHub and submitting pull requests.
* *PROPOSAL:* Set up a dedicated, public mailing list?

Strands
-------

<ul>
{% for page in site.pages | sort:"title" %}
{% if page.strand %}
<li><a href="{{ site.baseurl }}{{ page.url }}">{{ page.title }}</a></li>
{% endif %}
{% endfor %}
</ul>

### Individual Specifications ###

<ul>
{% for page in site.pages | sort:"title" %}
{% if page.status %}
<li><a href="{{ site.baseurl }}{{ page.url }}">{{ page.title }}{% if page.version %} {{ page.version }}{% endif %}</a> <span class="badge spec-badge-status-{{ page.status }}">{{ page.status }}</span></li>
{% endif %}
{% endfor %}
</ul>

Specification Status
--------------------

The possible statuses of the specifications are as follows:

Proposed
: Document is for review and discussion, may change

Adopted
: IIPC has adopted the proposal and it may eventually be incorporated into an official standard. In any case, it represents current best practices.

Standard
: Has been incorporated into an offical standard, would include a version number

