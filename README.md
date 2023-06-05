# Code Club

This repo contains materials related to the State Library of Victoria's Code Club, an initiative intended to help improve data literacy across the organisation's staff. It is also intended to make coding less daunting, encourage experimentation and maybe also be fun.

## Create a directory for your code

It is useful to create a folder/directory for your code to live in. If you are using an SLV machine then (usually) your personal drive is mapped to the 'f' drive, therefore it's recommended to create your local code repo there.

You can use Git Bash to do so by following these steps:

- open Git Bash
- navigate to the 'f' drive: `cd /f/`
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

#### SQL client

## Course contents

Much of the content related to Python material has been adapted from sections of the excellent [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/2e/) by Al Sweigert.

### Python

1. Intro to Python basics
2. Flow control
3. Functions
4. Lists
5. Dictionaries and structuring data
6. Manipulating strings
7. Working with dates
8. Pattern matching and RegEx
9. Pandas
10. Jupyter notebooks

### SQL

1. SQL Basics
2. Database design
3. Working with SQL programmatically
