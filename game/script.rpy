# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:   
    import functools 
    time = 0 #initialize time
    run = 1 # initialize run
    trigger = False # initialize trigger

    # initialize story vars
    loop2_investigate = False
    loop3_investigate = False
    smoke_break = False

    # define function to increment time by 1 every line of dialogue + add flowers/triggers
    def inctime(event, interact=True, fnum=None, trig=False, **kwargs):
        global time
        global flowers
        global trigger
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

            if trig:
                trigger = True
            else:
                trigger = False
        return

    # config.character_callback = inctime # set callback for character statements to increase time

    # create persistent flower class
    class Flowers(NoRollback):
        def __init__(self):
            self.flower1 = False
            self.flower2 = False
            self.flower3 = False
            self.flower4 = False

    # create persistent endings class
    class Endings(NoRollback):
        def __init__(self):
            self.ending1 = False
            self.ending2 = False
            self.ending3 = False

    def history_time_callback(x):
        global time
        global run
        # if trigger:
        #     x.what = "{color=#f00}>>>TRIGGER>>>{/color} " + x.what
        x.what = "RUN " + str(run) + " | TIME " + str(time) + "\n" + x.what
    config.history_callbacks.append(history_time_callback)
    # Add new function to the history callbacks
    # if history_trigger_callback not in config.history_callbacks:
    #     config.history_callbacks.append(history_trigger_callback)

define narrator = Character(None,callback=None)
define delilah = Character("Delilah",callback=inctime)
define julian = Character("Julian",callback=inctime)
define cody = Character("Cody",callback=inctime)
define sandra = Character("Sandra",callback=inctime)

screen showtime: # screen for showing time
    text "Time [time]" xpos 0.1 ypos 0.1
screen showflower: # screen for showing flowers
    if flowers.flower1:
        text "Flower 1" xpos 0.1 ypos 0.15
    if flowers.flower2:
        text "Flower 2" xpos 0.1 ypos 0.2
    if flowers.flower3:
        text "Flower 3" xpos 0.1 ypos 0.25
    if flowers.flower4:
        text "Flower 4" xpos 0.1 ypos 0.3

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
    $ endings = Endings() # initialize endings vars

    # initialize story vars
    $ loop2_investigate = False
    $ loop3_investigate = False
    $ smoke_break = False

    show screen showtime
    show screen showflower

    scene bg scene1 with dissolve

    "BEGIN"

    $ renpy.block_rollback() # prevent rollback before this point
    $ config.rollback_enabled = True # re-enable rollback

    call checkrun

    jump mainrun

    # return
