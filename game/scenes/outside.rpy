# The script of the game goes in this file.

label outside:

    call incphase from _call_incphase_9
    
    show bg scene3 with dissolve

    "9 PM"
    pause 1.0

    delilah_thoughts "The door slams behind me." # replace with door slam sfx
    # delilah_thoughts "The door slams behind Delilah." # replace with door slam sfx

    if run == 1:
        "She stands on the back patio and gazes out at the water for a moment. What would happen if she just started walking? The thought creeps into her mind. What if she just picked a direction and started walking indefinitely? Would she find peace? It's a possibility."
    # delilah_thoughts "She stands on the back patio and gazes out at the water for a moment. What would happen if she just started walking? The thought creeps into her mind. What if she just picked a direction and started walking indefinitely? Would she find peace? It was a possibility."

    pause 1.0
    
    show julian fade onlayer characters at center:
        zoom 0.7 # should have him zoomed out in distance
    pause 3.0
    
    delilah_thoughts "Along the shoreline, by the rocks, that shadowy figure once again stands just out of view."
    # delilah_thoughts "Along the shoreline, by the rocks, she sees that shadowy figure once again standing just out of view."
    
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

    show julian neutral onlayer characters at center:
        zoom 0.7
    pause 1.0

    delilah_thoughts "The figure stumbles for a moment and then collapses on the rocks."
    delilah "Hey!"
    # replace line below with running sfx + moving/zoom bg
    delilah_thoughts "She runs down the hill towards the lakeshore."
    delilah "Hey, are you okay?!"

    # now have Julian appear full
    show julian neutral onlayer characters at center:
        zoom 1.0
    pause 2.0

    call incphase from _call_incphase_10

    if not flowers.flower1:
        delilah_thoughts "Laying on rocks, trembling in agony, is a boy clutching a glowing flower."
    else:
        delilah_thoughts "Laying on rocks, trembling in agony, is a boy clutching...nothing."
    delilah_thoughts "He looks at Delilah with equal parts desperation and shock." # replace with expression change

    if not flowers.flower1:

        delilah_thoughts "He holds out the flower."

    if not flowers.flower1:
        call screen flower1_pick
    if flowers.flower1 and not config.rollback_enabled:
        delilah_thoughts "The boy goes limp. He's maybe a year or two older than me, I guess."
    if flowers.flower1 and not config.rollback_enabled:
        hide julian onlayer characters with Dissolve(3.0)
    if flowers.flower1 and not config.rollback_enabled:
        delilah "Oh my God! Oh my God!"
    if flowers.flower1 and not config.rollback_enabled:
        delilah_thoughts "She looks around at the empty stillness of the night." # replace with animated sprite
    if flowers.flower1 and not config.rollback_enabled:
        delilah "Somebody help! Somebody help! He's not moving!" 

    $ config.rollback_enabled = True # re-enable rollback

    if flowers.flower1:
        
        hide julian onlayer characters with Dissolve(3.0)

    # PLACEHOLDER LINE
    "(add some line here to hint to player that they have to rollback to first screen)"

    $ phase = 0 # reset

    return