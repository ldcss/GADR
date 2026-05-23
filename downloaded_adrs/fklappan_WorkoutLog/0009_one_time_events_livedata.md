# 9. There is a need for "one time" events

Date: 2021-09-23

## Status

Accepted

## Context

LiveData events will be pushed again after certain LifeCycle events. Ie. when rotating the device or
after returning to a fragment from another navigation path. Errors or special events like automatic
navigation should only be executed once. 

## Decision

A new event will be introduced for the ViewModels which has the clear purpose of only occur once.

## Consequences

The existing ViewModel classes with the need for one time events have to be edited. A second 
LiveData variable needs to be exposed to the view which also has a state "none" which will be 
skipped by the views.