# The script of the game goes in this file.

label start_loop3:
    delilah_thoughts_run3 "I trace my fingers along the back of my neck, remembering the feeling of it snapping on the rocks."
    delilah_thoughts_run3 "I look down to see two glowing flowers in my other hand."

    call incphase from _call_incphase_19

    delilah_thoughts_run3 "There's no denying the reality of the situation anymore. Me and Julian are stuck in a loop together and these flowers are the cause."

    menu:
        delilah " " (callback = functools.partial(inctime))
        "{color=#0f0}Open the door for mom and Cody{/color}":
            hide julian onlayer characters
            with { "characters" : Dissolve(3.0) }
            delilah_thoughts_run3 "Open the door for Mom and Cody"
            jump open_door
        "{color=#0f0}Go find Julian at the shore{/color}":
            delilah_thoughts_run3 "Go find Julian at the shore"
            jump back_to_shore