# Define the structure of a pattern created by the PatternAtlas

* Deciders: [Manuela Weigold, Michael Falkenthal] 


## Context and Problem Statement

When creating and updating pattern languages and patterns, the structure should be defined so that users can implement their own renderers for a specific pattern language. 

## Decision Drivers 

* Pattern languages can be very different, so we should restrict their properties as little as possible. 


## Decision Outcome

A pattern consists of 
* name (string), e.g. "Elastic Infrastructure"
* type (string), e.g. <https://purl.org/patternpedia/cloudcomputingpatterns#CloudComputingPattern>
* uri (string, e.g. <https://purl.org/patternpedia/cloudcomputingpatterns/elasticinfrastructure#ElasticInfrastructure>) 
* a Map for the section properties of its pattern language (Map<section, string | string[]>), 
e.g. for the section  https://purl.org/patternpedia/cloudcomputingpatterns#hasLogo we can obtain the corresponding value  "https://www.cloudcomputingpatterns.org/img/book.png" or an array of strings

To render the pattern properties best, section should contain information about the value type, e.g. xsd:anyURI, xsd:string. This will allow us to display properties like "https://www.cloudcomputingpatterns.org/img/book.png" as links/pictures and not only as text. 




