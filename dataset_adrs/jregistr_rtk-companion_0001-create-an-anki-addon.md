# Create an Anki Addon for RTK

* Status: accepted
* Date: 2020-08-20

Technical Story: 

Create an Anki addon for browsing and creating notes for Kanji from the
6th edition of RTK.

## Context and Problem Statement
Rather than using a user uploaded deck for RTK, I decided to create cards as
I go through the book. The user decks I went through sometimes would have cards in an 
odd order or would just contain fields I care not about. 

Also, I wanted to make an Anki addon to exercise my rusty python.

Creating own cards though is quite involved. It usually goes something like this:
1. Lookup the kanji number in [Koohi](https://kanji.koohii.com/).
1. Copy paste into Anki. Write the number and keyword in Anki.
1. Browse Koohi stories for inspiration. 
1. Look up radicals in Jisho for inspiration.
1. Write the story in Anki.
1. Find stroke order image/gif (usually done by taking a screenshot on [Jisho](https://jisho.org/))

## Considered Options

### Chrome extension to extract svg stroke order for Kanji

Make a chrome extension with a one button click to get an svg or png of the stroke order
diagram from Jisho for a given Kanji.

### Anki addon - Gather all data
Anki addon that has all the data for the RTK kanji in one place.

## Decision Outcome

Chose to experiment with making an Anki addon housing all the information I was using to create
RTK notes displayed in a way that allows easy browsing between Kanji.

The addon should create a window that displays a Kanji along with:
- Heisig number (Edition 6)
- Keyword
- List of radicals
- Stroke order gif and/or image
- Shared stories on Koohi for kanji

Lastly, it should have a button to add a new note to an existing deck for the currently viewed
Kanji.

## Pros and Cons of the Options <!-- optional -->

### Chrome extension to extract svg stroke order for Kanji
* Pro: easy way to copy stroke order for Kanji
* Con: All other manual labor remain

### Anki Addon
* Pro: Gather all information into Anki, no need to switch application windows.
* Con: New to Anki addons development

## Links

* [Kanji Koohi](https://kanji.koohii.com/)
* [Jisho](https://jisho.org/)
* [Authoring Addons](https://addon-docs.ankiweb.net/#/)
