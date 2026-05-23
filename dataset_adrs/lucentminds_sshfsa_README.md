# Architecture Decision Records
11-29-2016
From: https://www.promptworks.com/blog/the-cure-for-architectural-amnesia

Great, so you've decided that you want to make your very first Architecture Decision Record. I'll walk you through the steps you should follow.

First, create the file! Name it something like 001-adopting-python3.md. You'll want these to be sequential, of course.

Next, give it a title, which should be short and to the point:

```markdown
# Title
ADR-001: Adopting Python 3
```
These should be short enough to fit in a commit message.

Next, even though our record should be short, we should give a summary. For example:

```markdown
# Summary
We decided to upgrade from Python 2 to Python 3 to support Unicode
better.
```
This should be super short and concise—maybe even 140 characters or less.

Next, the context describes the state of the system when the decision was made. It also records other external forces that come into play:

```markdown
# Context
We are currently using Python 2 everywhere. The users want to start
sending us Unicode characters in the API.
```

This should eventually become out of date, but still be contextually relevant! Without this context, the decision record might not make sense when reviewed in hindsight. And usually the implementation of this particular architectural decision will make the context out of date—but this is fine!

Next, the decision is made up of full sentences, in the active voice:

```markdown
# Decision
We will migrate to Python 3 for services X, Y and Z.
```

After this, the next section should list all consequences (not just the benefits) to the decision, including what could go wrong.

```markdown
# Consequences
We will be able to handle Unicode characters, but we might have to
provide backwards-compatible support for some dependencies that
haven't been ported to Python 3 yet.
```

Finally the status section should only be one of the following:

* Proposed
* Accepted
* Deprecated
* Superseded

The last two are the only time when a decision record should be modified after creation (unless something is found to be factually wrong in the record). Furthermore, in the case of “superseded,” it may be useful to provide a link to the decision record which supersedes it:

```markdown
# Status
Superseded by [ADR-002](/adrs/002-going-back-to-python-2.md)
```

## Put it under version control

Finally, either start a new repository just for your decision records, or make a directory in another repository, such as ./docs/adrs/, so they're easy to see all at once:

```bash
$ ls adrs
001-adoptiong-python-3.md
002-going-back-to-python-2.md
003-saying-screw-it-and-rewriting-the-whole-thing-in-visual-basic.md
```

You should put your decision records up for review like any other code change, so your teammates can check them for accuracy!

Once merged, your records should live in version control for perpetuity, and serve as a point of reference for future decisions and new developers.

## Choosing what to record

One concern I've heard with regards to decision records is that it's difficult to know what changes are significant enough to record.

Obviously, we can't record every single little change that we make to our architecture. Some things are truly small and discrete enough to actually be obvious.

My recommendation is if you find yourself weighing two or more options, doing research and extending into an unknown domain, or feel the need to inform your teammates of the change, then that is when a decision record is most relevant.

## Choosing when to record

Another concern is when to write the decision record. Just like the code you need to write, it should be started when the implementation of the change is started, and should be the last step in implementing the change.5

# Tips
* Immutable - Just status changes but numbers and content don't

* Need to be used in architecture meetings and aresentations. Separate text in presentations NOT allowed.

* Add a section for UML diagram where applicable. You may not big on UML but for complex parts add a UML diagram for later reference.