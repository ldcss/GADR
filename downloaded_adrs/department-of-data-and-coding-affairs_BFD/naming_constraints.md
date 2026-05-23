## Naming constraints

Criteria:

Namespaces, tags, objects and users are named things in the BFD. Simple and URL
friendly conventions are needed so endpoints are readable and accessible to
multiple locales.

Candidates:

* Limited by length. 
* Limited to alpha-numeric / URL friendly characters (`_` and `-`).
* UTF-8.

Commentary:

Some REST based services end up with huge illegible URLs (because of escape
characters and other limitations).

If users wish to share BFD related URLs, the URL should make it obvious what
data they're going to get. Furthermore, such URL related names should be easy
to write. As a result, the names that could be found in URLs should be limited
in such a way that they encourage read/write-ability.

Limiting the length of names ensures readability, limiting to alpha-numeric
and URL friendly characters (`-` and `_`) ensures the URL isn't full of
hard-to-decypher escape sequences and allowing UTF-8 means "alpha-numeric"
includes a wide range of characters from non-English/Latin character sets.

---

* Status: approved.
* Decision: limited length / limited to alpha-numeric / UTF-8.
* Author: ntoll.
