---
layout: doc
id: TechnicalWG
title: Technical Working Group
---

The OBO Foundry Operations Committee Technical WG is involved in maintaining the technical infrastructure for the OBO Foundry. This includes establishment of policies to be implemented in common tools, website maintenance, etc.

## Members

<table class="table">
<thead>
<tr>
    <th role="columnheader">Name</th>
    <th role="columnheader">ORCID</th>
    <th role="columnheader">Affiliation</th>
</tr>
</thead>
<tbody>
{% for member in site.data.technical.members %}
<tr>
    <td>{% if member.link %}<a href="{{ member.link }}">{{ member.name }}</a>{% else %}{{ member.name }}{% endif %}</td>
    <td>{% if member.orcid %}<a href="https://orcid.org/{{ member.orcid }}">{{ member.orcid }}</a>{% endif %}</td>
    <td>{{ member.affiliation }}</td>
</tr>
{% endfor %}
</tbody>
</table>

## Links

- <a href='TechnicalWGMeetings.html'>Meetings</a>
- <a href='Policy_for_OBO_namespace_and_associated_PURL_requests.html'>Creating a prefix and domain for a resource</a>
- <a href='OBOPURLDomain.html'>How is the OBO PURL configured</a>

## Contact Us

The best way to contact the OBO Foundry Technical Working Group is through the <a href='https://github.com/OBOFoundry/OBOFoundry.github.io/issues'>issue tracker</a>. Select the Technical group template or the Prefix/domain request template.<br>
<br>
The mailing list for the OBO Foundry Technical Working Group is <a href='mailto:obo-foundry-technical-working-group@googlegroups.com'>obo-foundry-technical-working-group@googlegroups.com</a>. This is currently a closed list, but non-members can post to the list.
