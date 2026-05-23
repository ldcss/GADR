# 4. Nginx caching of case list response

Date: 2021-06-07

## Status

Accepted

## Context

The performance of the case list page is currently reasonably slow on account of the complex database queries it entails. It's also central to the user journey and thus has high traffic whilst receiving few updates for most of the day. This makes it a good candidate for caching which should hopefully significantly improve UX whilst reducing load on the court-case-service.  

## Decision

An nginx reverse-proxy will be introduced in front of the court-case-service which will act as a cache. We will make a cheap fast query to determine the last modified date of a case list and returning this in a Last-Modified header, the client (in this case an nginx proxy) can provide this timestamp back to us in an If-Modified-Since header which court-case-service can then use to return a 304 Not Modified status in the case where no changes have been made to that case list. Nginx will then serve a cached response having validated it is still fresh. 

## Consequences

- Speed of response on repeat calls for a case list should improve drastically
- If a court has no cases for the requested date then Last-Modified will be set to a default date in the past before the service went live (2020-01-01). This will allow the (empty) case list to be cached. 
