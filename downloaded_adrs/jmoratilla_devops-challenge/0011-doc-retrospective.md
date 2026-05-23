# 11. doc-retrospective

Date: 2020-03-03

## Status

Accepted

## Context

This is a retrospective about how I have performed while working on this test.  It includes my personal feelings in order to keep a record of my work and the things I should improve for next tries.

I have launched several questions to myself in order to wonder and make an instrospective work to create a retrospective.  Not only in the technical aspect of the target, but emotional and comprehensive aspects too.

## Decision

This is the dump of my retrospective:

### How did I approach it from the beginning? 

I wanted to do a very big test, with microservices made in several languages. I also wanted to be able to deploy them on various platforms. And as for the logs, I wanted to use the possibilities of heroku. 

### How I organized the work

The first time, in November, I did a project on Youtrack, of jetbrains, but when I went to redo it, I didn't find myself motivated to use that platform and I was more messy. 

Then I resorted to the pomodoro technique, but at the beginning  I worked without order and I didn't follow them much either. Step by step I have started using them again, but I still find it difficult to limit myself to the task I have indicated. Although I am making progress.

### How has the performance been?

Very poor at first. As I got frustrated, I dropped out. It wasn't until Wednesday that I got serious. At the weekend I could barely do anything, but in fact, the most I could do was on Monday and Tuesday.

I also have to say that the kids took a lot of time (Ruben's birthday, games, park...) in the afternoons until I got serious. 

### How did I feel?

Interestingly, the more pressure I felt, the better I felt, since I was doing something in a focused way and I was concentrated on that task, rejecting everything else.  I also had a lot of anxiety.

### What steps did I take to take the test?

Leaving my entire line of thought in ADR format made it easier for me to document, and I associated an ADR with a feature, so I think it turned out pretty well.

Initially I wanted to mount a cluster of kubernetes in my machines.  But I started to find many problems when defining the network model (it has about 10 models)

My initial goal was to mount it with anxiousness on my machines, but I wasn't concentrating.

Later, when I wanted to do something, I didn't get out and in the end I pulled kops and deployment in AWS.  I wanted to convert it to terraform, but it didn't work, so I researched how to mount it using kops templates.  That worked and gave me oxygen.

I had a lot of trouble understanding how to assemble an ELB balancer for the services deployed in kubernes.  I found that the LoadBalancer service type worked for these cases, but when a baremetal cluster is used, I don't know what to do.

I got stuck with the nginx ingress and other kubernet addons.  They are not difficult, but I don't know how to manage these addons and which tool is the right one.

It was clear to me that I wanted to use the springboot microservices practice.  I also quickly saw that I would want to use a mono-repost for the deployment of all services to facilitate build and deployment based on the modifications.

CircleCI was also an option from the beginning, as jenkins has a lot of configuration that is not seen, and is misleading.

For deployment management, I was confident that I would learn quickly how Helm works, however by then, I was already out of time and exhausted.

### How did the test go in the end? 

I demonstrated that I  can easily mount a kubernetes on aws using kops templates, and that you can also continuously deploy a number of microservices using CircleCI.

However, I haven't shown anything about how to mount the horizontal scalability, although I've left it indicated in the documentation.

I haven't touched on the subject of testing either, although I have referenced it in the documentation, nor on monitoring.

The code is displayed, although I've only managed to make the eureka and the product work, because I found a problem that I didn't expect, the naming resolution doesn't work as I expected in kubernetes with eureka.

At this point, the practice doesn't work (sigh).  I'm learning how to make spring cloud work with kubernetes.

### What have I learned and how have I applied it?

- kops: I've learned how to use it better and some things like templates and importing or replacing are new and seem good for my purpose.
- kubernetes: I've learned how to assemble the base, but I still have a lot to learn:
  - assembling the addons
  - run the network
  - manage permissions
- springboot: I've learned about netflix architecture (with eureka, zuul, ribbon, feign), but I still have a lot to learn.
- asdf: a jewel.  A rbenv type download manager, but for many more development tools.
- ADRs: I think it's a good idea to have a repo-associated documentation like this one, but it lacks something.  Maybe I would like to develop more the life cycle of an ADR.

### What have I noticed? 

- kubernetes is a kraken, it has many pieces
- I have no idea why they say I'm SRE
- I have no idea about testing under conditions
- I have a hard time organizing a job I've never done
- On the internet there were repositories with a much simpler base than mine.  I would have saved a lot of time and effort.
- AWS is cheap if you know how to use it well.  A good recommendation is to mount the cluster with a node-type master (t3a.large is very cheap) and the rest with spot instances (t3a.medium at 0.025 are great).
- Last thing is about this kind of tests: it's not easy to do one of these test for the first time.  Next time I will be ready.


## Consequences

The first consequence is to feel ashamed of the bad things, but I should enforce myself focusing in the accomplished things and the progress I did.  I need to encourage myself to expose my thoughts and feelings in order to learn how to do the job better.


