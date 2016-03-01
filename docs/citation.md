# OBO Foundry Citation and Attribution Policy #

This policy pertains to ontologies that have been submitted to the OBO - the Open Biomedical Ontologies, also called the OBO Library.
The policies that are recommended here are intended to be normative for OBO Foundry ontologies and suggested for all OBO Library ontologies. 

As OBO Ontologies are intended to meet the requirements of the OBO [Open principle](/principles/fp-001-open.html), they tend to be utilized in a diversity of ways by a diversity of people.
We want this to continue to occur, but we simultaneously would like to promote proper attribution to the creators and contributors and reproducibility where relevant.

## Referencing a single class or property ##

When referencing a specific ontology term, one should reference the URI of the class or property:
http://purl.obolibrary.org/obo/UBERON_0001244
or the CURIE and the label:
'anal sphincter' UBERON:0001244

## Citing a specific ontology version ##
In the context of reproducibility, it is important that the version of each ontology be recorded. 
The version IRI can be found in the OWL file header, for example:

```<owl:versionIRI rdf:resource="http://purl.obolibrary.org/obo/uberon/releases/2016-01-26/uberon.owl"/>```

In citing a specific version in a manuscript, one should use the IRI: http://purl.obolibrary.org/obo/uberon/releases/2016-01-26/uberon.owl

In some circumstances when referring more generally to an ontology, it is appropriate to cite the base purl: http://purl.obolibrary.org/obo/uberon.owl

For journal citations, we can utilize the new data citation extension to JATS, see https://peerj.com/articles/cs-1/ for more info. 
Essentially this allows the citation of any identifier outside the paywall of the journal. In this way, either a specific version IRI or base URI can be referenced with the creators of the ontology listed as authors. 
Note that these are seen in the ontology file directly:

```<dc:creator rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Chris Mungall - http://orcid.org/0000-0002-6601-2165</dc:creator>```

The order of authors is not important, though you can use the primary contact listed on the OBO site as the first author as a default.
Here is an example citation:

Mungall, C., Haendel, M., Dahdul, W., Ibrahim, N., Segerdell, E., Blackburn, D., Comte, A., Niknejad, A., and Decechi, A. (2016), Uberon Ontology, http://purl.obolibrary.org/obo/uberon/releases/2016-01-26/uberon.owl 

Note that this does not do full diligence to the very many of contributors to any given ontology that have contributed directly or via the tracker or discussion lists.
However, these are readily retrieved in analyses if the proper URI is referenced in the citation.

## Journal article citations ##

Some ontologies also recommend citation of specific publications, please see their respective homepages for this information. 
For example, [Uberon] (/ontology/uberon.html) lists two publications under "Cite."


