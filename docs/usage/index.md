---
layout: default
title: 'Usage'
---
## Usage
`mynotepad -e (editor) -c (username) -p (repo_name, description, private{T/F}) fileName -d (destination) -m (list filenames)`

### editor
Option to specify editor to open the file with. Default is Atom.

Editor options supported:
- atom
- sublime
- gedit
- vim
- emacs
- nano
- visual studio code
- notepad++

### comments
Option to add a header comment with "Created by username on [date]."

### project
Option to create a repository on the account with the given <Your_Git_Access_Token> on setup.

Must specify:
- repository name
- repository description
- whether the repository is private (T/F)

### name
Required argument of file name to open.

### destination
Option to specify location the files will be created

### multiple
Option to specify more files to be created and opened

Files should be listed with a space in between
