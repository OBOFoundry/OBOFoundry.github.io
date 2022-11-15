---
layout: default
permalink: /pages
title: Pages and Posts
---

<table class="table table-striped">
<thead>
<tr>
<th>ID</th>
<th>URL</th>
<th>Title</th>
</tr>
</thead>
<tbody>
{% assign filtered_posts = site.pages | sort: "url" %}
{% for page in filtered_posts %}
{% unless page.url contains "/ontology" %}
<tr>
<td><code>{{ page.id }}</code></td>
<td>
   <a href="{{ page.url }}">{{ page.url }}</a>
</td>
<td>
    <a href="{{ page.url }}">{{ page.title }}</a>
</td>
</tr>
{% endunless %}
{% endfor %}
</tbody>
</table>
