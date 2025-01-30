# The script of the game goes in this file.

label open_door:

    # open door scene: black with transparent window to moon + door windowpanes showing lake scene
    # once open door window fades to open door cutout

    pause 2.0 # play unlocking sound here

    show bg black with dissolve
    pause 1.0

    if run == 3 and loop3_investigate:
        call incphase from _call_incphase_5

        time_centered "8 PM"
        pause 1.0

        call unlock_door from _call_unlock_door_2

        sandra_d "Oh, how gracious of you to finally decide to let us in, Del. Very gracious indeed."
        
        show cody happy onlayer characters at center_right
        
        cody_d "Yes, very gracious."

        hide cody onlayer characters
        hide sandra onlayer characters
        with dissolve
        
        jump dinner_convo

    elif run == 2 and loop2_investigate:

        call unlock_door from _call_unlock_door

        if run == 2:
            "{color=#f00}As soon as she opens the door, Delilah grabs her mom by the hand.{/color}"
        delilah_run2 "There's a boy in the backyard! He needs help! Come on!"
        sandra_run2_d "What? Hold on! Who is?"
        delilah_run2 "Some guy! I don't know who he is but he needs help!"

        jump back_to_lake

    else:
        
        call incphase from _call_incphase_6

        time_centered "8 PM"
        pause 1.0

        call unlock_door from _call_unlock_door_1
        
        sandra_d "Oh, how gracious of you to finally decide to let us in, Del. Very gracious indeed."
        
        show cody happy onlayer characters at center_right
        
        cody_d "Yes, very gracious."
        delilah "Hey, are there still landscapers working in the yard?"
        sandra_d "Landscapers? Not at this hour, no. Why do you ask?"
        delilah worried "Could've sworn I saw someone out back. Thought it might have been a landscaper."
        sandra_d "Probably just one of the neighbor kids, I wouldn't worry about it."
        
        hide cody onlayer characters
        hide sandra onlayer characters
        with dissolve
        
        jump dinner_convo

