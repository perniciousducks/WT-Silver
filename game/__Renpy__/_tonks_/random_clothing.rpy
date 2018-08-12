


label tonks_random_clothing:

    $ random_number = renpy.random.randint(1, 20)
    if random_number in [1,2,3,4]:
        if not tonks_strip_happened:
            $ tonks_strip_happened = True
            $ tonks_naked = True

            call set_tonks_action("strip_naked")

            m "Great, you are here. I need you to--"
            call play_sound("scratch")
            with hpunch
            g4 "!!!"
            call ton_main("","base","base","base","mid",xpos="mid",ypos="base",trans="d5")
            call ctc

            hide screen tonks_main
            with d5
            call ton_main("Hi, [ton_genie_name].","horny","base","raised","mid",xpos="base",ypos="base",trans="d5")
            g9 "You are naked!"
            call ton_main("Indeed I am.","open","base","raised","mid")
            call ton_main("Is that a problem, [ton_genie_name]?","horny","base","raised","mid")
            call ton_main("Am I going to get fired now?","open","base","raised","mid")
            call ton_main("A person of authority?","open","base","raised","R")
            call ton_main("For inapropriate behaviour?","horny","base","raised","mid")
            g9 "How about a raise instead?"
            call ton_main("(Fuck me... I love this job...)","base","base","raised","ahegao")
            call ton_main("A raise? For showing you my naked body?","open","base","raised","mid")
            call ton_main("How much am I worth to you, [ton_genie_name]?","base","base","raised","mid")

            menu:
                "-1 gold-":
                    m "A gold, if anything..."
                    call ton_main("(bastard... How humiliating.)","base","base","raised","ahegao")
                    call ton_main("Thank you so much, [ton_genie_name].","base","base","base","mid")
                    m "Don't mention it, [tonks_name]."
                    $ gold -= 1
                "-20 gold-" if gold >= 20:
                    m "How does 20 gold sound?"
                    call ton_main("(Hmm... I kind of expected more.)","base","base","base","R")
                    call ton_main("Thank you, [ton_genie_name].","base","base","base","mid")
                    g9 "No, [tonks_name]. I have to thank you."
                    $ gold -= 20
                "-100 gold-" if gold >= 100:
                    m "Does 100 gold sound nice to you?"
                    g9 "With a body like that, you could earn a fortune at a strip club!"
                    call ton_main("Really...","horny","base","raised","mid")
                    call ton_main("You think a noble teacher like me,... an ex-auror,... would quit her highly regarded job to become a cheap stripper?","open","base","base","mid")
                    m "Well, no. I still want to keep you as a teacher."
                    m "I merely suggested that you could--"
                    call ton_main("Well, the dueling stage isn't seeing any use...","base","base","base","R")
                    call ton_main("Maybe I should arrange some extra curricular classes for a couple of my favourite students,... give them a little show...","open","base","raised","mid")
                    g9 "I'm sure they would all love to watch their perverted teacher strip!"
                    call ton_main("Maybe I won't just end it at stripping!","horny","base","raised","mid")
                    $ gold -= 100

        else:
            $ ton_request_wear_coat = True

            if tonks_naked:
                call set_tonks_action("strip_naked")

            call load_tonks_cloathing_saves
            call update_tonks_body
            call ton_main("Hi there, [ton_genie_name].","horny","base","base","mid",xpos="base",ypos="base")

    else:
        if weather_gen >= 5: #Rainy & thundery weather.
            $ ton_request_wear_coat = True
        else:
            $ ton_request_wear_coat = False

        if tonks_naked:
            call set_tonks_action("strip_naked")

        call load_tonks_cloathing_saves
        call update_tonks_body
        call ton_main("You've called, [ton_genie_name]?","base","base","base","mid",xpos="base",ypos="base")





    return
