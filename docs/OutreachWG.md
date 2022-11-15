---
layout: doc
id: OutreachWG
title: Outreach Working Group
---

The OBO Foundry Outreach WG is involved in public relations for the OBO Foundry. This includes monitoring and following up discussions on mailing lists, preparing documentation and educational materials, and presenting OBO Foundry activities at workshops, conferences, or other venues.

## Contact Us

The best way to contact the OBO Foundry Outreach Working Group is through the <a href='https://github.com/OBOFoundry/OBOFoundry.github.io/issues'>obo foundry issue tracker</a>. A member of the OBO admin group will assign the `outreach` label to the ticket.

The mailing list for the OBO Foundry Outreach Working Group is <a href='mailto:obo-foundry-outreach-working-group@googlegroups.com'>obo-foundry-outreach-working-group@googlegroups.com</a>. This is currently a closed list, but non-members can post to the list.

## Members

<table class="table table-striped table-hover">
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
{% assign members = site.data.operations.members | sort: "name" | where_exp:"item","item.groups contains 'outreach'" %}
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
