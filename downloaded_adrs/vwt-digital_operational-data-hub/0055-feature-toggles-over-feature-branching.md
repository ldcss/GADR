# 55. Feature toggles over feature branching

Date: 2020-09-21

## Status

Accepted

Implements [4. Create software defined everything](0004-create-software-defined-everything.md)

## Context

Continuous integration is defined as developers doing mainline integration as soon as they have a healthy commit they can share, usually less than a day's work. For larger features, this means code changes for features are already committed to the mainline before the feature is finished. To prevent confronting users with unfinished features, these features are hidden by a keystone interface or feature toggle. The keystone interface is a user interface component that gives access to the new feature. By hiding or disabling this component, the feature is invisible to the user. The feature toggle is a configurable switch that can be used to enable or disable the feature. Both techniques allow code of partly implemented features to be integrated and deployed without exposing it to the user.

Another way of concurrent development of new features on an existing code base is feature branching. With feature branching all work for a feature is put on its own branch and not integrated into mainline until the feature is complete. Feature branching appears to be the most common branching strategy in the industry at the moment, but there is a vocal group of practitioners who argue that Continuous Integration is usually a superior approach. The key advantage that Continuous Integration provides is that it supports higher, often a much higher, integration frequency.

Higher frequency of integration leads to less involved integration and less fear of integration. If you've lived in a world of integrating every few weeks or months, integration is likely to be a very fraught activity. It can be very hard to believe that it's something that can be done many times a day. But integration is one of those things where frequency reduces difficulty. It's a counter-intuitive notion - "if it hurts - do it more often". But the smaller the integrations, the less likely they are to turn into an epic merge of misery and despair. With feature branching, this argues for smaller features: days not weeks (and months are right out).

Continuous integration allows a team to get the benefits of high-frequency integration, while decoupling feature length from integration frequency. If a team prefers feature lengths of a week or two, continuous integration allows them to do this using feature toggles while still getting all the benefits of the highest integration frequency by merging to the mainline often.

## Decision

We prefer continuous integration (using feature toggles) over feature branching.

## Consequences

Continuous integration prevents complicated merge conflicts and keeps all developers up-to-date with the lastest changes. However, it requires an automated development build pipeline including sufficient testing to make sure every commit results in working software. If that is in place, the software can be released anytime as soon as a new feature is finished, while partially implemented features are already integrated, but deactivated by a feature toggle.

## References

* https://martinfowler.com/articles/branching-patterns.html, retrieved 4 November 2020
