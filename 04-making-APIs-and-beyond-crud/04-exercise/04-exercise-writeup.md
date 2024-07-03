# Building and Using Your Own API

In this exercise you'll be challenged to write two pieces of code.

1) An API server that can perform at least one basic CRUD operation, and use at least one RPC style route.
2) A script that utilizes the API.

**Note that:** You should be able to reuse a lot of either your own code, or code from the provided solutions to previous exercises to complete these tasks!

## The Tasks

### The Server 

Using FastAPI, create a server with one route each for performing the following tasks:

* Download the day's judgements from Reddit and save them each into a file.
* Process all the existing judgement files and determine the most wholesome based on largest share of NTA votes.
    * Make a brand new file that is always named `current_most_wholesome`
* A simple GET route that returns the contents of `current_most_wholesome` as JSON
* Make or replace a private gist on your Github account so that it contains whatever the `current_most_wholesome` file contains

**Note that:** You will have to make some decisions on your own about how and where to store these files, and what their format should be. 

### The Script

A script that uses the API server to:

* Gets today's aholes
* Refresh the current_most_wholesome
* Updates the Github gist

## Bonus Points

If you finish early, try adding these two routes to your server, and utilizing them in your script!

* Add a POST route that allows you to manually add a story to the list of files.
    * Ensure whatever JSON data you persist has all (and only) the same values as your serialization format.
* Add a DELETE route that allows you to delete all the existing files.