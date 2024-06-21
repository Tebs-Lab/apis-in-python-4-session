# Practice Using the Github API

This exercise has a few goals:

1. Force you to practice searching through and reading API documentation.
    * These docs are written in particular ways and can be hard for beginners to parse.
    * However, there is a lot of overlap in how REST APIs are documented from application to application, so getting used to a single set of docs has future benefits. 
    * Plus, the standard way to learn to use an API is to Read the Docs™ so it's good practice.
    * Be aware, documentation is often incomplete... 

2. Get a sense of what REST APIs can do, and how they might be useful in general.

3. More practice dealing with and handling the request/response cycle
    * Especially, using API responses to generate new, relevant API requests.

## The Exercise -- Repo Report:

Write a script or CLI application that uses the Github API to generate a detailed report about a user-specified repository. Specifically, accept the name of an organization and a repository as input. Use that information and the API to produce a text report (print it to the console or save it to a text file) that includes the following information:

* The description of the repo.
* The URL of the repo
* The number of stars this repository has.
* The number and names of all the branches in the repo, as well as the latest commit hash for each branch.
    * For **bonus points** get the commit message of the latest commit on each branch
    * Sometimes there may be so many results that they are 'paginated'. Just use whatever is returned, in the first response. For **more bonus points**, fetch all the additional pages.
* The number of additions and deletions made to the repo this week.
    * Hint: don't try to calculate this, instead find the right API endpoint...
    * This endpoint has some special cases when the data will not be available. Handle them specially.
        * Hint: Look at the possible status codes in the documentation.
* A list of currently open pull requests against the repo.
    * Print the title, username of the user who opened it, and when it was created
    * Sometimes there may be so many results that they are 'paginated'. Just use whatever is returned, in the first response. For **bonus points**, fetch all the additional pages.

* Small warning: everything labeled as **bonus points** (and especially the commit message for each branch) will require many more requests per run of your script, which may trigger Github's rate limiting. I suggest you complete all non-bonus features first.

## Some Tips

* Only test against public repos so that you don't need to authenticate.
    * A good starting repo is the one containing these materials!
* Add the same User-Agent header to all your requests, it will reduce Github's rate limiting.
* You shouldn't have to calculate or compute much of anything -- the API has endpoints that will give you the data. Find them in the documentation!
* Use functions to separate the work into manageable chunks.
* Run and test your code frequently.
* Pick a task, finish it, move on to the next task. Don't try to do everything all at once. 