# JSON framework independence

## Status

Accepted.

## Context

We frequently need to deal with information that will be serialized as JSON, either because it needs to be used in a web API, or because it is serialized in some JSON-based storage system. For many years, Json.NET has been the de facto API for working with JSON in .NET applications. However, now that .NET Core has `System.Text.Json` built in, there are good reasons to want to move to that. This means that libraries that depend on Json.NET become problematic.

So we need ways for our libraries to work with JSON data without forcing the decision of whether to use Json.NET or `System.Text.Json`.

## Decision

We have moved types previously in `Corvus.Extensions.Newtonsoft.Json` into `Corvus.Json.Abstractions`, having modified them to remove any direct dependency on Json.NET.

Currently, only the property bag type has been moved. (And it is now an `IPropertyBag` interface.) A great deal of what's in `Corvus.Extensions.Newtonsoft.Json` is already in the right place, because it deals directly with Json.NET-specific concerns (e.g., custom type converters).

## Consequences

The property bag concept was never conceptually tied to Json.NET. The dependency was largely a matter of convenience, but it has had the side effect of making `Corvus.Tenancy` depend on Json.Net, which in turn has imposed the same dependency on a a great deal of the rest of our code. So this will make adoption of `System.Text.Json` much easier. As part of this, `IPropertyBag` is now a read-only abstraction, with modifications managed through a new `IPropertyBagFactory` interface. This is a better fit with JSON consumption models in which data is parsed in situ rather than extracting it into an object model before use.