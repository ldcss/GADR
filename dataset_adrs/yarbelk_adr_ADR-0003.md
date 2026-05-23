# ADRs should have a Writer/Reader interface

*Number:* ADR-0003

*Created:* 2019-03-29 04:18:03 +0000 UTC

*Status:* DRAFT

*Authors:*
- James Rivett-Carnac


# Background

The initial pass at writing this was 'get init, new and render' working
as fast as possible.  As such, there is a lot of inline opening and closing
of files; and this makes it "hard" to test.

# Complication

By "hard" to test, I mean I can only YOLO it and test from the command line.
This means I miss things like the fact that multiple authors are not rendering
correctly.  It also makes it much more annoying to work with and see what
is going on in the code

# Options Considered

1. this interface
```
Read(*ADR) (ok bool, err error)
Write(*ADR) (n int, err error)
```
Not quite an `io.Reader`, but it is a domain specific reader.
I *know* I want an ADR out.  The details of it are implementation
specific.

Might need to have this as well:

```
func New(MarshalerUnMarshaler, io.ReadWriter) (ADRRepo) {}
```
Which exposes a
2. maybe something else: like the Marshal/Unmarshal interface
from JSON?

```
Marshaler {
  Marshal() ([]byte, error)
}

UnMarshaler {
  UnMarshal([]byte) (error)
}
```

The problem with this is that its more the domain of
the encoding; and from an end user point of view (cobra.Command)
I don't care.  I just want to 'read from this file', write
to 'that file'.  the marshal/unmarshal stuff is entirely
interchangable.

# Decision

Going to start with some kind Reader/Writer idea that
takes in a marshaler/unmarshaler.  that way later
we can do things like, configurable rendering and 
swappable encoding (YAML, XML <bleh>)
using the same abstraction

# Outcome

