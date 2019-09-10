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
    {%- assign refs = site.data.refs %}
    {%- assign fields = site.data.warc_fields %}
    {%- for field in fields %}
        {%- assign name = field.first %}
        {%- assign attrs = field.last %}
        {%- assign spec = attrs.spec %}
        {%- assign spec_base = spec | replace: "#", "/" | split: "/" | first %}
        {%- if refs[spec] %}
            {%- assign lower_name = name | downcase %}
            {%- assign spec_url = refs[spec] | append: "#" | append: lower_name %}
        {%- else  %}
            {%- if refs[spec_base] %}
                {%- assign spec_url = spec | replace_first: spec_base, refs[spec_base] %}
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
