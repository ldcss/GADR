# 1. Maps API choice

Date: 2019-04-09

## Status

Accepted 

## Context

For the project, we need an API for a map: interface, search, marker placement, satellite or road map imagery. There are several options for maps, will be a primary mode of interacting with the site.

* Google maps
* OpenLayers
* TomTom
* MapBox
* HERE
* Mapfit

Main factor are cost, and ease of use (documentation for the API)

Google maps are highly customizable in style and appearance, and configerable for marker placement, information windows, and interface/controls.

## Decision

Upon examining the options, Google Maps was considered the most mature, easy-to-use and well-supported option. The API has excellent documentation and example code. The interface will be familiar to the majority of site users.

## Consequences

Google Maps has several modular APIs for Places, Routes, etc. A single API key will work for all of these.

 * Cost: for the project purpose we should not exceed the free threshold (views per day, click rate, $300 credit)
 * Limit scalability: If the project were a commercial project, Google's costs would severely limit the size the website could grow too without justifying through profitibility.
 * A 3th party map API requires a URL or Javascript page which exposes the API key and the Https request.
