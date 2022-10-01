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

New members: follow the instructions on the [onboarding doc](https://docs.google.com/document/d/1MKhNTjZjGx6Ls72dybIV2ajYtbqtwP7O4lwxN2v3RBA/edit#heading=h.10q6n5qc13dp)

## Alumni

<table class="table">
<thead>
<tr>
    <th role="columnheader">Name</th>
    <th role="columnheader">ORCID</th>
    <th role="columnheader">Note</th>
</tr>
</thead>
<tbody>
{% for member in site.data.alumni.members %}
<tr>
    <td>{% if member.link %}<a href="{{ member.link }}">{{ member.name }}</a>{% else %}{{ member.name }}{% endif %}</td>
    <td>{% if member.orcid %}<a href="https://orcid.org/{{ member.orcid }}">{{ member.orcid }}</a>{% endif %}</td>
    <td>{% if member.note %}{{ member.note }}{% endif %}</td>
</tr>
{% endfor %}
</tbody>
</table>



<ul>
{% for member in site.data.alumni.members %}
<li>
{% if member.link %}<a href="{{ member.link }}">{{ member.name }}</a>{% else %}{{ member.name }}{% endif %}
{% if member.note %}({{ member.note }}){% endif %}
</li>
{% endfor %}
</ul>
