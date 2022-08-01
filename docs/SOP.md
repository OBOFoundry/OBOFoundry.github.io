---
layout: doc
id: SOP
title: Standard Operating Procedures
---
# Standard Operating Procedures

**Description**:  
 
This document contains standard operating procedures (SOPs) for the OBO Foundry Operations Committee, and is intended for internal use only.

## SOPs
- [New Ontology Requests](#NOR)
- [Reviewing Ontologies for OBO Membership](#ROOM)
- [Changing ontology metadata in the registry](#META)

<a name="NOR"></a> 
### New Ontology Requests (NOR) 

1. When receiving a new ontology request (NOR), the OBO dashboard administrator should thank the submitter for their submission.
1. The OBO dashboard administrator adds the new submission to the NOR dashboard, which is deployed at https://obofoundry.github.io/obo-nor.github.io/
1. After the dashboard is run, the OBO dashboard administrator informs the submitter about the need to fix the issues revealed by the dashboard, noting this is not part of the review itself, just a precursor, and that upon completion, a liaison will be assigned.
1. At the next OBO Foundry Operations Committee conference call (hereafter, "Operations call"), a liaison is selected to be responsible for the issue. This liaison becomes familiar with the new ontology and rallies the appropriate people to provide feedback.
1. At the next Operations call after that one, the liaison presents the NOR to the OBO Foundry Operations Committee and answers questions. In most cases, the information provided will be sufficient to either grant or refuse the prefix request. In some cases, the committee may choose to postpone its decision to require some clarification and fixes from the submitter.
The liaison MUST be present at the Operations call in order for the NOR case to be discussed. If the liaison does not participate for 2 consecutive Operations calls, the chair of the second call emails the liaison to request a statement confirming the ability to continue as liaison. If the liaison does not participate in 3 consecutive Operations calls and did not respond to the email above, a new liaison is assigned during that third call.

<a name="ROOM"></a> 
### Reviewing Ontologies for OBO Membership (ROOM) 

The goal of this SOP is to provide a clear set of criteria to be checked for the manual review of an ontology in response to a request to register a new ontology with the OBO Foundry. It is expected that a programmatic review using the Dashboard has already been done and the submitters have addressed those problems found. The purpose of the manual review is to check the ontology for issues that the Dashboard review does not cover. In order for this review to be relatively quick (~ 2 hours), a sample of terms/axioms should be checked; the reviewer is not expected to review all the terms/axioms.

Check the following and provide a brief summary in the tracker issue for the new ontology request. All items of feedback must be provided using GitHub checklist syntax (`- [ ] TODO`) in order to track how far they are being addressed. Addressable issues identified as part of the review should be added to the new ontology’s issue tracker. 
1. Ontology scope. The new ontology must present some use cases where it will be relevant to life-sciences.  Was the ontology developed using expert input or trusted scientific sources representative of the consensus in its target domain of knowledge? If the ontology was developed for a very specific purpose or community, representation and consensus need not be broad; however, this scope should be clearly stated.
2. Terms with the new ontology prefix. The new terms provided by the ontology must not already be available in an available OBO Foundry ontology. There must not be a term with the same label available. There should not be another OBO Foundry ontology whose scope covers those terms and if there is there should be some evidence of contacting that OBO Foundry ontology.
3. Correct use of imported terms. Does the ontology accurately - in both a technical and substantive sense - reuse terms from other OBO ontologies?
If terms are reused, is there textual and (where relevant) axiomatic definition preserved?
Are imported terms in appropriate hierarchies? That is, has the import of the term preserved its upper-level alignment?
Are any additional axioms used for these terms correct in both a technical (e.g. passes reasoning) and substantive sense?
4. Basic review of axiomatic patterns:
Are existential restrictions used correctly? Typical mistakes include “R some (A and B and C)” to mean “(R some A and R some B and R some C)”
Are axioms generally highly complex? If so, we should review a handful to ensure they are as intended.
5. Appropriate use of object properties. Examples of incorrect usage include those based on some interpretation of the label of the object property but not actually fitting the property definition or domain and range. 
6. Responsiveness to fixing changes. A willingness to fix any identified issues must be demonstrated.

<a name="META"></a> 
### Changing ontology metadata in the registry

In general, the metadata record of an ontology in the OBO Foundry metadata registry ([example](https://github.com/OBOFoundry/OBOFoundry.github.io/blob/master/ontology/go.md)) is managed and curated by the ontology team that is responsible for the respective ontology. However, as an open data organisation, the OBO Foundry does accept proposals by any member of the community to change this metadata. Such change proposal can include fixing typos, adding a tag, adding a publication where it was missed. The following SOP exists to ensure that these changes are not performed without the knowledge of the responsible ontology team.

1. Any member of the community (OBO Foundry or otherwise) may propose a change in the form of a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).
2. This pull request is reviewed by a member of the OBO Foundry operations committee and may be rejected. 
3. The OBO Foundry operations committee member MUST then tag the listed contact person using their GitHub handle on the pull request requesting a review (initial request for feedback).
4. After two weeks without activity, an OBO Foundry operations committee member will update the pull request and announce a prospective merge date no earlier than two weeks in the future.
5. After at least 4 weeks have passed since the initial request for review:
   - If the change pertains to one of the following metadata fields, an OBO Foundry operations committee member MUST send an email to the listed contact with a link to the pull request: `activity_status`, `contact`.
   - If the change pertains to any change other than the above, the OBO Foundry operations committee member MAY merge the pull request at their own discretion.
6. If at least 3 months have passed after the initial request for feedback, and the above conditions are met, any OBO Foundry operations committee member MAY merge the pull request at their own discretion.

For a discussion on this SOP, see [here](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1848).
