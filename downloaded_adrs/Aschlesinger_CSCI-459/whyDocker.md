# Why Dockerfiles and containers
# Date: 2/5/2019

# Status: Accepted
# Decision makers: Alexander Schlesinger

## Dockerfiles and docker-compose.yml
- With the combination of Dockerfiles and docker-compose a software can be quickly built simply by executing the docker-compose file. This compose file calls the Dockerfiles which then pull a docker image (an independent splice of a software). These Images are built into separate containers which are then linked to each other. The linking and environment variables are set with in the docker-compose file.

- The reason this is so handy is I can build a containerized applications that anyone can download and build by simply executing one file.

## Why this is good for this application
- In regards to this application - building this in docker allowed for separation of systems. Meaning my DB, Webserver, and PHP are all within their own container. This isolation was extremely helpful for me during development:
  - I was struggling a fair bit with the DB. I knew that the other containers were working fine and were not causing the issues I was encountering. So rather then rebuilding all three containers each time I would implement new code (an issue you would encounter using a VM), I would simply rebuild the DB container, speeding up this entire process. 
