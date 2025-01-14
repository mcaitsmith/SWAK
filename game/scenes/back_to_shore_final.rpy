# The script of the game goes in this file.

label back_to_shore_final:

    call incphase

    "8 PM"
    pause 1.0

    delilah "At the shore, Julian is standing there waiting for you to meet with him. Deliah tells him about the conversation she just had with Cody, how difficult it was. Julian feels for her and apologizes for putting her through that. This confuses Delilah since his life is at stake. Sort of dwarfs in comparison. Julian doesn't see it that way. His martyr complex comes through in this moment."
    delilah "They discuss that there is only ONE flower left to find. Delilah is confounded by where it could be. Julian acts suspicious, clutching his shirt pocket. Delilah notices that it's glowing and asks what he has."
    delilah "Julian admits to having the flower and apologizes. He admits that he's enjoyed being here with her and wants to be there to comfort her for the family crisis that she's about to endure when she goes home."
    # delilah takes flower
    if not flowers.flower4:
        delilah "Delilah takes the flower" (callback = functools.partial(inctime, fnum=4))
    else:
        pass

    call incphase # should end up at totality for final choice

    delilah "Delilah has three possible choices she can follow from here:"
    menu:
        delilah "Dialogue choice" (callback = functools.partial(inctime))
        "Ending 1":
            delilah "Delilah can force Julian to take the flowers and go home, resulting in a heartfelt moment in which they tearfully say goodbye and kiss. The story ends with her going to take care of her brother and mom as they endure the crisis that lies ahead."
            hide julian onlayer characters with dissolve
            show bg black with dissolve
            $ endings.ending1 = True
            return
        "Ending 2":
            delilah "Delilah can embrace Julian with the flowers and follow him back to his world where she will suddenly be trapped in a time loop there."
            # hide delilah with dissolve
            show bg black with dissolve
            $ endings.ending2 = True
            return
        "Ending 3":
            delilah "Delilah can agree to remain in the time loop with him as the game simply restarts and the time loop begins again."
            # for this ending instead of actually restarting just show the intro again in the credit sequence
            show bg black with dissolve
            $ endings.ending3 = True
            return