import pathlib
import json
from typing import List

import requests


def save_todays_aholes(judgements_directory: pathlib.Path):
    '''
    Fetch and serialize the top posts from the AmITheAsshole subreddit. Serialization format:
    JSON:
    {   
        'situation': str # The users description of the situation.
        'YTA': int, # The number of top-level comments indicating YTA (and so on for others)
        'NTA': int,
        'ESH': int,
        'NAH': int
    }
    '''
    top_urls = fetch_top_urls()

    for url in top_urls:
        votes = compute_votes_from_post_url(url)
        post_mini_title = url.split('/')[-2]

        with open(judgements_directory / f'{post_mini_title}', 'w') as outfile:
            outfile.write(json.dumps(votes))

def fetch_top_urls() -> List[str]:
    # Get the top posts from today.
    all_listings_response = requests.get(
        'https://www.reddit.com/r/AmItheAsshole/top/.json?t=day',
        headers={
            'User-Agent': 'top-daily-ahole-calculator-bot'
        }
    )

    # Extract today's top n posts (set to 3 here to reduce rate limiting):
    top_n_post_urls = []
    for post in all_listings_response.json()['data']['children']:
        top_n_post_urls.append(post['data']['url'])

    return top_n_post_urls


def compute_votes_from_post_url(url: str) -> List[dict]:
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


def compute_NTA_ratio(votes: dict) -> float:
    '''
    Given a dict in the votes serialization format (seen below) compute the 
    ratio of (NTA votes) / (total votes)

    Format:
    {   
        'situation': str # The users description of the situation.
        'YTA': int, # The number of top-level comments indicating YTA (and so on for others)
        'NTA': int,
        'ESH': int,
        'NAH': int
    }
    '''
    total_votes = votes['YTA'] + votes['NTA'] + votes['ESH'] + votes['NAH']
    return votes['NTA'] / total_votes
