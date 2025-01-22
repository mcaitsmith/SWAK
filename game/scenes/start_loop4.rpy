# The script of the game goes in this file.

label start_loop4:
    delilah_thoughts_run4 "Before turning to go look for Julian, I stop to examine Cody."
    show cody happy onlayer characters at center with dissolve
    delilah_thoughts_run4 "I think about how he reacted to the news of our father's infidelity, how he seemed so long, and how the entire revelation was undone in an instant."
    delilah_thoughts_run4 "He still has life in his eyes."
    delilah_thoughts_run4 "Good, I think to myself, holding three of the four flowers. Never do that to Cody again."

    menu:
        delilah " " (callback = functools.partial(inctime))
        # "Open the door for her mom":
        #     hide julian onlayer characters with dissolve
        #     jump open_door
        "{color=#0ff}Continue to the shore{/color}":
            hide cody onlayer characters with dissolve
            jump back_to_shore_final