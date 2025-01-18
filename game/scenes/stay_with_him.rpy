# The script of the game goes in this file.

label stay_with_him:

    delilah_run2 "Okay. I'll stay with you."

    delilah_thoughts_run2 "I sit down on a patch of grass just above his head."
    # delilah_thoughts "She sits down on a patch of grass just above his head. "
    pause 1.0

    boy_run2 "Thank you."

    call incphase from _call_incphase_13
    
    delilah_run2 "So...what do you want to do to fill the time? It could be a while till you, y'know..."
    boy_run2 "Hmm. Why don't you tell me about yourself? What's your name? What brings you out here to this fine patch of jagged rocks?"
    delilah_thoughts_run2 "She chuckles painfully." # replace
    delilah_run2 "I'm Delilah. Uh, just here on a short weekend trip with the family."
    boy_run2 "Right, and that lovely creature I saw you with before must be your sister then?"
    delilah_run2 "Mother and where were you?? I went for help and you disappeared!"
    boy_run2 "Oh, y'know, I was halfway between lakes. There and not there."
    delilah_run2 "How did you get like...this?"
    boy_run2 "Beats the hell out of me. Like I said, I was out picking flowers and ended up here."
    delilah_run2 "Picking flowers? Really?"
    boy_run2 "Yeah, for my grandparents' flower shop. Is there something wrong with that?"
    delilah_run2 "No, no, it's just- I wouldn't ever have guessed."
    boy_run2 "They're probably worried sick about me. Say, you haven't heard of a 'Schneider's Happy Petals' have you?"
    delilah_run2 "Nothing like that around here."
    boy_run2 "Wow. Then I must really be far from home."
    delilah_thoughts_run2 "He starts coughing violently."
    boy_run2 "Ouch."
    delilah_run2 "Are you okay?"
    boy_run2 "Yeah...No...Don't worry about it..."
    delilah_run2 "You're...dying again, aren't you?"
    boy_run2 "It sure feels like it. But, hey, at least I wasn't alone this time."
    delilah_thoughts_run2 "I look up and down his body for any sign of injury, none to be found."
    # delilah_thoughts "She looks up and down his body for any sign of injury, none to be found."
    boy_run2 "If you come around this way again...if I end up here dying again...you promise you'll wait it out with me again?"
    delilah_run2 "Yeah...yeah I promise."
    boy_run2 "Rad..."
    delilah_run2 "Hey, you never told me your name."
    julian_run2 "Oh, how rude of me...uh, it's Julian."
    delilah_thoughts_run2 "He tilts his head back and the light drains from his eyes."
    hide julian onlayer characters with dissolve

    call incphase from _call_incphase_14

    delilah_thoughts_run2 "He's gone again. I stare at his body, trying to process that I've now witnessed death twice in the same 24-hour period."
    # delilah_thoughts "He's gone again. Delilah stares at his body, trying to process that she has now witnessed death twice in the same 24-hour period."

    if run == 2:
        "{color=#f00}She lays back on the grass, next to Julian, her gaze going up to the stars in the sky.{/color}"
    if not flowers.flower2:
        delilah_thoughts_run2 "Several feet above me, another nearly identical glowing flower dangles on the edge of a tree branch."
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