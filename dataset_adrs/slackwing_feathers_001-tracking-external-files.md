## Tracking External Files <sub>ADR-001</sub>

### Status

_<s>Accepted</s>_

_Superseded by [ADR-003](https://github.com/slackwing/feathers/blob/master/adr/003-tracking-external-files-revisited.md)_

### Context

How can I track files like .bashrc and program configs in a git repo?

- They're often read and modified by external programs.
- Therefore they can't change locations.

### Approaches

#### 1. Why track them at all?

If the sole purpose is backup, then a low-cost approach is to sync via Dropbox or Drive. Although, it does add another ecosystem to track. In my case, I'd like to share some files publicly and in the same place as my projects, so this doesn't work.

#### 2. Softlink repo to system file

    ln -s ~/.bashrc ~/repo/some/path/.bashrc
    
This won't commit the file's contents, only the literal bytes of the softlink.

#### 3. Hardlink repo to system file

    ln ~/.bashrc ~/repo/some/path/.bashrc
    
This works, mostly. Opening and editing the file from either location affects the target, as we want. Therefore changes by us or programs show up as unstaged changes in `git status`.

But there's a problem. If a remote change is made, like through Github's web interface or from another computer, the `git pull` will overwrite the symlink with a new copy of the file. As a result, external changes to ~/.bashrc stop showing up as unstaged changes, leaving us without a hint that anything's changed. The files may then diverge, meaning we can't just blindly recreate the hardlink (`ln -f`)—we'd always have to diff and manually merge first.

#### 4. Softlink system to repo file

    ln -s ~/repo/some/path/.bashrc ~/.bashrc
    
This averts the `git pull` issue, since a softlink will point to the repo's file by path.

But, much like the `git pull` issue, only translated to the other side, ~/.bashrc can be overwritten as well, destroying the symlink. For example, programs—maybe even some editors—commonly do an "atomic write" by writing contents to a temporary file then copying that file over. Then here too, the files may diverge.

In fact, #3 is weak to this issue as well—in other words, hardlinks break when overwritten on either side. (It was just easier to explain this here.)

#### 5. Hardlink system to repo file

    ln ~/repo/some/path/.bashrc ~/.bashrc

But now we know that hardlinks are brittle. This is the worst of both #3 and #4.

### Decision

Clearly #4—softlinking the system to the repo file—has the least issues.

We'll go with that, supplemented with a git hook that detects broken links:

 1. If broken link and diff, warn and confirm to continue operation.
 1. If broken link and no diff, warn and confirm to force softlink.

This way, we're nagged until the two files match, and only then given the option to force a symlink.

To generalize this for many files, we'll work from an array in the hook. (Oddly, the array should contain the file containing it, since hooks are not pushed.)

### Accepted Tradeoffs

None known.

### Retrospective

See [ADR-003](https://github.com/slackwing/feathers/blob/master/adr/003-tracking-external-files-revisited.md).
