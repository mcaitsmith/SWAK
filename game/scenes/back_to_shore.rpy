# The script of the game goes in this file.

label back_to_shore:
    # zoom bg plus sfx
    delilah_thoughts_run3 "When I get to the bottom of the hill, Julian is already waiting for me."
    show julian neutral onlayer characters at center:
        zoom 1.0
    pause 1.0
    julian_run3 "Back so soon?"
    delilah_run3 "After you died, I found this."
    delilah_thoughts_run3 "I hold out the second flower."
    julian_run3 "Ah, pretty. Why thank you." # He says dryly. (expression)
    delilah_run3 "Yeah, I broke my neck to get it."
    julian_run3 "You broke...? Oh, God, I'm so sorry. Why?"
    delilah_run3 "Call it a hunch, but I'm guessing these have something to do with this condition of ours. What do you know about them?"
    julian_run3 "These? They're Selene Lillies. Extremely rare luminescent flowers. They're what I was gathering before."
    # add some line around here about how the lilies are rumored to mess with time and space and cause "interference" (or just include in puzzle hint/solution text)
    delilah_run3 "You don't think they have something to do with all of...this?"
    julian_run3 "I think that's a bit out there, Delilah. I think it's bizarre, and a bit of a reach. But then again, I've died multiple times in the past twelve hours, so I'm liable to believe whatever you tell me."
    delilah_run3 "When I got this second flower I noticed...I don't know...something new. I was suddenly able to see more possible outcomes if that makes sense."
    julian_run3 "Not really. My 'outcome' has been pretty consistent."
    delilah_run3 "How many flowers did you have before you wound up here?"
    julian_run3 "Four. Was putting together a bouquet for my folks' shop. Just four Selene Lillies would sell for enough to keep the lights on for a year."
    delilah_run3 "So maybe if we get all four together we can send you home and break the loop?"
    julian_run3 "Couldn't hurt to try, I suppose. We're halfway there already."
    delilah_run3 "Where do you think we should start looking?" 
    julian_run3 "That could be tricky. Part of the legend of the Selene lillies is that the only time they appear for you is if you aren't looking for them."
    delilah_run3 "So if we go out searching for them we'll be stuck here forever."
    julian_run3 "Exactly."
    delilah_run3 "What do you suggest then?"
    julian_run3 "Honestly? Keep going about the loop like normal, try new outcomes, and see if we can stumble upon any new lillies. Think of it like walking backwards with a blindfold on except the entire time I'll be repeatedly dying."
    delilah_run3 "So, I should go be with my mom and brother then?"
    julian_run3 "Is that a problem?"
    delilah_run3 "Sort of. Things have just been really tense lately."
    julian_run3 "Want to talk about it?"
    menu:
        delilah " " (callback = functools.partial(inctime))
        "{color=#0f0}No. It's not important. I'll deal with it.{/color}":
            delilah_run3 "No. It's not important. I'll deal with it."
            julian_run3 "If you say so. I'm here if you do want to talk about it later. Not like we're exactly running out of time."
            delilah_run3 "I appreciate it."
            hide julian onlayer characters with dissolve
            $ loop3_investigate = True
            jump open_door
        "{color=#0f0}Open up to him{/color}":
            delilah_thoughts_run3 "Open up to him"
            delilah_run3 "My little brother has always been a bit of a nightmare, but some stuff happened a few months ago and...I don't know...I can't really look at my mom the same way again."
            julian_run3 "How so?"
            delilah_run3 "Well, like, you know how when you're a kid your parents are just perfect in every way to you? When you find out that they aren't, or even that they're a bit fucked up, it shatters your world."
            julian_run3 "I guess I'm lucky for that then. I lost my folks when I was young, so they'll always get to be perfect to me."
            delilah_run3 "Oh, Julian I'm so sorry. I had no idea."
            julian_run3 "It was a long time ago...ancient history. I just meant to say that I AM fortunate for that part of it, painful as it may have been."
            delilah_run3 "Why do you do that?"
            julian_run3 "Do what?"
            delilah_run3 "Act like it's okay. You've been doing that this entire time. Even when you're repeatedly dying in agony."
            julian_run3 "I don't know if I'd call it 'agony'."
            menu:
                delilah " " (callback = functools.partial(inctime))
                "{color=#0f0}If you say so.{/color}":
                    delilah_run3 "If you say so."
                    julian_run3 "I do say so. Now. Let's get back to the task at hand..."
                    hide julian onlayer characters with dissolve
                    $ loop3_investigate = True
                    jump open_door
                "{color=#0f0}Call him out{/color}":
                    delilah_thoughts_run3 "Call him out"

                    call incphase from _call_incphase_15

                    delilah_run3 "There you go again! Why do you need to do that?"
                    julian_run3 "Old habits. After I lost my folks, my grandparents took me in. They did their best but, y'know, their age shows pretty often. I take care of them more than they take care of me."
                    delilah_run3 "Does it feel so weird for me to be worried about you?"
                    julian_run3 "In all honesty, yes. I'm not used to it. I don't...talk...to people much. Especially girls who are, y'know...pretty."
                    delilah_thoughts_run3 "I look at him confused, then smile."
                    julian_run3 "That was weird to say, sorry."
                    delilah_thoughts_run3 "I laugh."
                    delilah_run3 "Not at all. I guess I just took you for a bit of a casanova initially."
                    julian_run3 "Me? As if."
                    delilah_thoughts_run3 "He snorts nervously."
                    julian_run3 "Just some kid who works at a flowershop."
                    pause 1.0
                    delilah_thoughts_run3 "We stare into each others' eyes, holding onto the moment for as long as possible."

                    call incphase from _call_incphase_16
                    time_centered "9 PM" (callback = functools.partial(inctime)) # intentionally skip 8pm for this ending
                    pause 1.0

                    delilah_thoughts_run3 "Julian's knees start to shake and abruptly fold underneath him."
                    delilah_run3 "Julian!"
                    delilah_thoughts_run3 "His eyes start to wander around. His arm quickly reaches up and I catch his hand."
                    julian_run3 "It's happening again..."
                    delilah_run3 "Oh God, oh shit, oh no. I'm here! I'm here!"
                    delilah_thoughts_run3 "He laughs."
                    delilah_run3 "What? What's funny?"
                    julian_run3 "We talked for so long we forgot to go look for the flowers."
                    delilah_run3 "Oh shit. We did."
                    delilah_thoughts_run3 "I laugh."
                    delilah_run3 "My mom and brother have probably been standing waiting for me to open the front door this entire time."
                    julian_run3 "For like hours!"
                    delilah_run3 "Do you think they're still just standing there?"
                    julian_run3 "No way, they had to have figured you left or something."
                    delilah_thoughts_run3 "He chuckles then coughs up a bit of blood."
                    delilah_run3 "I really enjoyed talking to you for a bit, Julian."
                    julian_run3 "Likewise. You're good company. Talk again soon?"
                    delilah_run3 "Yeah, I come around here often."
                    # hide julian onlayer characters with Dissolve(3.0)
                    show julian glitch onlayer characters with dissolve
                    hide julian glitch onlayer characters with Dissolve(3.0)

                    call incphase from _call_incphase_17
                    
                    if run == 3:
                        "{color=#0f0}She holds his hand and smiles till he goes limp,\nthinking of how nice it would be to spend another loop with him.{/color}"
                    $ phase = 0 # reset

                    return