import requests

# Making a request is very easy with requests
response = requests.get('https://api.github.com')

# Take a look at the properties available on this response
# reference: https://docs.python-requests.org/en/latest/api/#requests.Response
print(dir(response), '\n')

# Some important ones to note:

# Every HTTP response has a status code.
# 200 means everything was good. 3xx, 4xx, and 5xx mean errors
# Reference: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
print(response.status_code, '\n') 

# There are MANY headers in HTTP, some more important than others.
# reference: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
print(response.headers, '\n')

# The headers are provided as a dictionary by the requests library. We can
# Therefore get individual header values of interest:
print(response.headers['Content-Type'], "\n")

# If the web response is some kind of formatted text (the vast majority are)
# you can access that text as a string:
print(response.text, '\n\n')

# In this case, we know the data being sent to use is a type called JSON.
# JSON (Javascript Object Notation) is a text format derived from Javascript
# objects, and it is similar to dictionaries in Python. So similar that 
# requests will automatically parse JSON into a dictionary if asked:
content = response.json()
print(content['current_user_url'])


# Micro-exercise: use the requests library to make a get request 
# to a website of your choice. Examine the headers and content 
# of the response object.
