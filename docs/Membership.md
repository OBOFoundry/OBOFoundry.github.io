---
layout: doc
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
    <th role="columnheader">Picture</th>
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
    <td><img src="/images/ofoc/{{ member.github }}.png" alt="{{ member.name }} photo" style="max-height: 100px" class="align-text-top"></td>
    <td>{% if member.link %}<a href="{{ member.link }}">{{ member.name }}</a>{% else %}{{ member.name }}{% endif %}</td>
    <td><a href="https://orcid.org/{{ member.orcid }}">{{ member.orcid }}</a></td>
    <td><a href="https://github.com/{{ member.github }}">{{ member.github }}</a></td>
    <td>{{ member.affiliation.name }}</td>
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

