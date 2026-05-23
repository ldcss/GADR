# 11. Include code instead of packages for certain types of OSS libraries.

Date: 2017-09-12

## Status

Accepted

## Context

Instead of reinvinting the wheel, we reuse OSS libraries. Some of these libraries are written as finished products, to be reused as is, without any alteration to the library. Examples of these are `Microsoft.Net.Aspnet`, `Newtonsoft.Json`, `Xunit` or `FluentAssertions`.

Other OSS libraries are a collection of best practices, and are specifically recommended by the library authors to be included into your own project. These projects realize and admit that there is no single solution, no silver bullet to the problem they're trying to solve. While these libraries typically have a packaged version to be included, you are instead advised not to use them unless absolutely necessary. Examples of these are `AggregateSource` and `Cedar.CommandHandling`.

## Decision

We will include code in a separate csproj per library, instead of including packages, where advised by the library authors.
We will also include the tests for these projects, to maintain quality when adapting these libraries to our needs.

We will revise this approach if it starts to negatively impact our build times. A possible alternative for this could be to repackage our altered versions on a private NuGet server.

## Consequences

Build times will increase by at least something. We will need to monitor this, and periodically revisit our approach.

We will be able to use tried and tested best practices and guidelines from OSS library authors, and still maintain the possibility to alter these to our own needs.
