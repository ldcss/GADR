# Use OpenAPI specification

* Status: accepted
* Deciders: [StoneOne, USTUTT team]

## Context and Problem Statement

Since we use the OpenAPI for frontend client code generations, the HATEOAS links are no longer needed or used.  

## Decision Drivers

* readable API documentation
* development effort to test/gather the HATEOAS links

## Considered Options

* continue to provide HATEOAS links
* remove the HATEOAS links from all entities

## Decision Outcome

Chosen option: remove the HATEOAS links from all entities, because this further simplifies the DTO entities

## License

Copyright (c) 2021 the qc-atlas contributors.

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
