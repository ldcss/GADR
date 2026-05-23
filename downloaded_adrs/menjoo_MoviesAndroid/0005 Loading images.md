# Use a library for image loading or write image loading code myself?

* Date: 2018-04-23

## Considered Options

* Picasso
* Glide
* None, write the code myself

## Decision Outcome

Chosen option: "Picasso", because it will produce highly performing image loading code. And one 
should not try to reinvent the wheel. The libraries are open source and well maintained for years.

Positive Consequences: 
* Less code, cleaner code
* High performance
* Highly adopted

Negative consequences: 
* Dependency itself. If they will ever be deprecated, work is needed.

## Pros and Cons of the Options

### Picasso

* Good, because lower footprint in Kb
* Good, because lower footprint in method count
* Good, because loads images slightly faster 
* Bad, because uses more memory

### Glide

* Bad, because higher footprint in Kb
* Bad, because higher footprint in method count
* Bad, because loads images slightly slower 
* Good, because uses less memory

### Do it yourself

* Bad, because will contain bugs
* Bad, because has to be maintained
* Bad, because wont perform as well
* Good, because no dependency

## Links

* [Picasso or Glide comparison](https://medium.com/@multidots/glide-vs-picasso-930eed42b81d)
* [Picasso](http://square.github.io/picasso/)
* [Glide](https://github.com/bumptech/glide/)
