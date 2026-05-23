# Use typescript in javascript projects

* Date: 2019-01-01

## Context and Problem Statement

JavaScript has been part of 100% of projects over the last 6+ years.
In addition to using pure JavaScript there are multiple languages available that
can be compiled to JavaScript and offer extensions to JavaScript.

## Considered Options

* none
* [TypeScript](https://www.typescriptlang.org/)
* [CoffeeScript](https://coffeescript.org/)
* [Kotlin](https://kotlinlang.org/docs/tutorials/javascript/kotlin-to-javascript/kotlin-to-javascript.html)

## Choosen Option

Use Typescript. If not applicable use standard JavaScript.

**Reasons**

* TypeScript adds basic function documentation without much overhead for documentation (just by defining the types)
* TypeScript is well established (e.g., in [VisualStudioCode](https://code.visualstudio.com/docs/languages/typescript)) in modern IDEs and enables completion helpers out of the box
* TypeScript allows for typechecking prior to compile-/run-time
* Typescript can be [configured](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html) to fit the demands of a project
* TypeScript is standard language for major frameworks like [Angular](https://www.typescriptlang.org/docs/handbook/angular.html) and can be integrated easily in most framework CLIs (e.g., [create-react-app](https://facebook.github.io/create-react-app/docs/adding-typescript))
* TypeScript is a superset of JavaScript that adds language features without changing the core components of the language. Most extensions are based off of discussions that will eventually be added to the ECMAScript core itself (e.g.,[async/await](https://github.com/tc39/ecmascript-asyncawait)).
* Other alternatives (Kotlin, CoffeeScript) are [less established](https://stackshare.io/stackups/coffeescript-vs-kotlin-vs-typescript)
