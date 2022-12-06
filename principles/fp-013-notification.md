---
layout: principle
id: fp-013-notification
title: Notification of Changes (principle 13)
---

Summary
-------

Ontologies SHOULD announce major changes to relevant stakeholders and collaborators ahead of release.

Purpose
-------

To maintain the reliability of an ontology for stakeholders, advance announcement of upcoming changes--as
opposed to giving after-the-fact notice (or none at all)--is crucial. Such announcement will provide stakeholders an opportunity for input on upcoming changes,
and will allow updates to any dependencies (e.g., terms, annotations, ontologies) affected by those changes.

Recommendations and Requirements
-------
Ontology owners SHOULD, in accordance with this principle, pre-announce changes to a primary group of users who actively monitor the ontology and its changes, for example, via a mailing list (ontology-specific or more general, as deemed suitable), a social media group (relevant to the ontology), or via announcements on a home page or elsewhere.

The lead time for announcements can be determined according to release lifecycles of major ontology applications and is expected to vary by domain.

Implementation
--------------

The need for notification of changes--and the time frame in which notifications are made--should be based on the granularity of the changes and their potential impact
(for example, changes to low-level terms are likely not as impactful as those to high-level terms). Types of changes that might benefit from notification include term
obsoletions, term modifications, new terms, and any others that are determined with stakeholder benefit in mind. Announcments can be concise or verbose, and
SHOULD be made a minimum of 7 days in advance of the release in which the changes take effect.

The following are possible avenues for notification:
* Submission of a GitHub ticket announcing the change
* Announcement made via social media (Twitter, Facebook, Slack, etc)
* Announcement made via general or ontology-specific mailing list
* Announcement of pending changes made as a GitHub pre-release
* Change log or release note, if published in advance

It is expected that announcements include links to where discussions or questions can be directed.

Examples
--------

- GitHub issue: https://github.com/geneontology/go-announcements/issues/275
- Social media (Twitter): https://twitter.com/diseaseontology/status/1301907848625033216
- Mailing list announcement (general): https://groups.google.com/g/obo-discuss/c/RrCF5f9FRC4/m/nEVwLqN5CQAJ
- Mailing list announcement (ontology-specific): https://groups.google.com/g/obi-users/c/wweskCfHbSc
- GitHub pre-release: https://github.com/obi-ontology/obi/pull/1558
- Advance release note: https://proconsortium.org/download/release_55.0/pro_release_note.txt

Counter-Examples
----------------

The following mechanisms, while useful, do not fulfill the recommendations herein since they occur concurrently with the changes of interest:

- Announcement of changes in a release note when that note is for the same release as that in which the change first appears
- A change log that is not published in advance

Criteria for Review
-------------------

Notification of changes SHOULD be published prior to a new release version of the Ontology. The period between publishing the changes
and the release date must be no less than 7 days but can be longer (based upon agreement between ontology developers and users).

## Feedback and Discussion

To suggest revisions or begin a discussion pertaining to this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Editorial+WG,principles&title=Principle+%2313+%22Notification%22+%3CENTER+ISSUE+TITLE%3E).

To suggest revisions or begin a discussion pertaining to the automated validation of this principle, please [create an issue on GitHub](https://github.com/OBOFoundry/OBOFoundry.github.io/issues/new?labels=attn%3A+Technical+WG,automated+validation+of+principles&title=Principle+%2313+%22Notification%22+-+automated+validation+%3CENTER+ISSUE+TITLE%3E).

