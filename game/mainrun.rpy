# The script of the game goes in this file.

label mainrun:

    show delilah happy at left with dissolve

    delilah "Dialogue START{alt}{noalt}{color=#f00} hidden code{/color}{/noalt}{/alt}"

    call intro

    delilah "Dialogue END"

    hide delilah with dissolve

    show bg black with dissolve

    return
