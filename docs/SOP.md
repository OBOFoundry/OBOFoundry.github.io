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
- [Changing ontology metadata in the registry](#META)

<a name="NOR"></a>

### New Ontology Requests (NOR)

1. When receiving a new ontology request (NOR), the OBO dashboard administrator should thank the submitter for their submission.
1. The OBO dashboard administrator adds the new submission to the NOR dashboard, which is deployed at https://obofoundry.github.io/obo-nor.github.io/
1. After the dashboard is run, the OBO dashboard administrator informs the submitter about the need to fix the issues revealed by the dashboard, noting this is not part of the review itself, just a precursor, and that upon completion, a liaison will be assigned.
1. At the next OBO Foundry Operations Committee conference call (hereafter, "Operations call"), a liaison is selected to be responsible for the issue. This liaison becomes familiar with the new ontology and rallies the appropriate people to provide feedback.
1. At the next Operations call after that one, the liaison presents the NOR to the OBO Foundry Operations Committee and answers questions. In most cases, the information provided will be sufficient to either grant or refuse the prefix request. In some cases, the committee may choose to postpone its decision to require some clarification and fixes from the submitter.
   The liaison MUST be present at the Operations call in order for the NOR case to be discussed. If the liaison does not participate for 2 consecutive Operations calls, the chair of the second call emails the liaison to request a statement confirming the ability to continue as liaison. If the liaison does not participate in 3 consecutive Operations calls and did not respond to the email above, a new liaison is assigned during that third call.

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
