# The script of the game goes in this file.

# initial variable definitions and imports
init python:   
    import functools 
    gametime = 0 #initialize time
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

    # How to play text
init:
    default playtext = "HOW TO PLAY\nMake choices to control your future.\nRoll back with the Back button to return to the past.\nSkip across time with the Skip button.\nReview your History to remember what happened.\nNot everything follows the rules of time and space."

init:
    call init_screens # define UI screens
    call init_moonglitchimages # define moon glitch images
    call init_loop2puzzle # define function for loop 2 puzzle
    call init_classes # define persistent variable classes

init python:
    # define function to increment time by 1 every line of dialogue + add flowers/triggers
    def inctime(event, interact=True, fnum=None, g1=False, g2=False,g3=False,g4=False,g5=False, checkskip=False,**kwargs):
        global gametime
        global flowers
        # global moonglitches
        global puzzles
        global solves
        if event == "begin":
            gametime +=1

            if fnum == 1:
                flowers.flower1 = True
            if fnum == 2:
                flowers.flower2 = True
            if fnum == 3:
                flowers.flower3 = True
            if fnum == 4:
                flowers.flower4 = True

            if puzzles.loop2 and not solves.loop2:
                check_loop2puzzle(g1,g2,g3,g4,g5,checkskip) # defined in init_loop2puzzle
        return

    # config.character_callback = inctime # set callback for character statements to increase time

    def history_time_callback(x):
        global gametime
        global run
        x.what = "RUN " + str(run) + " | TIME " + str(gametime) + "\n" + x.what
    config.history_callbacks.append(history_time_callback)
    # Add new function to the history callbacks
    # if history_trigger_callback not in config.history_callbacks:
    #     config.history_callbacks.append(history_time_callback)

# Declare characters used by this game.
define narrator = Character(None,callback=None,what_style="centered_text", window_style="centered_window")
define delilah = Character("Delilah",image="delilah",callback=inctime)
define delilah_run2 = Character("Delilah",image="delilah",what_prefix='{color=#f00}', what_suffix='{/color}',callback=inctime)
define delilah_thoughts = Character("Delilah",image="delilah",what_prefix='(', what_suffix=')', what_italic=True,callback=inctime)
define delilah_thoughts_run2 = Character("Delilah",image="delilah",what_prefix='{color=#f00}(', what_suffix='){/color}', what_italic=True,callback=inctime)
define julian = Character("Julian",image="julian",callback=inctime)
define julian_run2 = Character("Julian",image="julian",what_prefix='{color=#f00}', what_suffix='{/color}',callback=inctime)
define boy = Character("???",image="julian",callback=inctime)
define boy_run2 = Character("???",image="julian",what_prefix='{color=#f00}', what_suffix='{/color}',callback=inctime)
define cody = Character("Cody",image="cody",callback=inctime)
define cody_run2 = Character("Cody",image="cody",what_prefix='{color=#f00}', what_suffix='{/color}',callback=inctime)
define sandra = Character("Sandra",image="sandra",callback=inctime)
define sandra_run2 = Character("Sandra",image="sandra",what_prefix='{color=#f00}', what_suffix='{/color}',callback=inctime)

# define animated fade sprite for Julian
image julian fade:
    "images/chars/julian neutral.png"
    alpha 0.0
    linear 0.05 alpha 0.03
    linear 0.05 alpha 0.0
    0.25
    linear 0.05 alpha 0.1
    linear 0.05 alpha 0.0
    0.25
    linear 0.05 alpha 0.06
    linear 0.05 alpha 0.0
    0.5
    repeat

# define scene bgs (placeholder)
image bg scene1 = "#4680bd"
image bg scene2 = "#f0c047"
image bg scene3 = "#5646bd"
image bg black = "#000000"

image rearview = "images/props/rearview.png"
image reflection = "images/props/rearview_reflection.png"
image windshield = "images/props/windshield.png"

# define flower images
image flower_run2:
    "images/props/flower.png"
    zoom 0.6
    linear 0.05 alpha 0.7
    linear 0.05 alpha 1
    0.25
    linear 0.05 alpha 0.4
    linear 0.05 alpha 1
    0.25
    linear 0.05 alpha 0.8
    linear 0.05 alpha 1
    0.5
    repeat
image flower_run3:
    "images/props/flower.png"
    zoom 0.6
    linear 0.05 alpha 0.8
    linear 0.05 alpha 1
    0.5
    linear 0.05 alpha 0.7
    linear 0.05 alpha 1
    0.25
    linear 0.05 alpha 0.4
    linear 0.05 alpha 1
    0.25
    repeat
image flower_run4:
    "images/props/flower.png"
    zoom 0.6
    linear 0.05 alpha 0.4
    linear 0.05 alpha 1
    0.25
    linear 0.05 alpha 0.8
    linear 0.05 alpha 1
    0.5
    linear 0.05 alpha 0.7
    linear 0.05 alpha 1
    0.25
    repeat

# define custom positions for sprites
transform center_left:
    xalign 0.3 yalign 1.0
transform center_right:
    xalign 0.7 yalign 1.0

# define screen layers
define config.layers = [ 'master', 'background','background_overlay','characters','transient', 'screens', 'overlay', 'interface' ]
$ config.tag_layer['bg'] = 'background'

# check run number at beginning to progress runs
label checkrun:
    if flowers.flower3:
        $ run = 4
        show flower_run2:
            xalign 0.4
            yalign 0.6
        show flower_run3:
            xalign 0.5
            yalign 0.6
        show flower_run4:
            xalign 0.6
            yalign 0.6
    elif flowers.flower2:
        $ run = 3
        show flower_run2:
            xalign 0.45
            yalign 0.6
        show flower_run3:
            xalign 0.55
            yalign 0.6
    elif flowers.flower1:
        $ run = 2
        show flower_run2:
            xalign 0.5
            yalign 0.6
    else:
        $ run = 1
    # if run >= 2:
    #     show reflection:
    #         xalign 0.5
    #         yalign 0.05
    #     with { "master" : Dissolve(1.0) }
    "7 PM"
    hide flower_run2
    hide flower_run3
    hide flower_run4
    # "RUN [run]"
    return

# increase eclipse phase on screen
label incphase:
    $ phase += 1
    show screen eclipse onlayer background_overlay with Dissolve(2.0)
    pause 1.0
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

    show screen howtoplay
    $ renpy.pause()
    hide screen howtoplay

    # "BEGIN"
    pause 2.0

    $ renpy.block_rollback() # prevent rollback before this point
    $ config.rollback_enabled = True # re-enable rollback

    scene bg black with dissolve

    show screen moonglitchscreen onlayer interface
    show screen flowerscreen onlayer interface

    # show rearview:
    #     xalign 0.5
    #     yalign 0.05

    with { "master" : Dissolve(1.0) }
    call checkrun from _call_checkrun

    jump mainrun

    # return
