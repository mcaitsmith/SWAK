# The script of the game goes in this file.

label search_for_julian:

    time_centered "8 PM" (callback = functools.partial(inctime))
    pause 1.0

    # sfx/bg change
    if run == 2:
        "{color=#f00}This guy, whoever he is, will die if they do nothing.\nSo, Delilah goes walking along the lakeshore, hopping across fences and docks.{/color}"
    show bg scene3 with dissolve
    if run == 2:
        "{color=#f00}She thinks to call out for him, but remembers that she doesn't know his name.\nWhat would she yell out? \"Boy!\" \"Hello? I'm looking for a boy!\" No.\nInstead, she walks around in the dark.{/color}"
    pause 1.0
    delilah_thoughts_run2 neutral "Stepping across a pile of rocks, I feel something person-shaped under my heel."
    # delilah_thoughts "Delilah, stepping across a pile of rocks, feels something person-shaped under her heel."

    show julian pain onlayer characters at center with dissolve

    boy_run2_d worried "Ow!"
    delilah_run2 "Oh! I'm sorry! I'm sorry!"
    show julian worried onlayer characters
    boy_run2_d "Watch where you're stepping! Ow."

    call incphase from _call_incphase_11

    show julian neutral onlayer characters
    delilah_run2 "There you are! Where did you go before? I was trying to help you!"
    boy_run2_d "Wasn't up to me. I keep popping in and out like that. Ending up different places around the lake."
    delilah_run2 neutral "Popping in and out?"
    show julian worried onlayer characters
    boy_run2_d"Yeah. Like one minute I'm picking flowers around a deserted lake and the next there's a whole neighborhood built around it and a rude girl stepping on me. I keep going back and forth."
    delilah_run2 worried "Oh no, you're delirious. How much blood have you lost?"
    boy_run2_d "None. I haven't lost any. But I AM dying, unfortunately."
    delilah_run2 "What? How?"
    boy_run2_d "It already happened once before. You were there, and it's about to happen again."
    delilah_run2 "How could you know that you're dying?"
    boy_run2_d "Death has a very unmistakable taste to it. Very metallic."
    delilah_run2 "What can I do to help? Should I go get an ambulance?"
    show julian neutral onlayer characters
    boy_run2_d "Something tells me that won't help...honestly what I'd really appreciate is if you stuck around and kept me company. Y'know, just stay till the last light goes out."
    
    # delilah "Delilah goes outside to look for the boy she saw. She walks down the shoreline for a while before finding him laying on top of some rocks, fading in and out of consciousness. He's glad to see Delilah again and apologizes for disappearing. He's switching between her reality and his repeatedly and being in her reality is killing him. He describes it almost like \"being a weed in someone else's garden\". And that he is being pruned. Delilah panics and asks if there is anything she can do. He just asks that she stay with him for a while, talk to him while he dies."
    menu:
        delilah_run2 " " (callback = functools.partial(inctime))
        "{color=#f00}Stay with him{/color}":
            delilah_thoughts_run2 "Stay with him"
            jump stay_with_him
        "{color=#f00}Go get help{/color}":
            delilah_thoughts_run2 "Go get help"
            jump get_help