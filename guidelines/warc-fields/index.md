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
    {%- for field in site.data.warc_fields %}
        {%- assign spec_base = field.spec | replace: "#", "/" | split: "/" | first %}
        {%- if refs[field.spec] %}
            {%- assign lower_name = field.name | downcase %}
            {%- assign spec_url = refs[field.spec] | append: "#" | append: lower_name %}
        {%- else  %}
            {%- if refs[spec_base] %}
                {%- assign spec_url = field.spec | replace_first: spec_base, refs[spec_base] %}
            {%- endif %}
        {%- endif %}
        {%- assign status = field.status %}
        {%- unless status %}
            {%- if field.since %}
                {%- assign status = "standard" %}
            {%- endif %}
        {%- endunless %}
        <tr>
            <td>{{ field.name }}</td>
            <td><span class='badge spec-badge-status-{{ status }}'>{{ status }}</span></td>
            <td>{{ field.since }}</td>
            <td><a href="{{ spec_url }}">{{ field.spec | split: "#" | first }}</a></td>
        </tr>
    {%- endfor %}
    </tbody>
</table>
