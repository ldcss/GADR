# Title
ADR-001: SSHFS Assistant.

# Summary
Added configurable way to use sshfs.

# Context
sshfs is a really handy tool, but I felt that if I could mount AND unmount with it while still using the local user's ssh config file, it would make it super easy and fast to manage.

# Decision
I created a global npm command called `sshfsa` that will mount an SFTP session to an existing file path.

# Consequences
I will be able to mount and unmount without needing to type out the local mount path.

# Status
Accepted