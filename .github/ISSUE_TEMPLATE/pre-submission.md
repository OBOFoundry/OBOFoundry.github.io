name: Pre-submission Inquiry
description: Make a pre-submission inquiry for an ontology. The purpose of a pre-submission inquiry is to announce an early ontology project that is not yet ready for review. It also serves as a reservation of an ontology namespace for 6 months.
title: Pre-submission Inquiry for Ontology [NAME]
labels: [ pre-submission ]
body:
  - type: markdown
    attributes:
      value: |
        Do _NOT_ use this form to register a new ontology with the OBO Foundry. Please read the instructions provided here: http://obofoundry.org/docs/NewOntologyRegistrationInstructions.html.
  - type: input
    id: title
    attributes:
      label: Title
      description: What is the full title of your ontology? Please do not include redundant acronyms.
      placeholder: ex. Chemical Entities of Biological Interest
    validations:
      required: true
  - type: input
    id: slug
    attributes:
      label: Short Description
      description: Please provide a short description of your ontology in one sentence.
    validations:
      required: true
  - type: input
    id: idspace
    attributes:
      label: Identifier Space
      description: What is the prefix for the identifier space associated with your ontology? This is typically all capital letters with at least 3, ideally 4 or more, characters. This MUST NOT conflict with any entries in the [Bioregistry](https://bioregistry.io/registry) nor [BioPortal](https://bioportal.bioontology.org). See OBO Principle [FP-003 "URI/Identifier Space"](https://obofoundry.org/principles/fp-003-uris.html).
      placeholder: ex. UBERON
    validations:
      required: true
  - type: dropdown
    id: domain
    validations:
      required: true
    attributes:
      label: Domain
      description: Please choose the domain that best describes your ontology
      options:
        - upper
        - anatomy and development
        - health
        - phenotype
        - investigations
        - environment
        - biochemistry
        - microbiology
        - agriculture
        - diet, metabolomics, and nutrition
        - biological systems
        - information technology
        - organisms
        - information
        - simulation
  - type: markdown
    attributes:
      value: |
        # Links

        This section of the ontology request form contains links to various resources associated with your ontology.
  - type: input
    id: repository
    attributes:
      label: Source Code Repository
      description: What is the URL of the repository? Typically, this will be a link to a public GitHub or Gitlab repository.
      placeholder: e.g. https://github.com/obophenotype/uberon/
    validations:
      required: true
  - type: input
    id: tracker
    attributes:
      label: Issue Tracker
      description: What is the URL of the public issue tracker? Typically, this will be the link to the GitHub repository with a trailing `/issues` URL part.
      placeholder: e.g. https://github.com/obophenotype/uberon/issues
    validations:
      required: true
  - type: input
    id: download
    attributes:
      label: Ontology Download Link
      description: What URL can be used to download your ontology?
      placeholder: e.g. https://github.com/obophenotype/uberon/raw/master/uberon.owl
    validations:
      required: true

  - type: markdown
    attributes:
      value: |
        # Contact

        This section of the ontology request form contains information about the contact person for the ontology. See also OBO Principle [FP-011 "Locus of Authority"](https://obofoundry.org/principles/fp-011-locus-of-authority.html)
  - type: input
    id: contact-name
    attributes:
      label: Contact Name
      description: What is the full name of the contact for the ontology?
      placeholder: e.g. Charles Tapley Hoyt
    validations:
      required: true
  - type: input
    id: contact-email
    attributes:
      label: Contact Email
      description: What is the email address of the contact for the ontology?
      placeholder: e.g. cthoyt@gmail.com
    validations:
      required: true
  - type: input
    id: contact-github
    attributes:
      label: Contact GitHub Username
      description: What is the GitHub username of the contact for the ontology? Do not include the @ symbol.
      placeholder: e.g. cthoyt
    validations:
      required: true
  - type: input
    id: contact-orcid
    attributes:
      label: Contact ORCID Identifier
      description: What is the ORCID identifier of the contact for the ontology? ORCID identifiers can be made at https://orcid.org.
      placeholder: e.g. 0000-0003-4423-4370
    validations:
      required: true

  - type: markdown
    attributes:
      value: |
        # Other information

  - type: textarea
    id: scenarios
    attributes:
      label: Intended Use Cases and/or Related Projects
      description: For projects, please include a link to their websites or other location to find more information.
    validations:
      required: false
  - type: textarea
    id: remarks
    attributes:
      label: Additional comments or remarks
      description: Is there any other information that will be helpful for the OBO community and reviewers of your ontology?
    validations:
      required: false

