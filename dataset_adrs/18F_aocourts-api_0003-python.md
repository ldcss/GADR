# 1. Using Python on the backend

Date: 2021-08-09

## Status

Accepted

## Context

To support the E&I phase of 18F's work with the Administrative Office of the Courts we need to build a small API that is easy to maintain, easy to deploy, and flexible. Naturally, one of the first (and sometimes consequential) decisions we will make is the choice of programming language. Considerations for this choice include:

- Supported by cloud services without a lot of custom work
- Well-understood by people on the team with easily available documentation
- Mature enough to have all the tools and libraries we will need
- Sufficient concurrency model for designing and API

## Decision

For the current work we will build the API using Python and related tools such as FastAPI, Pytest, and SQLAlchemy.

## Consequences

The original Path Analysis pointed to CM/ECF's use of perl as problematic because:

> it is a dynamically-typed scripting language, which means certain types of errors that are easy to detect in other languages are very difficult to detect safely in Perl.

Two natural choices for designing this API: Python and Javascript are also dynamically typed. However both offer typing systems — Typescript with Javascript, and optional typing with Python — that address some of the problems associated with dynamic typing. Both are also extremely popular with developers. Most statically typed languages such as C++, Java, or Scala are poor choices for this phase of work because they bring significant overhead in tooling, many fewer developers are fluent in them, and they are not nearly as easy to deploy to cloud providers.

Python is fully-featured and includes excellent libraries for testing, validation, database interaction, and serving web requests. It also offers a multi-paradigm programming model so developers can freely mix object-oriented and functional styles where appropriate allowing developers a great deal of flexibility. Python is also fully supported and used frequently on cloud providers including Cloud.gov, AWS, and Google Cloud Services. Most importantly, a LOT of people know Python and use it daily.

A language's concurrency model should be a consideration when developing an application with intense I/O work such as querying a database while serving incoming networking requests. Python's support for concurrent programming is adequate but can be confusing since it offers concurrency models based on processes, threads, and asyncio coroutines or any combination thereof. If a decision is made to move forward with a larger project, a language like Go, built from the ground up with concurrency in mind, may be worth considering. It is also strongly-typed, which would address the path analysis's recommendation. 


