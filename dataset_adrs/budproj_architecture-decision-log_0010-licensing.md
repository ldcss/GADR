# ADR 0010: Licensing

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [More reading](#more-reading)

## Context

Since we're going open-source, we must choose the correct license to allow our paying customers to use our software on-premise and enable the community to contribute and replicate our applications.

## Decision

After further research, we’ve decided to use [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) based on the following assumptions:

* The source code doesn’t need to be public when a distribution of the software is made.
* Modifications to the software can be released under any license.
* Changes made to the source code must be documented.
* It offers the same patent usage protection as GPLv3.
* It explicitly prohibits the use of trademarked names found in the project.

## Status

Accepted.

## Consequences

Apache is not restrictive as the GNU license, but it offers adequate protection for us and allows our on-premise customers to use our software. Open-source always has the risk of copycats, but the community we're going to create worth the risk and effort.

---

## More reading

* [Apache License](https://www.apache.org/licenses/LICENSE-2.0)
