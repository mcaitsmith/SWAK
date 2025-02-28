﻿# This script runs before game start and defines the UI screens

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
            if in_house:
                add 'images/props/moon.png' zoom 0.8 xalign 1.0 ypos 0.19
            else:
                add 'images/props/moon.png' zoom 0.8 xalign 0.68 ypos 0.05
        elif phase == 1:
            if in_house:
                add 'moon_phase1' zoom 0.8 xalign 1.0 ypos 0.19
            else:
                add 'moon_phase1' zoom 0.8 xalign 0.68 ypos 0.05
        elif phase == 2:
            if in_house:
                add 'moon_phase2' zoom 0.8 xalign 1.0 ypos 0.19
            else:
                add 'moon_phase2' zoom 0.8 xalign 0.68 ypos 0.05
        elif phase == 3:
            if in_house:
                add 'moon_phase3' zoom 0.8 xalign 1.0 ypos 0.19
            else:
                add 'moon_phase3' zoom 0.8 xalign 0.68 ypos 0.05
        elif phase == 4:
            if in_house:
                add 'moon_phase4' zoom 0.8 xalign 1.0 ypos 0.19
            else:
                add 'moon_phase4' zoom 0.8 xalign 0.68 ypos 0.05
        elif phase == 5:
            if in_house:
                add 'moon_phase5' zoom 0.8 xalign 1.0 ypos 0.19
            else:
                add 'moon_phase5' zoom 0.8 xalign 0.68 ypos 0.05

    screen flowerscreen: # screen for showing flowers
        if flowers.flower1:
            add 'images/props/flower.png' zoom 0.5 xpos 0.05 ypos 0.0
            # text "Flower 1" xpos 0.1 ypos 0.15
        if flowers.flower2:
            add 'images/props/flower.png' zoom 0.5 xpos 0.1 ypos 0.0
            # if solves.loop2:
            #     add 'images/props/flower_hover.png' zoom 0.5 xpos 0.1 ypos 0.0
            # else:
            #     add 'images/props/flower.png' zoom 0.5 xpos 0.1 ypos 0.0
        if flowers.flower3:
            add 'images/props/flower.png' zoom 0.5 xpos 0.15 ypos 0.0
            # if solves.loop3:
            #     add 'images/props/flower_hover.png' zoom 0.5 xpos 0.15 ypos 0.0
            # else:
            #     add 'images/props/flower.png' zoom 0.5 xpos 0.15 ypos 0.0
        if flowers.flower4:
            add 'images/props/flower.png' zoom 0.5 xpos 0.2 ypos 0.0
            # if solves.loop4:
            #     add 'images/props/flower_hover.png' zoom 0.5 xpos 0.2 ypos 0.0
            # else:
            #     add 'images/props/flower.png' zoom 0.5 xpos 0.2 ypos 0.0

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
    screen endscreenq:
        text "{size=100}END?{/size}" xalign 0.5 yalign 0.5

    # transform endflip:
    #     xalign 0.5 
    #     yalign 0.5 
    #     xzoom -1.0
    # screen endscreenqr:
    #     text "{size=100}END?{/size}" at endflip
    screen endscreenqr:
        text "{size=100}END{/size}" xalign 0.5 yalign 0.8

    screen creditscreen:
        text "{font=retro_party.ttf}{size=100}CREDITS{/size}{/font}" xalign 0.5 yalign 0.2
        text "{a=https://itch.io/profile/merrygold}Merrygold{/a} - Programmer and Designer" xalign 0.5 yalign 0.35
        text "{a=https://itch.io/profile/patty-o}Patty-O{/a} - Writer" xalign 0.5 yalign 0.4
        text "{a=https://ryu-san.itch.io/}Ryu_San{/a} - Character Artist" xalign 0.5 yalign 0.45
        text "CorvidClowns & {a=https://tooooffeeart.itch.io/}TooooffeeArt{/a} - Background Artists" xalign 0.5 yalign 0.5
        text "{a=www.circlesinthesky.com}Skyler Newsome{/a} - Composer" xalign 0.5 yalign 0.55
        text "Special thanks to Vika for playtesting" xalign 0.5 yalign 0.65

    screen hintstory:

        tag menu

        ## Avoid predicting this screen, as it can be very large.
        predict False

        use game_menu(_("Hints"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

            style_prefix "history"

            # for h in _history_list:
            # for h in [] + ([hint_1] if hints.hint1 else []) + ([hint_2] if hints.hint2 else []) + ([hint_3] if hints.hint3 else []):
            for h in hintlist.list:

                window:

                    ## This lays things out properly if history_height is None.
                    has fixed:
                        yfit True

                    # if h.who:

                    #     label h.who:
                    #         style "history_name"
                    #         substitute False

                    #         ## Take the color of the who text from the Character, if
                    #         ## set.
                    #         if "color" in h.who_args:
                    #             text_color h.who_args["color"]

                    # $ what = renpy.filter_text_tags(h, allow=gui.history_allow_tags)
                    $ what = renpy.filter_text_tags(h, allow=['i','b'])

                    # $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False

            # if not _history_list:
            #     label _("The dialogue history is empty.")

    return