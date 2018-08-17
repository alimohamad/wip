#!/usr/bin/env python

import os
import emoji

print("WORK (adding)")
print(emoji.emojize(""""
      :stuck_out_tongue_closed_eyes:
     /||\_ 
     - -
   _/   \_ """))
os.system("git add .")

print("IN (committing)")
print("""
    :wave:  
     \ :flushed:
       || \_
      - -
    _/   \_ """)
os.system('git commit  -m "wip" ')

print("PROGRESS (pushing)")
print("""
            :wave:       
        :weary:  /
     _/ ||
        - -
      _/   \_""")
os.system("git push origin master")