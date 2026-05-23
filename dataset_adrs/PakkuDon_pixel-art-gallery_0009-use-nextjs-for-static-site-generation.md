# 9. Use Next.js for Static Site Generation

Date: 2023-07-03

## Status

Accepted (Implemented 2023-07-17)

## Context

This project is written in React and bundled with Webpack. Aside from a `div` that the React application is mounted into, all content within the `body` tag is rendered client-side. This can result in a delay between the time at which the page first loads and the time at which the content is rendered.

Furthermore in development this project uses [`webpack-dev-server`](https://www.npmjs.com/package/webpack-dev-server) to serve the generated HTML, CSS and JavaScript. The dev server is configured to respond to all `GET` requests that aren't for a specific asset with the `index.html` file. However, Github Pages does not have an option to enable similar behaviour. To enable the project to handle requests to specific entries a HTML page containing a link to the bundled source code as well as some additional metadata unique to each entry is generated for each pixel art entry.

This build process has the following consequences:

- Requests to specific pixel art entries result in different HTML responses between development and production.
- There's two separate but similar HTML templates - one for requests to `/` and another for specific pixel art entries that has different metadata

The only source of data for this application is a set of JSON files that are exposed via a repository object. As this data is fixed at build-time we have the data we need to render each page ahead of time.

## Decision

- This project will be migrated to Next.js
- Build scripts will be replaced by Next.js' static site generation functionality where possible

## Consequences

- Directory structure will be modified to conform with Next.js' conventions
- All pages will be statically generated and hydrated on the client-side. This will enable us to improve performance by reducing the bundle size sent back to the user
- Behaviour between the local development environment and what's rendered in production will be more closely aligned as we will generate the same HTML in both cases
- Rendering of RSS feed and specific pages for each pixel art entry will be handled by Next.js. This will reduce the number of steps required during the deployment process
- Compilation will be performed using Next.js' compiler which will allow us to remove Webpack and other associated dependencies
