# The script of the game goes in this file.

label intro:

    # car scene: basic shaking rearview mirror at top on top of black
    # D's reflection in it only for run screen + first narration, then fades out as she turns away
    # ambient car driving sfx

    # initial narration only on first run it appears
    # note: narration text style 80s typewriter text but glowy
    # run/end text in retro 80s font with outline/drop shadow

    # delilah_thoughts neutral "Delilah was stuck. She was between the tumultuous indignities of adolescence and the quiet ennui of adulthood, frozen in place before this choice that life had presented her with. Right on the line of 'too old to be acting like this' and 'too young to be trusted.'"

    # show windshield behind rearview at truecenter 

    # show bg scene1 with dissolve
    
    if run == 1:
        # show reflection:
        #     xalign 0.5
        #     yalign 0.05
        # with { "master" : Dissolve(1.0) }

        "Delilah is stuck.\nBetween the tumultuous indignities of adolescence and the quiet ennui of adulthood,\nfrozen in place before this choice that life has presented her with.\nRight on the line of 'too old to be acting like this' and 'too young to be trusted.'"
    pause 1.0
    # hide reflection with dissolve
    # pause 1.0
    show sandra neutral onlayer characters at center_right
    sandra "So, have you considered what colleges you want to tour next summer?"
    # delilah_thoughts "She waited till the end of the ride to ask her daughter this question. Four hours in the car, pure silence, and she waited till the lakehouse was practically in sight to ask a question like that."
    delilah_thoughts neutral "Mom waited till the end of the ride to ask me this question. Four hours in the car, pure silence, and she waited till the lakehouse was practically in sight to ask a question like that."
    delilah laugh "That's not for another nine months."
    show sandra laugh onlayer characters
    sandra_d neutral "Sooner than you think, Del. Always good to get a head start. Plus, I have my friend who teaches at State. Could get you a tour any time you like!"
    show sandra neutral onlayer characters
    show cody neutral onlayer characters at center_left
    cody_d "Ugh, I can't wait for you to be gone."
    delilah angry "Shut up, insect."
    delilah_thoughts "I punch my little brother in the arm." # add punch sfx to replace + shake cody sprite
    show cody angry onlayer characters
    cody_d "Ow!"
    show sandra laugh onlayer characters
    sandra_d neutral "Oh hush, you'll be missing her when she's gone. Just you wait."
    show cody happy onlayer characters
    cody_d "Yeah right. She'll be back every weekend, I bet, if she doesn't flunk out that is." 
    delilah angry "I said shut up!"
    cody_d "Make me!" 
    show sandra neutral onlayer characters
    sandra_d "Quiet! We're here!"

    hide cody onlayer characters
    hide sandra onlayer characters
    # hide windshield
    # hide rearview
    show bg scene1

    # show moon/eclipse at beginning of run
    show screen eclipse onlayer background_overlay
    with Dissolve(3.0)
    pause 2.0

    if run == 1:
        "The house is lifeless, suspended in time until the two weekends per year that they use the place. Nearly every house on the block is someone's home away from home, loved only by the landscaping and housekeeping staff that keep them from becoming a cobweb metropolis of wild animals."
        "Delilah's thinking a lot lately about the difference between a house and a home.\nFor most of her life, she thought they were synonymous. But recently she's realized that a home is a place you feel at home, a house is a place you lived in."
        "She doesn't feel at home anywhere. Not anymore."

    call incphase from _call_incphase_4

    show sandra neutral onlayer characters at center
    sandra "Hey, Del, my front door key isn't working."
    delilah neutral "So?"
    sandra_d "So...can you go try the backdoor? The spare should still be under the tacklebox next to the hottub."
    menu:
        delilah neutral " " (callback = functools.partial(inctime))
        "Fine.":
            delilah laugh "Fine."
        "Make Cody do it!":
            delilah angry "Make Cody do it!"
        "Do it yourself.":
            delilah happy "Do it yourself."

    show sandra laugh onlayer characters
    sandra_d "Thanks, Del. You're a peach."
    show sandra neutral onlayer characters
    show cody happy onlayer characters at center_right
    cody_d "Yeah, Del, thanks."
    delilah_thoughts neutral "He laughs." # add laugh sound to replace
    delilah_thoughts angry "I stamp my feet, making sure the earth can feel how unfair this situation is." # replace with animation/sfx

    hide cody onlayer characters
    hide sandra onlayer characters
    with dissolve

    pause 2.0 # possible transition to new bg or maybe zoom in current one

    if run == 1:
        "Each house in the neighborhood backs up to the lake, a fleet of boats and jetskis parked at each private dock.\nIt was fun to spend the summer here as a kid, when Dad would take them out on the water, but now...\nwell, things are different."
    pause 1.0

    show julian fade onlayer characters at center:
        zoom 0.7 # in distance
    pause 3.0

    menu:
        delilah neutral " " (callback = functools.partial(inctime))
        "Wait, who is that?":
            delilah "Wait, who is that?"
            show julian shadow onlayer characters at center:
                zoom 0.7 # in distance
            delilah_thoughts "Along the shoreline is what looks like a person standing there, but it's hard to make out."
            menu:
                delilah " " (callback = functools.partial(inctime,checkskip=True))
                "Hey! You there!":
                    delilah "Hey! You there!"
                "Can I help you with something?":
                    delilah "Can I help you with something?"
                "Quietly move closer":
                    delilah_thoughts "Quietly move closer"
                "{color=#f00}Wait...I'm getting a sense of Deja Vu...{/color}" if run == 2:
                    delilah_thoughts_run2 worried "Wait...I'm getting a sense of Deja Vu..."
                    jump start_loop2
                "{color=#0f0}Ow, that really really hurt{/color}" if run == 3:
                    delilah_thoughts_run3 worried "Ow, that really really hurt!"
                    jump start_loop3
                "{color=#0ff}Look over at Cody{/color}" if run == 4:
                    delilah_thoughts_run4 worried "Look over at Cody"
                    jump start_loop4

            hide julian onlayer characters with Dissolve(3.0)
            pause 2.0

            delilah "Whatever. Probably one of the landscapers."
        "Just open the damn door.":
            hide julian onlayer characters
            with { "characters" : Dissolve(3.0) }

            delilah_thoughts "Just open the damn door."

    jump open_door

    return
