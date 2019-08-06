

label end_hermione_event:
    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3

    call her_chibi(action="hide")

    $ hermione_busy = True

    jump main_room


label too_much:
    stop music fadeout 2.0
    call her_main("[genie_name]??!","shock","wide",xpos="mid",trans="fade")
    her "How could you ask for such a thing!?"
    call her_main("I think I better leave.","angry","worriedCl",emote="05")

    call her_walk(action="leave", speed=2.5)

    $ her_mood += 6

    jump end_hermione_event


label very_no:
    stop music fadeout 2.0
    call her_main("Absolutely not!","annoyed","angryL",xpos="mid",trans="fade")
    her "I'll show you that my integrity and honour as a Gryffindor cannot be bought!"
    call her_main("I'm leaving this instant.","scream","angryCl")

    call her_walk(action="leave", speed=2.5)

    $ her_mood += 9

    jump end_hermione_event



label her_walk_desk_blkfade:

    hide screen bld1
    hide screen blktone
    hide screen hermione_main
    with d3
    pause.2

    call her_walk(xpos="desk", ypos="base", speed=2, loiter=False, redux_pause=2)
    call blkfade

    return



label hg_chibi_transition(action="stand", xpos="mid", ypos="base", flip=False, trans="fade"):
    call hide_characters
    show screen blkfade

    $ menu_y = 0.75 # Menu moved down.
    call her_chibi("hide")
    call gen_chibi("hide")

    if action in ["lift_top", "lift_skirt"]:
        $ menu_y = 0.5
        call her_chibi(action, xpos, ypos, flip)
        call gen_chibi("sit_behind_desk")

    elif action in ["admire_breasts"]:
        show screen genie_and_tits_01

    elif action in ["stand_behind_desk"]:
        if flip:
            show screen no_groping_02 # Towards Door.
        else:
            show screen no_groping_01 # Towards Cupboard.

    elif action in ["admire_ass","admire_ass_jerk_off","admire_ass_cum"]:
        if action == "admire_ass": # Bend over desk, with clothes on.
            show screen hermione_chibi_ass(ani=action)
        else:
            show screen chair_left
            if flip:
                $ masturbating = True
                if action == "admire_ass_jerk_off":
                    call gen_chibi("jerking_off","behind_desk","base") # Fix position
                if action == "admire_ass_cum":
                    call gen_chibi("cumming","behind_desk","base") # Fix position
            show screen no_groping_02

    elif action in ["grope_breasts"]:
        show screen chair_left

        if hermione_use_action and hermione_action in ["lift_top"]:
            show screen groping_naked_tits
        else:
            show screen groping_03

    elif action in ["grope_ass"]:
        if flip:
            show screen groping_02 # Towards Door.
        else:
            show screen groping_01 # Towards Cupboard.

    elif action in ["jerk_off"]:
        show screen chair_left
        show screen jerking_off_01

    ### Handjob ###
    elif action in ["hj","hj_pause","hj_kiss","hj_cumming_in","hj_cumming_in_pause","hj_cumming_on","hj_cumming_on_pause"]:
        show screen chair_left
        show screen desk
        show screen hermione_chibi_hj(ani=action, xpos=230, ypos=0)

    ### Blowjob ###
    elif action in ["bj","bj_pause","bj_cumming_in","bj_cumming_out","bj_cumming_out_blink"]:
        show screen chair_left
        show screen hermione_chibi_bj(ani=action)
        if action in ["bj_cumming_out","bj_cumming_out_blink"]:
            $ uni_sperm = True
            $ u_sperm = "characters/hermione/face/auto_08.png"

    ### Sex ###
    elif action in ["sex","sex_slow","sex_fast","sex_pause","sex_cumming_out","sex_cumming_out_blink","sex_creampie","sex_creampie_pause"]:
        show screen chair_left
        show screen hermione_chibi_sex(ani=action)
        if action in ["sex_cumming_out","sex_cumming_out_blink","sex_creampie","sex_creampie_pause"]:
            $ uni_sperm = True
            $ u_sperm = "characters/hermione/face/auto_08.png"

    else:
        $ menu_y = 0.5
        call reset_hermione
        call her_chibi("stand", xpos, ypos)
        call gen_chibi("sit_behind_desk")

    hide screen bld1
    hide screen blkfade
    if trans != "fade":
        call transition(trans)
    else:
        with fade # Default

    return
