# Separation of concerns in component registration

## Status

Proposed

## Context

When the library was originally built, an extension method on `IServiceCollection` was provided to make it simple to add library components to the dependency injection container.

Over time, additional components have been added to this single extension method. As a result, it is misnamed; it's currently called `AddJsonSerializerSettings` but it adds:
- Endjin's standard `IJsonSerializerSettingsProvider` implementation
- Property bag support via `JsonNetPropertyBagFactory`
- Several `JsonConverter` implementations

The problem described in https://github.com/corvus-dotnet/Corvus.Extensions.Newtonsoft.Json/issues/145 has highlighted the fact that not all clients require all of those different things to be registered. For example, the referenced issue would not happen if it weren't for the combination of our standard `JsonSerializerSettingsProvider` (which sets `DateParseHandling` to `DateParseHandling.DateTimeOffset`) and the inclusion of the `DateTimeOffsetConverter`, which was originally implemented as a way of ensuring `DateTimeOffset` values serialized into CosmosDb remained sortable and filterable.

As a result, it would be useful for clients to be able to register the particular components they need from those provided by the library.

## Decision

We will modify the `JsonSerializerSettingsProviderServiceCollectionExtensions` class to provide separate methods to register the various components.

The existing `AddJsonSerializerSettings` method will be deprecated via the `ObsoleteAttribute` and replaced with multiple separate methods.

## Consequences

The use of `ObsoleteAttribute` on the existing method prevents this change from being a breaking one, but it will mean that codebases that depend on this library and treat warnings as errors will need minor code changes in order to accept this update.