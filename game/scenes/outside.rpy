# The script of the game goes in this file.

label outside:
    $ phase += 1
    show bg scene3 with dissolve
    delilah "After dinner, Delilah is standing along the lake shore watching the waves crash against the rocks. She's contemplating running away forever, abandoning her family and never seeing them again. She wants to grow up. But she also thinks of Cody and despite how much she loathes him, she can't stand imagining him growing up alone. The player is presented with the choice to leave or not but this first round results in the same way regardless."
    show julian sad at right with dissolve
    delilah "She hears movement behind her and turns around. Standing there is Julian, a strange boy around her age, clutching his side in pain and kneeling to the ground. In his hand he's holding a glowing flower. He collapses."
    $ phase += 1
    if not flowers.flower1:
        call screen flower1_pick
        delilah "Delilah takes the flower, presented as a player choice, and notices that something feels different."
        # delilah "Delilah takes the flower, presented as a player choice, and notices that something feels different." (callback = functools.partial(inctime, fnum=1))
    else:
        delilah "If the flower has already been taken on a first loop, there is nothing in Julian's hands. Instead he just collapses then and there. The game stops until the player uses history to try a different passage option. Same happens if Delilah searches for Julian after dinner on the second loop."
    $ phase = 0 # reset
    hide julian with dissolve
    return