

label summon_tonks:
    call play_music("tonks_theme")
    call play_sound("door")

    $ active_girl = "tonks"
    $ tonks_busy = True
    call update_ton_tier

    call tonks_summon_setup

    label tonks_requests:
    $ tonks_class.get_cloth("hair").color = tonks_haircolor
    $ tonks_haircolor = tonks_class.get_cloth("hair").color

    call ton_main(xpos="base",ypos="base")
    $ hide_transitions = False

    menu:

        # Talk
        "-Level Up-" if ton_level_up != None:
            call tonks_level_up(tier=ton_level_up)
            jump tonks_requests

        "-Talk-":
            if not chitchated_with_tonks:
                call tonks_chit_chat
                jump tonks_talk
            else:
                jump tonks_talk


        # Requests
        "-Public Requests-" if daytime and tonks_requests_unlocked:
            jump tonks_requests_menu

        "{color=#858585}-Public Requests-{/color}" if not daytime and tonks_requests_unlocked:
            call nar(">Public requests are available during the daytime only.")
            jump tonks_requests


        # Fireplace Chats
        "-Let's hang-" if (wine_ITEM.number >= 1 and nt_he_drink.counter == 0) or firewhisky_ITEM.number >= 1:
            jump tonks_hangout

        "{color=#858585}-Let's hang-{/color}" if firewhisky_ITEM.number < 1 and nt_he_drink.counter != 0:
            m "(I don't have any firewhisky...)"
            jump tonks_requests

        # Wardrobe
        "-Wardrobe-" if tonks_wardrobe_unlocked:
            call ton_main(xpos="wardrobe",ypos="base", face="neutral")
            call t_wardrobe("ton_main")
            jump tonks_requests

        "{color=#858585}-Hidden-{/color}" if not tonks_wardrobe_unlocked:
            call nar(">You haven't unlocked this feature yet.")
            jump tonks_requests


        # Gifts
        "-Gifts-" if not gave_tonks_gift:
            call expression 'gift_menu' pass (return_label="tonks_requests")

        "{color=#858585}-Gifts-{/color}" if gave_tonks_gift:
            m "I already gave her a gift today."
            jump tonks_requests


        # Dismiss
        "-Never mind-":
            stop music fadeout 1.0

            if daytime:
                ton "Alright, back to work then..."
            else:
                ton "Sweet dreams, [ton_genie_name]."

            call play_sound("door")

            $ tonks_busy = True
            $ tonks_class.wear("all")

            jump main_room


# Tonks level up
label update_ton_tier:
    if ton_tier == 1 and nt_he.favors_E2:
        $ ton_level_up = 1

    return

label tonks_level_up(tier=None):

    call bld
    if tier == 1:
        g9 "(Time to teach those students something useful!)"

    $ ton_tier = tier+1
    $ ton_level_up = None

    pause.5
    call nar(">Tonks has reached level "+str(ton_tier)+"!")

    call update_ton_tier

    return


# Tonks Requests Menu
label tonks_requests_menu:
    call update_ton_requests
    python:
        menu_choices = []
        for i in nt_requests_list:
            if i in []: # Not in the game yet.
                menu_choices.append(("{color=#858585}-Not Available-{/color}","na"))
            elif i.start_tier > ton_tier:
                menu_choices.append(("{color=#858585}-Not ready-{/color}","vague"))
            else:
                menu_choices.append((i.getMenuText(),i.start_label))
        menu_choices.append(("-Never mind-", "nvm"))
        result = custom_menu(menu_choices)
    if result == "nvm":
        jump tonks_requests
    elif result == "vague":
        call favor_not_ready
        jump tonks_requests
    elif result == "na":
        call not_available
        jump tonks_requests
    else:
        $ renpy.jump(result)

label update_ton_requests:
    # Set event tier to current Tonks tier if they are different
    python:
        for i in nt_requests_list:
            if i.tier != ton_tier and i.max_tiers >= ton_tier:
                i.tier = ton_tier

    return



