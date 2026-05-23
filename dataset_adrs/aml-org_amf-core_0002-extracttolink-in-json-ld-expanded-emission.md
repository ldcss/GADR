# 2. extractToLink in JSON-LD expanded emission

Date: 2020-09-03

## Status

Accepted

## Context
Expanded JSON-LD emission embeds node links. This means that whenever a node references another node, instead of using a 
JSON-LD link we render the referenced node in place. This is because the advantage of the JSON-LD expanded emission is 
to allow consumer applications (e.g. API Console) to consume JSON-LD as regular JSON; and for that we cannot use JSON-LD
links.

**The problem**: Embedding nodes causes the resulting JSON-LD to be very big (because the same node is rendered many times). 

_Note: Flattened JSON-LD emission does not suffer this problem because it only renders each node once and then uses 
JSON-LD links for every node reference._

## Decision

`extractToLink` is a logic we developed for the expanded JSON-LD emission that introduces _AMF links_ (as opposed to 
JSON-LD links) for some node references. Specifically, it introduces an AMF link and extracts the link target to a 
_declaration_. 

_AMF links_ are only available for `Linkable` domain elements, so we use it in only for certain elements. These links 
are part of the model as opposed to JSON-LD links which are simple graph references. 


## Consequences
`extractToLink` **helps** in reducing the size of the JSON-LD **but it's non-optimal** since only a part of the total 
references are replaced with links, the rest are still embedded.

It also produces the following consequences/side effects:
1. Consumer applications must be able to follow AMF links, (API Console does)
2. It alters the model (it introduces AMF links and declarations). The rendered JSON-LD does not match the input BaseUnit
3. It rollbacks some parts of resolution (resolution resolves AMF links)
4. It mutates the input BaseUnit