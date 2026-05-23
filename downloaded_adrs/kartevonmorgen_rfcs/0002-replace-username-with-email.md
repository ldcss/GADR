# 0002 - Replace user name by e-mail address

## Status
[status]: #status

Accepted

## Summary
[summary]: #summary

Users shall be uniquely identified by an e-mail address only.

## Context
[context]: #context

Currentrly existing users are identified by both a *user name* and an *e-mail address*.
Only the user name is guaranteed to be unique, but not the e-mail address.

The database already contains different users for the same e-mail address:

```sql
select id, role, username, email, email_confirmed
from users
where email in (select email from users group by email having count(*) > 1)
order by email;
```

Users are able to provide either the user name or the e-mail address and all
database queries have to account for this duality.

For new users the user name is already generated from the e-mail address
and cannot be chosen. The user name has become redundant and could be
replaced by the e-mail address.

## Decision
[decision]: #decision

Use the e-mail address for identifying users:

- Merge users with the same e-mail address into a single user
- Prevent duplicate e-mail addresses in the future
- Replace all references of *username* by *email*
- Remove *username* from the database and the code base

## Consequences
[consequences]: #consequences

### Advantages

Cleaning up the database and using the e-mail address as the a unique identifier
for users simplifies the implementation and prevents errors, e.g. when resetting passwords
[kartevonmorgen #539](https://github.com/kartevonmorgen/kartevonmorgen/issues/539).

### Drawbacks

Subscriptions for redundant user names are deleted, i.e. only a single subscription
for each user ()= e-mail address) will be supported.
