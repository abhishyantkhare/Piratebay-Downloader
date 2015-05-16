git add -A 
read -p "Commit Message: " msg
git commit -m "$msg"
git pull
git push