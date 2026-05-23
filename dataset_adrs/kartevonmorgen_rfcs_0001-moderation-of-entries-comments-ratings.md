# 0001 - Moderation of entries, comments, and ratings

## Status
[status]: #status

Accepted

## Summary
[summary]: #summary

Admins and scouts shall be able to archive or delete entries (both places and events)
as well as the corresponding comments and ratings.

## Context
[context]: #context

Any anonymous user is allowed to both create and edit entries. In order to maintain the
overall data quality of the Karte-von-morgen (Kvm) contents, modifications need to be
monitored and moderated, i.e. by revising or correcting recent changes.

Users are assigned one of the following roles:

- admin
- scout
- user
- guest

The roles are strictly ordered and each role includes the permission of all subordinate roles.

The moderation is done by so called _scouts_ (or "Regionalpiloten") that are
responsible for a region and/or a subject defined by the corresponding tag(s).
The _scouts_ are nominated by either other _scouts_ or _admins_.

Anonymous users or users with unverified e-mail address are considered as _guests_.

## Decision
[decision]: #decision

### Common / Back-end

- Entries are never physically deleted, only archived.
- If the user is logged in entries are associated with the user when modified: `created_by` (optional).
This is the same field name that is used for events and identifies the user that _created_ this version,
i.e. it applies to both newly created and updated entries.
- Entries can be archived and restored (unarchived) by scouts or admins.
- If an entry is archived it must be tagged with one or more of the following predefined _archive_ tags:
    - #archive-duplicate
    - #archive-obsolete
    - #archive-invalid
    - #archive-illegal
    - #archive-spam
- When archiving an entry it is not modified. Only _archive_ tags are added and `created_by` is set.
- Archived entries cannot be modified, only when restored.
- The _archive_ tags are regular tags that can be used by anyone.
- The UI may offer a convenient function for logged-in user to report entries by assigning _archive_ tags.
- The _archive_ tags need to be removed manually when restoring an entry by a scout or admin.
- The back-end provides queries to get both current and archived entries.

### Front-end

- Depending on the role of the logged-in user the front-end may show additional views
- The available actions in the front-end depend on the role of the logged in user,
i.e. additional actions are available for certain roles.
- The admin interface includes a link to edit entries directly on kartevonmorgen.org.

## Consequences
[consequences]: #consequences

- The database schema for entries needs to be extended by adding the addtional field `created_by`.
- The public API needs to be extended with additional operations and parameters.
- The back-end needs to verify that users are authorized to execute operations depending on their role.

### Open Issues

- What happens with existing links that have been archived? Should the content of archived
entries be returned if they are explicitly requested by the API?

## References
[references]: #references

- https://github.com/kartevonmorgen/kartevonmorgen/issues/267
