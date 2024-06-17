# Exercise: Dictionaries and Lists In The Wild

This exercise is meant to help you:

* Conceptualize how dictionaries and lists are used in real world systems.
* Conceptualize how complex data structures are composed from simpler ones.
* Understand, parse, and process complex data structures.

## The Exercise

The vast majority of real world programming applications rely on some kind of well structured data to perform their job. In this exercise, you'll fetch data about the current front page of the `/r/awww` subreddit (which is a forum dedicated to pictures of cute animals) and parse through that data programmatically to extract the following information for the top posts:

1. The title of the post.
2. The username of the poster.
3. The upvote ratio for this post.
4. The URL for the content (if applicable).

For each post, print this information to the console.

In addition to printing this information, compute the following details about posts:

1. How many users made more than one post?
2. What was the average upvote ratio across all the posts?

## Resources

Reddit provides this data in a textual format called JavaScript Object Format (JSON). This format is ubiquitous on the web for a variety of reasons. Although we use built in tools to parse this JSON formatted data into a deeply nested Python dictionary, you may still want to read this [overview of using the JSON format in Python](https://realpython.com/python-json/).

Reddit's JSON format is "well structured" which means it always follows a consistent set of rules. Many of these rules are documented on [Reddit's API documentation](https://www.reddit.com/dev/api) with additional information about the JSON structure on this [Reddit Wiki page](https://github.com/reddit-archive/reddit/wiki/JSON).

This data can be fetched from any subreddit by adding .json to the end of the usual URL. For example, for the current top posts on /r/awww in json simply go to [https://www.reddit.com/r/aww.json](https://www.reddit.com/r/aww.json).

It can be extremely helpful to look at this data in program designed to navigate JSON. Firefox has an excellent JSON navigator built in, so if you open the JSON URL in Firefox you'll see something like this:

![](assets/firefox-json.png)

If you click on one of the arrows next to a field whose data is also a collection (either a dictionary or list) it will expand.

![](assets/firefox-json-expanded.png)

This popular Chrome extension provides similar functionality in Chrome [https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh). 

If you don't want to install Firefox or this Chrome extension, this online tool provides similar functionality: [https://codebeautify.org/jsonviewer](https://codebeautify.org/jsonviewer).

## Getting Started

If you will not have access to the internet but want to complete this exercise, we have saved the JSON that Reddit was serving at a previous moment in time into the file `supplemental-materials/reddit-awww.json`. The following code will read that data from the file (as opposed to getting the current data from Reddit).

The following code snippet fetches the relevant data from Reddit or the provided file, whichever you specify:

```python
import json
import pathlib
import requests
import ssl

# Change this to False to use the file data.
use_live_data = True

if use_live_data:
    # Fetching the live data from reddit.
    url = "http://www.reddit.com/r/aww.json"
    request = requests.get(url, headers={
        'User-Agent': 'awww-parser-bot-tebs-lab-exercise'
    })

    listing = request.json()
else:
    # Alternatively, loading the data from the provided json file.
    containing_dir = pathlib.Path(__file__).parent.resolve()
    with open(pathlib.Path(containing_dir / 'supplemental-materials' / 'reddit-aww.json')) as json_file:
        listing = json.load(json_file)
```

## Check Your Work

For testing purposes, the answers to our two questions for the data in `supplemental-materials/reddit-awww.json` are provided:

Users `linuxxx4` and `[deleted]` both posted twice, while no other users made more than 1 post. The average upvote ratio is `0.9596153846153844` though it may be possible to get a slightly different answer due to rounding errors that may accrue differently.

## Troubleshooting

Reddit sometimes throttles users who make too many requests too fast. If you get an error like this:

```
urllib.error.HTTPError: HTTP Error 429: Too Many Requests
```

Switch to reading the data from the provided file instead. Once your code works with the file switch back to using the live data.