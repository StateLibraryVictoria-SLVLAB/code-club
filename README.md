# Code Club

This repo contains materials related to the State Library of Victoria's Code Club, an initiative intended to help improve data literacy across the organisation's staff. It is also intended to make coding less daunting, encourage experimentation and maybe also be fun.

## Create a directory for your code

It is useful to create a folder/directory for your code to live in. If you are using an SLV machine then (usually) your personal drive is mapped to the `f:` drive, therefore it's recommended to create your local code repo there.

You can use Git Bash to do so by following these steps:

- open Git Bash
- navigate to the f drive: `cd /f/`
- create a new directory with a meaningful name e.g. 'development': `mkdir development`
- navigate into the newly created folder: `cd development`

## Installation and setup guide

This guide assumes that the user already has a Git Bash, Terminal, PowerShell or something that allows them to run commands installed on the computer they're using.

### Git

[Git for Windows download](https://git-scm.com/download/win)

Test it's installed correctly by opening Git Bash or PowerShell and running `git --version` from it. if git has installed correctly it should return something like `git version 2.38.1.windows.1` (version number will likely vary)

#### GitHub

[Sign up for an account](https://github.com/signup)

Once you have an account you need to setup credentials on your PC to authorise interaction with code repositories hosted on GitHub. There are several different authentication methods, including the use of SSH keys which this guide recommends. To set-up SSH authentication for GitHub follow this guide: [https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

To check that you have set up authentication correctly, open Git Bash (or equivalent) and navigate to the directory you'd like to save your code to and enter the following command: `git@github.com:StateLibraryVictoria/code-club.git` If the command has run successfully you should be able to navigate into the newly created directory by running `cd code-club`

### Python (3.9 or higher)

[Official Python site download center](https://www.python.org/downloads/)

Windows makes many different versions of Python available through the 'Microsoft Store' e.g. [Python 3.9](https://www.microsoft.com/store/productId/9P7QFQMJRFP7). The benefit of using the official store is that it should handle the config for you and allow you to use Python straight away!

#### Python IDE

If you've already successfully completed the steps outlined in the guide above, and you have a text editor, then you already have everything you need to create and run Python scripts. However, it is recommended that you install an IDE (Integrated Development Environment) because they tend to have lots of features that make writing scripts easier. There are a plethora of IDEs available and if you get really into writing code, it's probably worth road-testing a few and seeing which one(s) you like best. However, give that this course covers both Python and SQL (and maybe more!) it's recommended that you use an IDE that works well with both e.g. [VS Code](https://apps.microsoft.com/store/detail/XP9KHM4BK9FZ7Q)
<!-- 
#### SQL client

There are a range of SQL clients, many of which would be suitable for following the contents of this course. [Azure Data Studio]() (as the name suggests) integrates very well with -->