# This script runs before game start and defines the function to run the loop 2 puzzle

# Glitch puzzle loop 3

label init_loop3puzzle:

    init python:
        def check_loop3_1puzzle(g3,g4,checkskip):
            global moonglitches
            global puzzles
            global solves
            if g3==False and checkskip and not renpy.is_skipping():
                moonglitches.glitch3 = False
                moonglitches.glitch4 = False
            elif checkskip and renpy.is_skipping() and not renpy.get_screen("choice"):
                pass
            else:
                if g3==True and not renpy.is_skipping(): # initiate cycle from 1
                    moonglitches.glitch3 = True
                    moonglitches.glitch4 = False

                if g4==True and not renpy.in_rollback() and renpy.is_skipping() and moonglitches.glitch3: # if did not roll back or skip from 1 to 2
                    moonglitches.glitch4 = True
                elif g4==True:
                    moonglitches.glitch4 = True
                    moonglitches.glitch3 = False

                if g3 == False and g4 == False:
                    moonglitches.glitch4 = False
                    moonglitches.glitch3 = False

            if moonglitches.glitch3 == True and moonglitches.glitch4 == True:
                renpy.play("orex_sfx_sparkle.ogg") # solved!
                solves.loop3_1 = True
                hintlist.list.append("{b}Sealed glitch " + str(sum([solves.loop2,solves.loop3_1,solves.loop3_2,solves.loop3_3,solves.loop4])) + " of 5{/b}\n")
                hints.seen_hint = False
            elif g4 == True and renpy.is_skipping() and hints.hint2 and hints.hint3 and not hints.hint9:
                renpy.play("orex_sfx_sparkle.ogg")
                hintlist.list.append(hint_9)
                hints.hint9 = True
                hints.seen_hint = False

        def check_loop3_2puzzle(g5,g6,checkskip):
            global moonglitches
            global puzzles
            global solves
            if g5==False and checkskip and not renpy.is_skipping():
                moonglitches.glitch5 = False
                moonglitches.glitch6 = False
            elif checkskip and renpy.is_skipping() and not renpy.get_screen("choice"):
                pass
            else:
                if g5==True and not renpy.is_skipping(): # initiate cycle from 1
                    moonglitches.glitch5 = True
                    moonglitches.glitch6 = False

                if g6==True and not renpy.in_rollback() and renpy.is_skipping() and moonglitches.glitch5: # if did not roll back or skip from 1 to 2
                    moonglitches.glitch6 = True
                elif g6==True:
                    moonglitches.glitch6 = True
                    moonglitches.glitch5 = False

                if g5 == False and g6 == False:
                    moonglitches.glitch6 = False
                    moonglitches.glitch5 = False

            if moonglitches.glitch5 == True and moonglitches.glitch6 == True:
                renpy.play("orex_sfx_sparkle.ogg") # solved!
                solves.loop3_2 = True
                hintlist.list.append("{b}Sealed glitch " + str(sum([solves.loop2,solves.loop3_1,solves.loop3_2,solves.loop3_3,solves.loop4])) + " of 5{/b}\n")
                hints.seen_hint = False
            elif g6 == True and renpy.is_skipping() and hints.hint2 and hints.hint3 and not hints.hint9:
                renpy.play("orex_sfx_sparkle.ogg")
                hintlist.list.append(hint_9)
                hints.hint9 = True
                hints.seen_hint = False

        def check_loop3_3puzzle(g7,g8,checkskip):
            global moonglitches
            global puzzles
            global solves
            global flowers
            if g7==False and checkskip and not renpy.is_skipping():
                moonglitches.glitch7 = False
                moonglitches.glitch8 = False
            elif checkskip and renpy.is_skipping() and not renpy.get_screen("choice"):
                pass
            else:
                if g7==True and not renpy.is_skipping(): # initiate cycle from 1
                    moonglitches.glitch7 = True
                    moonglitches.glitch8 = False

                if g8==True and not renpy.in_rollback() and renpy.is_skipping() and moonglitches.glitch7: # if did not roll back or skip from 1 to 2
                    moonglitches.glitch8 = True
                elif g8==True:
                    moonglitches.glitch8 = True
                    moonglitches.glitch7 = False

                if g7 == False and g8 == False:
                    moonglitches.glitch8 = False
                    moonglitches.glitch7 = False

            if moonglitches.glitch7 == True and moonglitches.glitch8 == True and flowers.flower3:
                renpy.play("orex_sfx_sparkle.ogg") # solved!
                solves.loop3_3 = True
                hintlist.list.append("{b}Sealed glitch " + str(sum([solves.loop2,solves.loop3_1,solves.loop3_2,solves.loop3_3,solves.loop4])) + " of 5{/b}\n")
                hints.seen_hint = False
            elif g8 == True and renpy.is_skipping() and hints.hint2 and hints.hint3 and not hints.hint9:
                renpy.play("orex_sfx_sparkle.ogg")
                hintlist.list.append(hint_9)
                hints.hint9 = True
                hints.seen_hint = False

    return