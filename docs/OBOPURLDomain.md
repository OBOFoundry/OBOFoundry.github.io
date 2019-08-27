---
layout: doc
id: OBOPURLDomain
title: OBO_PURL_Creation
---
# Background #

Every ontology in OBO has a PURL, each version has a PURL, and every class also gets a PURL. The PURLs for ontologies can be found on individual ontology home pages.

The [OBO ID Policy](http://www.obofoundry.org/docs/Policy_for_OBO_namespace_and_associated_PURL_requests.html) describes the requirements and process for requesting a new PURL.

For technical details of how the OBO PURL system works, and the format of individual purls, refer to https://github.com/OBOFoundry/purl.obolibrary.org/.

# SOP for new PURL creation #

This SOP is intended for use by the OBO Foundry Technical Working Group. If you are an ontology developer wanting to request a new PURL, please see the [PURL Request Guidelines](http://www.obofoundry.org/docs/Policy_for_OBO_namespace_and_associated_PURL_requests.htm). Savvy users may follow some of these steps to create their own ontology metadata files and then make a pull request, following the two week period of public comment.

## Prerequisites ##
1. Someone has requested a new PURL, following the [PURL Request Guidelines](http://www.obofoundry.org/docs/Policy_for_OBO_namespace_and_associated_PURL_requests.htm), i.e. they have already sent an email to [obo-discuss](mailto:obo-discuss@googlegroups.com) and created an issue on the [tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues).

## PURL request review process ##
1. All members of the OBO community should respond to requests on obo-discuss as appropriate. This is particurly important if the new resource overlaps with an ontology you work on.
1. Review any new or outstanding PURL requests at the start of each OBO Operations Committee meeting. Ideally, this should happen within two weeks of the issue being created.
1. If there are any concerns, one person on the OBO ops call is responsible for reaching out to the requestor to try to address them
1. If the request is rejected, notify the requestor as soon as possible. Any rejection should include steps to bring the ontology more into line with OBO principles. There should generally be some discussion before a rejection, except in the case of a bogus request.
1. If the request is accepted, proceed to PURL creation and registration in the OBO Library.

## PURL creation ##
1. PURLs are configured automatically using scripts to translate a YAML configuration file for each ontology into the needed Apache configuration. Code for this process is at https://github.com/OBOFoundry/purl.obolibrary.org.
1. To create a new PURL, create a new YAML file, as described fully at https://github.com/OBOFoundry/purl.obolibrary.org/blob/master/README.md.
1. If the ontology was created using the [Ontology Development Kit](https://github.com/INCATools/ontology-development-kit), the required YAML file will be created and stored under src/metadata.
1. Otherwise, the YAML file can be created manually, or by copying and editing the file for an existing ontology.

## Ontology registration ##
1. In order for the ontology to be displayed on the [OBO Foundry website](http://www.obofoundry.org/), and ontology metadata file in markdown (.md) must be created in the [OBO Foundry repo](https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/ontology).
1. If the ontology was created using the [Ontology Development Kit](https://github.com/INCATools/ontology-development-kit), the required metadata file will be created and stored under src/metadata.
1. Otherwise, the metadata file can be created manually, or by copying and editing the file for an existing ontology.


