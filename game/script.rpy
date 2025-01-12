# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.0

init python:   
    import functools 
    time = 0 #initialize time
    phase = 0 # initialize phase
    run = 1 # initialize run

    # initialize story vars
    loop2_investigate = False
    loop3_investigate = False
    smoke_break = False

    # initialize puzzle vars
    moonglitch1 = False
    moonglitch2 = False
    moonglitch3 = False
    moonglitch4 = False
    moonglitch5 = False

    # define function to increment time by 1 every line of dialogue + add flowers/triggers
    def inctime(event, interact=True, fnum=None, g1=False, g2=False,g3=False,g4=False,g5=False, checkskip=False,**kwargs):
        global time
        global flowers
        global moonglitches
        global solves
        if event == "begin":
            time +=1

            if fnum == 1:
                flowers.flower1 = True
            if fnum == 2:
                flowers.flower2 = True
            if fnum == 3:
                flowers.flower3 = True
            if fnum == 4:
                flowers.flower4 = True

            if puzzles.loop2 and not solves.loop2:
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

                    if g2==True and renpy.in_rollback() and moonglitches.glitch1: # if rolled back from 1 to 2
                        moonglitches.glitch2 = True
                    elif g2==True:
                        moonglitches.glitch2 = False
                        moonglitches.glitch1 = False

                    if g3==True and not renpy.in_rollback() and moonglitches.glitch2 and moonglitches.glitch1: # if did not rollback to 3
                        moonglitches.glitch3 = True
                    elif g3==True:
                        moonglitches.glitch3 = False
                        moonglitches.glitch2 = False
                        moonglitches.glitch1 = False

                    if g4==True and not renpy.in_rollback() and not renpy.is_skipping() and moonglitches.glitch3 and moonglitches.glitch2 and moonglitches.glitch1: # if did not rollback to 4:
                        moonglitches.glitch4 = True
                    elif g4==True:
                        moonglitches.glitch4 = False
                        moonglitches.glitch3 = False
                        moonglitches.glitch2 = False
                        moonglitches.glitch1 = False

                    if g5==True and moonglitches.glitch4 == True and moonglitches.glitch3 and moonglitches.glitch2 and moonglitches.glitch1:
                        moonglitches.glitch5 = True
                    elif g5==True:
                        moonglitches.glitch5 = False
                        moonglitches.glitch4 = False
                        moonglitches.glitch3 = False
                        moonglitches.glitch2 = False
                        moonglitches.glitch1 = False

                    if g1 == False and g2 == False and g3 == False and g4 == False and g5 == False:
                        moonglitches.glitch5 = False
                        moonglitches.glitch4 = False
                        moonglitches.glitch3 = False
                        moonglitches.glitch2 = False
                        moonglitches.glitch1 = False

                if moonglitches.glitch1 == True and moonglitches.glitch2 == True and moonglitches.glitch3 == True and moonglitches.glitch4 == True and moonglitches.glitch5 == True:
                    renpy.play("orex_sfx_sparkle.ogg") # solved!
                    solves.loop2 = True
        return

    # config.character_callback = inctime # set callback for character statements to increase time

    # create persistent flower class
    class Flowers(NoRollback):
        def __init__(self):
            self.flower1 = False
            self.flower2 = False
            self.flower3 = False
            self.flower4 = False

    # create persistent class for unlocked puzzles
    class Puzzles(NoRollback):
        def __init__(self):
            self.loop2 = False
            self.loop3 = False
            self.loop4 = False

    # create persistent class for solved puzzles
    class Solves(NoRollback):
        def __init__(self):
            self.loop2 = False
            self.loop3 = False
            self.loop4 = False

    # create persistent class for solved puzzles
    class MoonGlitches(NoRollback):
        def __init__(self):
            self.glitch1 = False
            self.glitch2 = False
            self.glitch3 = False
            self.glitch4 = False
            self.glitch5 = False

    # create persistent endings class
    class Endings(NoRollback):
        def __init__(self):
            self.ending1 = False
            self.ending2 = False
            self.ending3 = False

    def history_time_callback(x):
        global time
        global run
        x.what = "RUN " + str(run) + " | TIME " + str(time) + "\n" + x.what
    config.history_callbacks.append(history_time_callback)
    # Add new function to the history callbacks
    # if history_trigger_callback not in config.history_callbacks:
    #     config.history_callbacks.append(history_time_callback)

define narrator = Character(None,callback=None)
define delilah = Character("Delilah",callback=inctime)
define julian = Character("Julian",callback=inctime)
define cody = Character("Cody",callback=inctime)
define sandra = Character("Sandra",callback=inctime)

image moon_phase1 = ConditionSwitch(
    "run == 2 and moonglitch2 == True and not solves.loop2", "moon_phase1_glitch",
    "True", "images/props/moon_phase1.png")
