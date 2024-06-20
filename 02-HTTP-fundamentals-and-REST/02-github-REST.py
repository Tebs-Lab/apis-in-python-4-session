import requests

# Github has a RESTful API with a ton of features and resources.
# The documentation lives here: https://docs.github.com/en/rest
# The Github API is extensive, try not to be overwhelmed!

# Lets make a simple request to the GH API that will list
# the Tebs-Lab organizations repositories. See: https://docs.github.com/en/rest/repos/repos
response = requests.get(
    'https://api.github.com/orgs/Tebs-Lab/repos',
)

# GH API uses JSON as the response type, we need to parse it into a dictionary 
list_of_repos = response.json()

# The API returns a list
print(f'There are {len(list_of_repos)} in this result')

# We can loop over them
for repo in list_of_repos:
    print('================')
    print(repo['name'])
    print(repo['description'])
    print('================\n')

# For a particular repo, we can request information about its history
# See: https://docs.github.com/en/rest/repos/repos#list-repository-activities
# The doc specifies that we should use the NAME not the ID for this endpoint
repo_of_interest = list_of_repos[-1] # We'll just get the last one, whatever that is.
response_2 = requests.get(
    f'https://api.github.com/repos/Tebs-Lab/{repo_of_interest["name"]}/activity',
)
list_of_actions = response_2.json()
for action in list_of_actions:
    print('==========')
    print(action['timestamp'])
    print(action['activity_type'])
    print(action['actor']['login'])
    print('==========')

# Last example I'll show you is using the "search" function
# Sometimes HTTP requests include "query parameters" to indicate
# additional information that is optional on a given URL
# For example, the github API allows you to search for repositories
# using the 'q' parameter. 
# Reference: https://docs.github.com/en/rest/reference/search
# Reference 2: https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories

# Note the "params" option is a dictionary.
# 'q' is the name of the query parameter, and the value is 'org:Tebs-Lab'
# Multiple key-value pairs are allowed, though this example only uses one
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'org:Tebs-Lab'}
)

# Query parameters are ultimately expressed as part of the URL:
print(response.url, "\n")

# Again, the Github API is returning JSON
content = response.json()

# Lets look at the names and urls of the matched repositories.
for repo in content['items']:
    print('===========')
    print(f'Name: {repo["name"]}\n{repo["html_url"]}\n')
    print('===========')


# Mini-exercise: Use the search endpoint to find repos with the following properties
# 1) Published by Google (their org name is 'google')
# 2) Have at least 5000 stars
# 3) Have Python code in them
# Then, loop over those repos printing out their name and description
# (useful documentation: https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)