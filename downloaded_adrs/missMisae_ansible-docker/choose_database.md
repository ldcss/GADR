## Title: Choose mySQL database to faciliate data storage 
### Status: ACCEPTED
### Context: A method of data storage is necessary to fufill the requirements for the assignment. 
* Having used mySQL in previous courses and personal projects, I found mySQL a suitable choice for supporting database capabilities.
* Many of the examples provided by my instructor are using mySQL, thus for the benefit of staying consistent with course material mySQL is a good choice.
### Decision: The change proposed to the current implementation is to add mySQL as a method for data storage.
### Consequences: MySQL is popular, however there may be a more modern tool with additional features that could be used instead. Thus, there is a risk of limitied functionality.

## Title: Choose ACID Compliancy for Database
### Status: ACCEPTED
### Context: A consistency model is needed to determine the architecture and durability of the database 
* MySQL is ACID Compliant because it abides by the guidelines to be considered an ACID compliant model which are....
  * **Atomic:** All operations succceded or every operation is rolled back 
  * *example: if a tuple fails to insert a value into a particular column, the entire operation is rolled back- values are not  inserted into the other columns* 
  * **Consistent:** On the completion of a transaction the database is structurally sound 
  * *example: the database doesn't break after an insert, update, delete, or create* 
  * **Isolated:** Transactions can't happen at the same time
  * *example: an insert and delete cannot happen at the same time* 
  * **Durable:** the results of a transaction are permanent
  * *example: values do not revert to old values once updated* 
### Decision: There is no change to the implementation fo the database, this is the out-of-box implementation of mysql
### Consequences: Acid Transactions can be considered "pessimistic" and not as flexible as base transactions. 
