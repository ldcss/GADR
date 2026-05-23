# 7. License information should be available from within the app

Date: 2019-10-06

## Status

Accepted

## Context

Open Source Software should be honored and apart from our obligation to show the used open source libraries, we think
the great people have to be named to honor their contribution.

## Decision

We need a new view showing all relevant open source libraries we are using including a link to the project-page.
For simplicity we should use a simple webview showing a pre created HTML page.

## Consequences

A new fragment containing a WebView has to be implemented.