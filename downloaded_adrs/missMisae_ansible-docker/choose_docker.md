## Title: Using Docker Containers 
### Status: ACCEPTED 
### Context: A docker contaienr is necessary to fufill the requirements of the assignment 
* The benefits of employing docker contianers when builidng applications inlcude... 
  * **Isolation:** if something in the mySQL container breaks, the PHP web server and application are still in-tact
  * **Portability:** applications and dependencies can be bundled inside the container allowing, them to be moved to different machines easily. 
  * **light-weight:** docker containers are small allowing for speedy delivery of applications. 
* Docker vs. Virtual Machines 
  * docker containers *share* libraries with the host machine
  * VM's are more isolated- they do not share libraries with the host machine or any hardware. This gives VM's the benefit of an extra layer of security. 
  * VM's come with an operating system making them heavy-weight. Thus, docker has the advantage of being more light-weight. 
  * applications run in docker are faster
 ### Consequences: No real consequences besides abstraction and incorporating new tools. Docker is a useful tool for building applications and deploying applicaitons on other machines. 
