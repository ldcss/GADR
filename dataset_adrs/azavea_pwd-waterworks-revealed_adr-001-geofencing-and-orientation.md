# Assess HTML5 Geofencing and Device Orientation Viability

## Context

PWD Waterworks Revealed is a mobile application enabling users to view
designated spots around the Waterworks museum on a map in order to visit those
spots, then browse through historical photographs by orienting the device in a
way that matches the orientation of the original camera.

The app was originally built using PhoneGap; we intend to rewrite it as a mobile
web application using React and HTML5 device geolocation and orientation APIs.
This ADR constitutes a quick assessment of these APIs capabilities and limits,
and includes a few suggestions for things we should consider as we adapt it
from PhoneGap to React.

## Geolocation and Geofencing

[The Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation)
seems developed enough to render a more-or-less accurate lat/lng to plot on a
Leaflet map and intersect with an existing area of interest for a geofence.

We used [Cordova Plugin Geolocation](https://github.com/apache/cordova-plugin-geolocation)
to manage location services in the origina PhoneGap prototype. This plugin has
an interface modeled on the browser geolocation API spec and seems to use
device-browser-specific implementations under the hood.

### Capabilities

In both Android Chrome and iOS Safari it seemed as if new React prototype's use
of the geolocation API was roughly similar, very precise, and generally
accurate -- with some limitations.

### Limits

While the geolocated coordinates were very precise and updated regularly enough
to work with large geofences (10 - 100 meters at least?), these coordinates
were routinely not accurate at the level of feet, which is the level we would
ideally prefer in order to make geofence detection the primary way users
interact with the app.

That said: we seem to have received reports that the original app wasn't always
accurate at the level of feet, and [had issues activating some clustered zones](https://github.com/azavea/pwd-waterworks-revealed/issues/175).
Additionally, even the most accurate iOS native location services API accuracy
seems to be within 10 meters rather than 5-10 feet.

Lastly there are some limits related to the user's device settings: iOS users
can disable Safari's geolocation API as a whole -- and thus never see a prompt
for location. Likewise a React web app would have the same native hooks to know
when the app has been foregrounded or backgrounded, and in turn to stop or
resume geolocating. That said the browswer's [Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API)
may provide similar life cycle hooks to use.

### Recommendation

It seems like we can undertake some work to complement the less-than-ideal
accuracy of the geolocation values with other ways to detect the what zone the
user is in or around. Had we taken the PhoneGap app toward production, we would
have had to make similar computations for bugfixes, so I don't think we lose
much here. Additionally, we can probably revisit the original prototype's
implementation for some ideas about how to minimize any differences in accuracy
between old and new prototype.

However, we will also have to assume that it's possible -- maybe likely -- that
users will use the app without geofencing always working accurately. We should
consider having users manually select areas of interest to activate zones. We
would still show the user's location on the map in relation to the zones, but
would also account for the possibility that the geofence may not always work.

## Device Orientation

[The device orientation API](https://developer.mozilla.org/en-US/docs/Web/API/Detecting_device_orientation)
seems to me much more dependable.

### Capabilities

In testing the React prototype's usage around the office, the functionality
seemed to work as expected: the prototype app registered the device's
orientation with the level of accuracy that we'd need in both Android Chrome
and iOS Safari.

### Limits and Quirks

While testing we did notice that there is at least one major difference between
Android Chrome and iOS Safari support: namely, the direction heading value was
exactly reversed on Chrome when compared with Safari (or vice versa). In
practice this meant that a phone using Android Chrome and a phone using iOS
Safari would have to point in exactly opposite directions to align properly
with an image; in development this means we'll have to detect browsers and make
the logic for how this works subtly different.

One additional practical consideration is that the device orientation API event
listener issues new values really really rapidly so we'll need to ensure we
the constant stream of these values doesn't lead to a constant stream of costly
unnecessary React component rerenderings.

### Recommendation

The device orientation API seems more production-ready for our purposes. While
I do think we should intend to have some fallback interface for activating and
browsing through different zones' historical photographs, it seems viable to
design the application around the expectation that device orientation would be
the primary way to view those photos.
