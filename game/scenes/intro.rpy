# The script of the game goes in this file.

label intro:

    delilah neutral "Delilah was stuck. She was between the tumultuous indignities of adolescence and the quiet ennui of adulthood, frozen in place before this choice that life had presented her with. Right on the line of 'too old to be acting like this' and 'too young to be trusted.'"
    show sandra neutral onlayer characters at center_right
    sandra "So, have you considered what colleges you want to tour next summer?"
    delilah "She waited till the end of the ride to ask her daughter this question. Four hours in the car, pure silence, and she waited till the lakehouse was practically in sight to ask a question like that."
    delilah "That's not for another nine months."
    sandra "Sooner than you think, Del. Always good to get a head start. Plus, I have my friend who teaches at State. Could get you a tour any time you like!"
    show cody happy onlayer characters at center_left
    cody "Ugh, I can't wait for you to be gone."
    delilah "Shut up, insect."
    delilah "She punches her little brother in the arm."
    cody "Ow!"
    sandra "Oh hush, you'll be missing her when she's gone. Just you wait."
    cody "Yeah right. She'll be back every weekend, I bet, if she doesn't flunk out that is." 
    delilah "I said shut up!"
    cody "Make me!" 
    sandra "Quiet! We're here!"

    hide cody onlayer characters
    hide sandra onlayer characters
    show bg scene1
    show screen eclipse onlayer background_overlay
    with Dissolve(3.0)
    pause 2.0

    delilah "The house was lifeless, suspended in time until the two weekends per year that they used the place. Nearly every house on the block was someone's home away from home, loved only by the landscaping and housekeeping staff that kept them from becoming a cobweb metropolis of wild animals."
    delilah "Delilah was thinking a lot lately about the difference between a house and a home. For most of her life, she thought they were synonymous. But recently she realized that a home was a place you felt at home, a house was a place you lived in."
    delilah "She didn't feel at home anywhere. Not anymore."

    $ phase += 1
    show screen eclipse onlayer background_overlay with Dissolve(2.0)
    pause 1.0

    show sandra neutral onlayer characters at center
    sandra "Hey, Del, my front door key isn't working."
    delilah "So?"
    sandra "So...can you go try the backdoor? The spare should still be under the tacklebox next to the hottub."
    menu:
        delilah " " (callback = functools.partial(inctime))
        "Fine.":
            delilah "Fine."
        "Make Cody do it!":
            delilah "Make Cody do it!"
        "Do it yourself.":
            delilah "Do it yourself."

    sandra "Thanks, Del. You're a peach."
    show cody happy onlayer characters at center_right
    cody "Yeah, Del, thanks."
    cody "He laughs."
    delilah "Delilah stamped her feet, making sure the earth could feel how unfair this situation was."

    # delilah happy "Game begins with Delilah, a sixteen year old girl, arriving at her family's lakehouse. It's just her, her mother, and her obnoxious little brother, Cody. They're spending a weekend away while dad is on one of his many frequent business trips. He's frequently absent these days."
    # delilah "Delilah is deeply unhappy for reasons we don't yet know but she gives her mother a hard time and antagonizes Cody."

    hide cody onlayer characters
    hide sandra onlayer characters
    with dissolve
    pause 2.0
    # possible transition to new bg or maybe zoom in current one
    delilah "Each house in the neighborhood backed up to the lake, a fleet of boats and jetskis parked at each private dock. It was fun to spend the summer here as a kid, when Dad would take them out on the water, but now...well, things were different."
    pause 1.0
    show julian fade onlayer characters at center
    pause 3.0
    if run == 2: # glitch 2 - phase 1
        $ moonglitch2 = True
    menu:
        delilah " " (callback = functools.partial(inctime))
        "Wait, who is that?":
            delilah "Wait, who is that?"
            delilah "Along the shoreline is what looks like a person standing there, but it's hard to make out."
            menu:
                delilah " " (callback = functools.partial(inctime,checkskip=True))
                "Hey! You there!":
                    delilah "Hey! You there!"
                "Can I help you with something?":
                    delilah "Can I help you with something?"
                "Quietly move closer":
                    delilah "Quietly move closer"
                "Wait, haven't I been here before?" if run == 2:
                    delilah "Wait, haven't I been here before?"
                    jump start_loop2
            hide julian fade onlayer characters with Dissolve(3.0)
            pause 2.0
            delilah "Whatever. Probably one of the landscapers."
        "Just open the damn door.":
            hide julian fade onlayer characters
            with { "characters" : Dissolve(3.0) }
            delilah "Just open the damn door."
            if run == 2:
                $ moonglitch2 = False
    pause 2.0 # play unlocking sound here
    jump open_door
    # delilah "When they arrive, it's close to sunset. The key to the front door isn't working so Delilah has been told to try using the back door. She goes around the back and sees the lake. She sees something just along the shore. The player might stop for a moment or go unlock the door. If they stop for a moment they see what looks lke a shadowy figure standing in the distance. Is that a person? If the player has chosen to linger, her mom shouts for her to open the door."
    # # glitch 2 - phase 1
    # $ moonglitch2 = True
    # menu:
    #     delilah "Dialogue choice" (callback = functools.partial(inctime,checkskip=True))
    #     "Open the door":
    #         $ moonglitch2 = False
    #         hide julian onlayer characters with dissolve
    #         jump open_door
    #     "Wait, haven't I been here before?" if run == 2:
    #         jump start_loop2
    #     "Oh god that hurt" if run == 3:
    #         jump start_loop3
    #     "Im sorry I had to do that" if run == 4:
    #         jump start_loop4

    return
