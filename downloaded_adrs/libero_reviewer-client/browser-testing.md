# 1. Browser testing

## Pupose of this document
We need a copmprehensive strategy for dealing with the browser / e2e tests. This should include what technologies to use and how they should be implemented. This document is the first pass on the investigations on libraries, more may be suggested and can be added to the repo (mentioned in the Libraries section) and discussed here. The document will also outline some remaining questions and decisions that need to be made by the team.
 
## Issues
- What library to use?
- Browser tests vs E2E tests.
- When should the tests run.

## Libraries
There are many browser testing libraries out and they are often very different. We need to use one that will allow us to write our tests using Typescript, be performant and have good integration with Browserstack. There are threee libraries that have been teststed (so far): [Nightwatch](https://github.com/nightwatchjs/nightwatch), [Intern](https://github.com/theintern/intern) and [TestCafe](https://github.com/DevExpress/testcafe), [Cucubmer](https://cucumber.io/) and Selenium have also been considered but not tested. The three libraries that were tested were all run against a quick very simple [repo](https://github.com/will-byrne/browser-test-playground) that mimicks Reviewer, a react typescript frontend with a nest.js back end, actual database interaction wasnt implemented for expediency. All three libraries ran the same test to see their relative speeds and how easy each test was to write.

### Nightwatch
Nightwatch uses selenium under the hood and is a quick and powerful testing library that runs on nodejs. The tests are simple to write and the library is easy to set up. It has no native understanding of typescript so the tests need to be compiled before they run. The tests are simple to write and follow a logical pattern for waits and finding elements. Nightwatch can take an optional parameter to slow down the tests to more accurately simulate human interactions which will be useful for testing any look ahead searches (like on the new people picker designs).

```js
module.exports = {
  "Test Form": function(browser) {
    browser
      .url("http://localhost:3000")
      .waitForElementVisible("form")
      .setValue("input[name=name]", "Sparkles")
      .setValue("input[name=age]", "42")
      .setValue("select[name=favouriteColour]", "glitter")
      .click("button[type=select]")
      .waitForElementVisible("h2")
      .assert.containsText(
        "h2",
        "Recieved Sparkles who is 42 years old and their favourite colour is glitter"
      )
      .end();
  }
};
```
this test on a local dev machine takes around 7 seconds, including starting up the test framework and browser.

### TestCafe
This library has been used before on Xpub and there were a lot of issues with the ci and the browser tests. After doing some research into the issues it is clear this was not a problem with the library but the code it was testing. Testcafe is one of the more popular libraries out there and has a large community behind it making it a very good choice. Tests written in typescript will be compiled at runtime by the Testcafe runner so we will not need to implement and maintain a separate compilation step for the test files. An advantage of testcafe is that there is already some knowledge on the team from the Xpub project so getting started should be quick.

```js
import { Selector } from "testcafe";

fixture`Form`.page`http://localhost:3000/`;

const colourSelect = Selector("select");
const colourOptions = colourSelect.find("option");

test("Can submit", async t => {
  await t
    .typeText(Selector("input[name=name]"), "Sparkles")
    .typeText(Selector("input[name=age]"), "42")
    .click(colourSelect)
    .click(colourOptions.withText("Glitter"))
    .click("button")
    .expect(Selector("h2").textContent, { timeout: 2000 })
    .eql(
      "Recieved Sparkles who is 42 years old and their favourite colour is glitter"
    );
});
```
Unfortunatley due to a currently existing bug the tests couldnt be written in Typescript ([issue here](https://github.com/DevExpress/testcafe/issues/4405)). This test took 13 seconds to run. The main issue visible for testcafe is that is always uses a human style interaction, each character is visibly typed in which is why it is almost double the duration of the nightwatch test.

### Intern
Intern is another selenium wrapper that uses JS to write tests that execute agains the browser. The documentation for Intern is not very good and was of no help trying to get the test to run, in the end they were abandoned due to an invalid version of chrome causing the test runner to crash. The tests are written in a nice way, there are no suprises of quirks that were immediately visible apart from the lack of a `waitForElement` type function and as seen in the code below a `sleep(5000)` was used (this is ideally avoided because it has a best / worst case scenario of 5 seconds, where as a `waitForElement` function with a 5 second timeout has a best case of a few milliseconds).

```js
const { describe, it } = intern.getPlugin("interface.bdd");
const { assert } = intern.getPlugin("chai");

describe("form", () => {
  it("should submit", async test => {
    const { remote } = test;

    await remote
      .get("http://localhost:3000")
      .findByName("name")
      .type("Sparkles")
      .end()
      .findByName("age")
      .type("42")
      .end()
      .findByName("favouriteColour")
      .click()
      .end()
      .findByCssSelector('option[value="glitter"]')
      .click()
      .end()
      .findByTagName("button")
      .click()
      .end()
      .sleep(5000)
      .findByTagName("h2")
      .getVisibleText()
      .then(text => {
        assert.equal(
          text,
          "Recieved Sparkles who is 42 years old and their favourite colour is glitter"
        );
      });
  });
});
```
As stated above this test was not run due to browser version issues so no timings took place, it should also be noted that while Nightwatch and Testcafe include all of their dependencies Intern requires Java to run which is another complexity to add to the CI.

### Codeceptjs
Codecept appears to be able to use a wide variety of libraries to do the actual testing and provides wrappers around these with a nicely named api. The code executes pretty quicky and the following test took only 5 seconds on the local dev machine.
```js
Feature("Form.test.js");

Scenario("test something", I => {
  I.amOnPage("http:localhost:3000");
  I.seeElement("form");
  I.fillField("name", "Sparkles");
  I.fillField("age", 42);
  I.selectOption("favouriteColour", "glitter");
  I.click("Submit");
  I.see(
    "Recieved Sparkles who is 42 years old and their favourite colour is glitter"
  );
});
```
This test was written using the webdriver api and requires the use of selenium to run.

### WebdriverIO
The webdriverio testing library is very lightweight but that also means its a very barebones, when testing it the tests were not as simple to write and the output for failing tests was not very clear.
```js
const assert = require("assert");

describe("Frorm.tsx", () => {
  it("should allow a person to be added", () => {
    browser.url("http://localhost:3000");
    const form = $("form");
    assert(form.isDisplayed(), true);
    $("input[name=name]").setValue("Sparkles");
    $("input[name=age]").setValue(42);
    $("select").selectByAttribute("value", "glitter");
    $("button").click();
    const response = $("h2");
    response.waitForExist(5000);
    debugger;
    assert(
      response.getText(),
      "Recieved Sparkles who is 42 years old and their favourite colour is glitter"
    );
  });
});
```

### Cucubmer
This is a strange testing framework that uses its own declarative style of writing tests. In a perfect world this would be fine however it would make later switching to another library a lot more expensive as the tests are that different. See example below:
```
Feature: Form
  Does the form work

  Scenario: Form data is entered
    Given name is Sparkles
    And Given age is 42
    And Given favourite colour is glitter
    When I submit
    Then I should be told "Recieved Sparkles who is 42 years old and their favourite colour is glitter" 
```
This syntax would make it quite quick to writ tests but there is a large maintenance cost with implementing all of the code to run these tests. Each of the lines needs a function that tells the browser what to do. This added cost is very high for a library that offers no real advantages over Nightwatch of Testcafe.

## Browser tests vs E2E tests
These two types of tests need to test different things and should definately be run at different steps on the CI and not on every build. The main difference between the two are that browser tests are testing UX logic and interactions across a set of browsers where E2E is testing the user stories accross both client and server.

### Browser tests
Should: 
- be quick to run (on a single browser)
- be run on PRs and remote branches.
- use a mocked out back end.
- only test UX interactions and not communication between client and server (for example if upload too many documents does the validation warning appear and disable the upload button) 
- should be run in parallel

### End to End tests
Should:
- be run on the final buit artifact.
- ideally be run last and only on merge to master with a reject merge if they fail (alternatively can be run on PR).
- test the user stories and never just test UX features.
- test issues that have been reported to prevent regressions.
- use test data and use stored SQL files to populate database.
- should never be conflicting (for example a test that deletes a submission should not interfere with another that opens a submission for editting)
- ideally be run in parallel.
- be written sparingly so as not to tie up CI resources.

### Both
Should:
- use page objects to navigate in the tests. This allows for much more concise tests and prevents a lot of duplicated code.

## When should the test run
The tests should ideally run on every push to the remote, however this is unrealistic given the amount of time they will take to run. Both need to run and pass before the code can be merged fully to master so we need to look into a hook for travis / github that will allow us to revert a merge if it fails in CI or to merge master into the branch before running the tests. The tests also have to be runnable localy, with both a full browser and a headless one, it would be good to also have the option of running it with the docker images having been build and run as if it were on the CI to allow for debugging CI issues faster.

## Issues / Decisions
### Decisions to be made
- When / where should the tests run
- What library should be used
