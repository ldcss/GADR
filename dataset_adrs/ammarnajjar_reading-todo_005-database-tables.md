# Database Tables

Date: Sun Sep 29 06:32:35 CEST 2019

## Milestone

0.1.0

## Context

For the project a database structure need to be chosen and adopted.

## Decision

Three table database will be used at this point:

![database structure](./assets/db_structure.png)

```
Table book {
  isbn varchar(50) [pk]
  title varchar(300)
  year char(4)
  category varchar(300)
  sub_category varchar(300)
}


Table author {
  id bigserial [pk]
  name varchar(300)
}

Table book_author {
  book_isbn varchar(50) [ref: > book.isbn]
  author_id bigint [ref: > author.id]
}
```

## Consequences

Why:

- A book might have multiple authors.
- An author might have written multiple books.
