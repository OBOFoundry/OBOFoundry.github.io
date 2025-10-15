---
layout: citation
title: Known Ontology Project Publications
---

This list is generated automatically from OBO Foundry ontology metadata. It is not intended to be authoritative or exhaustive.
<div>
  {% for ontology in site.ontologies %}
    {% if ontology.publications and ontology.publications.size > 0 %}
      <h5>{{ ontology.title }} ({{ ontology.id }})</h5>
      <ul>
      {% for publication in ontology.publications %}
        <li><a href="{{ publication.id }}" target="_blank" rel="noopener">{{ publication.title }}</a></li>
      {% endfor %}
      </ul>
    {% endif %}
  {% endfor %}
</div>
