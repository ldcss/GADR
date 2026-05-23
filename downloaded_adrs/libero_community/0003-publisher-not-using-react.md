# 3. Publisher not using React

Date: 2019-10-01

## Status

Accepted

## Context
Investigation into stronger alignment of technologies, practices and processes across the Libero Suite of products has resulted in time-boxed discovery sessions to find the advantages and consequences of various different aspects.
One such area was front-end technologies. Other areas looked at aligning around JavaScript technologies and removing PHP from Libero Publisher.

Libero Reviewer uses React and JavaScript so the hypothesis was that aligning Libero Publisher around those technologies would improve the developer experience and encourage more reuse between the products. However, Libero Publisher needs a read-optimised, highly performant, progressively enhanced front end. This need has been deprioritised in Producer and Reviewer, but Publisher has a strong need for this.

## Decision
We will not use the React ecosystem for Libero Publisher.

The full decision and more context is given in [this community-accessible document](https://docs.google.com/document/d/1FkdvBjSb1BH1fhgujtppunvL_NX5U3xVuxv7L0fV010/edit#heading=h.oip2sudw7pju).

Further decisions on where the front-end developer experience can be improved through sharing of tools and styles will be documented in subsequent ADRs.

## Consequences
Libero Publisher front end can be light weight and will work without JavaScript in the browser.

Libero Publisher will not be able to share pattern template code with Libero Reviewer.

