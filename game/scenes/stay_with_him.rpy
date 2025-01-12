# The script of the game goes in this file.

label stay_with_him:
    $ phase += 1
    delilah "(if the player already tried to get help, there is an additional line about deciding that the only option is to just stay here with him)"
    delilah "Delilah decides to stay there on the lakeshore with Julian. They formally introduce each other and talk a bit about their lives. Julian seems resigned to die here, laments about what will happen to his grandparents without him. A few minor dialogue choices are present here which let the player have different responses to various questions/statements, but nothing that alters the course of the game."
    $ phase += 1
    delilah "After a moderately lengthy conversation in which Delilah and Julian start a budding friendship with some romantic tension, he begins to die, thanking her for staying with him so he didn't have to die alone."
    hide julian with dissolve
    if not flowers.flower2:
        if not solves.loop2:
            $ puzzles.loop2 = True # unlock puzzle
            call screen flower_glitch
        else:
            call screen flower2_pick
        delilah "After he dies, Delilah notices in the tree above them is one of the glowing flowers on a branch. The player is presented with the choice to climb the tree and grab the flower. After they do, Delilah falls from the tree, bashing her neck against the rocks below. She can't move. Her mom calls out to her while Delilah tries to scream but finds herself unable to. With the two flowers in her hand, she is able to rollback in time to the start of the game with a new loop option."
        # delilah "After he dies, Delilah notices in the tree above them is one of the glowing flowers on a branch. The player is presented with the choice to climb the tree and grab the flower. After they do, Delilah falls from the tree, bashing her neck against the rocks below. She can't move. Her mom calls out to her while Delilah tries to scream but finds herself unable to. With the two flowers in her hand, she is able to rollback in time to the start of the game with a new loop option." (callback = functools.partial(inctime, fnum=2))
    else:
        pass
    $ phase = 0
    return