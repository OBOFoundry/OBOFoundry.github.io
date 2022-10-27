---
layout: doc
id: Membership
title: Membership
---

The OBO Foundry Operations Committee discusses, oversees, and ensures the completion of the fundamental day-to-day activities of the Foundry. The Committee is composed of three working groups. Anyone who is active in a working group (active being based on both attendance at WG meetings and actual work done for working groups) is considered a member of the Operations Committee.

There are currently three working groups. Each page lists their respective members:

- [Editorial Working Group](EditorialWG.html)
- [Technical Working Group](TechnicalWG.html)
- [Outreach Working Group](OutreachWG.html)

<table class="table table-striped table-hover">
<thead>
<tr>
    <th role="columnheader">Name</th>
    <th role="columnheader">ORCID</th>
    <th role="columnheader">GitHub</th>
    <th role="columnheader">Affiliation</th>
    <th role="columnheader">Country</th>
    <th role="columnheader">Groups</th>
</tr>
</thead>
<tbody>
{% assign members = site.data.operations.members | sort: "name" %}
{% for member in members %}
<tr>
    <td>{% if member.link %}<a href="{{ member.link }}">{{ member.name }}</a>{% else %}{{ member.name }}{% endif %}</td>
    <td><a href="https://orcid.org/{{ member.orcid }}">{{ member.orcid }}</a></td>
    <td><a href="https://github.com/{{ member.github }}">{{ member.github }}</a></td>
    <td>{{ member.affiliation }}</td>
    <td>{{ member.country }} </td>
    <td>{{ member.groups | join: ", " }}</td>
</tr>
{% endfor %}
</tbody>
</table>

New members: follow the instructions on the [onboarding doc](https://docs.google.com/document/d/1MKhNTjZjGx6Ls72dybIV2ajYtbqtwP7O4lwxN2v3RBA/edit#heading=h.10q6n5qc13dp)

## Alumni

<table class="table table-striped table-hover">
<thead>
<tr>
    <th role="columnheader">Name</th>
    <th role="columnheader">ORCID</th>
    <th role="columnheader">GitHub</th>
    <th role="columnheader">Departed</th>
    <th role="columnheader">Note</th>
</tr>
</thead>
<tbody>
{% assign alumni_members = site.data.alumni.members | sort: "name" %}
{% for member in alumni_members %}
<tr>
    <td>{% if member.link %}<a href="{{ member.link }}">{{ member.name }}</a>{% else %}{{ member.name }}{% endif %}</td>
    <td><a href="https://orcid.org/{{ member.orcid }}">{{ member.orcid }}</a></td>
    <td>{% if member.github %}<a href="https://github.com/{{ member.github }}">{{ member.github }}</a>{% endif %}</td>
    <td>{% if member.departed %}{{ member.departed }}{% endif %}</td>
    <td>{% if member.note %}{{ member.note }}{% endif %}</td>
</tr>
{% endfor %}
</tbody>
</table>

## Roles

{% for role in site.data.roles %}

### {{ role.name }}

{{ role.description }}

{% if role.open %}
<blockquote>This role is open to new members.</blockquote>
{% endif %}

{% if role.requirements %}

#### Requirements

<ol>
{% for requirement in role.requirements %}
    <li>{{ requirement }}</li>
{% endfor %}
</ol>
{% endif %}

{% if role.responsibilities %}

#### Responsibilities

<ol>
{% for responsibility in role.responsibilities %}
    <li>{{ responsibility }}</li>
{% endfor %}
</ol>
{% endif %}

#### People

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
