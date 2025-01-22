# This script runs before game start and defines the function to run the loop 2 puzzle

# Moon puzzle loop 2
# 1 starts at phase 2 - rollback to 2 (1) - skip to 3 (2) - click right choice to 4 (3) - skip to 5 (4)
# note need to have "Unseen Text" or "After Choices" selected in prefs for skipping to work

label init_loop2puzzle:

    init python:
        def check_loop2puzzle(g1,g2,g3,g4,g5,checkskip):
            global moonglitches
            global puzzles
            global solves
            if g1==False and checkskip and not renpy.is_skipping():
                moonglitches.glitch1 = False
                moonglitches.glitch2 = False
                moonglitches.glitch3 = False
                moonglitches.glitch4 = False
                moonglitches.glitch5 = False
            elif checkskip and renpy.is_skipping() and not renpy.get_screen("choice"):
                pass
            else:
                if g1==True: # initiate cycle from 1
                    moonglitches.glitch1 = True
                    moonglitches.glitch2 = False
                    moonglitches.glitch3 = False
                    moonglitches.glitch4 = False
                    moonglitches.glitch5 = False

                # if g2==True and not renpy.in_rollback() and not renpy.is_skipping() and moonglitches.glitch1: # if did not roll back or skip from 1 to 2
                if g2==True and not renpy.in_rollback() and renpy.is_skipping() and moonglitches.glitch1: # if did not roll back or skip from 1 to 2
                    moonglitches.glitch2 = True
                elif g2==True:
                    # moonglitches.glitch2 = False
                    moonglitches.glitch2 = True
                    moonglitches.glitch1 = False

                # if g3==True and not renpy.in_rollback() and moonglitches.glitch2 and moonglitches.glitch1: # if did not rollback to 3
                #     moonglitches.glitch3 = True
                # elif g3==True and renpy.in_rollback():
                #     moonglitches.glitch4 = False
                #     moonglitches.glitch3 = True
                #     moonglitches.glitch2 = False
                #     moonglitches.glitch1 = False
                # elif g3==True:
                #     # moonglitches.glitch3 = False
                #     moonglitches.glitch3 = True
                #     moonglitches.glitch2 = False
                #     moonglitches.glitch1 = False

                # if g4==True and not renpy.in_rollback() and not renpy.is_skipping() and moonglitches.glitch3 and moonglitches.glitch2 and moonglitches.glitch1: # if did not rollback to 4:
                #     moonglitches.glitch4 = True
                # elif g4==True:
                #     # moonglitches.glitch4 = False
                #     moonglitches.glitch4 = True
                #     moonglitches.glitch3 = False
                #     moonglitches.glitch2 = False
                #     moonglitches.glitch1 = False

                # if g5==True and moonglitches.glitch4 == True and moonglitches.glitch3 and moonglitches.glitch2 and moonglitches.glitch1:
                #     moonglitches.glitch5 = True
                # elif g5==True:
                #     # moonglitches.glitch5 = False
                #     moonglitches.glitch5 = True
                #     moonglitches.glitch4 = False
                #     moonglitches.glitch3 = False
                #     moonglitches.glitch2 = False
                #     moonglitches.glitch1 = False

                if g1 == False and g2 == False and g3 == False and g4 == False and g5 == False:
                    moonglitches.glitch5 = False
                    moonglitches.glitch4 = False
                    moonglitches.glitch3 = False
                    moonglitches.glitch2 = False
                    moonglitches.glitch1 = False

            # if moonglitches.glitch1 == True and moonglitches.glitch2 == True and moonglitches.glitch3 == True and moonglitches.glitch4 == True and moonglitches.glitch5 == True:
            if moonglitches.glitch1 == True and moonglitches.glitch2 == True:
                renpy.play("orex_sfx_sparkle.ogg") # solved!
                solves.loop2 = True

    return