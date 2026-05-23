# Retry Endpoint Design (Round 2!)

Date: 2021-05-19


## Motivation for the Endpoint:

The current requirement for the Batch/Bulk UI is to be able to retry jobs that have either "errored" out, or were terminated.
The UI allows you to retry either single jobs, or multiple jobs, and saves you from having to cancel and resubmit each job individually,
which is not currently implemented in the UI anyway. 

### Motivation for the `code spike` for retry endpoint and follow up design ADR
>As I mentioned, as the product owner, I find our ability to deliver functionality to be pretty awful. 
>We have invested so much effort in refactoring that its killed our timeline - we started in late July, and it is now almost May with no functioning >bulk uploader, which was just the first deliverable.
>If we are going to refactor, we need to be able to do it in a timely fashion, and have it not kill the schedule any more than it has.
>I want to see the estimate for a quick and dirty solution that implements a proposed retry endpoint, that can be deployed ASAP, and then once the API >contract has been established, and the functional MVP is done, we begin the cleanup of the backend code.
>Note that this is NOT business as usual, the usual way we do this is the nasty MVP gets deployed and then we don't go back until much later.
>Here, we get the API working so that it doesn't block dependencies, and we immediately start the refactoring. The refactor needs to be broken down into >smallish chunks of ~3 days estimated work, and each merge should maintain functionality and incrementally improve the codebase.
>Tasks that take more than a couple of days are more likely to be far off in their estimate and this is how we mitigate the risk of poor estimation.
>


### High Level Behavior of the `retry` endpoint
The current implementation of retry is to run jobs using the `retry_job` or `retry_jobs` endpoint. 
The endpoint takes a job or list of job ids and then attempts to resubmit them to the queue, using the exact same set of parameters and version of the app.

### Current Behavior

* Spec file is located at https://github.com/kbase/execution_engine2/blob/8baab8e3ac5212f4bbe59fd935980aa41b4ee06d/execution_engine2.spec#L201-L247
  
* A job id is provided. If there are sufficient permissions, the call will proceed, if not, it will error out, unless the `as_admin` flag is provided by an admin
* The retry will only continue if the status of the job to be retried is in [Status.terminated.value, Status.error.value]
* If the job id points to a job that has already been retried, it will attempt to retry that job's `retry_parent` instead.
* If the job id has never been retried, it becomes the `retry_parent` 
* EE2 looks up the method versions and parameters, and then submits the job to be retried, incrementing the `retry_count` of the job being retried, and the newly launched job gains a field called `retry_parent` that contains the job id of the job from the original request.
* The job is submitted and upon successful submission, the child job adds the field `retry_parent` and notifies the `parent_job_id` that a new `child_job` has been added by appending itself to the `parent_job.child_jobs[]` field
* There is no way to specify ResourceRequirements with a retry at the moment, even if the job was previously submitted by an administrator and had specfified ResourceRequirements. The retry will only use resource requirements from the catalog / ee2 config.


### Batch Behavior

* If a job has the attribute of `batch_job=True` the retry will fail, since there is no method to re-run. This is a bug, as it doesn't fail gracefully. Gracefully handling jobs with children means that it won't throw an error about not having a method to re-run, and instead will throw an error that says "Cannot retry batch job parents. Must retry individual jobs"
* If a job has the attribute of `batch_job=True`, but is actually a child job, the parent will be notified of this new retried job
* Multiple in-flight retries are allowed.
* Adds `child_job_id` to `parent_job_id.child_job_ids[]`

## Retry_job behavior
* Blocking and single submit to HTCondor. It should be fine as it returns relatively quickly
  
## Retry_jobs behavior
* Submitting multiple jobs for retry serially calls the same code path
used for running a single job and blocks until all jobs have been
submitted to the condor queue. This can cause issues if the
network drops, and makes the narrative not aware of the state of
the retry. Submitting 100 jobs currently takes 9 seconds, and that
is a lot of time for things to go wrong. 
* (Follow up: Hopefully the making the narrative aware of the state of the retry will be mitigated by the narrative backend. It just blocks on the call anyway, with the default service timeout, which I think is something wacky like half an hour. As long as the user doesn't kill the kernel at that time, all should be well. Of course, if it were me, and it looked frozen for more than a couple minutes, I'd probably restart. )
* Multiple in-flight retries are allowed.

### Desired Behavior

#### General
* Prevent multiple in-flight retries to prevent the user from wasting their own resources (and the queues resources)
* Non blocking job submission for submitting multiple jobs, possibly via using `run_job_batch` (requires refactor of run_job_batch)
* One single submission to HTCondor instead of multiple job submissions
* Ability to gracefully handle batch container jobs with children to throw proper error ([See Batch Behavior](#Batch-Behavior))
* Ability to handle database consistency during retry failure
* See if we can make some preflight (before the job starts) checks fail before job submission and handle them differently than those that appear during job submission 

#### Data inconsistency
* A new `retry_ids` field will show a list of jobs that have been retried using this parent id. Retry_count will be returned as a calculated field based off of retry_ids
* `retry_toggle` field will allow a seperate process to check and possibly correct for jobs that didn't finish the entire retry lifecycle:
1) Launch child jobs
2) Notify the batch parent of the child,
3) Notify the retry parent of the child,
4) Update the retry_toggle field

