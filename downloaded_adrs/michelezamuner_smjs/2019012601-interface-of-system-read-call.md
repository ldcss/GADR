# System interface


## Context

Any architecture must have a way to communicate with the system over which the virtual machine is running, otherwise it wouldn't be possible to do any kind of input/output, thus for a program to perform any meaningful work.

We want to support different kinds of system abstractions: for example the operating system where a command-line virtual machine is running, or a system emulation over the Web that does input/output with the Web page.

To support this, we need to define a common interface for the System component, so that all possible architecture mods will know what they can do with it.

The main problem is that certain operations like `read` needs the concept of memory buffer to work, because we need to provide a buffer to it, where the read data will be stored. However, we don't support any concept of "memory" in our domain, so we cannot use anything like that to implement a buffer.


## Solution

The reason why the traditional `read` call returns the data in a buffer passed by reference, is that it also needs to return the number of bytes read, like:
```
int read(int fd, char** buffer, int count)
```

However, we're not bound to this interface in our System implementation: we can freely return a complex `Data` object, that will contain both the actual data that has been read, and its size, at the same time:
```
Data data = system.read(fd, count)
Size size = data.getSize()
```

Of course the actual implementation of the system will have to adapt this interface to the interface of the real system it's interacting with; for example, for a real operating system it could be something like:
```
class System
    read(Integer fd, Size count): Data
        Buffer buffer = new Buffer(count)
        int read = filesystem.read(fd, buffer, count)
        
        return new Data(buffer.slice(0, read));
```

## Status

Proposed


## Consequences

We're able to use generic systems with any architecture implementation.
