## Tag Values

Criteria:

Namespaced tags attach values to objects. What is the "type" system for the
BFD. It needs to:

* Be clear.
* Promote consistency.
* Promote thoughtful definition of data.
* Avoid unexpected value related side effects.

Candidates:

Tag/value types are:

* Static. 
* Dynamic.

In addition, should the BFD allow for null values to be associated with a tag
on an object?

Commentary:

Knowing and enforcing the type of data at the tag level ensures clarity and
consistency. Furthermore, forcing the creator of a tag to define the tag's type
ensures they think carefully about the sort of value the tag will be used to
represent. Finally, by disallowing null values users can be certain that any
value they retrieve will be guaranteed to be a value of the type of the tag. If
a value of a tag for a certain object is unknown, then that tag should not
exist on that object (otherwise, what's stopping every tag from being attached
to every object with the value null, until someone updates the value?).

---

* Status: approved.
* Decision: static / no null.
* Author: ntoll.
