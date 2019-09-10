---
title: List of WARC Fields
type: guidelines
---

This page attempts to track all known WARC fields whether standard, proposed for
standardisation or just used in the wild without formal specification.

<table class='table'>
    <thead>
        <tr>
            <th>Field</th>
            <th>Status</th>
            <th>Since</th>
            <th>Specification</th>
        </tr>
    </thead>
    <tbody>
    {%- assign specs = site.data.warc_fields.specs %}
    {%- assign fields = site.data.warc_fields.fields | sort: 0 %}
    {%- for field in fields %}
        {%- assign name = field.first %}
        {%- assign attrs = field.last %}
        {%- assign spec = attrs.spec %}
        {%- assign spec_base = spec | replace: "#", "/" | split: "/" | first %}
        {%- if specs[spec] %}
            {%- assign lower_name = name | downcase %}
            {%- assign spec_url = specs[spec] | append: "#" | append: lower_name %}
        {%- else  %}
            {%- if specs[spec_base] %}
                {%- assign spec_url = spec | replace_first: spec_base, specs[spec_base] %}
            {%- endif %}
        {%- endif %}
        {%- assign status = attrs.status %}
        {%- unless status %}
            {%- if attrs.since %}
                {%- assign status = "standard" %}
            {%- endif %}
        {%- endunless %}
        <tr>
            <td>{{ name }}</td>
            <td><span class='badge spec-badge-status-{{ status }}'>{{ status }}</span></td>
            <td>{{ attrs.since }}</td>
            <td><a href="{{ spec_url }}">{{ spec_base }}</a></td>
        </tr>
    {%- endfor %}
    </tbody>
</table>
