# 9. Handling concurrent DB updates

Date: 2021-12-06

## Status

Accepted

## Context

Our two feeds for court case data, Libra and Common Platform, both send data to us in a way that can result in concurrent database updates leading to errors. 

- **Libra** - Lists of court cases received as a batch at specified times throughout the day. In practice, we quite often see multiple updates to the same cases coming either in the same payloads or in very quick succession. The effect of this is that multiple updates to the same case are processed at `court-case-service` within milliseconds of each. This can lead to race-conditions when updating records causing persistence to fail on some of these requests so they have to be retried.
- **Common Platform** - Individual updates to cases are received in real time throughout the day. Again, we very frequently see multiple updates for the same cases coming through in immediate succession leading to the same issues as seen with Libra data.

Prior to this ADR being adopted, the most common failures we saw as a result of this concurrency were:
1. **[OptimisticObjectLockingExceptions](https://www.baeldung.com/jpa-optimistic-locking)**: Thrown when a change happens between reading the state of an object and subsequently saving it.   
2. **DataIntegrityViolationException**: Thrown when an attempted update violates a database constraint. Specifically `offender_match_group_uq1` - compound key `defendantId` and `caseId` must be unique for a give offender match group 

Neither of these are fatal errors within the context of the larger system because the `court-case-matcher` will retry failed requests and the retries will generally succeed. The frequency of these issues is a definite problem though as our alerts channel is rife with these errors, potentially obscuring more serious issues.

# Decision

Though the `court-case-matcher` will also retry on failed HTTP calls, we have decided to retry within `court-case-service` as these are known and recoverable exceptions. This is also preferable to updating our alerting to filter out these exceptions which is the other alternative but isn't really dealing with the underlying problem. 

1. Apply `@Transactional(isolation = Isolation.REPEATABLE_READ)` to force transactions to acquire a lock before attempting an update (see docs [here](https://www.baeldung.com/spring-transactional-propagation-isolation) for isolation level). If this acquisition fails then a `CannotAcquireLockException` will be thrown. Though this does not prevent the transaction from failing in the first place it does provide a guarantee using database level mechanisms that no bad updates can be applied. Also, as a lock is required before beginning the transaction it will fail fast rather than by doing the query portion of the transaction and falling over on the save as it does currently.
2. Apply `@Retryable(value = CannotAcquireLockException.class)`. This in conjunction with `1` this will allow recovery from failed transactions caused by concurrent updates where a lock could not be acquired. If the application fails to get the lock, it then simply tries again after a second when the conflicting transaction should hopefully have completed.
3. Apply `@Retryable(value = DataIntegrityViolationException.class)` to catch instances of failure `2`. These happen as a result of two new records with the same compound key being created concurrently. This differs from the first failure mode in that it cannot be guarded against with a row level lock as the conflicting row causing the failure does not exist when the transaction is started. As the code checks for existing records prior to creating new ones, if we retry here it will now update the conflicting record rather than attempting to create a new one.  

## Consequences

- Fewer alerts
- There is some possibility that over time new issues will arise resulting in novel issues being caught by this mechanism in error. The risk of this happening however is very low given the tight constraints on the errors we're handling and the fact that retrying should be valid in most if not all cases of these exceptions anyway. If a retry fails to resolve the issue then the request will fail so any fatal errors should still be caught.
- This ADR addresses the problem of concurrent updates, it does not address the issue of ordering. As we are receiving these requests in very close succession there is a very real possibility that they are being applied out of order. This is not something that we currently have a solution for and applies to a larger scope than just the `court-case-service`.
