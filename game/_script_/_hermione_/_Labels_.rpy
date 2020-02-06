label too_much:
    stop music fadeout 2.0
    call her_main("[genie_name]??!", "shock", "wide", "base", "L",xpos="mid",trans=fade)
    her "How could you ask for such a thing!?"
    call her_main("I think I better leave.", "angry", "happyCl", "worried", "mid",emote="05")

    call her_walk(action="leave")

    $ her_mood += 6

    jump end_hermione_event


label very_no:
    stop music fadeout 2.0
    call her_main("Absolutely not!", "annoyed", "narrow", "angry", "R",xpos="mid",trans=fade)
    her "I'll show you that my integrity and honour as a Gryffindor cannot be bought!"
    call her_main("I'm leaving this instant.", "scream", "closed", "angry", "mid")

    call her_walk(action="leave")

    $ her_mood += 9

    jump end_hermione_event
