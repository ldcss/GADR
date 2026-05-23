# Replace KBParallels with another solution to avoid Deadlocks

Date: 2021-09-22

[Related ADR](https://github.com/kbase/execution_engine2/blob/develop/docs/adrs/rework-batch-analysis-architecture.md)

## Note
This ADR is more of a place to keep the current discussions we had at https://docs.google.com/document/d/1AWjayMoqCoGkpO9-tjXxEvO40yYnFtcECbdne5vTURo
Rather than to make a decision. There is still more planning, scoping and testing involved before we can fully design this system.

Still to be determined (not in scope of this ADR):
* UI and how it relates to the bulk execution
* XSV Analysis and how it relates to the bulk execution


## Intro
Sometimes a calculation requires too many resources from one node (walltime, memory, disk), so the calculation gets spread across multiple machines.
The final step of the app that uses KBParallels is to create a report. This step may use results from all of the computed jobs to create the final report.
In order to do this, the following apps use a mechanism called KBParallel
* kb_Bowtie2
* refseq_importer
* kb_concoct
* kb_phylogenomics
* kb_hisat2
* kb_meta_decoder
* kb_Bwa

## The current implementation of Batch Analysis in [kb_BatchApp](https://github.com/kbaseapps/kb_BatchApp) at KBase has the following issues:

* Current UI is not adequate: Users shouldn’t have to code in order to run batch analysis. Also it’s difficult to do so, even for those familiar with KBase code (have to find object names)
* Dependency on [KBParallel](https://github.com/kbaseapps/KBParallel): any changes to KBParallel could affect KB Batch and subsequently all other apps. 
* Queue deadlocking: users have a max of 10 slots in the queue, with the current implementation one management job is created to manage the jobs that it submits. This could lead to deadlock scenarios, as there can be 10 management jobs waiting to submit computation jobs, but they cannot, as there all slots are being used up.
* KBP can spawn other KBP jobs. Batch jobs can spawn other batch jobs. 
* Missing the ability to be able to run, manage (cancel) and track jobs and their subjobs along with the ability to specify resources differently between the main and sub jobs
* No good way to test and hard to benchmark or measure performance 
* Code is split more than is necessary
* UI doesn't properly display progress of batch jobs

## Author(s)

@bio-boris, @mrcreosote

## Status
Needs more planning, but current ideas are documented here


## Decision Outcome (pending more research to iron out more details)

For the first pass, we would likely limit the number of kbparallel runs.

For the next pass, we would want to create a comprehensive generalized solution to submit,split and aggregate, with recipes or conveniences for common operations for creating sets, reports, or things of that nature.

We would also want to do a user study on what we want from the UI and which functionality we want, as the UI may inform the design of the backend system.


### Deprecate KBP and instead break out apps into 3 parts

* Fan out (FO)
* Process in parallel (PIP)
* Fan in (FI)


### Steps:
1. User launches job as normal
2. Possibly the job is marked as a FO job, Makes it easier for the UI to display the job correctly initially, Ideally would be marked in the spec, but this might be a lot of work Could potentially be marked in the catalog UI (e.g. along with the job requirements) 
3. Job figures out what the PIP / sub jobs should be
4. Job sends the following info to EE2
* Its own job ID
* The parameters for each of the sub jobs
* The app of the FI job, e.g. kb_phylogenomics/build_microbial_speciestree_reduce
* EE2 starts the subjobs and associates them with with FO job (Probably need retry handling for the subjobs to deal with transient errors)
5. Whenever a subjob finishes, EE2 checks to see if all the subjobs are finished
* If true, EE2 starts the FI job, providing the outputs of the subjobs as a list to the reduce job
* When the FI job is finished, the job is done.
* The various jobs can communicate by storing temporary data in the caching service or in the Blobstore. If the latter is used, the FI job should clean up the Blobstore nodes when its complete.
* Could make a helper app for this?
* What about workflow engines (WDL, Cromwell)? Are we reinventing the wheel here?
* Can new EE2 endpoints speed up or reduce the complexity of any of these steps?

### Notes about DAG in ee2 Endpoints
```
Your dag would need to have (at least) a first job followed by a SUBDAG EXTERNAL.
Somewhere in the first job you'd generate a new dag workflow that
defines the N clusters followed by the N+1 job, which runs in the
subdag.

As for DAGMan support in the Python bindings, we do this in the
following two ways:

1) There is a htcondor.Submit.from_dag() option which takes the name
of a dag filename. You then submit the resulting object just like any
regular job.
2) We have a htcondor.dags library which can be used to
programmatically construct a DAG workflow in computer memory, then
write to a .dag file and submit using the function mentioned in 1)
above.
```

Between these there are several different ways to do what you want.

There's a useful example here that shows the general workflow in the
bindings: https://htcondor.readthedocs.io/en/latest/apis/python-bindings/tutorials/DAG-Creation-And-Submission.html#Describing-the-DAG-using-htcondor.dags

## Consequences

* We will have to implement a new narrative UI, however this was work that would happen regardless due as we are looking to improve the UX for batch upload and analysis at KBase. 
* This will take significant time to further research and engineer the solutions

Still to be determined (not in scope of this ADR): 
* UI and how it relates to the bulk execution
* XSV Analysis and how it relates to the bulk execution

## Alternatives Considered

* Ignore most issues and just make apps that run kbparallels limited to N instances of kbparallels per user to avoid deadlocks
* Remove kbparallels and change apps to a collection of 2-3 apps that do submit, split and aggregate and an use an ee2 endpoint to create a DAG
* Different DevOps solutions
* Rewriting KBP or swapping it out for a lightweight alternative that has a subset of the KBP features


## Pros and Cons of the Alternatives

### General Notes
*  With the current implementation of KBP, Having a separate KBP queue with multiple machines can save a spot from a user's 10 job maximum for running more jobs, but takes up / wastes compute resources (especially if the nodes sit idle). The user still gets  10 jobs, but there are less spots for jobs to run overall in the system if we make another queue, as this requires taking up more compute nodes that are currently dedicated to the NJS queue.
* Without changing apps that use KBP, running multiple KBP apps on the same machine can interfere with each other and we want to avoid this. 
* If we scrap KBP in favor of a "lightweight alternative" we can avoid some of the previous issues, if we modify all apps that use KBP to use a lightweight alternative.  A lightweight alternative would have to guarantee that no computation besides job management occured, and then we could have the management jobs sit and wait for other jobs without interfering with other jobs on the system. 

### Increase number of slots per user > 10
* `+` Simple solutions, quick turnarounds, fixes deadlock issue for small numbers of jobs.
* `-` Doesn't fix deadlock issue as the user can still submit more KBP jobs
* `-` Addresses only the deadlocking issue, UI still broken for regular runs and batch runs
* `-` A small amount of users can take over the entire system by being able to submit more than 10 jobs
* `-` > 10 nodes will continue be taken up by jobs that do little computation as each job gets its own node
* `-` Capacity is still wasted, as some KBP jobs sit around waiting for other jobs to run

### LIMIT KBP jobs to a maximum of N<10 active KBP jobs per user
* `+` Simple solution requires ee2 to maintain list of KBP apps, and add a KBP_LIMIT to jobs from this list. [Condor](https://github.com/kbase/condor/pull/26) will need KBP_LIMIT Added
* `+` List of apps is not frequently updated
* `+` Apps do not need to be modified
* `-` If a new app uses KBP and their app is not on the list, it won't be limited by the KBP_LIMIT unless the owner lets us know.
* `-` If an existing app no longer uses KBP, their app is still limited unless the owner lets us know.
* `-` Nodes will continue be taken up by jobs that do little computation as each job gets its own node.
* `-` Users may not be able to effectively use up their 10 job spots 
* `-` Capacity is still wasted, as some KBP jobs sit around waiting for other jobs to run

###  LIMIT KBP jobs to a maximum of N<10 active jobs per user + Seperate queue for kbparallels apps 
* `+` Same pros as above
* `+` Users will be able to more effectively use their 10 job spots
* `+` Allows us to group up KBP jobs onto fewer machines, instead of giving them their entire node
* `-` Requires going through each app and understanding the worst case computational needs in order to  set the estimated cpu and memory needs for each app 
* `-` Apps can interfere with other innocent apps and take them down
* `-` Creating a new queue requires balancing between how many active KBP nodes there vs how many nodes are available for other NJS jobs.
* `-` Capacity is still wasted, as some KBP jobs sit around waiting for other jobs to run


### Build KBP Lightweight Version + KBP Queue


#### Design of new verison


* All apps must be modified to use the new KBP lightweight version, which will: 
* Can either modify KBP, or create a new tool/package to use instead of KBP


1) Launch a management job called the *Job Manager* that sits in the KBP Queue, alongside other KBP jobs. Other jobs are launched in the NJS queue.
2) Launch the *Setup Job* which will
 * Use the *User Parameters* and/or
 * Optionally Download the Data from the *User Parameters*  to figure out *Job Manager* parameters
 * Use the results of information gathered from the initial download and or *User Parameters*
 * Generate final parameters to be sent to the *Job Manager* to launch *Fan Out* jobs, or directly launch *Fan Out* jobs and return job ids
3) The *Job Manager* now has enough parameters to launch and/or monitor *Fan Out* Jobs, and monitor/manage the jobs (and possibly retry them upon failure)
4) *Fan Out* jobs download data and perform calculations, save them back to the system, and return references to the saved objects
5) The *Job Manager* launches one *FanIn* job based on User Parameters and or the results of *Fan Out* Jobs
6) The *FanIn* (a.k.a Group/Reduce/Report) job downloads objects from the system, and creates a set or other grouping, and then saves the object(s) back to the system. Final data and report is uploaded back to the system
8) The *Job Manager* returns the reference to the results of the *Report Job*

Pros/Cons

* `+` All KBP jobs can run on a small subset of machines, deadlock issue is fixed
* `+` No changes to ee2 required
* `-` Addresses the deadlocking issue, UI still broken for regular runs and batch runs if we re-use KBP
* `-` On an as needed basis, would have to rewrite apps that use KBP to use this new paradigm

 
### Modify Apps to do only local submission by remove KBP, and moving the job 
* `+` Simple solutions, quick turnarounds, fixes deadlock issue, fixes UI issues
* `-` We have a limited number of larger resources machines
* `-` Continued dependency on deprecated KBP tools
* `-` App runs may take longer since fewer resources may be available to the app run
