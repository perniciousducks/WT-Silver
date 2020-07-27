label too_much:
    stop music fadeout 2.0
    call her_main("[genie_name]??!", "shock", "wide", "base", "stare",xpos="mid",trans=fade)
    her "How could you ask for such a thing!?"
    call her_main("I think I better leave.", "angry", "happyCl", "worried", "mid",emote="05")

    call her_walk(action="leave")

    $ _responses = [
        "(*Hmm*... I guess it was a little too soon for that.)",
        "(Did I say something wrong...?)",
        "(Welp, was worth a shot I guess.)",
        "(Perhaps I should rethink my appraoch...)",
        "(Judging by her reaction she's not yet ready for it...)"
        ]

    $ renpy.say(m, renpy.random.choice(_responses))

    $ her_mood += 6

    jump end_hermione_event

label too_much_public:
    stop music fadeout 2.0
    call her_main("[genie_name]??!", "shock", "wide", "base", "stare",xpos="mid",trans=fade)
    her "How could you ask for such a thing!?"
    her "People would take me for a whore, I cannot let it happen!"
    call her_main("I think I better leave.", "angry", "happyCl", "worried", "mid",emote="05")

    call her_walk(action="leave")

    $ _responses = [
        "(*Hmm*... Maybe I should start with some easier tasks to lower her reputation first.)",
        "(I guess she still cares too much about her precious reputation.)",
        "(Silly girl still doesn't understand that her *reputation* isn't as important as she thinks.)",
        "(Did I ask too much of her...?)",
        "(She doesn't seem to be ready for this just yet.)"
        ]

    $ renpy.say(m, renpy.random.choice(_responses))

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
