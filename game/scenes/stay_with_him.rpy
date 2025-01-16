# The script of the game goes in this file.

label stay_with_him:

    delilah "Okay. I'll stay with you."

    delilah_thoughts "I sit down on a patch of grass just above his head."
    # delilah_thoughts "She sits down on a patch of grass just above his head. "
    pause 1.0

    boy "Thank you."

    call incphase
    
    delilah "So...what do you want to do to fill the time? It could be a while till you, y'know..."
    boy "Hmm. Why don't you tell me about yourself? What's your name? What brings you out here to this fine patch of jagged rocks?"
    delilah_thoughts "She chuckles painfully." # replace
    delilah "I'm Delilah. Uh, just here on a short weekend trip with the family."
    boy "Right, and that lovely creature I saw you with before must be your sister then?"
    delilah "Mother and where were you?? I went for help and you disappeared!"
    boy "Oh, y'know, I was halfway between lakes. There and not there."
    delilah "How did you get like...this?"
    boy "Beats the hell out of me. Like I said, I was out picking flowers and ended up here."
    delilah "Picking flowers? Really?"
    boy "Yeah, for my grandparents' flower shop. Is there something wrong with that?"
    delilah "No, no, it's just- I wouldn't ever have guessed."
    boy "They're probably worried sick about me. Say, you haven't heard of a 'Schneider's Happy Petals' have you?"
    delilah "Nothing like that around here."
    boy "Wow. Then I must really be far from home."
    delilah_thoughts "He starts coughing violently."
    boy "Ouch."
    delilah "Are you okay?"
    boy "Yeah...No...Don't worry about it..."
    delilah "You're...dying again, aren't you?"
    boy "It sure feels like it. But, hey, at least I wasn't alone this time."
    delilah_thoughts "I look up and down his body for any sign of injury, none to be found."
    # delilah_thoughts "She looks up and down his body for any sign of injury, none to be found."
    boy "If you come around this way again...if I end up here dying again...you promise you'll wait it out with me again?"
    delilah "Yeah...yeah I promise."
    boy "Rad..."
    delilah "Hey, you never told me your name."
    julian "Oh, how rude of me...uh, it's Julian."
    delilah_thoughts "He tilts his head back and the light drains from his eyes."
    hide julian onlayer characters with dissolve

    call incphase

    delilah_thoughts "He's gone again. I stare at his body, trying to process that I've now witnessed death twice in the same 24-hour period."
    # delilah_thoughts "He's gone again. Delilah stares at his body, trying to process that she has now witnessed death twice in the same 24-hour period."

    if run == 2:
        "She lays back on the grass, next to Julian, her gaze going up to the stars in the sky."
    if not flowers.flower2:
        delilah_thoughts "Several feet above me, another nearly identical glowing flower dangles on the edge of a tree branch."
        # delilah_thoughts "Several feet above her, another nearly identical glowing flower dangles on the edge of a tree branch."
    if not flowers.flower2:
        if not solves.loop2:
            $ puzzles.loop2 = True # unlock puzzle
            call screen flower_glitch
        else:
            call screen flower2_pick
        # delilah "After he dies, Delilah notices in the tree above them is one of the glowing flowers on a branch. The player is presented with the choice to climb the tree and grab the flower. After they do, Delilah falls from the tree, bashing her neck against the rocks below. She can't move. Her mom calls out to her while Delilah tries to scream but finds herself unable to. With the two flowers in her hand, she is able to rollback in time to the start of the game with a new loop option."
        # delilah "After he dies, Delilah notices in the tree above them is one of the glowing flowers on a branch. The player is presented with the choice to climb the tree and grab the flower. After they do, Delilah falls from the tree, bashing her neck against the rocks below. She can't move. Her mom calls out to her while Delilah tries to scream but finds herself unable to. With the two flowers in her hand, she is able to rollback in time to the start of the game with a new loop option." (callback = functools.partial(inctime, fnum=2))
    else:
        pass
    $ phase = 0
    return