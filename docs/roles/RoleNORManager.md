---
layout: doc
permalink: /roles/nor-manager
title: OBO Role: New Ontology Request (NOR) Manager
---

The New Ontology Request (NOR) Manager has these basic duties:

1. Receiving `new ontology` requests on OBO and acknowledging the receipt
2. Including the ontology in the OBO New Ontology Request (NOR) Dashboard
3. Supporting the New Ontology requestor to pass the OBO Dashboard
4. Assigning a provisional reviewer from the OBO Operations Committee
5. Removing the accepted ontology from the NOR Dashboard upon acceptance


### Receiving `new ontology` requests on OBO and acknowledging the receipt

- The NOR Manager MUST actively listen to issues on the [OBO Issue Tracker](https://github.com/OBOFoundry/OBOFoundry.github.io/issues).
- When a new ontology request is received, and the wrong issue template was used, the New Ontology Request (NOR) Manager must inform the NOR requestor to use the correct issue template and close the wrongly submitted issue.
- When a valid NOR request is received the NOR Manager acknowledges the receipt with the following message:
    ```markdown
    Dear @GITHUBNAME,
    
    Thank you for your submission. The review will be executed as a two stage process. 
    First, you will have to pass [OBO NOR Dashboard](https://obofoundry.org/obo-nor.github.io/dashboard/index.html). Pass means that no check _apart from `Users` may be red_.
    After you have successfully passed the Dashboard you will be assigned an OBO Operations committee member to review the ontology.
    
    Usually, the review will result in an opportunity for you to improve the ontology.
    When the reviewer believes the ontology is ready for presentation to the OBO Operations Committee, they will present
    your ontology during an OBO Operations Call. This gives other members of the
    committee the opportunity to assess your work.
    
    When a decision is reached by the committee you will be informed here on the issue tracker.
    The process can take any number of weeks or months, depending on the case at hand.
    Please inform us about any reasons you might have for increased urgency.
    
    You will be informed once your ontology is loaded in the OBO NOR Dashboard.
    
    Good luck.
    ```

### Including the ontology into the OBO New Ontology Request (NOR) Dashboard

The OBO NOR Dashboard is managed here: https://github.com/OBOFoundry/obo-nor.github.io.

Integrating the submitted ontology into OBO dashboard means simply adding a new record into the `ontologies->custom` subsection
of the [dashboard config file](https://github.com/OBOFoundry/obo-nor.github.io/blob/master/dashboard-config.yml). Only information explicitly mentioned in the New Ontology Request should be used.

### Supporting the New Ontology requestor to pass the OBO Dashboard

For many New Ontology requestors it is not always easy to interpret the warnings on the OBO Dashboard. The NOR Manager is responsible for supporting the requestor interpreting the dashboard (but _not_ to fix the problems). There is no need to dig deep into the ontologies to diagnose problems - that is the requestors responsibility - but pointing to documentation like the [OBO Foundry Principles](https://obofoundry.org/principles/fp-000-summary.html) may be necessary.

### Assigning a provisional reviewer from the OBO Operations Committee

If and only if the requested ontology passes the dashboard, i.e. no more "red" exists aside from the `Usage` column, the NOR manager assigns the next available reviewer from the ['OBO Operations Members' sheet in the OBO Duty Rotation Table](https://docs.google.com/spreadsheets/d/19GrEWVnpxjnrig0iYUOiUvsZ0JDbprMh1USnRb-SXtg/edit). The reviewer is assigned by 

1. Adding them to the ['Ontology Review Rotation' sheet in the OBO Duty Rotation Table](https://docs.google.com/spreadsheets/d/19GrEWVnpxjnrig0iYUOiUvsZ0JDbprMh1USnRb-SXtg/edit)
2. Assigning the NOR GitHub issue to the reviewer
3. Announcing the reviewer assignment to the OBO Operations Technical Working Group Liaison to include in their report at the next OBO Operations meeting.

### Removing the accepted ontology from the Dashboard upon acceptance

When the ontology is accepted, the OBO NOR reviewer needs to make sure that the accepted ontology is removed from the OBO NOR Dashboard.

Note 29.11.2022: There is a [work in progress](https://github.com/OBOFoundry/obo-nor.github.io/pull/23) which can deal with this step automatically, but the responsibility still stays with the OBO NOR Manager.
