---
layout: doc
id: EditorialWG
title: Editorial Working Group
---

The primary task of the Editorial WG is to facilitate the review of candidate OBO Foundry ontologies. This task includes developing the principles against which ontologies are reviewed, developing the review process itself, conducting the reviews, and setting policies governing the process.

## Scope

The OBO Foundry Editorial WG will:

- create guidelines for ontology review process (how we do reviews, operationally)
- create policies for ontology review criteria (what aspects of an ontology and which ontologies we should review)
- manage the ontology review process

Current activities are focused on creating guidelines for reviews. Once those guidelines are in place, the working group will shift its focus to carrying out the review process, with an aim of reducing the backlog of ontologies awaiting review.

## Draft guidelines and policies

### Ontology Review

- [Ontology review process guidelines](/docs/ReviewProcessGuidelines.html)
- [Ontology review criteria policies](/docs/ReviewCriteriaPolicies.html)

### Principles Review

[Principles review workflow](/docs/PrinciplesReviewWorkflow.html)

## Contact Us

The best way to contact the OBO Foundry Editorial Working Group is through the <a href='https://github.com/OBOFoundry/OBOFoundry.github.io/issues/'>issue tracker</a>.<br>
<br>
The mailing list for the OBO Foundry Editorial Working Group is <a href='mailto:obo-foundry-editorial-working-group@googlegroups.com'>obo-foundry-editorial-working-group@googlegroups.com</a>. This is currently a closed list, but non-members can post to the list.

## Members

Membership in the OBO Foundry Editorial WG is open to all members of the OBO Foundry Operations Committee who are willing to actively participate. If you are interested in joining the working group, send an email to the mailing list.

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
{% assign members = site.data.operations.members | sort: "name" | where_exp:"item","item.groups contains 'editorial'" %}
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