image moon_phase2 = ConditionSwitch(
    "run == 2 and moonglitch1 == True and not solves.loop2", "moon_phase2_glitch",
    "run == 2 and moonglitch3 == True and not solves.loop2", "moon_phase2_glitch2",
    "True", "images/props/moon_phase2.png")
image moon_phase3 = ConditionSwitch(
    "run == 2 and moonglitch4 == True and not solves.loop2", "moon_phase3_glitch",
    "True", "images/props/moon_phase3.png")
image moon_phase4 = ConditionSwitch(
    "run == 2 and moonglitch5 == True and not solves.loop2", "moon_phase4_glitch",
    "True", "images/props/moon_phase4.png")
image moon_phase5 = "images/props/moon_phase5.png"

# 1 starts at phase 2 - rollback to 2 (1) - skip to 3 (2) - click right choice to 4 (3) - skip to 5 (4)
# note need to have "Unseen Text" or "After Choices" selected in prefs for skipping to work

image moon_phase1_glitch:
    Glitch("images/props/moon_phase1.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
    linear 1
    "images/props/moon_phase2.png"
image moon_phase2_glitch:
    Glitch("images/props/moon_phase2.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
    linear 1
    "images/props/moon_phase1.png"
image moon_phase2_glitch2:
    Glitch("images/props/moon_phase2.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
    linear 1
    "images/props/moon_phase3.png"
image moon_phase3_glitch:
    Glitch("images/props/moon_phase3.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
    linear 1
    "images/props/moon_phase4.png"
image moon_phase4_glitch:
    Glitch("images/props/moon_phase4.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
    linear 1
    "images/props/moon_phase5.png"

screen showtime: # screen for showing time
    # text "Time [time]" xpos 0.1 ypos 0.1
    if puzzles.loop2 and not solves.loop2:
        text "Glitches: 1-[moonglitches.glitch1] 2-[moonglitches.glitch2] 3-[moonglitches.glitch3] 4-[moonglitches.glitch4] 5-[moonglitches.glitch5]" xpos 0.1 ypos 0.1
    if solves.loop2:
        text "Glitches: solved!" xpos 0.1 ypos 0.1

screen eclipse: # screen for showing eclipse
    if phase == 0:
        add 'images/props/moon.png' xpos 0.6 ypos 0.05
    elif phase == 1:
        add 'moon_phase1' xpos 0.6 ypos 0.05
    elif phase == 2:
        add 'moon_phase2' xpos 0.6 ypos 0.05
    elif phase == 3:
        add "moon_phase3" xpos 0.6 ypos 0.05
    elif phase == 4:
        add "moon_phase4" xpos 0.6 ypos 0.05
    elif phase == 5:
        add "moon_phase5" xpos 0.6 ypos 0.05

screen showflower: # screen for showing flowers
    if flowers.flower1:
        text "Flower 1" xpos 0.1 ypos 0.15
    if flowers.flower2:
        text "Flower 2" xpos 0.1 ypos 0.2
    if flowers.flower3:
        text "Flower 3" xpos 0.1 ypos 0.25
    if flowers.flower4:
        text "Flower 4" xpos 0.1 ypos 0.3

screen flower1_pick:
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "images/props/flower.png"
        hover "images/props/flower_hover.png"
        action [SetVariable("flowers.flower1", 1), Hide("flower1_pick"), Return()]
screen flower2_pick:
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "images/props/flower.png"
        hover "images/props/flower_hover.png"
        action [SetVariable("flowers.flower2", 1), Hide("flower2_pick"), Return()]
screen flower_glitch:
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle Glitch("images/props/flower.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version

# define scene bgs
image bg scene1 = "#4680bd"
image bg scene2 = "#f0c047"
image bg scene3 = "#5646bd"
image bg black = "#000000"

# check run
label checkrun:
    if flowers.flower3:
        $ run = 4
    elif flowers.flower2:
        $ run = 3
    elif flowers.flower1:
        $ run = 2
    else:
        $ run = 1
    "RUN [run]"
    return

# The game starts here.

label start:

    $ config.rollback_enabled = False # disable rollback

    $ flowers = Flowers() # initialize flowers vars
    $ puzzles = Puzzles() # initialize unlocked puzzles vars
    $ solves = Solves() # initialize puzzle solves vars
    $ moonglitches = MoonGlitches() # initialize moon glitch vars
    $ endings = Endings() # initialize endings vars

    # initialize story vars
    $ loop2_investigate = False
    $ loop3_investigate = False
    $ smoke_break = False

    show screen showtime
    show screen showflower
    show screen eclipse

    scene bg scene1 with dissolve

    "BEGIN"

    $ renpy.block_rollback() # prevent rollback before this point
    $ config.rollback_enabled = True # re-enable rollback

    call checkrun from _call_checkrun

    jump mainrun

    # return
