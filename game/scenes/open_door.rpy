# The script of the game goes in this file.

label open_door:

    # open door scene: black with transparent window to moon + door windowpanes showing lake scene
    # once open door window fades to open door cutout

    pause 2.0 # play unlocking sound here

    show bg black with dissolve
    pause 1.0

    if run == 3 and loop3_investigate:
        call incphase

        "8 PM"
        pause 1.0

        jump dinner_convo
    elif run == 2 and loop2_investigate:
        "8 PM"
        pause 1.0

        delilah "With one flower in possession, Delilah is quick to let her mom and brother in. She tells them that there's a boy by the lake who needs medical attention." (callback = functools.partial(inctime, checkskip=True))
        hide cody onlayer characters with dissolve
        jump back_to_lake
    else:
        
        call incphase

        # glitch 4 - phase 3
        if run == 2:
            $ moonglitch4 = True

        "8 PM" (callback = functools.partial(inctime, g4=True))
        pause 1.0

        if run == 2:
            $ moonglitch4 = False

        # add footsteps/ backdoor opening sfx
        delilah_thoughts "Sure enough, the key was still under the tacklebox, just where Dad always kept it." (callback = functools.partial(inctime,checkskip=True))
        # delilah_thoughts "Sure enough, the key is still under the tacklebox, just where Dad always kept it. The backdoor unlocks and Delilah enters the house." (callback = functools.partial(inctime, g4=True))

        if run == 1:
            "With the dust floating in the air like flakes, for a moment Delilah thinks she's walked into a snowglobe of her own childhood." (callback = functools.partial(inctime,checkskip=True))

        # delilah_thoughts "With the dust floating in the air like flakes, for a moment Delilah thinks she's walked into a snowglobe of her own childhood." (callback = functools.partial(inctime,checkskip=True))
        
        delilah_thoughts "Cody's pressing his nose against the window, banging his hand on the glass like a zombie." (callback = functools.partial(inctime,checkskip=True))
        # delilah_thoughts "She looks across the foyer to see Cody pressing his nose against the window, banging his hand on the glass like a zombie." (callback = functools.partial(inctime,checkskip=True))
        delilah_thoughts "Open the door" (callback = functools.partial(inctime,checkskip=True))
        
        # add open door sound here to replace line above
        pause 1.0
        
        show sandra neutral onlayer characters at center
        
        sandra "Oh, how gracious of you to finally decide to let us in, Del. Very gracious indeed." (callback = functools.partial(inctime,checkskip=True))
        
        show cody happy onlayer characters at center_right
        
        cody "Yes, very gracious." (callback = functools.partial(inctime,checkskip=True))
        delilah "Hey, are there still landscapers working in the yard?" (callback = functools.partial(inctime,checkskip=True))
        sandra "Landscapers? Not at this hour, no. Why do you ask?" (callback = functools.partial(inctime,checkskip=True))
        delilah "Could've sworn I saw someone out back. Thought it might have been a landscaper." (callback = functools.partial(inctime,checkskip=True))
        sandra "Probably just one of the neighbor kids, I wouldn't worry about it." (callback = functools.partial(inctime,checkskip=True))
        
        hide cody onlayer characters
        hide sandra onlayer characters
        with dissolve
        
        jump dinner_convo

