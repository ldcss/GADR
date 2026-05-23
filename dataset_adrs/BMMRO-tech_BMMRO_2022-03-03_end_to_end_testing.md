# End to end testing 

**Status:** Accepted

## Context

There was no e2e testing in the app, this meant we had to do a lot of manual testing before deploying the app, which was very repeative and time consuming. E2E testing would allow more security when pushing the application, making sure we are not pushing broken code. 

We needed a E2E testing framework that:
- Supports the browsers that the client was using: Safari.
- Supports the language of the app, Javascript.
- Gives access to the firebase datastore.
- Gives feedback on what issues in e2e tests.
- Easily maintainable by the developers.


## Options

### Option 1 - Taiko
Benefits:
- Highly readable and maintainable
- Supports Javascript
- Creates reports for things that have gone wrong 

Drawbacks: 
- Doesn't support Safari
- No documentation on how to link Taiko and Firebase


### Option 2 - Selenium 
Benefits: 
- Compatiable with all browsers
- Supports various frameworks and proggramming languages including Javascript
- Creates reports for things that have gone wrong
- Support access to Firebase
- Used with Jest which concords with the unit tests in the project
- Widely used so well documented

Drawbacks 
- Require more setup 
- Not as understandable as Cypress and Takio for someone who is not used to reading code

### Option 3 - Cypress 
Benefits:
- Highly readable and maintainable
- Supports Javascript
- Creates reports for things that have gone wrong 
- Supports access to Firebase

Drawbacks: 
- Doesn't support Safari
- Does not support mobile actions such as swiping

## Decision

### ✅ Selenium 

We chose Selenium as it fitted with all of our criteria, as well as being well documented. 

## Links

- [Selenium Guide](https://www.selenium.dev/documentation/webdriver/getting_started/)