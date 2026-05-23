# 2. Use systemd as the cgroup driver for docker

Date: 2019-05-31

Status
------

Accepted

Context
-------

When I first installed kubernetes with nothing but default settings, I
got this warning:

```
[WARNING IsDockerSystemdCheck]: detected "cgroupfs" as the Docker cgroup driver. The recommended driver is "systemd". Please follow the guide at https://kubernetes.io/docs/setup/cri/
```

Turns out, they don't recommend using docker's default cgroup driver in
tandem with systemd long-term.

Decision
--------

So I'm doing as the kubernetes website recommends, because they seem
trustworthy.

Consequences
------------

That warning message no longer appears.
