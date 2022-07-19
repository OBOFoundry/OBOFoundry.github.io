---
layout: faq
title: Permissible content
---

This FAQ is about the content of the various fields in your ontology metadata file. Instructions on how to edit that file is covered by the FAQ <a href="{{site.baseurl}}faq/how-do-i-edit-metadata.html">How do I edit the metadata for my ontology?</a>

NOTE: In the instructions below, items in angle brackets--including the brackets <> themselves--should be replaced by the appropriate content.

## What can I put in the 'publications' field?
Allowed number of entries: *any*<br>
Each entry under this field should have one 'id' subfield and one 'title' subfield with content as indicated:
- id: \<cited reference> The cited reference must take the form of a URI (e.g., https://...") that points to one of the following permitted resources: PubMed, PubMed Central, and the Digital Object Identifier (DOI) service. Note that preprint servers such as arXiv, bioRxiv, medRxiv, and ChemRxiv--as well as alternative hosting platforms such as Zenodo and FigShare--can still be used, but not directly. For example, instead of a direct link to Zenodo such as  https://zenodo.org/record/6685957, the equivalent DOI record https://doi.org/10.5281/zenodo.6685957 should be used. Links to Semantic Scholar (https://www.semanticscholar.org) or CEUR-WS (http://ceur-ws.org/) are not permitted. As an alternative, the Zenodo platform can be used to upload content that does not have a home in any of the permitted resources.

- title: <title of cited reference> Technically this is a free-text field, but best practice is to use the title of the publication cited under the 'id' subfield.
