import requests


# org_name = input("Type the organization name: ")
# repo_name = input("Type the repo name: ")

# DEBUG -- Remove
# org_name = 'Tebs-Lab'
# repo_name = 'intro-to-deep-learning'

# DEBUG -- Remove
org_name = 'tensorflow'
repo_name = 'tensorflow'


repo_response = requests.get(
    f'https://api.github.com/repos/{org_name}/{repo_name}',
)

repo_response_content = repo_response.json()
repo_owner = repo_response_content['owner']['login']

# Extracting the requested top level info
description = repo_response_content['description']
url = repo_response_content['url']
star_count = repo_response_content['stargazers_count']
print('====Top Level Details====')
print(f'Owner: {repo_owner}\nName: {repo_name}\nURL: {url}\nDescription: {description}\nStars: {star_count}\n')

# Using the provided URLs rather than hardcoding them
# (as you'll see this will require some formatting code, though)
collaborators_url = repo_response_content['collaborators_url']
pulls_url = repo_response_content['pulls_url']
branches_url = repo_response_content['branches_url']

# This weird syntax is required because of how Python's .format function works
# and how Github has chosen to return these URLs. Each one has some optional sections,
# and those sections are listed by GH like this: /required{/optional}

# This is in a style that Python can use .format, but the normal thing to do is say
# .format(format_value_name=desired_value) in our example's case that would be:
# .format(/optional='hello')

# BUT, the / character is not allowed as a keyword parameter name. So instead
# we're using ** (the 'dictionary unpacking') operator, and a dictionary with the 
# desired key/value pair. 
# (honestly, it might be cleaner to hardcode them, as we did with code_frequency)

branches_resp = requests.get(branches_url.format(**{'/branch': ''}))
branches_data = branches_resp.json()

print('====Branches====')
for b in branches_data:
    print(f'{b["name"]} at commit {b["commit"]["sha"]}\n')

pulls_resp = requests.get(
    pulls_url.format(**{'/number': ''}),
    params={'state': 'open'}
)
pulls_data = pulls_resp.json()

print('====Pull Requests====')
for pr in pulls_data:
    print(f'{pr["title"]} opened by {pr["user"]["login"]} on {pr["created_at"]}\n')

# They don't provider the code frequency URL on the response so we have to generate this one
code_frequency_url = f'https://api.github.com/repos/{org_name}/{repo_name}/stats/code_frequency'

code_frequency_resp = requests.get(code_frequency_url)
if code_frequency_resp.status_code == 202:
    code_frequency_printable = "Code frequency currently unavailable, try later."
elif code_frequency_resp.status_code == 422:
    code_frequency_printable = 'Too many commits, code frequency will never be available.'
else:
    code_frequency_data = code_frequency_resp.json()
    code_frequency_printable = f'Additions: {code_frequency_data[1]}\n Deletions: {code_frequency_data[2]}'

print('====Code Frequency====')
print(code_frequency_printable)