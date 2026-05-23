# Fetch Repository Worker


## Issue

The end-point for fetching repositories may take too long to respond since it needs to fetch the repository issues from the GitHub API using pagination. The high quantity of requests per repository would abuse the GitHub API rate limits.


## Description

To calculate the issues average age of an repository, we need to fetch all the issues from the repository using the GitHub API. To do that, we need to iterate over all the pages, which has a limit of 100 issues per page. There are repositories that may need too many requests to fetch all of the issues, e.g. [angular/angular](https://github.com/angular/angular) with 21,678 issues at 25/10/2020. For this one, we would need to make 217 requests to the GitHub API. Doing this discriminately would abuse the API rate limits.


## Decision

Decided to move the refreshing of repositories to a worker with a limit of parallel jobs at a time.


## Details

  * Requests to fetch a repository data with many issues would take longer than 15 seconds, which is a common timeout value, and is way far from an acceptable response time.

  * Issues statistics, which can only be calculated by paginating the issues, should never be calculated in the end-point for the reason above.

  * When a repository is not in the database, the end-point still needs to fetch the minimum information that can be provided to the user.

  * Using an worker gives more control over the number of requests sent to the GitHub API.


## Notes

  * This may help it to not reach the API rate limit, but it's still possible to happen. By requesting many different repositories with a high number of issues inside the period of one hour would make it reach the limit even with the limit of parallel jobs.
