# The script of the game goes in this file.

label start_loop2:
    delilah_thoughts "There's a glowing flower in my hand." (callback = functools.partial(inctime, g2=True))
    # delilah_thoughts "Delilah looks down to see a glowing flower in her hand." (callback = functools.partial(inctime, g2=True))
    $ moonglitch2 = False

    call incphase
    
    # glitch 1 - phase 2
    if run == 2:
        $ moonglitch1 = True
    if run == 2:
        "A dam ruptures and she can see the image of that boy dying on the lakeshore burned into her mind." (callback = functools.partial(inctime, g1=True, checkskip=True))
    if run == 2:
        $ moonglitch1 = False
    delilah_thoughts "This has already happened. The dinner. The fight. The boy dying in our backyard." (callback = functools.partial(inctime, checkskip=True))
    # delilah_thoughts "This has already happened. The dinner. The fight. The boy dying in their backyard. " (callback = functools.partial(inctime, checkskip=True))
    # glitch 3 - phase 2
    if run == 2:
        $ moonglitch3 = True
    menu:
        delilah " " (callback = functools.partial(inctime,g3=True))
        "Go to the lakeshore":
            if run == 2:
                $ moonglitch3 = False
            # glitch 4 - phase 3
            if run == 2:
                $ moonglitch4 = True
            delilah_thoughts "Go to the lakeshore"
            if run == 2:
                $ moonglitch4 = False
            jump investigate_lakeshore
        "Open the backdoor for Mom and Cody":
            hide julian onlayer characters
            with { "characters" : Dissolve(3.0) }
            if run == 2:
                $ moonglitch3 = False
            # glitch 4 - phase 3
            if run == 2:
                $ moonglitch4 = True
            delilah_thoughts "Open the backdoor for Mom and Cody" (callback = functools.partial(inctime,g4=True))
            if run == 2:
                $ moonglitch4 = False
            jump open_door