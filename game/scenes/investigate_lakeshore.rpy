# The script of the game goes in this file.

label investigate_lakeshore:
    # zoom bg plus sfx
    if run == 2:
        "Delilah runs down the hill. The air is silent, aside from the sound of the water lapping against the rocks." (callback = functools.partial(inctime))
    delilah_thoughts "Did I imagine the whole thing? That must be it. There is no boy dying on the lakeshore."
    # delilah_thoughts "Did she imagine the whole thing? That must be it. There is no boy dying on the lakeshore."
    pause 1.0
    show julian neutral onlayer characters at center:
        zoom 0.7
    pause 1.0
    if run == 2:
        "A shadow materializes out of the corner of her eye. It slowly peels into existence until it takes the shape of a person. Then finally a face and body forms...the one from her memory."
    # delilah "Delilah goes by the shore to find Julian standing there confused. He remembers Delilah and then everything fading to black. He's afraid of you but then starts to remember that she took the flower from him before everything went black." (callback = functools.partial(inctime))

    delilah_thoughts "He gasps for air, looking around frantically."
    delilah "Oh my God, you're..."
    boy "S-stay away from me..."
    delilah_thoughts "He clutches his side, trying and failing to hold himself up."
    delilah "It's okay! You're okay! Just stay here, I'll get help!"

    # delilah "As the two talk, Julian keels over in pain. Delilah asks what's wrong but not even he knows. Delilah's mom calls for her. She leaves to go get help."
    hide julian onlayer characters with dissolve
    $ loop2_investigate = True
    jump open_door