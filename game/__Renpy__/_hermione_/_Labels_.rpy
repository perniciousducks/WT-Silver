

label end_hermione_event:

    hide screen hermione_main
    hide screen hermione_main_ass

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
