# 3. Flattened JSON-LD parsing & emission for self-encoded dialects

Date: 2020-09-14

## Status

Accepted

## Context

Self-encoded dialects define dialect instances which share the same ID between the instance document and the dialect 
domain element encoded in such document. This allows the document and the encoded dialect domain element to be treated 
as the same resource.

On the other hand Flattened JSON-LD emission only renders one node for each ID.  

## Decision

We merge both nodes (the document and the encoded domain element) and emit the single merged node with the shared ID. 
The merged node contains both the properties from the document and the encoded domain element. 

When parsing the resulting flattened JSON-LD we parse the merged node twice: first as a domain element and then as a 
document. Parsing the properties from the domain element ignores the properties from the document and vice-versa.  

## Consequences

Source maps for the encoded domain element are lost since it is the only property shared by both the domain element and 
the document. 