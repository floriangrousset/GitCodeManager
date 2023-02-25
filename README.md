# Git Code Manager

<pre>
   ______ _  __     ______            __     
  / ____/(_)/ /_   / ____/____   ____/ /___  
 / / __ / // __/  / /    / __ \ / __  // _ \ 
/ /_/ // // /_   / /___ / /_/ // /_/ //  __/ 
\____//_/ \__/   \____/ \____/ \__,_/ \___/  
    __  ___                                       
   /  |/  /____ _ ____   ____ _ ____ _ ___   _____
  / /|_/ // __ `// __ \ / __ `// __ `// _ \ / ___/
 / /  / // /_/ // / / // /_/ // /_/ //  __// /    
/_/  /_/ \__,_//_/ /_/ \__,_/ \__, / \___//_/     
                             /____/
</pre>
Tired of having your GitHub repositories scattered all over your local file system and not necessarily up to date?

Git Code Manager is a command-line tool for managing cloned GitHub repositories in a clean fashion on your local file system under the ~/Code/ folder. It helps with keeping your locally cloned repositories always organized and up to date. Current features include cloning repositories from GitHub, displaying the directory tree of cloned repositories along with their latest local and remote commit checksum.

All reposotories are stored in the following directory structure:

```bash
~/Code
    |
    |--username
        +--repository
```

More features are coming soon like auto comparison of local and remote repositories, auto update of local repositories, and more.

## Usage

To run the tool, simply run the following command in your terminal:
```bash
$ ./gcm.py
```

This will start an interactive menu with two options:

 - Clone a GitHub repository: allows users to clone a GitHub repository and store it in the proper directory structure in the local file system.
 - List cloned repositories: allows users to display the directory tree of cloned repositories. The command also displays the latest commit checksum of each local and remote repository.

Here is an example of the output:

```bash
joshua@WOPR:~/gcm.py 
==================================================================================================================
   ______ _  __     ______            __         __  ___                                       
  / ____/(_)/ /_   / ____/____   ____/ /___     /  |/  /____ _ ____   ____ _ ____ _ ___   _____
 / / __ / // __/  / /    / __ \ / __  // _ \   / /|_/ // __ `// __ \ / __ `// __ `// _ \ / ___/
/ /_/ // // /_   / /___ / /_/ // /_/ //  __/  / /  / // /_/ // / / // /_/ // /_/ //  __// /    
\____//_/ \__/   \____/ \____/ \__,_/ \___/  /_/  /_/ \__,_//_/ /_/ \__,_/ \__, / \___//_/     
                                                                          /____/               
==================================================================================================================
/home/joshua/Code
    |
    |--norad-defunc
        |--WOPR | local: ae7705f6e3acb04ba1a1db876c07106dc3556fd8 | remote: None
        +--GitCodeManager | local: 790e229642ed86c3b7e5a8124cf23b0f22c13476 | remote: 790e229642ed86c3b7e5a8124cf23b0f22c13476
    |--JPaulMora
        +--Pyrit | local: f0f1913c645b445dd391fb047b812b5ba511782c | remote: f0f1913c645b445dd391fb047b812b5ba511782c
    |--aanarchyy
        +--bully | local: 3ab3bc830738f447dce112e8551e3ac8193bf521 | remote: 3ab3bc830738f447dce112e8551e3ac8193bf521
    |--aircrack-ng
        +--rtl8812au | local: d98018d038a5db96066e79f26ed4a72f2fe1774e | remote: d98018d038a5db96066e79f26ed4a72f2fe1774e
    |--UNC0V3R3D
        +--Flipper_Zero-BadUsb | local: 6e71fece6db47fe9191b357c8bbfe6af5e685e3f | remote: 6e71fece6db47fe9191b357c8bbfe6af5e685e3f
==================================================================================================================
What would you like to do?
1. Clone a repository
2. Quit the tool
> 1
Please enter the GitHub username:
> norad-defunc
Please enter the repository name:
> DB
Cloning into '/home/joshua/Code/norad-defunc/DB'...
remote: Enumerating objects: 61, done.
remote: Counting objects: 100% (61/61), done.
remote: Compressing objects: 100% (55/55), done.
remote: Total 61 (delta 0), reused 58 (delta 0), pack-reused 0
Receiving objects: 100% (61/61), 944.79 KiB | 3.90 MiB/s, done.
==================================================================================================================
```

## Credits

I'd like to thank my cat for being so cute and distracting me from my work. :)