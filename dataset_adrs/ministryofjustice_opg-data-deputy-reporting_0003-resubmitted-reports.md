# 3. Resubmitted Reports

Date: 2020-02-05

## Status

Proposed

## Context

An erroneous report would be unsubmitted by the case manager, corrected and resubmitted by the deputy. In that case, we'd probably make the request again with the same source, report dates and year (though a different date submitted).

## Decision

The original report submission needs to be retained, and the 'context' of that decision retained also. The context means all the supporting files around the original submission.

When the report is re-submitted, a new document is created in Supervision, and also the context surrounding THAT submission.

Practically, what this means is that all of the supporting documents need to be submitted again, because it's impractical for us to check for documents added, removed, or modifiedfor this new submission


## Consequences

Duplication of files - takes up greater space and will require careful UX so as not to overwhelm the 'documents' tab in Supervision
