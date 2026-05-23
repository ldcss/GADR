# 2. Use ASP.NET Core

Date: 2017-09-24

## Status

Accepted

## Context

With the introduction of .NET Core, we need to decide whether to use ASP.NET with .NET v4.x or ASP.NET Core.

## Decision

We will use ASP.NET Core.

## Consequences

The application can on a machine running Linux, MacOS or Windows, rather than being restricted to Windows.

The .NET Core implementation and tooling is still evolving, which may result in certain .NET Core releases requiring changes to the project structure.

Commonly used libraries, such as Entity Framework, have specific versions for use with .NET Core. In some cases the APIs differ from the .NET v4.x versions.

Some libraries have not yet carried out the work necessary to be compatible with .NET Core. It will not be possible to use these libraries until the required work is completed.
