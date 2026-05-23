# 4. Use markdown as documentation format.

Date: 2017-06-08

## Status

Accepted

## Context

Project documentation is formatted using HTML. Documentation is accessible only online. 
A browser is needed to read the pages. Too much noise around the important text.
Documentation can differ from the version bundled with the project, 
usually not updated online. Update needs HTML editing/formatting/reformatting. 
Not portable.

## Decision

Use the [markdown syntax](https://daringfireball.net/projects/markdown/syntax) 
to format documentation.

## Consequences

Following industry standards. Offline readable. Minimal formatting of the text. 
Only a text editor needed to read/write. IDE support for display and edit 
(e.g.: IntelliJ IDEA products). Easy to bundle with any project. 
