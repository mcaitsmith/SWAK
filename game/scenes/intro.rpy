# The script of the game goes in this file.

label intro:

    show cody happy at center with dissolve
    show sandra neutral at right with dissolve
    delilah "Game begins with Delilah, a sixteen year old girl, arriving at her family's lakehouse. It's just her, her mother, and her obnoxious little brother, Cody. They're spending a weekend away while dad is on one of his many frequent business trips. He's frequently absent these days."
    delilah "Delilah is deeply unhappy for reasons we don't yet know but she gives her mother a hard time and antagonizes Cody."
    hide cody with dissolve
    hide sandra with dissolve
    show julian sad at right with dissolve
    delilah "When they arrive, it's close to sunset. The key to the front door isn't working so Delilah has been told to try using the back door. She goes around the back and sees the lake. She sees something just along the shore. The player might stop for a moment or go unlock the door. If they stop for a moment they see what looks lke a shadowy figure standing in the distance. Is that a person? If the player has chosen to linger, her mom shouts for her to open the door."
    menu:
        delilah "Dialogue choice" (callback = functools.partial(inctime, trig=True))
        "Open the door":
            hide julian with dissolve
            jump open_door
        "Wait, haven't I been here before?" if run == 2:
            jump start_loop2
        "Oh god that hurt" if run == 3:
            jump start_loop3
        "Im sorry I had to do that" if run == 4:
            jump start_loop4

    return
