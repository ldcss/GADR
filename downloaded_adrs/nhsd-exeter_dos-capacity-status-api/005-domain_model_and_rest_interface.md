# 005 - Domain Model and REST Interface

- Date: 2020/01/14
- Status: Proposed
- Deciders: Daniel Stefaniuk, Jonathan Pearce, Matthew Begley

## Context

The Capacity Status API will be built using the Django web framework. The framework offers a number of modules and features that can be utilised when building an API. This ADR discusses these concepts and the decisions made in determining which Django features to use, and how we can use them. Essentially, this comes down to three distinct parts:

- Rest Interface (views and controllers)
- Serialization (the broker between the request and the domain model; and the domain model and the response)
- Domain Model (where and how the information is kept)

The Capacity Status API is required to:

- Take in capacity status information to update a specific service, containing the following information:
  - Capacity Status (the capacity status to put the service into in readable format: Red, Amber, Green)
  - Reset Status In Minutes (when setting the capacity status to either a Red or Amber state, this is the number of minutes the service will persist in this state. After this time, the service will be automatically set back to the Green capacity status)
  - Notes (a free text field that the requester can set)

- Update the capacity status information in Core DoS with the following information:
  - Capacity Status (in enumerated format: 1, 2, 3)
  - Reset Date Time (a timestamp specifying when the service should revert back to a Green capacity status)
  - Notes
  - Modified By (the user who has updated the capacity information)
  - Modified Date (a timestamp specifying when the capacity information was last updated)

- Respond with the capacity information for a requested service, containing the following information:
  - Service UID (the UID identifying the service)
  - Service Name (the human readable name of the service)
  - Capacity Status (Red, Amber, Green)
  - Reset Date Time
  - Notes
  - Modified By
  - Modified Date


## Decision

### Rest Interface

For the interface, we decided upon using the Django Rest Framework extension (DRF). This extension provides a vast number of useful modules and components which form part of a modern RESTful API, and by leveraging these components we keep our code clean, understandable, and easy to maintain. In addition, it is very easy to plugin API documentation into this framework, the majority of the documentation being automatically generated from code, therefore keeping documentation maintenance down to a minimum.

The extension comes with already defined 'views' which automatically configure (and give) the API any set of the standard REST endpoints that we would require. The Capacity Status API will require a GET and PUT endpoint, which can be automatically configured using the DRF RetrieveUpdateAPIView view. The default endpoint functionality provided by the DRF can also be easily modified to suit the specific business needs of the API.


### Serialization

Django provides a component known as a 'Serializer' which deals with everything concerning the transfer of data to and from the client (request/response) to and from the domain model. The serializer deals with:

- validation of the data
- conversion of the data (from JSON to domain model or visa-versa)

The Capacity Status API needs to deal with three streams of information:
- Capacity information coming in
- Capacity information held in the data model
- Capacity going out

Each stream of information contains slightly different views on the capacity information, we have therefore decided to adopt a three-serializer approach in dealing with this use case. In doing this, we have a separate, well defined serializer for each information stream. Each serializer will be configured with its own set of validation rules specifically catered to handle its specified data stream. Each serializer will also have its own defined mechanism to deal with passing the data along to the next information stream. This gives us clear separation of concerns for what each serializer is doing. We therefore have:

- Payload Serializer - responsible for consuming the JSON payload from the request, validating the data, and converting the data into the format that the Data Model Serializer expects.
- Data Model Serializer - responsible for consuming the data from the Payload Serializer, validating the data, and updating the Domain Model. Also responsible for retrieving capacity information from the Domain Model.
- Response Serializer - responsible for consuming the data from the Data Model Serializer, validating the data, and converting the data into JSON for the response.

### Domain Model

The Capacity Status API comprises of two domain models:
- Capacity Status model
- User Management model

The Capacity Status domain model represents the capacity status information for every service in Core DoS, extending to which users have which permissions to be able to view or manipulate the capacity status information. There are a collection of related tables which make up this model, and these are stored and maintained within the Core DoS database.

The part of the model relating to capacity status information (not user permissions) is coupled to the Data Model Serializer in the API. This allows the API to be able to retrieve and update capacity information using the Django framework, thus keeping the API code clean and removing the need for bespoke ORM code. Although this introduces tight coupling of this part of the Core DoS database to the API, we consider this very low risk since the probably of changes in this area of Core DoS is considered low.

The part of the model relating to user permissions to be able to update capacity status information also resides in the Core DoS database, and retrieval of this data will be performed by a dedicated 'DoS' module that the Capacity Status API can call. The mechanism for interfacing with the DoS DB is discussed in ADR-006. The driving purpose of the 'DoS' module is to reduce coupling concerns between Core DoS and the API itself, thus maintaining the integrity of the APIs core code base.

Finally, the User Management model is created and maintained by the API and is stored in its own database. This further decouples the concept of the API user (or more specifically the API Key) from what is known as the user in Core DoS. The approach taken is for Django to manage the data model, and this will be performed by Django's built in database migration tools. Using this approach we are completely decoupled from what type of database we are using as Django will automatically apply the correct drivers to whatever database we choose. This also means that database migration scripts do not need to be created. This is all handled by Django.

## Consequences

Framework takes away the vast majority of boiler plate code.
API documentation is automatically generated from both endpoints and serializers, vastly reducing overheads on creating and maintaining API documentation.
Clear separation of concerns for handling the data flows through the API.
Clear separation for handling retrieval and update of a service, from dealing with user permissions, management, and authentication.
The API is tightly coupled to the Core DoS database when storing and retrieving capacity status information. Although for our immediate use case, this is an acceptable risk.
No database scripting or maintenance is required for the User Management domain model.
