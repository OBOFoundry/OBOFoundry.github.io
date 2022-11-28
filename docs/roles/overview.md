---
layout: doc
title: Roles Overview
permalink: /roles/overview
---

{% for role in site.data.roles %}

## {{ role.name }}

{{ role.description }}

{% if role.open %}
<blockquote>This role is open to new members.</blockquote>
{% endif %}

{% if role.requirements %}

### Requirements

<ol>
{% for requirement in role.requirements %}
    <li>{{ requirement }}</li>
{% endfor %}
</ol>
{% endif %}

{% if role.responsibilities %}

### Responsibilities

<ol>
{% for responsibility in role.responsibilities %}
    <li>{{ responsibility }}</li>
{% endfor %}
</ol>
{% endif %}

### People

<table class="table">
<thead>
<tr>
<th>Name</th>
<th>ORCID</th>
<th>Status</th>
<th>Start</th>
</tr>
</thead>
<tbody>
{% for person in role.people %}
<tr>
    <td>{{ person.name }}</td>
    <td><a href="https://orcid.org/{{ person.orcid }}">{{ person.orcid }}</a></td>
    <td>{{ person.status }}</td>
    <td>{{ person.start }}</td>
</tr>
{% endfor %}
</tbody>
</table>

{% endfor %}
