# Keep low level building block view diagrams (for now)

**Decision Date**: 2021-02-12

**Summary**: We are aware that many of the current building block view diagrams are likely too low level, but we will keep them for now until we can agree on a sensible lowest level to document by hand.

## Details

[Building block view](https://docs.arc42.org/section-5/) diagrams are supposed to provide an overview of the structure and dependencies of software components on an abstract level without disclosing implementation details. We found this to work well for the level 1 "Overall System" whitebox diagrams, and for some of the diagrams showing the next lower level, e.g. the one for [Entity Change Notifications](../../systems/Client/05-Building_Block_View.md#entity-change-notifications) which shows the inner building blocks as well as neighboring black boxes. The kind of diagrams that we think are on a too low level show categorized lists of code level dependencies, such as the one for the [description API action](../../systems/Client/05-Building_Block_View.md#action-api-description).

The problem with these diagrams is that they get outdated as soon as files within that building block are renamed, added or deleted. Outdated docs at this level are probably more harmful than useful. They also don't provide much more information than the the code itself. They mostly show the constructor dependencies.

We do think that there is value in these diagrams nonetheless, since they categorize dependencies which in some cases cannot easily be derived by reading the code. We suspect that instead of creating the diagrams by hand, we should try to generate them from the code, possibly by adding annotations. Moving them closer to the code decreases the risk of getting outdated and generating them removes the effort of creating the diagrams by hand.

Aside from the overall whitebox diagram we generally struggled to create useful diagrams on the [component level](https://c4model.com/#ComponentDiagram) without getting into implementation details on the [code level](https://c4model.com/#CodeDiagram). This may also be a symptom of a lack of modularization of the code.
