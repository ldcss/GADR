# 003 - Technology Stack and Framework

- Date: 2020/01/14
- Status: Accepted
- Deciders: Daniel Stefaniuk, Jonathan Pearce, Matthew Begley

## Context

A need has been identified for the development of an API to enable UEC service providers and DoS Leads to change the RAG status (also known as the Capacity Status) of their services in DoS. The API will need to authenticate users via a modern authentication approach, and will need to establish whether the user is authorised to be able to update the state of the service. The API will need full API documentation and will need to have fully automated testing and deployment into our cloud platform.

This ADR is concerned with the technology stack in which the API is to be written in. The following three python web application frameworks were considered and evaluated:

- Flask
- Django
- Tornado

## Decision

Flask and Django were considered the best options for the development of the API, while Tornado seemed inappropriate because we are not dealing with long running queries or processes; neither are we dealing with hundreds of thousands of requests. Flask offers a very light touch framework whereby anything other than the most basic of functionality will need to be brought in as flask plugins or extensions. Django has a much more prescriptive framework, and comes with the majority of functionality straight out of the box. Both frameworks are well established and maintained, and both come with very good documentation and active community groups.

The decision was made to implement the API using the Django framework. Although Django has a more prescriptive framework, and therefore potentially a steeper initial learning curve, the modules and functionality provided by the framework will handle the bulk of the APIs boiler or template code. With the Django framework developers can focus on the business logic of the API leaving Django to take care of the rest, leading to much cleaner code, and reducing the concerns of whether one particular extension would play nicely with another. As said, the initial learning curve for Django is perhaps steeper than that of Flask, but by leveraging the Django framework as much as possible it is envisaged that the API will adhere to Django standards (meaning that any Django developer would be able to understand it); will have far fewer bugs and teething problems to have to deal with; and will encourage rapid code development post learning curve. The documentation for the Django framework is excellent, and is supported by good examples, making finding out about the framework and what Django offers relatively simple.

Although Django comes with the majority of the functionality required for the API, Django itself is configurable with its own extensions, a few of which will be utilised.

Our technology stack:

- Python: v3.7
- Django: v3.0.2
  - Django Rest Framework: v0.1.0 (adds additional REST framework components for REST APIs)
  - Django Request Id: v1.0.0 (adds a unique request identifier to every line in the log file that is associated with a request call to the API)
  - Django Request Logging: v0.7.0 (adds logging capabilities)
  - Django Rest Framework Api Key: v1.4.1 (adds API Key authentication functionality)
  - Django Rest Framework Yet Another Schema Generator: v1.17.0 (adds API Documentation capability)

## Consequences

- Slightly steeper learning curve up front to learn about Django framework
- Everything except API business logic is abstracted away (in the framework), leaving developers to focus on business code logic
- API code is less cluttered with boiler/template type code, leading to clean, easy to understand and maintain code
- API conforms to Django's prescriptive framework and approach, making it understandable to any Django developer
- Django framework offers support for making API documentation easy to create
- Django has a well established testing framework to cover all types of testing (unit, module)
- Django has rich documentation and coding examples, making the learning of the framework a relatively simple task
- Django encourages rapid development once an understanding of the framework is gained
