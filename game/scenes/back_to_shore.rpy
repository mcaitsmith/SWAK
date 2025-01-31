# The script of the game goes in this file.

label back_to_shore:
    # zoom bg plus sfx
    delilah_thoughts_run3 "When I get to the bottom of the hill, Julian is already waiting for me."
    show julian neutral onlayer characters at center with dissolve:
        zoom 1.0
    pause 1.0
    show julian neutral onlayer characters
    julian_run3_d "Back so soon?"
    delilah_run3 happy "After you died, I found this."
    delilah_thoughts_run3 "I hold out the second flower."
    show julian happy onlayer characters
    julian_run3_d "Ah, pretty. Why thank you." # He says dryly. (expression)
    delilah_run3 worried "Yeah, I broke my neck to get it."
    show julian worried onlayer characters
    julian_run3_d "You broke...? Oh, God, I'm so sorry. Why?"
    delilah_run3 neutral "Call it a hunch, but I'm guessing these have something to do with this condition of ours. What do you know about them?"
    show julian serious onlayer characters
    julian_run3_d "These? They're Selene Lillies. Extremely rare luminescent flowers. They're what I was gathering before."
    # add some line around here about how the lilies are rumored to mess with time and space and cause "interference" (or just include in puzzle hint/solution text)
    delilah_run3 "You don't think they have something to do with all of...this?"
    show julian worried onlayer characters
    julian_run3_d "I think that's a bit out there, Delilah. I think it's bizarre, and a bit of a reach. But then again, I've died multiple times in the past twelve hours, so I'm liable to believe whatever you tell me."
    delilah_run3 worried "When I got this second flower I noticed...I don't know...something new. I was suddenly able to see more possible outcomes if that makes sense."
    julian_run3_d "Not really. My 'outcome' has been pretty consistent."
    delilah_run3 "How many flowers did you have before you wound up here?"
    julian_run3_d "Four. Was putting together a bouquet for my folks' shop. Just four Selene Lillies would sell for enough to keep the lights on for a year."
    delilah_run3 "So maybe if we get all four together we can send you home and break the loop?"
    show julian neutral onlayer characters
    julian_run3_d "Couldn't hurt to try, I suppose. We're halfway there already."
    delilah_run3 "Where do you think we should start looking?" 
    show julian worried onlayer characters
    julian_run3_d "That could be tricky. Part of the legend of the Selene lillies is that the only time they appear for you is if you aren't looking for them."
    delilah_run3 neutral "So if we go out searching for them we'll be stuck here forever."
    show julian serious onlayer characters
    julian_run3_d "Exactly."
    delilah_run3 "What do you suggest then?"
    show julian worried onlayer characters
    julian_run3_d "Honestly? Keep going about the loop like normal, try new outcomes, and see if we can stumble upon any new lillies. Think of it like walking backwards with a blindfold on except the entire time I'll be repeatedly dying."
    delilah_run3 "So, I should go be with my mom and brother then?"
    show julian neutral onlayer characters
    julian_run3_d "Is that a problem?"
    delilah_run3 laugh "Sort of. Things have just been really tense lately."
    julian_run3_d "Want to talk about it?"
    menu:
        delilah " " (callback = functools.partial(inctime))
        "{color=#0f0}No. It's not important. I'll deal with it.{/color}":
            delilah_run3 neutral "No. It's not important. I'll deal with it."
            julian_run3_d "If you say so. I'm here if you do want to talk about it later. Not like we're exactly running out of time."
            delilah_run3 "I appreciate it."
            hide julian onlayer characters with dissolve
            $ loop3_investigate = True
            jump open_door
        "{color=#0f0}Open up to him{/color}":
            delilah_thoughts_run3 worried "Open up to him"
            delilah_run3 worried "My little brother has always been a bit of a nightmare, but some stuff happened a few months ago and...I don't know...I can't really look at my mom the same way again."
            julian_run3_d "How so?"
            delilah_run3 "Well, like, you know how when you're a kid your parents are just perfect in every way to you? When you find out that they aren't, or even that they're a bit fucked up, it shatters your world."
            show julian worried onlayer characters
            julian_run3_d "I guess I'm lucky for that then. I lost my folks when I was young, so they'll always get to be perfect to me."
            delilah_run3 happy "Oh, Julian I'm so sorry. I had no idea."
            show julian serious onlayer characters
            julian_run3_d neutral "It was a long time ago...ancient history. I just meant to say that I AM fortunate for that part of it, painful as it may have been."
            delilah_run3 angry "Why do you do that?"
            julian_run3_d "Do what?"
            delilah_run3 "Act like it's okay. You've been doing that this entire time. Even when you're repeatedly dying in agony."
            show julian happy onlayer characters
            julian_run3_d "I don't know if I'd call it 'agony'."
            menu:
                delilah " " (callback = functools.partial(inctime))
                "{color=#0f0}If you say so.{/color}":
                    delilah_run3 neutral "If you say so."
                    show julian neutral onlayer characters
                    julian_run3_d "I do say so. Now. Let's get back to the task at hand..."
                    hide julian onlayer characters with dissolve
                    $ loop3_investigate = True
                    jump open_door
                "{color=#0f0}Call him out{/color}":
                    delilah_thoughts_run3 "Call him out"

                    call incphase from _call_incphase_15

                    delilah_run3 "There you go again! Why do you need to do that?"
                    show julian worried onlayer characters
                    julian_run3_d "Old habits. After I lost my folks, my grandparents took me in. They did their best but, y'know, their age shows pretty often. I take care of them more than they take care of me."
                    delilah_run3 neutral "Does it feel so weird for me to be worried about you?"
                    show julian sad onlayer characters
                    julian_run3_d neutral "In all honesty, yes. I'm not used to it. I don't...talk...to people much. Especially girls who are, y'know...pretty."
                    show julian blush onlayer characters
                    delilah_thoughts_run3 happy "I look at him confused, then smile."
                    julian_run3_d "That was weird to say, sorry."
                    delilah_thoughts_run3 laugh "I laugh."
                    delilah_run3 "Not at all. I guess I just took you for a bit of a casanova initially."
                    julian_run3_d neutral "Me? As if."
                    show julian happy onlayer characters
                    delilah_thoughts_run3 "He snorts nervously."
                    julian_run3_d "Just some kid who works at a flowershop."
                    show julian serious onlayer characters
                    delilah_thoughts_run3 happy "We stare into each others' eyes, holding onto the moment for as long as possible."

                    call incphase from _call_incphase_16
                    show bg scene3 with dissolve
                    time_centered "9 PM" (callback = functools.partial(inctime)) # intentionally skip 8pm for this ending
                    pause 1.0

                    show julian pain onlayer characters
                    delilah_thoughts_run3 worried "Julian's knees start to shake and abruptly fold underneath him."
                    delilah_run3 worried "Julian!"
                    show julian worried onlayer characters
                    delilah_thoughts_run3 "His eyes start to wander around. His arm quickly reaches up and I catch his hand."
                    julian_run3_d "It's happening again..." (callback = functools.partial(inctime))
                    delilah_run3 "Oh God, oh shit, oh no. I'm here! I'm here!" (callback = functools.partial(inctime,g3=True))
                    # start glitch
                    if run == 3 and not solves.loop3_1:
                        show julian puzzle_pain onlayer characters
                    else:
                        show julian pain onlayer characters
                    if run == 3 and not solves.loop3_1 and not hints.hint2:
                        $ hintlist.list.append(hint_2)
                        $ renpy.play("chime.ogg")
                        # play animation to indicate new hint
                        $ hints.hint2 = True
                        $ hints.seen_hint = False
                    if hints.hint2 and not hints.hint5 and not solves.loop3_1 and sum([solves.loop2,solves.loop3_1,solves.loop3_2,solves.loop3_3,solves.loop4]) > 0:
                        $ hintlist.list.append(hint_5)
                        $ renpy.play("chime.ogg")
                        # play animation to indicate new hint
                        $ hints.hint5 = True
                        $ hints.seen_hint = False
                    if run == 3 and not solves.loop3_1:
                        show julian puzzle_happy onlayer characters
                    else:
                        show julian pain onlayer characters
                    if run == 3 and not solves.loop3_1:
                        delilah_thoughts_run3 "He laughs." (callback = functools.partial(inctime,checkskip=True))
                    else:
                        show julian pain onlayer characters
                    if run == 3 and not solves.loop3_1:
                        delilah_run3 "What? What's funny?" (callback = functools.partial(inctime,checkskip=True))
                    else:
                        show julian pain onlayer characters
                    if run == 3 and not solves.loop3_1:
                        julian_run3_d "We talked for so long we forgot to go look for the flowers." (callback = functools.partial(inctime,checkskip=True))
                    else:
                        show julian pain onlayer characters
                    if run == 3 and not solves.loop3_1:
                        delilah_run3 laugh "Oh shit. We did." (callback = functools.partial(inctime,checkskip=True))
                    else:
                        show julian pain onlayer characters
                    if run == 3 and not solves.loop3_1:
                        delilah_thoughts_run3 "I laugh." (callback = functools.partial(inctime,checkskip=True))
                    else:
                        show julian pain onlayer characters
                    if run == 3 and not solves.loop3_1:
                        delilah_run3 "My mom and brother have probably been standing waiting for me to open the front door this entire time." (callback = functools.partial(inctime,checkskip=True))
                    else:
                        show julian pain onlayer characters
                    if run == 3 and not solves.loop3_1:
                        julian_run3_d "For like hours!" (callback = functools.partial(inctime,checkskip=True))
                    else:
                        show julian pain onlayer characters
                    if run == 3 and not solves.loop3_1:
                        delilah_run3 "Do you think they're still just standing there?" (callback = functools.partial(inctime,checkskip=True))
                    else:
                        show julian pain onlayer characters
                    if run == 3 and not solves.loop3_1:
                        show julian puzzle_neutral onlayer characters
                    else:
                        show julian pain onlayer characters
                    if run == 3 and not solves.loop3_1:
                        julian_run3_d "No way, they had to have figured you left or something." (callback = functools.partial(inctime,checkskip=True))
                    else:
                        show julian pain onlayer characters
                    if run == 3 and not solves.loop3_1:
                        show julian puzzle_pain onlayer characters
                    else:
                        show julian pain onlayer characters
                    if run == 3 and not solves.loop3_1:
                        delilah_thoughts_run3 worried "He chuckles then coughs up a bit of blood." (callback = functools.partial(inctime,checkskip=True))
                    else:
                        show julian neutral onlayer characters
                    if run == 3 and not solves.loop3_1:
                        show julian pain onlayer characters
                    else:
                        show julian pain onlayer characters
                    if run == 3 and not solves.loop3_1 and not hints.hint3:
                        $ hintlist.list.append(hint_3)
                        # play animation to indicate new hint
                        $ renpy.play("chime.ogg")
                        $ hints.hint3 = True
                        $ hints.seen_hint = False
                    menu:
                        delilah " " (callback = functools.partial(inctime,g4=True))
                        "{color=#0f0}Say goodbye{/color}":
                            delilah_thoughts_run3 worried "Say goodbye"
                    show julian neutral onlayer characters
                    delilah_run3 happy "I really enjoyed talking to you for a bit, Julian."
                    show julian happy onlayer characters
                    julian_run3_d "Likewise. You're good company. Talk again soon?"
                    delilah_run3 happy "Yeah, I come around here often."
                    # hide julian onlayer characters with Dissolve(3.0)
                    show julian glitch onlayer characters with dissolve
                    hide julian glitch onlayer characters with Dissolve(3.0)

                    call incphase from _call_incphase_17
                    
                    if run == 3:
                        "{color=#0f0}She holds his hand and smiles till he goes limp,\nthinking of how nice it would be to spend another loop with him.{/color}"

                    if not hints.hint4 and run > 1:
                        # play animation to indicate new hint
                        $ renpy.play("chime.ogg")
                        $ hintlist.list.append(hint_4)
                        $ hints.hint4 = True
                        $ hints.seen_hint = False

                    $ phase = 0 # reset

                    return