# 2. REST client for access on the OpenMRS API

Date: 2017-07-08

## Status

Accepted

## Context

In order to get information from the OpenMRS instance, HTTP requests need to be created.
There are various libraries with which this can be done:

- Using the standard Java SE API
- [OkHttp](https://github.com/square/okhttp)
- Jersey
- [Unirest](https://github.com/mashape/unirest-java)
- Apache Http Client
- Spring REST templates
- [DavidWebb](https://github.com/hgoebl/DavidWebb), a thin wrapper around `HttpURLConnection`

# Descision

Instead of an elaborate evaluation of the alternatives, this project will start with Unirest
as it seems easy to use and provides a rich set of features, e.g. [Jackson](https://github.com/FasterXML/jackson-docs) support.

Let's see if using this library is acceptable for users of this project and maybe change it later if not.

## Consequences

- The REST requests will have a very simple syntax
- Thus it might be possible for developers with little experience in this area to make extensions
- Unirest could be used on Android, but it might be necessary to add some workarounds (see [blog.mashape.com](http://blog.mashape.com/using-unirest-java-for-your-android-projects/))
- Compared to other options like using the core libraries or DavidWebb, Unirest will lead to bigger application packages
