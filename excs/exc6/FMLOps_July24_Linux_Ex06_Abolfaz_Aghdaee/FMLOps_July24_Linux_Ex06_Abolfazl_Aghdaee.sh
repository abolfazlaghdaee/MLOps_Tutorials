#!/bin/bash


#scenario 1


mkdir first
cd first
git init
git config --global user.name "abolfazlaghdaee"
git config --global user.email "abolfazlaghdaee2001@gmail.com"

echo "HI" > Readme.md
git add Readme.md
git commit -m "Initial commit"


###################################
#Scenario2 

git branch feature-branch
git checkout feature-branch

echo "Hello" > feature.txt
git add feature.txt
git commit -m "Add txt file"



#################################
# Scenario3

git blame  app.py
git show  0164f747 


#################################
# Scenario 4
git clean -n
git clean -f





###############################
# Scenario 5
ssh-keygen

eval "$(ssh-agent -s)"

ssh -T git@github.com


###############################
# Scenario6


#git clone git@github.com:abolfazlaghdaee/for_exc6.git

git branch feature-branch

# add some changing  in feature branch and add and commit 


git push origin feature-branch


###############################
# Scenario7

git checkout  main 
git merge feature-branch

git add . 
git commit -m 'add files from  feater'
git push origin main















