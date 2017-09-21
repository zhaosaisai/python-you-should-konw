#/usr/bin/env bash

# push ro origin 
git add . && git commit -m "$1" && git push origin master >> git.log 2>&1 &&  exit 1  ||  exit 0 
