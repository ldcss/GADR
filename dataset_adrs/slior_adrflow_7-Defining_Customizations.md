# 7 Defining Customizations

## Status

Proposed 2017-12-28
  
Accepted 2017-12-30

extends [3](3-Allow_More_Permissive_File_Names.md)

## Context
The need to customize different features in the tool raises the question of how to specify the customization.

On the one hand, there's a need to offer flexibility and expressive power. Assuming the average user is a competent developer, the most obvious way to achieve this  is to enable
some kind of a programming interface/definition.  
Given that the tool is written in JS, it's reasonable to assume a definition that will be done in JS as well.  
This might be too much power, resulting in potential performance/bugs/security issues.

On the other hand, there's the motivation to keep the tool simple enough, so configuration is minimal, but still expressive.

We can always start with a limited definition, but with an eye for further extensions. In any case, we'd like customizations to happen in a consistent and uniform manner.

This in a sense extends/generalizes the [decision to allow more permissive file names](3-Allow_More_Permissive_File_Names.md) by simply allowing any kind of customized file names, when working with the file name customization.

## Decision
In order to enable future extensions, we'll choose a customization method based on JS-based extensions.  
We'll define a file called `adr_custom.js` which will contain customization done to the tool. This file will need to reside in the ADR directory (the directory with the `.adr` file).

The customization code will be simple JS code, w/ predefined objects, depending on the API as defined by the tool. To be documented separately.  
For example, for defining the file name pattern, we'll probably require some JS object, with a predefined name, to be in that file.

The customization file (`adr_custom.js`) will be in a module form (using `module.export` etc.), so it can be easily consumed in the tool's code.

We assume that a user customizing the tool is competent enough to handle simple scripting.  
Limitations on customizations, resulting in easier customization, are left to specific features.

## Consequences

Features in the tool that require customization will need to read this file, and document the necessary expected objects in it.


    