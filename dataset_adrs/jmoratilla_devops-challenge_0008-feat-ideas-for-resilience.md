# 8. feat_ideas_for_resilience

Date: 2020-02-25

## Status

Draft

## Context

Here I'm adding some ideas to add as a cul-de-sac about resilience and 
 previous experiences in order to keep a production environment under
 control.

### Mechanisms for resilience and fault tolerance

#### What can go wrong?

To identify possible points of failure, I will go upstreams from production to development.

#### Production

Attending to Murphy's Law: Anything that can possibly go wrong, does, I should meter anything.  So first point of failure here is monitoring.

##### Monitoring

If is not monitorized, it is not in production

Anything that goes in production is a result of an effort to earn money, so we should be consciuous of the benefits of the feature as soon as it is deployed.

For me, any new feature request should have a way to meter the success or failure rate of the solution, and that check must be defined before the feature runs in production, just to show it is not in production yet.

To handle this, I would add a requirement in the specs for any feature request that should establish what is a success and what is a failure for the product owner that requested it.

A product owner dashboard should exist so any product owner should see a way to measure the success rates of her decisions.

This monitoring comes from Business, but as technicians we need to measure how the platform is performing, and the capacity of the current resources in order to answer the following question:

Will the next feature get into the current platform?

You can use [RED method](https://thenewstack.io/monitoring-microservices-red-method/) to monitoring features.

##### Name Resolution

What if you have a website nobody can reach because your nameservers are 
 down?

You should have a primary and secondary nameservers in different 
 providers.

##### Name System Attacks

What if your nameservers have been poisoned to deliver different 
 addresses?

Your nameservers must verify and check their data consistency.

##### Name Changes Response Time

Your servers must be quite fast to respond queries, and fast enough to 
 propagate changes when endpoints are affected.

##### Network and Security

Your services should have enough bandwidth to avoid queueing requests and deliver quick responses.  Your network is vulnerable to several attacks, from DDoS to specific website malformed urls or known product vulnerabilities.

Monitor your network capacity and get a provider that can handle all your needs.  In cloud environments is easy if you have the money.

Monitor your traffic using Firewalls or Web Application Firewalls, that inspect the requests looking for known vulnerabilities.

If you are using web services, perform the following recomendations:

- Use HTTP2
- Use CDN solutions
- Use WAF solutions that can automatically ban attackers IP addresses


##### SSL certificates

Your web applications and sites won't work if your SSL certificates are not valid.

Valid certificates means they are in working conditions and they are recognized by the users as trusted certificates.

Monitor your SSL certificates expiration dates and set a prodedure to renew them and publish them automatically.

Use global solutions like [Cloudflare](https://cloudflare.com) that provide solutions for DNS, CDN and Certificate management.  But keep an eye on other providers to have a failover.

##### Know your servers, avoid stupid downtimes

Some servers can create unexpected conditions when you don't know their limits.  For example: nginx is known for be a good load balancer and reverse proxy, but it's also true that it caches the IP addresses of the upstream servers.  If the IP address of an upstream server changes (because reprovisioning a node), then nginx can behaves unexpectedly and it can return error codes.

Other issues can be related to timeouts.  If a web request last more than 40 seconds, nginx automatically rejects the request with a 504 (Gateway Timeout) error code.

To solve this, use your preproduction / staging environments to reproduce possible scenarios, and get knowledge about the limits of the servers, services and platforms used.

##### Invest in your logs

Get all the possible info from the servers and any service involved in the production environment.

Process all your logs in order to aggregate data and set a baseline to detect anomalies.

Use solutions like Splunk, Logentries, Devo, Airbrake

#### Preproduction

##### Schedule backups from production to preproduction / staging

TBD

##### Pseudoanonymize backups from production to upstream environments

TBD

##### Perform load tests

TBD

##### Perform releases in staging and take times

TBD

#### QA

##### Match specs with tests

TBD

#### Development

TBD

## Decision

Here are lots of ideas to explore for next discussions.

## Consequences

To discuss.