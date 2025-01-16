# The script of the game goes in this file.

label back_to_lake:
    show bg scene3 with dissolve
    if run == 2:
        "Leading her down the patio stairs and down the hill towards the lake, they head to the lakeshore." (callback = functools.partial(inctime, checkskip=True))
    sandra "Is this where you saw him?" (callback = functools.partial(inctime, checkskip=True))
    delilah "Yes! He was right here!" (callback = functools.partial(inctime, checkskip=True))
    sandra "Well...if he was here he's gone now." (callback = functools.partial(inctime, checkskip=True))
    delilah "Should we look for him?" (callback = functools.partial(inctime, checkskip=True))
    sandra "I mean...he's probably just one of the neighbor kids. Had too much to drink maybe? I'm sure he'll be fine." (callback = functools.partial(inctime, checkskip=True))
    delilah "But he wasn't...he looked like he wasn't even from around here." (callback = functools.partial(inctime, checkskip=True))
    sandra "Could've been one of the landscapers' kids then. Who knows? It hardly seems like any of our business, Del." (callback = functools.partial(inctime, checkskip=True))
    delilah "Wow." (callback = functools.partial(inctime, checkskip=True))
    sandra "What?" (callback = functools.partial(inctime, checkskip=True))
    delilah "I'm somehow completely unsurprised and still shocked by you." (callback = functools.partial(inctime, checkskip=True))
    # replace below with animation/sfx
    delilah_thoughts "She turns around and starts her way back up the hill." (callback = functools.partial(inctime, checkskip=True))
    sandra "Let's just go try and have a normal evening together, yeah?" (callback = functools.partial(inctime, checkskip=True))
    # delilah "Sandra is receptive and follows Delilah back to the lake but when they get there Julian is gone. Sandra believes Delilah that there is a boy out there who needs help, but she decides that it's best to just ignore the situation. \"Someone will find him and get him help, let's just go inside.\" " (callback = functools.partial(inctime, checkskip=True))
    # delilah "Delilah is deeply disturbed by this." (callback = functools.partial(inctime, checkskip=True))
    menu:
        delilah " " (callback = functools.partial(inctime, checkskip=True))
        "Fine.":
            delilah "Fine."
            hide sandra onlayer characters
            show bg black
            with dissolve

            # show bg scene2 with dissolve
            # show cody happy onlayer characters at center with dissolve
            jump dinner_convo
            
        "Go looking for the boy":
            delilah_thoughts "Go looking for the boy"
            hide sandra onlayer characters with dissolve
            jump search_for_julian