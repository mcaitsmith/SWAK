# The script of the game goes in this file.

label stay_with_him:

    delilah_run2 "Okay. I'll stay with you."

    delilah_thoughts_run2 "I sit down on a patch of grass just above his head."
    pause 1.0

    boy_run2_d "Thank you."

    call incphase from _call_incphase_13
    
    delilah_run2 "So...what do you want to do to fill the time? It could be a while till you, y'know..."
    boy_run2_d "Hmm. Why don't you tell me about yourself? What's your name? What brings you out here to this fine patch of jagged rocks?"
    delilah_thoughts_run2 "I chuckle painfully." # replace
    delilah_run2 "I'm Delilah. Uh, just here on a short weekend trip with the family."
    boy_run2_d "Right, and that lovely creature I saw you with before must be your sister then?"
    delilah_run2 "Mother and where were you?? I went for help and you disappeared!"
    boy_run2_d "Oh, y'know, I was halfway between lakes. There and not there."
    delilah_run2 "How did you get like...this?"
    boy_run2_d "Beats the hell out of me. Like I said, I was out picking flowers and ended up here."
    delilah_run2 "Picking flowers? Really?"
    boy_run2_d "Yeah, for my grandparents' flower shop. Is there something wrong with that?"
    delilah_run2 "No, no, it's just- I wouldn't ever have guessed."
    boy_run2_d "They're probably worried sick about me. Say, you haven't heard of a 'Schneider's Happy Petals' have you?"
    delilah_run2 "Nothing like that around here."
    boy_run2_d "Wow. Then I must really be far from home."
    delilah_thoughts_run2 "He starts coughing violently."
    boy_run2_d "Ouch."
    delilah_run2 "Are you okay?"
    boy_run2_d "Yeah...No...Don't worry about it..."
    delilah_run2 "You're...dying again, aren't you?"
    boy_run2_d "It sure feels like it. But, hey, at least I wasn't alone this time."
    delilah_thoughts_run2 "I look up and down his body for any sign of injury, none to be found."
    boy_run2_d "If you come around this way again...if I end up here dying again...you promise you'll wait it out with me again?"
    delilah_run2 "Yeah...yeah I promise."
    boy_run2_d "Rad..."
    delilah_run2 "Hey, you never told me your name."
    julian_run2_d "Oh, how rude of me...uh, it's Julian."
    delilah_thoughts_run2 "He tilts his head back and the light drains from his eyes."
    # hide julian onlayer characters with dissolve
    show julian glitch onlayer characters with dissolve
    hide julian glitch onlayer characters with Dissolve(3.0)

    call incphase from _call_incphase_14
    time_centered "9 PM" (callback = functools.partial(inctime))
    pause 1.0

    delilah_thoughts_run2 "He's gone again. I stare at his body, trying to process that I've now witnessed death twice in the same 24-hour period."

    if run == 2:
        "{color=#f00}She lays back on the grass, next to Julian, her gaze going up to the stars in the sky.{/color}"
    if not flowers.flower2:
        delilah_thoughts_run2 "Several feet above me, another nearly identical glowing flower dangles on the edge of a tree branch."
        pause 1.0
    if not flowers.flower2:
        if run == 2:
            "{color=#f00}Something inside Delilah compels her to get that glowing flower.\nThe way Julian mentioned gathering them before he ended up here\nand the way she suddenly was able to travel backwards by getting the first one,\nshe feels that if she gets another that maybe she'll get an answer as to why this is happening.{/color}"
    if not flowers.flower2:
        if run == 2:
            "{color=#f00}She used to climb trees all the time as a kid.\nHer dad would hoist her up and she'd cling to a branch like a koala.\nShe thinks of this while planting her foot onto a knot on the side of its trunk. Higher and higher she reaches, farther and farther the ground becomes.{/color}"
    if not flowers.flower2:
        delilah_thoughts_run2 "I inch my way across the tree's feeble branch and reach for the flower..."
    # if not flowers.flower2 and not solves.loop2:
    #     show flower_glitch_image
    # else:
    #     hide flower_glitch_image
    #         # call screen flower_glitch
    # if not flowers.flower2 and not solves.loop2:
    #     delilah_thoughts_run2 "Huh...it looks strange. Staticky."
    # else:
    #     hide flower_glitch_image

    # # puzzle hints
    # if not flowers.flower2:
    #     if not flowers.flower2 and puzzles.loop2 and not solves.loop2 and hints.loop2_1:
    #         delilah_thoughts_run2 "That staticky glitch...there's something {i}wrong{/i} about it. Have I seen that static somewhere before?"
    #     if not flowers.flower2 and puzzles.loop2 and not solves.loop2 and hints.loop2_2:
    #         delilah_thoughts_run2 "I don't know what's going on, but I feel like that glitch doesn't belong in this world. Something's {i}pulling{/i} it here. Maybe if I seal it off somewhere else the flower will become real again."
    #     if not flowers.flower2 and puzzles.loop2 and not solves.loop2 and hints.loop2_3:
    #         delilah_thoughts_run2 "Is there a way to SKIP past points in time that are glitched? Wait, what am I talking about? There's no such thing as time travel."
    #     if not flowers.flower2 and puzzles.loop2 and not solves.loop2:
    #         menu:
    #             narrator "Need a hint?" (callback = functools.partial(inctime))
    #             "Yes" if not hints.loop2_1 and not flowers.flower2:
    #                 if not flowers.flower2 and puzzles.loop2 and not solves.loop2:
    #                     delilah_thoughts_run2 "That staticky glitch...there's something {i}wrong{/i} about it. Have I seen that static somewhere before?"
    #                     $ hints.loop2_1 = True
    #                 # if puzzles.loop2 and not solves.loop2:
    #                 #     jump pick_flower2
    #             "Get another hint" if hints.loop2_1 and not hints.loop2_2 and not flowers.flower2:
    #                 if not flowers.flower2 and puzzles.loop2 and not solves.loop2:
    #                     delilah_thoughts_run2 "I don't know what's going on, but I feel like that glitch doesn't belong in this world. Something's {i}pulling{/i} it here. Maybe if I seal it off somewhere else the flower will become real again."
    #                     $ hints.loop2_2 = True
    #                 # if not flowers.flower2:
    #                 #     jump pick_flower2
    #             "Get final hint" if hints.loop2_2 and not hints.loop2_3 and not flowers.flower2:
    #                 if not flowers.flower2 and puzzles.loop2 and not solves.loop2:
    #                     delilah_thoughts_run2 "Is there a way to SKIP past points in time that are glitched? Wait, what am I talking about? There's no such thing as time travel."
    #                     $ hints.loop2_3 = True
    #                 # if not flowers.flower2:
    #                 #     jump pick_flower2
    #             "No" if not hints.loop2_3 and not flowers.flower2:
    #                 pass
    #                 # if not flowers.flower2:
    #                 #     jump pick_flower2
    #             "Pick the flower anyway" if not flowers.flower2:
    #                 # if not flowers.flower2 and puzzles.loop2 and not solves.loop2:
    #                 hide flower_glitch_image
    #                 if not flowers.flower2 and puzzles.loop2 and not solves.loop2:
    #                     $ skip_puzzle2 = True
    #                 if not flowers.flower2 and puzzles.loop2 and not solves.loop2:
    #                     call screen flower2_glitch_pick
    #     else:
    #         hide flower_glitch_image
    # else:
    #     hide flower_glitch_image

    if not flowers.flower2:
        call screen flower2_pick

    # if not flowers.flower2:
    #     if not solves.loop2:
    #         $ puzzles.loop2 = True # unlock puzzle
    #         call screen flower_glitch
    #         hide flower_glitch_image

    #     else:
    #         call screen flower2_pick

    if flowers.flower2 and not config.rollback_enabled:
        $ renpy.choice_for_skipping()
    if flowers.flower2 and not config.rollback_enabled:
        $ _skipping = False
    if flowers.flower2 and not config.rollback_enabled:
        delilah_thoughts_run2 "Once it's in my hand I immediately feel different."
    else:
        $ config.rollback_enabled = True
    if flowers.flower2 and not config.rollback_enabled:
        delilah_thoughts_run2 "Something emanates from the petals of the flower into my mind."
    else:
        $ config.rollback_enabled = True
    if flowers.flower2 and not config.rollback_enabled:
        delilah_thoughts_run2 "I'm able to remember things in other ways and somehow remember things that would have been."
    else:
        $ config.rollback_enabled = True
    if flowers.flower2 and not config.rollback_enabled:
        if run == 2:
            "{color=#f00}As soon as she feels this, the branch cracks under her and the ground throws itself at her.{/color}"
    else:
        $ config.rollback_enabled = True
    if flowers.flower2 and not config.rollback_enabled:
        show bg black with dissolve
    else:
        $ config.rollback_enabled = True
    if flowers.flower2 and not config.rollback_enabled:
        if run == 2:
            "{color=#f00}Her neck slams against the rocks and audibly snaps.{/color}"
    else:
        $ config.rollback_enabled = True
    if flowers.flower2 and not config.rollback_enabled:
        if run == 2:
            "{color=#f00}She lays there facing Julian, staring into his eyes.\nAs the light in her fades she notices how many colors can be seen in his irises.{/color}"
    else:
        $ config.rollback_enabled = True

    if not hints.hint10:
        # play animation to indicate new hint
        $ renpy.play("orex_sfx_sparkle.ogg")
        $ hintlist.list.append(hint_10)
        $ hints.hint10 = True
        $ hints.seen_hint = False
    $ config.rollback_enabled = True # re-enable rollback

    # else:
    #     pass

    $ phase = 0
    return