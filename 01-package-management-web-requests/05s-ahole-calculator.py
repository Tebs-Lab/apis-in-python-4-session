import requests
import pathlib

# Reusable format string for printing
AHOLE_FORMAT_STRING = """
URL: {url}
==========================
The Situation: {situation}
==========================

Votes:
YTA: {YTA}
NTA: {NTA}
ESH: {ESH}
NAH: {NAH}
"""

def main():
    top_urls = fetch_top_urls()

    # Bonus, create a folder to store the summary judgments:
    output_dir = pathlib.Path(__file__).parent / 'judgments'
    output_dir.mkdir(exist_ok=True)
    
    print(f'======Top Daily AHole Judgements====')
    for url in top_urls:
        votes = compute_votes_from_post_url(url)
        summary_text = AHOLE_FORMAT_STRING.format(url=url, **votes)
        print(summary_text)

        # Bonus: write each post to it's own file!
        post_mini_title = url.split('/')[-2]

        with open(output_dir / f'{post_mini_title}', 'w') as outfile:
            outfile.write(summary_text)

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
        # if comment['kind'] != 't1': continue # t1 is the comment type, sometimes other types appear like "more"
        text = comment['data']['body']
        
        for vote_type in votes.keys():
            if vote_type in text:
                votes[vote_type] += 1

     # Some API's have deeply nested (and weird) data patterns, look at this monstrosity:
    votes['situation'] =  comments_json[0]['data']['children'][0]['data']['selftext']
    return votes

if __name__ == '__main__':
    main()