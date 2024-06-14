---
layout: doc
title: OBO Citation and Attribution Policy
---

Open Biological and Biomedical Ontologies are used in a diversity of ways. The following guidelines are intended to promote proper attribution of the ontology creators and contributors, and to promote reproducibility in informatics applications.

## Referring to a single term

When referring to a single ontology term, use the full [Internationalized Resource Identifier (IRI)](http://tools.ietf.org/html/rfc3987), for example:

> http://purl.obolibrary.org/obo/UBERON_0000948

You can use a shorter [Compact URI (CURIE)](https://www.w3.org/TR/curie/) by defining a prefix that abbreviates the first part of the IRI. For example, the prefix "UBERON" can abbreviate "http://purl.obolibrary.org/obo/UBERON_", then "http://purl.obolibrary.org/obo/UBERON_0000948" can be shortened to "[UBERON:0000948](http://purl.obolibrary.org/obo/UBERON_0000948)". A footnote like this one should be included with the first use of the prefix:

> [UBERON:0000948](http://purl.obolibrary.org/obo/UBERON_0000948) is a Compact URI (CURIE). Here and subsequently the prefix "UBERON" expands to "http://purl.obolibrary.org/obo/UBERON_". The full identifier for the term is then <http://purl.obolibrary.org/obo/UBERON_0000948>. Browsing to this address gives further information about the term.

In situations that allow the use of hyperlinks, every CURIE should be a hyperlink with its full IRI as its target, as in these examples.

We also recommend including the primary label of the term in quotation marks before the IRI or CURIE:

> 'heart' ([UBERON:0000948](http://purl.obolibrary.org/obo/UBERON_0000948))

## Referring to an ontology

To facilitate reproducibility, be specific about the version of the ontology that you are referring to by using an ontology version IRI that contains the release date:

> http://purl.obolibrary.org/obo/uberon/releases/2016-01-26/uberon.owl

The ontology version IRI is indicated by the [owl:versionIRI](https://www.w3.org/2002/07/owl#versionIRI) property.

When referring to an ontology in general (not a specific version) you can use its ontology IRI:

> http://purl.obolibrary.org/obo/uberon.owl

The ontology IRI or ontology version IRI should be accompanied by a citation of the ontology, in any context where citations are appropriate.

## Citing an ontology

Some ontologies recommend citation of specific publications. Please see their respective homepages for this information. For example, [Uberon]({{ "ontology/uberon.html#publications" | prepend: site.baseurl }}) lists two publications under "Publications."

In addition to the recommended publication, you should also cite the ontology using its IRI and the [new data citation extension to JATS](https://peerj.com/articles/cs-1/). When no specific publication is recommended, you must cite the ontology by its IRI. Here is an example citation:

> Mungall, C., Haendel, M., Dahdul, W., Ibrahim, N., Segerdell, E., Blackburn, D., Comte, A., Niknejad, A., and Decechi, A. (2016), Uberon Ontology, http://purl.obolibrary.org/obo/uberon/releases/2016-01-26/uberon.owl

Our ontology files list authors using the [dc:creator](http://purl.org/dc/elements/1.1/creator) property. The order of authors is not important, but you can use the primary contact for the ontology listed on the [OBO site](http://obofoundry.org) as the first author. Note that this does not necessarily include all those who have contributed directly to the ontology, via its issue tracker or on its mailing lists, for example. However, these can be readily retrieved if the proper IRI is referenced in the citation.
