---
layout: faq
title: The OBO Foundry Dashboard
---

## What is the OBO Foundry Dashboard?

The [OBO Foundry Dashboard (or OBO Dashboard)](http://dashboard.obofoundry.org/dashboard/index.html)
automatically checks ontologies for adherence to OBO Foundry principles.
The OBO Dashboard is being developed by the OBO Operations Committee and members of the Technical Working Group.
Our goal is to provide a set of automated tests that establish a minimum level of compliance with OBO Principles and best practises.

Please see the [OBO Dashboard About page](http://dashboard.obofoundry.org/dashboard/about.html) for more information.

## What does it mean for an ontology to "pass" the Dashboard?

Each element of the Dashboard check (corresponding to each principle) has four possible results:
- Pass - check (tick) mark, green background
- Info - italics 'i', blue background
- Warning - '!', yellow background
- Error - 'x', red background

The last column of the Dashboard ('Summary') corresponds to the lowest result of all checks. For example, if there are any errors, this column will contain an 'x' on a red background. If there are any 'Info' results, but no 'Error' or 'Warning' results, this column will contain an italics 'i' on a blue background.

An ontology is considered to have "passed" the OBO Dashboard checks if the status in the 'Summary' column is anything other than that of 'Error'.

## How can I assess my ontology using the OBO Dashboard?

- Evaluations for ontologies accepted into the OBO Foundry occur monthly, and can be found at the [OBO Dashboard](http://dashboard.obofoundry.org/dashboard/index.html) page.
- Evaluations for newly-submitted ontologies occur weekly, and can be found at the [New Ontology Request Dashboard](https://obofoundry.org/obo-nor.github.io/dashboard/index.html) page throughout the submission process (that is, during the period extending from initial submission through acceptance or rejection). This is a separate dashboard specifically for new ontology requests.

### What if I want to check my ontology's OBO compliance without submitting it to the OBO Foundry?

- The OBO Academy OBook has a how-to guide on how to run the dashboard locally: [https://oboacademy.github.io/obook/howto/deploy-custom-obo-dashboard/](https://oboacademy.github.io/obook/howto/deploy-custom-obo-dashboard/)
- Another approach is to install the [ROBOT](https://robot.obolibrary.org/) command-line tool and use the ['report' command](https://robot.obolibrary.org/report)
which prints a summary to the console of issues with your ontology (categorized as ERROR/WARN/INFO depending on severity).

## Where can I find information describing how to rectify issues reported by the OBO Dashboard?

Guidance on how to rectify issues can be accessed from links within the Dashboard report for an ontology of interest. First, access the report itself by following the link connected to the ontology name at the left of the Dashboard. Within the report, the section labeled "Error Breakdown" contains a column labeled "Automated Check". Each of the rows of this column link to the relevant Automated Check page for the indicated principle, and the "Fixes" section of that page contains instructions on how to rectify issues associated with that principle.

