# The script of the game goes in this file.

label outside:

    call incphase from _call_incphase_9

    $ in_house = False
    
    show bg scene3 with dissolve

    time_centered "9 PM"
    pause 1.0

    delilah_thoughts neutral "The door slams behind me." # replace with door slam sfx
    # delilah_thoughts "The door slams behind Delilah." # replace with door slam sfx

    if run == 1:
        "She stands on the back patio and gazes out at the water for a moment.\nWhat would happen if she just started walking? The thought creeps into her mind.\nWhat if she just picked a direction and started walking indefinitely? Would she find peace?\nIt's a possibility."
    # delilah_thoughts "She stands on the back patio and gazes out at the water for a moment. What would happen if she just started walking? The thought creeps into her mind. What if she just picked a direction and started walking indefinitely? Would she find peace? It was a possibility."

    pause 1.0
    
    show julian fade onlayer characters at center:
        zoom 0.7 # should have him zoomed out in distance
    pause 3.0
    
    delilah_thoughts "Along the shoreline, by the rocks, that shadowy figure once again stands just out of view."
    # delilah_thoughts "Along the shoreline, by the rocks, she sees that shadowy figure once again standing just out of view."

    show julian shadow onlayer characters at center with dissolve:
        zoom 0.7 # in distance
    menu:
        delilah " " (callback = functools.partial(inctime))
        "Hey, I can see you!" if run == 1:
            delilah "Hey, I can see you!"
        "This is private property, asshole!" if run == 1:
            delilah "This is private property, asshole!"
        "Hey! Do you need help?!" if run == 2:
            delilah "Hey! Do you need help?!"
        "Silently approach":
            delilah_thoughts "Silently approach"

    show julian neutral onlayer characters at center with dissolve:
        zoom 0.7
    pause 1.0

    delilah_thoughts "The figure stumbles for a moment and then collapses on the rocks."
    delilah "Hey!"
    # replace line below with running sfx + moving/zoom bg
    delilah_thoughts "I run down the hill towards the lakeshore."
    delilah "Hey, are you okay?!"

    # now have Julian appear full
    show julian neutral onlayer characters at center:
        zoom 1.0
    pause 2.0

    call incphase from _call_incphase_10

    # show julian happy onlayer characters

    # julian "test"

    if not flowers.flower1:
        delilah_thoughts "Laying on rocks, trembling in agony, is a boy clutching a glowing flower."
    else:
        delilah_thoughts "Laying on rocks, trembling in agony, is a boy clutching...nothing."
    delilah_thoughts "He looks at me with equal parts desperation and shock." # replace with expression change


    if not flowers.flower1:

        delilah_thoughts "He holds out the flower."
    if not flowers.flower1:

        show julian blur onlayer characters with dissolve

    if not flowers.flower1:
        call screen flower1_pick
    if flowers.flower1 and not config.rollback_enabled:
        $ renpy.choice_for_skipping()
    if flowers.flower1 and not config.rollback_enabled:
        $ _skipping = False
    if flowers.flower1 and not config.rollback_enabled:
        show julian neutral onlayer characters with dissolve
    if flowers.flower1 and not config.rollback_enabled:
        delilah_thoughts "The boy goes limp. He's maybe a year or two older than me, I guess."
    if flowers.flower1 and not config.rollback_enabled:
        show julian glitch onlayer characters with dissolve
    if flowers.flower1 and not config.rollback_enabled:
        hide julian glitch onlayer characters with Dissolve(3.0)
    if flowers.flower1 and not config.rollback_enabled:
        delilah "Oh my God! Oh my God!"
    if flowers.flower1 and not config.rollback_enabled:
        delilah_thoughts "I look around at the empty stillness of the night." # replace with animated sprite
    if flowers.flower1 and not config.rollback_enabled:
        delilah "Somebody help! Somebody help! He's not moving!" 
    if flowers.flower1 and not config.rollback_enabled:
        pause 1.0
    if flowers.flower1 and not config.rollback_enabled:
        delilah_thoughts "Holding the flower, I feel something in me change."
    if flowers.flower1 and not config.rollback_enabled:
        delilah_thoughts "At the center of my mind is a flower, its petals closed tightly like a fist. Then with a glimmer of light, it opens, releasing a cloud of golden aura into the air."
    if flowers.flower1 and not config.rollback_enabled:
        delilah_thoughts "With each breath I take, I can feel myself here and now as well as in the past simultaneously. I remember being in the car with my family, arriving at the lake, and the ability to remember my choices...differently."
    if flowers.flower1 and not config.rollback_enabled:
        delilah_thoughts "What has changed in my history?"

    if not hints.hint1:
        # play animation to indicate new hint
        $ renpy.play("orex_sfx_sparkle.ogg")
        $ hintlist.list.append(hint_1)
        $ hints.hint1 = True
        $ hints.seen_hint = False
    if not hints.hint4 and run > 1:
        # play animation to indicate new hint
        $ renpy.play("orex_sfx_sparkle.ogg")
        $ hintlist.list.append(hint_4)
        $ hints.hint4 = True
        $ hints.seen_hint = False
    $ config.rollback_enabled = True # re-enable rollback

    if flowers.flower1 and renpy.showing("julian","characters"):
        show julian glitch onlayer characters with dissolve
        hide julian onlayer characters with Dissolve(3.0)

    $ phase = 0 # reset

    return