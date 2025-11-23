#!/bin/bash
cd /Users/abhijeetthombare/ab_lib/code_test/python-90days/.abhi_commit.sh
date >> heartbeat.log
/usr/bin/git checkout dev
/usr/bin/git pull
/usr/bin/git add .
/usr/bin/git commit -m "Abhi-commit"
/usr/bin/git push origin dev
