## ADR 2: Using Windows Presentation Foundation (WPF)
July 25, 2019

### Context
The touch table app should support multi touch while also being robust enough to handle various UI demands. Although we initially considered a 3D model of the universe in the center of the table, that approach was dropped as it didn't help accomplish our learning goals. Given that we use a Windows device for the touch table, we must choose a technology that can run on such a machine.

### Decision
Although considering Unity early in the planning phases, we dropped that consideration due to the learning curve of C++. Unity has also dropped support of Javascript, a language most of our team is familiar with. The transition from Javascript to C# seemed less jarring, and we have more resources and shared knowledge in C#. Initial work on the table was also done with the help of Florian Block, who designed the [DeepTree](https://lifeonearth.seas.harvard.edu/learning-activities/deeptree/), another app built in WPF.

### Status
Accepted

### Consequences
Fortunately, documentation for C# is quite strong, and the language allows enough flexibility to fit the needs of the table. The .NET community is also very active, and it is easy to find answers to obstacles we would encounter during development. However, WPF seems to be losing popularity, and many of the articles concerning WPF were written a decade ago, although some Stack Overflow posts are only a year or two old.

_In Retrospect_: Although I'm concerned about the longevity of WPF, the subsystem fits our needs for this project. It's also helpful to have the [Panoptes .NET client](https://github.com/zooniverse/panoptes-net-client) available for future C# projects. However, it is discerning to see many frameworks and packages used by WPF becoming deprecated (Silverlight, Microsoft Surface SDK).

In the future, I think it would be worthwhile to explore new technologies; however, WPF is a suitable choice for most of our needs.
