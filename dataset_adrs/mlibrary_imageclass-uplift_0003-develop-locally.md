# 3. Develop Locally

Date: 2021-01-28

## Status

Accepted

## Context

Developing in DLXS can be tedious, especially experiments:

* DLXS uses CVS for version control (no easy branches!)

* the CVS repository is *everything* (no easy branches!)

* Mostly developers work against production data

* Configuring modern front-end tooling will be its own project

But:

* DLXS can trivially generate the XML that is processed as source by the page templates

## Decision

The uplift front-end will be developed locally using modern front-end tooling. Experiments can be deployed to Netlify (etc) for sharing/comments.

## Consequences

* DLXS uses XSLT for page templates, in a fashion that are not natively compatible with all browsers (see: Blink/WebKit and `xsl:import`)

* We will capture the generated XML for a set of diverse collections (e.g. low-metadata vs. high-metadata)

* Local development will transform XML via XSLT into HTML and apply locally developed CSS and Javascript

