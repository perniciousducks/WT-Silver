


label tonks_random_clothing:
    $ random_number = renpy.random.randint(1, 20)
    if random_number in [1,2,3,4,5,7] and tonks_class.get_worn("top") and ast_affection >= 2 and ton_friendship >= 5: #Naked
        if not tonks_strip_happened: #First time.
            $ tonks_strip_happened = True

            $ tonks_class.strip("all")

            m "Great, you are here. I need you to--"
            call play_sound("scratch")
            with hpunch
            g4 "!!!"
            call play_music("chipper_doodle")

            call ton_main("","base","base","base","mid",xpos="mid",ypos="base",trans="d5")
            call ctc

            call ton_main("Hi, [ton_genie_name].","horny","base","raised","mid")
            g9 "You are naked!"
            call ton_main("Indeed I am.","open","base","raised","mid")
            call ton_main("Is that a problem, [ton_genie_name]?","horny","base","raised","mid")
            call ton_main("Am I going to get fired now?","open","base","base","R")
            call ton_main("A person of authority?","open","base","base","mid")
            call ton_main("For inappropriate behaviour?","open","base","base","ahegao")
            call ton_main("Am I going to get punished?","horny","base","raised","mid")

        else: #Repeated Event.
            call play_music("chipper_doodle")

            $ tonks_class.strip("all")

            call ton_main("","base","base","base","mid",xpos="mid",ypos="base",trans="d5")
            call ctc

            call ton_main("Hi, [ton_genie_name].","horny","base","raised","mid")
            g9 "You are naked again."
            call ton_main("Yes. Just felt like it.","base","base","raised","ahegao")
            m "You don't worry if anybody's sees you?"
            if random_number in [1,2]:
                m "Snape could have been in here."
                call ton_main("Snape? He already knows how I roll...","open","base","raised","mid")
                call ton_main("He asked me for a blowjob yesterday...","open","base","base","R")
                m "And? Did you?"
                call ton_main("Let's just say I'm still toying with him...","base","base","base","mid")
            else: #3,4
                m "Astoria could have seen you."
                call ton_main("Oh I would love for her to see me like this...","horny","base","raised","mid")
                call ton_main("Why don't you invite her to your office!","horny","base","base","mid")
            m "Are you always such a slut?"
            call ton_main("I'm sorry, [ton_genie_name]! But it's in my nature.","horny","base","raised","mid")
            call ton_main("Are you going to punish me? For being such a masochistic freak?","open_wide_tongue","base","base","ahegao")

        menu: #Continuation.
            "-Play nice-":
                g9 "How about a raise instead?"
                call ton_main("(Fuck me... I love this job...)","base","base","raised","ahegao")
                call ton_main("A raise? For showing my body to my own boss?","open","base","raised","mid")
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

            "-Scold her-":
                m "You know I have to, Miss [tonks_name]."
                m "Walking into the room of your boss, completely naked?"
                m "A behaviour like that from a teacher... that's just unspeakable!"
                call ton_main("I'm terribly sorry, [ton_genie_name]...","open","base","base","down")
                m "What will you do next? Climb under my desk and suck my cock?"
                g4 "Spread your legs for one of your students?"
                call ton_main("(Hngh-- I'd love to. All of it!)","base","base","raised","ahegao")
                g4 "A cunt like you doesn't deserve to be a teacher. You are nothing more than a disgusting whore!"
                call ton_main("You are so right, [ton_genie_name]!","open_wide_tongue","base","worried","ahegao")
                m "I should make you the school's cum-dumpster instead. How would you like that position?"
                m "Boys lining up in front of the school toilets, waiting their turn to dump their cum into their teacher's mouth, day after day!"
                call ton_main("You are making me wet, [ton_genie_name]!","base","base","base","ahegao")
                call ton_main("Maybe some day I'll get bored of my current position here at Hogwarts,... you never know...","horny","base","raised","mid")
                m "I'm not done with your punishment, Miss [tonks_name]!"
                m "You went to this school, didn't you? Which house were you in?"
                call ton_main("Me? I was in Hufflepuff.","open","base","raised","mid")
                m "Very well then."
                m "Minus 10 points from house-hufflepuff!"
                $ hufflepuff -=10
                call ton_main("What? But [ton_genie_name]! I'm not even a student--","open","wide","wide","mid",trans="hpunch")
                g4 "In addition, from this point forward, you will be forbidden to wear even a single piece of clothing whenever you step into this room!"
                call ton_main("Of course, [ton_genie_name].","base","base","raised","down")
                m "Even if there is a student in here. Or if I call somebody... Anybody!"
                m "You will remain naked!"
                g4 "Did you hear me, [tonks_name]?"
                call ton_main("Yes, [ton_genie_name]!","base","base","base","mid")
                m "Good."

        call ton_main("Whenever you want me to put my clothes back on, just tell me...","base","base","base","mid")

        #Unlocks Wardrobe.
        if not tonks_wardrobe_unlocked:
            call popup("You can now access Tonks' wardrobe and change her appearance!", "Congratulations!", "interface/icons/head/head_tonks_4.png")

            $ tonks_wardrobe_unlocked = True

        call ton_main(xpos="base",ypos="base",trans="fade")

    else:
        #if weather_gen >= 5: #Rainy & thundery weather.
            #$ ton_request_wear_coat = True
        #else:
            #$ ton_request_wear_coat = False

        call ton_main("You've called, [ton_genie_name]?","base","base","base","mid",xpos="base",ypos="base")

    return
