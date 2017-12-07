{% if page.status %}
{% for op in site.pages %}
{% if page.version-of == op.version-of %}
{% if op.latest == true and op.version != page.version %}
{% assign latest-version = op %}
{% endif %}
{% if op.version == page.previous-version %}
{% assign previous-version = op %}
{% endif %}
{% endif %}
{% if page.version == op.version %}
{%   if page.errata-for and page.errata-for == op.version-of %}
{%     assign errata-for = op %}
{%   endif %}
{%   if page.version-of and page.version-of == op.errata-for %}
{%     assign errata = op %}
{%   endif %}
{% endif %}
{% endfor %}
  <div class="panel panel-default" id="issues_panel">
    <div class="panel-heading">
      <h3 class="panel-title nocount">
        About
      </h3>
    </div>
    <div class="panel-body">
    <dl>
    <dt>Title<dt>
    <dd>{{ page.title }}{% if page.version %} {{ page.version }}{% endif %}&nbsp;<span class="badge spec-badge-status-{{ page.status }}">{{ page.status }}</span></dd>
{% if errata-for %}
    <dt>Errata for</dt>
    <dd><a href="{{ site.baseurl }}{{ errata-for.url }}">{{errata-for.title}} {{errata-for.version}}</a></dd>
{% else %}
    <dt>Latest version</dt>
{% if latest-version %}
    <dd><a href="{{ site.baseurl }}{{ latest-version.url }}">See version {{ latest-version.version }}</a></dd>
{% else %}
    <dd>This is the latest version</dd>
{% endif %}
    <dt>Previous version<dt>
{% if previous-version %}
    <dd><a href="{{ site.baseurl }}{{ previous-version.url }}">See version {{ previous-version.version }}</a></dd>
{% else %}
    <dd>None</dd>
{% endif %}
{% endif %}
{% if errata %}
    <dt>Errata</dt>
    <dd><a href="{{ site.baseurl }}{{ errata.url }}">See the errata for version {{ page.version }}</a></dd>
{% endif %}
{% if page.version-of %}
    <dt>Issues</dt>
    <dd><a href="https://github.com/iipc/warc-specifications/labels/{{ page.version-of }}">View issues on GitHub&nbsp;<span class="glyphicon glyphicon-tags"></span></a></dd>
{% endif %}
    </dl>
    </div>
</div>
{% endif %}
