# Use a HTTP library or write the HTTP code myself?

* Date: 2018-04-23

## Considered Options

* Retrofit with OkHttp
* OkHttp only
* None, write the code myself

## Decision Outcome

Chosen option: "Retrofit with OkHttp", because it will produce highly performing clean networking 
code. And one should not try to reinvent the wheel. The libraries are open source and well maintained 
for years.

Positive Consequences: 
* Less code, cleaner code
* High performance
* Highly adopted

Negative consequences: 
* Dependencies itself. If they will ever be deprecated, work is needed.

## Links

* [Retrofit](http://square.github.io/retrofit/)
* [OkHttp](http://square.github.io/okhttp/)