label dinner_convo:
    if run == 3 and loop3_investigate:
        call argument from _call_argument_2

        delilah_thoughts_run3 neutral "The three of us sit in silence for a moment."
        if not flowers.flower3:
            cody_run3_d "I found a weird flower in the yard!"
        if not flowers.flower3:
            delilah_thoughts_run3 worried "I perk up."
        if not flowers.flower3:
            sandra_run3_d "Oooh, very cool. Is it a rose?"
        if not flowers.flower3:
            cody_run3_d "Nope!"
        if not flowers.flower3:
            sandra_run3_d "Is it....a daisy?"
        if not flowers.flower3:
            cody_run3_d "Nope!"
        if not flowers.flower3:
            delilah_run3 "Does it glow?"
        if not flowers.flower3:
            cody_run3_d "Yeah! How'd you know?"
        if not flowers.flower3:
            menu:
                delilah " " (callback = functools.partial(inctime))
                "{color=#0f0}I saw some outside.{/color}" if not flowers.flower3:
                    if not flowers.flower3:
                        delilah_run3 neutral "I saw some outside."
                "{color=#0f0}I heard they were local to the area.{/color}" if not flowers.flower3:
                    if not flowers.flower3:
                        delilah_run3 neutral "I heard they were local to the area."
        if not flowers.flower3:
            cody_run3_d "Well, it's mine now. Think I'll make it into a bookmark."
        if not flowers.flower3:
            delilah_run3 "Do you think you could give it to me?"
        if not flowers.flower3:
            cody_run3_d "Heck no! Finders keepers, Del!"

        call incphase from _call_incphase_18

        delilah_thoughts_run3 "Mom stands up from the table."
        sandra_run3_d "I can see this conversation is going in a fun direction. I'll be having a smoke outside if you need me."

        # delilah "Now looking for the Selene Lillies, Delilah proceeds with the previously established dinner scene with Cody and her mom. However, she is a bit less antagonistic of them as she now has a new goal of saving Julian. During dinner, she notices something glowing in Cody's pocket. Sandra steps out to have a smoke while Cody and Delilah clean up the kitchen."
        hide sandra onlayer characters with dissolve
        menu:
            delilah " " (callback = functools.partial(inctime))
            "{color=#0f0}Follow her outside{/color}":
                delilah_thoughts_run3 "Follow her outside"
                delilah_thoughts_run3 "I stand up from the table and follow Mom outside to the back patio."
                hide cody onlayer characters with dissolve
                call smoke_break from _call_smoke_break
            "{color=#0f0}Stay with Cody{/color}":
                delilah_thoughts_run3 neutral "Stay with Cody"
        if not flowers.flower3:
            delilah_thoughts_run3 neutral "I lean toward Cody."
        if not flowers.flower3:
            delilah_run3 laugh "You want to show me that flower you found?"
        if not flowers.flower3:
            cody_run3_d "Why? So you can take it?"
        # if not flowers.flower3:
        menu:
            delilah " " (callback = functools.partial(inctime))
            "{color=#0f0}It's really important that you give it to me.{/color}" if not flowers.flower3:
                delilah_run3 worried "It's really important that you give it to me."
                cody_run3_d "Why?"
                delilah_run3 angry "It just is."
                cody_run3_d neutral "That's not an explanation."
                menu:
                    delilah " " (callback = functools.partial(inctime))
                    "{color=#0f0}Explain the whole situation{/color}":
                        delilah_thoughts_run3 worried "Explain the whole situation"
                        delilah_thoughts_run3 "I go into great detail, explaining everything I've experienced up to this moment. No details spared."
                        call chase_cody from _call_chase_cody
                    "{color=#0f0}Tell him just enough{/color}":
                        delilah_thoughts_run3 "Tell him just enough"
                        call chase_cody from _call_chase_cody_1
                    "{color=#0f0}You just have to believe me!{/color}":
                        delilah_run3 worried "You just have to believe me!"
                        cody_run3_d "Why?"
                        delilah_run3 "You just do."
                        cody_run3_d "Why?"
                        delilah_run3 neutral "Because."
                        cody_run3_d "Because why?"
                        delilah_run3 "Because seriously bad stuff will happen if you don't."
                        cody_run3_d "Like what?"
                        delilah_run3 "I don't have time to tell you."
                        cody_run3_d "Why?"
                        delilah_run3 angry "Quit being a brat and just give me the flower!"
                        delilah_thoughts_run3 "He slowly steps back."
                        cody_run3_d "Okay, let me go get it for you..."
                        delilah_thoughts_run3 "Before I can say anything more, he turns and runs towards the stairs."
                        call cody_in_room from _call_cody_in_room
            "{color=#0f0}Just tell me where it is or I'll pummel you.{/color}" if not flowers.flower3:
                delilah_run3 "Just tell me where it is or I'll pummel you."
                cody_run3_d "Testy, testy."
                delilah_thoughts_run3 "He looks at me for a moment."
                cody_run3_d "Okay. You can have it. Just follow me upstairs."
                delilah_thoughts_run3 neutral "We start our way up the stairs but before I can say anything, he turns and makes a break for it."
                call cody_in_room from _call_cody_in_room_1
            "{color=#0f0}I'll give you $20 to give me that flower.{/color}" if not flowers.flower3:
                delilah_run3 "I'll give you $20 to give me that flower."
                cody_run3_d "You'll give me $20?"
                delilah_run3 "That's right."
                cody_run3_d "You don't even have $20."
                delilah_run3 neutral "I'll give you $20 once I get my next allowance."
                delilah_thoughts_run3 "He thinks about it for a moment."
                cody_run3_d "$100."
                menu:
                    delilah " " (callback = functools.partial(inctime))
                    "{color=#0f0}$30.{/color}":
                        delilah_run3 "$30."
                    "{color=#0f0}$50.{/color}":
                        delilah_run3 "$50."
                cody_run3_d "$90."
                menu:
                    delilah " " (callback = functools.partial(inctime))
                    "{color=#0f0}$65.{/color}":
                        delilah_run3 "$65."
                    "{color=#0f0}$70.{/color}":
                        delilah_run3 "$70."
                cody_run3_d "$80 and one dollar from every allowance until your 18th birthday..."
                menu:
                    delilah " " (callback = functools.partial(inctime))
                    "{color=#0f0}Absolutely not!{/color}":
                        delilah_run3 angry "Absolutely not!"
                cody_run3_d "Then it looks like you're shit out of luck..."
                menu:
                    delilah " " (callback = functools.partial(inctime))
                    "{color=#0f0}Fine.{/color}":
                        delilah_run3 neutral "Fine."
                cody_run3_d "Pleasure doing business with you. Just follow me upstairs."
                delilah_thoughts_run3 "I follow him up the stairs but before we get to the door to his bedroom, he leaps inside and slams the door."
                hide cody onlayer characters
                show bg black
                with dissolve
                delilah_run3 angry "Hey! We had a deal, dick!"
                cody_run3_d "We did, but you know, I thought about how much money you offered and, truthfully, the satisfaction I'll get from destroying something you want is worth more than any amount of money!" (callback = functools.partial(inctime))
                delilah_run3 worried "No! Stop!" (callback = functools.partial(inctime,g5=True))
                # glitch 3
                if run == 3 and not solves.loop3_2 and not hints.hint2:
                    $ hintlist.list.append(hint_2)
                    $ renpy.play("orex_sfx_sparkle.ogg")
                    # play animation to indicate new hint
                    $ hints.hint2 = True
                    $ hints.seen_hint = False
                if run == 3 and not solves.loop3_2 and hints.hint2 and not hints.hint5 and sum([solves.loop2,solves.loop3_1,solves.loop3_2,solves.loop3_3,solves.loop4]) > 0:
                    $ hintlist.list.append(hint_5)
                    # play animation to indicate new hint
                    $ renpy.play("orex_sfx_sparkle.ogg")
                    $ hints.hint5 = True
                    $ hints.seen_hint = False
                if run == 3 and not solves.loop3_2:
                    delilah_thoughts_run3 glitch "The shredded petals of the Selene lilly are slid beneath the door. The light slowly bleeds away from them before they become as brittle as paper in my hands." (callback = functools.partial(inctime,checkskip=True))
                if run == 3 and not solves.loop3_2 and not hints.hint3:
                    $ hintlist.list.append(hint_3)
                    # play animation to indicate new hint
                    $ renpy.play("orex_sfx_sparkle.ogg")
                    $ hints.hint3 = True
                    $ hints.seen_hint = False
            # "{color=#0f0}You know Dad is having an affair right?{/color}" if smoke_break and not flowers.flower3:
            "{color=#0f0}You know Dad is having an affair right?{/color}" if smoke_break:
                # if not flowers.flower3:
                delilah_run3 "You know Dad is having an affair right?"
                # if not flowers.flower3:
                cody_run3_d "What?"
                # if not flowers.flower3:
                delilah_thoughts_run3 "He laughs."
                # if not flowers.flower3:
                delilah_run3 "Yeah. It's true. I found a letter in his suitcase from some woman, probably a stripper." (callback = functools.partial(inctime))
                # if not flowers.flower3:
                cody_run3_d "Dad wouldn't do something like that, quit making stuff up!" (callback = functools.partial(inctime,g7=True))
                # glitch 4
                if flowers.flower3 and run == 3 and not solves.loop3_3:
                    show cody glitch onlayer characters
                else:
                    show cody neutral onlayer characters
                if flowers.flower3 and run == 3 and not solves.loop3_3:
                    show cody glitch onlayer characters
                if run == 3 and not solves.loop3_3:
                    delilah_run3 "She talked about how much she liked sleeping with him. They're probably together right now, Cody. That's why he isn't here..." (callback = functools.partial(inctime,checkskip=True))
                else:
                    show cody neutral onlayer characters
                if flowers.flower3 and run == 3 and not solves.loop3_3:
                    show cody glitch onlayer characters
                if run == 3 and not solves.loop3_3:
                    cody_run3_d "No...Dad's on a business trip..." (callback = functools.partial(inctime,checkskip=True))
                else:
                    show cody neutral onlayer characters
                if flowers.flower3 and run == 3 and not solves.loop3_3:
                    show cody glitch onlayer characters
                if run == 3 and not solves.loop3_3:
                    delilah_run3 "Yeah! BUSINESS trip. That's a good one. Mom knows about it too. She's divorcing him soon and then you won't have a family anymore while I'm at college." (callback = functools.partial(inctime,checkskip=True))
                else:
                    show cody neutral onlayer characters
                if flowers.flower3 and run == 3 and not solves.loop3_3:
                    show cody glitch onlayer characters
                if run == 3 and not solves.loop3_3:
                    delilah_thoughts_run3 "He looks at his feet and turns red, like he's about to start crying. Instead, something wells up in him and then dissipates in a long breath." (callback = functools.partial(inctime,checkskip=True))
                else:
                    show cody neutral onlayer characters
                if flowers.flower3 and run == 3 and not solves.loop3_3:
                    show cody glitch onlayer characters
                if run == 3 and not solves.loop3_3:
                    cody_run3_d "Oh." (callback = functools.partial(inctime,checkskip=True))
                else:
                    show cody neutral onlayer characters
                if flowers.flower3 and run == 3 and not solves.loop3_3:
                    show cody glitch onlayer characters
                if run == 3 and not solves.loop3_3:
                    delilah_run3 "Oh?" (callback = functools.partial(inctime,checkskip=True))
                else:
                    show cody neutral onlayer characters
                if flowers.flower3 and run == 3 and not solves.loop3_3:
                    show cody glitch onlayer characters
                if run == 3 and not solves.loop3_3:
                    cody_run3_d "Yeah. Oh. I guess I sort of knew already. Now that you point it out, it does make a lot of sense. I just didn't think it was possible. I think I need to go for a walk." (callback = functools.partial(inctime,checkskip=True))
                else:
                    show cody neutral onlayer characters
                if flowers.flower3 and run == 3 and not solves.loop3_3:
                    show cody glitch onlayer characters
                if flowers.flower3 and run == 3 and not solves.loop3_3:
                    if not hints.hint5 and sum([solves.loop2,solves.loop3_1,solves.loop3_2,solves.loop3_3,solves.loop4]) > 0:
                        $ hintlist.list.append(hint_5)
                        $ renpy.play("orex_sfx_sparkle.ogg")
                        # play animation to indicate new hint
                        $ hints.hint5 = True
                        $ hints.seen_hint = False
                if flowers.flower3 and run == 3 and not solves.loop3_3 and not hints.hint2:
                    $ hintlist.list.append(hint_2)
                    $ renpy.play("orex_sfx_sparkle.ogg")
                    # play animation to indicate new hint
                    $ hints.hint2 = True
                    $ hints.seen_hint = False
                if run == 3 and not solves.loop3_3:
                    delilah_thoughts_run3 worried "I look into his eyes to find what little life is in there slowly dimish into nothing. He didn't just lose his innocence, I ripped it out of him." (callback = functools.partial(inctime,checkskip=True))
                else:
                    show cody neutral onlayer characters
                if flowers.flower3 and run == 3 and not solves.loop3_3:
                    show cody neutral onlayer characters
                if flowers.flower3 and run == 3 and not solves.loop3_3 and hints.hint2 and not hints.hint3:
                    $ hintlist.list.append(hint_3)
                    # play animation to indicate new hint
                    $ renpy.play("orex_sfx_sparkle.ogg")
                    $ hints.hint3 = True
                    $ hints.seen_hint = False
                # if not flowers.flower3:
                #     menu:
                #         delilah " " (callback = functools.partial(inctime,g8=True))
                #         "{color=#0f0}Get the flower{/color}" if not flowers.flower3:
                #             if not flowers.flower3:
                #                 delilah_thoughts_run3 "Get the flower"
                if not flowers.flower3:
                    delilah_run3 worried "Uh, Cody, the flower?"
                if not flowers.flower3:
                    cody_run3_d "Oh, that. Yeah, it's in my room. Feel free to take it. I...don't think I'll need it anymore."

                if not flowers.flower3:
                    hide cody onlayer characters with dissolve

                if not flowers.flower3:
                    delilah_thoughts_run3 "He leaves out the front door into the night."

                if not flowers.flower3:
                    show bg black with dissolve
                if not flowers.flower3:
                    delilah_thoughts_run3 neutral "I don't stop him, instead going up the stairs to his bedroom to find the glowing flower sitting on his bed."

                # if not flowers.flower3 and not solves.loop3:
                #     show flower_glitch_image
                # else:
                #     hide flower_glitch_image
                # if not flowers.flower3 and not solves.loop3:
                #     delilah_thoughts_run3 "Static again! Like it's caught between worlds..."
                # else:
                #     hide flower_glitch_image

                # # puzzle hints
                # if not flowers.flower3:
                #     if not flowers.flower3 and puzzles.loop3 and not solves.loop3 and hints.loop3_1:
                #         delilah_thoughts_run3 "I've been seeing glitched-up ghosts of Julian appearing where my family should be. Creepy."
                #     if not flowers.flower3 and puzzles.loop3 and not solves.loop3 and hints.loop3_2:
                #         delilah_thoughts_run3 "Their words are the same but their identities are all garbled. If only I could REMEMBER who they really are..."
                #     if not flowers.flower3 and puzzles.loop3 and not solves.loop3 and hints.loop3_3:
                #         delilah_thoughts_run3 "Those glitched-up Julians probably need to get fixed in time and space, like I did with the moon. But how?"
                #     if not flowers.flower3 and puzzles.loop3 and not solves.loop3:
                #         menu:
                #             narrator "Need a hint?" (callback = functools.partial(inctime))
                #             "Yes" if not hints.loop3_1 and not flowers.flower3:
                #                 if not flowers.flower3 and puzzles.loop3 and not solves.loop3:
                #                     delilah_thoughts_run3 "I've been seeing glitched-up ghosts of Julian appearing where my family should be. Creepy."
                #                     $ hints.loop3_1 = True
                #             "Get another hint" if hints.loop3_1 and not hints.loop3_2 and not flowers.flower3:
                #                 if not flowers.flower3 and puzzles.loop3 and not solves.loop3:
                #                     delilah_thoughts_run3 "Their words are the same but their identities are all garbled. If only I could REMEMBER who they really are..."
                #                     $ hints.loop3_2 = True
                #             "Get final hint" if hints.loop3_2 and not hints.loop3_3 and not flowers.flower3:
                #                 if not flowers.flower3 and puzzles.loop3 and not solves.loop3:
                #                     delilah_thoughts_run3 "Those glitched-up Julians probably need to get fixed in time and space, like I did with the moon. But how?"
                #                     $ hints.loop3_3 = True
                #             "No" if not hints.loop3_3 and not flowers.flower3:
                #                 pass
                #             "Pick the flower anyway" if not flowers.flower3:
                #                 hide flower_glitch_image
                #                 if not flowers.flower3 and puzzles.loop3 and not solves.loop3:
                #                     $ skip_puzzle3 = True
                #                 if not flowers.flower3 and puzzles.loop3 and not solves.loop3:
                #                     call screen flower3_glitch_pick
                #     else:
                #         hide flower_glitch_image
                # else:
                #     hide flower_glitch_image

                # if not flowers.flower3:
                #     if not solves.loop3:
                #         $ puzzles.loop3 = True # unlock puzzle
                #         call screen flower_glitch
                #         hide flower_glitch_image
                #     else:
                #         call screen flower3_pick

                if not flowers.flower3:
                    call screen flower3_pick

                if flowers.flower3 and not config.rollback_enabled:
                    $ renpy.choice_for_skipping()
                if flowers.flower3 and not config.rollback_enabled:
                    $ _skipping = False
                if flowers.flower3 and not config.rollback_enabled:
                    delilah_thoughts_run3 "As I take it, I find my memory expanding once again. "
                else:
                    $ config.rollback_enabled = True

                $ config.rollback_enabled = True # re-enable rollback

        menu:
            delilah neutral " " (callback = functools.partial(inctime,g6=True,g8=True))
            "{color=#0f0}Go outside{/color}":
                delilah_thoughts_run3 "Go outside"
        hide cody onlayer characters
        hide sandra onlayer characters
        with dissolve

        jump outside
    elif run == 2 and loop2_investigate:
        call incphase from _call_incphase_7

        time_centered "8 PM"
        pause 1.0

        call argument from _call_argument

        jump outside

    else:
        
        call argument from _call_argument_1

        jump outside

