#!/usr/bin/env python

import os

print("WORK (adding)")
print(""""
     /||\_ 
     - -
   _/   \_ """)
os.system("git add .")

print("IN (committing)")
print("""
      
     \ 
       || \_
      - -
    _/   \_ """)
os.system('git commit  -m "wip" ')

print("PROGRESS (pushing)")
print("""
           
          /
     _/ ||
        - -
      _/   \_")
os.system("git push origin master""")