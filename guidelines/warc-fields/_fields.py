#!/usr/bin/env python3

import yaml
from textwrap import dedent, indent

data = yaml.load(open("_fields.yml"))

print(dedent("""
{% comment %}
Generated from fields.yml. Don't edit this directly. Run 'make' to update.
{% endcomment %}
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
""").strip('\n'))

for name, value in sorted(data['fields'].items()):
    spec = value.get('spec')
    if '/' in spec:
        spec_id, path = spec.split('/', 1)
        spec_url = data['specs'][spec_id] + '/' + path
    elif '#' in spec:
        spec, path = spec.split('#', 1)
        spec_url = data['specs'][spec] + '#' + path
    elif spec in data['specs']:
        spec_url = data['specs'][spec] + '#' + name.lower()
    else:
        spec_url = ''

    status = value.get('status', '')
    if not status and 'since' in value:
        status = "standard"

    row = f"""
        <tr>
            <td>{name}</td>
            <td><span class='badge spec-badge-status-{status}'>{status}</span></td>
            <td>{value.get('since', '')}</td>
            <td><a href="{spec_url}">{spec}</a></td>
        </tr>
    """
    print(indent(dedent(row).strip('\n'), "    "))

print(dedent("""
    </tbody>
</table>
""").strip('\n'))
