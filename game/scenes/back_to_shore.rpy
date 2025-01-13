# The script of the game goes in this file.

label back_to_shore:
    delilah "Delilah goes to the shore to find Julian there again. They're both confused as to how they're alive but they think the Selene Lillies are the source of this. They talk a bit about the time loop situation they're in. Julian shares what he knows about the Selene Lillies: that they're extremely rare and mysterious flowers local to his world. Julian explains that he was in the process of making a bouquet when he found himself here. He thinks that by getting all five flowers he might be able to break the loop and go home. Because of his unstable physical state, he needs Delilah to find all five flowers on her own."
    delilah "The player can come back to this scene at any time during the third loop to engage in optional dialogue with Julian."
    delilah "When the player is done with this conversation, Delilah can hear her mom calling and can then unlock the door for her mom"
    hide julian onlayer characters with dissolve
    $ loop3_investigate = True
    jump open_door