label unlock_door:
    # add footsteps/ backdoor opening sfx
    delilah_thoughts "Sure enough, the key was still under the tacklebox, just where Dad always kept it."

    if run == 1:
        "With the dust floating in the air like flakes,\nfor a moment Delilah thinks she's walked into a snowglobe of her own childhood."
    
    delilah_thoughts "Cody's pressing his nose against the window, banging his hand on the glass like a zombie."
    menu:
        delilah " " (callback = functools.partial(inctime))
        "Open the door":
            delilah_thoughts "Open the door"
    
    # add open door sound here to replace line above
    pause 1.0
    
    show sandra neutral onlayer characters at center

    return

label argument:

    $ in_house = True

    show bg scene2 with Dissolve(2.0)
    
    delilah_thoughts neutral "Not even a minute after Sandra tips the pizza delivery driver, Cody has two slices on his plate."
    
    show cody happy onlayer characters at center
    
    delilah_thoughts "He pulls the cheese off and eats it separately, then licks the sauce off the crust before eating it."
    # replace this line below with expression change
    delilah_thoughts worried "I watch in horror."
    if not (run == 3 and loop3_investigate):
        delilah angry "Can't even eat pizza like a normal person?"
    cody_d "I can't help it if my eccentricities extend to my dining preferences."
    if run == 3 and loop3_investigate:
        delilah_run3 neutral "I didn't say anything this time."
    else:
        delilah "Eccentricities? Is that what they're calling being a little weirdo now?"
    delilah_thoughts neutral "Mom sits down at the table with nothing but a salad on her plate."
    
    show sandra neutral onlayer characters at right
    
    sandra_d "Oh, hush, Del, you used to have particular eating habits too."
    if run == 3 and loop3_investigate:
        delilah_run3 worried "I didn't even say anything!"
        sandra_run3_d "..Oh...I could've sworn that you had..."
        return
    elif run == 2 and loop2_investigate:
        delilah_run2 angry "I'm not talking to you. And it's not like he's about to stop being a little cretin anyway."
        cody_run2_d "Wastoid. I can't believe we're related."
        delilah_run2 "At the rate Dad's going, I wouldn't be surprised if we weren't related afterall."
        sandra_run2_d "What do you mean by that?"
    else:
        delilah laugh "Yeah, when I was five. Cody's almost in high school. God help my reputation if anyone finds out we're related!"
        cody_d "I'm not exactly shouting from the roof tops about being related to a wastoid either."
        delilah angry "Bite me!"
    cody_d "{size=15}Bitch...{/size}"
    # make line above small text to replace line below
    # cody "he says under his breath."
    if run == 2 and loop2_investigate:
        delilah_run2 "Fuck you."
    else:
        delilah "You little!"
        # replace line below with animated sprites
        delilah_thoughts "I stand up and raise my fist like I'm going to punch him from across the table."
    show sandra angry onlayer characters
    sandra_d "Hey! Hey! Relax!"
    if run == 2 and loop2_investigate:
        delilah_run2 "Oh, now you want to intervene?"
    else:
        delilah "Make him apologize!"
    sandra_d "Cody...will you please apologize to your sister for calling her a b-word?"
    cody_d "She started it!"
    sandra_d "Cody...things are hard enough as is..."
    # replace line below with animated sprite
    delilah_thoughts neutral "I cross my arms and raise an eyebrow."
    cody_d "I'm sorry...that you're a bitch."
    sandra_d "That's it! Upstairs, now!"
    delilah_thoughts "He drops his bare crusts in the trash dramatically then heads for the stairs."
    cody_d "I wonder why Dad prefers his business trips to being here!"
    
    hide cody onlayer characters with dissolve

    call incphase from _call_incphase_8

    menu:
        delilah " " (callback = functools.partial(inctime))
        "What a little brat" if not (run == 2 and loop2_investigate):
            delilah angry "What a little brat"
        "I can't believe you let him get away with that." if not (run == 2 and loop2_investigate):
            delilah angry "I can't believe you let him get away with that."
        "{color=#f00}He's right you know.{/color}" if run == 2 and loop2_investigate:
            delilah_run2 "He's right you know."
        "{color=#f00}Setting a great example for your kids, Sandra.{/color}" if run == 2 and loop2_investigate:
            delilah_run2 "Setting a great example for your kids, Sandra."
    show sandra neutral onlayer characters
    sandra_d "Well, Del, you don't exactly make it easy by antagonizing him." (callback = functools.partial(inctime))
    if run == 2 and loop2_investigate:
        # start loop 2 glitch
        delilah_run2 neutral "I'm not doing anything. I'm just like you, Sandra." (callback = functools.partial(inctime,g1=True))
        if run == 2:
            $ moonglitch5 = True
        if run == 2 and loop2_investigate and not hints.hint2:
            $ hintlist.list.append(hint_2)
            $ renpy.play("orex_sfx_sparkle.ogg")
            # play animation to indicate new hint
            $ hints.hint2 = True
            $ hints.seen_hint = False
        if run == 2 and not solves.loop2:
            sandra_run2_d "What is this about?" (callback = functools.partial(inctime,checkskip=True))
        if run == 2 and not solves.loop2:
            delilah_thoughts_run2 laugh "I laugh." (callback = functools.partial(inctime,checkskip=True))
        if run == 2 and not solves.loop2:
            delilah_run2 "You know what really pisses me off about this whole situation? You won't even admit to what we already know." (callback = functools.partial(inctime,checkskip=True))
    else:
        delilah neutral "I don't antagonize him..."
        delilah_thoughts worried "Those last words he said before storming off..."
        delilah "He's right though, about Dad, I mean."
        sandra_d neutral "Your dad wishes he could be here more than anything in the world. Work has been brutal lately."
        delilah_thoughts laugh "I laugh." # add laugh sound to replace this or just (haha)
        delilah "Yeah, I'm sure."
    if not (run == 2 and loop2_investigate and solves.loop2):
        sandra_d "What's that supposed to mean?" (callback = functools.partial(inctime,checkskip=True))
    if not (run == 2 and loop2_investigate and solves.loop2):
        delilah "I think you know what I mean." (callback = functools.partial(inctime,checkskip=True))
    if not (run == 2 and loop2_investigate and solves.loop2):
        sandra_d "No, I don't, and you should watch what you say or you'll regret it." (callback = functools.partial(inctime,checkskip=True))
    if run == 2 and loop2_investigate:
        if run == 2 and not solves.loop2:
            delilah_run2 "I dare you to be honest with me. Just show a single shred of honesty and respect to your children and just tell us: why isn't Dad here?" (callback = functools.partial(inctime,checkskip=True))
        # if run == 2 and not solves.loop2:
        #     pause 1.0
        if run == 2 and not solves.loop2:
            delilah_thoughts_run2 "Mom's throat trembles, like she's choking on the words." (callback = functools.partial(inctime,checkskip=True))
        if run == 2 and not solves.loop2:
            sandra_run2_d "He's on a business trip, Del." (callback = functools.partial(inctime,checkskip=True))
        if run == 2 and not solves.loop2:
            delilah_run2 "That's what I thought." (callback = functools.partial(inctime,checkskip=True))
        if run == 2:
            $ moonglitch5 = False
        if run == 2 and loop2_investigate and not hints.hint3:
            $ hintlist.list.append(hint_3)
            # play animation to indicate new hint
            $ renpy.play("orex_sfx_sparkle.ogg")
            $ hints.hint3 = True
            $ hints.seen_hint = False
        menu:
            delilah " " (callback = functools.partial(inctime,g2=True))
            "{color=#f00}I'll be outside.{/color}":
                delilah_run2 "I'll be outside."

    else:
        delilah "Is that a promise?"
        sandra_d "Don't you start."
        menu:
            delilah " " (callback = functools.partial(inctime))
            "Dad can't stand you.":
                delilah "Dad can't stand you."
            "It's your fault he isn't here.":
                delilah "It's your fault he isn't here."
            "This family is a joke.":
                delilah "This family is a joke."
        sandra_d "Upstairs. Now."
        # delilah "Fuck you, I'm going for a walk."
        menu:
            delilah " " (callback = functools.partial(inctime))
            "Fuck you, I'm going for a walk.":
                delilah "Fuck you, I'm going for a walk."

    hide sandra onlayer characters with dissolve

    return

