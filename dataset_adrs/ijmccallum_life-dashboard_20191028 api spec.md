# Which API Spec to use

Going to try an use some kind of spec standard to define and generate the api, this doc is to decide which spec to use.

## Choices - pros cons

 - OpenAPI 3.0 (Yaml or JSON)
   - Pros: Turns out this _is_ swagger, just newer
   - cons: is there much point thinking about cons - haven't come across any competitors.
 - Swagger (Yaml or JSON)
   - Pros: More stuff works with it maybe?
   - Cons: it's the older one!

 - JSON: 
   - Pros: My code can read it directly (assuming I'm in JS)
   - Cons: More syntax to write
 - YAML:
   - Pros: It's not as tempting to try generating my own & it's more concice
   - Cons: It's not able to be read nativly by my code.

## Decision

OpenAPI.YAML

Newer spec, yaml is prettier. Simple as!