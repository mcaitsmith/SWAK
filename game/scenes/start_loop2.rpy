# The script of the game goes in this file.

label start_loop2:
    delilah "With the first flower obtained, Delilah is able to access history and make new choices." (callback = functools.partial(inctime, g2=True))
    $ moonglitch2 = False
    $ phase += 1
    show screen eclipse onlayer background_overlay with Dissolve(2.0)
    pause 1.0
    # glitch 1 - phase 2
    $ moonglitch1 = True
    delilah "A new line is added to the intro in which Delilah notices one of the flowers in her hand." (callback = functools.partial(inctime, g1=True, checkskip=True))
    $ moonglitch1 = False
    delilah "The first choice that becomes available is whether to open the door or" (callback = functools.partial(inctime, checkskip=True))
    # glitch 3 - phase 2
    $ moonglitch3 = True
    menu:
        delilah "Dialogue choice" (callback = functools.partial(inctime,g3=True))
        "investigate the lake shore":
            $ moonglitch3 = False
            jump investigate_lakeshore
        "Open the door":
            $ moonglitch3 = False
            hide julian onlayer characters with dissolve
            jump open_door