label tonks_talk:
    menu:
        # Temporarily disabled
        #
        # "-Ask about outfit upgrades-":
            # m "[tonks_name],..."
            # m "Do you think you could change any of these outfits?"
            # m "You know..."
            # g9 "Make them sluttier!"
            # call ton_main("Let me see...","base","base","base","down")

            # #call check_tonks_clothing_upgrades #Adds items to the list. Picks one random item.
            # if upgradable_clothing != []:
                # $ ton_clothing_upgrades += 1
                # call ton_main("Oh I really like this one.","open","base","raised","down")
                # call ton_main("I could make some adjustments here...","base","base","raised","down")
                # call ton_main("Maybe make this a bit shorter and...","horny","base","base","down")
                # call ton_main("There you go, [ton_genie_name], all done.","base","base","base","mid")
                # call unlock_clothing(text = ">A sexier variant of an outfit has been unlocked!", item = clothing_unlock)
                # $ clothing_unlock.unlocked = True
                # $ clothing_unlock = None
                # g9 "Nice!"
                # m "Thanks a ton!"
                # call ton_main("Don't mention it, [ton_genie_name].","base","base","base","mid")
                # jump tonks_requests

            # else:
                # call ton_main("I'm sorry [ton_genie_name], but I don't think I can improved these outfits any further.","open","base","raised","mid")
                # call ton_main("I will see what I can do should you get any new ones.","base","base","base","mid")
                # jump tonks_requests

        "-Get naked!-" if tonks_strip_happened and (not tonks_class.get_worn("top") or not tonks_class.get_worn("bottom") or not tonks_class.get_worn("robe")):
            m "Get naked, [tonks_name]!"
            call ton_main("Of course, [ton_genie_name].","horny","base","base","ahegao")
            hide screen tonks_main
            with d3

            $ tonks_class.strip("all")
            pause.8

            call ton_main("Do you like it, [ton_genie_name]?","horny","base","raised","mid")
            call ton_main("The exposed body of one of your subordinates?","open_wide_tongue","base","raised","ahegao")
            g4 "I do, [tonks_name]!"
            g9 "You should teach like that!"
            call ton_main("Hmm...","base","base","base","R")
            call ton_main("I like the way you think, [ton_genie_name]!","horny","base","base","mid")
            jump tonks_requests

        "-Get dressed-" if tonks_strip_happened and not (tonks_class.get_worn("top") or tonks_class.get_worn("bottom") or tonks_class.get_worn("robe")):
            m "Put on some clothes, would you..."
            m "This is a school, after all."
            call ton_main("Of course, [ton_genie_name].","base","base","base","mid")
            hide screen tonks_main
            with d3

            $ tonks_class.wear("all")
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
                    call ton_main("I have to say, for your age you are in a really great shape...","horny","base","base","down")
                    m "That's part of the benefits of being immortal. Your body doesn't age..."
                    call ton_main("You're lucky then... I've had men that were a couple hundred years old, who's bodies were quite fragile...","open","base","base","R")
                    m "All mortals? How did they get that old?"
                    call ton_main("Ever heard of the \"philosopher stone?\"","base","base","base","mid")
                    m "*Ah!* Is it a tiny, red, stone-looking gem, that lengthens the owner's life?"
                    m "It's called the \"sorcerer's stone\" in my world, however."
                    call ton_main("Really? Why is that?","open","base","raised","mid")
                    m "I have no clue..."
                    call ton_main("Didn't you say you were an \"all knowing\" being?","open","base","angry","mid")
                    call ton_main("I guess you really are an \"old man\", Genie...","base","base","base","mid")
                    m "..............."
                    jump tonks_talk

                "-Genie-":
                    $ ton_genie_name = "Genie"
                    call ton_main("Of course.","base","base","base","mid")
                    g9 "Sweet."
                    call ton_main("Will I get my three wishes too?","open","base","base","mid")
                    call ton_main("Or would I have to rub your \"thing\" first?","horny","base","base","mid", hair="horny")
                    m "My lamp?"
                    call ton_main("I was talking about your dick, but-","base","base","base","R")
                    with hpunch
                    g4 "My lamp!!!"
                    g4 "Shit, where even is that thing?"
                    g4 "I must have lost it when I got to this place!"
                    call ton_main("Do you even need it? Didn't you say you were a free Genie now?","open","base","worried","mid")
                    g4 "Of course I still need it! What sort of question is that, woman?!"
                    call ton_main("(................)","angry","base","base","down")
                    g4 "How would you like to suddenly be robbed of your house?!"
                    call ton_main("(I guess I can jerk him off some other time...)","angry","base","worried","R")
                    m "If you find a golden, shiny looking lamp, return it to me..."
                    call ton_main("Sure, [ton_genie_name]...","upset","base","base","R")
                    jump tonks_talk

                "-Lord Voldemort-":
                    $ ton_genie_name = "Lord Voldemort"
                    call ton_main("Bold of you to say his name out loud... Who even told you about the dark lord?","open","base","angry","mid")
                    m "I've read the stories..."
                    call ton_main("So you know this wizard did some terrible things in his lifetime?","open","base","angry","R")
                    m "Did he corrupt young witches for his own twisted pleasure?"
                    call ton_main("You could say that... He corrupted many witches and wizards alike.","upset","base","base","mid")
                    m "....................."
                    m "So he was \"Bi\" is what you're saying?"
                    call ton_main("What? No.","open","wide","wide","wide")
                    call ton_main("I mean, I'm not really sure if someone like him would have even be capable of loving anything...","angry","base","worried","R")
                    call ton_main("All that mattered to him was power, and achieving his own immortality...","open","base","angry","mid")
                    m "Both fairly overrated once you have it, if you ask me..."
                    call ton_main("You don't say...","base","base","raised","mid")
                    m "I bet all he secretly wanted was to have a wife, and a kid that loved him..."
                    call ton_main("Voldemort, having a child? Are you serious?","open","wide","wide","wide")
                    m "Of course not."
                    m "Once you're immortal, the last thing you need is some annoying brat on your mind..."
                    g9 "All we really want to do is waste a majority of our existence with mindless sex!"
                    call ton_main("Oh my...","horny","base","base","mid", hair="horny")
                    m "And sometimes a bit of kinky roleplay..."
                    m "Are you going to call me \"Lord Voldemort\" now or what?"
                    call ton_main("Fine... I will call you, [ton_genie_name], if it makes you happy...","base","base","base","mid")
                    g9 "Yippee!"
                    jump tonks_talk

                "-Daddy-":
                    $ ton_genie_name = "Daddy"
                    call ton_main("Well, you do look about thrice as old as me...","base","base","raised","mid")
                    call ton_main("Crazy to think you geezers gets to bang all those young, innocent witches here...","open","base","base","R")
                    m "(Geezers?)"
                    m "But I thought you didn't mind it?"
                    call ton_main("Oh, I don't mind at all, [ton_genie_name]!","horny","base","base","mid")
                    jump tonks_talk

                "{color=#858585}-Master-{/color}" if ton_friendship < 60:
                    call ton_main("No.","base","base","base","R")
                    m "What?- Why not?"
                    call ton_main("Because... that title has to be earned!","horny","base","angry","mid")
                    m "Seriously?"
                    call ton_main("Yes. Show me that you're worth to be my master, and I'll gladly become your bitch!","open","base","angry","mid")
                    g4 "!!!"
                    call ton_main("Until then you can forget about it...","base","base","base","mid")
                    m "...................."
                    jump tonks_talk
                "-Master-" if ton_friendship >= 60:
                    $ ton_genie_name = "Master"
                    call ton_main("Yes, [ton_genie_name].","open","base","base","mid")
                    m "(...)"
                    call ton_main("","base","base","raised","mid")
                    call ctc
                    m "(...?)"
                    m "You have permission to speak?"
                    call ton_main("Thank you, [ton_genie_name].","base","base","base","down")
                    g9 "(I could get used to that.)"
                    jump tonks_talk

                "-Custom Input-" if cheats_active or ton_friendship >= 60:
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        pass
                    else:
                        $ ton_genie_name = temp_name
                        call ton_main("Hmm, [ton_genie_name]... I like it.","horny","base","raised","mid")
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
                    call ton_main("*Ugh*-","angry","base","angry","R")
                    call ton_main("Really, [ton_genie_name]?","open","base","angry","mid")
                    call ton_main("I hate that name,...","open","base","worried","R")
                    m "Well you better get used to hearing it then, [tonks_name]..."
                    call ton_main("................","upset","base","angry","R")
                    jump tonks_talk
                "-Nympho-":
                    $ tonks_name = "Nympho"
                    call ton_main("You think I'm a nympho, [ton_genie_name]?","horny","base","raised","mid")
                    call ton_main("Like a filthy, sex craved maniac? Who wouldn't shy away from fulfilling every single one of her fantasies?","open","base","worried","mid")
                    call ton_main("It fits quite well, actually.","base","base","base","ahegao")
                    jump tonks_talk
                "-Fuck Puppet-":
                    $ tonks_name = "Fuck Puppet"
                    call ton_main("A fuck puppet?","open","base","raised","mid")
                    call ton_main("[ton_genie_name], did you know I can take the shape of every person or being imaginable?","horny","base","base","mid")
                    m "You might have mentioned that..."
                    call ton_main("You could say I'm perfect for that job.","open_wide_tongue","base","raised","ahegao")
                    m "You need to show me one day. That ability of yours!"
                    call ton_main("Of course, [ton_genie_name].","horny","base","base","mid")
                    jump tonks_talk
                "-Bitch-":
                    $ tonks_name = "Bitch"
                    call ton_main("Hihi--","base","base","base","R")
                    call ton_main("If only you knew...","horny","base","raised","ahegao")
                    m "(...)"
                    g4 "(What does she mean by that?)"
                    jump tonks_talk

                "{color=#858585}-Cunt-{/color}" if ton_friendship < 60:
                    call ton_main("[ton_genie_name], I'm used to getting insulted by my many previous lovers...","base","base","raised","mid")
                    call ton_main("Truth be told I bloody love it!","open_wide_tongue","base","base","ahegao")
                    call ton_main("But we aren't close enough for that yet, don't you think?","open","base","worried","mid")
                    call ton_main("Maybe we should wait with that until we know each other a bit better.","base","base","worried","R")
                    m "Of course.{w} And I will respect that."
                    call ton_main("I'm glad.{w} You are a very polite man, [ton_genie_name]...","base","base","base","mid")
                    m "..........................."
                    jump tonks_talk
                "-Cunt-" if ton_friendship >= 60:
                    $ tonks_name = "Cunt"
                    call ton_main("*Uuuh*, [ton_genie_name]...","base","base","raised","mid")
                    call ton_main("You better not call me that in front of a student...","open","base","base","mid")
                    g9 "What if I do?"
                    call ton_main("Do it, I dare you!","horny","base","base","mid", hair="horny")
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
