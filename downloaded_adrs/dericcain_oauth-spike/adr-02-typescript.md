# ADR 2 - Static Types with TypeScript

## Context

When writing client side code, there are several choices for the language to use.

- Raw JavaScript
- Modern / proposed JavaScript (transpiled with Babel for better browser support)
- JavaScript with static types (TypeScript or Flow)
- Other languages that transpile to JavaScript (e.g. Reason is OCaml transpiled to JS, CoffeeScript was
  once the default for Ruby on Rails projects)

The industry standard choice is modern JavaScript transpiled with Babel. The emerging best
practice is JavaScript plus static typing. TypeScript and Flow are fairly comparable, with TypeScript
being more popular.

At Guidewire:

- The Enterprise pod has used TypeScript on smaller projects (payment-iframe-2, web-rating-poc).
- The original payment iFrame used Flow.

### Pros

- Types serve as additional documentation and supports IDE features such as autocomplete,
  especially beneficial for libraries which will be consumed by third parties
- Arguably safer / more correct code
- Arguably easier to maintain code

### Cons

- Higher learning curve for new developers and less standard than regular JavaScript (there is no ECMAScript standard for static types)
- More complex project configuration
- Arguably slower to develop in than raw JavaScript

### At Companies that Create Large SPAs

- Microsoft created, and extensively uses, TypeScript
- Facebook created, and extensively uses, Flow
- Google created Dart and AtScript; chose TypeScript for Angular2+
- Slack migrated their codebase to TypeScript

### Links

- "the morning paper" discusses use of Flow at Facebook: https://blog.acolyer.org/2017/11/08/fast-and-precise-type-checking-for-javascript/
- Microsoft uses TypeScript for Word Online: https://medium.com/web-on-the-edge/modernizing-word-onlines-ux-platform-df1050344e3a
- Slack ports codebase to TypeScript: https://slack.engineering/typescript-at-slack-a81307fa288d
- ThoughtWorks categorizes TypeScript as "Trial": https://www.thoughtworks.com/radar/languages-and-frameworks/typescript
- ThoughtWorks categorizes Flow as "Assess": https://www.thoughtworks.com/radar/languages-and-frameworks/typescript
- Microsoft hiring TypeScript devs for Skype: https://www.linkedin.com/jobs/view/software-engineer-messaging-javascript-typescript-react-xp-at-microsoft-779542439
- Microsoft uses TypeScript for their Office components library: https://github.com/OfficeDev/office-ui-fabric-react
- James Kyle's (FB employee, Babel contributor) stating static types are a best practice: https://discuss.reactjs.org/t/if-typescript-is-so-great-how-come-all-notable-reactjs-projects-use-babel/4887/2
- TypeScript at Google: http://neugierig.org/software/blog/2018/09/typescript-at-google.html
- Facebook converts Messenger.com to Reason (a statically typed, transpiled to JS language): https://reasonml.github.io/blog/2017/09/08/messenger-50-reason.html

## Decision

We will use TypeScript as a type checker but not a compiler. This means we are using JS + types, while
avoiding TypeScript's non-standard features (e.g. namespaces). This should ease the transition back
to regular JavaScript if needed.

## Status

Adopted. TypeScript is in use but could be removed with moderate effort (it may or may not be possible to
programmatically remove the type annotations).

## Consequences

- Additional project configuration is being maintained.
- We perform type checking as a prepush git hook; this may catch some errors.
- We are shipping a types definition file which will be useful to some consumers of the library.
