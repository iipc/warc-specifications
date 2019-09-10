  <div class="panel panel-default" id="toc_panel">
    <div class="panel-heading">
      <h3 class="panel-title nocount">
        Contents
      </h3>
    </div>
    <div class="panel-body">
    <div id="toc">
{% if page.numbered == true %}
<div class="numbered-headers">
{% endif %}
<div markdown="1">
*  Auto generated table of contents
{:toc}
{% if page.numbered == true %}
</div>
{% endif %}
</div>
    </div>
    </div>
  </div>

<!-- CUT -->

{{ page.content }}
