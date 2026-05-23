## Title: Choose PHP Web Application 
### Status: ACCEPTED 
### Context: A web applicaiton is necessary to fufill the requirements for this assigment 
* Having used PHP in previous courses and personal projects, I found it to be a good choice to pair with mySQL
* There is alot of documentation and examples online demonstrating how to interact with mySQL using PHP. 
### Decision: The change proposed to the current implementation is to add the functionality of a PHP web application to display SQL data in a broswer with the help of a webserver (see choose_webserver.md for information concerning the server)
### Consequences: PHP is not the most sophisticated of web applications, it is possible I could be limited by CSS and HTML styling effects. 

## Title: Extend PHP Web Application to Support All CRUD Ooperations 
### Status: ACCEPTED
### Context: CRUD operations have to be supported by the web applications to manipulate data within the database. 
* CREATE: allows a user to add data to an existing database 
* READ: allows a user to view data in the databse in a format that makes logical sense
* UPDATE: allows a user to update an existing record in the database 
* DELETE: allows a user to delete an existing record from the database 
### Decision: The change proposed to the current implementation is to add the ability to manipulate tuples/records in a database. 
* Example: 
> say that our PHP web application reflects a libarary mangement system, the librarian must be able to add books to a library members checkout list, delete books from library members checkout list once returned, update a library members contact information, or view books that are checked out or member contact information. 
### Consequences: extending the web application to support CRUD operations increases the complexity of the application and requires more time and effort to manage and maintain the system.

## Title: Choose MVC Design Pattern for application
### Status: ACCEPTED
### Context: MVC pattern will allow the application to function in an efficient manner. 
* Model: The representation of the data (MySQL database)
* View: The UI (php code to present the database and its content inside the browser)
* Controller: The "glue" connecting the model and view (The SQL queries)
### Decision: The change proposed to the current implmentation is to organize files in such a way that the model, view & controller are isolated. 
### Consequences: employing the MVC can add another layer of abstraction to the application. 
