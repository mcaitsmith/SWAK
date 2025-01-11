# The script of the game goes in this file.

label search_for_julian:
    show julian sad at right with dissolve
    delilah "Delilah goes outside to look for the boy she saw. She walks down the shoreline for a while before finding him laying on top of some rocks, fading in and out of consciousness. He's glad to see Delilah again and apologizes for disappearing. He's switching between her reality and his repeatedly and being in her reality is killing him. He describes it almost like \"being a weed in someone else's garden\". And that he is being pruned. Delilah panics and asks if there is anything she can do. He just asks that she stay with him for a while, talk to him while he dies."
    menu:
        delilah "Dialogue choice" (callback = functools.partial(inctime, trig=True))
        "Go get help":
            hide julian with dissolve
            jump get_help
        "Stay with him":
            jump stay_with_him