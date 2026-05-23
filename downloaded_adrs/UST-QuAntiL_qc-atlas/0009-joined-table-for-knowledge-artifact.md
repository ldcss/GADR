# Use a Joined Database Table for KnowledgeArtefacts

* Status: [accepted] <!-- optional -->
* Deciders: [Fabian Bühler] <!-- optional -->
* Date: [2021-05-07] <!-- optional -->

Technical Story: [<https://github.com/UST-QuAntiL/qc-atlas/issues/182>] <!-- optional -->

## Context and Problem Statement

The class `KnowledgeArtifact` is a helper base class that was not intended to have its own database table (see Issue [#182](https://github.com/UST-QuAntiL/qc-atlas/issues/182)).
The current implementation as a joined table generates a database table.
Should we keep the current joined table implementation for `KnowledgeArtifact`?

## Decision Drivers <!-- optional -->

* The `KnowledgeArtifact` table is referenced by a foreign key from `DiscussionTopic`

## Considered Options

All strategies for inheritance described by <https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#entity-inheritance>.

* [MappedSuperclass](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#entity-inheritance-mapped-superclass)
* [Single table](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#entity-inheritance-single-table)
* [Joined table](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#entity-inheritance-joined-table)
* [Table per class](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#entity-inheritance-table-per-class)

## Decision Outcome

Chosen option: "[Joined table]", because it is already implemented, allows for references in both ways and has no significant downside.

### Positive Consequences <!-- optional -->

* The current implementation can stay

## Pros and Cons of the Options <!-- optional -->

### [MappedSuperclass](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#entity-inheritance-mapped-superclass)

* Good, because no database table is created for `KnowledgeArtifact`
* Bad, because references from a `KnowledgeArtifact` subclass to `DiscussionTopic` need to be configured manually for each subclass
* Bad, because references from `DiscussionTopic` to a `KnowledgeArtifact` cannot be easily implemented later
* Bad, because no polymorphic query is not supported with this strategy

### [Single table](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#entity-inheritance-single-table)

* Good, because only one shared database table is created for all `KnowledgeArtifact` subclasses
* Good, because no joins needed for a polymorphic query of a `KnowledgeArtifact`
* Bad, because the shared table contains columns of all `KnowledgeArtifact` subclasses
* Bad, because a discriminator column is needed

### [Joined table](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#entity-inheritance-joined-table)

* Good, because the relation between `KnowledgeArtifact` and `DiscussionTopic` is only specified once for all subclasses
* Good, because no discriminator column is needed
* Bad, because of the extra table for the class `KnowledgeArtifact` that should be an abstract class based on the type hierarchy in Java
* Bad, because potentially many joins needed for a polymorphic query of a `KnowledgeArtifact`
    * Currently no such query is used

### [Table per class](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#entity-inheritance-table-per-class)

* Good, because no database table is created for `KnowledgeArtifact`
* Good, because references from a `KnowledgeArtifact` subclass to `DiscussionTopic` can be configured once in `KnowledgeArtifact`
* Bad, because references from `DiscussionTopic` to a `KnowledgeArtifact` cannot be easily implemented later
* Bad, because no polymorphic query needs a union for every subclass
