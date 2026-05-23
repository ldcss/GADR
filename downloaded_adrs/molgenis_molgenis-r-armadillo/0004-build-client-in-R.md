# 4. Build the first Armadillo client in R

Date: 2020-06-05

## Status

Accepted

## Context

### Data management
Data managers (in LifeCycle) use R to upload their data into Opal as this stage. Data managers often create scripts to generate the (harmonised) data they need to expose for a certain collection of variables. 

### Usage Armadillo
We are required to upload .RData files into the Armadillo service to be used in DataSHIELD. So .RData files need to be created before it can be pushed to the service.

### Possible solutions
Possible solutions regarding buildframeworks are R, Python or Java. Every framework has pros and cons. 

**R**
To connect to the current way of working with the data in LifeCycle, R is the most integrated platform to use. You can use the Armadillo client to integrate in the existing scripts of the data managers. You do not need a lot of training to incorparate the Armadillo client in the workflow. RData is the file format Armadillo uses and R is the platform to build .RData in which makes it easier to build the RData file in. When there is a need to do basic checks in the future, you can implement them.

**Python**
Python can be used together in one script with the molgenis-commander. Which is usefull when you use the MOLGENIS data provider. It allowes you to automate the whole process, from extracting data from MOLGENIS to converting into the right format for the Armadillo service (if Python supports generating .RData). From there you can upload it into the Armadillo. Another advantage is that Python is a language we are more experienced to program in.
A disadvantage is that at this point prospect customers are not used to work with python. You will need to teach them how to use Python and then how to use the client.

## Decision
The Armadillo client will be written based on R to integrate easily in the current prospect customers infrastructure. We will look at the possibility of writing other clients in the near future when we need to add other customers as well.

## Consequences
- It is tightly bound to the R environment
- It integrates with the usage in existing projects currently
