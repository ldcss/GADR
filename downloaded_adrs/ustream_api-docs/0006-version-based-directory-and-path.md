# 6. Version based directory and path.

Date: 2017-06-08

## Status

Accepted

## Context

Old or specific versions of a documentation can not be accessed. 
Only the actual version exists online. Every project's documentation
is in the same directory, no structure.

## Decision

Create project specific directories under the `/_posts` directory and
create version numbered directories e.g.: `/_posts/android/1.0`,
`/_posts/ios/2.1`. Put each documentation file (`README.md`, `CHANGELOG.md`, ...)
inside the version numbered directory.
Create one YAML Front Matter index file for each product which points 
to the latest version, see example below where latest version is `0.5`.
Use the `permalink: /player-sdk/android/latest` key to specify where 
the latest documentation is accessible online, like: 
http://developers.ustream.tv/player-sdk/android/latest
  
```
/_posts/android/2017-01-01-readme.md

---
layout: markdown
title: Player SDK for Android (v0.5)
weight: 30
category: player-sdk
categoryItemType: documentation
categoryItemIsShown: 1
categoryItemWidth: 6
categoryItemDescription:
categoryItemLabel: Read the documentation
permalink: /player-sdk/android/latest/
---
{% include_relative 0.5/README.md  %}
```

Change the `include_relative` setting to include the latest version.
Use the `categoryItemIsShown: 1` setting to direct Jekyll to show 
this document when listing category contents.

Create a YAML Front Matter index file in each version numbered directory
in which the version is specified, example:

```
/_posts/android/0.5/2017-02-02-readme.md

---
layout: markdown
title: Player SDK for Android (v0.5.x)
weight: 3
category: player-sdk
categoryItemType: documentation
categoryItemIsShown: 0
categoryItemWidth: 6
categoryItemDescription:
categoryItemLabel: Read the documentation
permalink: /player-sdk/android/0.5/
---
{% include_relative README.md  %}
```

Use the `categoryItemIsShown: 0` to hide this version from category listing, 
as only the latest should be listed.

Previous version can be accessed online using urls like:
* http://developers.ustream.tv/player-sdk/android/0.4/
* http://developers.ustream.tv/player-sdk/android/0.5/
* http://developers.ustream.tv/player-sdk/android/latest/ - which only points to `0.5` 

## Consequences

Each platform/project has its own directory. Each version has its own directory 
under its project. Previous versions can be addressed/linked easily:
`http://developers.ustream.tv/<project>/<platform>/<version-number>`.
Latest version is always accessible online using the schema:   
`http://developers.ustream.tv/<project>/<platform>/latest`.
Changelogs can cross-reference earlier versions. 
