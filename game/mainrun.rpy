﻿# The script of the game goes in this file.

label mainrun:

    # show delilah neutral at left with dissolve

    # delilah neutral "Dialogue START{alt}{noalt}{color=#f00} hidden code{/color}{/noalt}{/alt}"
    pause 2.0

    call intro from _call_intro

    if restart_vars:
        hide screen eclipse onlayer background_overlay with dissolve
        $ _skipping = True
        jump runstart

    if true_ending:
        "CREDITS HERE"
        hide screen eclipse onlayer background_overlay
        stop music fadeout 1.0
        pause 1.0

    else:

        $ renpy.choice_for_skipping() # stop skipping
        $ _skipping = False

        # delilah neutral "Dialogue END"
        pause 2.0
        show screen endscreen
        $ renpy.pause()
        # "END"

        # hide delilah with dissolve

        show bg black
        hide screen flowerscreen onlayer interface
        with dissolve

        $ renpy.pause()

        hide screen eclipse onlayer background_overlay
        hide screen endscreen
        show screen endscreenq
        with dissolve

        $ renpy.pause()

        stop music fadeout 1.0
        hide screen endscreenq with dissolve

    return
