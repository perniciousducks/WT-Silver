

label summon_tonks:

    call play_sound("door")
    $ menu_x = 0.5
    $ menu_y = 0.5

    #ADD Tonks chibi here.
    call tonks_random_clothing

    label tonks_requests:

    $ menu_y = 0.5 #Menu is moved to the middle. #Don't add xpos!

    menu:
        "-Talk-":
            if not chitchated_with_tonks:
                call tonks_chit_chat
                jump tonks_talk
            else:
                jump tonks_talk

        "{color=#858585}-Send Astoria with her-{/color}" if spells_locked and (astoria_busy or not daytime):
            if daytime:
                call nar(">Astoria is currently unavailable.")
            else:
                call nar(">It is too late to send Astoria with Tonks today! Try again tomorrow.")
            jump tonks_requests
        "-Send Astoria with her-" if spells_locked and daytime and not astoria_busy:
            call blkfade
            call nar(">You summon Astoria.")
            pause.5
            hide screen blkfade
            call ast_main("Hi, [ast_genie_name]!","grin","base","base","mid",xpos="mid",ypos="base",trans="fade")
            if tonks_naked:
                call ast_main("He--","worried","closed","base","mid")
                call ast_main("[ast_tonks_name]?!","open","wide","wide","R",trans="hpunch")
                call ast_main("[ast_genie_name], why is she naked?","scream","closed","worried","mid",trans="hpunch")
                call ton_main("Because your headmaster wants me to...","horny","base","base","mid")
                g9 "That's right!"
            else:
                call ast_main("Uhm, hello, Miss Tonks.","worried","base","worried","R")
                call ton_main("Hello, [ton_astoria_name].","horny","base","raised","L")
                call ast_main("{size=-2}[ast_tonks_name]...{/size}","pout","narrow","narrow","L")
            if one_out_of_three == 1:
                m "Astoria, I want you to spend the day with Miss [tonks_name] again."
            if one_out_of_three == 2:
                m "Miss Greengrass, you are going to spend some quality time with Miss [tonks_name] today."
            if one_out_of_three == 3:
                m "Girl, you're going with Miss [tonks_name] today. Like it or not..."
            call ast_main("Again?! Do I really have to?","pout","base","worried","mid")
            m "Yes."
            call ton_main("Don't worry [ton_astoria_name]. It's gonna be fun!","base","base","base","L")
            call ton_main("Take care, [ton_genie_name].","base","base","base","mid")
            call ast_main("...","pout","base","worried","L")
            call play_sound("door")
            hide screen tonks_main
            with d3

            pause.5
            call play_sound("door")
            hide screen astoria_main
            hide screen bld1
            with d3

            $ astoria_busy = True
            $ tonks_busy = True

            $ astoria_tonks_event_in_progress = True

            call play_music("brittle_rille") #Day Theme
            jump day_main_menu


        "-Never mind-":
            stop music fadeout 1.0
            $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)

            if daytime:
                ton "Alright, back to work then..."
            else:
                ton "Sweet dreams, [ton_genie_name]."

            $ tonks_busy = True
            hide screen bld1
            hide screen tonks_main
            with d3
            call play_sound("door")

            if daytime:
                call play_music("brittle_rille") #Day Theme
                jump day_main_menu
            else:
                call play_music("manatees") #Night Theme
                jump night_main_menu


