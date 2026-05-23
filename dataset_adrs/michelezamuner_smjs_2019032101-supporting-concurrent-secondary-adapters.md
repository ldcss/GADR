# Supporting concurrent secondary adapters


## Context

When we define a secondary port, the purpose is to allow different kinds of adapters to hook to that port. However, in the simplest case, the implementation of an application will only allow a single adapter to be attached to a port at the same time. For example:
```java
public interface Notifier
{
    public void notify(Message message);
}
```
```java
public class Logger implements Notifier
{
    @override
    public void notify(Message message)
    {
        logger.log(message.getMessage());
    }
}
```
```java
public class Provider
{
    public void register()
    {
        container.bind(Notifier, Logger);
    }
}
```

so a single type of adapter can be attached to a specific port at the same time, and that's obvious because the application services that use that port, will each expect to receive a single object as instance of that port. But what if we need to attach multiple adapters to the same port at the same time? In the example above, what if we want multiple notifiers to send notifications when the abstract message is produced, for example sending an email in addition to logging the message?


## Decision

The standard solution in this cases is using a message bus, so that multiple handlers can be registered to handle certain types of messages. What we can do, then, is creating a bus adapter that would work as a proxy that routes the messages to all registered handlers:
```java
public class BusNotifier implements Notifier
{
    public void notify(Message message)
    {
        bus.send(message);
    }
}
```

so we would still be attaching a single secondary adapter, but at the same time supporting multiple ones, like a logger, an email notifier, etc.

Of course the same application structure can be reused with no change whatsoever the moment we decide that we only need a single secondary adapter: we could then replace the bus adapter with the single adapter we need.


## Status

Proposed


## Consequences

Multiple secondary adapters can indirectly be attached to the same port at the same time, without hindering the application structure. 
