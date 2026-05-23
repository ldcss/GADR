# Rich text editing with TOAST UI Editor

**User Story:** [EASI-3121](https://jiraent.cms.gov/browse/EASI-3121)

EASi users would like rich text editing in some areas of the app.

The required editor features are
- Bold and italic text
- Ordered and unordered lists
- URL links
- Pasting in clipboard contents from another editor such as Word

## Considered Alternatives

* [TinyMCE](https://github.com/tinymce/tinymce)
* [Quill](https://github.com/quilljs/quill)
* [TOAST UI Editor](https://github.com/nhn/tui.editor/tree/master)
* [Lexical](https://github.com/facebook/lexical)

## Decision Outcome

* Chosen Alternative: TOAST

Toast is quick to integrate into our project and meets all feature requirements out-of-the-box. It's easy to set up an editor using the basic options.

Though it's easy to start with, modification options can be limited and plugins may need to be written to extend or alter functionality. For example, the built-in Link tool doesn't have a way to edit links after they're added. Extending that functionality would be done as a hack or creating a user plugin.

The editor's baseline appearance is set through its own theme which needs style overrides to match ours.

Keep an eye out on Lexical for when there's more time and resources.

## Pros and Cons of the Alternatives

### TOAST UI Editor
* `+` Quick setup; React wrapper readily available
* `+` All feature requirements supported
* `-` Bigger bundle
* `-` Interfaces the Editor object via legacy ref
* `-` Extending a behavior might need to be done as a plugin

### TinyMCE

* `+` Well-known and mature library
* `-` Could not integrate; conflicting module reconciliation
* `-` Huge bundle

### Quill

* `+` Minimal
* `+` Smaller bundle
* `-` Needs additional plugin for Markdown
* `-` Current release is old
* `-` Current project activity is questionable

### Lexical

* `+` Cutting-edge
* `+` Modular
* `+` Smallest bundle
* `-` It's a framework to build rich text editors from scratch
* `-` Every bit of the editor is a plugin to set up
