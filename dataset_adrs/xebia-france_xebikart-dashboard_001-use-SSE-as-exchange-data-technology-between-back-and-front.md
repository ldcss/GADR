# [Exchange technology to use between front and backend]

* Status: [Accepted]
- Date: 2019-03-11

## Context and Problem Statement

We would like to create a reactive Dashboard for the xebiKart. As a leaf component we will be noticed of event occurred on other component, like the car.
In order to be reactive, we must find a way to notify the front of event come from back.

## Decision Drivers

* An open source standart
* Esay to use in Javascript or in a backend side
* Limit change to done on network

## Considered Options

* [WebSocket](https://www.w3.org/TR/websockets/)
* [Server Side Event](https://www.w3.org/TR/2009/WD-eventsource-20090421/)

## Decision Outcome

Chosen option: "[WebSocket]", because it's a standart provide by HTTP2, supported in major language, easy to provide with network.
