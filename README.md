# behave_tests
##1. Install relate python package with pip
pip install -r requirements.txt

##2. Execute test cases
behave
or
behave --tags="regression"

##3. Generate reports

modify behave.ini

setup allure:
  for macos: 
    
      brew install allure
        
  for others, please refer to: https://docs.qameta.io/allure/

install python package:

    pip install allure-behave

generate allure format output:

    behave -f allure_behave.formatter:AllureFormatter -o reports/ ./features
 
show test report:

    allure serve reports/
    
##4. Bamboo

(1) Go to https://www.atlassian.com/software/bamboo/ to download atlassian-bamboo-7.0.2.tar.gz
(The latest version should be OK), then uncompress.

(2) Make sure jdk1.8 is installed on your system

(3) Go to https://confluence.atlassian.com/bamboo/getting-started-with-bamboo-289277283.html to
choice guidance base on your operating system.

(4) start bamboo(Take macos as an example):
    
    a) In the command line, change the directory to <Bamboo installation directory> and run 
    the commands to start Bamboo:
        $ cd <Bamboo installation directory>
        $ ./bin/start-bamboo.sh
    
    b) After successfully starting Bamboo, you will find it online at: 
        http://localhost:8085/
        
    Details refer to: https://confluence.atlassian.com/bamboo/installing-bamboo-on-mac-os-x-289276789.html

(5) Create a project by menu "Create/Create project"

(6) Config a new repository by menu "Specs/Setup Specs repository"
   user credential of source codes version control tool should be filled

(7) Create a plan by menu "Create plan"
   Choose to run this job on "agent environment" or "Docker container"
   Create tasks or configure default tasks
   Define your task, for example, you need to define the command line if your task type is "command"

(8) Run test plan

(9) The view of result and logs

(10) Create a deployment project if necessary
   Configure the tasks of deployment.
   Link to existing plan or a new plan.

##5. Git
(1) Git download:
    Please verify if the git has been installed by command "git --version".
    Otherwise, you can download the install file from:
        https://git-scm.com/downloads
    
(2) set git name and email:
    git config --global user.name 'your github username'
    git config --global user.email 'your github email'
    verify your name and email with below command:
        git config user.name
        git config user.email

(3) Generate SSH key
   ssh-keygen -t rsa -C 'your github email'

(4) Go to github and configure public key
  Go to users/yourname/.ssh on you computer, and copy the public key content.
  Go to github, and choice "Settings/SSH and GPG Keys/New SSH Key", paste your public key into it.
  
(5) list branches:
    git branch
    The branch with asterisk is your current branch
(6) switch branch
    git checkout master
(7) git

git fetch --all
git reset --hard origin/master

git checkout nfv20
git push origin nfv20:nfv20 --force

git stash
git pull
git stash pop


git reset test.py
git checkout test.py

git push origin :feature
git stash list

把本地的dev合并到master
git checkout master
git merge dev

git branch -r -d origin/jim
git push origin :jim

git rm -r --cached .
git add .
git commit -m "update .gitignore"

git branch --set-upstream-to=origin/nfvcli 

cancel the merging:
git reset --hard HEAD (or sha_1)  




