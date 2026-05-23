# Seperate Ends Decision record

* **Issue**: We need to choose between having two completely separate ends vs. having the backend render the front-end when a request is sent to a set path

* **Decision**: We decided to host two different ends separately

* **Status**: Decided

* **Notes**: That means in this directory, two folders are completely separated. They only communicate with each other through http requests. It is ok to put them into different places.