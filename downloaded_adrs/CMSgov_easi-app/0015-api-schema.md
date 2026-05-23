# Use schema for API and frontend collaboration

We need a way to agree upon and collaborate on features
that require changes in the frontend and backend. Using an
API schema will allow developers to collaborate more quickly
without breaking things that are working. This also may
frontend to contribute to the schema while backend
engineers are working on other things.

## Considered Alternatives

* Use go-swagger with OpenAPI 2.0
* Document with OpenAPI 3.0
* JSON Schema
* RAML
* Do nothing

## Decision Outcome

* Chosen Alternative: Document with OpenAPI 3.0
* OpenAPI 3.0 allows us the most flexibility in
writing schema. It is becoming industry standard. It is
lightweight to initialize and easy to organize into human-readable
ways (like putting all errors in one yaml file).
We can still use SwaggerUI or other OpenAPI 3.0 online validators.

## Pros and Cons of the Alternatives

### Use go-swagger with OpenAPI 2.0

* `+` Generates code for us
* `+` What Truss uses on MilMove
* `+` Lays out responses and requests of API
* `+` Human and machine readable
* `-` Doesn't handle nullable types well
* `-` Feels a little bit too "magic" for development
* `-` go-swagger doesn't support OpenAPI 3.0
* `-` OpenAPI 2.0 isn't as flexible as 3.0

### Document with OpenAPI 3.0

* `+` Most updated specs allows for more flexible response types
* `+` Allows a modular schema file system
* `+` Supports almost all JSON types
* `+` Lays out responses and requests of API
* `+` Human and machine readable
* `+` Shiniest industry standards
* `-` No code generation for this at the moment
* `-` We'd have to write our own validations

### JSON Schema

* `+` Easy to test responses against
* `+` Lays out responses of API
* `+` JSON Schema has wide adoption and support
* `+` Human and machine readable
* `-` Doesn't handle nullable types well
* `-` Doesn't handle the request or parameter specifications
* `-` No code generation for this

### RAML

* `+` Lays out responses and requests of AP
* `-` MuleSoft, the supporters of RAML have joined the Open API Initiative
* `-` Not very flexible
* `-` Doesn't handle nullable types well
* `-` No code generation for this

### Do nothing

* `+` Requires no work
* `-` Can require more communication between frontend and backend engineers
* `=` Code is source of truth for API
