﻿# This script runs before game start and defines the function to run the loop 2 puzzle

# Glitch puzzle loop 4

label init_loop4puzzle:

    init python:
        def check_loop4puzzle(g9,g10,checkskip):
            global moonglitches
            global puzzles
            global solves
            if g9==False and checkskip and not renpy.is_skipping():
                moonglitches.glitch9 = False
                moonglitches.glitch10 = False
            elif checkskip and renpy.is_skipping() and not renpy.get_screen("choice"):
                pass
            else:
                if g9==True and not renpy.is_skipping(): # initiate cycle from 1
                    moonglitches.glitch9 = True
                    moonglitches.glitch10 = False
                if g10==True and not renpy.in_rollback() and renpy.is_skipping() and moonglitches.glitch9: # if did not roll back or skip from 1 to 2
                    moonglitches.glitch10 = True
                elif g10==True:
                    moonglitches.glitch10 = True
                    moonglitches.glitch9 = False

                if g9 == False and g10 == False:
                    moonglitches.glitch10 = False
                    moonglitches.glitch9 = False

            if moonglitches.glitch9 == True and moonglitches.glitch10 == True:
                renpy.play("orex_sfx_sparkle.ogg") # solved!
                solves.loop4 = True

    return