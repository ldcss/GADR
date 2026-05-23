# Handling generic Input/Output


## Context

Currently we use a single View from the Presenter, to render the normal output of the use case, that is bound to the View interface in the general provider. However, we're not handling different views that might be needed, nor error messages, which are directly written to the STDERR of the application.

Regarding the former, we're not allowing the user to choose the output representation she prefers to get. Regarding the latter, if we're decoupling the presenter from the controller to support segregation between input and output devices, we cannot then just assume that the input device will also be able to support output, like we're doing now.


## Decision

### Segregation of input and output devices

We assume that a generic application can be connected to several different input and output devices: this means that input may come from different input devices (for example keyboard and mouse), and the output may go to different output devices (for example `STDOUT`, a GUI, and the filesystem). Of course this requires us to drop the assumption that all usual Web applications make, that the input device is the same as the output device (a Web browser, or maybe a Web/application server to be more precise).

One of the objectives of modern architectures is exactly allowing multiple different output devices to be used by the same application, and also from the same input device. To allow this, it's necessary that the controller is oblivious of the specific output device that will be used: for example, the controller shouldn't know if the output is going to a GUI, a CLI, a log, an audio speaker or a combination of these.

It's also important to mention that the strict separation between input and output is an application-level concern, which expects input to come from an interface (input boundary), and to send output to a different interface (output boundary). This is important because the application doesn't need to care if the device providing the input is the same as the one receiving the output or not. However, in most cases the input device will also support some kind of output, at least to display errors of input validation, and it would be very weird if the input came from a device, and the output were sent to a different one, because the user using the first device would expect to see the output there as well. However, this kind of architecture easily supports also cases where the input device has no output capability, and the output is to be sent somewhere else (like a game controller and a monitor).

### Controllers and presenters

While a use case interactor performs its application logic, it may not need to perform a single presentation, for two reasons:
- there are many different kinds of presentations, that will likely need to be handled differently, like main successful output, and error output
- there are some presentations that will be produced immediately, like input validation results, and some that may be produced asynchronously, like command execution results

For this reason, the interactor will in general have to define several different presenter interfaces, instead of just one, and juggle the various presenters according to the application logic that is unfolding.

Now, we're describing this on the grounds that the presenters will be injected into the interactor. Now, in theory it's possible to achieve the same by returning a single response from the interactor, instead of letting the interactor call the presenters. This would actually work, and keep the dependency inversion principle respected, since the interactor still knows nothing of the details of presentation, however:
- we need to stuff all possible response cases into a single response object, instead of cleanly separate the various cases
- the controller will need to parse the response, understand what case it's about, and call different presenters according to it, adding much more responsibility to the controller than just having to translate the input data from the adapter format to the application format; additionally, the controller would really be just unpacking the same information that was packaged by the application, i.e. that a certain presenter needs to be called in a certain output situation, and the controller cannot deviate from this logic either, otherwise it would be taking presentation responsibility
- the single response object could be returning asynchronous output, in addition to synchronous one, so the controller will also need to check which part of the response should be treated as asynchronous (like attaching a callback to a promise), and which as synchronous
- even if the interactor was a coroutine (avoiding the problem of creating a single response for all cases), the controller would still need to check the kind of output at each return, and do the job of the interactor of associating a presenter to that kind of output, while the interactor already knows this information in the first place, in addition to still having to handle asynchronous output

