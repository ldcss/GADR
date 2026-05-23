## ADR 4: Choosing a Framework
July 26, 2019

### Context
While being a novice to C# and WPF, I thought it might be helpful to adopt a popular framework to make the development process easier and remove some of the unnecessary "gotchas" of writing in a new language. Using a framework might also quicken the pace of development and remove the need to write many helper classes.

### Decision
The Galaxy Zoo touch table app will not use a framework. Adopting a framework seems like a shortcut to learning the basics of C#, and I want to focus more on _how_ the language works rather than than simply getting something working. Also, a framework might cause a lot of overhead if only a few aspects of the framework are being used. Learning a new framework along with learning C# and .NET might be overwhelming.

### Status
Declined

### Consequences
While some frameworks are well documented (MVVM Light), others are quickly becoming deprecated (Silverlight), so there is a worry that any framework could soon lose favor in the .NET community. By declining the use of a framework, there is the potential of adding more dev time that will be spent creating a messenger, view model base, and other components often found in a WPF framework.

_In Retrospect:_ After becoming more familiar with WPF, I wish I had chosen a framework (perhaps MVVM Light) to achieve some of my needs for this app. For example, although I created my own messenger based on a Stack Overflow post, I often ran into issues with the messenger and was unable to find advice on Stack Overflow as most of those answers reference the MVVM Light messenger. I don't think MVVM Light would've been a huge load on the code. It's likely using a framework could've cleaned up some sections of code. I can see the merits of declining a framework for novices to WPF, but I don't think much is gained from going without.
