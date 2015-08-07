---
layout: doc
id: OBOPURLDomain
title: OBOPURLDomain
---

# Introduction #

To enable URI dereferencing while allowing users to keep control over their resources, a resolution system in multiple steps has been implemented.

# Create the prefix/domain #

  * Add the prefix to the file ontologies.txt

**CHANGE MARCH 25th 2013**

Due to the Sourceforge upgrade, we have to switch to using the ontologies.txt in the obo-registry repository at http://obo-registry.googlecode.com/svn/trunk/metadata/ontologies.txt. Note that you will need to have committing rights on the google code project at [https://code.google.com/p/obo-registry/](https://code.google.com/p/obo-registry/)
After editing, copy the file and commit it under the OBO SF CVS at [http://obo.cvs.sourceforge.net/viewvc/obo/obo/website/cgi-bin/ontologies.txt](http://obo.cvs.sourceforge.net/viewvc/obo/obo/website/cgi-bin/ontologies.txt). Note that you will need to have sourceforge access to the OBO project at [https://sourceforge.net/projects/obo/](https://sourceforge.net/projects/obo/)

  * Add the tracker information
In the file [http://obo.cvs.sourceforge.net/viewvc/obo/obo/website/cgi-bin/trackers.txt](http://obo.cvs.sourceforge.net/viewvc/obo/obo/website/cgi-bin/trackers.txt)

  * Create the admin group

Create a group with the name obo-IDSPACE (e.g., obo-IAO), and add the OBO group as well as the requester to it. This group will administer all PURLs related to that domain.

  * Create the top-level PURL

Please check the [PURLGuide](/docs/PURLGuide.html) beforehand if you are not familiar with the PURL software/interface.

Go to [http://purl.org](http://purl.org) and register the new domain as a subdomain of /obo/. Once logged in, go to the tab "Domains", option "create a new domain", and create the domain /obo/prefix (where prefix is the prefix chosen by the resource, e.g., IAO). Note that you need to have writing permission on the OBO domain to create subdomains.

Note that if there's no /obo/$idspace.owl purl registered then the fallback is to direct to http://berkeleybop.org/ontologies/$idspace.owl, which is generated automatically by [Jenkins](http://www.obofoundry.org/wiki/index.php/Jenkins).

  * Update original tracker ticket
    * created PURL group obo-idspace
    * created PURL domain /obo/idspace (pending approval)
    * created obo/idspace.owl purl
    * added metadata in ontologies.txt (under obo-registry, copied under CVS)
    * added tracker info in trackers.txt (under CVS)
    * TODO: check domain approval in a few days.


# How does it work #
## httpRange-14 ##

When resolving IRIs, there is an ambiguity between what non-hash IRIs denote in real life (e.g, a car) and what is returned upon querying for them, i.e., a document. The W3C Technical Architecture Group (TAG) establishes a best practice to make the range of HTTP responses less ambiguous, by agreeing that (cite 1):
  * If an "http" resource responds to a GET request with a 2xx response, then the resource identified by that URI is an information resource;
  * If an "http" resource responds to a GET request with a 303 (See Other) response, then the resource identified by that URI could be any resource;
  * If an "http" resource responds to a GET request with a 4xx (error) response, then the nature of the resource is unknown.

Our architecture follows the recommendation of the TAG, and all requests to access IRIs result in an HTTP response status code 303. We add an extra step to the above by using a Canonical Name Record (CNAME)  for purl.obolibrary.org, which is an alias for http://www.berkeleybop.org/ontologies/. This allows us to leverage existing infrastructure - the PURL resolver - while allowing for immediate redirection should it fail.
Ultimately, the server responds with a 200 and sends back the RDF/XML document that describes the resource, thereby identified as an information resource as per the httpRange-14.

The [OBO ID Policy](https://obofoundry.org/id_policy.shtml) describes the general schema for which purls are then create, and what the format of individual purls are.

## Practical examples ##

### Request for /obo/aero.owl ###
This takes precedence over the general PURL redirection for the /obo/ domain as it is a more specific PURL.

### Request for http://purl.obolibrary.org/obo/IAO_1234567 ###
  * http://purl.obolibrary.org/ is a CNAME (i.e. an alias) that redirect to purl.org
  * purl.org/obo/ gets redirected to the berkeley server
  * the berkeley server has a rule such that IRIs looking like OBO IDs are redirected to /obo/NS/about/ID, where NS is the prefix (e.g. IAO) and the ID is IAO\_1234567

```
## INHERIT:
## OBO Redirect from Alan
RewriteRule ^/ontologies/(\w+)_([A-Za-z0-9]+) 
http://purl.obolibrary.org/obo/$1/about/$1_$2  [R=303,L]
```

  * if developers of a resource set up a partial redirect such that purl.org/obo/NS/about/ it will redirect to the location they such indicate
  * otherwise a rule will catch those back on the berkeley server

```
## Fallthough OBO catch.
## If the rewrite below ends back up at us, then use the stand-in
## page on ontobee.
RewriteRule ^/ontologies/\w+/about/(\w+)_([A-Za-z0-9]+) 
http://www.ontobee.org/browser/rdf.php?o=$1&iri=http://purl.obolibrary.org/obo/$1_$2
```
redirects to Ontobee where the IRIs are dereferenced.


(cite 1) http://www.w3.org/2001/tag/issues.html#httpRange-14

# Temporary Workaround (Oct 2014) #

While OntoBee is down you can use OLS:

Instructions:

Log into purl.oclc.org

Do a search for the /about/ entry for your ontology - e.g. "/obo/uberon/about/"

Change the entry from:
```
http://www.ontobee.org/browser/rdf.php?o=UBERON&iri=http://purl.obolibrary.org/obo/
```
to:
```
http://www.ebi.ac.uk/ontology-lookup/browse.do?ontName=UBERON&termId=http://purl.obolibrary.org/obo/
```
(substituting UBERON for your ID space - must be upper case)

Troubleshooting: I've never quite understood the OCLC rules for case sensitivity, in my case I had to change value of "Path:" from "/obo/uberon/about/" to "/obo/UBERON/about/" to get this to work
