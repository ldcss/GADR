# Which tech to use

The goal is to have the least number of technologies that will allow a project to run on native desktop, native mobile, and web. Ideally without hybrid apps (eg the whole webview thing). 

## Technologie notes

- **electron** Desktop build from JS (webview)
    - Will it run react native components?
- **react-native-web** Web build from react-native components
- **react-native** Native mobile build
- **lerna** managing monorepos & shared packages
    - lerna handling monorepos, maximising shared code.
    - different packages for each platform, common packages shared.
    - platform specific code in their own packages
    - business logic in plain js packages
- **nodegui** native desktop build from JS
    - JS to Native Desktop with Qt, internals are in c++
    - it's a WIP, very young. Many dragons! Hell of a learning opportunity though.
- **react-nodegui** native desktop build from react components
- **ionic**, creating hybrid apps in web views
    - works with plain JS, so we can use svelte or preact
    - has a prebuilt component lib
    - capacitor / cordova give the webview access to native mobile APIS
- **svelte-native** native mobile builds from svelte code
- **expo** 
    - builds web, iOS, android using React
    - uses react-native-web under the covers

|                  | Src          | Web | Native mobile | Native desktop | WebView mobile | WebView desktop |
|------------------|--------------|-----|---------------|----------------|----------------|-----------------|
| expo             | react-native | x   | x             |                |                |                 |
| react-nodegui    | react        |     |               | x              |                |                 |
|------------------|--------------|-----|---------------|----------------|----------------|-----------------|
| nodegui          | JS           |     |               | x              |                |                 |
| svelte-native    | svelte       |     | x             |                |                |                 |
|------------------|--------------|-----|---------------|----------------|----------------|-----------------|
| react-native-web | react-native | x   |               |                |                |                 |
| react-native     | react-native |     | x             |                |                |                 |
| ionic            | JS           |     |               |                | x              |                 |
| Electron         | JS           | x   |               |                |                | x               |

## Choices

### react-native
**lerna** & **expo** > **react-nodegui**

Lerna coordinates the multiple packages that divide the codebase. Within that, 2 seperate builds will generate builds as detailed in the bullets below. At build time set env variables to switch component wrappers: one wrapper for the react-nodegui Qt components and another wrapper for the react-native-web wrappers. 

- react-native > expo
    - Outputs html, css, js GUI for the web 
    - Outputs native mobile GUI
- react-native > expo > react-nodegui
    - Outputs native desktop GUI

### react-native / electron
**lerna** & **expo** > **electron**

expo has an electron adapter. https://dev.to/evanbacon/making-desktop-apps-with-electron-react-native-and-expo-5e36

### Svelte
**lerna** & **nodegui** & **svelte-native**

Again Lerna coordinates the packages. Within that, 2 seperate builds will generate builds as detailed in the bullets below. At build time set env variables to switch component wrappers: one wrapper for the nodegui Qt components and another wrapper for the svelte-native wrappers. 

- nativescript > nodegui ?????
    - Outputs Windows GUI build
    - Outputs Linux GUI build
    - Outputs Mac GUI build
- nativescript > svelte-native
    - Outputs Android GUI build (nativescript playground)
    - Outputs iOS GUI build

1. Set up a hello world for each type of build
    - [x] nodegui 
    - [x] svelte-native
    - [x] react-native-web
    - [x] expo
    - [x] react-nodegui
2. create a common "hello world" component to try and share between each of the two options.
    - [ ] react hello world
    - [ ] plain js hello world


## Decision

**expo & react-nodegui**

Expo uses react-native-web.