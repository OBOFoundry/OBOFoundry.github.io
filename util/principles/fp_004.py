#!/usr/bin/env python3

## ## "Versioning" Automated Check
##
## ### Requirements
## 1. The released ontology **must** have a version IRI.
## 2. The version IRI *should* follow a dated format (NS/YYYY-MM-DD/ontology.owl)
##
## ### Implementation
## The version IRI is retrieved from the ontology using OWL API. For very large ontologies, the RDF/XML ontology header is parsed to find the owl:versionIRI declaration. If found, the IRI is compared to a regex pattern to determine if it is in date format. If it is not in date format, a warning is issued. If the version IRI is not present, this is an error.

import dash_utils
import re

from dash_utils import format_msg

# regex pattern to match dated version IRIs
pat = r'http:\/\/purl\.obolibrary\.org/obo/.*/([0-9]{4}-[0-9]{2}-[0-9]{2})/.*'

# descriptions of issues
bad_format = 'version IRI \'{0}\' is not in recommended format'
missing_version = 'missing version IRI'


def has_versioning(ontology):
    """Check fp 4 - versioning.

    Retrieve the version IRI from the OWLOntology object. If the version IRI
    does not exist, ERROR. If the version IRI does exist, check if it is in the
    recommended date format. If not, WARN. Otherwise PASS.

    Args:
        ontology (OWLOntology): ontology object

    Return:
        PASS, INFO, WARN, or ERROR with optional message
    """
    if ontology is None:
        return format_msg('INFO', ['unable to load ontology'])

    # retrieve version IRI or None from ontology
    version_iri = ontology.getOntologyID().getVersionIRI().orNull()
    if version_iri:
        # compare version IRI to the regex pattern
        version_iri_str = version_iri.toString()
        search = re.search(pat, version_iri_str)
        if search:
            return 'PASS'
        else:
            return format_msg('WARN', [bad_format.format(version_iri_str)])
    else:
        return format_msg('ERROR', [missing_version])

    # TODO: check that versionIRI resolves
    # TODO: check that versionIRI is in date format


def big_has_versioning(file):
    """Check fp 4 - versioning.

    This is suitible for large ontologies as it reads the file line by line,
    instead of loading an OWLOntology object. This method looks for the
    owl:versionIRI property in the header.

    Args:
        file (str): path to ontology

    Return:
        PASS, INFO, WARN, or FAIL with optional message
    """
    # may return empty string if version IRI is missing
    # or None if ontology cannot be parsed
    version_iri = dash_utils.get_version_iri(file)

    if version_iri and version_iri != '':
        # compare version IRI to the regex pattern
        search = re.search(pat, version_iri)
        if search:
            return 'PASS'
        else:
            return format_msg('WARN', [bad_format.format(version_iri)])
    elif version_iri == '':
        return format_msg('ERROR', [missing_version])
    else:
        return format_msg('INFO', ['unable to parse ontology'])
