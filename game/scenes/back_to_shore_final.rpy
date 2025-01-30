# The script of the game goes in this file.

label back_to_shore_final:

    show bg scene3 with dissolve

    call incphase from _call_incphase

    time_centered "8 PM"
    pause 1.0

    delilah_thoughts_run4 happy "By the time I reach the lake shore, Julian is already standing there with an adorable smile on his face."
    show julian happy onlayer characters at center:
        zoom 1.0
    pause 1.0
    julian_run4_d happy "Back so soon?"
    delilah_run4 neutral "Got the third flower."
    show julian neutral onlayer characters
    julian_run4_d "Nicely done! Where was it."
    delilah_run4 worried "My brother had it. But to get it I had to tell him our parents were getting a divorce. It really messed with his head."
    show julian worried onlayer characters
    julian_run4_d "Oh, I'm so sorry, is he okay?"
    delilah_run4 worried "Yeah, he is now that everything reset but he wasn't when I told him."
    julian_run4_d "Delilah, I'm so sorry. I would never have asked you to do that if I knew."
    delilah_run4 happy "It's fine. Like I said, it's like it never happened now. It was my choice, plus he doesn't even remember it."
    show julian neutral onlayer characters
    julian_run4_d "Yeah, but you do. I'm sorry for that."
    delilah_run4 "You don't have to apologize, Julian. Let's focus on getting you home. Now, where to start with that last flower?"
    julian_run4_d "I'm not sure. It could be anywhere."
    # pause 1.0
    delilah_thoughts_run4 neutral "I notice something glowing in his jacket pocket."
    julian_run4_d "What?"
    delilah_run4 worried "Is that the last flower?"
    show julian worried onlayer characters
    julian_run4_d "No."
    show julian happy onlayer characters
    julian_run4_d "Yes."
    delilah_run4 angry "Why did you lie?"
    show julian worried onlayer characters
    julian_run4_d "I just...I'm not ready to go yet."
    delilah_run4 "Not ready?! You're dying!"
    julian_run4_d "I know but...I'm worried about you..."
    delilah_run4 happy "Oh, Julian."
    julian_run4_d "I know things have been really tough for you right now. I want to be there for you for it. I'm frustrated because I physically can't."
    delilah_run4 "We just met..."
    show julian neutral onlayer characters
    julian_run4_d "I know but...I still care. You're cooler than anyone I know."
    delilah_run4 laugh "You live with your grandparents."
    # delilah_thoughts_run4 "I laugh."
    delilah_run4 "You don't know many people."
    show julian happy onlayer characters
    julian_run4_d "Fair. Even so. I wish we could still see each other."
    delilah_run4 happy "Maybe we can."
    show julian neutral onlayer characters
    julian_run4_d "What do you mean?"
    delilah_run4 "Well, I could just...throw these away. We'd forget about them and spend a bit more time together."
    julian_run4_d "But what would even happen? Would we forget about each other?"
    delilah_run4 "I'll find you again."
    show julian worried onlayer characters
    julian_run4_d "You'll be stuck here, you'll be trapped here in this moment with me."
    delilah_run4 "There are worse fates."
    julian_run4_d "No, Del, think really carefully about this. Are you sure it's what you want?"

    call incphase from _call_incphase_1 # should end up at totality for final choice

    if not hints.hint7 and choose_timeline: # shows up if on second runthrough
        # play animation to indicate new hint
        $ renpy.play("orex_sfx_sparkle.ogg")
        $ hintlist.list.append(hint_7)
        $ hints.hint7 = True
        $ hints.seen_hint = False

    menu:
        delilah " " (callback = functools.partial(inctime))
        "{color=#0ff}Give Julian the flowers{/color}" if solves.loop2 and solves.loop3_1 and solves.loop3_2 and solves.loop3_3 and solves.loop4:
            delilah_thoughts_run4 "Give Julian the flowers"
            # at this point the 3 flowers show up glitched

            # if not flowers.flower4 and not solves.loop4:
            #     show flower_glitch_image_final onlayer characters
            # else:
            #     hide flower_glitch_image_final onlayer characters
            #         # call screen flower_glitch
            # if not flowers.flower4 and not solves.loop4:
            #     delilah_thoughts_run4 "Huh...it looks strange. Staticky."
            # else:
            #     hide flower_glitch_image_final onlayer characters

            # # puzzle hints
            # if not flowers.flower4:
            #     if not flowers.flower4 and puzzles.loop4 and not solves.loop4 and hints.loop4_1:
            #         delilah_thoughts_run4 "I've been seeing glitched-up ghosts of Julian appearing where my family should be. Creepy."
            #     if not flowers.flower4 and puzzles.loop4 and not solves.loop4 and hints.loop4_2:
            #         delilah_thoughts_run4 "Their words are the same but their identities are all garbled. If only I could REMEMBER who they really are..."
            #     if not flowers.flower4 and puzzles.loop4 and not solves.loop4 and hints.loop4_3:
            #         delilah_thoughts_run4 "Those glitched-up Julians probably need to get fixed in time and space, like I did with the moon. But how?"
            #     if not flowers.flower4 and puzzles.loop4 and not solves.loop4:
            #         menu:
            #             narrator "Need a hint?" (callback = functools.partial(inctime))
            #             "Yes" if not hints.loop4_1 and not flowers.flower4:
            #                 if not flowers.flower4 and puzzles.loop4 and not solves.loop4:
            #                     delilah_thoughts_run4 "I've been seeing glitched-up ghosts of Julian appearing where my family should be. Creepy."
            #                     $ hints.loop4_1 = True
            #             "Get another hint" if hints.loop4_1 and not hints.loop4_2 and not flowers.flower4:
            #                 if not flowers.flower4 and puzzles.loop4 and not solves.loop4:
            #                     delilah_thoughts_run4 "Their words are the same but their identities are all garbled. If only I could REMEMBER who they really are..."
            #                     $ hints.loop4_2 = True
            #             "Get final hint" if hints.loop4_2 and not hints.loop4_3 and not flowers.flower4:
            #                 if not flowers.flower4 and puzzles.loop4 and not solves.loop4:
            #                     delilah_thoughts_run4 "Those glitched-up Julians probably need to get fixed in time and space, like I did with the moon. But how?"
            #                     $ hints.loop4_3 = True
            #             "No" if not hints.loop4_3 and not flowers.flower4:
            #                 pass
            #             "Pick the flower anyway" if not flowers.flower4:
            #                 hide flower_glitch_image_final onlayer characters
            #                 if not flowers.flower4 and puzzles.loop4 and not solves.loop4:
            #                     $ skip_puzzle4 = True
            #                 if not flowers.flower4 and puzzles.loop4 and not solves.loop4:
            #                     call screen flower4_glitch_pick
            #     else:
            #         hide flower_glitch_image_final onlayer characters
            # else:
            #     hide flower_glitch_image_final onlayer characters

            # if not flowers.flower4:
            #     if not solves.loop4:
            #         $ puzzles.loop4 = True # unlock puzzle
            #         call screen flower_glitch_final
            #         hide flower_glitch_image_final onlayer characters

            #     else:
            #         call screen flower4_pick

            show julian neutral onlayer characters
            delilah_thoughts_run4 "I reach out to take the final flower."

            if not flowers.flower4:

                show julian blur onlayer characters with dissolve

            if not flowers.flower4:
                call screen flower4_pick

            $ config.rollback_enabled = False # prevent rollback from here
            $ renpy.choice_for_skipping() # prevent skipping
            $ _skipping = False

            show julian neutral onlayer characters with dissolve

            stop music fadeout 1.0

            delilah_run4 "What am I thinking...I can't keep you here, Julian."
            julian_run4_d "I know...it's a nice thought, but we should both face the music. Go back to our lives."
            
            play music endingmusic
            
            delilah_run4 "Aside from everything that sucked...I really liked meeting you."
            julian_run4_d "I don't think I'll ever be able to forget you for as long as I live."
            delilah_thoughts_run4 "I lean closer to him."
            pause 1.0
            # show kiss CG
            show kiss_cg onlayer cg with Dissolve(3.0)
            $ flowers.flower4 = False
            $ flowers.flower3 = False
            $ flowers.flower2 = False
            $ flowers.flower1 = False
            show flower1 onlayer characters:
                xalign 0.5
                yalign 0.625
            show flower2 onlayer characters:
                xalign 0.515
                yalign 0.75
                rotate 20
            show flower3 onlayer characters:
                xalign 0.485
                yalign 0.75
                rotate -20
            show flower4 onlayer characters:
                xalign 0.5
                yalign 0.775
            $ renpy.pause()
            hide kiss_cg onlayer cg with Dissolve(3.0)

            delilah_thoughts_run4 "Julian stands there completely frozen, holding the flowers."
            julian_run4_d "That was...cool..."
            delilah_thoughts_run4 "I laugh."
            delilah_run4 "Yeah. I don't think I'll be able to forget you either, Julian."
            hide julian onlayer characters
            hide flower1 onlayer characters
            hide flower2 onlayer characters
            hide flower3 onlayer characters
            hide flower4 onlayer characters
            with { "characters" : Dissolve(3.0) }
            pause 3.0
            delilah_thoughts_run4 "He fades into thin air, his smile being the last thing to disappear completely."
            # pause 2.0
            delilah_thoughts_run4 "I'm left standing here. Just me and the sound of the waves splashing along the lakeshore. It's calm."
            delilah_thoughts_run4 "I turn to look at the house, thinking about all of the things that I'll have to face when I get there. My family is still holding together by a thread."
            # pause 3.0
            sandra_run4_d "Delilah!"
            delilah_thoughts_run4 "I hear Mom call from the front yard."
            # pause 1.0
            # show bg black
            # with { "master" : Dissolve(3.0) }
            delilah_thoughts_run4 "It'll be difficult, but I'll be able to handle it. Knowing that Julian is out there somewhere will make it all easier."

            show bg black with Dissolve(3.0)

            # jump to credits here
            $ true_ending = True

            # hide julian onlayer characters with dissolve
            # jump open_door
        "{color=#0ff}Toss the flowers in the lake{/color}":
            delilah_thoughts_run4 "Toss the flowers in the lake"
            # have a few are you sure choices
            show black behind bg
            show julian neutral onlayer characters
            delilah_run4 "I could do for a couple more go arounds."
            julian_run4_d "You're sure?"
            delilah_run4 "Yeah. I'm sure. Besides, who's to say this is the first time we've done this?"
            show julian happy onlayer characters
            julian_run4_d "I suppose it's possible. How would we remember if we had." (callback = functools.partial(inctime))
            show julian neutral onlayer characters
            delilah_run4 "I'd choose to stay with you every time." (callback = functools.partial(inctime,g9=True))

            # delilah_thoughts_run4 "I lean in closer to him."
            # (Show image of kiss)

            if not solves.loop4:
            # if not renpy.is_skipping() and not solves.loop4:
                $ flowers.flower3 = False
            # else:
            #     $ config.rollback_enabled = True
            if not solves.loop4:
            # if not renpy.is_skipping() and not solves.loop4:
                $ flowers.flower2 = False
            # else:
            #     $ config.rollback_enabled = True
            if not solves.loop4:
            # if not renpy.is_skipping() and not solves.loop4:
                $ flowers.flower1 = False
            # else:
            #     $ config.rollback_enabled = True
            if not solves.loop4:
            # # if not renpy.is_skipping() and not solves.loop4:
                $ config.rollback_enabled = False # prevent rollback from here
            # else:
            #     $ config.rollback_enabled = True

            # if not renpy.is_skipping() and not solves.loop4:
            #     $ renpy.choice_for_skipping() # prevent skipping
            # else:
            #     $ config.rollback_enabled = True
            # if not renpy.is_skipping() and not solves.loop4:
            #     $ _skipping = False
            # else:
            #     $ config.rollback_enabled = True
            # if not renpy.is_skipping():
            if not solves.loop4:
                show bg scene3 glitch
            if not solves.loop4 and not hints.hint2:
                $ hintlist.list.append(hint_2)
                $ renpy.play("orex_sfx_sparkle.ogg")
                # play animation to indicate new hint
                $ hints.hint2 = True
                $ hints.seen_hint = False
            hide julian onlayer characters
            with { "characters" : Dissolve(3.0) }
            # if not renpy.is_skipping():
            if not solves.loop4:
                delilah_thoughts_run4 "As I release the flowers into the water, they're pulled under by the ripples of the water and slowly disappear." (callback = functools.partial(inctime,checkskip=True))
            # else:
            # if renpy.is_skipping() and not solves.loop4:
            #     $ renpy.play("orex_sfx_sparkle.ogg") # solved!
            # if renpy.is_skipping() and not solves.loop4:
            #     $ solves.loop4 = True
            #     $ hintlist.list.append("{b}Sealed glitch " + str(sum([solves.loop2,solves.loop3_1,solves.loop3_2,solves.loop3_3,solves.loop4])) + " of 5{/b}\n")
            #     $ hints.seen_hint = False

            if not solves.loop4:
                delilah_thoughts_run4 "Am I refusing to let go of Julian? Or am I running from things I need to face?" (callback = functools.partial(inctime,checkskip=True))
            show bg scene3
            # $ renpy.choice_for_skipping() # prevent skipping
            # $ _skipping = False

            # if solves.loop4:
            #     if not hints.hint7:
            #         # play animation to indicate new hint
            #         $ renpy.play("orex_sfx_sparkle.ogg")
            #         $ hintlist.list.append(hint_7)
            #         $ hints.hint7 = True
            #         $ hints.seen_hint = False
            if solves.loop4:
                $ config.rollback_enabled = True

            if not solves.loop4:
                if not hints.hint6:
                    # play animation to indicate new hint
                    $ renpy.play("orex_sfx_sparkle.ogg")
                    $ hintlist.list.append(hint_6)
                    $ hints.hint6 = True
                    $ hints.seen_hint = False

            menu:
                delilah " " (callback = functools.partial(inctime,g10=True))
                "Restart loop":
                    pass
            # show screen endscreenqr with dissolve
            # $ renpy.pause()
            $ renpy.choice_for_skipping() # prevent skipping
            $ _skipping = False
            hide bg scene3 with dissolve
            # if not solves.loop4:
            $ restart_vars = True # return to beginning loop with vars re-initialized (except for glitches)
            $ sealed_glitches = str(sum([solves.loop2,solves.loop3_1,solves.loop3_2,solves.loop3_3,solves.loop4]))
            "{b}Sealed glitches [sealed_glitches] of 5{/b}"
            "Something's preventing you from moving forward.\nThe anomaly that sent Julian to this world is bleeding across timelines.\n\nYou've now unlocked timeline select. Explore different branches and outcomes to find and seal whatever's corrupting the timelines."
            "[hint_7]"
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