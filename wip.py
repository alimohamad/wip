#!/usr/bin/env python

import os
import emoji

print("WORK (adding)")
print(emoji.emojize("""
      :stuck_out_tongue_winking_eye:
  :punch: /||\_ 
     - -
   _/   \_ 
   """, use_aliases=True))
os.system("git add .")

print("IN (committing)")
print(emoji.emojize("""
    :wave: 
     \ :flushed:
       || \_
      - -
    _/   \_ 
    """, use_aliases=True))
os.system('git commit  -m "wip" ')

print("PROGRESS (pushing)")
print(emoji.emojize("""
            :wave:       
        :weary:  /
     _/ ||
        - -
      _/   \_
      """,use_aliases=True))
os.system("git push origin master")