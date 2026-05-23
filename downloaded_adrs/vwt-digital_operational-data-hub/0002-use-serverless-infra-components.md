# 2. Use serverless infra components

Date: 2020-09-21

## Status

Accepted

## Context

Serverless computing offers a number of advantages over traditional cloud-based or server-centric infrastructure. For many developers, serverless architectures offer greater scalability, more flexibility, and quicker time to release, all at a reduced cost. With serverless architectures, developers do not need to worry about purchasing, provisioning, and managing backend servers.

## Decision

We will use serverless infrastructure components where possible. 

## Consequences

### Advantages
- **Cost** Only paying for the resources used, reducing cost
- **Elasticity** Serverless systems inherently scale down as well as up. As Google puts it: "from prototype to production to planet-scale."
- **No server management is necessary** Although 'serverless' computing does actually take place on servers, developers never have to deal with the servers. They are managed by the vendor.
- **Quick deployments and updates are possible** With function as a service, the units of code exposed to the outside world are simple event driven functions. This means that typically, the programmer does not have to worry about multithreading or directly handling requests in their code.

### Disadvantages
- **Performance** Infrequently-used serverless code may suffer from greater response latency than code that is continuously running on a dedicated server, virtual machine, or container.
- **Resource limits** Serverless computing is not suited to some computing workloads, such as high-performance computing, because of the resource limits imposed by cloud provider.
- **Monitoring and debugging** Diagnosing performance or excessive resource usage problems with serverless code may be more difficult than with traditional server code
- **Security**  Serverless is sometimes mistakenly considered as more secure than traditional architectures. While this is true to some extent because OS vulnerabilities are taken care of by the cloud provider, the total attack surface is significantly larger as there are many more components to the application compared to traditional architectures and each component is an entry point to the serverless application.
- **Vendor lock-in** Serverless computing is provided as a third-party service. Applications and software that run in the serverless environment are by default locked to a specific cloud vendor.
- **Serverless architectures are not built for long-running processes** This limits the kinds of applications that can cost-effectively run in a serverless architecture.
