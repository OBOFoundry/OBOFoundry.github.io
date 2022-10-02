---
layout: doc
id: TechnicalWG
title: Technical Working Group
---

The OBO Foundry Operations Committee Technical WG is involved in maintaining the technical infrastructure for the OBO Foundry. This includes establishment of policies to be implemented in common tools, website maintenance, etc.

- <a href='TechnicalWGMeetings.html'>Meetings</a>
- <a href='Policy_for_OBO_namespace_and_associated_PURL_requests.html'>Creating a prefix and domain for a resource</a>
- <a href='OBOPURLDomain.html'>How is the OBO PURL configured</a>

## Contact Us

The best way to contact the OBO Foundry Technical Working Group is through the <a href='https://github.com/OBOFoundry/OBOFoundry.github.io/issues'>issue tracker</a>. Select the Technical group template or the Prefix/domain request template.<br>
<br>
The mailing list for the OBO Foundry Technical Working Group is <a href='mailto:obo-foundry-technical-working-group@googlegroups.com'>obo-foundry-technical-working-group@googlegroups.com</a>. This is currently a closed list, but non-members can post to the list.

## Members

<table class="table">
<thead>
<tr>
    <th role="columnheader">Name</th>
    <th role="columnheader">ORCID</th>
    <th role="columnheader">GitHub</th>
    <th role="columnheader">Affiliation</th>
    <th role="columnheader">Country</th>
</tr>
</thead>
<tbody>
{% assign members = site.data.operations.members | sort: "name" | where_exp:"item","item.groups contains 'technical'" %}
{% for member in members %}
<tr>
    <td>{% if member.link %}<a href="{{ member.link }}">{{ member.name }}</a>{% else %}{{ member.name }}{% endif %}</td>
    <td><a href="https://orcid.org/{{ member.orcid }}">{{ member.orcid }}</a></td>
    <td><a href="https://github.com/{{ member.github }}">{{ member.github }}</a></td>
    <td>{{ member.affiliation }}</td>
    <td>{{ member.country }}</td>
</tr>
{% endfor %}
</tbody>
</table>
