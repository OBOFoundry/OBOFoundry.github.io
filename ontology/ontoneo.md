---
layout: ontology_detail
id: ontoneo
title: Obstetric and Neonatal Ontology
contact:
  email: fernanda.farinelli@gmail.com
  github: FernandaFarinelli
  label: Fernanda Farinelli
  orcid: 0000-0003-2338-8872
description: The Obstetric and Neonatal Ontology is a structured controlled vocabulary to provide a representation of the data from electronic health records (EHRs) involved in the care of the pregnant woman, and of her baby.
license:
  label: CC BY 4.0
  url: https://creativecommons.org/licenses/by/4.0/
domain: health 
homepage: ontoneo.com 
mailing_list: http://groups.google.com/group/ontoneo-discuss
preferredPrefix: ONTONEO
publications: 
products:
- id: ontoneo.owl
  title: ONTONEO
  description: The full version of ONTONEO in OWL format.
build:
 source_url: https://raw.githubusercontent.com/ontoneo-project/Ontoneo/master/ontoneo.owl
  - id: ontoneo.owl
tracker: https://github.com/ontoneo-project/Ontoneo/issues
browsers:
  - label: BioPortal
    title: BioPortal Browser
    url: https://bioportal.bioontology.org/ontologies/ONTONEO
  - label: OntoBee
    title: OntoBee Browser
    url: https://ontobee.org/ontology/ONTONEO
publications:
- id: https://ceur-ws.org/Vol-1747/IT403_ICBO2016.pdf
  title: "OntONeo: The Obstetric and Neonatal Ontology"
repository: https://github.com/ontoneo-project/Ontoneo
tracker: https://github.com/ontoneo-project/Ontoneo/issues
usages:
- user: http://recol.eci.ufmg.br/ (Link to group)
  description: The ReCOL research group uses OntONeo to model and structure biomedical information, particularly in obstetrics and neonatology.
  examples:
  - url: [Ontology-driven data architecture: fostering interoperability between health systems (in portuguese)](https://mba.eci.ufmg.br/wp-content/uploads/Anais_CBIS_2018_FarinelliAlmeidaLouize.pdf)
    description: The ontology has been applied in studies on data interoperability and semantic integration, improving access to structured medical information and enabling knowledge sharing between systems.
- user: Health Information Systems and Clinical Decision Support
  examples:
  - descripiton: OntONeo serves as a knowledge representation framework to support clinical decision-making and data interoperability in healthcare. It is used in information retrieval applications, enabling structured queries over medical databases and facilitating access to critical obstetric and neonatal health information.
- user: Hospital Felício Rocho, Belo Horizonte
  description: Hospital Felício Rocho is a reference center in Belo Horizonte for high-complexity healthcare, including obstetrics and gynecology. The hospital integrates advanced technologies and research in medical informatics to improve patient care and data management.
  - url: https://www.feliciorocho.org.br/
      description: Application of ontology-driven healthcare data management for obstetric and gynecological care. DOI:10.56238/devopinterscie-267
  
activity_status: active

The OntONeo suite is a collection of open ontologies available about Obstetric and Neonatal domain, currently designed to be composed by three complementary sub-ontologies covering several data from electronic health records (EHRs) involved in the care of the pregnant woman, and of her baby.