#### Won't do
* Add retry_number field

## New priority

For MVP
* Create a retry_jobs field, and expose list in api, and a T/F completeness toggle
* Add failure conditions in run method to fail before creating db records  

Not for mvp
* Non blocking job submission / (Possibly htcondor submit)
* Add thread/reaper to perform actions based on toggle



### Questions

#### Answered:
#### Q: should the number of retries of a job be limited, and if so, where? e.g. a max_retries field in the parent job? wait and see whether people attempt to rerun jobs that have already failed nine zillion times?
A: Make a ticket for this and add to backlog

#### Q: How do we prevent jobs with identical parameters from being rerun more than once within a retry_jobs request?
A: We have decided to allow multiple jobs with the same params to be re-run in the same `retry_jobs` request.

#### Q: How do we find the most recent retry of a job?
A: The client using the ee2 API would have to figure it out using the `retry_parent` and job creation date fields. (Unless we added other fields to help with this)

#### Q: How do we ensure that the app version is correctly run each time when submitting from the narrative?
A: We would need to change the narrative to submit the git commit hash instead of a version tag

#### Q: How do we handle DB consistency during retry failure? 
Looks like the options are
* implement db integrity checks and two-phase commits for making the relationships between a job, its `retry_parent`, and the batch container
* accept that the db info may be incomplete and write workarounds into the clients
* (upgrade to Mongo 4.4 for better transaction support)
A: We have decided to use a `retry_toggle` in order to mark that the entire transaction has occurred for a retry job, and to set up a monitor to fix the jobs that didn't finish the retry lifecycle.

##### Q: Do we want to support ResourceRequirements
A: Probably not in the short term


#### Q: how to prevent incorrect parent-child relationships being created -- should the client be allowed to specify a parent ID? Is it currently possible to add a new child to a parent job if the child is a new job, rather than an existing job ID / set of params that is being rerun?
A: Not necessarily relevant to this endpoint, more of a `run_job_batch` endpoint question. Currently the `retry_parent` and `parent_job_id` are looked up from the ee2 record on retry, and not specified in this endpoint.

#### Shorter Q and A

    Should we track a retry count? (Done)
    Should users see this retry count? A: Visible in the EE2 API, UI is TBD 
    Are retried jobs saved in some sort of data structure linking them, possibly indirectly, to the parent job or are they orphaned? (Yes, retry_parent)
    If the former, is the retry relationship linear or a tree? E.g. what happens if there are two simultaneous calls to retry a job? (Tree, simultaneous jobs run)
    Should it be at least theoretically possible to see the list of retried jobs in order? (It is possible by sorting on creation date)
    Should there be a maximum retry count? Or a warning that more retries are not likely to help?  (Unknown TBD)
    Can a job in states other than failed or canceled be retried? Or should the user be required to cancel a job before it can be retried? (Job must be in Error/Cancel state)


# Work estimation for MVP
Priority descending

### Address data inconsistency via retry_count, retry_ids and retry_toggle
> Estimate 3-4 days
> https://kbase-jira.atlassian.net/browse/DATAUP-461

### Preflight checks
> Estimate 3-4 days
> https://kbase-jira.atlassian.net/browse/DATAUP-528
> Requires retry to be able to force the same app `git_commit versions` and `JobRequirements` from the db records
https://kbase-jira.atlassian.net/browse/DATAUP-461

### Create a created jobs and queued jobs reaper that cancels created jobs older than 1 hour, and cancels queued jobs over 14 days old.
> Estimate 2-3 days 
https://kbase-jira.atlassian.net/browse/DATAUP-536

# Work estimation for POST MVP

###  Hookup retries to refactored code
*  Non blocking job submission for submitting multiple jobs, possibly via using `run_job_multiple` 
*  Requires refactor of retry to gracefully handle jobs with children by notifying the batch containers for retry of ids not in the same batch. If you retry jobs from batch 1 and from batch 2, you want the correct batch parent to be notified. 
*  Switching from starting the retried jobs one at a time to starting them in batch mode will require refactoring how the batch and retry parents are updated
> Estimate 3 days
> https://kbase-jira.atlassian.net/browse/DATAUP-535

Not for MVP
### One single submission to HTCondor instead of multiple job submission ()
> Estimate 1-2 days
> https://kbase-jira.atlassian.net/browse/DATAUP-391
Not for MVP
### Prevent multiple in-flight retries to prevent the user from wasting their own resources (and the queues resources)
> Estimate 3-4 days
https://kbase-jira.atlassian.net/browse/DATAUP-439