label chase_cody:
    delilah_thoughts_run3 "Cody looks at me astonished."
    cody_run3_d "Wow. I can't believe it."
    delilah_run3 "Well, it's true. All of it."
    cody_run3_d "I mean, I can't believe how completely nuts you are. I knew you were a mental case, sure, but imaginary boys? Magic flowers? Someone's getting sent to the funny farm..."
    delilah_run3 worried "I'm not crazy! You have to give me that flower!"
    delilah_thoughts_run3 "Before I can say anything more, he turns and runs towards the stairs, shouting."
    cody_run3_d "Help! Help! My sister's gone crazy!"
    call cody_in_room from _call_cody_in_room_2
    return

label cody_in_room:
    hide cody onlayer characters with dissolve
    delilah_run3 angry "Come back here you little turd!"
    delilah_thoughts_run3 "I chase after him."
    show bg black with dissolve
    delilah_thoughts_run3 "He runs into his bedroom and slams the door behind him."
    delilah_run3 "Open up before I kill you!"
    cody_run3_d "I'm gonna rip up the flower!"
    delilah_run3 worried "You don't know what you're doing!"
    cody_run3_d "You can't stop me!" (callback = functools.partial(inctime))
    menu:
        delilah " " (callback = functools.partial(inctime))
        "{color=#0f0}Please, Cody!{/color}":
            delilah_run3 "Please, Cody!" (callback = functools.partial(inctime,g5=True))
        "{color=#0f0}Don't you dare!{/color}":
            delilah_run3 "Don't you dare!" (callback = functools.partial(inctime,g5=True))
    # pause 1.0
    # glitch 3
    if not solves.loop3_2 and not hints.hint2:
        $ hintlist.list.append(hint_2)
        $ renpy.play("orex_sfx_sparkle.ogg")
        # play animation to indicate new hint
        $ hints.hint2 = True
        $ hints.seen_hint = False
    if run == 3 and not solves.loop3_2 and hints.hint2 and not hints.hint5 and sum([solves.loop2,solves.loop3_1,solves.loop3_2,solves.loop3_3,solves.loop4]) > 0:
        $ hintlist.list.append(hint_5)
        # play animation to indicate new hint
        $ renpy.play("orex_sfx_sparkle.ogg")
        $ hints.hint5 = True
        $ hints.seen_hint = False
    if run == 3 and not solves.loop3_2:
        delilah_thoughts_run3 glitch "The shredded petals of the Selene lilly are slid beneath the door. The light slowly bleeds away from them before they become as brittle as paper in my hands." (callback = functools.partial(inctime,checkskip=True))
    if run == 3 and not solves.loop3_2 and not hints.hint3:
        $ hintlist.list.append(hint_3)
        # play animation to indicate new hint
        $ renpy.play("orex_sfx_sparkle.ogg")
        $ hints.hint3 = True
        $ hints.seen_hint = False
    return