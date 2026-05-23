# 3. All content will be translated

Date: 2019-05-01

## Status

Accepted

## Context

To allow this project to be used by other parties (mostly non-Dutch speaking), it will be necessary to be able to translate all content in the application that is not coming from the APIs.

## Decision

The application's content will be stored in translation files. The code will make use of [React-Intl](https://github.com/formatjs/react-intl). Also see the [i18n documentation](https://github.com/react-boilerplate/react-boilerplate/blob/master/docs/js/i18n.md) in the [react-boilerplate repository](https://github.com/react-boilerplate/react-boilerplate).

## Consequences

None of the components or containers can have hardcoded text or labels. Everything needs to be stored in and come from the [translation files](../../app/translations).

In turn, it will be a lot easier to provide translated content when required.

Note that, in order to have snapshot tests passing, [the full-icu package](https://www.npmjs.com/package/full-icu) needs to be available as a globally installed NPM package in the environment in which builds need to be run. OSX has support for ICU, but Linux doesn't always. The package will be installed in the [Docker container](../../Dockerfile#L31).
