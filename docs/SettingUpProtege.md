# Introduction #

This page explains how to set up Protege 4.3 to comply with the OBO Foundry [ID policy](http://obofoundry.org/id-policy.shtml)

In the following, the example of the Epidemiology Ontology, EPO, will be used (with permission from Catia Pesquita). It is assumed that you requested and obtained a PURL and prefix from the OBO Foundry administrators. Instructions to do so are available [here](http://code.google.com/p/obo-foundry-operations-committee/wiki/Policy_for_OBO_namespace_and_associated_PURL_requests)

In summary, following the policy entails that:
  * your main file is available at http://purl.obolibrary.org/obo/epo.owl (and this is your Ontology IRI)
  * you release dated versions of your file (and have a versionIRI in your file)
  * the IRIs of your terms are of the form http://purl.obolibrary.org/obo/EPO_7digits


# Details #

When you open Protege, the first screen you see is "Active Ontology":

![http://obo-foundry-operations-committee.googlecode.com/svn/wiki/img/SettingUpProtege1.png](http://obo-foundry-operations-committee.googlecode.com/svn/wiki/img/SettingUpProtege1.png)

You want to set up the Ontology IRI and Ontology Version IRI here. For specific details of the format, check the ID policy mentioned above.

![http://obo-foundry-operations-committee.googlecode.com/svn/wiki/img/SettingUpProtege4.png](http://obo-foundry-operations-committee.googlecode.com/svn/wiki/img/SettingUpProtege4.png)

Protege asks if you want to update existing IRIs - you can chose yes or no - it doesn't matter very much, as defaults IRIs in Protege use a "#" (e.g., http://purl.obolibrary.org/obo/epo.owl#EO:0000043), so we will need to update those anyway.

You now want to set up Protege so that future entities you create are, by default, following the ID policy (and also auto incrementing their ID). To do so, go to "Protege > Preferences > New entities" Update the values as shown below:

![http://obo-foundry-operations-committee.googlecode.com/svn/wiki/img/SettingUpProtege3.png](http://obo-foundry-operations-committee.googlecode.com/svn/wiki/img/SettingUpProtege3.png)

Each entity should start with http://purl.obolibrary.org/obo, followed by a /, and ending with an auto-generated ID. This auto-generated ID should be numeric and iterative, and start with the `EPO_` prefix, and use 7 digits. Here, you will need to know which is the latest ID you used in the file so as not to overwrite existing entities. To do so, you can open the .owl file using a text editor - Protege writes them in order. For EPO, the last ID is 140, so we'll ask to start at 141.

Don't close the text file yet; you want to update existing IDs. In the EPO case, we want to replace http://epidemiology_ontology.owl#EO: with http://purl.obolibrary.org/obo/EPO_. If you are using an XML entity as shortcut, you also want to replace this. Here for example, &epidemiology\_ontology;EO: should also be replaced by http://purl.obolibrary.org/obo/EPO_