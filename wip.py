#!/usr/bin/env python

import os
import sys

print("Test")
os.system("git add .")

print("Commit")
os.system('git commit  -m "wip" ')

print("Push")
os.system("git push origin master")