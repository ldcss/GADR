# 1. Use of GitHub's Project feature for a KanBan

Date: 2019-04-09

## Status

Accepted 

## Context

A SCRUM-based agile devlopment workflow would benefit from a central KANBAN board to keep track of userstories that have been written, are in progress, and are complete. This will help identify the sprint backlog, and the current focus of the sprint. Labels could be used to indicate size/priority/difficuly or value to the project, to help calculate the sprint velocity and determine what can get done inside a single sprint.

## Decision

Using the GitHib Project page with a single project for the repo, and using Issues labelled as User Stories, with columns for "To Do", "In progress", and "Completed".  We can leverage some of the automatic rules in Git to help automate some of the completetion of tasks ties to Milestones for each sprint:

https://github.com/witseie-elen4010/2019-005-project/projects/1

## Consequences

Manually Use story cards used so far will become redundant. Need to tie physical cards into the digital version in the interim. Will not maintain the physical cards beyond Sprint 1.

 * simplifies workflow
 * Directly ties git issues and User Stories to individual developers
 * Easy to modify an existing User story - need to maintain discipline to avoid retroactively modifying tasks
 * Acceptance tests can be specified as sub-issues, or as checkboxes on an issue.
