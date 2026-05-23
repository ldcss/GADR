# 2. How to implement special pages

Date: 2019-05-16

## Status

Accepted

## Context

I need to implement two special pages, the privacy policy page and the about me page.

They can't be in the map, I don't want them there because the user would 
be forced to read them when scanning the spiral.

## Solution 1 Use external pages

I mean that I could create pages like /privacy-policy.html users access outside the map.
They are ad-hoc pages that don't have the map as background.

### Pros

* Simple
* No need for rest api call

### Cons

* Not really good looking because the url has an html extension when the others don't and
the map disappears. It would be better to see the map below the item like for any other item, even if
the carpet is just at the centre of the map because the item has no position on the map.
* To mitigate the cons of html extension, I may add a rule to the nginx file.

## Solution 2 Make them Items like the ones in the map

### Pros

* At a given point I will have to be able to show items that are not in the map
like items that belong to a blog. With this solution, I start building such a system
even if it's not complete.
* I don't need to implement the blog yet, just these two special pages

### Cons

* More complicated to implement. I may need an additional field for items and to change
the items view. I have to figure out how to show an item that's outside the map because I need
the item's title that is not in the item content. The rest api that returns the items in the map,
doesn't return any item outside by definition.
* To simplify the implementation I may renounce to the title, but sure later, when I want to use 
this implementation to display other items, I will need the title.

## Decision

I'll implement solution 1 because solution 2 is complicated and I want to prioritise 
the release of a first working website.

## Consequences

Later I will have to implement the second solution anyway.
