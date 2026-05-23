# DECISION 003 - Not using the data dictionary helpers for MetaData

## WHEN 
11- April-2020

## WHAT?
The data dictionary helpers are to allow descriptions to be attached to objects using a simpler call to stored procedures rather than the complexity of the extended property stored procedure

* [sp_addextendedproperty](https://docs.microsoft.com/en-us/sqlrelational-databases/system-stored-procedures/sp-addextendedproperty-transact-sql?view=sql-server-ver15)
* [sp_updateextendedproperty](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-updateextendedproperty-transact-sql?view=sql-server-ver15)
* [sp_dropextendedproperty](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-dropextendedproperty-transact-sql?view=sql-server-ver15)

In this case although we create the helpers in the MetaData schema we don't use them to document themselves

## WHY?

We may revisit this decision at a later date.

The key deliverable is the table, view and column descriptions for the Data Catalog product.  The time constraints require that the focus be placed on the Data Catalog documentation and not the peripheral items.

## See Also
* [Light Weight Decision Register](README.md)

