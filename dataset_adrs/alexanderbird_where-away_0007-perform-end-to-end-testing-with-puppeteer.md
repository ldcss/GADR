# 7. perform end to end testing with puppeteer

Date: 2020-11-07

## Status

Accepted

## Context

I'd like to write automated tests to do outside-in TDD (mostly London Style) so
I want to start with end-to-end testing. In this case that means initialize a
new npm package, install where-away, run the cli, render the generated html, and
test it.

Options I've used for this type of testing before:
 - manual testing with repeatable instructions
 - puppeteer
 - selenium

I referred to this comparison of headless testing options (because I don't want
to do the manual testing thing) https://www.testim.io/blog/puppeteer-selenium-playwright-cypress-how-to-choose/

Puppeteer wins over Selenium because:
 - I don't care about cross-browser (puppeteer will test chrome, I'll do my
   styling and manual dev in firefox, my preferred browser -- so that'll cover
   chrome + Firefox)
 - apparently puppeteer execution is faster, and I care about that

Also I have a vague impression that puppeteer is simpler (maybe it's based on
past experiences? maybe it's a baseless bias?). I really don't like heavy UI
testing tools (or UI testing in general) so simpler sounds better to me.

Fortunately for me, my quick analysis based on a single blog post from an
unknown company slightly supports my predisposition, so I'm going to go with
puppeteer and pretend it was a data driven decision.

## Decision

Use [Puppeteer](https://www.npmjs.com/package/puppeteer) for headless browsing.

## Consequences

See context. 

