# 10. Necessary rework for V2
Date: 2022-03-06

## Status
Planning

## Context
The planned purpose to input freeform workouts is achieved but is insufficient for comparable workout results.
- it's on the user to decide whether or not a workout was done faster (lower "score" is better) or with more reps (higher score is better)
- workouts with only strength exercises (classic bodybuilder or gym workouts) are hard to compare because they contain different exercises, with different weights or reps

I do not have an idea for comparable gym workouts because it is - at least for now - far out of scope for this app and not the main purpose of "my" fitness schedule. I also often mix different exercises or substitute some of them (pain, personal preference, variety, etc.) so a comparison of those would be real hard.

But for the other workouts, where the goal is clear (to beat a time or a rep count) there is an easy solution:

### Workout Types
Currently there is no kind of type. Everything is freeform, free input, no comparison. But the purpose of single workouts are clear:
- for time: lower score is better. ie. 5k row, 5k run, 200 burpees.
- max score: higher score is better. ie max reps, max weight, max distance in a given time

Unfortunately max score only works for a clear pre defined workout like "5 rep max Deadlifts". It does not work or at least not that easyily for workouts like "chest/arms" or "push/pull" with a variety of exercises, reps and weights.

## Decision
TBA

## Consequences
TBA