label dinner_convo:
    if run == 3 and loop3_investigate:
        delilah "Now looking for the Selene Lillies, Delilah proceeds with the previously established dinner scene with Cody and her mom. However, she is a bit less antagonistic of them as she now has a new goal of saving Julian. During dinner, she notices something glowing in Cody's pocket. Sandra steps out to have a smoke while Cody and Delilah clean up the kitchen."
        hide sandra onlayer characters with dissolve
        menu:
            delilah "Dialogue choice" (callback = functools.partial(inctime))
            "go with Sandra":
                hide cody onlayer characters with dissolve
                call smoke_break from _call_smoke_break
            "stay inside":
                delilah "In this scene, the player talks with Cody and discovers that he found one of the glowing flowers in the front yard. If Delilah asks for it back he attempts to bargain for it, but, being a little brat, tears it apart instead of giving it to you. You can reattempt the conversation as many times as you want, trying different options each time, even explaining the situation with Julian to him, but he laughs and rips the flower up every time."
                show sandra neutral onlayer characters at center_right with dissolve
                delilah "After Cody rips up the flower, the player can punch Cody just as Sandra walks in. Delilah gets in trouble and Sandra tells her to come outside."
        if smoke_break:
            delilah "If the player has completed the smoke break conversation, a new dialogue option is available with Cody in which she can tell him everything about their father's infidelity. Just as Sandra said, the news is devastating and he refuses to accept it, but you go further and further by sharing details from the letter Delilah read. Each detail hurts him more and more. He looks at the flower for a moment, questioning everything he's ever known, and then leaves it on the counter."
            if not flowers.flower3:
                delilah "Delilah gets the flower and is able to roll back and start the fourth loop." (callback = functools.partial(inctime, fnum=3))
            else:
                pass
            # sandra returns, delilah goes outside
            show sandra neutral onlayer characters at center with dissolve
        hide cody onlayer characters with dissolve
        hide sandra onlayer characters with dissolve
        jump outside
    elif run == 2 and loop2_investigate:
        call incphase

        delilah "If the player goes back inside, Delilah experiences the dinner conversation again, except her attitude is much harsher with more options to antagonize Cody and Sandra. We get a few more clues as to what is truly upsetting Delilah but we don't outright know it yet."
        delilah "The dinner ends in a much more explosive manner than the first time and Delilah can either"
        menu:
            delilah "Dialogue choice" (callback = functools.partial(inctime))
            "run outside":
                hide cody onlayer characters with dissolve
                hide sandra onlayer characters with dissolve
                jump outside
            "tell off her mom before going outside":
                delilah "With the second option Delilah says some incredibly hurtful things, the sort that would make a relationship impossible to fix. It's obvious how hurt Sandra is. Then she goes back to the regular \"outside\" passage"
                hide cody onlayer characters with dissolve
                hide sandra onlayer characters with dissolve
                jump outside
    else:
        
        show bg scene2 with Dissolve(2.0)
        
        delilah_thoughts "Not even a minute after Sandra tips the pizza delivery driver, Cody has two slices on his plate." (callback = functools.partial(inctime,checkskip=True))
        
        show cody happy onlayer characters at center
        
        delilah_thoughts "He pulls the cheese off and eats it separately, then licks the sauce off the crust before eating it." (callback = functools.partial(inctime,checkskip=True))
        # replace this line below with expression change
        delilah_thoughts "Delilah watches in horror." (callback = functools.partial(inctime,checkskip=True))
        delilah "Can't even eat pizza like a normal person?" (callback = functools.partial(inctime,checkskip=True))
        cody "I can't help it if my eccentricities extend to my dining preferences." (callback = functools.partial(inctime,checkskip=True))
        delilah "Eccentricities? Is that what they're calling being a little weirdo now?" (callback = functools.partial(inctime,checkskip=True))
        delilah_thoughts "Mom sits down at the table with nothing but a salad on her plate." (callback = functools.partial(inctime,checkskip=True))
        # delilah_thoughts "Sandra sits down at the table with nothing but a salad on her plate." (callback = functools.partial(inctime,checkskip=True))
        
        show sandra neutral onlayer characters at right
        
        sandra "Oh, hush, Del, you used to have particular eating habits too." (callback = functools.partial(inctime,checkskip=True))
        delilah "Yeah, when I was five. Cody's almost in high school. God help my reputation if anyone finds out we're related!" (callback = functools.partial(inctime,checkskip=True))
        cody "I'm not exactly shouting from the roof tops about being related to a wastoid either." (callback = functools.partial(inctime,checkskip=True))
        delilah "Bite me!" (callback = functools.partial(inctime,checkskip=True))
        cody "Bitch..." (callback = functools.partial(inctime,checkskip=True))
        # make line above small text to replace line below
        cody "he says under his breath." (callback = functools.partial(inctime,checkskip=True))
        delilah "You little!" (callback = functools.partial(inctime,checkskip=True))
        # replace line below with animated sprites
        delilah_thoughts "She stands up and raises her fist like she's going to punch him from across the table." (callback = functools.partial(inctime,checkskip=True))
        sandra "Hey! Hey! Relax!" (callback = functools.partial(inctime,checkskip=True))
        delilah "Make him apologize!" (callback = functools.partial(inctime,checkskip=True))
        sandra "Cody...will you please apologize to your sister for calling her a b-word?" (callback = functools.partial(inctime,checkskip=True))
        cody "She started it!" (callback = functools.partial(inctime,checkskip=True))
        sandra "Cody...things are hard enough as is..." (callback = functools.partial(inctime,checkskip=True))
        # replace line below with animated sprite
        delilah_thoughts "Delilah crosses her arms and raises an eyebrow." (callback = functools.partial(inctime,checkskip=True))
        cody "I'm sorry...that you're a bitch." (callback = functools.partial(inctime,checkskip=True))
        sandra "That's it! Upstairs, now!" (callback = functools.partial(inctime,checkskip=True))
        delilah_thoughts "He drops his bare crusts in the trash dramatically then heads for the stairs." (callback = functools.partial(inctime,checkskip=True))
        cody "I wonder why Dad prefers his business trips to being here!" (callback = functools.partial(inctime,checkskip=True))
        
        hide cody onlayer characters with dissolve

        call incphase

        # glitch 5 - phase 4
        if run == 2:
            $ moonglitch5 = True
        menu:
            delilah " " (callback = functools.partial(inctime, g5=True))
            "What a little brat":
                if run == 2:
                    $ moonglitch5 = False
                delilah "What a little brat"
            "I can't believe you let him get away with that.":
                if run == 2:
                    $ moonglitch5 = False
                delilah "I can't believe you let him get away with that."
        sandra "Well, Del, you don't exactly make it easy by antagonizing him."
        delilah "I don't antagonize him..."
        delilah_thoughts "Those last words he said before storming off..."
        # delilah_thoughts "she thought about the last words he said before storming off."
        delilah "He's right though, about Dad, I mean."
        sandra "Your dad wishes he could be here more than anything in the world. Work has been brutal lately."
        delilah_thoughts "She laughs." # add laugh sound to replace this or just (haha)
        delilah "Yeah, I'm sure."
        sandra "What's that supposed to mean?"
        delilah "I think you know what I mean."
        sandra "No, I don't, and you should watch what you say or you'll regret it."
        delilah "Is that a promise?"
        sandra "Don't you start."
        menu:
            delilah " " (callback = functools.partial(inctime))
            "Dad can't stand you.":
                delilah "Dad can't stand you."
            "It's your fault he isn't here.":
                delilah "It's your fault he isn't here."
            "This family is a joke.":
                delilah "This family is a joke."
        sandra "Upstairs. Now."
        delilah "Fuck you, I'm going for a walk."

        hide sandra onlayer characters with dissolve

        jump outside