---
title: WARC Extensions
license: CC0 1.0
---
{% assign fields = site.pages | where: "warc_extension_type", "field" %}

## Named fields

<table>
{% for field in fields %}
  <tr>
    <td>[{{ field.title }}]({{ site.baseurl }}{{ field.url }})</td>
    <td>{{field.status}}</td>
  </tr>
{% endfor %}
</table>

# Scope

Additive proposals to the WARC format such as new named fields, record types and profiles.

This is not the primary home for clarification, correction or usage guidance for the main WARC specification. Instead 
see the [community annotations](../warc-1.1-annotated/) and [guidelines](../../guidelines/).

# Licensing Note

The text of these extensions is intended to be freely reusable in implementations, API documentation and later standards
work. To this end they should be marked as [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) whenever possible.
