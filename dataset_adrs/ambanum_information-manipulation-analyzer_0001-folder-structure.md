# Decision Record - Folder structure

We have decided for this project to use NextJs as it is a growing ecosystem and facilitates a lot of processing such as

- api generation
- HTML pre-rendering
- page creation

This is a really accesible and clean framework for anybody who know a bit of React and javascript

## Folder structure

We have decided to differ a bit from the common folder structure proposed by Vercel

- `src` folder
- organisation of code through independent `modules`
- re-export of pages logic inside previous modules

The goal with this architecture is to be able to easily be able to copy one module from a project to another as we may have in the future many other projects that could rely on this.

At the moment though, we may have only one module that will be called `Common` and that will contain most of our logic.
