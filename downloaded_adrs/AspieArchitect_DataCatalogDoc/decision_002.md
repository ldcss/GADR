# DECISION 002 - Use of views on views

## WHEN 
11- April-2020
## WHAT?
Under normal circumstances using views on views would be strongly discouraged.

Views on views create diagnostic nightmares and inadvertent duplication of joins and datasets

In this case the choice to use views on views is a concious one.

## WHY?

There can be both a foreign key and default column description that can be applied to a column.

Both the column default and foreign key queries are quite convoluted.  Combining their functionality into a single query would make the query difficult to read.

As there is little scope for expanding the functionality of these helper queries the choice of simplified readability is unlikely to result in obscure diagnostics in the future.

## See Also
* [Light Weight Decision Register](README.md)
