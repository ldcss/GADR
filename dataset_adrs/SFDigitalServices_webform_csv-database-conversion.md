# Convert form submissions from CSV to Database
The Form Builder has a function to store form submissions to CSV files. This is quick and easy, but hard to maintain in the long haul. Propsed solution is to store form submissions in a database.

## Considered Alternatives
* Use Mysql database, Lumen's Eloquent ORM is an out of the box solution.
* Optional consideration: use a Document oriented database, Mongo, Couch...etc.

## Decision Outcome
* Chosen Alternative: Mysql database.
* Straight conversion path from CSV to Mysql tables.
* We know how to do this, just fill in the details.
* Only need to maintain 1 database.

## Tasks and things to consider
* Create a new controller or helper class?
* Code and tests. For every form input type, write a database mapper.
* Upates to the form setting should not affect submitted data. i.e, new form fields would have null values for the existing form data.
* For every form, create a table on form save. Form permissions?
* For form modifications, validate on form update that existing column ids are unaltered.
* How do we handle form submissions? Form author updates settings on a published form, user form submits to the published form without refreshing.
* Test how many tables can the system handle.
* How do we guard against bots submitting forms?