# The script of the game goes in this file.

label investigate_lakeshore:
    delilah "Delilah goes by the shore to find Julian standing there confused. He remembers Delilah and then everything fading to black. He's afraid of you but then starts to remember that she took the flower from him before everything went black."
    delilah "As the two talk, Julian keels over in pain. Delilah asks what's wrong but not even he knows. Delilah's mom calls for her. She leaves to go get help."
    hide julian with dissolve
    $ loop2_investigate = True
    jump open_door