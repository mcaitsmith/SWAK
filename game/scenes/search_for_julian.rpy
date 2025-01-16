# The script of the game goes in this file.

label search_for_julian:

    # sfx/bg change
    if run == 2:
        "This guy, whoever he is, would die if they did nothing. So, Delilah went walking along the lakeshore, hopping across fences and docks."
        "She thought to call out for him, but remembered that she didn't know his name. What would she yell out? \"Boy!\" \"Hello? I'm looking for a boy!\" No. Instead, she walked around in the dark."
    pause 1.0
    delilah_thoughts "Stepping across a pile of rocks, I feel something person-shaped under my heel."
    # delilah_thoughts "Delilah, stepping across a pile of rocks, feels something person-shaped under her heel."

    show julian sad onlayer characters at center with dissolve

    boy "Ow!"
    delilah "Oh! I'm sorry! I'm sorry!"
    boy "Watch where you're stepping! Ow."

    call incphase

    delilah "There you are! Where did you go before? I was trying to help you!"
    boy "Wasn't up to me. I keep popping in and out like that. Ending up different places around the lake."
    delilah "Popping in and out?"
    boy "Yeah. Like one minute I'm picking flowers around a deserted lake and the next there's a whole neighborhood built around it and a rude girl stepping on me. I keep going back and forth."
    delilah "Oh no, you're delirious. How much blood have you lost?"
    boy "None. I haven't lost any. But I AM dying, unfortunately."
    delilah "What? How?"
    boy "It already happened once before. You were there, and it's about to happen again."
    delilah "What can I do to help? Should I go get an ambulance?"
    boy "Something tells me that won't help...honestly what I'd really appreciate is if you stuck around and kept me company. Y'know, just stay till the last light goes out."
    
    # delilah "Delilah goes outside to look for the boy she saw. She walks down the shoreline for a while before finding him laying on top of some rocks, fading in and out of consciousness. He's glad to see Delilah again and apologizes for disappearing. He's switching between her reality and his repeatedly and being in her reality is killing him. He describes it almost like \"being a weed in someone else's garden\". And that he is being pruned. Delilah panics and asks if there is anything she can do. He just asks that she stay with him for a while, talk to him while he dies."
    menu:
        delilah " " (callback = functools.partial(inctime))
        "Stay with him":
            delilah_thoughts "Stay with him"
            jump stay_with_him
        "Go get help":
            delilah_thoughts "Go get help"
            jump get_help