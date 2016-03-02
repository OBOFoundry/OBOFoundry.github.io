# OBO Citation and Attribution Policy

Open Biological and Biomedical Ontologies are used in a diversity of ways. The following guidelines are intended to promote proper attribution of the ontology creators and contributors, and to promote reproducibility in informatics applications.


## Referring to a single term

When referring to a single ontology term, use the full [Internationalized Resource Identifier (IRI)](http://tools.ietf.org/html/rfc3987), for example:

> http://purl.obolibrary.org/obo/UBERON_0000948

When it is clear from the context which ontology is being used, you can use a shorter [Compact URI (CURIE)](https://www.w3.org/TR/2009/CR-curie-20090116/) with a prefix rather than a full IRI:

> UBERON:0000948

We also recommend including the primary label of the term, in quotation marks, before or after the term identifier:

> 'heart' UBERON:0000948

> UBERON:0000948 'heart'


## Referring to an ontology

To facilitate reproducibility, be specific about the version of the ontology that you are referring to by using an ontology version IRI that contains the release date:

> http://purl.obolibrary.org/obo/uberon/releases/2016-01-26/uberon.owl

The ontology version IRI is indicated by the [owl:versionIRI](https://www.w3.org/2002/07/owl#versionIRI) property.

When referring to an ontology in general, you can use its ontology IRI:

> http://purl.obolibrary.org/obo/uberon.owl


## Citing an ontology

Some ontologies recommend citation of specific publications. Please see their respective homepages for this information. For example, [Uberon](http://obofoundry.org/ontology/uberon.html) lists two publications under "Cite."

When no specific publication is recommended, use the [new data citation extension to JATS](https://peerj.com/articles/cs-1/). Our ontology files list authors using the [dc:creator](http://purl.org/dc/elements/1.1/creator) property. The order of authors is not important, but you can use the primary contact for the ontology listed on the [OBO site](http://obofoundry.org) as the first author. Here is an example citation:

> Mungall, C., Haendel, M., Dahdul, W., Ibrahim, N., Segerdell, E., Blackburn, D., Comte, A., Niknejad, A., and Decechi, A. (2016), Uberon Ontology, http://purl.obolibrary.org/obo/uberon/releases/2016-01-26/uberon.owl

Note that this does not necessarily include all those who have contributed directly to the ontology, via its issue tracker or on its mailing lists, for example. However, these can be readily retrieved if the proper IRI is referenced in the citation.
