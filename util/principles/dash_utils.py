#!/usr/bin/env python3


import json

obo = 'http://purl.obolibrary.org/obo/'


def format_msg(level, issues):
    """Return a formated message for the dashboard CSV.

    Args:
        level (str): violation level
        issues (list): list of issues causing violation

    Return:
        violation level and optional help message as one string
    """
    if level == 'PASS' and len(issues) == 0:
        return level
    else:
        return '{0}|{1}'.format(level, '. '.join(issues))


def get_ontology_annotation_value(annotations, ann_prop):
    """Return the annotation value for a given property in a set of
    annotations.

    Args:
        annotations (list): list of OWLAnnotations
        ann_prop (OWLAnnotationProperty): annotation property to find value of

    Return:
        value of annotation property
    """
    for a in annotations:
        prop_iri = a.getProperty().getIRI()
        if prop_iri.toString() == ann_prop:
            return get_annotation_value(a)


def get_annotation_value(a):
    """Return the string value of an annotation without datatype or lang tags.

    Args:
        a (OWLAnnotation): annotation to get value of

    Return:
        string value of annotation
    """
    # maybe is IRI
    val_iri = a.getValue().asIRI().orNull()
    # maybe is literal
    val_lit = a.getValue().asLiteral().orNull()
    if val_iri:
        val = val_iri.toString().rstrip().lower()
    elif val_lit:
        clz = val_lit.getClass().getSimpleName().lower()
        if clz == 'owlliteralimplstring':
            # string datatype, get the literal value
            val = val_lit.getLiteral().rstrip().lower()
        else:
            val = val_lit.toString().rstrip().lower()
    else:
        val = None

    # remove datatype or lang tags
    if val is not None and '"^^' in val:
        val = val.split('^^')[0]
    elif val is not None and '"@' in val:
        val = val.split('@')[0]

    # get rid of quotes and return
    if val is not None:
        return val.replace('"', '')
    return val


def get_prefix(line):
    """Get the prefix for a full namespace from a prefix line.

    Args:
        lines (str): RDF/XML line with prefix defintion

    Return:
        the string prefix in that line
    """
    return line.split('=')[0].split(':')[1]


def get_resource_value(line):
    """Get the resource value from an RDF/XML line with rdf:resource.

    Args:
        line (str): RDF/XML line with rdf:resource

    Return:
        rdf:resource string value (an IRI)
    """
    resource = line.split('=')[1].replace('"', '').replace('/>', '').rstrip()
    if '&obo;' in resource:
        # normalize XML with prefixes
        return resource.replace('&obo;', obo)
    return resource


def get_literal_value(line):
    """Return the literal value between the tags in an RDF/XML line.

    Args:
        line (str): RDF/XML line with a literal value

    Return:
        literal string value
    """
    return line.split('>')[1].split('<')[0]


def get_version_iri(file):
    """Get the version IRI from an RDF/XML ontology file.

    Args:
        file (str): path to ontology file

    Return:
        version IRI as string
    """
    prefixes = True
    valid = False
    owl = None
    version_iri = None

    with open(file, 'r') as f:
        for line in f:
            # if we get to rdf:about the ontology
            # we have passed the prefixes
            if 'Ontology' and 'about' in line:
                if not owl:
                    # no OWL prefix = we cannot parse
                    return format_msg('INFO', ['unable to parse ontology'])
                prefixes = False

            elif prefixes and 'http://www.w3.org/2002/07/owl#' in line:
                # set the OWL prefix
                owl = get_prefix(line)

            elif owl and '{0}:versionIRI'.format(owl) in line:
                # we found the version IRI
                # no need to continue reading lines
                version_iri = get_resource_value(line)
                valid = True
                break

            elif owl and '</{0}:Ontology>'.format(owl) in line:
                # valid RDF/XML but no version IRI was found
                valid = True
                break
    if not valid:
        return None
    if not version_iri:
        version_iri = ''
    return version_iri


def is_obsolete(annotation):
    """Determine if an annotation using the owl:deprecated property has value
    true.

    Args:
        annotation (OWLAnnotation): annotation using owl:deprecated

    Return:
        True if annotation value is 'true'
    """
    val = annotation.getValue().asLiteral().orNull()

    if val is None:
        # TODO - why is it 'None'?
        # if it uses the owl:deprecated property it is probably deprecated
        return True

    if val.isBoolean():
        return val.parseBoolean()
    else:
        if val.isLiteral():
            val = val.getLiteral()
        elif val is not None:
            val = normalize_label(val.toString())
        elif not val:
            # TODO - why is it 'None'?
            # if it uses the owl:deprecated property it is probably deprecated
            return True
        if val == 'true':
            return True

    return False


def load_schema(schema_file):
    """Load and return a JSON object from JSON schema.

    Args:
        schema_file (str): path to JSON schem

    Return:
        schema JSON object
    """
    try:
        with open(schema_file, 'r') as s:
            return json.load(s)
    except Exception as e:
        print('Unable to load %s: %s' % (schema_file, str(e)))
