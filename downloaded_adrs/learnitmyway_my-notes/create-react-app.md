# Fork and extend Create React App

## April 13 2019

### Context

It would be nice to have `babel-plugin-jsx-remove-data-test-id` but I don't know of a way to add it to Create React App.
it would be possible to fork CRA and adjust the config there. However, that seems to involved the following:

1. Fork CRA
2. Add plugin to babel-preset-react-app
3. Publish developerdavo-babel-preset-react-app
4. Point to developerdavo-babel-preset-react-app in react-scripts
5. Publish developerdavo-react-scripts

Not to mention, local development requires package linking and updating dependencies in developerdavo-babel-preset-react-app would require publishing two packages.

### Decision

It doesn't seem to be worth the maintenance cost
