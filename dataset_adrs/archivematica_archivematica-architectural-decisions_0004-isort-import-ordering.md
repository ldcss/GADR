---
layout: page
status: proposed
adr: "0004"
title: Isort Import Formatting
deciders:
date:
---

## Context and problem statement

Import ordering in Archivematica related projects is inconsistant and can be
a distraction from actual content.

The import style described by [PEP 8][0] is good, but not specific enough.

As with code formatting tools, automating import ordering simplifies developer
decisions and code review.

## Considered options

* [isort][1] - the standard, widely used
* [black][2] - black is considering making import reodering an option, but it
               hasn't happend yet

## Recommendation

isort, because it's well established. If black does add support, it may make
sense to move to it.

### Recommended format

* future
* stdlib
* third party
* artefactual libs (e.g metsrw)
* archivematicaCommon
* dashboard, mcpclient, mcpserver

For example:

```python
from __future__ import unicode_literals

import os

from lxml import etree
from django import forms
from django.conf import settings

from countryCodes import getCodeForCountry

from main.models import Derivation, File, FPCommandOutput, RightsStatement
```

[0]: https://www.python.org/dev/peps/pep-0008/#imports
[1]: https://github.com/timothycrosley/isort
[2]: https://github.com/ambv/black/issues/333
