# 8. Build off lbh-frontend rather than govuk-react

Date: 2019-10-30

## Status

Accepted

## Context

We need to be consistent with the Hackney styles within lbh-frontend. We could
derive styles from [lbh-frontend](https://github.com/LBHackney-IT/LBH-frontend),
while reimplementating the HTML and JS. We could also use
[govuk-react](https://github.com/govuk-react/govuk-react), a repository
pre-built that derives from
[govuk-frontend](https://github.com/alphagov/govuk-frontend), and then apply the
modifications from lbh-frontend to it. The repository for govuk-react has a
large amount of issues raised against it, which may also be issues we would run
into if we worked off the repository. It is also built using
[styled-components](https://www.styled-components.com/) for styling, using a
reflection of a version of govuk-frontend, meaning updates to govuk-frontend
will require the respective CSS to be updated. Given that lbh-frontend also
utilizes SASS, we would run into the same problem again.

## Decision

We will create a React component library that derives the styles from
lbh-frontend, and will reimplement the HTML and JS so that it works correctly in
a React environment.

## Consequences

We will be able to use the styles from lbh-frontend and will have to build each
React component to match previous implementations from lbh-frontend and
govuk-frontend. We will not inherit any of the issues that may have previously
affected govuk-react at the risk of creating our own.
