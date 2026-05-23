# Use AWS logging tools

We would like a set of tooling to aid in debugging and monitoring
the EASi application. We would like this solution to be easy to
send logs into, easy to integrate infrastructure tooling into,
and manageable alongside our infrastructure configuration if possible.

## Considered Alternatives

* *AWS built-in tooling*
* *ELK stack*
* *Honeycomb*
* *NewRelic*

## Decision Outcome

Chosen Alternative: *AWS built-in tooling*

AWS provides common tooling for logging of infrastructure services.
Cloudwatch and S3 are common endpoints to send both metrics and logs into.
We can use Cloudwatch to create dashboards and we can use Athena
we would be able to create dashboards and explore the data.
Additionally we can manage the configuration of these tools in Terraform
alongside the configuration for the infrastructure we define in Terraform.

## Pros and Cons of the Alternatives

### *AWS built-in tooling*

* `+` Configuration is built into the infrastructure platform
* `+` Truss has internal experience with these tools
* `+` Can be configured in Terraform
* `+` Can easily be adapted for application logs
* `-` Minor latency in logs being indexed
* `-` Cloudwatch configuration can be a bit limited

### *ELK stack*

* `+` Provided for us by AWS West
* `+` Required by AWS West
* `-` Kibana has a steep learning curve
* `-` Latency in the logs being indexed
* `-` It's behind a VPN and less accessible

### *Honeycomb*

* `+` CMS has some kind of contract with Honeycomb
* `+` Cool log exploration tool
* `+` Easy to send what you find to each other
* `-` AWS West has not implemented this tooling
* `-` Needs additional tooling
* `-` Steep learning curve

### *NewRelic*

* `+` CMS does have a NewRelic contract
* `+` Can also do metrics
* `-` Not entirely sure CMS uses the logging feature set
* `-` Logging isn't NewRelic's main product
* `-` Requires installing their agent
