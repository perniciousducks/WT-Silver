label too_much:
    $ renpy.block_rollback()
    stop music fadeout 2.0
    call her_main("[genie_name]??!", "shock", "wide", "base", "stare",xpos="mid",trans=fade)
    her "How could you ask for such a thing!?"
    call her_main("I think I better leave.", "angry", "happyCl", "worried", "mid",emote="05")

    call her_walk(action="leave")

    $ her_mood += 6

    play music "music/Final Fantasy 7 Game Over Theme.mp3" fadein 1 fadeout 1
    jump game_over


label very_no:
    $ renpy.block_rollback()
    stop music fadeout 2.0
    call her_main("Absolutely not!", "annoyed", "narrow", "angry", "R",xpos="mid",trans=fade)
    her "I'll show you that my integrity and honour as a Gryffindor cannot be bought!"
    call her_main("I'm leaving this instant.", "scream", "closed", "angry", "mid")

    call her_walk(action="leave")

    $ her_mood += 9

    play music "music/Final Fantasy 7 Game Over Theme.mp3" fadein 1 fadeout 1
    jump game_over


label game_over:
    stop bg_sounds fadeout 4
    show screen blkfade
    with d5

    pause 1
    centered "{size=+7}{color=#cbcbcb}Game Over...{/color}{/size}"
    call ctc

    $ MainMenu(confirm=False)
    #$ renpy.full_restart()
