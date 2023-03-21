---
layout: faq
title: The OBO Foundry Dashboard
---

## What is the OBO Foundry Dashboard?

The [OBO Foundry Dashboard (or OBO-Dashboard)](http://dashboard.obofoundry.org/dashboard/index.html)
automatically checks ontologies for adherence to OBO Foundry principles.
The OBO Dashboard is being developed by the OBO Operations Committee and members of the Technical Working Group.
Our goal is to provide a set of automated tests that establish a minimum level of compliance with OBO Principles and best practises.

Please see the [OBO-Dashboard About page](http://dashboard.obofoundry.org/dashboard/about.html) for more information.

## How can I assess my ontology using the OBO Dashboard?

After you have [submitted an ontology to be considered for the OBO Foundry](/faq/how-do-i-register-my-ontology.html),
your ontology is added to [https://obofoundry.org/obo-nor.github.io/dashboard/index.html](https://obofoundry.org/obo-nor.github.io/dashboard/index.html), which is a separate dashboard specifically for new ontology requests.

### But what if I want to check my ontology's OBO compliance without submitting it to the OBO Foundry?

The OBO Academy OBook has a how-to guide on how to run the dashboard locally: [https://oboacademy.github.io/obook/howto/deploy-custom-obo-dashboard/](https://oboacademy.github.io/obook/howto/deploy-custom-obo-dashboard/)

Another approach is to install the [ROBOT](https://robot.obolibrary.org/) command-line tool and use the ['report' command](https://robot.obolibrary.org/report)
which prints a summary to the console of issues with your ontology (categorized as ERROR/WARN/INFO depending on severity).
