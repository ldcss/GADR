# Separation of read and modify operations

## Status

Accepted.

## Context

Our initial design for tenancy in Corvus (which necessarily affected Marain.Tenancy) comingled read and write behaviour. The model was similar to the .NET Entity Framework: if you wanted to modify a tenant, you would first fetch an object representing that tenant, then make changes to that object, and then invoke an operation indicating that you wanted those changes to be written back.

We made various changes to the Property Bag system that tenancy uses to store tenant properties to disassociate the API from any particular JSON serialization framework. We had previously forced a dependency on Json.NET, but we wanted to be able to move onto `System.Text.Json`, so we wanted to introduce a Property Bag abstraction that was independent of serialization mechanism (although still with a presumption that it must be possible for the properties to be serialized as JSON).

One of the basic principles of efficient JSON parsing in the new world is that you don't build an object model representing the JSON unless you really need to. Ideally, you leave the JSON in its raw UTF-8 state, referred to via one or more `IMemory<byte>` values, and extract what data you need only as you need it. This can dramatically reduce GC pressure, particularly in cases where most of the data in question is not used most of the time. However, this model does not fit well with the "modifiable entities" approach to updates. If anything is free to modify the properties at any time, this implies an ability to edit or regenerate the JSON.

In practice, modification of tenant properties is the exception, not the rule. Most Marain services will only ever fetch tenant properties. Only the Marain.Tenancy service should normally directly edit these properties. So the "modifiable entities" approach is not really necessary, and causes problems for migration to allocation-efficient strategies.

## Decision

Since `Corvus.Json.Abstractions` separates out read and update operations for `IPropertyBag`, and `Corvus.Tenancy` therefore does the same (since it uses property bags), Marain.Tenancy will follow suit.

The web API presented by Marain.Tenancy for modifying tenants uses JSON Patch. So instead of this procedure:

* fetch a serialized representation of an ITenant from the web API
* modify that representation to reflect the changes you wish to make
* PUT that serialized representation of an ITenant back to the web API

we now use this procedure instead:

* send a PATCH request in describing the changes required in JSON Patch format

For example, to rename a tenant, you would send this PATCH to the Marain.Tenancy service, using the URL representing the tenant (the same URL from which you would fetch the tenant if reading) with an `application/json-patch+json` content type:

```json
[{
  "path": "/name",
  "op": "replace",
  "value": "NewTenantName"
}]
```

JSON Patch supports multiple changes in a single request, e.g.:

```json
[
   {
       "op": "add",
       "path": "/properties/StorageConfiguration__corvustenancy",
       "value": {
          "AccountName": "mardevtenancy",
          "Container": null,
          "KeyVaultName": "mardevkv",
          "AccountKeySecretName": "mardevtenancystore",
          "DisableTenantIdPrefix": false
      }
   },
   {
       "op": "add",
       "path": "/properties/Foo__bar",
       "value": "Some string"
   },
   {
       "op": "add",
       "path": "/properties/Foo__spong",
       "value": 42
   }
]
```

The `op` can be set to `remove` to delete properties.

Clients will not typically build these PATCH requests themselves, because the `ClientTenantStore` type contains the relevant code. `ClientTenantStore` provides an implementation of `ITenantStore` that works by using the web API provided by Marain.Tenancy. So in practice, updating the name of a tenant is as simple as:

```csharp
await tenantStore.UpdateTenantAsync(tenantId, name: "NewTenantName");
```

Adding or changing a property looks like this:

await tenantStore.UpdateTenantAsync(
    tenantId,
    propertiesToSetOrAdd: new Dictionary<string, object>()
    {
        { "StorageConfiguration__corvustenancy", myStorageConfig },
        { "SomeOtherSetting": 42 },
    });


## Consequences

The operation of the Marain.Tenancy web API is aligned with the same command/query separation that has been introduced in `IPropertyBag` and the corresponding updates to `Corvus.Tenancy`.

Clients of tenancy that only need to be able to read properties get a much simpler API. This simplicity comes from removing the "modifiable entities" aspect of that API, and this in turn makes it easier for that API to be independent of any particular JSON serialization technology.