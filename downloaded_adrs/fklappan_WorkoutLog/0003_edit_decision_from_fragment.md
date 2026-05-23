# 3. Fragment (View) decides what should happen if the user clicks Edit through the options menu

Date: 2019-08-18

## Status

Accepted

## Context

The ViewModel is responsible for the data, so i tried an attempt to notify the ViewModel from within the view that the
user clicked the "edit" menu item. The ViewModel exposed a LiveData object which was observed by the view to trigger the
navigation to a edit fragment.
After editing the workout and clicked saved, the edit fragment was opened again instantly. This was caused by the
ViewModel which triggered the edit event again.

## Decision

The view (DetailviewWorkoutFragment) no longer notifies the ViewModel about the edit action but directly calls the
navigation component to open the EditWorkoutFragment, and therefore decides what should be done after the edit action
was clicked (normally the view should not make this kind of decision).

## Consequences

In this special case the solution is ok, because we have direct access to the arguments which contains the necessary
workout id (to load the workout). In other cases we might have to store data directly in the view which is bad practice
because we use ViewModel for that...