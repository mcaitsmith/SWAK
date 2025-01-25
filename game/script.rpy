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
    skip_puzzle2 = False
    skip_puzzle3 = False
    skip_puzzle4 = False

    # How to play text
init:
    default playtext = "HOW TO PLAY\nMake choices to control your future.\nRoll back with the Back button to return to the past.\nSkip across time with the Skip button.\nReview your History to remember what happened.\nNot everything follows the rules of time and space."

init:
    call init_screens from _call_init_screens # define UI screens
    call init_moonglitchimages from _call_init_moonglitchimages # define moon glitch images
    call init_loop2puzzle from _call_init_loop2puzzle # define function for loop 2 puzzle
    call init_classes from _call_init_classes # define persistent variable classes

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
        # x.what = "RUN " + str(run) + " | TIME " + str(gametime) + "\n" + x.what
        x.what = "RUN " + str(run) + "\n" + x.what
    config.history_callbacks.append(history_time_callback)
    # Add new function to the history callbacks
    # if history_trigger_callback not in config.history_callbacks:
    #     config.history_callbacks.append(history_time_callback)

# Declare characters used by this game.
define narrator = Character(None,callback=None,what_style="centered_text", window_style="centered_window",what_outlines=[(2,"#000000",0,0)])
define time_centered = Character(None,callback=None,what_style="centered_text", window_style="centered_window",what_font="retro_party.ttf",what_size = 100, what_outlines=[(2,"#000000",0,0)])
define delilah = Character("Delilah",image="delilah",color="#EB28D2",callback=inctime)
define delilah_run2 = Character("Delilah",image="delilah",color="#EB28D2",what_prefix='{color=#f00}', what_suffix='{/color}',callback=inctime)
define delilah_run3 = Character("Delilah",image="delilah",color="#EB28D2",what_prefix='{color=#0f0}', what_suffix='{/color}',callback=inctime)
define delilah_run4 = Character("Delilah",image="delilah",color="#EB28D2",what_prefix='{color=#0ff}', what_suffix='{/color}',callback=inctime)
define delilah_thoughts = Character("Delilah",image="delilah",color="#EB28D2",what_prefix='(', what_suffix=')', what_italic=True,callback=inctime)
define delilah_thoughts_run2 = Character("Delilah",image="delilah",color="#EB28D2",what_prefix='{color=#f00}(', what_suffix='){/color}', what_italic=True,callback=inctime)
define delilah_thoughts_run3 = Character("Delilah",image="delilah",color="#EB28D2",what_prefix='{color=#0f0}(', what_suffix='){/color}', what_italic=True,callback=inctime)
define delilah_thoughts_run4 = Character("Delilah",image="delilah",color="#EB28D2",what_prefix='{color=#0ff}(', what_suffix='){/color}', what_italic=True,callback=inctime)
define julian = Character("Julian",image="julian",color="#71A4B0",callback=inctime)
define julian_run2 = Character("Julian",image="julian",color="#71A4B0",what_prefix='{color=#f00}', what_suffix='{/color}',callback=inctime)
define julian_run3 = Character("Julian",image="julian",color="#71A4B0",what_prefix='{color=#0f0}', what_suffix='{/color}',callback=inctime)
define julian_run4 = Character("Julian",image="julian",color="#71A4B0",what_prefix='{color=#0ff}', what_suffix='{/color}',callback=inctime)
define boy = Character("???",image="julian",color="#71A4B0",callback=inctime)
define boy_run2 = Character("???",image="julian",color="#71A4B0",what_prefix='{color=#f00}', what_suffix='{/color}',callback=inctime)
define cody = Character("Cody",image="cody",color="#aa2b3a",callback=inctime)
define cody_run2 = Character("Cody",image="cody",color="#aa2b3a",what_prefix='{color=#f00}', what_suffix='{/color}',callback=inctime)
define cody_run3 = Character("Cody",image="cody",color="#aa2b3a",what_prefix='{color=#0f0}', what_suffix='{/color}',callback=inctime)
define sandra = Character("Sandra",image="sandra",color="#F0D193",callback=inctime)
define sandra_run2 = Character("Sandra",image="sandra",color="#F0D193",what_prefix='{color=#f00}', what_suffix='{/color}',callback=inctime)
define sandra_run3 = Character("Sandra",image="sandra",color="#F0D193",what_prefix='{color=#0f0}', what_suffix='{/color}',callback=inctime)
define sandra_run4 = Character("Sandra",image="sandra",color="#F0D193",what_prefix='{color=#0ff}', what_suffix='{/color}',callback=inctime)

