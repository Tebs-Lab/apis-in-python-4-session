import requests

# One way you'll want to modify your requests is by 
# adding header values. This is also done using a dictionary.

# In this example we're setting the User-Agent header, which 
# is used to tell the server what kind of program is making the 
# request. Many APIs use this data to rate limit bad acting user
# agents, track bots, or calculate metrics about who is using the
# service.
# 
# We're also setting the 'Accept' header, which tells the server
# what kind of data we're willing to get back. Some APIs can send
# their response in multiple formats, and they can accommodate our
# request for a particular kind of data.
# 
# This API, the dad jokes API, asks that we send both of these in it's
# documentation: https://icanhazdadjoke.com/api

# Many APIs will not respond, or will severely rate limit programs that 
# do not respect the API's requests.
response = requests.get(
    'https://icanhazdadjoke.com/',
    headers={
        'Accept': 'text/plain',
        'User-Agent': 'Tebs Lab Learn Python Bot|contact:https://www.tebs-lab.com/contracting'
    }
)

# Here's your random dad joke.
print(response.text, '\n')

# Mini-exercise: Read the section of the documentation for this dad joke api about the 
# Accept header (https://icanhazdadjoke.com/api) then make a request for each of the three
# valid options. Examine the results, how are they different?