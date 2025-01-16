# The script of the game goes in this file.

label get_help:

    call incphase

    delilah "No, no, you need help!"
    boy "Please...just stay..."
    
    hide julian onlayer characters
    with { "characters" : Dissolve(3.0) }

    delilah_thoughts "But before I can answer him, my feet are already carrying me to the nearest road."
    # delilah_thoughts "But before she could answer him, her feet were already carrying her to the nearest road."

    show bg black with dissolve

    delilah_thoughts "Along the dark roads, illuminated by street lamps, I try to find a payphone. After fifteen minutes of searching I find one and dial 9-1-1."
    # delilah_thoughts "Along the dark roads, illuminated by street lamps, she tried to find a payphone. After fifteen minutes of searching she found one and dialed 9-1-1."
    delilah_thoughts "Thirty minutes pass and paramedics arrive."
    delilah_thoughts "I explain the situation, the boy down on the rocks who was dying from some unseen condition. They take me at my word and follow me down the hill towards the lake."
    # delilah_thoughts "She explains the situation, the boy down on the rocks who was dying from some unseen condition. They take her at her word and follow her down the hill towards the lake."

    call incphase
    # delilah "If the player rejects this idea and goes for help, she runs down the street, finds a payphone, and calls for an ambulance. By the time paramedics arrive, there is nobody on the lakeshore."
    show bg scene3 with dissolve

    delilah_thoughts "When we get there, the boy has disappeared once again. Not a trace of him is left behind."
    # delilah_thoughts "When they get there, the boy has disappeared once again. Not a trace of him is left behind."
    
    # delilah "The game stops here unless the player uses the history function to try a different choice."
    
    $ phase = 0 # reset
    
    return