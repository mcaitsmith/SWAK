# The script of the game goes in this file.

label investigate_lakeshore:
    # zoom bg plus sfx
    if run == 2:
        "{color=#f00}Delilah runs down the hill.\nThe air is silent, aside from the sound of the water lapping against the rocks.{/color}" (callback = functools.partial(inctime))
    delilah_thoughts_run2 "Did I imagine the whole thing? That must be it. There is no boy dying on the lakeshore."
    # delilah_thoughts "Did she imagine the whole thing? That must be it. There is no boy dying on the lakeshore."
    pause 1.0
    show julian neutral onlayer characters at center with dissolve:
        zoom 0.7
    pause 1.0
    if run == 2:
        "{color=#f00}A shadow materializes out of the corner of her eye.\nIt slowly peels into existence until it takes the shape of a person. Then finally a face and body forms...the one from her memory.{/color}"
    # delilah "Delilah goes by the shore to find Julian standing there confused. He remembers Delilah and then everything fading to black. He's afraid of you but then starts to remember that she took the flower from him before everything went black." (callback = functools.partial(inctime))

    delilah_thoughts_run2 "He gasps for air, looking around frantically."
    delilah_run2 "Oh my God, you're..."
    boy_run2 "S-stay away from me..."
    delilah_thoughts_run2 "He clutches his side, trying and failing to hold himself up."
    delilah_run2 "It's okay! You're okay! Just stay here, I'll get help!"

    # delilah "As the two talk, Julian keels over in pain. Delilah asks what's wrong but not even he knows. Delilah's mom calls for her. She leaves to go get help."
    hide julian onlayer characters with dissolve
    $ loop2_investigate = True
    jump open_door