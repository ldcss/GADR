# CEDAR Data Model Definition

**User Story:** [EASI 1134](https://jiraent.cms.gov/browse/EASI-1134)

Data records from the EASi Governance workflow needs to be pushed to CEDAR,
which then does an extract/transform/load process on the data, and pushes
it further to the Alfabet system.

The EASi team operates in an agile methodology, and the data model of the
governance system being built is necessarily in flux with frequently discovered
adjustments to its requirements.

The CEDAR team published an OpenAPI/Swagger specification of the API, to which
the EASi team was responsible for pushing data. However, this specification was
tightly bound to the EASi internal data model. This meant that as the EASi data
model changed, the CEDAR team continually had to play catch-up to keep the
specification in synchronization.

This design lead to the EASi/CEDAR relationship and interactions being very
high-coordination and very high-cost.

## Decision Outcome

After some discussion, the CEDAR team has published a new OpenAPI/Swagger API
specification and endpoint to which EASi will publish governance workflow data.
This new API only has a few high-level fields predefined, along with a field
that is defined to be a string, but is expected to be a string-encoded
arbitrary JSON object (which will be referred to through this document as a
JSON "blob").

Despite the loosely-defined nature of the JSON "blob", there still needs to be
a well-defined schema, because the CEDAR team will continue to hold
responsibility for reading and parsing the submitted data in order to submit it
to Alfabet. The "blob" will allow us to move the responsibilities for defining
the data schema from the CEDAR team to the EASi team.

To give the CEDAR team an indication as to which schema to operate against, one
of the predefined fields in the API endpoint is used to communicate the name of
which schema was used for constructing the information in the "blob". Upon
submission from EASi to CEDAR, any data with a recognized schema will be
processed and pushed to Alfabet in near real time. Submissions with schema names
unrecognized by CEDAR will be queued on the CEDAR side until the CEDAR team has
implemented their translations for the new schema, after which the queued
submissions will be de-queued and processed.

This process rightly puts the onus of communicating/distributing a new schema
squarely on the EASi team to reach out to the CEDAR team when, or in
anticipation of, updating the schema. Additionally, the queue aspect of the
CEDAR implementation gives the teams some flexibility so that the CEDAR team
does _not_ need to be in synchronous lock-step with the EASi data model.

To define the schema, the EASi team will create an OpenAPI/Swagger
specification document that inherits its API superstructure from the CEDAR
published endpoint (which is now expected to be low-flux), while additionally
defining the JSON "wire representation" of the governance data and
relationships. This spec will then generate the SDK that is used to build and
send the governance information to the CEDAR API. Changes to the "wire
representation" are what will require a new schema name/version, and will need
to be communicated to the CEDAR team (as stated above).
