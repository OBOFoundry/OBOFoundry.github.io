---
layout: doc
title: Publications Related to the OBO Foundry
---
## Citing the OBO Foundry

[**OBO Foundry in 2021: operationalizing open data principles to evaluate ontologies**](https://academic.oup.com/database/article/doi/10.1093/database/baab069/6410158) **(2021)**.

Rebecca Jackson, Nicolas Matentzoglu, James A Overton, Randi Vita, James P Balhoff, Pier Luigi Buttigieg, Seth Carbon, Melanie Courtot, Alexander D Diehl, Damion M Dooley, William D Duncan, Nomi L Harris, Melissa A Haendel, Suzanna E Lewis, Darren A Natale, David Osumi-Sutherland, Alan Ruttenberg, Lynn M Schriml, Barry Smith, Christian J Stoeckert Jr., Nicole A Vasilevsky, Ramona L Walls, Jie Zheng, Christopher J Mungall, Bjoern Peters. *Database*, Volume 2021, baab069, https://doi.org/10.1093/database/baab069

## Other papers about the OBO Foundry

[The OBO Foundry: coordinated evolution of ontologies to support biomedical data integration](http://www.nature.com/nbt/journal/v25/n11/abs/nbt1346.html)

Barry Smith, Michael Ashburner, Cornelius Rosse, Jonathan Bard, William Bug, Werner Ceusters, Louis J Goldberg, Karen Eilbeck, Amelia Ireland, Christopher J Mungall, The OBI Consortium, Neocles Leontis, Philippe Rocca-Serra, Alan Ruttenberg, Susanna-Assunta Sansone, Richard H Scheuermann, Nigam Shah, Patricia L Whetzel, and Suzanna Lewis

*Nature Biotechnology* **25**, 1251 - 1255 (2007)

[Google Scholar list of papers citing The OBO Foundry](https://scholar.google.ca/scholar?cites=13806088078865650870&as_sdt=2005&sciodt=0,5&hl=en)

### Some Ontology Project Publications (not a complete list)

<ul>
{% for ontology in site.ontologies %}
{% for publication in ontology.publications %}
<li>
    {{ ontology.title }} ({{ ontology.id }}):
    <a href="{{ publication.id }}">{{ publication.title }}</a>
</li>
{% endfor %}
{% endfor %}
</ul>
