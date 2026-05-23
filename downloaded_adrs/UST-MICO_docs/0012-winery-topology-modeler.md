# Re-use capabilites of Winery Topology Modeler

Technical Story: [Evaluate re-use capabilites of Winery Topology Modeler #32](https://github.com/UST-MICO/mico/issues/32)

## Context and Problem Statement

We want to use a component to graphically model nodes and edges in a web application.

## Decision Drivers <!-- optional -->

* usable with Angular
* number of dependecies
* features
  + create Nodes
  + create Connections
* usability

## Considered Options

* [Winery Topology Modeler](https://github.com/eclipse/winery/tree/master/org.eclipse.winery.topologymodeler.ui)
* [ngx-graph](https://github.com/swimlane/ngx-graph)
* [d3.js](https://d3js.org/), from React Version implemented in Angular

## Decision Outcome

Chosen option: Choosen a Combination of ngx-graph and plain d3.js, because ngx-graph might miss some usefull features but has good usability which is worth to have a look at

### Positive Consequences <!-- optional -->

* easy to use graph modeler
* only a few dependencies
* full control over features and behavior

### Negative consequences <!-- optional -->

* needs to be implemented

## Pros and Cons of the Options <!-- optional -->

### Winery Topology Modeler

* Bad, since package doesnt work when importing into plain Angular App, created issue report on their repository

### ngx-graph

* Good, because possibility to create templates for nodes, links
* Good, because runs as angular component
* Bad, because might not provide all the needed features

### d3.js

* Good, because full control over everything
* Good, because can implement the necessary behavior
* Bad, because implementation has to be done
