## ADR 3: Choosing the MVVM Pattern
July 25, 2019

### Context
We should structure files in a way that makes the codebase easy to navigate and intuitive when searching for certain components. Organization should adhere to accepted practices in the .NET community.

### Decision
The MVVM (Model-View-View Model) approach is widely used by the WPF (Windows Presentation Foundation) community. It's difficult to search the web for insight into building WPF applications without running into information about MVVM architecture. MVVM appears to be the standard.

Application components should be divided into a Model, View, and View Model folder, with each folder containing the necessary items for displaying the UI and interpreting data on the app.

### Status
Accepted

### Consequences
It will be easier to find solutions to coding problems online by accepting a widely-used design pattern. However, this doesn't necessarily solve the problem of how other items should be organized (lib, images, fonts, etc.).

_In Retrospect:_ The MVVM pattern was overall beneficial, but I was often confused as to how strictly I should adhere to the MVVM pattern. MVVM says each view should have an accompanying view model and model. However, with an app containing so many design elements, it often felt unnecessary to have a data model tied to each view. What would the model be for a modal and how would that be different from the view model?  
