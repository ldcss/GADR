## Webserver: nginx
# Date: 1/22/2019

# Status: Accepted
# Decision makers: Alexander Schlesinger

#Contextual outline:

Using nginx and PHP to launch and build a webpage. nginx and PHP are built as their own container using a Dockerfiles that are then called by a docker-compose.yml file(The same docker-compose.yml file that is used for the database)

#Decision:

My choice of PHP was simple: I've worked in it before and I had projects that I was confident I could rebuild for the purpose of this assignment.

The Choice of nginx on the other hand had a bit more thought behind it: Nginx is a light weight image version of an apache server built off the alpine image.
I knew, I wanted something light because I would most likely be deleting and re-pulling this image multiple times during this process and waiting for downloads would bottleneck my progress.
