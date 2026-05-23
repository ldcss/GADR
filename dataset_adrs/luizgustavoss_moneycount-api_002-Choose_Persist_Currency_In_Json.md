# Title: 002 - Choose Persist Currency Definitions in JSON File


## Status 

accepted


## Context 

I have to decide how to persist data related to supported currencies in the project. Choices are a relational database or text files such as txt, xml or json. Even NoSQL databases could be used.


## Decision 

I decided to use json files to persist supported currencies in the project because this kind of data doesn't change all the time. JSON files are easy to store, to write, and to read in Java Objects. Each time a new currency is added it's just a matter of update the file.


## Consequences 

Even if a lot of currencies are supported in the future, no changes are needed in the code, just an update in the json file. A lot of persistence code were saved with a simpler solution.
