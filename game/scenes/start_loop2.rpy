# The script of the game goes in this file.

label start_loop2:
    delilah "With the first flower obtained, Delilah is able to access history and make new choices. A new line is added to the intro in which Delilah notices one of the flowers in her hand. The first choice that becomes available is whether to open the door or"
    menu:
        delilah "Dialogue choice" (callback = functools.partial(inctime, trig=True))
        "investigate the lake shore":
            jump investigate_lakeshore
        "Open the door":
            hide julian with dissolve
            jump open_door