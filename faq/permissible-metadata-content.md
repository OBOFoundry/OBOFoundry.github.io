---
layout: faq
title: Permissible content
---

This FAQ is about what content is permissible in the metadata file.

 * To edit ontology metadata, see the FAQ <a href="{{site.baseurl}}faq/how-do-i-edit-metadata.html">How do I edit metadata</a>

## Permissible content for the 'publications' field
  -id: <URL of cited reference>
    Identifiers (e.g., CURIEs, URIs) for references to publications that appear in ontology metadata must refer to a resource that
    1) hosts its own original content and metadata, and 2) can be used to look up metadata about the corresponding publication including its title, venue, authors, etc.

    Resources like PubMed, PubMed Central, arXiv, bioRxiv, medRxiv (via DOI), and ChemRxiv (via DOI) constitute well-known first-party resources.
    Further, the Digital Object Identifier (DOI) service qualifies as a high-quality first-party resource.

    Resources like Semantic Scholar which do not host original content and loose PDF links (e.g., in http://ceur-ws.org) are not sufficient under these new standards. As an alternative, the Zenodo platform can be used to upload content that does not have a home in any of the other first-party services.

  - title: <title of cited reference>
