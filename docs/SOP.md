---
layout: doc
id: SOP
title: Standard Operating Procedures
---

This document contains standard operating procedures (SOPs) for the OBO Foundry Operations Committee, and is intended for internal use only.

# SOPs

- [New Ontology Requests](#NOR)
- [Changing ontology metadata in the registry](#META)
- [Chairing an OBO Operations Committee meeting call](#OPS_CHAIR)

<a name="NOR"></a>

## New Ontology Requests (NOR)

1. When receiving a new ontology request (NOR), the OBO dashboard administrator should thank the submitter for their submission.
1. The OBO dashboard administrator adds the new submission to the NOR dashboard, which is deployed at https://obofoundry.github.io/obo-nor.github.io/
1. After the dashboard is run, the OBO dashboard administrator informs the submitter about the need to fix the issues revealed by the dashboard, noting this is not part of the review itself, just a precursor, and that upon completion, a liaison will be assigned.
1. At the next OBO Foundry Operations Committee conference call (hereafter, "Operations call"), a liaison is selected to be responsible for the issue. This liaison becomes familiar with the new ontology and rallies the appropriate people to provide feedback.
1. At the next Operations call after that one, the liaison presents the NOR to the OBO Foundry Operations Committee and answers questions. In most cases, the information provided will be sufficient to either grant or refuse the prefix request. In some cases, the committee may choose to postpone its decision to require some clarification and fixes from the submitter.
   The liaison MUST be present at the Operations call in order for the NOR case to be discussed. If the liaison does not participate for 2 consecutive Operations calls, the chair of the second call emails the liaison to request a statement confirming the ability to continue as liaison. If the liaison does not participate in 3 consecutive Operations calls and did not respond to the email above, a new liaison is assigned during that third call.

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

<a name="OPS_CHAIR"></a>

## Chairing an OBO Operations Committee meeting call

### Before the call (a day or two in advance):
1. Prepare a stub in the OBO Operations Committee (OFOC) [rolling agenda](https://docs.google.com/document/d/1aka4i6R89i04IYPS7CyzItQPOyb3IgtW4m75G475qcc/edit) with the following <b>Repeating Agenda Items</b>:

     1. Check for [pending members for obo-discuss](https://groups.google.com/g/obo-discuss/pending-members) 
     2. Get volunteers to sign up to lead upcoming meetings (if needed)
     3. Review [new ontology requests](https://github.com/OBOFoundry/OBOFoundry.github.io/labels/new%20ontology)
     4. Report from Editorial Working Group (EWG) (Darren)
     5. Report from Technical Working Group (TWG) (Nico)
     6. Review additional [open issues](https://github.com/OBOFoundry/OBOFoundry.github.io/labels/attn%3A%20OFOC%20call) and [pull requests](https://github.com/OBOFoundry/OBOFoundry.github.io/pulls?q=is%3Apr+is%3Aopen+label%3A%22attn%3A+OFOC+call%22) that are labeled "attn: OFOC call"

2. Check the issues labeled ["attn:OFOC call"](https://github.com/OBOFoundry/OBOFoundry.github.io/labels/attn%3A%20OFOC%20call) found at the OBO foundry github repository. Pick one or two open issues you deem important and put them towards the end of the stub agenda, after the Working Group reports and before the review of additional open issues.
3. Send an email to obo-operations-committee @ googlegroups.com (not obo-discuss!) with the subject "OBO Operations Committee meeting" and the following text given between quotes:<br>

"I am chairing this week’s OFOC meeting. The Zoom link is given in the agenda document (see below).<br>

Please review
[new ontology requests](https://github.com/OBOFoundry/OBOFoundry.github.io/labels/new%20ontology),
[open pull requests](https://github.com/OBOFoundry/OBOFoundry.github.io/pulls), and
[recent tracker items](https://github.com/OBOFoundry/OBOFoundry.github.io/issues?q=is%3Aopen).<br>

Please also add agenda items to https://docs.google.com/document/d/1aka4i6R89i04IYPS7CyzItQPOyb3IgtW4m75G475qcc/edit."

### During the call:
1. Wait until approximately 8-10 people have joined. Begin no more than 4-5 minutes after the hour regardless of how many people are present.
2. Share your screen to show the agenda, greet the attendees, and drive the agenda. (You don't have to show your face, but some people choose to do so. It is up to you).
3. It is important to keep the discussion on track: 
   1. If it appears that the group will not reach consensus after long discussion of a particular item, you (or one of the primary participants in the discussion) should politely summarize the discussion and call for agreement on next steps so that the next item on the agenda can be addressed.
   1. Be aware that sometimes not every agenda item can be discussed in a single meeting. It is more important that the items that do get addressed are discussed fully.
4. Add notes to the agenda capturing important discussion points, summaries, decisions made, action items (with assignees), and next steps. These can be brief but it is important to capture what has been discussed and/or decided so that the group doesn’t forget. Don’t worry if it takes a little time. Make note of any new issues (or comments on existing issues) that are needed; these will be done after the call.
5. End the call on time. Don’t start new topics too close to the end or let discussions drag on after the hour.
6. Thank everyone for taking the time to attend!
### After the call:
1. Make a pass through the minutes for the purposes of streamlining, formatting, and providing clarity.
2. Make sure that all new issues are logged on GitHub. Add comments to all GitHub issues that were discussed, as appropriate.

For a discussion on this SOP, see [here](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/2043).


