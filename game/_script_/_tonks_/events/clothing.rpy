


label tonks_summon_setup:

    $ tonks_wardrobe_unlocked = True

    $ random_number = renpy.random.randint(1, 20)
    if random_number in [1,2,3,4,5] and tonks.is_worn("top") and ton_friendship >= 50: #Naked

        if not tonks_strip_happened: #First time.
            $ tonks_strip_happened = True

            $ tonks.strip("all")
            call play_sound("door")
            call ton_chibi("stand","mid","base")
            with d3

            call play_sound("scratch")
            with hpunch
            g4 "!!!"

            call play_music("chipper_doodle")
            call ton_main("","base","base","base","mid", hair="horny", xpos="mid", ypos="base", trans=d5)
            call ctc

            call ton_main("Hi, [ton_genie_name].","horny","base","raised","mid")
            g9 "You're naked!"
            call ton_main("Indeed I am.","open","base","raised","mid")
            call ton_main("Is that a problem, [ton_genie_name]?","horny","base","raised","mid")
            call ton_main("Am I going to get fired now?","open","base","base","R")
             #don't think there needs to be a line here tbh
            call ton_main("For inappropriate behaviour?","open","base","base","ahegao")
            call ton_main("Am I going to get punished?","horny","base","raised","mid")

        else: #Repeated Event.

            $ tonks.strip("all")
            call play_sound("door")
            call ton_chibi("stand","mid","base")
            with d3

            call play_music("chipper_doodle")
            call ton_main("","base","base","base","mid", hair="horny", xpos="mid", ypos="base", trans=d5)
            call ctc

            call ton_main("Hi, [ton_genie_name].","horny","base","raised","mid")
            g9 "You are naked again."
            call ton_main("Yes. Just felt like it.","base","base","raised","ahegao")
            m "What if someone sees you?"

            if random_number in [1,2]:
                m "Snape could have been in here."
                call ton_main("Snape? He already knows how I roll...","open","base","raised","mid")
                call ton_main("He asked me for a blowjob yesterday...","open","base","base","R")
                m "And? Did you?"
                call ton_main("Let's just say I'm still toying with him...","base","base","base","mid")
            else: #3,4
                m "One of the girl could have seen you..."
                call ton_main("Oh I would love for them to see me like this...","horny","base","raised","mid")
                call ton_main("Why don't you invite one to your office!","horny","base","base","mid")

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
                        call ton_main("(Bastard... How humiliating.)","base","base","raised","ahegao")
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
                        call ton_main("You think a noble teacher like me- an ex-auror... Would quit her highly regarded job to become a cheap stripper?","open","base","base","mid")
                        m "Well, no. I still want to keep you as a teacher."
                        m "I merely suggested that you could--"
                        call ton_main("Well, the dueling stage isn't seeing any use...","base","base","base","R")
                        call ton_main("Maybe I should arrange some extra curricular activities for a couple of my favourite students, give them a little show...","open","base","raised","mid")
                        g9 "I'm sure they would all love to watch their perverted teacher strip!"
                        call ton_main("Maybe I won't just stop at stripping!","horny","base","raised","mid")
                        $ gold -= 100

            "-Scold her-":
                m "You know I have to, Miss [tonks_name]."
                m "Walking into your boss' office, completely naked?"
                m "A behaviour like that from a teacher... that's just unspeakable!"
                call ton_main("I'm terribly sorry, [ton_genie_name]...","open","base","base","down")
                m "What will you do next? Climb under my desk and suck my cock?"
                g4 "Spread your legs for one of your students?"
                call ton_main("(Hngh-- I'd love to. All of it!)","base","base","raised","ahegao")
                g4 "A bitch like you doesn't deserve to be a teacher. You are nothing more than a disgusting whore!"
                call ton_main("You are so right, [ton_genie_name]!","open_wide_tongue","base","worried","ahegao")
                m "I should make you the school's cum-dumpster instead. How would you like that position?"
                m "Boys lining up in front of the school toilets, waiting their turn to dump their cum into their teacher's mouth, day after day!"
                call ton_main("You're making me so wet, [ton_genie_name]!","base","base","base","ahegao")
                call ton_main("Maybe some day I'll get bored of my current position here at Hogwarts,... you never know...","horny","base","raised","mid")
                m "I'm not done with your punishment, Miss [tonks_name]!"
                m "You went to this school, didn't you? Which house were you in?"
                call ton_main("Me? I was in Hufflepuff.","open","base","raised","mid")
                m "Very well then."
                m "Minus 10 points from house hufflepuff!"
                $ hufflepuff -=10
                call ton_main("What? But [ton_genie_name]! I'm not even a student--","open","wide","wide","mid", trans=hpunch)
                g4 "In addition, from this point forward, you will be forbidden to wear even a single piece of clothing whenever you step into this room!"
                call ton_main("Of course, [ton_genie_name].","base","base","raised","down")
                m "Even if there is a student in here. Or if I call somebody... Anybody!"
                m "You will remain naked!"
                g4 "Did you hear me, [tonks_name]?"
                call ton_main("Yes, [ton_genie_name]!","base","base","base","mid")
                m "Good."

        call ton_main("Whenever you want me to put my clothes back on, just tell me...","base","base","base","mid")

        call ton_main(xpos="base", ypos="base", trans=fade)

        return
        
    # if tonks_outfits_schedule:
        # $ tmp_outfits = get_character_outfits_schedule("tonks")
        # if len(tmp_outfits) > 0:
            # $ tonks.equip(renpy.random.choice(tmp_outfits))

    call play_sound("door")
    call ton_chibi("stand","mid","base")
    with d3

    call play_music("tonks")
    call ton_main("You called, [ton_genie_name]?","base","base","base","mid", xpos="base", ypos="base")

    return
