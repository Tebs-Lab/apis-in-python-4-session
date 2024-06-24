# This is a built in function that acts like input, but doesn't show what is being typed
# in the console for safety / security purposes
from getpass import getpass 

from bs4 import BeautifulSoup
import requests


# Pretend we're a browser... this isn't strictly necessary
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# The format Github expects for a login is particular.
login_data = {
    'commit': 'Sign in',
    'utf8': '%E2%9C%93',
    'login': input("Type your username: "),
    'password': getpass('Type your password: ')
}

# Using requests "session" object will automatically persist cookies, like a web browser would
with requests.Session() as session:
    url = "https://github.com/session"
    response = session.get(url, headers=headers)

    # Github's web interface uses something called an "authenticity token"
    # which it embeds in the HTML response. If you attempt to login without 
    # passing this value, Github refuses the connection. We extract that with
    # BeautifulSoul (an HTML parsing library)
    # (this makes it harder to execute brute force password attacks)
    soup = BeautifulSoup(response.content, 'html.parser')
    login_data['authenticity_token'] = soup.find('input', attrs={'name': 'authenticity_token'})['value']

    response_2 = session.post(url, data=login_data, headers=headers)

    # Now we should be logged in, lets look at the cookie!
    print(response_2.headers['set-cookie'])

    # Github requires 2-factor auth!
    # Need the new authenticity token
    soup = BeautifulSoup(response_2.content, 'html.parser')
    verification_data = {
        'authenticity_token': soup.find('input', attrs={'name': 'authenticity_token'})['value'],
        'app_otp': input('Type the key from 2FA app: ')
    }
    response_3 = session.post('https://github.com/sessions/two-factor', headers=headers, data=verification_data)
    print(response_3.status_code)
    
    # We should also be able to go to the settings/profile url without getting an error or redirect
    # because we appear to be a logged in user!
    response_4 = session.get('https://github.com/settings/profile', headers=headers, data=verification_data)

    # The HTML for a real settings/profile page includes your name in the settings header
    # so lets try to extract that!
    soup = BeautifulSoup(response_4.content, 'html.parser')
    name_anchor = soup.select('#settings-header a')
    print(name_anchor[0].contents[0])

# Outside of the session, we no longer have a cookie. Lets see what happens when we go to the 
# settings/profile, since it should be different!
response_5 = requests.get('https://github.com/settings/profile')
print(response_5.status_code)

# I'll just show you the difference in lengths between a logged in profile and a non-logged in profile.
print(len(response_5.content), len(response_4.content))