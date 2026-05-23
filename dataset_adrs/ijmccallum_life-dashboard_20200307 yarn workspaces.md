# Switching to Yarn

Yarn solved some build issues between expo and lerna. The build-expo project imported app-root which failed to compile (webpack missing a loader). Even when app-root was just importing the react-native View and Text components only. The compiling issue went away when moving the app-root file into the build-expo package. So it's clearly something to do with lerna's symlinking and expo's build system.

Looking around the web there's one example project showing expo working with lerna - the biggest difference seemed to be that project's use of yarn workspaces. After looking into the subject a bit it turns out that if you set up a project to use yarn workspaces, lerna delegates all monorepo package management to yarn.

Monorepo package management:

Lerna: Symlinks local dependencies.
Yarn workspaces: hoists all dependencies into a single root.

https://doppelmutzi.github.io/monorepo-lerna-yarn-workspaces/