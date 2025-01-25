# This script runs before game start and defines the UI screens

label init_screens:

    screen moonglitchscreen: # screen for showing moon glitch status
        # text "Time [gametime]" xpos 0.1 ypos 0.1
        if run==2 and puzzles.loop2 and not solves.loop2:
            if moonglitches.glitch1:
                add 'images/props/moon_phase1.png' zoom 0.3 xpos 0.075 ypos 0.175
            else:
                # add Glitch("images/props/moon_phase1.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") zoom 1.0 xpos 0.1 ypos 0.15 # glitched version
                add 'images/props/moonglitch1_UI.png' zoom 0.3 xpos 0.075 ypos 0.175

            if moonglitches.glitch2:
                add 'images/props/moon_phase2.png' zoom 0.3 xpos 0.125 ypos 0.175
            else:
                # add Glitch("images/props/moon_phase2.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") zoom 0.3 xpos 0.15 ypos 0.15 # glitched version
                add 'images/props/moonglitch2_UI.png' zoom 0.3 xpos 0.125 ypos 0.175

            if moonglitches.glitch3:
                add 'images/props/moon_phase3.png' zoom 0.3 xpos 0.175 ypos 0.175
            else:
                # add Glitch("images/props/moon_phase3.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") zoom 0.3 xpos 0.2 ypos 0.15 # glitched version
                add 'images/props/moonglitch3_UI.png' zoom 0.3 xpos 0.175 ypos 0.175


            if moonglitches.glitch4:
                add 'images/props/moon_phase4.png' zoom 0.3 xpos 0.225 ypos 0.175
            else:
                # add Glitch("images/props/moon_phase4.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") zoom 0.3 xpos 0.25 ypos 0.15 # glitched version
                add 'images/props/moonglitch4_UI.png' zoom 0.3 xpos 0.225 ypos 0.175

            if moonglitches.glitch5:
                add 'images/props/moon_phase5.png' zoom 0.3 xpos 0.275 ypos 0.175
            else:
                # add Glitch("images/props/moon_phase5.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") zoom 0.3 xpos 0.3 ypos 0.15 # glitched version
                add 'images/props/moonglitch5_UI.png' zoom 0.3 xpos 0.275 ypos 0.175

            # text "Glitches: 1-[moonglitches.glitch1] 2-[moonglitches.glitch2] 3-[moonglitches.glitch3] 4-[moonglitches.glitch4] 5-[moonglitches.glitch5]" xpos 0.1 ypos 0.1
        if run==2 and solves.loop2:
            # text "Glitches: solved!" xpos 0.1 ypos 0.1
            add 'images/props/moon_phase1.png' zoom 0.3 xpos 0.075 ypos 0.175
            add 'images/props/moon_phase2.png' zoom 0.3 xpos 0.125 ypos 0.175
            add 'images/props/moon_phase3.png' zoom 0.3 xpos 0.175 ypos 0.175
            add 'images/props/moon_phase4.png' zoom 0.3 xpos 0.225 ypos 0.175
            add 'images/props/moon_phase5.png' zoom 0.3 xpos 0.275 ypos 0.175

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
            add 'images/props/flower_hover.png' zoom 0.5 xpos 0.05 ypos 0.0
            # text "Flower 1" xpos 0.1 ypos 0.15
        if flowers.flower2:
            if solves.loop2:
                add 'images/props/flower_hover.png' zoom 0.5 xpos 0.1 ypos 0.0
            else:
                add 'images/props/flower.png' zoom 0.5 xpos 0.1 ypos 0.0
        if flowers.flower3:
            if solves.loop3:
                add 'images/props/flower_hover.png' zoom 0.5 xpos 0.15 ypos 0.0
            else:
                add 'images/props/flower.png' zoom 0.5 xpos 0.15 ypos 0.0
        if flowers.flower4:
            if solves.loop4:
                add 'images/props/flower_hover.png' zoom 0.5 xpos 0.2 ypos 0.0
            else:
                add 'images/props/flower.png' zoom 0.5 xpos 0.2 ypos 0.0

    screen flower1_pick:
        imagebutton:
            xalign 0.5
            yalign 0.6
            idle "images/props/flower.png"
            hover "images/props/flower_hover.png"
            action [SetVariable("flowers.flower1", 1), SetVariable("config.rollback_enabled", False), Hide("flower1_pick"), Return()]
    screen flower2_pick:
        imagebutton:
            xalign 0.5
            yalign 0.5
            idle "images/props/flower.png"
            hover "images/props/flower_hover.png"
            action [SetVariable("flowers.flower2", 1), SetVariable("config.rollback_enabled", False), Hide("flower2_pick"), Return()]
    screen flower3_pick:
        imagebutton:
            xalign 0.5
            yalign 0.6
            idle "images/props/flower.png"
            hover "images/props/flower_hover.png"
            action [SetVariable("flowers.flower3", 1), SetVariable("config.rollback_enabled", False), Hide("flower3_pick"), Return()]
    screen flower4_pick:
        imagebutton:
            xalign 0.5
            yalign 0.6
            idle "images/props/flower.png"
            hover "images/props/flower_hover.png"
            action [SetVariable("flowers.flower4", 1), SetVariable("config.rollback_enabled", False), Hide("flower4_pick"), Return()]
    screen flower_glitch:
        if puzzles.loop2:
            imagebutton:
                xalign 0.5
                yalign 0.5
                idle Glitch("images/props/flower.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
        else:
            add Glitch("images/props/flower.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") xalign 0.5 yalign 0.5
    screen flower_glitch_final: # 3 flowers glitched
        if puzzles.loop2:
            imagebutton:
                xalign 0.5
                yalign 0.5
                idle Glitch("images/props/flower.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
        else:
            add Glitch("images/props/flower.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") xalign 0.5 yalign 0.5
    screen flower2_glitch_pick:
        imagebutton:
            xalign 0.5
            yalign 0.5
            idle Glitch("images/props/flower.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
            hover Glitch("images/props/flower_hover.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
            action [SetVariable("flowers.flower2", 1), SetVariable("config.rollback_enabled", False), Hide("flower2_pick"), Return()]
    screen flower3_glitch_pick:
        imagebutton:
            xalign 0.5
            yalign 0.5
            idle Glitch("images/props/flower.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
            hover Glitch("images/props/flower_hover.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
            action [SetVariable("flowers.flower3", 1), SetVariable("config.rollback_enabled", False), Hide("flower3_pick"), Return()]
    screen flower4_glitch_pick: # 3 flowers glitched
        imagebutton:
            xalign 0.5
            yalign 0.5
            idle Glitch("images/props/flower.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
            hover Glitch("images/props/flower_hover.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
            action [SetVariable("flowers.flower4", 1), SetVariable("config.rollback_enabled", False), Hide("flower4_pick"), Return()]


    screen howtoplay:
        text "[playtext]" xalign 0.5 yalign 0.5 text_align 0.5
        
    screen endscreen:
        text "{size=100}END{/size}" xalign 0.5 yalign 0.5

    return