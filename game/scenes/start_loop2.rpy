﻿# The script of the game goes in this file.

label start_loop2:
    delilah_thoughts_run2 worried "There's a glowing flower in my hand."

    call incphase from _call_incphase_12
    
    if run == 2:
        "{color=#f00}A dam ruptures and she can see the image of that boy dying on the lakeshore burned into her mind.{/color}" 
    delilah_thoughts_run2 "This has already happened. The dinner. The fight. The boy dying in our backyard."

    menu:
        delilah " "
        "{color=#f00}Go to the lakeshore{/color}":
            delilah_thoughts_run2 "Go to the lakeshore"
            jump investigate_lakeshore
        "{color=#f00}Open the backdoor for Mom and Cody{/color}":
            hide julian onlayer characters
            with { "characters" : Dissolve(3.0) }
            delilah_thoughts_run2 neutral "Open the backdoor for Mom and Cody"
            jump open_door