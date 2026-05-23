# 8. Protect Exposed IDs

Date: 2017-09-24

## Status

Accepted

## Context

To access and modify a user's articles stored in Pocket, they have to give us permission. Once permission has been granted, we have to be careful not to leak this privillaged access to malicious parties.

ASP.NET Core has [Data Protection APIs](https://docs.microsoft.com/en-us/aspnet/core/security/data-protection/introduction) for managing the encryption and decryption of data. These APIs requires the private key data to be persisted in a location where it will not be destroyed when the application is restarted.

## Decision

We will use the encrypted ID of a PocketAccount entity as an access token, representing the right to access a particular user's articles.

We will encrypt the IDs of Pocket articles returned in API responses, using the ASP.NET Core Data Protection APIs.

We will store the private key material in the database.

## Consequences

The API exposed by this application can only be used to delete or archive an article where the ID for that article has been returned in an API response.

A malicious user that has been given read access by a user will not be able to use this application to gain the ability to modify articles for that user.

A malicious user will be able to delete all of the articles belonging to a user by continuously retrieving an article from the endpoints exposed by this application and subsquently deleting it using those same endpoints.

A malicious user attempting to discover a valid access token by brute force would have to correctly encrypt potential access tokens, requiring knowledge of the private key material used by the API.

If the private key material is leaked, it can be used to bypass this protection.

Storing the private key material in the database requires the implementation of a custom [IXmlRepository](https://docs.microsoft.com/en-us/aspnet/core/security/data-protection/extensibility/key-management?tabs=aspnetcore2x#ixmlrepository).

The private key material is initialised by an IStartupFilter that is added by the Data Protection APIs. The IStartupFilter interface is explained in more detail [here](https://andrewlock.net/exploring-istartupfilter-in-asp-net-core/). As we will be storing the private key material in a database, the migrations must be handled by a custom IStartupFilter that is added before the Data Protection API's IStartupFilter.


