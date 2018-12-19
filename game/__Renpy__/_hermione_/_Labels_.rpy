

label end_hg_pf: #Hides screens. Hermione walks out. Resets Hermione.
    hide screen hermione_main

    hide screen bld1
    hide screen blktone

    if hermione_chibi_xpos_name in ["desk"]:
        call her_chibi("stand","desk","base")
    elif hermione_chibi_xpos_name in ["mid"]:
        call her_chibi("stand","mid","base")
    else:
        call her_chibi("hide")

    call gen_chibi("sit_behind_desk")

    with d3

    #Walk
    if hermione_chibi_xpos_name in ["desk"]:
        call her_walk("desk","leave",2.7)
    if hermione_chibi_xpos_name in ["mid"]:
        call her_walk("mid","leave",2)

    call reset_hermione

    $ hermione_busy = True

    jump main_room



label hg_pr_transition_block:

    hide screen bld1
    hide screen hermione_main
    hide screen blktone
    with d3

    if hermione_chibi_xpos_name == "desk":
        call her_walk("desk","leave",2.7)
    elif hermione_chibi_xpos_name == "mid":
        call her_walk("mid","leave",2)
    else:
        call her_chibi("leave")

    $ hermione_busy = True

    jump main_room



label could_not_flirt: #Sent here when choose "Favour failed! No points for you!" (Hermione is leaving without getting any points).

    show screen blkfade #Should be active anyways.

    hide screen hermione_main
    hide screen hermione_main_ass

    hide screen chair_left
    hide screen desk
    hide screen groping_naked_tits
    hide screen genie_and_tits_01
    hide screen jerking_off_01 #Hermione topless. Genie jerking off.
    if hermione_chibi_xpos_name == "desk":
        call her_chibi("stand","desk","base")
    else:
        call her_chibi("stand","mid","base")
    show screen genie

    hide screen bld1
    hide screen blktone
    hide screen blkfade
    with fade

    if hermione_chibi_xpos_name == "desk":
        call her_walk("desk","leave",2.7)
    else:
        call her_walk("mid","leave",2)

    $ hermione_busy = True

    jump main_room



### MUSIC BLOCK ###
label music_block:
    if daytime:
        call play_music("day_theme")
    else:
        call play_music("night_theme")
    return

### YOU LUCK IMAGINATION ###
label vague_idea:

    call nar(">You lack imagination for an idea of this caliber.")

    return





label her_walk_desk_blkfade:

    hide screen bld1
    hide screen blktone
    hide screen hermione_main
    with d3
    pause.2

    call her_walk("mid","desk",2,loiter=False, redux_pause = 2)
    call blkfade

    return

#############This massage shows when you make a request, and Hermione refuses because she is not slutty enough yet.
label too_much:
    stop music fadeout 2.0
    call her_main("[genie_name]??!","shock","wide",xpos="mid",trans="fade")
    her "How could you ask for such a thing!?"
    call her_main("I think I better leave.","angry","worriedCl",emote="05")

    $ her_mood += 7

    jump end_hg_pf

label very_no:
    stop music fadeout 2.0
    call her_main("Absolutely not!","annoyed","angryL",xpos="mid",trans="fade")
    her "I'll show you that my integrity and honour as a Gryffindor cannot be bought!"
    call her_main("I'm leaving this instant.","scream","angryCl")

    $ her_mood += 7

    jump end_hg_pf
