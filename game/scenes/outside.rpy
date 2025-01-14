# The script of the game goes in this file.

label outside:

    call incphase
    
    show bg scene3 with dissolve
    delilah "The door slams behind Delilah. She stands on the back patio and gazes out at the water for a moment. What would happen if she just started walking? The thought creeps into her mind. What if she just picked a direction and started walking indefinitely? Would she find peace? It was a possibility."
    pause 1.0
    show julian fade onlayer characters at center:
        zoom 0.7 # should have him zoomed out in distance
    pause 3.0
    delilah "Along the shoreline, by the rocks, she sees that shadowy figure once again standing just out of view."
    menu:
        delilah " " (callback = functools.partial(inctime))
        "Hey, I can see you!":
            delilah "Hey, I can see you!"
        "This is private property, asshole!":
            delilah "This is private property, asshole!"
        "Silently approach":
            delilah "Silently approach"
    show julian neutral onlayer characters at center:
        zoom 0.7
    pause 1.0
    delilah "The figure stumbles for a moment and then collapses on the rocks."
    delilah "Hey!"
    delilah "She runs down the hill towards the lakeshore." # now have Julian appear full
    delilah "Hey, are you okay?!"
    show julian neutral onlayer characters at center:
        zoom 1.0
    pause 2.0
    delilah "Laying on rocks, trembling in agony, is a boy clutching a glowing flower. He looks at Delilah with equal parts desperation and shock."
    # delilah "After dinner, Delilah is standing along the lake shore watching the waves crash against the rocks. She's contemplating running away forever, abandoning her family and never seeing them again. She wants to grow up. But she also thinks of Cody and despite how much she loathes him, she can't stand imagining him growing up alone. The player is presented with the choice to leave or not but this first round results in the same way regardless."
    # show julian sad onlayer characters at center with dissolve
    delilah "She hears movement behind her and turns around. Standing there is Julian, a strange boy around her age, clutching his side in pain and kneeling to the ground. In his hand he's holding a glowing flower. He collapses."
    delilah "He holds out the flower."
    
    call incphase

    if not flowers.flower1:
        call screen flower1_pick
        delilah "Once Delilah takes the glowing flower in hand, the boy goes limp. He's maybe a year or two older than her, she guesses."
        hide julian onlayer characters with Dissolve(3.0)
        delilah "Oh my God! Oh my God!"
        delilah "She looks around at the empty stillness of the night."
        delilah "Somebody help! Somebody help! He's not moving!" 
        # delilah "Delilah takes the flower, presented as a player choice, and notices that something feels different."
        # delilah "Delilah takes the flower, presented as a player choice, and notices that something feels different." (callback = functools.partial(inctime, fnum=1))
    else:
        delilah "If the flower has already been taken on a first loop, there is nothing in Julian's hands. Instead he just collapses then and there. The game stops until the player uses history to try a different passage option. Same happens if Delilah searches for Julian after dinner on the second loop."
        hide julian onlayer characters with Dissolve(3.0)
    $ phase = 0 # reset
    # hide julian onlayer characters with dissolve
    return