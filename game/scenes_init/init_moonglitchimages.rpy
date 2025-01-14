# This script runs before game start and defines the images for the moon glitches

label init_moonglitchimages:

    image moon_phase1 = ConditionSwitch(
        "run == 2 and moonglitch2 == True and not solves.loop2", "moon_phase1_glitch",
        "True", "images/props/moon_phase1.png")
    image moon_phase2 = ConditionSwitch(
        "run == 2 and moonglitch1 == True and not solves.loop2", "moon_phase2_glitch",
        "run == 2 and moonglitch3 == True and not solves.loop2", "moon_phase2_glitch2",
        "True", "images/props/moon_phase2.png")
    image moon_phase3 = ConditionSwitch(
        "run == 2 and moonglitch4 == True and not solves.loop2", "moon_phase3_glitch",
        "True", "images/props/moon_phase3.png")
    image moon_phase4 = ConditionSwitch(
        "run == 2 and moonglitch5 == True and not solves.loop2", "moon_phase4_glitch",
        "True", "images/props/moon_phase4.png")
    image moon_phase5 = "images/props/moon_phase5.png"

    image moon_phase1_glitch:
        Glitch("images/props/moon_phase1.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
        linear 1
        "images/props/moon_phase2.png"
    image moon_phase2_glitch:
        Glitch("images/props/moon_phase2.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
        linear 1
        "images/props/moon_phase1.png"
    image moon_phase2_glitch2:
        Glitch("images/props/moon_phase2.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
        linear 1
        "images/props/moon_phase3.png"
    image moon_phase3_glitch:
        Glitch("images/props/moon_phase3.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
        linear 1
        "images/props/moon_phase4.png"
    image moon_phase4_glitch:
        Glitch("images/props/moon_phase4.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
        linear 1
        "images/props/moon_phase5.png"

    return