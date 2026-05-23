# 2. Use Java as Language

Date: 2019-10-19

## Status

Accepted

## Context

We need to use a language to implement the software. Scratch itself is written in Javascript and runs in the browser.  
So Javascript would be a natural choice.  
But the authors are more proficient in Java than Javascript. Also to compile the C code we always need a way to execute  
native processes. Thus we always can execute Java programs.  
This means that we only need a small bridge from Javascript to Java and can write most code in Java.   

## Decision

We will use Java to implement the software.

## Consequences

It becomes harder to run the Java code in a browser, but it would be possible by using e.g. GWT, TeaVM or another transcompiler.  
We will have to ship a Java runtime.   
