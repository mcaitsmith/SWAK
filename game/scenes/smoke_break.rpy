# The script of the game goes in this file.

label smoke_break:
    show bg scene3 with dissolve
    show sandra neutral at right with dissolve
    delilah "Delilah and Sandra talk. Delilah considers telling her about Julian but doesn't even bother since she's already seen that her mom doesn't care and will do nothing. In this scene, Delilah reveals to her mom that she knows about her father's infidelity. Sandra is shocked at first, not sure what to make of this discovery. She apologizes for not saying something sooner, but justifies her actions as best as she can. Sandra really is just doing her best while trying to hide her broken heart from her children."
    delilah "She ends the conversation by saying \"don't tell your brother, I don't think he could handle it.\""
    # delilah goes back inside
    hide sandra with dissolve
    show bg scene2 with dissolve
    show cody happy at center with dissolve
    $ smoke_break = True
    return