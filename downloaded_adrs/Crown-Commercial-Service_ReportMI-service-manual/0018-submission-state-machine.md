# 18. Submission state machine

Date: 2018-08-15

## Status

Proposed

## Context

As outlined in [ADR-0016][adr-0016], the Data Submission Service will use
"submissions" to describe something that a supplier has submitted to us in order
to complete a "task".

Submissions will exist in a state machine that outlines what is happening with
them.

Currently, we expect there to be 6 states:

* **pending** - a blank submission that is awaiting data
* **processing** - a submission where data is being processed
(eg a file is being ingested or data is being validated)
* **validation_failed** - the submitted data has failed the validation process
and needs to be corrected
* **validation_passed** - the submitted data has passed the validation process,
and the supplier now needs to review the results
* **supplier_rejected** - the supplier has reviewed the result of the data
processing and has rejected it (eg they have realised that their data needs to
  be amended)
* **supplier_accepted** - the supplier has reviewed the result of the data
processing and are happy that it is accurate

Other states may added in future to cover approval processes, and fixing
mistakes in returns.

## Decision

The system will model the 6 states highlighted above.

Submissions containing data will proceed through the states from `pending` to
`processing` to either `validation_failed` or `validation_passed`. If the
validation has passed, the supplier can reject the submission (move to
`supplier_rejected`) or accept the submission (move to `supplier_accepted`).

A 'no business' submission will proceed straight to `supplier_accepted` once
the supplier has confirmed they wish to make this submission.

This is shown in the following diagram.

![Submission state machine diagram](../diagrams/0018-submission-states.jpg)

## Consequences

We will need to model submissions to have this state machine.

This will impact exports to the Data Warehouse as these states differ to that of
MISO. The warehouse will have to be updated to handle these states and the
import process changed. This will be covered in more detail in a future ADR.

[adr-0016]: 0016-data-structure-tasks-submissions-entries-and-files.md