For these reason, although returning the response from the interactor is technically feasible (and in certain scenarios it's certainly the best solution), it cannot be chosen as the general approach to use: rather it should be regarded as a special case, that works best only in specific situations.

### Presenters and views

Each specific presenter that can be used to implement the output port represents a specific output model, which is characterized by the set of view fields and data type conversions it supports, or in other words, the kind of view model it will produce. For example, a "screen" view model might convert the application response to a certain set of fields of certain type, with the intent of having them being displayed to a screen, while a "print" view model might produce from the same application response a different set of fields, of different types, specialized for being sent to a printer.

Still, the same view model, representing a certain output model, can be rendered on the selected output device in different ways: a "screen" output model, containing fields belonging to a screen representation, might still be rendered as an HTML page, or as TXT file, or again as a graph. All these alternatives are represented by different views. This means that a specific presenter component, for example the "screen" presenter component, will define a "screen" view interface, that will then be implemented by multiple actual "screen" view instances, like HTML screen view, graph screen view, etc., one of which will then be selected and injected in the presenter, to be used for rendering.

### Input definition

We borrow a definition of "input" from the REST standard. According to this definition, an input will be made of:
- a resource identifier (for example `/path/to/my/resource`, URI in the Web context)
- some input parameters (for example `?some[]=value&some[]=other`)
- a resource representation (for example `.html`, `.pdf`, etc.)

this means that:
- the identifier is used to pick a couple of controller and action, that needs to be called to perform the requested use case
- the parameters are just passed to the action when it's called
- the representation is related to the specific view that will be used to render the output generated by the use case's presenter; additionally, once a view is selected, it's presenter is also chosen, because a presenter might have multiple views, but a view only belongs to one presenter

For example, let's assume we have an `entitiesList` control widget, which displays a specific representation of a list of entities. When we trigger the `update` event on the `entitiesList` control widget, a very specific input can be created: the identifier would reference the controller and the action, like `entitiesController.update`; the input parameters could perhaps be the name of a subset of entities that this specific widget is configured to represent; finally, the representation is related to the specific widget that is sending this input, meaning that the same resource needs different widgets to be represented with different views.

### Using a router

The interesting problem that arises is that the view to be chosen is known at input time, because it's related to the representation: this may lead to think that it should be known by the controller. However, the controller should be independent from any choice regarding the output, including which representation is used.

A solution can be to introduce a *router* component, that takes an input, and chooses a combination of *controller*, *action* and *view* according to the given input. This is much like what happens with usual MVC Web framework, but generalized for any kind of adapter. This choice made by the router can be statically configured, since it does not depend on the user input.

The input part is quite easy, in that the router needs just to create the right controller object, and call the right action method on it, passing the right parameters. The output part is trickier though: since the controller is decoupled from the presenter, it doesn't return any output object that can be then handled by the router, rather it forwards the execution to the presenter object, in a way that isn't in control of the router. What the router can do, though, is to select the correct view to be used, and use the container to bind it to the generic view interface. This way, when the presenter will be built, the right view object will automatically be injected into it.

### Main output and side output

A typical application can have many different kinds of output. One of these is used to talk back to the user that provided the input: we can call it *main output*, and it would be produced by the selected use case. The *side output* would be any other kind of output produced by the application, like logging, monitoring, etc., which is not directly related to the input, and usually is not expected to be received by the user who produced the input.

While the main output is handled with a presenter, side output can be handled by using a message bus to send it to a non-specified recipient from the application layer: inside the adapter, then, one or more configured handlers will receive the messages, and output them to the configured devices.

As a case study, we can consider the verbose output of a console application. At first, this may seem a case where some side output (info logs) need to be redirected to the main output (console STDOUT). What's really happening, though, is that the side output is being produced in a way that is completely unrelated to the presenter and views used by the main output: messages are sent containing the side output, and then in the adapter a new handler is configured to listen to these messages, and print them to the same output device used by the main output. This way we can print to the same output device, but keep the two kinds of output completely independent.

### Handling errors

We can identify three broad categories of errors: application errors, input errors and system errors. Errors generated by domain or application services can be caught inside the use case, and passed back to the presenter in the response. Input errors are related to wrong input, or input that doesn't pass validation, and they are again checked inside the application interactors: they shouldn't be handled by controllers, because controllers have no way to select a specific output device to forward errors to, and additionally it's better if controllers stick to their single responsibility of translating data using adapter-specific format, into request data using application-specific format; on the other hand, we can say that the use case interactor is taking the role that so-called "controllers" have in traditional Web applications, meaning validating input, using proper services to produce an output, and send the output to the proper presenter/view. Finally, system errors are programming or configuration errors that may happen in the adapter-specific code, and that are generally caught during development, but which may still happen in production, and make the application crash: since these errors might happen outside of the application logic, they cannot be handled by the application service, like application and input errors, but still they should be caught and displayed on an output device to notify the user.

System errors, not being generated inside the use case, don't concern any use case, and as such they don't need to be handled by any presenter. The way to handle them is to let any piece of code that is catching them sending a message to a widget that is responsible for displaying error messages, without needing to go through any application logic. Errors generated by domain or application services can be caught inside the use case, and passed back to a specific error presenter, which in turn will be configured with a specific view to be used in that situation.

### User interface widgets

Any user interface, whether graphical or not, is composed of widgets, representing specific contexts for user interaction and presentation of data.

User interfaces are meant to be frequently changed, so they need to be as flexible as possible. To support this, widgets have to be designed so that they are as independent, reusable and replaceable as possible. A key tool to achieve this is using an events mechanism: instead of knowing of the existence of a specific widget, and calling a specific method on it, we send an event, and widgets that are interested in that event will respond to it with some action. This way we can easily replace widgets, or add new ones, without disrupting existing functionality.

Events can be generated by the domain, the application, or the widgets themselves. Thus, widgets must be allowed to know about all existing events. Of course who generates an event depends on where the event belongs to: if an event represents the completion of a domain task, then the domain will need to send it, whereas if an event represents the change of state of a graphical widget (not related to any application or domain concern), then the widget should send it.

Sometimes, however, it's not possible, or not convenient, to interact with widgets using events. For example it can happen that we need to be sure that a specific widget is actually called, but the event system doesn't ensure that any widget will respond to the event: for example if we want to display an error message, it doesn't make sense to send an event, hoping that a message box widget will catch it, rather we want to make sure that the message is actually displayed the way we need. To support these cases, widgets' actions must also be callable directly.

Widgets can then be just regular objects, exposing a set of methods: these can both be registered as event handlers, to be automatically called when certain events are caught, and be called directly on the object itself. This way we can take into account any possible combination of input and output methods, without creating a taxonomy of widgets that can have input and output, or only input and not output, etc., which is not really relevant on the user interface layer.

### Widgets and use cases

The model of the communication with the application layer (i.e. with a port) distinguishes controllers from presenters, where the first are responsible for handling input, and the second are responsible for handling output. The reason why the two must be separated is that the presenters need to be injected into the use case interactor, since it may need to call different kinds of presenters in different situations, and also in an asynchronous fashion, and these are concerns of the application layer, not of the adapter.

Of course the use case interactor knows nothing of which widgets are used in the adapter, nor of the kind of user interface there is, so it cannot decide to update widgets: rather, the interactor defines some presenter interfaces representing the kinds of output it needs to perform, and then it is injected with the presenters of the actual widgets that are selected to be used.

However, from the point of view of the adapter layer (user interface), we don't necessarily need to separate controller objects from presenter objects. For example, an "entity list" widget might have a "load" controller action, that can be called directly to load entity data from the application, or as response to an event: this action will delegate to the "list entities" use case interactor, which will go through the query model to fetch the entities, and then call the given presenter to display them. In this case, the presenter will be the "entity list" widget itself, having a "fill" method for example, to fill the list with data. From the point of view of the interactor, it's enough that the entity list (or an adapter of it) implements the interface required by the interactor.

In the previous example the use case interactor will likely need to be injected also with an error presenter to display possible errors: this presenter can perhaps be implemented by a message box widget. Now, since the list widget will be injected with the interactor, it won't be required to know of the existence of the message box widget, nor of the fact that the list widget is used as a presenter itself, because these things are decided in the application configuration (the provider).

Additionally, this is one of those situations where a method should only be called while going through the application layer: we cannot call the "fill" method with random data, because the list widget need to contain domain entities that have gone through the application logic. However, since this method is public (whether it is meant to be just an event handler or not), nothing prevents some other object, or widget, from directly calling this method passing in somer random data, so we are left to the discipline of the implementer to remember to never call this method directly, but only as a handler of the proper application event. This risk is however mitigated by the fact that we're anyway following the discipline of letting the controller be known only by those few objects that really need to call it directly, by virtue of dependency injection: for example, the main application widget will likely need to use the entity list widget to call "load" or "show" on it at startup, but this is likely the only object that will have a reference to it.

Regarding widgets that display data, each widget is a specific view, or representation, of the data: this means that we can have different widgets (even at the same time) representing the same data, and thus using the same presenter. This means that presenters and controllers are not really part of the widgets themselves, but are actually distinct objects, that are used by one or more widgets. For example, we may have multiple different widgets dealing with weather data: one would display a graph of temperatures over time, another will display a geographical map with different colors for different temperatures, etc. All these widgets will need to use the same presenter, which converts the entities data coming from the "show temperatures" use case, to simple values: then, each different view will use the same values differently. So, when the graph widget receives the signal that temperatures have been updated, it uses the shared "show temperatures" controller to trigger the use case, which will have the presenter injected: now this presenter must be able to communicate with multiple different views at the same time, and the actual views may change during the execution, because we may hide some widget for example. So, the view interface used by the presenter won't be an actual object interface, but just a messaging protocol, and the interactor will be injected with a message bus, and calling the interface would mean sending a "present" message, to which any number of actual views can respond.

A similar situation happens when the same controller is called by multiple event handlers, or methods, of the same widget, like "load" and "update" on the entities list: both will have to go through the "list entities" controller action, delegating to the same use case interactor.

The application has two ways to communicate with the widgets. The most direct one is just calling the presenters that have been injected. However, the application can also send messages, to which widgets may respond. However, since calling a presenter may also be done by sending messages (in case we need to support concurrent presenters), there's not much difference between the two from a technical perspective. The real difference lays in the fact that presentation methods are meant to communicate to the adapter that the main output has been produced, while any other message is meant to communicate side events that happened, and to which someone may want to respond. If we're injecting a presenter object, it's important that the main output is communicated through that object, and not through sending messages, to keep the intent of the communication clear. If we're using a message bus to communicate with presenters too, it's important that messages are properly named, to make it clear which are sending back the main output.

### Examples of presentation situations

A common situation is the one where we create a new entity, from a view that doesn't need to be updated to display the updated entity data:

Use case, "create order":
- given I'm in the checkout view
- and the cart has valid information
- when I request to create a new order
- then a new order is created with the cart information
- and I am notified of the successful order creation

Use case "error creating order":
- given I'm in the checkout view
- and the cart has invalid information
- when I request to create a new order
- then no new order is created
- and I am notified of the error with the cart information

Let's say we have a GUI adapter, with a checkout window (view) and an orders window (view). The checkout window will have a "create order" control with a method that takes the data from the "cart" widget, crafts a use case request from it, and uses it to call the use case interactor, which will have been already injected with a "message box" widget as both error presenter and result presenter. When the interactor is called, it first does validation of the request data, immediately calling the error presenter if the validation failed, or using the command model to request the creation of a new order otherwise. The command model will be executed asynchronously, to avoid blocking the user interface: this will create the order, update the storage, and send a message when the operation is completed. This message is caught by the interactor again, which uses the result presenter (asynchronously here) to notify that the order has been succcessfully created. At this point, the user can use the "list orders" use case to open the orders window, whose interactor will just read the data from the denormalized storage and present it.

Let's see now a case where we create a new entity in the same view where all entities are listed:

Use case, "create todo item":
- given I'm in the todo list view
- and the item form has valid data
- when I request to create a new todo item
- then a new todo item is created with the given information
- and the todo list is updated to show the new todo item as well

Use case, "error creating todo item":
- given I'm in the todo list view
- and the item form has invalid data
- when I request to create a new todo item
- then no view item is created
- and I am notified of the error with the item information

Here we have a single window, which is the todo list view, with the following widgets: an "item" form, a "create new item" button, a todo list, an error box, and a loader widget. When the user loads the window, the "list items" use case is performed, meaning that an input is sent to the "load" action of the todo list, which will create a request for the "list items" interactor, which will be injected with the list presenter, and will use the query model to get all the currently stored items from the denormalized database, which will be used to create a response, which will be sent to the todo list presenter to be displayed in the widget. Then, when the user clicks the "create new item" button, its controller will read the data from the form, craft a use case request with it, and send it to the "create item" interactor, which will be pre-injected with the error presenter, and the result presenter: if the request data is invalid, the error presenter will be sent a response containing the validation errors, and the interactor will return, otherwise the interactor will asynchronously call the command model to create a new todo item, then call the result presenter to signal that the request has been accepted (this could perhaps trigger a loading animation to start), and finally call the result presenter again to signal that the request has been completed, from inside the event handler of the command model completion event. In the meanwhile, the todo list controller was already register to respond with the "update" action to the message that is sent by the command model after the creation of an item is completed, so as soon as the command model signals the termination of the job, the todo list controller is called, triggering the "list items" use case again to update the todo items in the list with the current values, containing also the new one. The same form widget can have a controller registered to respond to the creation started message: this way if the request fails because of validation issues, the information present in the form fields is maintained to allow the user to fix it without re-typing everything, but if instead the validation passes, the form can clean its fields to allow a new item to be added next. All of these are purely GUI concerns, and that's why they aren't handled by the interactor, which must be concerned only with what is explicitly mentioned in the use case scenarios.

A less common case is the one where input data comes from a source that doesn't support any output, or is not interested in getting any. In actuality, this should be described by the application layer, because we can't use an adapter that doesn't support an output, with a port that provides one, because the role of the adapter is to support the use cases defined by the port. Thus, we can think of a use case that doesn't produce any outout.

Use case, "signal activates actuator":
- when the sensor sends a new signal
- then the actuator is activated

Here the interactor receives an input, in the form of a signal, but then produces no output, because activating the actuator is a secondary concern, adn the sensor doesn't support any output, since it can't even receive data back from its adapter. 

### Sloth machine views

Being a command-line application, the Sloth machine uses the process as the input device, and the process itself, in addition perhaps to the filesystem, as output devices. In particular, we want to use the exit status and the STDOUT and STDERR as main output devices. It's important, though, to highlight that these same devices can be used also to render output coming from the program that is being executed by the virtual machine, in addition to the virtual machine itself, and they can also be used to display side output, for example information messages in a verbose configuration. For this reason, we should constantly keep in mind where some output is coming from, and not only on which device it's displayed.

The first thing to do is clearly understand what's the output that the use case is supposed to provide: in our case the output comprises two elements:
- the exit status of the program execution
- the error message that might possibly have happened

It's important to underline that we want errors to be part of the output, because they're still significant for the application. Including errors in the response means that they can be handled by a presenter, and the views attached to it. Alternatively, we could have chosen to send the errors to some kind of side output, for example events, but in that case the decision of whether to display these errors or not would have been taken by the adapter, and not by the application. By sending errors with the response, we are clearly stating that we want errors to be displayed, as an application rule.

Thus, our application will need to handle two output boundaries: `ExitStatusPresenter`, receiving an `ExitStatusResponse`, and `ErrorPresenter`, receiving an `ErrorResponse`. For both of them, concrete instances will need to be injected into the interactor. From the adapter point of view, we should decide which output models we want to support. For instance, we can think of a "console output", which is meant to be used when the application should be used as a standard console application, properly using the exit status, STDOUT and STDERR; additionally, we can think of a "textual output", which is meant to be used when all data produced by the application should be available as human-friendly textual information. These output models define two distinct sets of presenters: for the console output, we'll have a `ConsoleExitStatusPresenter` and a `ConsoleErrorPresenter`, while for the textual output we'll have a `TextualExitStatusPresenter` and a `TextualConsoleErrorPresenter`:
- the `ConsoleExitStatusPresenter` converts the `ExitStatus` object of the response into an integer included between `0` and `255` (using a default value if needed), because it needs to be sent to a console application exit status, abiding by POSIX standard, and produces a `ConsoleExitStatusViewModel`;
- the `TextualExitStatusPresenter` converts the `ExitStatus` object of the response into a string, avoiding changing its semantic at all, and produces a `TextualExitStatusViewModel`;
- both the `ConsoleErrorPresenter` and the `TextualErrorPresenter` will just convert the `Error` object of the response into a string, producing a `ConsoleErrorViewModel` or a `TextualErrorViewModel`;

Each output model can then be rendered into different widgets (views): these will be organized into output configurations, that can be selected by the user, for example through command-line arguments.

The *integrated configuration* is used to run programs on the virtual machine, as if they were normal executables; this means that the program's exit status is returned as the application's own exit status, and the error message is printed to STDERR: 
- the `ExitStatusWidget` is used to return a number as the exit status of the console application;
- the `StderrWidget` is used to print a message to the STDERR of the console;
- the `IntegratedExitStatusView` is used to render the `ConsoleExitStatusViewModel` to the `ExitStatusWidget`;
- the `IntegratedErrorView` is used to render the `ConsoleErrorViewModel` to the `StderrWidget`;

The *clean configuration* is used to run programs on the virtual machine, but hiding the error message, so to keep the console clean; the exit status is still returned as the application's own exit status, but now the error message is written to a file; a possible use case of this is when the actual program is writing stuff to STDERR, and we don't want it to mix with errors written by the application (instead of the program):
- the `ExitStatusWidget` is used to return a number as the exit status of the console application;
- the `OutputFileWidget` is used to write messages to an output file, instead of to STDOUT or STDERR;
- the `CleanExitStatusView` is used to render the `ConsoleExitStatusViewModel` to the `ExitStatusWidget` (here we could share a single `ConsoleExitStatusView` with the previous case instead perhaps);
- the `CleanErrorView` is used to render the `ConsoleErrorViewModel` to the `OutputFileWidget`;

The *verbose configuration* is used to gather all information on a centralized place, immediately visible; both the exit status and the error message are printed to STDOUT:
- the `StdoutWidget` is used to print messages to the STDOUT of the console;
- the `VerboseExitStatusView` is used to render the `TextualExitStatusViewModel` to the `StdoutWidget`;
- the `VerboseErrorView` is used to render the `TextualErrorViewModel` to the `StdoutWidget`;

The *archived configuration* is used to gather all information on a centralized place, but without clogging the console (notice that STDOUT and STDERR may still contain what the actual program is writing to them); both exit status and error message are printed to a file:
- the `OutputFileWidget` is used to write messages to an output file, instead of to STDOUT or STDERR;
- the `ArchivedExitStatusView` is used to render the `TextualExitStatusViewModel` to the `OutputFileWidget`;
- the `ArchivedErrorView` is used to render the `TextualErrorViewModel` to the `OutputFileWidget`;

Here's what some pseudo-code would look like:
```
ConsoleExitStatusPresenter
    ConsoleExitStatusPresenter(ConsoleExitStatusView view)
    present(ExitStatusResponse response)
        exitStatus = normalizeExitStatus(response.getExitStatus())
        viewModel = new ConsoleExitStatusViewModel(exitStatus)
        view.render(viewModel)

ConsoleErrorPresenter
    ConsoleErrorPresenter(ConsoleErrorView view)
    present(ErrorResponse response)
        error = response.getError().getMessage()
        viewModel = new ConsoleErrorViewModel(error)
        view.render(viewModel)

IntegratedExitStatusView: ConsoleExitStatusView
    IntegratedExitStatusView(ExitStatusWidget widget)
        render(ConsoleExitStatusViewModel viewModel)
            widget.setExitStatus(viewModel.getExitStatus())

IntegratedErrorView: ConsoleErrorView
    IntegratedErrorView(StderrWidget widget)
        render(ConsoleErrorViewModel viewModel)
            widget.setError(viewModel.getError())

ConsoleUi
    ConsoleUi(Container container)
        this.console = container.make(Console)
        this.exitStatus = new ExitStatusWidget()
        this.stderr = new StderrWidget()
        container.bind(ExitStatusWidget, exitStatus)
        container.bind(StderrWidget, stderr)
    getExitStatus(): ExitStatusWidget
        return exitStatus
    getStderr(): StderrWidget
        return stderr
    render()
        console.writeError(stderr.getError())
        console.exit(exitStatus.getExitStatus())

ConsoleUi ui = new ConsoleUi(container);
// send input, render views...
ui.render()
```

Here we encapsulate all UI related code into a single class, which binds specific instances of widgets to their classes, so when views are built by the container, they get the right widgets. This specific case is particularly interesting because we have to deal with the problem that when we call `console.exit()`, the application is terminated, so any other UI code that might need to run after that won't be able to. To avoid this, instead of directly call console methods inside views, we let the views populate the widgets, and then render the UI as the last thing. Had we allowed views to directly call the console, the order with which the various presenters were called inside the interactor would have been important for user interface concerns, because if the interactor called the exit status presenter before the error one (or a generic message one, since if there are errors, no exit status is produced in this specific case), then the application would have been terminated before the interactor even finished its execution, and this is of course unacceptable. Having had a graphical interactive UI, instead, we could've displayed the exit status in a widget as soon as it was produced, because it wouldn't have caused the application to terminate. 


## Status

Proposed


## Consequences

Everything regarding input and output for adapters is following a generic and reusable standard.

Different output representations and output devices are supported.

Input is actually completely decoupled from output.
