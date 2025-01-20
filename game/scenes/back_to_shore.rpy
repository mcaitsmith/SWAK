# The script of the game goes in this file.

label back_to_shore:
    # zoom bg plus sfx
    delilah_thoughts_run3 "When I get to the bottom of the hill, Julian is already waiting for me."
    show julian neutral onlayer characters at center
    pause 1.0
    julian_run3 "Back so soon?"
    delilah_run3 "After you died, I found this."
    delilah_thoughts_run3 "I hold out the second flower."
    julian_run3 "Ah, pretty. Why thank you." # He says dryly. (expression)
    delilah_run3 "Yeah, I broke my neck to get it."
    julian_run3 "You broke...? Oh, God, I'm so sorry. Why?"
    delilah_run3 "Call it a hunch, but I'm guessing these have something to do with this condition of ours. What do you know about them?"
    julian_run3 "These? They're Selene Lillies. Extremely rare luminescent flowers. They're what I was gathering before."
    delilah_run3 "You don't think they have something to do with all of...this?"
    julian_run3 "I think that's a bit out there, Delilah. I think it's bizarre, and a bit of a reach. But then again, I've died multiple times in the past twelve hours, so I'm liable to believe whatever you tell me."
    delilah_run3 "When I got this second flower I noticed...I don't know...something new. I was suddenly able to see more possible outcomes if that makes sense."
    julian_run3 "Not really."
    delilah_run3 "How many flowers did you have before you wound up here?"
    julian_run3 "Four. Was putting together a bouquet for my folks' shop. Just four Selene Lillies would sell for enough to keep the lights on for a year."
    delilah_run3 "So maybe if we get all four together we can send you home and break the loop?"
    julian_run3 "Couldn't hurt to try, I suppose. We're halfway there already."
    delilah_run3 "Where do you think we should start looking?" 
    julian_run3 "You know the area better than I do."
    # delilah "Delilah goes to the shore to find Julian there again. They're both confused as to how they're alive but they think the Selene Lillies are the source of this. They talk a bit about the time loop situation they're in. Julian shares what he knows about the Selene Lillies: that they're extremely rare and mysterious flowers local to his world. Julian explains that he was in the process of making a bouquet when he found himself here. He thinks that by getting all five flowers he might be able to break the loop and go home. Because of his unstable physical state, he needs Delilah to find all five flowers on her own."
    delilah "The player can come back to this scene at any time during the third loop to engage in optional dialogue with Julian."
    delilah "When the player is done with this conversation, Delilah can hear her mom calling and can then unlock the door for her mom"
    hide julian onlayer characters with dissolve
    $ loop3_investigate = True
    jump open_door