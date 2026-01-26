---
layout: doc
permalink: /roles/nor-manager
title: New Ontology Request (NOR) Manager
---

The New Ontology Request (NOR) Manager has these basic duties:

1. Receiving `new ontology` requests on the OBO Foundry GitHub issues tracker and acknowledging the receipt
2. Verifying that the submitted ontology meets the OBO Foundry technical quality criteria by:
    1. Manually reviewing the ontology’s core technical features
    2. Registering the ontology in the OBO New Ontology Request (NOR) Dashboard and keeping the entry up to date
    3. Assisting the ontology requestor in addressing issues required to satisfy the technical quality criteria
4. Assigning a provisional reviewer from the OBO Operations Committee
5. Removing the accepted ontology from the NOR Dashboard upon acceptance
6. Maintaining the OBO Duty Rotation Table

## Receiving new ontology requests on OBO and acknowledging the receipt

- The NOR Manager MUST actively listen to issues on the [OBOFoundry GitHub issues tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues).

- When a new ontology request is received, and the wrong issue template was used, the NOR Manager must inform the NOR requestor to use the correct issue template and close the wrongly submitted issue with the following message:
  
  ```markdown
  Dear @GITHUBNAME,
  
  Thank you for your submission. 
  However, the wrong issue template has been used. Please make sure to follow the [New Ontology Submission Instructions](https://obofoundry.org/docs/NewOntologyRegistrationInstructions.html) and use the [New Ontology Request issue template](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?assignees=&labels=new+ontology&template=new-ontology.yml&title=Request+for+new+ontology+%5BNAME%5D).
  Thank you.
  ```

- When a valid NOR request is received the NOR Manager acknowledges the receipt with the following message:
  
  ```markdown
  Dear @GITHUBNAME,
  
  Thank you for your submission. The review will be executed as a two stage process: 
  - First, you will have to pass [OBO NOR Dashboard](https://obofoundry.org/obo-nor.github.io/dashboard/index.html). Pass means that no check _apart from `Users` and `Versioning` may be red_.
  - After you have successfully passed the Dashboard you will be assigned an OBO Operations committee member to review the ontology. _The assigned reviewer is to be considered the final arbiter of requirements_; look to that reviewer's guidance regarding which suggestions made by other reviewers must be done, which suggestions are simply good to do but not required, and which should not be done.
  
  Usually, the review will result in an opportunity for you to improve the ontology. When the reviewer believes the ontology is ready for presentation to the OBO Operations Committee, they will present your ontology during an OBO Operations Call. This gives other members of the committee the opportunity to assess your work.
  
  When a decision is reached by the committee you will be informed here on the issue tracker. The process can take any number of weeks or months, depending on the case at hand.
  Please let us know about any reasons you might have for increased urgency.
  
  You will be informed once your ontology is loaded in the OBO NOR Dashboard.
  
  Good luck!
  ```

