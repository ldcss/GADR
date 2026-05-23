## Title: Choose Apache Webserver as Web Server 
### Status: ACCEPTED
### Context: A webserver is a necessary requirment to complete the assignment 
* A webserver is needed to host the web application.
* There is a PHP-apache bundle offered by docker (see Dockerfile in php directory), thus apache was chosen purely out of convenience. 
* I do not have much experience with Web Servers and there is a lot of documentation on apache. Again, convenience was a major factor in making the decision to use apache.
### Decision: The change proposed to the current implementation is to add an apache web server to host the php web application created in the php directory
### Consequences: No forseen consequences or drawbacks in using apache. 
