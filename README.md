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

Git Code Manager is a command-line tool for managing cloned GitHub repositories in a clean fashion on your local file system under the `~/Code/` folder. It helps with keeping your locally cloned repositories always organized and up to date. Current features include cloning repositories from GitHub, displaying the directory tree of cloned repositories along with their latest local and remote commit checksum.

All reposotories are stored in the following directory structure:

```bash
~/Code
    |
    |--username
        +--repository
```

More features are coming soon like auto comparison of local and remote repositories, auto update of local repositories, and more.

## Usage

### Cloning a repository with "clone"

The clone command allows users to clone a GitHub repository and store it in the proper directory structure in the local file system. The command takes two parameters: username and repository.

```bash
$ gcm clone username repository
```

### Listing cloned repositories with "list"

The list command allows users to display the directory tree of cloned repositories. The command doesn't take any parameters. It also displays the latest commit checksum of each local and remote repository.

```bash
$ gcm list
```

Output:

```bash
~/Code
    |
    |--floriangrousset
        |--TestJetBrainFleet | local: None | remote: None
        +--GitCodeManager | local: 50cc...39da | remote: None
    |--JPaulMora
        +--Pyrit | local: f0f1...782c | remote: f0f1...782c
    |--aanarchyy
        +--bully | local: c830...193b | remote: 3ab3...f521
    |--aircrack-ng
        +--rtl8812au | local: d980...774e | remote: d980...774e
    |--UNC0V3R3D
        +--Flipper_Zero-BadUsb | local: 6e71...5e3f | remote: fece...5e68
```

## Credits

I'd like to thank my cat for being so cute and distracting me from my work. :)