---
layout: doc
title: Standard Operating Procedures
---

This document contains standard operating procedures (SOPs) for the OBO Foundry Operations Committee, and is intended for internal use only.

## SOPs

- [New Ontology Requests](#NOR)
- [Reviewing Ontologies for OBO Membership](#ROOM)
- [Ontology Acceptance Email](#OAE)
- [Changing ontology metadata in the registry](#META)
- [Reviving obsolete, orphaned, or inactive ontologies](#REACTIVATION)
- [Becoming a member of the OBO Operations Committee](#OPS_MEMBER)
- [Chairing an OBO Operations Committee meeting call](#OPS_CHAIR)

<a name="NOR"></a>

### New Ontology Requests (NOR)

1. When receiving a new ontology request (NOR), the NOR Manager should thank the submitter for their submission. In addition, the NOR Manager should assist NOR submitters in understanding the NOR process and passing the NOR review during the whole process.
2. The NOR Manager adds the new submission to the NOR dashboard, which is deployed at https://obofoundry.github.io/obo-nor.github.io/
3. In addition to the dashboard, the NOR Manager could need to manually review that the submitted ontology adheres to the OBO foundry [principles](http://obofoundry.org/principles/fp-000-summary.html). For example, IRIs and object properties need to be reviewed manually pending the implementation of new automated checks. 
4. After the dashboard is run and the manual review is done, the NOR Manager informs the OBO Foundry Operations Committee of any issues for consideration. Until all issues are resolved or the NOR request is rejected, the NOR Manager acts as a liaison between the OBO Foundry Operations Committee and the NOR submitter.
5. Once the new ontology passes the review, the NOR manager assigns the next available reviewer from the OBO operation members.
6. Finally, when the ontology is fully accepted, the NOR manager remove the ontology from the OBO NOR dashboard.

New Ontology Requests SOP are fully documented [here](/roles/nor-manager). 


<a name="ROOM"></a>
### Reviewing Ontologies for OBO Membership

The goal of this SOP is to provide a clear set of criteria to be checked for the manual review of an ontology in response to a request to register that new ontology with the OBO Foundry. It is expected that a programmatic review using the Dashboard has already been done and the submitters have addressed any problems found. The purpose of the manual review is to check the ontology for issues that the Dashboard review does not cover. A sample of terms/axioms should be checked. In order for this review to be relatively quick (~ 2 hours), the reviewer is not expected to review all the terms/axioms.

Check the following and provide a brief summary in the tracker issue for the new ontology request. All items of feedback must be provided using GitHub checklist syntax (`- [ ] TODO`) in order to track how far along they are in being addressed. Addressable issues identified as part of the review should be added to the new ontology’s issue tracker.
1. Ontology scope. The new ontology must present use cases demonstrating its relevance to the life sciences.  Was the ontology developed using expert input or trusted scientific sources representative of the consensus in its target domain of knowledge? If the ontology was developed for a very specific purpose or community, representation and consensus need not be broad; however, this scope should be clearly stated.
2. Terms with the new ontology prefix. 
All new terms MUST follow the [OBO identifier scheme](http://obofoundry.org/id-policy) (often they are accidentally written wrongly, e.g. using https instead of http). 
There MUST NOT be a term with the same meaning available in another OBO Foundry ontology, ie there must not be a term referring to a concept that already exists in another OBO Foundry ontology (whether or not the label is identical). There SHOULD NOT be another OBO Foundry ontology whose scope covers any of the new terms. In the event that these conditions cannot be fulfilled, justification(s) MUST be provided. Such justification(s) include:
    - the demonstration that these terms are actually not the same (this happens when term meaning/concept is ambiguous); or
    - the other OBO Foundry ontology (for which the terms were in scope) was contacted and rejected the request for adding new terms in scope for that ontology.
3. Correct use of imported terms. Does the ontology accurately reuse terms from other OBO ontologies?
Are imported terms in appropriate hierarchies? That is, has the import of the term preserved its upper-level alignment?
Are any additional axioms used for these terms correct in both a technical (e.g. passes reasoning) and substantive sense?
4. Basic review of axiomatic patterns:
Are existential restrictions used correctly? Typical mistakes include “R some (A and B and C)” to mean “(R some A and R some B and R some C)”
Are axioms generally highly complex? If so, we should review a handful to ensure they are as intended.
5. Appropriate use of [object properties](https://www.w3.org/TR/2004/REC-owl-semantics-20040210/#owl_ObjectProperty). Examples of incorrect usage include those based on some interpretation of the label of the object property but not actually fitting the property definition or domain and range. A typical example of incorrect usage is R some (A and B and C) to mean R some A and R some B and R some C.
6. Responsiveness to fixing changes. A willingness to fix any identified issues during the review must be demonstrated. Issues expected to be addressed should be added using GitHub checklist syntax (`- [ ] TODO`) in the GitHub issue. The time limit for addressing these is 2 months; a longer period should be requested if needed.

Note that the NOR Manager (see [roles overview](https://obofoundry.org/roles/overview)) can help assist NOR submitters in understanding the NOR process and passing the NOR Dashboard, as well as later assisting successful NOR submitters in making registry metadata and PURL pull requests

<a name="OAE"></a>
## Ontology Acceptance/Rejection Decision
Once the reviewer has decided whether a new ontology meets the requirements, they present their review and recommendation to the OBO Ops committee.
The committee can ask the reviewer for clarifications, and then the people on the call make the decision about whether to accept the ontology.
The decision is made by “consensus” on the call: i.e., no one objects strenuously.
No quorum (minimum number of attendees) on the call is required.

### Ontology Acceptance Notification

Once a new ontology has been accepted, the ontology owner should be notified by the ontology reviewer, both in the ticket and also by via email (they were required to supply their email address as part of their new ontology request),
ccing obo-discuss & obo-operations-committee.
The following template should be used to let the ontology owner know that their ontology was accepted, and informing them about the next steps they should take:

"Thank you again for your ontology submission to the OBO Foundry. We are happy to inform you that your ontology (YOURID) has been accepted following discussion in the OBO Operations Committee meeting, YYYY-MM-DD. Before we can add it to the OBO ontology registry you need to complete the following steps.

Create a metadata record for your ontology to be included in the registry:
1. Create a new file in https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/ontology, called YOURID.md (there is an “Add file” button in the top right).
2. Obtain the already curated metadata that relates to your ontology from https://github.com/OBOFoundry/obo-nor.github.io/blob/master/dashboard-config.yml (you'll need to scroll down to locate yours; it will have your prefix in the " - id:" field.)
3. Create a pull request to add the metadata record. This pull request should include a link to this issue (the New Ontology Request issue).

Here is an example record for the PATO ontology: https://github.com/OBOFoundry/OBOFoundry.github.io/blob/master/ontology/pato.md?plain=1

Your metadata will be reviewed and merged by a member of the OBO Foundry Operations Committee. Permissible content for fields is being documented [here](https://obofoundry.org/faq/permissible-metadata-content.html).

To create a PURL registry entry for your ontology:
1. Go to https://github.com/OBOFoundry/purl.obolibrary.org/tree/master/config, click “Add file” and add a file named YOURID.yml.
2. Add the desired configuration.
3. Make a pull request with a link to this issue
See here for an example of a PURL yml file: https://github.com/OBOFoundry/purl.obolibrary.org/blob/master/config/pato.yml "

### Ontology Rejection Notification
If it is determined that a submitted ontology does not meet the requirements for acceptance in the OBO Foundry, and the submitter has been informed of the issues and at least two months have elapsed and they have not corrected the problems,
the reviewer can recommend to the OBO Operations Committee that the ontology should be rejected. The decision to reject an ontology is to be made by consensus from those on the call where the review is presented.
The reviewer should notify the ontology owner in the ticket and also by email, ccing obo-operations-committee (but maybe not obo-discuss?).

(Should there be a template for the rejection notice?)

<a name="META"></a>
## Changing ontology metadata in the registry

In general, the metadata record of an ontology in the OBO Foundry metadata registry ([example](https://github.com/OBOFoundry/OBOFoundry.github.io/blob/master/ontology/go.md)) is managed and curated by the ontology team that is responsible for the respective ontology. However, as an open data organisation, the OBO Foundry does accept proposals by any member of the community to change this metadata. Such change proposal can include fixing typos, adding a tag, adding a publication where it was missed. The following SOP exists to ensure that these changes are not performed without the knowledge of the responsible ontology team.

1. Any member of the community (OBO Foundry or otherwise) may propose a change in the form of a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).
2. This pull request is reviewed by a member of the OBO Foundry operations committee and may be rejected.
3. To prevent undue delays to website development, if the proposed change affects merely the presentation of the web page (for example, information is moved from one section of the website to another, URLs are changed from http to https, there is a change in the display/formatting of a page, typos) the OBO Foundry Operations Committee member may choose to accept the pull request without waiting for further review. In such case, the following steps may be ignored.
4. The OBO Foundry operations committee member MUST then tag the listed contact person using their GitHub handle on the pull request requesting a review (initial request for feedback).
5. After two weeks without activity, an OBO Foundry operations committee member will update the pull request and announce a prospective merge date no earlier than two weeks in the future.
6. After at least 4 weeks have passed since the initial request for review:
   - If the change pertains to one of the following metadata fields, an OBO Foundry operations committee member MUST send an email to the listed contact with a link to the pull request: `activity_status`, `contact`.
   - If the change pertains to any change other than the above, the OBO Foundry operations committee member MAY merge the pull request at their own discretion.
7. If at least 3 months have passed after the initial request for feedback, and the above conditions are met, any OBO Foundry operations committee member MAY merge the pull request at their own discretion.

For a discussion on this SOP, see [here](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/1848).

<a name="REACTIVATION"></a>

## Reactivating obsolete, orphaned, or inactive ontologies

To mark ontologies that were marked as either obsolete, orphaned, or inactive as active again, we follow this process. 
Currently, these are the required steps:

1. A person involved in developing the ontology (usually the contact person) makes a pull request (PR) on the metadata file with the desired change in status. The PR must include evidence to demonstrate new activity, for example by referring to recently-closed issues (we will provide more detailed guidelines as this SOP matures). If the PR was made by someone other than the contact person, or if the contact person has changed, the contact should be tagged in the PR so that the proper followup can be done. The contact person then has one month to verify that the change is desired.
1. The ontology is added to the NOR dashboard to identify potential problems. Fixing basic issues revealed by the dashboard will be considered additional evidence that the ontology is indeed active.
1. The OBO Operations committee assigns a status change reviewer during the next call to analyse the evidence for the change. Only the evidence matters - no need to collect more evidence in favor of the status change.
1. The status change reviewer presents the arguments for and against the status change at an OBO Operations call.
1. If there is no significant objection, the status change is enacted by merging the pull request.

<a name="OPS_MEMBER"></a>

## Becoming a member of the OBO Operations Committee
The current processes of nomination, acceptance and onboarding are described [here](https://obofoundry.org/docs/NewOBOFC.html).

<a name="OPS_CHAIR"></a>

### Chairing an OBO Operations Committee meeting call

***Please note that as of 2023-01-10, OBO Operations meeting minutes are now viewable by the public.***

#### Before the call (a day or two in advance):

1. Prepare a stub in the OBO Operations Committee (OFOC) [rolling agenda](https://docs.google.com/document/d/1aka4i6R89i04IYPS7CyzItQPOyb3IgtW4m75G475qcc/edit) with the following <b>Repeating Agenda Items</b>:
     1. Get volunteers to sign up to lead upcoming meetings (if needed)
     2. Review [new ontology requests](https://github.com/OBOFoundry/OBOFoundry.github.io/labels/new%20ontology)
     3. Report from Editorial Working Group (EWG) (Darren)
     4. Report from Technical Working Group (TWG) (Ray)
     5. Review additional [open issues](https://github.com/OBOFoundry/OBOFoundry.github.io/labels/attn%3A%20OFOC%20call) and [pull requests](https://github.com/OBOFoundry/OBOFoundry.github.io/pulls?q=is%3Apr+is%3Aopen+label%3A%22attn%3A+OFOC+call%22) that are labeled "attn: OFOC call"

2. Check the issues labeled ["attn:OFOC call"](https://github.com/OBOFoundry/OBOFoundry.github.io/labels/attn%3A%20OFOC%20call) found at the OBO foundry github repository. Pick one or two open issues you deem important and put them towards the end of the stub agenda, after the Working Group reports and before the review of additional open issues.
3. Send an email to obo-operations-committee @ googlegroups.com (not obo-discuss!) with the subject "OBO Operations Committee meeting" and the following text given between quotes
(note that for safety, the Zoom URL is not included in this document -- please refer to the calendar invite or Slack):<br>
   <hr>
   "I am chairing this week’s OFOC meeting. The Zoom link is [...].<br>

   Please review
      - [new ontology requests](https://github.com/OBOFoundry/OBOFoundry.github.io/labels/new%20ontology),
      - [open pull requests](https://github.com/OBOFoundry/OBOFoundry.github.io/pulls), and
      - [recent tracker items](https://github.com/OBOFoundry/OBOFoundry.github.io/issues?q=is%3Aopen).

   Please feel free to add agenda items to [https://docs.google.com/document/d/1qhLFQL5IzTMUIBOtxJ5AqaEHcOCOQgNeXfvAb5O5P0A/edit](https://docs.google.com/document/d/1qhLFQL5IzTMUIBOtxJ5AqaEHcOCOQgNeXfvAb5O5P0A/edit)."
   <hr>

#### During the call:

1. Wait until approximately 8-10 people have joined. Begin no more than 4 minutes after the hour regardless of how many people are present.
2. Share your screen to show the agenda, greet the attendees, and drive the agenda. (You don't have to show your face, but some people choose to do so. It is up to you).
3. It is important to keep the discussion on track:
   - If it appears that the group will not reach consensus after long discussion of a particular item, you (or one of the primary participants in the discussion) should politely summarize the discussion and call for agreement on next steps so that the next item on the agenda can be addressed.
    - Be aware that sometimes not every agenda item can be discussed in a single meeting. It is more important that the items that do get addressed are discussed fully.
4. Add notes to the agenda capturing important discussion points, summaries, decisions made, action items (with assignees), and next steps. These can be brief but it is important to capture what has been discussed and/or decided so that the group doesn’t forget. Don’t worry if it takes a little time. Make note of any new issues (or comments on existing issues) that are needed; these will be done after the call.
5. End the call on time. Don’t start new topics too close to the end or let discussions drag on after the hour.
6. Thank everyone for taking the time to attend!

#### After the call:

1. Make a pass through the minutes for the purposes of streamlining, formatting, and providing clarity.
2. Make sure that all new issues are logged on GitHub. Add comments to all GitHub issues that were discussed, as appropriate.

For a discussion on this SOP, see [here](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2043).
