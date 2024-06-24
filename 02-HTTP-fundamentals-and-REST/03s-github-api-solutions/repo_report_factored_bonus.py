import argparse
from os import environ 
import requests

###### NOTE THAT #######
# This solution uses authentication because the bonus point problems tend to 
# quickly run into rate limiting issues without authentication. 
# If you have an environment variable called GITHUB_ACCESS_TOKEN with a valid
# access token it will be used to authenticate. If you don't the code will run
# but you'll surely reach your rate limit before the report finishes.
########################

ACCESS_TOKEN = environ['GITHUB_ACCESS_TOKEN']

def main():
    parser = argparse.ArgumentParser(
        prog = "Github Repo Report",
        description = "Given a Github owner name and Github repo name, generate a report about that repo"
    )

    parser.add_argument("owner", type=str, help="The name of the owner of the repo")
    parser.add_argument("repo", type=str, help="The name of the repo itself")
    parser.add_argument("output_filename", type=str, help="The name of the file to write this report to")
    args = parser.parse_args()

    with open(args.output_filename, 'w') as output_file:
        extract_top_level_details(args.owner, args.repo, output_file)
        extract_branches_details(args.owner, args.repo, output_file)
        extract_pull_request_details(args.owner, args.repo, output_file)
        extract_code_frequency_details(args.owner, args.repo, output_file)


def extract_top_level_details(repo_owner, repo_name, output_file):
    """
    Args:
        repo_owner (str) -- the name of a Github user or organization
        repo_name (str) -- the name of a Github repo owner by the repo_owner
        output_file (file) -- a text file representing the report
    
    Query the Github API then write the following to the specified file:
        Owner, name, URL, description, number of stargazers
    """
    repo_response = requests.get(
        f'https://api.github.com/repos/{repo_owner}/{repo_name}',
        headers={
            'Accept': 'application/json',
            'User-Agent': "Teb's Lab Github Exercise bot",
            'Authorization': f'Bearer {ACCESS_TOKEN}'
        }
    )

    repo_response_content = repo_response.json()
    repo_owner = repo_response_content['owner']['login']

    # Extracting the requested top level info
    description = repo_response_content['description']
    url = repo_response_content['url']
    star_count = repo_response_content['stargazers_count']
    
    output_file.write('====Top Level Details====\n')
    output_file.write(f'Owner: {repo_owner}\nName: {repo_name}\nURL: {url}\nDescription: {description}\nStars: {star_count}\n\n')



def extract_branches_details(repo_owner, repo_name, output_file):
    """
    Args:
        repo_owner (str) -- the name of a Github user or organization
        repo_name (str) -- the name of a Github repo owner by the repo_owner
        output_file (file) -- a text file representing the report

    Query the Github API then write the following to the specified file:
        One line for every branch with the branch name, most recent commit hash, and that commit's message
    """
    output_file.write('====Branches====\n')
    
    branches_resp = requests.get(
        f'https://api.github.com/repos/{repo_owner}/{repo_name}/branches',
        headers={
            'Accept': 'application/json',
            'User-Agent': "Teb's Lab Github Exercise bot",
            'Authorization': f'Bearer {ACCESS_TOKEN}'
        })
    
    while True:
        branches_data = branches_resp.json()
        for b in branches_data:
            commit_resp = requests.get(
                f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits/{b["commit"]["sha"]}',
                headers={
                    'Accept': 'application/json',
                    'User-Agent': "Teb's Lab Github Exercise bot",
                    'Authorization': f'Bearer {ACCESS_TOKEN}'
            })

            commit_data = commit_resp.json()
            commit_message = commit_data['commit']['message']
            output_file.write(f'{b["name"]} at commit {b["commit"]["sha"]}\nmessage: {commit_message}\n\n')
        
        # Pagination
        if branches_resp.links and branches_resp.links.get('next'):
            branches_resp = requests.get(
                branches_resp.links['next']['url'],
                headers={
                    'Accept': 'application/json',
                    'User-Agent': "Teb's Lab Github Exercise bot",
                    'Authorization': f'Bearer {ACCESS_TOKEN}'
            })
        else:
            break


def extract_pull_request_details(repo_owner, repo_name, output_file):
    """
    Args:
        repo_owner (str) -- the name of a Github user or organization
        repo_name (str) -- the name of a Github repo owner by the repo_owner
        output_file (file) -- a text file representing the report
    
    Query the Github API then write the following to the specified file:
        One line per PR containing the title, username of the creator, and the date it was created

    """
    pulls_resp = requests.get(
        f'https://api.github.com/repos/{repo_owner}/{repo_name}/pulls',
        params={'state': 'open'},
        headers={
            'Accept': 'application/json',
            'User-Agent': "Teb's Lab Github Exercise bot",
            'Authorization': f'Bearer {ACCESS_TOKEN}'
        }
    )
    
    output_file.write('====Pull Requests====\n')
    while True:
        pulls_data = pulls_resp.json()
        for pr in pulls_data:
            output_file.write(f'{pr["title"]} opened by {pr["user"]["login"]} on {pr["created_at"]}\n')

        # Pagination
        if pulls_resp.links and pulls_resp.links.get('next'):
            pulls_resp = requests.get(
                pulls_resp.links['next']['url'],
                headers={
                    'Accept': 'application/json',
                    'User-Agent': "Teb's Lab Github Exercise bot",
                    'Authorization': f'Bearer {ACCESS_TOKEN}'
            })
        else:
            break


def extract_code_frequency_details(repo_owner, repo_name, output_file):
    """
    Args:
        repo_owner (str) -- the name of a Github user or organization
        repo_name (str) -- the name of a Github repo owner by the repo_owner
        output_file (file) -- a text file representing the report
    
    Query the Github API then write the following to the specified file:
        The number of additions and deletions this week
    """
    code_frequency_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/stats/code_frequency'

    code_frequency_resp = requests.get(
        code_frequency_url,
        headers={
            'Accept': 'application/json',
            'User-Agent': "Teb's Lab Github Exercise bot",
            'Authorization': f'Bearer {ACCESS_TOKEN}'
        })
    
    if code_frequency_resp.status_code == 202:
        code_frequency_printable = "Code frequency currently unavailable, try later.\n"
    elif code_frequency_resp.status_code == 422:
        code_frequency_printable = 'Too many commits, code frequency will never be available.\n'
    else:
        code_frequency_data = code_frequency_resp.json()
        code_frequency_printable = f'Additions: {code_frequency_data[1]}\n Deletions: {code_frequency_data[2]}\n'

    output_file.write('\n====Code Frequency====\n')
    output_file.write(code_frequency_printable)

if __name__ == '__main__':
    main()