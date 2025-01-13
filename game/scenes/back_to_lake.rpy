# The script of the game goes in this file.

label back_to_lake:
    show bg scene3 with dissolve
    delilah "Sandra is receptive and follows Delilah back to the lake but when they get there Julian is gone. Sandra believes Delilah that there is a boy out there who needs help, but she decides that it's best to just ignore the situation. \"Someone will find him and get him help, let's just go inside.\" " (callback = functools.partial(inctime, checkskip=True))
    delilah "Delilah is deeply disturbed by this." (callback = functools.partial(inctime, checkskip=True))
    menu:
        delilah "Dialogue choice" (callback = functools.partial(inctime, checkskip=True))
        "go search for Julian":
            hide sandra onlayer characters with dissolve
            jump search_for_julian
        "go back inside":
            show bg scene2 with dissolve
            show cody happy onlayer characters at center with dissolve
            jump dinner_convo