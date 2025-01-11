# The script of the game goes in this file.

label start_loop3:
    delilah "Delilah sees that she now has two flowers in hand and is back at the start of the evening. From here the player can immediately"
    menu:
        delilah "Dialogue choice" (callback = functools.partial(inctime, trig=True))
        "go back to the shore":
            jump back_to_shore
        "Open the door":
            hide julian with dissolve
            jump open_door