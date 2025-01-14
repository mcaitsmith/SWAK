﻿# The script of the game goes in this file.

label outside:

    call incphase
    
    show bg scene3 with dissolve

    delilah_thoughts "The door slams behind Delilah." # replace with door slam sfx

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
        "Hey, I can see you!":
            delilah "Hey, I can see you!"
        "This is private property, asshole!":
            delilah "This is private property, asshole!"
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

    delilah_thoughts "Laying on rocks, trembling in agony, is a boy clutching a glowing flower."
    delilah_thoughts "He looks at Delilah with equal parts desperation and shock." # replace with expression change
    delilah_thoughts "He holds out the flower."
    
    call incphase

    if not flowers.flower1:

        call screen flower1_pick

        delilah_thoughts "The boy goes limp. He's maybe a year or two older than me, I guess."
        # delilah_thoughts "Once Delilah takes the glowing flower in hand, the boy goes limp. He's maybe a year or two older than her, she guesses."
        
        hide julian onlayer characters with Dissolve(3.0)
        
        delilah "Oh my God! Oh my God!"
        delilah_thoughts "She looks around at the empty stillness of the night." # replace with animated sprite
        delilah "Somebody help! Somebody help! He's not moving!" 

    else:
        
        delilah "If the flower has already been taken on a first loop, there is nothing in Julian's hands. Instead he just collapses then and there. The game stops until the player uses history to try a different passage option. Same happens if Delilah searches for Julian after dinner on the second loop."
        hide julian onlayer characters with Dissolve(3.0)

    $ phase = 0 # reset

    return