# ADR1: Use of SQL over MongoDB for database

A database also allows the administrator to manage and have access information of users. This is needed to manage the users and their information on the bill sharing application. There are two main choices for the databases that were explored being SQL and MongoDB.

SQL deals with relational databases that have operations such as update, delete, query, insert. The database can be set up both on Azure and on the github repository which makes it easier to work with because it is integrated in the project. SQL databases store user information in a tabular format.

MongoDB is not linked to the Azure platform in its default state. Therefore, one needs to make sure they can successfully link it to Azure platform for deployment purposes. MongoDB does not have clear schema definitions. 

## Decision

We have decided to use SQL for our database.

## Status

Accepted

## Consequences

    * SQL databases are in a tabular format, making it easy to read from and write data to the database. 
