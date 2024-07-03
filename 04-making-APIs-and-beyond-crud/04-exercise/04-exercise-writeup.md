# An RPC Server

In this exercise you'll be challenged to write two pieces of code.

1) An API server that can perform at least one basic CRUD operation, and use at least one RPC style route.
2) A script that utilizes the API.

**Note that:** You should be able to reuse a lot of either your own code, or code from the provided solutions to previous exercises to complete these tasks!

## The Tasks

A route each for:

* Download the day's judgements and save them each into a file
* Process all the existing judgement files and determine the most wholesome (largest share of NTA votes)
    * Make a brand new file that is always named `current_most_wholesome`
* A simple GET route that returns the contents of `current_most_wholesome` as JSON
* Make or replace a private gist on your Github account so that it contains whatever the `current_most_wholesome` file contains

A script that uses the API to:

* Gets today's aholes
* Refresh the current_most_wholesome
* Updates the Github gist

### Bonus Points

* Add a POST route that allows you to manually add a story to the list of files
* Add a GET route that allows you to fetch the contents any story by it's file name
* Add a DELETE route that allows you to delete all the existing files.