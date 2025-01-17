# The script of the game goes in this file.

label back_to_lake:
    show bg scene3 with dissolve
    if run == 2:
        "{color=#f00}Leading her down the patio stairs and down the hill towards the lake, they head to the lakeshore.{/color}" (callback = functools.partial(inctime, checkskip=True))
    sandra_run2 "Is this where you saw him?" (callback = functools.partial(inctime, checkskip=True))
    delilah_run2 "Yes! He was right here!" (callback = functools.partial(inctime, checkskip=True))
    sandra_run2 "Well...if he was here he's gone now." (callback = functools.partial(inctime, checkskip=True))
    delilah_run2 "Should we look for him?" (callback = functools.partial(inctime, checkskip=True))
    sandra_run2 "I mean...he's probably just one of the neighbor kids. Had too much to drink maybe? I'm sure he'll be fine." (callback = functools.partial(inctime, checkskip=True))
    delilah_run2 "But he wasn't...he looked like he wasn't even from around here." (callback = functools.partial(inctime, checkskip=True))
    sandra_run2 "Could've been one of the landscapers' kids then. Who knows? It hardly seems like any of our business, Del." (callback = functools.partial(inctime, checkskip=True))
    delilah_run2 "Wow." (callback = functools.partial(inctime, checkskip=True))
    sandra_run2 "What?" (callback = functools.partial(inctime, checkskip=True))
    # glitch 1 - phase 4
    if run == 2:
        $ moonglitch1 = True
    delilah_run2 "I'm somehow completely unsurprised and still shocked by you." (callback = functools.partial(inctime,g1=True))
    if run == 2:
        $ moonglitch1 = False
    # glitch 2 - phase 1
    if run == 2:
        $ moonglitch2 = True
    # replace below with animation/sfx
    delilah_thoughts_run2 "She turns around and starts her way back up the hill." (callback = functools.partial(inctime, g2=True))
    if run == 2:
        $ moonglitch2 = False
    sandra_run2 "Let's just go try and have a normal evening together, yeah?" (callback = functools.partial(inctime, checkskip=True))
    # delilah "Sandra is receptive and follows Delilah back to the lake but when they get there Julian is gone. Sandra believes Delilah that there is a boy out there who needs help, but she decides that it's best to just ignore the situation. \"Someone will find him and get him help, let's just go inside.\" " (callback = functools.partial(inctime, checkskip=True))
    # delilah "Delilah is deeply disturbed by this." (callback = functools.partial(inctime, checkskip=True))

    # glitch 3 - phase 3
    if run == 2:
        $ moonglitch3 = True
    menu:
        delilah " " (callback = functools.partial(inctime,g3=True))
        "{color=#f00}Fine.{/color}":
            if run == 2:
                $ moonglitch3 = False
            # glitch 4 - phase 5
            if run == 2:
                $ moonglitch4 = True
            delilah_run2 "Fine." (callback = functools.partial(inctime,g4=True))
            if run == 2:
                $ moonglitch4 = False
            hide sandra onlayer characters
            show bg black
            with dissolve

            jump dinner_convo
            
        "{color=#f00}Go looking for the boy{/color}":
            if run == 2:
                $ moonglitch3 = False
            delilah_thoughts_run2 "Go looking for the boy" (callback = functools.partial(inctime))
            hide sandra onlayer characters with dissolve
            jump search_for_julian