# define animated fade sprite for Julian
image julian fade:
    "images/chars/julianshadow.png"
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
image julian blur = im.Blur("images/chars/julian neutral.png", 2.5)
image julian glitch:
    "images/chars/julianglitch_1.png"
    0.1
    "images/chars/julianglitch_2.png"
    0.1
    "images/chars/julianglitch_3.png"
    0.1
    "images/chars/julianglitch_4.png"
    0.1
    "images/chars/julianglitch_3.png"
    0.1
    "images/chars/julianglitch_2.png"
    0.1
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
image flower_run1:
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
image flower_run2:
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
image flower_run3:
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

image flower_glitch_image:
    Glitch("images/props/flower.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
    xalign 0.5
    yalign 0.5
image flower_glitch_image_final: # bouquet of 3
    Glitch("images/props/flower.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
    xalign 0.5
    yalign 0.5

# define custom positions for sprites
transform center_left:
    xalign 0.3 yalign 1.0
transform center_right:
    xalign 0.7 yalign 1.0

# define screen layers
define config.layers = [ 'master', 'background','background_overlay','characters','transient', 'interface', 'screens', 'overlay' ]
$ config.tag_layer['bg'] = 'background'

# define music
define loop1music = "audio/music/SWAK Loop 1 MSTR V1.ogg"
define loop2music = "audio/music/SWAK Loop 1 MSTR V1.ogg"
define loop3music = "audio/music/SWAK Loop 3 MSTR V1.ogg"
define loop4music = "audio/music/SWAK Loop 4 MSTR V1.ogg"
# define endingmusic = ""

# check run number at beginning to progress runs
label checkrun:
    if flowers.flower3:
        $ run = 4
        show flower_run1:
            xalign 0.515
            yalign 0.6
            rotate 25
        show flower_run2:
            xalign 0.485
            yalign 0.6
            rotate -25
        show flower_run3:
            xalign 0.5
            yalign 0.6
        play music loop4music
    elif flowers.flower2:
        $ run = 3
        show flower_run1:
            xalign 0.51
            yalign 0.6
            rotate 15
        show flower_run2:
            xalign 0.49
            yalign 0.6
            rotate -15
        play music loop3music
    elif flowers.flower1:
        $ run = 2
        show flower_run1:
            xalign 0.5
            yalign 0.6
        play music loop2music
    else:
        $ run = 1
        play music loop1music
    # if run >= 2:
    #     show reflection:
    #         xalign 0.5
    #         yalign 0.05
    #     with { "master" : Dissolve(1.0) }
    time_centered "7 PM"
    hide flower_run1
    hide flower_run2
    hide flower_run3
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
    $ hints = Hints() # initialize puzzle hints vars
    $ moonglitches = MoonGlitches() # initialize moon glitch vars
    $ endings = Endings() # initialize endings vars

    # initialize story vars
    $ loop2_investigate = False
    $ loop3_investigate = False
    $ smoke_break = False

    # temporary disable puzzles
    $ solves.loop2 = True
    $ solves.loop3 = True
    $ solves.loop4 = True

    stop music fadeout 2.0

    show screen howtoplay
    $ renpy.pause()
    hide screen howtoplay

    # "BEGIN"
    pause 2.0

    $ renpy.block_rollback() # prevent rollback before this point
    $ config.rollback_enabled = True # re-enable rollback

    scene bg black with dissolve

    # show screen moonglitchscreen onlayer interface
    show screen flowerscreen onlayer interface

    # show rearview:
    #     xalign 0.5
    #     yalign 0.05

    # with { "master" : Dissolve(1.0) }
    call checkrun from _call_checkrun

    jump mainrun

    # return
