# GIT

- Distributed version control
- This means that there is a backup of your work, and a record of changes to your work, stored in the cloud
- This means you are protected from loss of data if you workstation is damaged
- The record of changes means that you can also roll back to a previous, stable version of your work if a change has caused you trouble
 

## Getting set up

1. Generate ssh key on your localhost
2. Once generated, collect .pub file, copy public key from localhost
3. Go to github account, paste into ```deploy key``` in settings
4. Should then have linked accounts, and be able to send files to github easily.

## Setting Up A New Repository

- On your github, click "New Repository"
- Can now choose whether to add soem basic files on github, Generally, preferable to do this yourself.
  
- Throughout this, remember to use ``git status`` to check which files are getting committed, and which files have been edited.
- In the directory where you have your initial files, use either gitbash or your IDE terminal to type
```git init```
  
- Now, use ```git add``` to "stage" the files you want in your first commit.
- You're now ready for your first commit. Use the command ```git commit -m "first commit"```. If you prefer, you can of course change the message.
- set the branch of your repo, using ```git branch -M main```
- Next, add the remote repository, using ```git remote add origin https://github.com/[username]/[reponame].git```. The correct url is usually shown by github when you set up a new repository.
- Finally, you push your committed files to the remote repo, using ```git push -u origin main```