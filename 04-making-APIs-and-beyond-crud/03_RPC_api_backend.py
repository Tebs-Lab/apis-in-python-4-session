# start this server with the command: fastapi dev 03_RPC_api_backend.py
from fastapi import FastAPI
import requests

app = FastAPI()

# So far, we've done very basic CRUD operations, in a way that is REST compliant.
# So now, lets look at a remote procedure call... hopefully this code looks familiar!
@app.get("/github_repos/{org_name}")
def get_repos(org_name: str):

    # Yo Dog, I heard you like APIs so we put an API call inside your API server...
    response = requests.get(
        f'https://api.github.com/orgs/{org_name}/repos',
    )

    list_of_repos = response.json()
    just_repo_names = [repo['name'] for repo in list_of_repos]

    return just_repo_names


# Another route that steals code from a previous exercise...
@app.get("/todays_top_ahole")
def get_top_ahole_reddit():
    top_post_url = fetch_top_urls(1)[0]
    return compute_votes_from_post_url(top_post_url)


# This function was stolen directly from the first exercise's solution
def fetch_top_urls(n_posts=-1):
    # Get the top posts from today.
    all_listings_response = requests.get(
        'https://www.reddit.com/r/AmItheAsshole/top/.json?t=day',
        headers={
            'User-Agent': 'top-daily-ahole-calculator-bot'
        }
    )

    # Extract today's top n posts (set to 3 here to reduce rate limiting):
    top_n_post_urls = []
    for post in all_listings_response.json()['data']['children'][:n_posts]:
        top_n_post_urls.append(post['data']['url'])

    return top_n_post_urls

# This function was stolen directly from the first exercise's solution
def compute_votes_from_post_url(url):
    # fetch the comments
    comment_response = requests.get(
        url + '.json',
        headers={
            'User-Agent': 'top-daily-ahole-calculator-bot'
        }
    )
    comments_json = comment_response.json()

    votes = {
        'YTA': 0,
        'NTA': 0,
        'ESH': 0,
        'NAH': 0
    }

    # The comments listing is always the second item in the post.
    comments = comments_json[1]['data']['children']
    for comment in comments:
        if comment['kind'] != 't1': continue # t1 is the comment type, sometimes other types appear like "more"
        text = comment['data']['body']
        
        for vote_type in votes.keys():
            if vote_type in text:
                votes[vote_type] += 1

     # Some API's have deeply nested (and weird) data patterns, look at this monstrosity:
    votes['situation'] =  comments_json[0]['data']['children'][0]['data']['selftext']
    return votes

# Mini Exercise: Add a POST route to this app that takes as input 
# a filename and text. Your route should create a file with the 
# specified name and containing the specified text. 