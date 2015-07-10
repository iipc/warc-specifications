{% if page.status %}
{% for op in site.pages %}
{% if page.version-of == op.version-of %}
{% if op.latest == true %}
{% assign latest-version = op %}
{% endif %}
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
    <dd>{{ page.title }}</dd>
    <dt>Status<dt>
    <dd><span class="badge spec-badge-status-{{ page.status }}">{{ page.status }}</span></dd>
    <dt>Versions<dt>
    <dd> {% if page.previous-version %}<a class="badge" href="../{{ page.previous-version }}">previous</a>{% endif %}&nbsp;{% if latest-version %}<a class="badge" href="{{ site.baseurl }}{{ latest-version.url }}">latest</a>{% endif %}</dd>
{% if page.version-of %}
    <dt>Issues</dt>
    <dd><a href="https://github.com/iipc/warc-specifications/labels/{{ page.version-of }}">View issues on GitHub&nbsp;<span class="glyphicon glyphicon-tags"></span></a></dd>
{% endif %}
    </dl>
    </div>
</div>
{% endif %}