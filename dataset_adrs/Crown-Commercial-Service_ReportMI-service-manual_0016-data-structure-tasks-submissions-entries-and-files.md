# 16. Data structure (tasks, submissions, entries and files)

Date: 2018-08-13

## Status

Accepted

## Context

The Data Submission Service will collect and store data provided by suppliers.

At the moment, suppliers submit data once a month for each framework they are
registered on.

A submission either contains data relating to the activity undertaken that month
or says that no business has been done.

A submission with data contains one or more lines of data. A supplier may make
multiple attempts to submit data, if, for example, the data they are submitting
contains errors. We should keep a record of failed submissions.

Initially at least, submissions with data involve uploading a file. We need
to keep a record of the uploaded file for audit purposes.

### Proposed data infrastructure

The data structure of the Data Submission Service will have a number of main
entities:

* Tasks
* Submissions
* Entries
* Files

#### Tasks

Tasks are an action which must be completed by a user of the system.

Generally, a task will apply to a particular supplier on a framework for a
specific month. For example:

> Company Ltd: Submit your MI return for R1557ix G-Cloud 9 for July 2018

#### Submissions

Submissions are an attempt at completing a task.

A task may have many submissions - for example there may be a submission that
has failed because it hasn't passed data validation alongside a submission that
has been completed.

#### Entries

Entries are the line items for a submission containing the actual MI data.

A submission will have 0 or more entries. A 'no business' submission will have
no entries, but a submission with data will contain an entry for each row.

#### Files

Files are documents (usually spreadsheets) which contain the MI data used to
complete a task. They are uploaded by users during the submission process.

A submission may have 0 or more related files. A 'no business' submission will
have no files, but a submission with data may have one or more files.

Files are processed to extract the entries, and so entries can be related to a
particular file.

## Decision

We will store submitted data using the following data entities as described
above:

* Tasks
* Submissions
* Entries
* Files

## Consequences

Our API structure and database will be configured to handle this structure.

We will need to consider how this structure will be translated into an
appropriate format when exporting/transferring data into external systems such
as the CCS Finance system and CCS Data Warehouse.
