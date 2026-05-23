# Templating engine

## Status

Proposed

## Context

Applications that consume `Marain.UserNotifications` need control over the appearance of the notifications that end users receive. At a bare minimum, notifications must convey all relevant information, but organizations also typically want communications to look 'on brand'. For example, they will want full control over the layout and design of email notifications. Furthermore, each communication channel is likely to have different requirements: SMS notifications need brevity and have very little design flexibility compared to email, for example.

This ADR describes how `Marain.UserNotifications` provides a templating mechanism to give consuming applications control over the presentation of notifications. Templating is a widely-used solution to this problem. It enables a separation of concerns: application code can focus on deciding when to send a notification, and collecting the relevant information; the concern of how to present that information is handled by templates.

A template defines the design and layout for a notification. Typically, most notifications of a particular type will share layout and even most of the content, but there will be places where values must be inserted to convey the particulars to the end user. For example, in a birthday email notification, most of the design and formatting of the email/subject will be fixed, but certain custom data (eg. the recipient's name) will be different in each notification. So an application defines templates with placeholders for this variable data, and the templating engine plugs the real data into place each time a message is to be sent.

## Decision

Code in a consuming application that raises a notification will build a property bag—a key/value collection containing all of the information that can vary across instances of a particular notification type. For example, this might include the display name of the message recipient, and the name of a customer. The application sends this, along with the notification type, to the `Marain.UserNotifications` Management API as a request to send a notification.

To enable `Marain.UserNotifications` to transform this property bag into an actual message (email/SMS/etc.), consuming applications define a set of templates for each distinct notification type they produce. This set must include one template for each communication channel (SMS, email, web push notifications etc.) through which notifications of that type will be sent. E.g., if an application defines 10 messages types, and if each of these could be sent either by SMS or email, the application will need to supply 20 templates. Whenever the application sends a notification, `Marain.UserNotifications` will apply the relevant template to produce a communication object of the appropriate type (Web push, Sms, Email etc.), which it will then send via the desired delivery channel (SendGrid, Twillio, Airship, etc.).

For example, if a notification is going to be sent as a web push message, the delivery channel requires an object that includes three things: a title, the message body, and an action URL. A web push notification template describes how to form all three of these from the property bag for a particular notification type.

### Creation and storage of templates

Templates are stored in tenanted blob storage, using the notification type and communication type as a filename. For example, the template describing how a notification of type `marain.lead.created.v1` would be presented as a web push message would live in a blob named:
`marain.lead.created.v1:WebPush`.

The blob would look something like this:

```json
{
  "body": "You have been assigned a new lead by {{assignedByUserName}}",
  "title": "New Lead",
  "contentType": "application/vnd.marain.usernotifications.notificationtemplate.webpushtemplate.v1",
  "notificationType": "marain.lead.created.v1",
  "actionUrl": "{{actionUrl}}"
}
```

Since different communication channels require different sets of information, the exact template structure will depend on the channel. For example, an email template would, like a web push template, have a `body` and a `title`, but would not have an `actionUrl`.

There are no default templates. Each organization must define a complete set of templates covering each communication channel for each notification type that it wishes to raise. It is an error for an application to attempt to send a notification if it has not defined a template for the notification type/channel combination. (If configuration dictates that the message will be delivered through multiple channels, then templates for every channel must be supplied for that notification type.) If certain channels will not be used for particular notification types, the application does not need to supply a template for those notification type/channel combinations.

### Rendering templates

When applications send a notification request to the Management API, they specify the notification type, and provide a property bag. The `Marain.UserNotifications` service is responsible for determining which channels are to be used, and then for each channel, it will locate the correct template (WebPush, Email), and apply the template engine for each of the fields that the channel requires.

`Marain.UserNotifications` uses the [`Corvus.DotLiquidAsync`](https://github.com/corvus-dotnet/Corvus.DotLiquidAsync) templating engine, supplying properties from the notification property bag. It invokes the engine for each required field. For example, with the Web Push template shown above, the template engine will be run three times for that template (with the same property bag each time) on the `body`, `title`, and `actionUrl` fields.

## Consequences

Applications that consume `Marain.UserNotifications` can tailor the presentation of notifications. They have complete control, because they define separate templates for each distinct combination of notification type and communication type.

Since templates are stored in tenanted blob storage, templates are always application-specific.

Although the absence of fallback default templates gives organizations complete control over how their messages are presented, it does also increase the amount of work required to be able to send a message at all.
The design and layout of communications can be changed without needing to deploy code updates, because the code that requests sending of notifications does not make decisions about presentation. Presentation is determined by templates that live in blob storage.

Applications must arrange for all relevant templates to be created in blob storage as part of their deployment process. If new notification types are added, additional templates will need to be created. If applications support end-user customization of templates, they will need take care to ensure that the mechanisms that ensure the initial deployment of templates do not overwrite user customizations.

We do not want to force applications to provide templates for every _conceivable_ combination of notification type and channel—for example, if an application will never attempt to send a particular notification type by SMS, there is no need to supply an SMS template for that notification type. Consequently, there is no straightforward way to verify that all necessary templates are present: `Marain.UserNotifications` has no way of knowing in advance which particular channels are used with which particular notification types. An upshot of this is that errors relating to missing templates will necessarily be raised at the point at which the application tries to send the message. (I.e., `Marain.UserNotifications` cannot offer to do a post-deployment check to verify that all required templates are present.)

This design does not provide a way to offer, say, Razor as an alternative templating engine. Templates do not specify the templating engine to be used, so there is an implicit assumption that templates will always use the dotliquid syntax.

Applications might define multiple message types that are all to be presented in the same way. (They might do this to enable end users to control which message types are delivered via SMS vs email, for example.) There is no mechanism for declaring that multiple message types are to use the same templates, so applications that work this way will need to provide multiple copies of the template sets, one for each message type.