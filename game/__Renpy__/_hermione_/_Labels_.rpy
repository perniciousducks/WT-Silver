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
    call her_main("[genie_name]??!", "shock", "wide", "base", "stare",xpos="mid",trans="fade")
    her "How could you ask for such a thing!?"
    call her_main("I think I better leave.", "angry", "worriedCl", "worried", "mid",emote="05")

    call her_walk(action="leave", speed=2.5)

    $ her_mood += 6

    jump end_hermione_event


label very_no:
    stop music fadeout 2.0
    call her_main("Absolutely not!", "annoyed", "narrow", "angry", "R",xpos="mid",trans="fade")
    her "I'll show you that my integrity and honour as a Gryffindor cannot be bought!"
    call her_main("I'm leaving this instant.", "scream", "closed", "angry", "mid")

    call her_walk(action="leave", speed=2.5)

    $ her_mood += 9

    jump end_hermione_event
