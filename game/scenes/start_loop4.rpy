# The script of the game goes in this file.

label start_loop4:
    delilah "At the start of the fourth loop, Delilah is remorseful of having to put Cody through that. When she interacts with him again in the opening sequence, he is completely ignorant of the conversation they just had. Delilah makes a mental note not to put him through that again."
    delilah "She takes inventory and reminds herself that there are only two flowers left to find."
    delilah "The player can continue with the story by going and"
    menu:
        delilah "Dialogue choice" (callback = functools.partial(inctime))
        "Open the door for her mom":
            hide julian onlayer characters with dissolve
            jump open_door
        "going to the shore for the fourth time":
            jump back_to_shore_final