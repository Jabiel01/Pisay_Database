1) Create a project folder and using Terminal/Command Prompt change to the project folder directory
	Terminal commands
		cd <insert directory name> -changes directory to desired folder name
		cd .. -exits current directory
		ls - list the folders and files 
		ls -ai -lists all files and folders including hidden folders

2) Setting up your own Virtual Environment
	Terminal Commands
		virtualenv <environment_name> - creates a virtualenv with the desired folder name
		source <environment_name>/bin/activate - activates virtual environment
		deactivate - deactivates and exits the virtual environment

4) Git Commands
	git clone <url> - Clones repository from url
	git status - Checks status
	git add <file> - Adds untracked files to be tracked by git
	git add . - Adds all untracked files to be commited
	git commit <file> - Commits all tracked/added files
	git log - Shows logs of commitments
	git log --oneline --graph --decorate --abbre
	git branch - Check current branch the user is on with an *
	git branch <branchname> - Creates new branch
	git checkout <branchname> - switches to branch with branchname
	git checkout -b <branchname> shourtcut to creating new branch and switching to new branch
	git merge <branchname> - Merges branch name to current branch
		* When merging, conflicts may arise. Don't be scared. Just keep coding.
	git rebase <source branch> - Rebasing is the rewinding of existing commits
		* Rebasing allows you to rewind individual commits created 
			Merging - is squashing two different commit statements into one commit statement
			Rebasing - is acknowledging the different commit statements as individual identites adding them one after
						the other allowing the user to revert to individual commitments
	git tag <tagname> - bookmarks current commit usually for Deployment Version 1, Version 2, etc.



Legend:
	* - notes


** Random codes you might like to use

	touch <file> - creates a file in current directory
		e.g. touch txt.file - Adds txt.file to directory
