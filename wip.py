#!/usr/bin/env python

import os

print("WORK (adding)")
print("""
      \U+1F61C:
    \U+1F44A /||\_ 
     - -
   _/   \_ """)
os.system("git add .")

print("IN (committing)")
print("""
    \U+1F44B  
     \ \U+1F633
       || \_
      - -
    _/   \_ """)
os.system('git commit  -m "wip" ')

print("PROGRESS (pushing)")
print("""
            \U+1F44B       
        \U+1F629  /
     _/ ||
        - -
      _/   \_""")
os.system("git push origin master")