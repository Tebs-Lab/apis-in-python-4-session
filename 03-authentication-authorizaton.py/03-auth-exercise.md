# Authenticated Github Actions

This exercise continues your practice with the Github REST API. In particular, we're focused on doing things that can only be done by authenticated users. 

## Creating a Fake Repo

You are to write a Python script that, when you run it, does all of the following:

* Creates a new Github repo
    * The repo should have a name and description.
    * It should have public visibility.
    * Issues should be enabled.
    * All other settings are at your discretion.
    * NOTE: if you are creating an organization repo vs a repo for the currently authenticated user, those are different routes. You may do either, the authenticated user route is simpler (plus not everyone has privileges to create an organization repo).

* Add at least 2 files to your repo.
    * A readme.md file, contents of which are at your discretion.
    * A copy of the script that was used to create the repo.
    * You may add any additional files at your discretion.
    * Hint: this will require you to use Base64 encodings. Python has a built in library for this:
        * Python Docs: [https://docs.python.org/3/library/base64.html](https://docs.python.org/3/library/base64.html)
        * Example: [https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/](https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/)

* Create an issue on the repo.
    * The name and description are at your discretion.

* Create a branch.
    * On the branch, cause one of the files to be modified somehow.
    * Hint: branches are a type of "reference" in git nomenclature
        * See: [https://docs.github.com/en/rest/git/refs](https://docs.github.com/en/rest/git/refs)
        * The 'ref' parameter is required and described obtusely. Use "refs/heads/<NEW-BRANCH-NAME>"
        * The 'sha' parameter is also required and described obtusely. Use the SHA hash of the main branch (which you can get from the response from the second file you created, or query for separately)

* Open a Pull Request, requesting the branch you created be merged to the main branch.

## Some Tips and Hints

* Adding a call to the "delete repo" route at the start of your script (and gracefully handling the error if it's already been deleted) can make your workflow simpler.
    * Note: You'll have to generate a new token that's allowed to delete repos.

* Consider working on each step in sequence, then ensuring it all works together at the end. For example:
    * Get the create repo call working, then comment out that code and...
    * Successfully add 2 files, then comment out that code and...
    * Create an issue, then comment out that code and... 
    * ... and so on ...