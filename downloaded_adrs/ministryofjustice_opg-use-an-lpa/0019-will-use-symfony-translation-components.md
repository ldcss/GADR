# 19. Will use Symfony translation components

Date: 2020-08-17

## Status

Accepted

## Context

We need to provide translation capabilities in a way that slots into our twig based rendering pipeline

## Decision

We're going to use symfony/translation to provide the translation capabilities

## Consequences

By using symfony/translation we'll be able to use the symfony/twig-bridge package which gives us a
much easier implementation path for translation. The chief difficulty being the automated extraction
of translatable strings.
