#!/usr/bin/python3

import os
import sys
import subprocess
import requests

# Define a function to clone a GitHub repository
def clone_repo(github_username, repo_name):
    code_dir = os.path.expanduser('~/Code')
    user_dir = os.path.join(code_dir, github_username)
    repo_dir = os.path.join(user_dir, repo_name)

    # Create the user directory if it doesn't exist
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)

    # Clone the repo
    subprocess.run(['git', 'clone', f'https://github.com/{github_username}/{repo_name}.git', repo_dir])


# Define a function to display the directory tree of cloned repositories
def show_code_tree():
    print('\033[1;33m' + '==================================================================================================================' + '\033[0m')
    code_dir = os.path.expanduser('~/Code')
    print('\033[1;37m' + code_dir + '\033[0m')
    print('\033[1;37m' + '    |')

    for github_username in os.listdir(code_dir):
        user_dir = os.path.join(code_dir, github_username)
        print('\033[1;37m' + '    |--' + '\033[1;31m' + github_username + '\033[0m')

        for index, repo_name in enumerate(os.listdir(user_dir)):
            repo_dir = os.path.join(user_dir, repo_name)
            print('        \033[1;37m', end='')
            if index == len(os.listdir(user_dir)) - 1:
                print('+--'  + '\033[0m', end="")
            else:
                print('|--'  + '\033[0m', end='')

            # Get the latest commit checksums for the local and remote repositories
            local_commit = get_latest_commit_local(github_username, repo_name)
            remote_commit = get_latest_commit(github_username, repo_name)
            # Print the repository name, local and remote commit checksums
            print('\033[1;32m' + f'{repo_name} | local: {local_commit} | remote: {remote_commit}' + '\033[0m')

    print('\033[1;33m' + '==================================================================================================================' + '\033[0m')


# Define a function to get the latest commit checksum of a GitHub repository
def get_latest_commit(github_username, repo_name):
    url = f'https://api.github.com/repos/{github_username}/{repo_name}/commits'
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        if len(commits) > 0:
            return commits[0]['sha']
        else:
            return "None"
    else:
        return "None"

# Define a function to get the latest commit checksum of a local GitHub repository
def get_latest_commit_local(github_username, repo_name):
    repo_dir = os.path.expanduser(f'~/Code/{github_username}/{repo_name}')
    cmd = f'cd {repo_dir} && git rev-parse HEAD'
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)

    if result.returncode == 0:
        return result.stdout.decode().strip()
    else:
        return "None"

# Define a function to display the tool's title
def display_title():
    print('\033[1;33m' + '==================================================================================================================' + '\033[0m')
    print('''\033[1;37m   ______ _  __     ______            __         __  ___                                       
  / ____/(_)/ /_   / ____/____   ____/ /___     /  |/  /____ _ ____   ____ _ ____ _ ___   _____
 / / __ / // __/  / /    / __ \ / __  // _ \   / /|_/ // __ `// __ \ / __ `// __ `// _ \ / ___/
/ /_/ // // /_   / /___ / /_/ // /_/ //  __/  / /  / // /_/ // / / // /_/ // /_/ //  __// /    
\____//_/ \__/   \____/ \____/ \__,_/ \___/  /_/  /_/ \__,_//_/ /_/ \__,_/ \__, / \___//_/     
                                                                          /____/               \033[0m''')

# Define the main function to handle command line input and prompts
def main():
    # Display the tool's title
    display_title()

    while True:
        # Always display the list of repositories
        show_code_tree()
        # Prompt the user for input
        print("What would you like to do?")
        print("1. Clone a repository")
        print("2. Quit the tool")
        choice = input("> ")

        if choice == "1":
            # Prompt the user for the GitHub username and repository name to clone
            print("Please enter the GitHub username:")
            github_username = input("> ")
            print("Please enter the repository name:")
            repo_name = input("> ")

            # Clone the repository
            clone_repo(github_username, repo_name)
        elif choice == "2":
            # Quit the tool
            print("Quitting Git Code Manager")
            return
        else:
            # Invalid input
            print("Invalid input. Please try again.")



if __name__ == "__main__":
    main()