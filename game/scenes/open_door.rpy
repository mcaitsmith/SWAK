# The script of the game goes in this file.

label open_door:
    show bg scene2 with dissolve
    show cody happy at center with dissolve
    show sandra neutral at right with dissolve
    if run == 3 and loop3_investigate:
        jump dinner_convo
    elif run == 2 and loop2_investigate:
        delilah "With one flower in possession, Delilah is quick to let her mom and brother in. She tells them that there's a boy by the lake who needs medical attention."
        hide cody with dissolve
        jump back_to_lake
    else:
        delilah "Delilah lingers in the house for a moment, taking in childhood memories at the lake house. She examines a few artifacts of her father's presence before her mother and brother start banging on the door. She lets them in and thinks a bit about the figure she saw on the shoreline."
        jump dinner_convo

label dinner_convo:
    if run == 3 and loop3_investigate:
        delilah "Now looking for the Selene Lillies, Delilah proceeds with the previously established dinner scene with Cody and her mom. However, she is a bit less antagonistic of them as she now has a new goal of saving Julian. During dinner, she notices something glowing in Cody's pocket. Sandra steps out to have a smoke while Cody and Delilah clean up the kitchen."
        hide sandra with dissolve
        menu:
            delilah "Dialogue choice" (callback = functools.partial(inctime, trig=True))
            "go with Sandra":
                hide cody with dissolve
                call smoke_break from _call_smoke_break
            "stay inside":
                delilah "In this scene, the player talks with Cody and discovers that he found one of the glowing flowers in the front yard. If Delilah asks for it back he attempts to bargain for it, but, being a little brat, tears it apart instead of giving it to you. You can reattempt the conversation as many times as you want, trying different options each time, even explaining the situation with Julian to him, but he laughs and rips the flower up every time."
                show sandra neutral at right with dissolve
                delilah "After Cody rips up the flower, the player can punch Cody just as Sandra walks in. Delilah gets in trouble and Sandra tells her to come outside."
        if smoke_break:
            delilah "If the player has completed the smoke break conversation, a new dialogue option is available with Cody in which she can tell him everything about their father's infidelity. Just as Sandra said, the news is devastating and he refuses to accept it, but you go further and further by sharing details from the letter Delilah read. Each detail hurts him more and more. He looks at the flower for a moment, questioning everything he's ever known, and then leaves it on the counter."
            if not flowers.flower3:
                delilah "Delilah gets the flower and is able to roll back and start the fourth loop." (callback = functools.partial(inctime, fnum=3))
            else:
                pass
            # sandra returns, delilah goes outside
            show sandra neutral at right with dissolve
        hide cody with dissolve
        hide sandra with dissolve
        jump outside
    elif run == 2 and loop2_investigate:
        delilah "If the player goes back inside, Delilah experiences the dinner conversation again, except her attitude is much harsher with more options to antagonize Cody and Sandra. We get a few more clues as to what is truly upsetting Delilah but we don't outright know it yet."
        delilah "The dinner ends in a much more explosive manner than the first time and Delilah can either"
        menu:
            delilah "Dialogue choice" (callback = functools.partial(inctime, trig=True))
            "run outside":
                hide cody with dissolve
                hide sandra with dissolve
                jump outside
            "tell off her mom before going outside":
                delilah "With the second option Delilah says some incredibly hurtful things, the sort that would make a relationship impossible to fix. It's obvious how hurt Sandra is. Then she goes back to the regular \"outside\" passage"
                hide cody with dissolve
                hide sandra with dissolve
                jump outside
    else:
        delilah "Fast forward to dinner. Things are tense. Cody tries to break the silence by being his quippy doofusy self and Delilah tears him a new one. A brief, bitter exchange occurs and Mom quickly shuts them down. This is a mistake. Now the attention is on her and the elephant in the room: Where is dad? The player is presented with several dialogue choices in this conversation, all with the same results but conveying different pieces of information about who these people are."
        delilah "Mom and Delilah fight. Delilah seems to be pushing her buttons, vying to get her to admit to... something...we aren't sure yet, but Mom is stubborn. No matter what she will not acknowledge that anything is amiss. Dinner ends abruptly and Delilah storms out."
        hide cody with dissolve
        hide sandra with dissolve
        jump outside