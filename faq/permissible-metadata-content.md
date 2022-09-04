---
layout: faq
title: Metadata content
---

This FAQ is about the content of the various fields in your ontology metadata file. Instructions on how to edit that file is covered by the FAQ <a href="faq/how-do-i-edit-metadata.html">How do I edit the metadata for my ontology?</a>

NOTE: In the instructions below, items in angle brackets&mdash;including the brackets `<>` themselves&mdash;should be replaced by the appropriate content.

## What can I put in the 'publications' field?

Allowed number of entries: _any_<br>
Each entry under this field should have one 'id' subfield and one 'title' subfield with content as indicated:

- id: `<cited reference>` The cited reference must take the form of a URI that points to one of the following permitted resources: PubMed, PubMed Central, or a Digital Object Identifier (DOI) service.

&emsp;&emsp;&emsp;Example URI for PubMed: https://www.ncbi.nlm.nih.gov/pubmed/27128319<br>
&emsp;&emsp;&emsp;Example URI for PubMed Central: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4851331<br>
&emsp;&emsp;&emsp;Example URI for a DOI: https://doi.org/10.1371/journal.pone.0154556

<ul>Examples of other DOI services include journals, preprint servers such as arXiv, bioRxiv, medRxiv, and ChemRxiv, and alternative hosting platforms such as Zenodo and FigShare. Note, however, that the DOI link for these must be used rather than the direct link. For example, instead of a direct link to Zenodo such as https://zenodo.org/record/6685957, the equivalent DOI record https://doi.org/10.5281/zenodo.6685957 must be used. Direct links to PDFs or resources such as CEUR-WS (http://ceur-ws.org/) that do not provide DOIs are not permitted. In such cases the Zenodo platform can be used to upload content that does not have a home in any of the permitted resources.</ul>

- title: `<title of cited reference>` Technically this is a free-text field, but best practice is to use the title of the publication cited under the 'id' subfield.
