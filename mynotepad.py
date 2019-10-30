#!/usr/bin/python3

import os
import sys
import time
from datetime import date
import argparse
import requests
import json
from git import Repo

git_access = <Your_Git_Access_Token>

class Notepad:
    # enums of file extensions
    python = '.py'
    java = '.java'
    text = '.txt'
    yaml = '.yaml'
    json = '.json'
    csharp = '.cs'
    c = '.c'
    header = '.h'
    html = '.html'
    css = '.css'
    cpp = '.cpp'
    r = '.r'
    shell = '.sh'

    # dictionary mapping to enums
    extensions = {
        'python' : python,
        'py' : python,
        '.py' : python,
        'text' : text,
        'txt' : text,
        '.txt' : text,
        'yaml' : yaml,
        '.yaml' : yaml,
        'java' : java,
        '.java' : java,
        'json' : json,
        '.json' : json,
        'csharp' : csharp,
        'cs' : csharp,
        '.cs' : csharp,
        'c' : c,
        '.c' : c,
        'header' : header,
        'h' : header,
        '.h' : header,
        'html' : html,
        '.html' : html,
        '.css' : css,
        'css' : css,
        '.cpp' : cpp,
        'cpp' : cpp,
        '.r' : r,
        'r' : r,
        'shell' : shell,
        '.sh' : shell,
        'sh' : shell
    }

    commentOpen = {
        '.py' : '"""',
        '.java' : '/*',
        '.cs' : '/*',
        '.c' : '/*',
        '.html' : '<!--',
        '.cpp' : '/*',
        '.css' : '/*'
    }

    commentClose = {
        '.py' : '"""',
        '.java' : '*/',
        '.cs' : '*/',
        '.c' : '*/',
        '.html' : '-->',
        '.cpp' : '*/',
        '.css' : '*/'
    }

    extension = ''
    folder = ''
    file = ''
    editor = ''
    path = os.getcwd()

    def pullExtension(self, file):
        parts = file[0].split('.')
        return parts[1]

    def __init__(self, editor, folder, file):
        self.editor = editor
        self.folder = folder
        self.file = file
        self.extension = self.extensions[self.pullExtension(file)]

    def makeAbsolute(self, folder):
        # creates absolute path from relative path
        if not os.path.isabs(folder):
            folder = os.path.join(self.path, folder)
        return folder

    def folderExists(self, folder):
        return os.path.isdir(self.makeAbsolute(folder))

    def fileExists(self, folder, file):
        if self.folderExists(folder):
            return os.path.isfile(file)
        else:
            return False

    def createPath(self, folder):
        # creates subfolders for path if they don't exist
        if not self.folderExists(folder):
            folder = self.makeAbsolute(folder)
            os.makedirs(folder)

    def createFiles(self, folder, multi):
        self.createPath(folder)
        os.chdir(self.makeAbsolute(folder))
        name = self.file[0]
        open(str(name), 'a').close()
        if multi is not None:
            for n in multi:
                open(str(n), 'a').close()

    def cloneRepo(self, url, folder):
        self.createPath(folder)
        os.chdir(self.makeAbsolute(folder))
        Repo.clone_from(url, os.getcwd())

    def createProject(self, repo, descript, priv, folder):
        # create repository and clone it to the specified folder
        url = "https://api.github.com/user/repos?access_token=" + git_access
        if priv == "T":
            priv = True
        if priv == "F":
            priv = False
        payload = {
            "name" : repo,
            "description" : descript,
            "private" : priv,
            "auto_init" : True
        }
        header = {'content-type': 'application/vnd.github.baptiste-preview+json', 'Accept-Charset': 'UTF-8'}
        payload = json.dumps(payload)
        r = requests.post(url, data=payload, headers=header)
        print(r.text)
        list = json.loads(r.text)
        clone_url = list['clone_url']
        print(clone_url)
        self.folder = os.path.join(folder,repo)
        folder = self.folder
        self.cloneRepo(clone_url, folder)
        print(self.folder)

    def openFiles(self, file, multi):
        # open files for name and all listed in multiple
        os.chdir(self.folder)
        os.system(self.editor+" "+file[0])
        if multi is not None:
            for n in multi:
                os.system(self.editor+" "+n)

    def comments(self, file, multi, user, folder):
        self.createPath(self.makeAbsolute(folder))
        today = date.today()
        comm = "Created by " + str(user[0]) + " on " + str(today)
        list = []
        list.extend(file)
        if multi is not None:
            list.extend(multi)
        os.chdir(self.makeAbsolute(folder))
        for n in list:
            if not self.fileExists(self.makeAbsolute(self.folder), n):
                with open(str(n),'w') as f:
                    if self.extension == self.extensions['java']:
                        # comment for java
                        f.write(str(self.commentOpen[self.extensions['java']]) + str(comm) + str(self.commentClose[self.extensions['java']]))
                    elif self.extension == self.extensions['python']:
                        # comment for python
                        f.write(str(self.commentOpen[self.extensions['python']]) + str(comm) + str(self.commentClose[self.extensions['python']]))
                    elif self.extension == self.extensions['c']:
                        # comment for c
                        f.write(str(self.commentOpen[self.extensions['c']]) + str(comm) + str(self.commentClose[self.extensions['c']]))
                    elif self.extension == self.extensions['header']:
                        # comment for header
                        f.write(str(self.commentOpen[self.extensions['header']]) + str(comm) + str(self.commentClose[self.extensions['header']]))
                    elif self.extension == self.extensions['cs']:
                        # comment for c#
                        f.write(str(self.commentOpen[self.extensions['cs']]) + str(comm) + str(self.commentClose[self.extensions['cs']]))
                    elif self.extension == self.extensions['cpp']:
                        # comment for c++
                        f.write(str(self.commentOpen[self.extensions['cpp']]) + str(comm) + str(self.commentClose[self.extensions['cpp']]))
                    elif self.extension == self.extensions['css']:
                        # comment for css
                        f.write(str(self.commentOpen[self.extensions['css']]) + str(comm) + str(self.commentClose[self.extensions['css']]))
                    elif self.extension == self.extensions['html']:
                        # comment for html
                        f.write(str(self.commentOpen[self.extensions['html']]) + str(comm) + str(self.commentClose[self.extensions['html']]))
            else:
                print('File already exists or does not accept comments. To prevent overriting comment not added')

parser = argparse.ArgumentParser(prog='MyNotePad', description='My notepad application to assist in programming in multiple languages')
parser.add_argument('--editor', '-e', nargs='?', default='atom', help='specify particular text editor to open note')
parser.add_argument('--comments', '-c', nargs=1, help='Adds a comment header with given user_name and todays date', metavar='user_name')
parser.add_argument('--project', '-p', nargs=3, help='creates git repository for project', metavar=('repo_name', 'description', 'private'))
parser.add_argument('name', nargs=1, help='name of file')
parser.add_argument('--dest', '-d', nargs='?', default='/Notes', help='location for file', metavar=('path'))
parser.add_argument('--multiple', '-m', nargs=argparse.REMAINDER, help='allows multiple files to be created/opened in a single command [name]')
args = vars(parser.parse_args())

if __name__ == '__main__':
    note = Notepad(args['editor'], args['dest'], args['name'])
    if args['project'] is not None:
        project = args['project']
        note.createProject(project[0], project[1], project[2], args['dest'])
    if args['comments'] is not None:
        note.comments(args['name'], args['multiple'], args['comments'], args['dest'])
    note.createFiles(args['dest'], args['multiple'])
    note.openFiles(args['name'], args['multiple'])
