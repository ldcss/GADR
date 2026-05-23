---
layout: layouts/page.njk
title: Architecture decisions
pageTitle: Architecture decisions
pageDescription: What major descisions have been made with resepect to technology and architecture?
path: /blueprint
permalink: /blueprint/adrs/index.html
eleventyNavigation:
  subgroup: Development
  parent: Blueprint
  key: Architecture decisions
  order: 12
---
<div class="nhsuk-table__panel-with-heading-tab">
  <h3 class="nhsuk-table__heading-tab">Architecture decision records</h3>
  <div class="nhsuk-table-responsive">
    <table class="nhsuk-table">
      <caption class="nhsuk-table__caption">Architecture decision records</caption>
      <thead class="nhsuk-table__head">
        <tr class="nhsuk-table__row">
          <th class="nhsuk-table__header" scope="col">ID</th>
          <th class="nhsuk-table__header" scope="col">Name</th>
        </tr>
      </thead>
      <tbody class="nhsuk-table__body">
        <tr class="nhsuk-table__row">
          <td class="nhsuk-table__cell" style="white-space:nowrap;">ADR-0001</td>
          <td class="nhsuk-table__cell "><a href="ADR-0001-record-architecture-decisions.html">Record architecture decisions</a></td>
        </tr>
        <tr class="nhsuk-table__row">
          <td class="nhsuk-table__cell">ADR-0002</td>
          <td class="nhsuk-table__cell "><a href="ADR-0002-use-github-for-source-control.html">Use Github for Source Control</a></td>
        </tr>
        <tr class="nhsuk-table__row">
          <td class="nhsuk-table__cell">ADR-0003</td>
          <td class="nhsuk-table__cell "><a href="ADR-0003-use-github-actions-for-automation.html">Use Github Actions for automation</a></td>
        </tr>
        <tr class="nhsuk-table__row">
          <td class="nhsuk-table__cell">ADR-0004</td>
          <td class="nhsuk-table__cell "><a href="ADR-0004-use-gherkin-for-describing-acceptance-tests.html">Use Gherkin for describing acceptance tests</a></td>
        </tr>
        <tr class="nhsuk-table__row">
          <td class="nhsuk-table__cell">ADR-0005</td>
          <td class="nhsuk-table__cell "><a href="ADR-0005-use-selenide-for-creating-and-managing-acceptance-tests.html">Use Selenide for creating and managing acceptance tests</a></td>
        </tr>
        <tr class="nhsuk-table__row">
          <td class="nhsuk-table__cell">ADR-0006</td>
          <td class="nhsuk-table__cell "><a href="ADR-0006-use-testcontainers-for-providing-ephemeral-test-environments.html">Use testcontainers for providing ephemeral test environments</a></td>
        </tr>
        <tr class="nhsuk-table__row">
          <td class="nhsuk-table__cell">ADR-0007</td>
          <td class="nhsuk-table__cell "><a href="ADR-0007-use-storybook-js-to-develop-and-document-screens-and-components.html">Use StoryBook.js to develop and document screens and components</a></td>
        </tr>
        <tr class="nhsuk-table__row">
          <td class="nhsuk-table__cell">ADR-0008</td>
          <td class="nhsuk-table__cell "><a href="ADR-0008-use-npm-to-host-hee-frontend-framework.html">Use NPM to host HEE front end framework</a></td>
        </tr>
        <tr class="nhsuk-table__row">
          <td class="nhsuk-table__cell">ADR-0009</td>
          <td class="nhsuk-table__cell "><a href="ADR-0009-use-react-to-manage-and-develop-the-components-for-the-hee-frontend-framework.html">Use React to manage and develop HEE frontend</a></td>
        </tr>
        <tr class="nhsuk-table__row">
          <td class="nhsuk-table__cell">ADR-0010</td>
          <td class="nhsuk-table__cell "><a href="ADR-0010-use-external-document-management-system.html">Use external document management system</a></td>
        </tr>
        <tr class="nhsuk-table__row">
          <td class="nhsuk-table__cell">ADR-0011</td>
          <td class="nhsuk-table__cell "><a href="ADR-0011-use-federated-authentication-provider.html">Use federated authentication provider</a></td>
        </tr>
        <tr class="nhsuk-table__row">
          <td class="nhsuk-table__cell">ADR-0012</td>
          <td class="nhsuk-table__cell "><a href="ADR-0012-use-external-search-service.html">Use an external search service</a></td>
        </tr>
        <tr class="nhsuk-table__row">
          <td class="nhsuk-table__cell">ADR-0013</td>
          <td class="nhsuk-table__cell "><a href="ADR-0013-use-bloomreach-channel-manager.html">Use bloomreach channel manager</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

## Architecture decisions:
An architecture decision record (ADR) is a document that captures an important architectural decision made along with its context and consequences.

An architecture decision (AD) is a software design choice that addresses a significant requirement.

An architecture decision log (ADL) is the collection of all ADRs created and maintained for a particular project (or organization).

An architecturally-significant requirement (ASR) is a requirement that has a measurable effect on a software system’s architecture.

## Decision identification:
- How urgent and how important is the AD?
- Does it have to be made now, or can it wait until more is known?
- Both personal and collective experience, as well as recognized design methods and practices, can assist with decision identification.
- Ideally maintain a decision todo list that complements the product todo list.

## Decision enactment and enforcement:
- ADs are used in software design; hence they have to be communicated to, and accepted by, the stakeholders of the system that fund, develop, and operate it.
- Architecturally evident coding styles and code reviews that focus on architectural concerns and decisions are two related practices.
- ADs also have to be (re-)considered when modernizing a software system in software evolution.
