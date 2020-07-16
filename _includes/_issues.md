{% if page.status or page.path == "index.md" %}
  <div class="panel panel-default" id="issues_panel">
    <div class="panel-heading">
      <h3 class="panel-title nocount">
        Open Issues
      </h3>
    </div>
    <div class="panel-body">

<script src="{{site.url}}/assets/javascripts/jquery.min.js"></script>
<div id="github-issues-widget"></div>
<script type="text/javascript">
  GITHUB_ISSUES_USER = "iipc";
  GITHUB_ISSUES_REPO = "warc-specifications";
  /* Uncomment the following line to filter issues by one or more labels.*/
  {% if page.version-of != %}
  GITHUB_ISSUES_LABELS = "{{ page.version-of }}";
  {% endif %}
  /* To filter by multiple labels use a CSV string: */
  // GITHUB_ISSUES_LABELS = "feature,bug";
</script>

</div>
</div>

<script>
var GithubIssuesWidget = {};
GithubIssuesWidget.url = "https://api.github.com/repos/" + GITHUB_ISSUES_USER + "/" + GITHUB_ISSUES_REPO + "/issues?callback=?"
if(typeof window.GITHUB_ISSUES_LABELS != "undefined") {
    GithubIssuesWidget.url += "&labels=" + GITHUB_ISSUES_LABELS;
}
GithubIssuesWidget.go = function () {
  $('#github-issues-widget').append('<p class="loading">Loading...</p>');
  $.getJSON(this.url, function (data) {
    var list = $('<ul></ul>');
    $.each(data.data, function (issueIndex, issue) {
      var issueHtml = "<li>";
      issueHtml += '<a href="' + issue.html_url+ '">';
      issueHtml += issue.title;
      issueHtml += "</a>";
      var style = "";
      if( typeof issue.labels != "undefined") {
      $.each(issue.labels, function (labelIndex, label) {
        style = 'background-color:#' + label.color + ';';
        if(label.color == "000000"){
          style = 'color: white;' + style;
        }
        issueHtml += '&nbsp;<span class="label label-' + label.name + '" style="' + style + '">' + label.name + '</span>';
      });
      }
      issueHtml += "</li>";
      list.append(issueHtml);
    });
    $('#github-issues-widget p.loading').remove();
    $('#github-issues-widget').append(list);
  });
};
GithubIssuesWidget.go();
</script>
{% endif %}
