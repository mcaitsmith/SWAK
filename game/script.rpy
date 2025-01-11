# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:   
    import functools 
    time = 0 #initialize time
    run = 1 # initialize run
    trigger = False # initialize trigger

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
            if fnum == 5:
                flowers.flower5 = True

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
            self.flower5 = False

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
define e = Character("Eileen",callback=inctime)

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
    if flowers.flower5:
        text "Flower 5" xpos 0.1 ypos 0.35

# define scene bgs
image bg scene1 = "#4680bd"
image bg scene2 = "#f0c047"
image bg scene3 = "#5646bd"
image bg black = "#000000"

# check run
label checkrun:
    if flowers.flower4:
        $ run = 5
    elif flowers.flower3:
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

    $ flowers = Flowers() # initialize flowers

    show screen showtime
    show screen showflower

    scene bg scene1 with dissolve

    "BEGIN"

    $ renpy.block_rollback() # prevent rollback before this point
    $ config.rollback_enabled = True # re-enable rollback

    call checkrun

    show eileen happy with dissolve

    e "Dialogue 1 START{alt}{noalt}{color=#f00} hidden code{/color}{/noalt}{/alt}"
    e "Dialogue 2"
    menu:
        e "Dialogue 3" (callback = functools.partial(inctime, trig=True))
        "Choice 1":
            e "Dialogue 4.1"
        "Choice 2 - HAVE FLOWER 1" if run == 2:
            e "Dialogue 4.2"

    show bg scene2 with dissolve

    e "Dialogue 5"
    e "Dialogue 6"
    e "Dialogue 7"

    show bg scene3 with dissolve

    e "Dialogue 8"
    if not flowers.flower1:
        e "Dialogue 9 - found FLOWER 1" (callback = functools.partial(inctime, fnum=1))
    else:
        e "Dialogue 9 (already found FLOWER 1)"
    e "Dialogue 10 END"

    hide eileen with dissolve

    show bg black with dissolve

    return
