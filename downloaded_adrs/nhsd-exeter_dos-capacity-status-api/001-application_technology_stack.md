# 001 - Application Technology Stack

- Date: 2019/12/18
- Status: Superseded by ADR-003
- Deciders: Daniel Stefaniuk, Jonathan Pearce, Steven Faro

## Context

A need has been identified for the development of an API to enable UEC service providers and DoS Leads to change the RAG status (also known as the Capacity Status) of their services in DoS. The API will need to authenticate users via a modern authentication approach, and will need to establish whether the user is authorised to be able to update the state of the service. The API will need full API documentation and will need to have fully automated testing and deployment into our cloud platform.

This ADR is concerned with the technology stack in which the API is to be written in. The following three python web application frameworks were considered and evaluated:

- Flask
- Django
- Tornado

## Decision

Due to the size of the API and the limited implementation time, Python and Flask were deemed the most appropriate technologies. It was decided that the Django framework was far too heavy weight and may not offer the flexibility we need. While Tornado seemed inappropriate because we are not dealing with long running queries or processes; neither are we dealing with hundreds of thousands of requests.

The technology stack is therefore:

- Python v3.7
- Flask framework v1.1, with extensions of:
  - Flask-Restplus
  - Flask-SQLAlchemy (and psycopg2-binary)
  - pytest

## Consequences

Very light touch framework with available extensions to only bring in exactly what the solution requires. Will need flask extensions to complete the solution, but these are well known about and documented. Identified extensions so far are:

- Flask-Restplus - provides REST functionality and API documentation that Swagger can plug into.
- Flask-SQLAlchemy (and psycopg2-binary) - both required to enable connectivity to a Postgres RDS database. Also provides ORM modelling.
- pytest - pythons automated unit test framework for writing and running unit tests.

Easy to work with. The documentation that comes with Flask is very good. Flask debug mode is concise and understandable.
