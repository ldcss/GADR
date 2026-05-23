# Representation of semantic metadata in markdown documents

* Status: Accepted
* Date: 2021-02-18

## Context and Problem Statement

Semantic information has to be inserted into the markdown document. How is this represented?

## Considered Options

1)  The sematic information is inserted into the text within brackets. e.g.


    * The name of the author is Shakespeare {{author.name="Shakespeare"}}

2) The information inserted as a comment and includes the markdown information. e.g for GitHUb Markdown:

    * The name of the author is Shakespeare <!--* The name of the author is {{author.name="Shakespeare'}} -->

## Decision Outcome

The chosen option is **2**, as this

* preserves the markdown for future updates of the document
* is typically not visible to readers of the markdown.
