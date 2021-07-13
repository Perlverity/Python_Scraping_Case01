import os
import git

COMMIT_LOG = 'First Commit!'

# Pushしたいリポジトリに移動
os.chdir(r'/Users/administrator/Google Drive/16 Python/01 Python Code/Python/94_Python_Scraping_Case01')
repo = git.Repo()

# git add
repo.git.add('.')

# git commit
repo.git.commit('.', '-m', COMMIT_LOG)

# git push
repo.git.push('origin', 'main')
