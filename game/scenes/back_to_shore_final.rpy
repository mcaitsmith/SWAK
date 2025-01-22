# The script of the game goes in this file.

label back_to_shore_final:

    show bg scene3 with dissolve

    call incphase from _call_incphase

    "8 PM"
    pause 1.0

    delilah_thoughts_run4 "By the time I reach the lake shore, Julian is already standing there with an adorable smile on his face."
    show julian neutral onlayer characters at center:
        zoom 1.0
    pause 1.0
    julian_run4 "Back so soon?"
    delilah_run4 "Got the third flower."
    julian_run4 "Nicely done! Where was it."
    delilah_run4 "My brother had it. But to get it I had to tell him our parents were getting a divorce. It really messed with his head."
    julian_run4 "Oh, I'm so sorry, is he okay?"
    delilah_run4 "Yeah, he is now that everything reset but he wasn't when I told him."
    julian_run4 "Delilah, I'm so sorry. I would never have asked you to do that if I knew."
    delilah_run4 "It's fine. Like I said, it's like it never happened now. He doesn't remember it."
    julian_run4 "Yeah, but you do. I'm sorry for that."
    delilah_run4 "You don't have to apologize, Julian. Let's focus on getting you home. Now, where to start with that last flower?"
    julian_run4 "I'm not sure. It could be anywhere."
    pause 1.0
    delilah_thoughts_run4 "I notice something glowing in his jacket pocket."
    julian_run4 "What?"
    delilah_run4 "Is that the last flower?"
    julian_run4 "No."
    julian_run4 "Yes."
    delilah_run4 "Why did you lie?"
    julian_run4 "I just...I'm not ready to go yet."
    delilah_run4 "Not ready?! You're dying!"
    julian_run4 "I know but...I'm worried about you..."
    delilah_run4 "Oh, Julian."
    julian_run4 "I know things have been really tough for you right now. I want to be there for you for it. I'm frustrated because I physically can't."
    delilah_run4 "We just met..."
    julian_run4 "I know but...I still care. You're cooler than anyone I know."
    delilah_run4 "You live with your grandparents."
    delilah_thoughts_run4 "I laugh."
    delilah_run4 "You don't know many people."
    julian_run4 "Fair. Even so. I wish we could still see each other."
    delilah_run4 "Maybe we can."
    julian_run4 "What do you mean?"
    delilah_run4 "Well, I could just...throw these away. We'd forget about them and spend a bit more time together."
    julian_run4 "But then...you'd be stuck here too."
    delilah_run4 "There are worse fates."
    julian_run4 "Only if you want it."

    call incphase from _call_incphase_1 # should end up at totality for final choice

    menu:
        delilah " " (callback = functools.partial(inctime))
        "{color=#0ff}Give Julian the flowers{/color}":
            delilah_thoughts_run4 "Give Julian the flowers"
            # at this point the 3 flowers show up glitched

            if not flowers.flower4 and not solves.loop4:
                show flower_glitch_image_final onlayer characters
            else:
                hide flower_glitch_image_final onlayer characters
                    # call screen flower_glitch
            if not flowers.flower4 and not solves.loop4:
                delilah_thoughts_run4 "Huh...it looks strange. Staticky."
            else:
                hide flower_glitch_image_final onlayer characters

            # puzzle hints
            if not flowers.flower4:
                if not flowers.flower4 and puzzles.loop4 and not solves.loop4 and hints.loop4_1:
                    delilah_thoughts_run4 "I've been seeing glitched-up ghosts of Julian appearing where my family should be. Creepy."
                if not flowers.flower4 and puzzles.loop4 and not solves.loop4 and hints.loop4_2:
                    delilah_thoughts_run4 "Their words are the same but their identities are all garbled. If only I could REMEMBER who they really are..."
                if not flowers.flower4 and puzzles.loop4 and not solves.loop4 and hints.loop4_3:
                    delilah_thoughts_run4 "Those glitched-up Julians probably need to get fixed in time and space, like I did with the moon. But how?"
                if not flowers.flower4 and puzzles.loop4 and not solves.loop4:
                    menu:
                        narrator "Need a hint?" (callback = functools.partial(inctime))
                        "Yes" if not hints.loop4_1 and not flowers.flower4:
                            if not flowers.flower4 and puzzles.loop4 and not solves.loop4:
                                delilah_thoughts_run4 "I've been seeing glitched-up ghosts of Julian appearing where my family should be. Creepy."
                                $ hints.loop4_1 = True
                        "Get another hint" if hints.loop4_1 and not hints.loop4_2 and not flowers.flower4:
                            if not flowers.flower4 and puzzles.loop4 and not solves.loop4:
                                delilah_thoughts_run4 "Their words are the same but their identities are all garbled. If only I could REMEMBER who they really are..."
                                $ hints.loop4_2 = True
                        "Get final hint" if hints.loop4_2 and not hints.loop4_3 and not flowers.flower4:
                            if not flowers.flower4 and puzzles.loop4 and not solves.loop4:
                                delilah_thoughts_run4 "Those glitched-up Julians probably need to get fixed in time and space, like I did with the moon. But how?"
                                $ hints.loop4_3 = True
                        "No" if not hints.loop4_3 and not flowers.flower4:
                            pass
                        "Pick the flower anyway" if not flowers.flower4:
                            hide flower_glitch_image_final onlayer characters
                            if not flowers.flower4 and puzzles.loop4 and not solves.loop4:
                                $ skip_puzzle4 = True
                            if not flowers.flower4 and puzzles.loop4 and not solves.loop4:
                                call screen flower4_glitch_pick
                else:
                    hide flower_glitch_image_final onlayer characters
            else:
                hide flower_glitch_image_final onlayer characters

            if not flowers.flower4:
                if not solves.loop4:
                    $ puzzles.loop4 = True # unlock puzzle
                    call screen flower_glitch_final
                    hide flower_glitch_image_final onlayer characters

                else:
                    call screen flower4_pick

            $ config.rollback_enabled = False # prevent rollback from here
            $ renpy.choice_for_skipping() # prevent skipping
            $ _skipping = False

            delilah_run4 "What am I thinking...I can't keep you here, Julian."
            julian_run4 "I know...it's a nice thought, but we should both face the music. Go back to our lives."
            delilah_run4 "Aside from everything that sucked...I really liked meeting you."
            delilah_thoughts_run4 "I lean closer to him."
            pause 1.0
            # show kiss CG
            $ flowers.flower4 = False
            $ flowers.flower3 = False
            $ flowers.flower2 = False
            $ flowers.flower1 = False
            delilah_thoughts_run4 "Julian stands there completely frozen, holding the flowers."
            julian_run4 "That was...cool..."
            delilah_thoughts_run4 "I laugh."
            delilah_run4 "Yeah. Goodbye, Julian."
            hide julian onlayer characters
            with { "characters" : Dissolve(3.0) }
            pause 1.0
            delilah_thoughts_run4 "He fades into thin air and finally disappears completely."
            pause 2.0
            delilah_thoughts_run4 "I'm left standing here. Just me and the sound of the waves splashing along the lakeshore."
            pause 3.0
            sandra_run4 "Delilah!"
            delilah_thoughts_run4 "I hear Mom call from the front yard."
            pause 1.0
            show bg black
            with { "master" : Dissolve(3.0) }
            delilah_thoughts_run4 "I turn away from the lake, ready to be with my family."

            # hide julian onlayer characters with dissolve
            # jump open_door
        "{color=#0ff}Toss the flowers in the lake{/color}":
            delilah_thoughts_run4 "Toss the flowers in the lake"
            # have a few are you sure choices
            delilah_run4 "I could do for a couple more go arounds."
            julian_run4 "See you around then."

            # delilah_thoughts_run4 "I lean in closer to him."
            # (Show image of kiss)

            $ config.rollback_enabled = False # prevent rollback from here
            $ renpy.choice_for_skipping() # prevent skipping
            $ _skipping = False
            $ flowers.flower3 = False
            $ flowers.flower2 = False
            $ flowers.flower1 = False
            hide julian onlayer characters
            show bg black
            with { "master" : Dissolve(3.0) }
            delilah_thoughts_run4 "As I release the flowers into the water, they're pulled under by the ripples of the water and slowly disappear."

    return

            # hide cody onlayer characters with dissolve
            # jump back_to_shore_final

    # delilah "At the shore, Julian is standing there waiting for you to meet with him. Deliah tells him about the conversation she just had with Cody, how difficult it was. Julian feels for her and apologizes for putting her through that. This confuses Delilah since his life is at stake. Sort of dwarfs in comparison. Julian doesn't see it that way. His martyr complex comes through in this moment."
    # delilah "They discuss that there is only ONE flower left to find. Delilah is confounded by where it could be. Julian acts suspicious, clutching his shirt pocket. Delilah notices that it's glowing and asks what he has."
    # delilah "Julian admits to having the flower and apologizes. He admits that he's enjoyed being here with her and wants to be there to comfort her for the family crisis that she's about to endure when she goes home."

    # # delilah takes flower
    # if not flowers.flower4:
    #     delilah "Delilah takes the flower" (callback = functools.partial(inctime, fnum=4))
    # else:
    #     pass

    # call incphase from _call_incphase_1 # should end up at totality for final choice

    # delilah "Delilah has three possible choices she can follow from here:"
    # menu:
    #     delilah "Dialogue choice" (callback = functools.partial(inctime))
    #     "Ending 1":
    #         delilah "Delilah can force Julian to take the flowers and go home, resulting in a heartfelt moment in which they tearfully say goodbye and kiss. The story ends with her going to take care of her brother and mom as they endure the crisis that lies ahead."
    #         hide julian onlayer characters with dissolve
    #         show bg black with dissolve
    #         $ endings.ending1 = True
    #         return
    #     "Ending 2":
    #         delilah "Delilah can embrace Julian with the flowers and follow him back to his world where she will suddenly be trapped in a time loop there."
    #         # hide delilah with dissolve
    #         show bg black with dissolve
    #         $ endings.ending2 = True
    #         return
    #     "Ending 3":
    #         delilah "Delilah can agree to remain in the time loop with him as the game simply restarts and the time loop begins again."
    #         # for this ending instead of actually restarting just show the intro again in the credit sequence
    #         show bg black with dissolve
    #         $ endings.ending3 = True
    #         return