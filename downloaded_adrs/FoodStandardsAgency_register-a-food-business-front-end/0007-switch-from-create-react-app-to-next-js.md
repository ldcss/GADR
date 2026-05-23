# 7. Switch from create-react-app to Next.js

Date: 2018-05-17

## Status

Accepted

## Context

React can be implemented from scratch, using the `create-react-app` CLI, or by using a 3rd-party framework such as Next.js.

## Decision

We will re-start the scaffold.

We will use Next.js as the basis for this project.

We will extend and customise Next.js to fit our more bespoke requirements.

## Consequences

Server-side rendering is the default behaviour, which is required for accessibility.

Automatic code-splitting into individual load-on-demand modules is the default behaviour, which increases performance for initial page loads.

The setup process is more involved, but results in better team understanding of the workings of the system.

Customisation of Next.js relies on the tools that Next.js provides for customisation, such as `next.config.js`.
