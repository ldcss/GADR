# Date and time fields

**Status:** Accepted

## Context

We need to agree on the way we handle dates and times in the forms and Firestore.

Currently we have the following date and time fields:

- Encounter form - `date` saved as timestamp and `startTime` and `endTime` will be added in the near future
- Habitat Use form - `startTime` and `endTime` saved as strings

Ideally we would like to save all date and time related fields as timestamps. However in order to generate a timestamp, we need to have access to both date and time values. At the moment we pass the date from Encounter to Habitat Use form. However the application flow is going to change and the user will be navigated to Habitat Use form first instead of Encounter form. There will be no way to pass the date to the `startTime` and `endTime` fields as the Encounter form containing the `date` field will be filled after the Habitat Use form is submitted.
We don't want to add the `date` field to the Habitat Use form as we want to have a single source of truth for the date (which will always be the same for all Habitat Use forms within the Encounter form).
In MS Access database `date` is one of the composite keys used for querying and it creates a relationship between the Habitat Use and Encounter forms so it has to match.

## Options

We are unable to generate timestamp based only on start time and end time field in the Habitat Use form. However in Encounter form we have access to both date and time fields. We are considering the following options:

1. Save all time fields as strings in both the web app and Firestore. To be able to query data by date range, save `date` field in the Encounter as a timestamp where the time is midnight.

   Pros:

   - consistency in saving the same type of data in one format
   - ability to query by date

   Cons:

   - inability to query by start time and end time

2. Same as option 1, but the time in `date` timestamp is the same as `startTime` field value.

   Pros:

   - consistency in saving the same type of data in one format
   - ability to query by either date or start time

   Cons:

   - inability to query by end time
   - we save the same information twice (start time will be saved in both `date` and `startTime` fields), therefore we need to make sure they are the same

3. Save time fields in the Habitat Use form as strings, but in Encounter form merge date and time fields into a timestamps and save them as two fields in the database - `startTimestamp` and `endTimestamp`.

   Pros:

   - ability to query by date, start time and end time
   - ability to easily calculate elapsed time

   Cons:

   - start time and end time are saved in different formats in Habitat Use and Encounter forms
   - more work required to translate between the UI (date and time fields as separate fields) and database (one timestamp)

## Decision

We decided to go with option 1 for the following reasons:

- it requires the least amount of dev work
- there is no indication that querying by either start or end time will be needed
- we will still be able to convert time fields to timestamps if requirements change in the future

## Links

- [Github Issue - Extend Encounter form to include all fields](https://github.com/BMMRO-tech/BMMRO/issues/74)
