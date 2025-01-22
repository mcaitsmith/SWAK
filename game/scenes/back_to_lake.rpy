# The script of the game goes in this file.

label back_to_lake:
    show bg scene3 with dissolve
    if run == 2:
        "{color=#f00}Leading her down the patio stairs and down the hill towards the lake, they head to the lakeshore.{/color}"
    sandra_run2 "Is this where you saw him?"
    delilah_run2 "Yes! He was right here!"
    sandra_run2 "Well...if he was here he's gone now."
    delilah_run2 "Should we look for him?"
    sandra_run2 "I mean...he's probably just one of the neighbor kids. Had too much to drink maybe? I'm sure he'll be fine."
    delilah_run2 "But he wasn't...he looked like he wasn't even from around here."
    sandra_run2 "Could've been one of the landscapers' kids then. Who knows? It hardly seems like any of our business, Del."
    delilah_run2 "Wow."
    sandra_run2 "What?"
    delilah_run2 "I'm somehow completely unsurprised and still shocked by you."
    # replace below with animation/sfx
    delilah_thoughts_run2 "Mom turns around and starts her way back up the hill."
    sandra_run2 "Let's just go try and have a normal evening together, yeah?"

    menu:
        delilah " " (callback = functools.partial(inctime))
        "{color=#f00}Fine.{/color}":
            delilah_run2 "Fine."
            hide sandra onlayer characters
            show bg black
            with dissolve

            jump dinner_convo
            
        "{color=#f00}Go looking for the boy{/color}":
            delilah_thoughts_run2 "Go looking for the boy"
            hide sandra onlayer characters with dissolve
            jump search_for_julian