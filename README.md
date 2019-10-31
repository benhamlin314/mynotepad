# mynotepad
Simple notepad command to automate creation of git repository, files, and basic file header comment.

Install requirements
-----------------------
use pip3 install -r requirements.txt

Setup
-----------------------
In your github account, create an access_token from the following
- go to settings
- click "Developer settings"
- click "Personal access tokens"
- click "Generate new token"
- name the token mynotepad to ensure
- ensure "repo" is checked
- click "Generate token"
- copy the only revealed token **NOTE THAT YOU CAN NOT FIND THIS TOKEN AGAIN WHEN YOU NAVIGATE AWAY**
- replace <Your_Git_Access_Token> with your token

Edit the batch or shell script:
- edit the path to match your path to mynotepad.py
- add the path to the shell or batch script to your source
OR
- add the function to your source directly
