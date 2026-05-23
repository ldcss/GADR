# 6. A state requirement

Date: 2020-06-14

## Status

Accepted

## Context

Just trying to implement bookmarks and I have come across something interesting.

We have a ui element that looks like this:

```html
<a href="javascript:application.bookmarks.add('gbj1jf')" class="bookmark">bookmark</a>
```

Which means "on click, please bookmark the news item with id 'gbj1jf'".

The bookmarking use case looks like this:

```js
bookmark = new Bookmark('id-a', 'http://abc', 'src-rnz');

await application.bookmarks.add(bookmark);
```

It is expecting more information for bookmarks so that it can be used later without any further lookups. 

We don't wish to have to look it up, especially since it may no longer exist in our sources -- and we don't want to store every single
article just for this purpose.

We don't really want to bake all the information into the link, either, that seems wrong for some reason. 

And we don't really want to add arguments to `application.bookmarks.add`, that also feels wrong.

## Decision

Introduce some idea of state in to `Application` so that it can handle notifications like this. 

It seems like simplifying UI elements is a good idea.

Another option is giving this responsibility to the view element. But then how do we let it know?


## Consequences

### Tests affected

We have introduced some internal state, and to check the bookmarks we have to populate that state.

Rather than make that state a port we are seeing what happens when it remains concealed, which means our test now has to invoke two use cases.


