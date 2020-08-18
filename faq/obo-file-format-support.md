


# Support for OBO File Format
A number of ontologist develop their ontologies using the [OBO file format](https://owlcollab.github.io/oboformat/doc/GO.format.obo-1_4.html). This page provides support for maintaining OBO file ontologies in accordance with OBO Foundry principles.   
The page is divided in sections containing OBO specific support for that principle.

## Principle 1: Open

OBO Foundry ontologies MUST specify the reuse constraints using the following annotations in any publically released OWL version of the ontology:
* dcterms:license - specifies the license
* rdfs:comment - specifies terms of reuse

In OBO-format ontologies, the license is a separate property annotation that can be converted to a dc:license statement when the ontology is converted to OWL. The example below demonstrates this.

### Example of OBO code for the license annotation:
```
property_value: http://purl.org/dc/terms/license http://creativecommons.org/licenses/by/4.0/

remark: *Ontology name* by *developer group(s)* is licensed under CC BY 4.0. You
    are free to share (copy and redistribute the material in any medium
    or format) and adapt (remix, transform, and build upon the material)
    for any purpose, even commercially. You must give appropriate credit
    (by using the original ontology IRI for the whole ontology or
    original term IRIs for individual terms), provide a link to the
    license, and indicate if any changes were made. You may do so in any
    reasonable manner, but not in any way that suggests the licensor
    endorses you or your use.

```

### Ontology re-use of terms
The attribution method for individual terms reused in another ontology (e.g., by MIREOT) is via use of their original IRI or ID.

In OBO file format, any ontology re-using individual terms from another ontology should:
* re-use the original term ID (of the form <GO:0000001>)
* include any XREFs to the original term editor(s) from the original ontology

## Principle 3: URI/Identifier Space
Each class and relation (property) in the ontology must have a unique identifier. The identifier should be constructed from a prefix that is unique within the Foundry (e.g. GO, CHEBI, CL) and a local identifier (e.g. 0000001). The local identifier should not consist of labels or mnemonics meaningful to humans.  

In OBO file format ontologies, this is satisfied so long as all identifiers are of the form <IDSPACE>:<NUMBER>

The identifier corresponds to OBO PURL with base URI http://purl.obolibrary.org/obo/<IDSPACE>_<NUMBER>.

## Principle 4: Versioning
For an OBO format ontology use the metadata `data-version` tag. For example, here is an example of a dated version.
```
data-version: 2015-03-31
```
And here is an example of numbered version.
```
data-version: 44.0
```
## Principle 6: Textual Definitions
In OBO file format ontologies, textual defintions are specified using the `def` annotation. 
### Example defintion
```
id: GO:0000109
name: nucleotide-excision repair complex
def: "Any complex formed of proteins that act in nucleotide-excision repair." [PMID:10915862]
```
