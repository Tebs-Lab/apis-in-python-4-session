import base64
from os import environ # This is the standard way to access env variables in Python

import webbrowser

import requests
from openai import OpenAI

# To reduce code duplication
HEADERS = {
    'Accept': 'application/json',
    'User-Agent': "Teb's Lab Github Exercise bot",
    'Authorization': f'Bearer {environ["GITHUB_ACCESS_TOKEN"]}'
}

def main():
    # Initialize the OpenAI client
    client = OpenAI()

    willing_to_spend = input('WAIT! Running this script will use some of your OpenAI budget. Type "yes" to continue.\n')
    if willing_to_spend != 'yes':
        print("You did not type 'yes' so this program is exiting.")
        quit()

    # Fetch the authenticated user to get the login name, which will be needed later
    response = requests.get('https://api.github.com/user', headers=HEADERS)
    user_name = response.json()['login']

    # Keeping these static for simplicity
    repo_name = input("Type the name of the repo. No spaces allowed.\n")
    repo_description = 'I made this repo using a Python script. That script is even in this repo!! Neat.'

    # Use gpt-3.5-turbo to generate a markdown file.
    readme_completion = client.chat.completions.create(
    model="gpt-3.5-turbo", # Because its the cheapest one
        messages=[
            {"role": "system", "content": "You are a utilitarian assistant responding simply and concisely"},
            {"role": "user", "content": "Generate a readme file for a github repository. Use markdown. Use 1000 words or less."}
        ]
    )
    readme_content = readme_completion.choices[0].message.content
    
    create_repo_response = create_repo(repo_name, repo_description)
    f1_response = add_file_to_repo(user_name, repo_name, 'readme.md', readme_content)

    with open(__file__, 'r') as this_file:
        this_file_as_str = this_file.read()
    f2_response = add_file_to_repo(user_name, repo_name, 'repo_creator.py', this_file_as_str)
    
    # We need this for later!
    hash_for_new_branch = f2_response.json()['commit']['sha']

    # Use AI to generate the body of the issue
    issue_completion = client.chat.completions.create(
    model="gpt-3.5-turbo", # Because its the cheapest one
        messages=[
            {"role": "system", "content": "You are a utilitarian assistant responding simply and concisely"},
            {"role": "user", "content": "Generate the body of a Github issue related to autogeneration of Github repositories using the Github API. Use markdown. Use less than 500 words."}
        ]
    )
    issue_content = issue_completion.choices[0].message.content
    create_issue_response = create_issue(user_name, repo_name, "This repo is actually whack.", issue_content)
    
    new_branch_name = 'a_branch'
    create_branch_response = create_branch(user_name, repo_name, hash_for_new_branch, new_branch_name)

    # Use AI to modify the body it previously created.
    modification_completion = client.chat.completions.create(
    model="gpt-3.5-turbo", # Because its the cheapest one
        messages=[
            {"role": "system", "content": "You are a utilitarian assistant responding simply and concisely"},
            {"role": "user", "content": f"Modify the following text to make sure it's at an 8th grade reading level:\n{readme_completion}"}
        ]
    )
    modified_readme = modification_completion.choices[0].message.content

    # We need some data from the file we're gonna modify:
    f1_contents = f1_response.json()
    modify_file_response = modify_existing_file(
        user_name, 
        repo_name, 
        f1_contents['content']['path'], 
        f1_contents['content']['sha'], 
        modified_readme, 
        new_branch_name
    )

    open_pr_response = open_merge_pr(
        user_name, 
        repo_name, 
        new_branch_name,
        'main', # main is the default first branch name
        'We need to merge!',
        'This new branch is way better, you need to merge it.'
    ) 

    webbrowser.open(create_repo_response.json()['html_url'], new=0, autoraise=True)


'''* Creates a new Github repo
    * The repo should have a name and description.
    * It should have public visibility.
    * Issues should be enabled.
    * All other settings are at your discretion.'''
def create_repo(repo_name, repo_description):
    response = requests.post(
        'https://api.github.com/user/repos',
        headers=HEADERS,
        json={
            'name': repo_name,
            'description': repo_description
            # public and allow issues are the defaults, so I'm not specifying them explicitly.
        })
    
    return response


'''
* Add at least 2 files to your repo.
    * A readme.md file, contents of which are at your discretion.
    * A copy of the script that was used to create the repo.
    * You may add any additional files at your discretion.
    '''
def add_file_to_repo(owner_name, repo_name, file_name, file_contents):
    # Because of Github's and the requests library's expectations we have to do this
    # weird things with the contents...
    # Github requires file contents be encoded as base64 binary data. Requests and
    # JSON don't accept binary data, though. So we encode the raw content into Base64,
    # then interpret that Base64 as a utf-8 string which we actually pass to the API. Whack.
    file_contents_encoded = base64.b64encode(file_contents.encode('utf-8'))
    encoded_file_as_str = file_contents_encoded.decode('utf-8')
    response = requests.put(
        f'https://api.github.com/repos/{owner_name}/{repo_name}/contents/{file_name}',
        headers=HEADERS,
        json={
            'message': f'Created {file_name}.',
            'content': encoded_file_as_str
    })
    
    return response

'''
* Create an issue on the repo.
    * The name and description are at your discretion.
'''
def create_issue(owner_name, repo_name, issue_name, issue_description):
    response = requests.post(
        f'https://api.github.com/repos/{owner_name}/{repo_name}/issues',
        headers=HEADERS,
        json={
            'title': issue_name,
            'body': issue_description
    })
    
    return response


'''
* Create a branch.
    * On the branch, cause one of the files to be modified somehow.
'''
def create_branch(owner_name, repo_name, source_branch_hash, new_branch_name):
    response = requests.post(
        f'https://api.github.com/repos/{owner_name}/{repo_name}/git/refs',
        headers=HEADERS,
        json={
            'ref': f'refs/heads/{new_branch_name}',
            'sha': source_branch_hash
    })
    
    return response


def modify_existing_file(owner_name, repo_name, file_path, file_sha, new_file_content, branch_name):
    file_contents_encoded = base64.b64encode(new_file_content.encode('utf-8'))
    encoded_file_as_str = file_contents_encoded.decode('utf-8')
    response = requests.put(
        f'https://api.github.com/repos/{owner_name}/{repo_name}/contents/{file_path}',
        headers=HEADERS,
        json={
            'message': f'Modified {file_path}.',
            'content': encoded_file_as_str,
            'branch': branch_name,
            'sha': file_sha
    })
    
    return response


'''
* Open a Pull Request, requesting the branch you created be merged to the main branch.
'''
def open_merge_pr(owner_name, repo_name, branch_to_merge, merge_into_branch, title, description):
    response = requests.post(
        f'https://api.github.com/repos/{owner_name}/{repo_name}/pulls',
        headers=HEADERS,
        json={
            'title': title,
            'head': branch_to_merge,
            'base': merge_into_branch,
            'body': description
    })
    
    return response


if __name__ == '__main__':
    main()