#!/usr/bin/env python

import os
import emoji

print("WORK (adding)")
print(emoji.emojize("""
      \U+1F61C:
    \U+1F44A /||\_ 
     - -
   _/   \_ """, use_aliases=True))
os.system("git add .")

print("IN (committing)")
print(emoji.emojize("""
    \U+1F44B  
     \ \U+1F633
       || \_
      - -
    _/   \_ """, use_aliases=True))
os.system('git commit  -m "wip" ')

print("PROGRESS (pushing)")
print(emoji.emojize("""
            \U+1F44B       
        \U+1F629  /
     _/ ||
        - -
      _/   \_""", use_aliases=True))
os.system("git push origin master")