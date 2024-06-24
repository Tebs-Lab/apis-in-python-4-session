from os import environ # This is the standard way to access env variables in Python
import requests

# Now that we have a token saved in our environment variables we have to use it in our 
# requests to the Github API. Github expects us to use the "Authorization: Bearer [TOKEN]" 
# header scheme, so lets do it.

# environ is just a dictionary!
access_token = environ['GITHUB_ACCESS_TOKEN']

# This code reads the content of this file into a string, which we're 
# going to copy to a Github gist using the API!
with open(__file__, 'r') as this_file:
    full_script_text = this_file.read()

# Lets prove it worked by doing something we couldn't have done before...
# We're going to create a gist! (https://docs.github.com/en/rest/gists/gists)
response = requests.post(
    'https://api.github.com/gists',
    headers={
        'Authorization': f'Bearer {access_token}'
    },
    # The "json" keyword parameter ensures the data is sent in a JSON format
    # using the normal "data" keyword parameter will cause Requests to encode
    # that data in another common format (that github doesn't accept).
    json={
        'description': 'This is a gist I created via the API. The content is the script I used. Neat!',
        'public': False,
        'files': {
            'create_gist.py': {
                'content': full_script_text
            }
        }
    }
)

resp_content = response.json()
print(resp_content['url'])
print(resp_content['html_url'])

# Mini-Exercise: Use the same endpoint (/gists) with the GET method and find your 
# brand new gist in the list Github returns!
# NOTE: you should comment out the code above so you don't keep re-creating the gist...
