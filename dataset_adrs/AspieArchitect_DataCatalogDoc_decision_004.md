# DECISION 004 - HTML and Markdown enhancements over the standard SQLDoc output

## WHEN 
11- April-2020

## WHAT?
* Changing index.md to README.md with updates to any existing links
* Column descriptions containing bulleted lists to render as bullet lists in markdown
* Bulleted lists outside of tables to retain markdown in HTML.
* Markdown links in HTML to be converted to HTML links.

## WHY?
The default document for a Git repository is README.md rather than index.md

SQLDoc HTML encodes any html tags so including html in descriptions will not work as intended.  For this reason markdown links are used and the code will convert markdown links in HTML files to HTML links.
Both href and title attributes of links will be supported

Markdown bullets can be converted  to html unordered lists within tables.  Failure to do so will break the tables.  There is no need to convert markdown bullets outside of tables as these will render correctly

## See Also
* [Light Weight Decision Register](README.md)

