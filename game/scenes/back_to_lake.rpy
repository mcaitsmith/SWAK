# The script of the game goes in this file.

label back_to_lake:
    show bg scene1 with dissolve
    if run == 2:
        "{color=#f00}Leading her down the patio stairs and down the hill towards the lake, they head to the lakeshore.{/color}"
    sandra_run2 "Is this where you saw him?"
    delilah_run2 "Yes! He was right here!"
    sandra_run2_d "Well...if he was here he's gone now."
    delilah_run2 "Should we look for him?"
    sandra_run2_d "I mean...he's probably just one of the neighbor kids. Had too much to drink maybe? I'm sure he'll be fine."
    delilah_run2 "But he wasn't...he looked like he wasn't even from around here."
    sandra_run2_d "Could've been one of the landscapers' kids then. Who knows? It hardly seems like any of our business, Del."
    delilah_run2 "Wow."
    sandra_run2_d "What?"
    delilah_run2 "I'm somehow completely unsurprised and still shocked by you."
    # replace below with animation/sfx
    delilah_thoughts_run2 "Mom turns around and starts her way back up the hill."
    sandra_run2_d "Let's just go try and have a normal evening together, yeah?"

    if run == 2 and flowers.flower2 and not hints.hint9 and not solves.loop2:
        $ config.rollback_enabled = False
        # play animation to indicate new hint
        $ renpy.play("orex_sfx_sparkle.ogg")
        $ hintlist.list.append(hint_9)
        $ hints.hint9 = True
        $ hints.seen_hint = False
        $ renpy.pause()

    $ config.rollback_enabled = True

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