from os import environ # This is the standard way to access env variables in Python
import requests

ACCESS_TOKEN = environ['GITHUB_ACCESS_TOKEN']

# I decided to just make one gist manually, and use the ID so that I'm not making
# tons of random gists.
GIST_ID = '79eae327df279513bc4f253da0a0d090'
GIST_FILENAME = 'current_most_wholesome.json'

def upload_to_gist(votes: str):
    '''
    Given a string, replace the gist file with the contents of the string.

    This will work even if votes is not in the proper format -- but it SHOULD 
    be a string representing json in the VOTES format used for serialization.
    '''
    # Lets prove it worked by doing something we couldn't have done before...
    # We're going to create a gist! (https://docs.github.com/en/rest/gists/gists)
    response = requests.patch(
        f'https://api.github.com/gists/{GIST_ID}',
        headers={
            'Authorization': f'Bearer {ACCESS_TOKEN}'
        },
        # The "json" keyword parameter ensures the data is sent in a JSON format
        # using the normal "data" keyword parameter will cause Requests to encode
        # that data in another common format (that github doesn't accept).
        json={
            'public': False,
            'files': {
                GIST_FILENAME: {
                    'content': votes
                }
            }
        }
    )

    resp_content = response.json()
    return resp_content


