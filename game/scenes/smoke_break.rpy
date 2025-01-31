# The script of the game goes in this file.

label smoke_break:

    $ in_house = False

    show bg scene3 with dissolve
    show sandra neutral onlayer characters at center with dissolve
    delilah_thoughts_run3 "Mom leans over the railing holding an unlit cigarrette between her fingers. I get as close as I can stomach."
    delilah_thoughts_run3 "Dad used to always say how nasty they smelled. Mom quit for a long time because of it."
    show sandra sad onlayer characters
    sandra_run3_d "I know, I know. You don't have to say it."
    menu:
        delilah " " (callback = functools.partial(inctime))
        "{color=#0f0}Mention Julian{/color}":
            delilah_thoughts_run3 "Mention Julian"
        "{color=#0f0}Don't mention Julian{/color}":
            delilah_thoughts_run3 "Don't mention Julian"
    delilah_thoughts_run3 "The thought enters my mind to mention Julian, his condition, and the magical glowing flower that I need to get from my brother. But then I remember how Mom reacted in the previous loop with complete and utter indifference."
    delilah_run3 angry "I don't care, smoke all you want, Sandra."
    show sandra neutral onlayer characters
    sandra_run3_d "You know, it wasn't that long ago you used to call me 'Mom'."
    delilah_run3 "Really? Feels like a lifetime ago."
    show sandra laugh onlayer characters
    sandra_run3_d "Yeah, a whole three months. I kept track. The first time came as a bit of a shock."
    delilah_run3 "You don't have any idea what changed?" 
    show sandra neutral onlayer characters
    sandra_run3_d "I don't know. Teenage angst?"
    if run == 3:
        "{color=#0f0}The image of that letter is burned into her mind forever.\nCuriosity got the best of her, she went looking through her dad's belongings, and found what she suspected but couldn't imagine.{/color}"
        hide sandra onlayer characters
        show bg black
        with dissolve
        "{color=#0f0}'You are so special to me' the letter said.\n'I wish we could see each other more. Your scent on my pillow haunts me like a sexy ghost.'\n'When you're with me, I feel at home. You are my home.'\n'There will always be a place for you here. Love, Charice'{/color}"
        "{color=#0f0}The first time she read it, she thought it must have been a joke or at the very worst a one-time affair.\nRich men slept with women all the time, right? That's what they do. Men can't help themselves.{/color}"
        "{color=#0f0}She kept the letter.\nFor days, she watched her dad's mannerisms carefully.\nShe searched the way he reached for his drink at the dinner table for any semblance of guilt.\nShe looked into the creases of his smile for any sly deceitfulness.\nWhen none could be found, she wondered if she ever knew her dad to begin with.\nShe wondered if her mom ever knew her husband to begin with.\nWas her entire family built on a lie?{/color}"
        "{color=#0f0}Delilah took the letter and placed it in Sandra's dresser drawer, hoping to raise alarms.{/color}"
        show bg scene3
        show sandra neutral onlayer characters at center
        with dissolve
    delilah_run3 neutral "You saw the letter."
    sandra_run3_d "The what?"
    delilah_run3 angry "The letter. Unless you haven't changed socks in three months, I know you saw it."
    sandra_run3_d "I don't know what you're referring..."
    delilah_run3 "Fuck, Sandra, stop it! I'm the one who put the letter there! I know you read it! You know Dad is cheating on you! So why are you pretending like everything is normal?!"
    show sandra sad onlayer characters
    delilah_thoughts_run3 "Mom turns to ice. The cigarette in her hand starts to lightly scorch the edges of her fingers."
    show sandra angry onlayer characters
    sandra_run3_d "How long have you known?"
    delilah_thoughts_run3 "Her voice is like a pile of glass shards embedded in her throat."
    delilah_run3 "Like I said, the entire time. I've known longer than you have."
    sandra_run3_d "Del...I wanted to protect you..."
    delilah_run3 "Well, what a great job you did!"
    show sandra sad onlayer characters
    sandra_run3_d "I've been making arrangements, setting myself up to leave. I wanted to wait till things were ready to tell you."
    delilah_run3 worried "And then what? Just drop it on us? 'Hey, kids, our family is a sham! Thanks and goodbye?'"
    show sandra angry onlayer characters
    sandra_run3_d "I...I didn't mean to hurt you, Del. I'm sorry. Please, just try to understand that I truly am doing my best. You're not the only one who doesn't know what to believe in anymore after all this."
    delilah_run3 "Yeah, well, I had to go through it alone."
    sandra_run3_d "So did I."
    delilah_run3 happy "Well...you don't have to. We can go through it together."
    show sandra neutral onlayer characters
    sandra_run3_d "Yeah. I think I'd like that."
    if run == 3:
        "{color=#0f0}For the first time in a while, Delilah felt the experience of belonging in her family. Things weren't resolved, not by a longshot, but she knew she wasn't alone.{/color}"
    sandra_run3_d neutral "Maybe we leave Cody out of this for now though? I don't think he could handle this. He looks up to his dad so much. It would destroy his world."
    delilah_run3 "Yeah. I'll be careful not to tell him."
    delilah_thoughts_run3 happy "We share a pleasant silence for a moment."

    # delilah "Delilah and Sandra talk. Delilah considers telling her about Julian but doesn't even bother since she's already seen that her mom doesn't care and will do nothing. In this scene, Delilah reveals to her mom that she knows about her father's infidelity. Sandra is shocked at first, not sure what to make of this discovery. She apologizes for not saying something sooner, but justifies her actions as best as she can. Sandra really is just doing her best while trying to hide her broken heart from her children."
    # delilah "She ends the conversation by saying \"don't tell your brother, I don't think he could handle it.\""
    # delilah goes back inside
    menu:
        delilah " " (callback = functools.partial(inctime))
        "{color=#0f0}Go back inside{/color}":
            delilah_thoughts_run3 neutral "Go back inside"

    hide sandra onlayer characters with dissolve
    $ in_house = True
    show bg scene2 with dissolve
    show cody happy onlayer characters at center with dissolve
    delilah_thoughts_run3 "Cody's still sitting at the table."
    $ smoke_break = True
    return