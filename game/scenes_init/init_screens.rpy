# This script runs before game start and defines the UI screens

label init_screens:

    screen moonglitchscreen: # screen for showing moon glitch status
        # text "Time [gametime]" xpos 0.1 ypos 0.1
        if run==2 and puzzles.loop2 and not solves.loop2:
            if moonglitches.glitch1:
                add 'images/props/moon_phase1.png' zoom 0.3 xpos 0.1 ypos 0.15
            else:
                add Glitch("images/props/moon_phase1.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") zoom 0.3 xpos 0.1 ypos 0.15 # glitched version

            if moonglitches.glitch2:
                add 'images/props/moon_phase2.png' zoom 0.3 xpos 0.15 ypos 0.15
            else:
                add Glitch("images/props/moon_phase2.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") zoom 0.3 xpos 0.15 ypos 0.15 # glitched version

            if moonglitches.glitch3:
                add 'images/props/moon_phase3.png' zoom 0.3 xpos 0.2 ypos 0.15
            else:
                add Glitch("images/props/moon_phase3.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") zoom 0.3 xpos 0.2 ypos 0.15 # glitched version

            if moonglitches.glitch4:
                add 'images/props/moon_phase4.png' zoom 0.3 xpos 0.25 ypos 0.15
            else:
                add Glitch("images/props/moon_phase4.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") zoom 0.3 xpos 0.25 ypos 0.15 # glitched version

            if moonglitches.glitch5:
                add 'images/props/moon_phase5.png' zoom 0.3 xpos 0.3 ypos 0.15
            else:
                add Glitch("images/props/moon_phase5.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") zoom 0.3 xpos 0.3 ypos 0.15 # glitched version

            # text "Glitches: 1-[moonglitches.glitch1] 2-[moonglitches.glitch2] 3-[moonglitches.glitch3] 4-[moonglitches.glitch4] 5-[moonglitches.glitch5]" xpos 0.1 ypos 0.1
        if run==2 and solves.loop2:
            # text "Glitches: solved!" xpos 0.1 ypos 0.1
            add 'images/props/moon_phase1.png' zoom 0.3 xpos 0.1 ypos 0.15
            add 'images/props/moon_phase2.png' zoom 0.3 xpos 0.15 ypos 0.15
            add 'images/props/moon_phase3.png' zoom 0.3 xpos 0.2 ypos 0.15
            add 'images/props/moon_phase4.png' zoom 0.3 xpos 0.25 ypos 0.15
            add 'images/props/moon_phase5.png' zoom 0.3 xpos 0.3 ypos 0.15

    screen eclipse: # screen for showing eclipse

        if phase == 0 or phase > 5:
            add 'images/props/moon.png' xalign 0.5 ypos 0.05
        elif phase == 1:
            add 'moon_phase1' xalign 0.5 ypos 0.05
            # text "test" xalign 0.5 ypos 0.2
        elif phase == 2:
            add 'moon_phase2' xalign 0.5 ypos 0.05
        elif phase == 3:
            add "moon_phase3" xalign 0.5 ypos 0.05
        elif phase == 4:
            add "moon_phase4" xalign 0.5 ypos 0.05
        elif phase == 5:
            add "moon_phase5" xalign 0.5 ypos 0.05

    screen flowerscreen: # screen for showing flowers
        if flowers.flower1:
            add 'images/props/flower.png' zoom 0.5 xpos 0.1 ypos 0.025
            # text "Flower 1" xpos 0.1 ypos 0.15
        if flowers.flower2:
            add 'images/props/flower.png' zoom 0.5 xpos 0.15 ypos 0.025
        if flowers.flower3:
            add 'images/props/flower.png' zoom 0.5 xpos 0.2 ypos 0.025
        if flowers.flower4:
            add 'images/props/flower.png' zoom 0.5 xpos 0.25 ypos 0.025

    screen flower1_pick:
        imagebutton:
            xalign 0.5
            yalign 0.5
            idle "images/props/flower.png"
            hover "images/props/flower_hover.png"
            action [SetVariable("flowers.flower1", 1), Hide("flower1_pick"), Return()]
    screen flower2_pick:
        imagebutton:
            xalign 0.5
            yalign 0.5
            idle "images/props/flower.png"
            hover "images/props/flower_hover.png"
            action [SetVariable("flowers.flower2", 1), Hide("flower2_pick"), Return()]
    screen flower_glitch:
        imagebutton:
            xalign 0.5
            yalign 0.5
            idle Glitch("images/props/flower.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version

    return