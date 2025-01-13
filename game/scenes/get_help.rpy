# The script of the game goes in this file.

label get_help:
    show bg black with dissolve
    $ phase += 1
    show screen eclipse onlayer background_overlay with Dissolve(2.0)
    pause 1.0
    delilah "If the player rejects this idea and goes for help, she runs down the street, finds a payphone, and calls for an ambulance. By the time paramedics arrive, there is nobody on the lakeshore."
    show bg scene3 with dissolve
    $ phase += 1
    show screen eclipse onlayer background_overlay with Dissolve(2.0)
    pause 1.0
    delilah "The game stops here unless the player uses the history function to try a different choice."
    
    $ phase = 0 # reset
    return