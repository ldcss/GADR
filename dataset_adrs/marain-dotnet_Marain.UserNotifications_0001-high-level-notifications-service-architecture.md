# High level notifications service architecture

## Status

Proposed

## Context

Many systems have a requirement to send notifications to users. This is a general enough requirement that it can be addressed by a standalone service. Such a service should be able to support:
- Creation and retrieval of notifications for users
- Categorisation of notifications
- Multiple delivery channels (e.g. email, push notification, SMS, etc)
- Delivery and read tracking, where supported by the specific delivery channels
- Configuration of delivery per user, notification category and channel

## Decision

```
                         +-------------+
  Query notifications    |             |
<------------------------+ Query API   +-------------+
                         |             |             |
                         |             |        +----v----------+
                         +-------------+        |               |
                                                | Notifications |
                                                | Store         |
                         +-------------+        |               |
                         |             |        +-----^---------+
 Create notifications    | Management  |              |
+------------------------> API         +--------------+
                         |             |
                         +-+--------^--+
                           |        |
                           |        | Status
                           |        | updates
                           |        |
             Notifications |        |
                           |        |
                           v        |
                  +--------+--------+-------+
                  |                         |
                  | Delivery channels       |
                  | (e.g. SendGrid, Twilio, |
                  | etc)                    |
                  |                         |
                  +-------------------------+
```

### Services

The core service will be implemented via two APIs; a "management" API which will be used to create notifications and to update their delivery/read statuses (and any other management operations that might be required in future), and a "query" API which can be used by applications presenting those notifications to a user. In that sense, the "query" API is a special case of a delivery channel.

### Storage

We expect that Azure Table storage will be used to store raw notifications, with the user's ID being used as the partition key and a notification sequence number as the row key.

### Delivery channels

To make the solution as extensible as possible, the core API will not handle notification delivery. It is envisaged that this will be handled by other "delivery channels" and integrated via WebHooks. An expected implementation approach for many delivery channels would be Power Automate/LogicApps, which have connectors available for many extenal messaging services already (e.g. SendGrid, Twilio).

We envisage that integration between the management and delivery APIs will be as follows:
- Available delivery channels will be "registered" with the management API. Registration would likely include an Id, a display name and a Uri to which new notifications will be POSTed using a defined data structure.
- In order for a specific category of notification to be sent to a delivery channel, additional configuration will be required. This will be channel specific, for example a template to convert notification data into an email.
- As well as this, it will be necessary to configure per user and notification category which delivery channels to use. In order to make this easier, we envisage a hierarchical categorisation system allowing configuration to be defined for any level in the category hierarchy.

As mentioned above, the query API is a special case of a delivery channel; it will not require special configuration and all notifications will be available via the API.

Where supported, we will allow delivery channels to update a notification with its delivery and read status via callback URLs.

### Notification categorisation

Categorisation of notifications has two related purposes:
- Allow per-user configuration of different delivery channels for each category of notifications.
- Control the display formatting of each category of notification

We will support a hierarchy of categories, expressed via dot-notation. For example, a set of notification categories could be as follows:
- `marain.workflows.instance-created`
- `marain.workflows.instance-state-change`
- `marain.workflows.instance-completed`
- `marain.workflows.instance-faulted`
- `marain.tenancy.tenant-created`
- `marain.operations.operation-started`
- `marain.operations.operation-failed`

We then expect to be able to provide configuration at different levels of hierarchy. For example, a user could configure email notifications for the category `marain.workflows`, ensuring that they receive email notifcations of the four subcategories, but they could also configure a more specific SMS notification for the `marain.workflows.instance-faulted` category.