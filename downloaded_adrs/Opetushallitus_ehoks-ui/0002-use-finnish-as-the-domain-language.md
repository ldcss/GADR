# 2. Use Finnish as the domain language

Date: 26.03.2020

## Status

Accepted

## Context

There are currently mixed conventions of translating domain words. For example mobx-state-tree-model properties are
in Finnish but react component props in English even though data might be exactly the same.

## Decision

We will use Finnish as the domain language (e.g. osaamisenHankkimistapa, koulutuksenJarjestaja) and English when
the word is not directly related to eHOKS domain. Words are refactored gradually so there might exist mixed
conventions quite some time.

Here is one expample:

```typescript
interface LearningEventProps {
  className?: string
  title?: React.ReactNode
  isDemonstration?: boolean
  size?: "small" | "large"
  description?: string
  startDate?: string
  endDate?: string
  periodSpecifier?: string
  demonstrationEnviromentDescription?: string
}
```

className, title, size, description, startDate, endDate are technical or generic words and should be in English.
Demonstration and demonstrationEnvironment are domain and datamodel words naytto and nayttoYmparisto and should be in
Finnish. PeriodSpecifier is straight from the data model and thus should be ajanjaksonTarkenne. LearningEvent is used for
both osaamisenHankkiminen and osaamisenOsoittaminen and there isn't domain word to describe these both so learningEvent
should stay as is, although probably best option would be to split learningEvent component to OsaamisenHankkiminen and
OsaamisenOsoittaminen components.

Example fixed:

```typescript
interface LearningEventProps {
  className?: string
  title?: React.ReactNode
  isNaytto?: boolean
  size?: "small" | "large"
  description?: string
  startDate?: string
  endDate?: string
  ajanjaksonTarkenne?: string
  nayttoymparistoDescription?: string
}
```

## Consequences

Translation causes confusion and misunderstandings. It's clearer when one ubiquitous language for domain is used in
coding and when talking to domain experts.