label tonks_talk:
    menu:
        "-Ask about outfit upgrades-":
            m "[tonks_name],..."
            m "Do you think you could change any of these outfits?"
            m "You know..."
            g9 "Make them sluttier!"
            call ton_main("Let me see...","base","base","base","down")

            call check_tonks_clothing_upgrades #Adds items to the list. Picks one random item.
            if upgradable_clothing != []:
                call ton_main("Oh I really like this one.","open","base","raised","down")
                call ton_main("I could make some adjustments here...","base","base","raised","down")
                call ton_main("Maybe make this a bit shorter and...","horny","base","base","down")
                call ton_main("There you go, [ton_genie_name], all done.","base","base","base","mid")
                call unlock_clothing(text = "> A sexier variant of an outfit has been unlocked!", item = clothing_unlock)
                $ clothing_unlock.unlocked = True
                $ clothing_unlock = None
                g9 "Nice!"
                m "Thanks a ton!"
                call ton_main("Don't mention it, [ton_genie_name].","base","base","base","mid")
                jump tonks_requests

            else:
                call ton_main("I'm sorry [ton_genie_name], but I don't think I can improved these outfits any further.","open","base","raised","mid")
                call ton_main("I will see what I can do should you get any new ones.","base","base","base","mid")
                jump tonks_requests

        "-Get naked!-" if tonks_strip_happened and not tonks_naked:
            $ tonks_naked = True
            m "Get naked, [tonks_name]!"
            call ton_main("Of course, [ton_genie_name].","horny","base","base","ahegao")
            hide screen tonks_main
            with d3

            call set_tonks_action("strip_naked")
            pause.8

            call ton_main("Do you like it, [ton_genie_name]?","horny","base","raised","mid")
            call ton_main("The exposed body of one of your subordinates?","tongue_wide","base","raised","ahegao")
            g4 "I do, [tonks_name]!"
            g9 "You should teach like that!"
            call ton_main("Hmm...","base","base","base","R")
            call ton_main("I like the way you think, [ton_genie_name]!","horny","base","base","mid")
            jump tonks_requests

        "-Get dressed-" if tonks_naked:
            $ tonks_naked = False
            m "Put on some clothes, would you..."
            m "This is a school, after all."
            call ton_main("Of course, [ton_genie_name].","base","base","base","mid")
            hide screen tonks_main
            with d3

            call set_tonks_action(None)
            pause.8

            call ton_main("...","base","base","base","mid")
            jump tonks_requests

        "-Address me only as-":
            menu:
                "-Sir-":
                    $ ton_genie_name = "Sir"
                    call ton_main("Of course, [ton_genie_name].","base","base","base","mid")
                    jump tonks_talk
                "-Dumbledore-":
                    $ ton_genie_name = "Dumbledore"
                    call ton_main("Sure thing, [ton_genie_name].","base","base","base","mid")
                    jump tonks_talk
                "-Professor-":
                    $ ton_genie_name = "Professor"
                    call ton_main("Alright, [ton_genie_name].","base","base","base","mid")
                    jump tonks_talk
                "-Old man-":
                    $ ton_genie_name = "Old man"
                    call ton_main("Please... You aren't that old...","base","base","base","R")
                    m "You think I'm-- Wait? What?"
                    call ton_main("Oh yes... I've had men far older than you...","horny","base","base","ahegao")
                    call ton_main("[ton_genie_name].","base","base","base","mid")
                    m "(Older than me?)"
                    m "(What's the deal with her...?)"
                    jump tonks_talk
                "-Genie-":
                    $ ton_genie_name = "Genie"
                    call ton_main("A genie?","open","wide","wide","wide")
                    m "Yes. Surprising isn't it."
                    call ton_main("I knew something was off about you!","open","wide","raised","mid")
                    m "Yes. Just don't tell anybody..."
                    call ton_main("I hope you are still in posess of your lower half.","horny","base","raised","down")
                    g9 "I am!"
                    call ton_main("Would you like to know a secret?","open","base","base","R")
                    call ton_main("I never did it with a genie...","base","base","base","mid")
                    call ton_main("But I would like to change that... Eventually...","horny","base","raised","mid")
                    g9 "At your service!"
                    jump tonks_talk
                "-Lord Voldemort-":
                    $ ton_genie_name = "Lord Voldemort"
                    call ton_main("Yeah... I'm not buying it.","base","base","angry","mid")
                    m "You don't?"
                    call ton_main("You don't posess the aura of a dark wizard.","open","base","base","R")
                    m "..."
                    call ton_main("But fine... I will call you, [ton_genie_name], if that's what makes you happy...","base","base","raised","mid")
                    g9 "Yippee!"
                    jump tonks_talk
                "-Daddy-":
                    $ ton_genie_name = "Daddy"
                    call ton_main("Well, you do look about thrice as old as me...","base","base","raised","mid")
                    call ton_main("Crazy to think you geezers get to bang all those young, innocent witches here...","open","base","base","R")
                    m "(Geezers?)"
                    m "But I thought you don't mind it?"
                    call ton_main("Oh, I don't mind at all, [ton_genie_name]!","horny","base","base","mid")
                    jump tonks_talk
                "-Master-":
                    $ ton_genie_name = "Master"
                    call ton_main("Yes, [ton_genie_name].","base","base","base","mid")
                    m "(...)"
                    call ton_main("","base","base","raised","mid")
                    call ctc
                    m "(...?)"
                    m "You have permission to speak?"
                    call ton_main("Thank you, [ton_genie_name].","base","base","base","down")
                    g9 "(I could get used to that.)"
                    jump tonks_talk
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        pass
                    else:
                        $ ton_genie_name = temp_name
                        call ton_main("Hmm, [ton_genie_name]... I loke it.","horny","base","raised","mid")
                    jump tonks_talk
                "-Never mind-":
                    jump tonks_talk


        "-From now on I will address you as-":
            menu:
                "-Tonks-":
                    $ tonks_name = "Tonks"
                    call ton_main("Sure, [ton_genie_name].","base","base","base","mid")
                    jump tonks_talk
                "-Nymphadora-":
                    $ tonks_name = "Nymphadora"
                    call ton_main("Ugh--","base","base","angry","R")
                    call ton_main("Really, [ton_genie_name]?","open","base","angry","mid")
                    call ton_main("How do you even know my real name?","open","base","raised","mid")
                    g9 "Just a lucky guess!"
                    call ton_main("I highly doubt that...","base","base","raised","up")
                    call ton_main("I despise that name, but...","open","base","raised","R")
                    call ton_main("You are the boss...","base","base","worried","R")
                    jump tonks_talk
                "-Nympho-":
                    $ tonks_name = "Nympho"
                    call ton_main("You think I'm a nympho, [ton_genie_name]?","horny","base","raised","mid")
                    call ton_main("Like a filthy, sex craved maniac? Who wouldn't shy away from fulfilling even a single one of her fantasies?","open","base","worried","mid")
                    call ton_main("It fits quite well, actually.","base","base","base","ahegao")
                    jump tonks_talk
                "-Fuck Puppet-":
                    $ tonks_name = "Fuck Puppet"
                    call ton_main("A fuck puppet?","open","base","raised","mid")
                    call ton_main("[ton_genie_name], did you know I can take the shape of every person or being imaginable?","horny","base","base","mid")
                    m "You might have mentioned that..."
                    call ton_main("You could say I'm perfect for that job.","tongue_wide","base","raised","ahegao")
                    m "You need to show me one day. That ability of yours!"
                    call ton_main("Of course, [ton_genie_name].","horny","base","base","mid")
                    jump tonks_talk
                "-Bitch-":
                    $ tonks_name = "Bitch"
                    call ton_main("Hihi--","base","base","base","R")
                    call ton_main("If only you knew...","horny","base","raised","ahegao")
                    m "(...)"
                    g4 "(What does she mean with that now?)"
                    jump tonks_talk
                "-Cunt-":
                    $ tonks_name = "Cunt"
                    call ton_main("Uuuh, [ton_genie_name]...","base","base","raised","mid")
                    call ton_main("You better not call me that in front of a studant...","open","base","base","mid")
                    g9 "What if I do?"
                    call ton_main("Do it, I dare you!","horny","base","base","mid")
                    jump tonks_talk
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        pass
                    else:
                        $ tonks_name = temp_name
                        call ton_main("Hmm...","base","base","base","R")
                        call ton_main("Alright.","base","base","base","mid")
                        m "Really? You don't mind?"
                        call ton_main("Not at all, [ton_genie_name].","horny","base","raised","mid")
                        call ton_main("I've been called quite many things by my lovers!","base","base","base","R")
                        g9 "I'm your lover now?"
                        call ton_main("Never say never.","base","base","base","mid")
                    jump tonks_talk
                "-Never mind-":
                    jump tonks_talk

        "-Never mind-":
            jump tonks_requests
