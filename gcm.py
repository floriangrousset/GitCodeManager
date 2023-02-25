#!/usr/bin/python3

import os
import sys
import subprocess
import requests

def clone_repo(github_username, repo_name):
    code_dir = os.path.expanduser('~/Code')
    user_dir = os.path.join(code_dir, github_username)
    repo_dir = os.path.join(user_dir, repo_name)

    # Create the user directory if it doesn't exist
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)

    # Clone the repo
    subprocess.run(['git', 'clone', f'https://github.com/{github_username}/{repo_name}.git', repo_dir])


def show_code_tree():
    code_dir = os.path.expanduser('~/Code')
    print('\033[1;37m' + code_dir + '\033[0m')
    print('\033[1;37m' + '    |')

    for github_username in os.listdir(code_dir):
        user_dir = os.path.join(code_dir, github_username)
        print('\033[1;37m' + '    |--' + '\033[1;31m' + github_username)

        for index, repo_name in enumerate(os.listdir(user_dir)):
            repo_dir = os.path.join(user_dir, repo_name)
            print('        \033[1;37m', end='')
            if index == len(os.listdir(user_dir)) - 1:
                print('+--', end="")
            else:
                print('|--', end='')
            print('\033[1;32m' + repo_name + "\033[1;37m | local: " + get_latest_commit_local(github_username, repo_name)+ " | remote: " + get_latest_commit(github_username, repo_name))


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


def get_latest_commit_local(github_username, repo_name):
    repo_dir = f'~/Code/{github_username}/{repo_name}'
    cmd = f'cd {repo_dir} && git rev-parse HEAD'
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)

    if result.returncode == 0:
        return result.stdout.decode().strip()
    else:
        return "None"


def display_title():
    print('''   ______ _  __     ______            __         __  ___                                       
  / ____/(_)/ /_   / ____/____   ____/ /___     /  |/  /____ _ ____   ____ _ ____ _ ___   _____
 / / __ / // __/  / /    / __ \ / __  // _ \   / /|_/ // __ `// __ \ / __ `// __ `// _ \ / ___/
/ /_/ // // /_   / /___ / /_/ // /_/ //  __/  / /  / // /_/ // / / // /_/ // /_/ //  __// /    
\____//_/ \__/   \____/ \____/ \__,_/ \___/  /_/  /_/ \__,_//_/ /_/ \__,_/ \__, / \___//_/     
                                                                          /____/               
                                            proudly brought to you by c0d3ki113r
    ''')


def main():
    display_title()
    if len(sys.argv) < 2:
        print("Usage: python git_code_manager.py <command> [parameters]")
        return

    command = sys.argv[1]

    if command == "clone":
        if len(sys.argv) < 4:
            print("Usage: python git_code_manager.py clone <username> <repository>")
            return
        username = sys.argv[2]
        repository = sys.argv[3]
        clone_repo(username, repository)
    elif command == "list":
        show_code_tree()
    else:
        print("Unknown command:", command)


if __name__ == "__main__":
    main()