- The NOR Manager must ensure that the requestors use the proper communication channels with the OBO community:
  
  - Make sure that the requestors have joined and send an appropriate email to the obo-discuss mailing list (see the [FAQ](https://obofoundry.org/faq/how-do-i-register-my-ontology.html)). If they have not, point them to the instructions and ask them to do so.
  - Invite the requestors (using the email listed in the metadata) to the OBO Foundry Slack space (using the `Slack->Invite people to obo-community` menu, adding the email provided.

## Verifying that the submitted ontology meets the OBO Foundry technical quality criteria

### Manually reviewing the ontology’s core features

Until sufficiently reliable automated checks are available, the NOR Manager shall perform a set of manual checks to ensure that the submitted artefact complies with the OBO Foundry pre-registration checklist. These checks include, but are not limited to, the following:

- **Valid artefact**: Verify that the submitted ontology opens without errors in Protégé.

- **URIs**: Verify that all URIs use `https` and conform to the OBO Foundry identifier format  
  ([OBO Foundry ID policy](http://obofoundry.org/id-policy)):  
  `http://purl.obolibrary.org/obo/ONTOLOGY_`

- **Definitions**: Verify that the ontology’s primary, originally defined classes are provided with textual definitions.

- **Properties**: Verify that object, data, and annotation properties are reused from authoritative sources (e.g. the Relation Ontology and OMO) wherever possible.

- **Release artefacts**: Verify that release artefacts are clearly identified and that at least one release file is provided which:
  - includes a version IRI,
  - includes a `dc:license` annotation, and
  - is serialised in RDF/XML.  
  Additionally, verify that a “base” release is provided alongside the main release and that this base release **does not include imported terms**.

### Including the ontology into the OBO New Ontology Request (NOR) Dashboard and updating the dashboard

The OBO NOR Dashboard is managed here: https://github.com/OBOFoundry/obo-nor.github.io.

Integrating the submitted ontology into OBO dashboard means simply adding a new record into the `ontologies->custom` subsection
of the [dashboard config file](https://github.com/OBOFoundry/obo-nor.github.io/blob/master/dashboard-config.yml). Only information explicitly mentioned in the New Ontology Request should be used.  
NOTE: 

> **All modifications on obo-nor.github.io repository MUST be done via pull requests and NOT via direct commits on the master branch.  
> The /workflow/dahsboard.yml file must indicate the GitHubID of the actual NOR manager as assignee.**  

Every update (adding or removing an ontology) should proceed as follows:  

1. Creation of a Pull Request (PR) for modification of the [dashboard config file](https://github.com/OBOFoundry/obo-nor.github.io/blob/master/dashboard-config.yml) for adding or deleting record in the `ontologies->custom` section of the file.
2. Once the previous PR is merged, it triggers the *Update dashboard run* [GitHub action](https://github.com/OBOFoundry/obo-nor.github.io/blob/master/.github/workflows/dashboard.yml). This action can also be triggered manually [here](https://github.com/OBOFoundry/obo-nor.github.io/actions/workflows/dashboard.yml) with the `run workflow` button.
3. Once the run is complete, a new PR named `Update dashboard run` is created. Manually check the diff, especially the /dashboard/dahsboard-result.yml file for inconsistencies.
4. Finally, merge the `Update dashboard run` PR. This PR should always be reviewed by the NOR Manager and not be automatically merged into the main branch as part of the GitHub action.

In addition, the *Update dashboard run* action is automatically triggered on Monday mornings and steps 3 and 4 must be performed afterward.

### Supporting the New Ontology requestor to pass the OBO Dashboard

For many New Ontology requestors it is not always easy to interpret the warnings on the OBO Dashboard. The NOR Manager is responsible for supporting the requestor interpreting the dashboard (but _not_ to fix the problems). There is no need to dig deep into the ontologies to diagnose problems - that is the requestors responsibility - but pointing to documentation like the [OBO Foundry Principles](https://obofoundry.org/principles/fp-000-summary.html) may be necessary.

During this process, all discussions between the requestors and the NOR manager must take place in the [OBO Issue Tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues) in the NOR issue created by the requestor.

## Assigning a provisional reviewer from the OBO Operations Committee

If and only if the requested ontology passes the dashboard, i.e. no more "red" exists aside from the `Usage` column, the NOR manager assigns the next available reviewer from the ['OBO Operations Members' sheet in the OBO Duty Rotation Table](https://docs.google.com/spreadsheets/d/19GrEWVnpxjnrig0iYUOiUvsZ0JDbprMh1USnRb-SXtg/edit). The reviewer is assigned by 

1. Adding them to the ['Ontology Review Rotation' sheet in the OBO Duty Rotation Table](https://docs.google.com/spreadsheets/d/19GrEWVnpxjnrig0iYUOiUvsZ0JDbprMh1USnRb-SXtg/edit)
2. Assigning the NOR GitHub issue to the reviewer
3. Announcing the reviewer assignment to the OBO Operations Technical Working Group Liaison to include in their report at the next OBO Operations meeting.

## Removing the accepted ontology from the NOR Dashboard upon acceptance

When the ontology is accepted, the OBO NOR reviewer needs to make sure that the accepted ontology is removed from the OBO NOR Dashboard.

Note 29.11.2022: There is a [work in progress](https://github.com/OBOFoundry/obo-nor.github.io/pull/23) which can deal with this step automatically, but the responsibility still stays with the OBO NOR Manager.

## Maintaining the OBO Duty Rotation Table

The OBO Duty Rotation Table is a Google spreadsheet available [here](https://docs.google.com/spreadsheets/d/19GrEWVnpxjnrig0iYUOiUvsZ0JDbprMh1USnRb-SXtg/edit).
When a new member is added to the OBO Operations Committee, the OBO NOR reviewer should add the new member's name to this table. Similarly, former members should be removed from the table. The list of current OBO Operations members is maintained in the file [operations.yml](https://github.com/OBOFoundry/OBOFoundry.github.io/blob/master/_data/operations.yml).

In addition, when a new ontology has been submitted, it should be added to the ['Ontology Reviewers' tab](https://docs.google.com/spreadsheets/d/19GrEWVnpxjnrig0iYUOiUvsZ0JDbprMh1USnRb-SXtg/edit?gid=1683009411#gid=1683009411) in the OBO Duty Rotation spreadsheet.
