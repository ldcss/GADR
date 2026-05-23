# 11. artist-images-from-spotify

Date: 2019-09-08

## Status

2019-09-08 accepted

## Context

Korin would look much better with artist images. Unfortunately LastFm [removed artist images][lastfm-images-gone] from their API and have replaced it with a placeholder. There are some options to get artist images which are:

- [Music story][music-story-api]: The documentation is not easy to understand and the SDK is designed for web browsers. It also uses a custom ID to associate artists, not IMDB. One unique feature is that it has lyrics too.
- [Music brainz][music-brainz-api]: Creative commons but has everything except artist images.
- [Spotify][spotify-api]: Has artist information including images but uses a custom ID, not IMDB.

## Decision

Spotify is the only viable alternative.

## Consequences

Use Spotify API

[lastfm-images-gone]: https://getsatisfaction.com/lastfm/topics/api-announcement-dac8oefw5vrxq
[music-story-api]: http://developers.music-story.com/developers/picture#c_artist
[music-brainz-api]: https://musicbrainz.org/doc/Artist
[spotify-api]: https://developer.spotify.com/documentation/web-api/reference/artists/get-artist/
