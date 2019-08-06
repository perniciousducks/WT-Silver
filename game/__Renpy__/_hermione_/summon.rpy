

label summon_hermione:

    call play_sound("door")

    call update_hermione
    call update_her_tier

    ### RANDOM CLOTHING EVENTS ###
    call hermione_random_clothing

    label hermione_requests:

    call reset_menu_position

    $ hide_transitions = False
    $ hermione_busy = True

    menu:

        # Talk
        "-Level Up-" if her_level_up != None:
            call hermione_level_up(tier=her_level_up)
            jump hermione_requests

        "-Talk-":
            if not chitchated_with_her:
                if her_mood <= 3:
                    $ chitchated_with_her = True
                    call chit_chat
                    jump hermione_talk
                else:
                    her "I have nothing to say to you sir..."
                    jump hermione_requests
            else:
                jump hermione_talk


        # Tutoring
        "-Tutoring-" if not daytime and her_tutoring < 14: #13 is last level.
            if her_mood >=1 and her_mood < 3:
                her "I'm sorry, maybe tomorrow..."
                jump hermione_requests
            elif her_mood >=3 and her_mood < 10:
                her "I am not in the mood today..."
                jump hermione_requests
            elif her_mood >= 10 and her_mood < 20:
                her "Absolutely not, [genie_name]."
                her "I {i}might{/i} consider it once you've said sorry..."
                jump hermione_requests
                # Question: What to do between 9 and 20? Only "jump l_tutoring_check"?
            elif her_mood >=20:
                her "After what you did, [genie_name]?"
                her "I don't think so..."
                jump hermione_requests
            else:
                jump l_tutoring_check


        # Favors
        "-Buy sexual favours-" if hermione_favors:
            if her_mood >=1 and her_mood < 3:
                her "I'm sorry, [genie_name], Maybe some other time..."
                jump hermione_requests
            elif her_mood >=  3 and her_mood < 10:
                her "I don't feel like it today..."
                her "Maybe in a couple of days..."
                jump hermione_requests
            elif her_mood >= 10 and her_mood < 20:
                her "No thank you...."
                jump hermione_requests
            elif her_mood >= 20 and her_mood < 30:
                her "After what you did, [genie_name]?"
                her "I don't think so..."
                jump hermione_requests
            elif her_mood >= 30 and her_mood < 40:
                her "You can't be serious!"
                jump hermione_requests
            elif her_mood >= 40:
                her "Is this some twisted joke to you, sir?!"
                her "After what you did I don't feel like doing this ever again!"
                jump hermione_requests
            else:
                jump hermione_favor_menu


        # Wardrobe
        "-Wardrobe-" if hermione_wardrobe_unlocked: # Unlocks after first summoning her.
            $ active_girl = "hermione"

            call load_hermione_clothing_saves

            call reset_wardrobe_vars
            call update_wr_color_list

            $ hide_transitions = True
            call her_main(xpos="wardrobe",ypos="base")
            call screen wardrobe


        # Cardgame
        "-Let's Duel- {image=interface/cards.png}" if snape_second_win:
            jump hermione_cardgame_menu


        # Gifts
        "-Gifts-" if not gave_hermione_gift:
            $ current_category = None
            jump hermione_gift_menu

        "{color=#858585}-Gifts-{/color}" if gave_hermione_gift:
            m "I already gave her a gift today. Don't want to spoil her too much..."
            jump hermione_requests


        # Dismiss
        "-Dismiss her-":
            if daytime:
                if her_mood >=3 and her_mood < 7:
                    her "..............................."
                elif her_mood >=7:
                    her "*Humph!*..."
                else:
                    her "Oh, alright. I will go to classes then."
            else:
                if her_mood >=3 and her_mood < 7:
                    her "..............................."
                elif her_mood >=7:
                    her "Tch..."
                else:
                    her "Oh, alright. I will go to bed then."

            call play_sound("door")

            $ hermione_busy = True

            jump main_room



label update_her_tier:
    if her_tier == 1 and her_whoring >= 3 and hg_T1_trigger == True:
        # Trigger: None
        $ her_level_up = 1
    elif her_tier == 2 and her_whoring >= 9 and hg_T2_jerk_off_trigger == True:
        # Trigger: When you get caught jerking off.
        if game_difficulty >= 3 and imagination < 2: # Hardcore only
            return
        $ her_level_up = 2
    elif her_tier == 3 and her_whoring >= 12 and hg_T3_strip_trigger == True:
        # Trigger: After she strips for you.
        if game_difficulty >= 3 and imagination < 3: # Hardcore only
            return
        $ her_level_up = 3
    elif her_tier == 4 and her_whoring >= 18 and hg_T4_handjob_trigger == True:
        # Trigger: None
        if game_difficulty >= 3 and imagination < 4: # Hardcore only
            return
        $ her_level_up = 4
    elif her_tier == 5 and her_whoring >= 21 and hg_T5_blowjob_trigger == True:
        # Trigger: First BJ
        if game_difficulty >= 3 and imagination < 5: # Hardcore only
            return
        $ her_level_up = 5

    return


label hermione_level_up(tier=None):

    call bld
    if tier == 1:
        show screen blktone5
        with d3
        ">Hermione`s second \"favour tier\" is now available."
        ">You can move up \"favour tiers\" by increasing her \"whoring level\", and by triggering \"favour milestones.\""
        if game_difficulty >= 3: # Hardcore, books are required.
            ">In addition, it is also required of you to increase your \"imagination level\" by reading \"fictional books\", to unlock Hermione's next tier of favours."
        hide screen blktone5
        with d3
        pause.5
        menu:
            "Would you like to increase Hermione's \"tier-level\" to 2?"
            "-Yes, increase her level-":
                pass
            "-No, stay on current level.-":
                return

    elif tier == 2:
        m "I wonder she's ready for some more advanced favours now..."
    elif tier == 3:
        m "(...)"
        m "Does she know what a handjob is? Or a titjob?..."
    elif tier == 4:
        m "I wonder if I can get her to suck me off today..."
        g4 "I'm dying to feel that mouth around my cock!"
    elif tier == 5:
        m "Yes, I think it's time..."
        g4 "I'm finally going to have sex with her!"

    $ her_tier = tier+1
    $ her_level_up = None

    pause.5
    call nar(">Hermione has reached level "+str(her_tier)+"!")

    call update_her_tier

    return


label hermione_favor_menu:
    call update_her_favors
    call update_her_requests

    if slytherin >= gryffindor or ravenclaw >= gryffindor or hufflepuff >= gryffindor:
        show screen hermione_main

        label silver_requests_root:
        menu:
            "-Personal favours-":
                python:
                    menu_choices = []
                    for i in hg_favor_list:
                        if i in []: # Not in the game yet.
                            menu_choices.append(("{color=#858585}-Not Available-{/color}","na"))
                        elif i.start_tier > her_tier:
                            menu_choices.append(("{color=#858585}-Not ready-{/color}","vague"))
                        else:
                            menu_choices.append((i.getMenuText(),i.start_label))

                    for i in hg_pf_list:
                        menu_choices.append((i.getMenuText(),i.start_label))
                    menu_choices.append(("-Never mind-", "nvm"))
                    result = custom_menu(menu_choices)
                if result == "nvm":
                    jump silver_requests_root
                if result == "vague":
                    call favor_not_ready
                    jump silver_requests_root
                elif result == "na":
                    call not_available
                    jump silver_requests_root
                else:
                    $ renpy.jump(result)

            "{color=#858585}-Public requests-{/color}" if not daytime:
                call nar(">Public requests are available during the daytime only.")
                jump silver_requests_root

            "-Public requests-" if daytime:
                python:
                    menu_choices = []
                    for i in hg_requests_list:
                        menu_choices.append((i.getMenuText(),i.start_label))
                    menu_choices.append(("-Never mind-", "nvm"))
                    result = custom_menu(menu_choices)
                if result == "nvm":
                    jump silver_requests_root
                else:
                    $ renpy.jump(result)

            "{color=#858585}-Public Shaming-{/color}" if not daytime:
                call nar(">Public Shaming events are available during the daytime only.")
                jump silver_requests_root
            "-Public Shaming-"if daytime:
                label not_now_ps:
                python:
                    menu_choices = []
                    for i in hg_ps_list:
                        if i.tier > bdsm_imagination:
                            menu_choices.append(("{color=#858585}-A vague idea-{/color}","vague"))
                        else:
                            menu_choices.append((i.getMenuText(),i.start_label))
                    menu_choices.append(("-Never mind-", "nvm"))
                    result = custom_menu(menu_choices)
                if result == "nvm":
                    jump silver_requests_root
                elif result == "vague":
                    call vague_idea
                    jump not_now_ps
                else:
                    $ renpy.jump(result)

            "-Never mind-":
                jump hermione_requests

    else:
        show screen hermione_main
        with d3
        if hermione_favors_convinced:
            call her_main("But we're in the lead already....","base","soft")
            if her_whoring >=20 and hermione_favors_convinced == 2:
                call her_main("But I'll do anything for you, [genie_name]...","smile","squint")
                jump silver_requests_root
            elif her_whoring >=18 and hermione_favors_convinced == 2:
                call her_main("I guess you do have a way with words,[genie_name]... I'll do it.","soft","wink")
                jump silver_requests_root
            elif her_whoring >=16:
                call her_main("I have told you before, [genie_name], it was just a one time thing....","open","squint")
                m "What about tomorrow though?"
                call her_main ("What about tomorrow?","base","squint")
                g9 "I made a graph detailing the current daily average points Slytherin gain... doesn't look that great."
                m "Just think about it."
                jump hermione_favors_convinced_check
        else:
            her "The Gryffindors are in the lead. I don't need to do this."
            if her_whoring >= 15:
                menu:
                    "-Change her mind-":
                        m "Are you sure it's not within your house best interests?"
                        call her_main("What do you mean?","base","squint")
                        g9 "Think about the future..."
                        label hermione_favors_convinced_check:
                        if her_whoring >=20:
                            m "If you do it now it could secu-..."
                            call her_main("I'll do it!","smile","squintL")
                            m "Just like that?!"
                            call her_main("Yes... just like that.","smile","closed")
                            g9 "That's my [hermione_name] right there!"
                            $ hermione_favors_convinced = 2
                            jump silver_requests_root

                        m "If you do it, you could secure the win for you household you know..."

                        if her_whoring >=18:
                            call her_main("You really know how to talk me through, [genie_name].","soft","down")
                            call her_main("Okay I agree.","open","down_raised")
                            $ hermione_favors_convinced = 2
                            jump silver_requests_root
                        elif her_whoring >=16 and not hermione_favors_convinced == 1:
                            call her_main("I guess you're right...","open","happy")
                            call her_main("I'll do it... but just this once okay?","grin","happyCl")
                            $ hermione_favors_convinced = 1
                            jump silver_requests_root
                        else:
                            call her_main("I could...","soft","glance")
                            call her_main("But I don't want to.","normal","closed")
                            jump hermione_requests
                    "-Forget it-":
                        pass
        jump hermione_requests


label update_her_favors:
    python:
        for i in hg_favor_list:
            if i.tier != her_tier and i.max_tiers >= her_tier:
                i.tier = her_tier

    return


label update_her_requests:
    python:
        for i in hg_requests_list:
            if i.tier != her_tier and i.max_tiers >= her_tier:
                i.tier = her_tier

    return


label hermione_talk:
    menu:
        "-Working-":
            label working_menu:
            menu:
                "-Work as a maid-" if daytime and hg_outfit_maid_ITEM.unlocked:
                    jump job_1

                "-Work as a maid-" if daytime and not hg_outfit_maid_ITEM.unlocked:
                    m "(I'll need an outfit for hermione if I want her to work.)"
                    jump working_menu

                "{color=#858585}-Work as a maid-{/color}" if not daytime:
                    "This job is only available during the day."
                    jump working_menu

                "-Work as a cheerleader for Gryffindor-" if daytime and (hg_cheer_g_ITEM.unlocked or hg_cheer_g_sexy_ITEM.unlocked):
                     jump job_3

                "-Work as a cheerleader for Gryffindor-" if daytime and not (hg_cheer_g_ITEM.unlocked or hg_cheer_g_sexy_ITEM.unlocked):
                    m "(I'll need an outfit for hermione if I want her to work.)"
                    jump working_menu

                "{color=#858585}-Work as a cheerleader for Gryffindor-{/color}" if not daytime:
                    "This job is only available during the day."
                    jump working_menu

                "-Work as a cheerleader for Slytherin-" if daytime and (hg_cheer_s_ITEM.unlocked or hg_cheer_s_sexy_ITEM.unlocked):
                    jump job_4

                "-Work as a cheerleader for Slytherin-" if daytime and not (hg_cheer_s_ITEM.unlocked or hg_cheer_s_sexy_ITEM.unlocked):
                    m "(I'll need a slytherin cheerleader outfit for hermione if I want her to work.)"
                    jump working_menu

                "{color=#858585}-Work as a cheerleader for Slytherin-{/color}" if not daytime:
                    "This job is only available during the day."
                    jump working_menu

                "{color=#858585}-Hidden-{/color}" if daytime and not cardgame_work and hg_gamble_slut_ITEM.unlocked:
                    "You haven't unlocked this feature yet"
                    jump working_menu

                "-Work by advertising the card game-" if daytime and cardgame_work and hg_gamble_slut_ITEM.unlocked:
                    jump job_5
                "-Work by advertising the card game-" if daytime and cardgame_work and not hg_gamble_slut_ITEM.unlocked:
                    m "(I'll need an outfit for hermione if I want her to work.)"
                    m "(Maybe the twins have something fitting for her in their stock.)"
                    jump working_menu

                "{color=#858585}-Work by advertising the card game-{/color}" if not daytime and cardgame_work:
                    "This job is only available during the day."
                    jump working_menu

                "-Never mind-":
                    jump hermione_talk


        # About Luna.
        "-Ask for a new student-" if hat_known and not luna_known:
            call luna_init
            $ luna_known = True
            jump hat_intro_2


        # About Astoria.
        "-Talk about the ministry letter-" if letter_curse_complaint_OBJ.read and not astoria_unlocked:
            #You tell Hermione about the curses.
            if snape_on_the_lookout: #Already talked to Snape.
                $ hermione_finds_astoria = True
                $ ag_event_pause = 2 # Event happens in 2 days.
            if hermione_on_the_lookout:
                call her_main("I'm still looking for that student, [genie_name]!","open","closed")
                call her_main("Trust in me, I will find that slytherin scum!","angry","angry")
                jump hermione_talk
            $ hermione_busy = True
            $ hermione_on_the_lookout = True
            jump letter_intro_hermione


        # About Cho.
        "{color=#858585}-Solve the matter with Cho-{/color}" if cho_intro_state == "talk_with_snape": # Before talking to Snape.
            m "(I should ask Snape what to do about that Cho girl first. Just to be save.)"
            m "(I should ask him to hang-out in the evening.)"
            jump hermione_talk

        "-Solve the matter with Cho-" if cho_intro_state in ["talk_with_hermione","nagotiate_with_hermione"]: # After talking to Snape.
            jump cho_hermione_talk

        "-Ask Hermione to commentate the game-" if quidditch_commentator == "talk_with_hermione":
            $ quidditch_commentator = "talk_with_cho"
            jump quidditch_commentator_event_2


        # General.
        "-Address me only as-":
            menu:
                "-Sir-":
                    $ genie_name = "Sir"
                    jump genie_change
                "-Dumbledore-":
                    $ genie_name = "Dumbledore"
                    jump genie_change
                "-Professor-":
                    $ genie_name = "Professor"
                    jump genie_change
                "-Old man-":
                    $ genie_name = "Old man"
                    jump genie_change
                "-Genie-":
                    if her_whoring >=5:
                        $ genie_name = "Genie"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-My Lord-":
                    if her_whoring >=7:
                        $ genie_name = "My Lord"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Darling-":
                    if her_whoring >=10:
                        $ genie_name = "Darling"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Lord Voldemort-":
                    if her_whoring >=15:
                        $ genie_name = "Lord Voldemort"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Daddy-":
                    if her_whoring >=20:
                        $ genie_name = "Daddy"
                        $ achievement.unlock("daddy")
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Master-":
                    if her_whoring >=20:
                        $ genie_name = "Master"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ genie_name = "Sir"
                        jump genie_change
                    if her_whoring >=20:
                        $ genie_name = temp_name
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Never mind-":
                    jump hermione_talk

        "-From now on I will refer to you as-":
            menu:
                "-Miss Granger-":
                    $ temp_name = "Miss Granger"
                    jump hermione_change
                "-Girl-":
                    $ temp_name = "Girl"
                    if her_whoring >=1:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Nerd-":
                    $ temp_name = "Nerd"
                    if her_whoring >=3:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Good Girl-":
                    $ temp_name = "Good Girl"
                    if her_whoring >=5:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Little Girl-":
                    $ temp_name = "Little Girl"
                    if her_whoring >=7:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Bad Girl-":
                    $ temp_name = "Bad Girl"
                    if her_whoring >=9:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Princess-":
                    $ temp_name = "Princess"
                    if her_whoring >=11:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Pet-":
                    $ temp_name = "Pet"
                    if her_whoring >=11:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Bitch-":
                    $ temp_name = "Bitch"
                    if her_whoring >=13:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Slut-":
                    $ temp_name = "Slut"
                    if her_whoring >=15:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Cumslut-":
                    $ temp_name = "Cumslut"
                    if her_whoring >= 17:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Slytherin Whore-":
                    $ temp_name = "Slytherin Whore"
                    if her_whoring >= 19:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Mudblood-":
                    $ temp_name = "Mudblood"
                    if her_whoring >= 21:
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ temp_name = "Miss granger"
                    if her_whoring >=21:
                        $ hermione_name = temp_name
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Never mind-":
                    jump hermione_talk

        "-Start the Ending-" if her_dress_wearable: #Starts the ending of the game.
            jump ball_ending_start

        "-Never mind":
            jump hermione_requests


label genie_change:
    call her_main("Ok, from now on I'll call you [genie_name].","base","base")
    jump hermione_talk

label genie_change_fail:
    call her_main("I'm not calling you that!","scream","angryCl")
    jump hermione_talk

label hermione_change:
    if temp_name == "Miss Granger":
        if her_whoring <=0:
            call her_main("Sure, [genie_name].","base","base")
        else:
            call her_main("You don't have to be so formal, [genie_name], you know?","base","closed")
            call her_main("","base","base")
    elif temp_name == "Girl":
        if her_whoring >=1 and her_whoring < 3:
            call her_main("This girl thing again?","annoyed","squint")
            call her_main("*sigh*...","soft","squintL")
        elif her_whoring >=3:
            call her_main("Fine... I don't mind.","soft","baseL")
    elif temp_name == "Nerd":
        if her_whoring >=3 and her_whoring < 5:
            call her_main("*sigh* I just enjoy books, that's all.","annoyed","down")
            m "I'm sure you'll find other things to enjoy soon enough..."
            call her_main("Like what exactly?","normal","glance")
            m "Nothing to worry about, things will work out..."
            g9 "Nerd..."
            call her_main("*tsk* ...","soft","glanceL")
            call her_main("","normal","glanceL")
        elif her_whoring >= 5 and her_whoring < 19:
            call her_main("I can be a bit nerdy sometimes I suppose..","angry","happyCl", emote="05")
            call her_main("","base","base")
        elif her_whoring >= 19:
            call her_main("I don't read as much as I used to anymore.","grin","glanceL", emote="05")
            call her_main("","base","glance")
    elif temp_name == "Good Girl":
        if her_whoring >=5 and her_whoring < 7:
            call her_main("Well, I do try my best, [genie_name].","base","closed")
            call her_main("","base","base")
        elif her_whoring >=7 and her_whoring < 19:
            call her_main("I'm not sure if I'd qualify, but fine.","annoyed","wink")
            call her_main("","normal","base")
        elif her_whoring >=19:
            call her_main("I could act like a good girl if you really want me to...","smile","wink", cheeks="blush")
            call her_main("","base","happy", cheeks="blush")
    elif temp_name == "Little Girl":
        if her_whoring >=7 and her_whoring < 9:
            call her_main("What's going on with with these silly nicknames of yours all of a sudden?","normal","frown")
            m "What do you mean by silly?"
            call her_main("It makes it sound as if I'm your...","soft","worriedL")
            call her_main("Ugh, forget I said anything...","open","down_raised",cheeks="blush")
            call her_main("","normal","baseL", cheeks="blush")
        elif her_whoring >=9 and her_whoring < 19:
            call her_main("Bit of an odd request but...","normal","down_raised",)
            call her_main("I like it...","soft","glanceL",cheeks="blush")
            call her_main("","base","glanceL",cheeks="blush")
        elif her_whoring >= 19:
            call her_main("Yes, [genie_name].","base","concerned",cheeks="blush")
    elif temp_name == "Bad Girl":
        if her_whoring >=9 and her_whoring < 11:
            call her_main("I guess I am a bit.","soft","down")
            call her_main("I did fail that test after all...","disgust","down_raised")
            call her_main("","normal","concerned")
            call her_main("","normal","base")
        elif her_whoring >=11 and her_whoring < 17:
            call her_main("I may be a little bit naughty at times.","base","SquintL",cheeks="blush")
        elif her_whoring >=17:
            call her_main("I may be a little bit naughty at times.","base","SquintL",cheeks="blush")
            call her_main("","base","base", cheeks="blush")
    elif temp_name == "Princess":
        if her_whoring >= 11 and her_whoring < 13:
            call her_main("That would make you my prince wouldn't it?","open","baseL",cheeks="blush")
            call her_main("","base","base", cheeks="blush")
        elif her_whoring >= 13:
            call her_main ("Yes... My prince.","smile","happy")
            m "..."
            call her_main("I-I mean, [genie_name].","smile","happyCl", emote="05")
            call her_main("","base","base")
    elif temp_name == "Pet":
        if her_whoring >= 11 and her_whoring < 13:
            call her_main("You want to call me.... {w=0.5}a pet?","normal","frown")
            m "Yes."
            call her_main(".... {w=0.5}.... {w=0.5}.... {w=0.5}....","normal","squint")
            call her_main("","normal","suspicious")
            m ".... {w=0.5}.... {w=0.5}...."
            call her_main("May I at least know why?","open","suspicious")
            m "No."
            call her_main("....","annoyed","worried")
        elif her_whoring >= 13:
            call her_main ("*Meow*","smile","happyCl")
            call her_main ("","smile","happy")
            m "Don't do that..."
            call her_main ("Such a party pooper.","annoyed","happyCl")
            call her_main("","base","base")
    elif temp_name == "Bitch":
        if her_whoring >=13 and her_whoring < 15:
            call her_main("Isn't this a bit inappropriate [genie_name]?","mad","down")
            m "And doing favours for house points isn't?"
            call her_main ("Fine...","base","down_raised",cheeks="blush")
        elif her_whoring >= 15 and her_whoring < 17:
            call her_main("...","normal","down",cheeks="blush")
            m "Any objections?"
            call her_main("...","soft","worriedL",cheeks="blush")
            g9 "Okay then..."
        elif her_whoring >= 17:
            call her_main("Alright.","base","happyCl",cheeks="blush")
            call her_main("","base","happy",cheeks="blush")
    elif temp_name == "Slut":
        if her_whoring >=15 and her_whoring < 17:
            call her_main("[genie_name]?!","shock","surprised")
            call her_main("You can't just call someone that!","mad","wide")
            m "It'll just be between us..."
            call her_main("...","disgust","suspicious")
            m "Nothing to add?"
            call her_main("","clench","closed", emote="01")
            m "So you'll let me call you that or not?"
            call her_main("{size=+5}FINE!{/size}","clench","angryCl", emote="01")
            m "..."
            call her_main("","normal","angryL")
        elif her_whoring >= 17:
            call her_main("I guess if you have to call me that sure...","base","down_raised",cheeks="blush")
        elif her_whoring >= 19:
            call her_main("I don't mind...","smile","happyCl",cheeks="blush")
    elif temp_name == "Cumslut":
        if her_whoring >= 17 and her_whoring < 19:
            call her_main("A cumslut?!","open","surprised")
            m "Something wrong?"
            call her_main("You have to even ask?","soft","down", cheeks="blush")
            call her_main("This is so degrading...","normal","down_raised",cheeks="blush")
            call her_main("\"But I kinda am a slut begging for cum aren't I...\"","base","happyCl",cheeks="blush")
        elif her_whoring >= 19:
            call her_main("...","soft","ahegao_raised")
            call her_main("\"When did I start enjoying it so much...\"","open","ahegao_raised",cheeks="blush")
            call her_main("\"That taste, the texture..\"", "open","ahegao",cheeks="blush")
            call her_main("\"..So warm, sticky and...\"","silly","ahegao_raised",cheeks="blush")
            m "Are you okay there, [temp_name]?"
            call her_main("Wha-","mad","wide")
            call her_main("Of course I am!","smile","baseL",cheeks="blush")
    elif temp_name == "Slytherin Whore":
        if her_whoring >=19 and her_whoring < 21:
            call her_main("Do you really have to call me that, [genie_name]?","disgust","worried")
            call her_main("Referring to me as a bitch or a slut for your own amusement is one thing...","mad","down",cheeks="blush")
            call her_main("You're aware of how much I loathe Slytherin.","open","concerned")
            call her_main("And I'm definitely not a whore...","soft","closed")
            her "I refuse!"
            menu:
                "-Say its fine-":
                    m "Fine, I won't call you that..."
                    call her_main("You won't?","open","base")
                    call her_main("","soft","base")
                    m "Of course..."
                    call her_main("I am glad we're on the same page on this one, [genie_name].","open","closed")
                    call her_main("","base","closed")
                    m "In fact, from this point forward you don't have to call me [genie_name] or exchange any favours..."
                    call her_main("","soft","base", emote="04")
                    m "Lets just void this whole... deal of yours shall we."
                    call her_main("B-but, [genie_name]?!","mad","wide_stare", emote="02")
                    call her_main("","mad","wide_stare")
                    m "I must apologize {b}Miss Granger{/b}, I thought we had come to some kind of agreeable arrangement by now..."
                    call her_main("But I...","mad","surprised")
                    m "...I should have known better to believe that this sort of thing would work out..."
                    call her_main("Maybe I coul-...","clench","WorriedCl")
                    m "...I thought we both had what we wanted..."
                    call her_main("List-...","soft","down")
                    call her_main("","normal","angryCl")
                    m "...Might as well hand in my resignation with the ministry and..."
                    with hpunch
                    call her_main("{size=+10}I AM A SLYTHERIN WHORE!!!{/size}","scream","angryCl",cheeks="blush")
                    call her_main("","normal","closed")
                    m "..."
                    call her_main("Now please, [genie_name]... Let's just forget this conversation ever happened.","disgust","worried")
                    m "Are you sure that's what you want, [temp_name]?"
                    call her_main("... Yes.","disgust","down", emote="05")
                    m "\"This girl really is beyond redemption...\""
                    call her_main("","base","down")
                "-Threaten her-":
                    g4 "Either accept my offer or Gryffindor lose five hundred points..."
                    with hpunch
                    call her_main("FIVE HUNDRED?!","shock","wide")
                    call her_main("[genie_name]... This is blackmailing!","scream","angryCl")
                    call her_main("","mad","angryCl")
                    m "It is?"
                    call her_main("What else would it be?","mad","angry",cheeks="blush")
                    g9 "Negotiations..."
                    call her_main("You...","clench","angryCl",cheeks="blush")
                    m "That's not an answer..."
                    call her_main("{size=-10}Okay..{/size}","soft","angryL",cheeks="blush")
                    m "What was that? I didn't hear you."
                    call her_main("I said yes, you can call me a slytherin whore... or whatever.","normal","annoyed", cheeks="blush")
                    call her_main("Happy now?!","open","angryCl", cheeks="blush")
                    g9 "Very."
                    call her_main ("{size=-6}You are the worst.{/size}","normal","glanceL", cheeks="blush")
                    $ her_mood += 15
        elif her_whoring >= 21:
            call her_main("Please, [genie_name], couldn't you call me something else instead?","open","worried")
            m "But where's fun in that?"
            call her_main("Why do I even bother... *sigh*","soft","glanceL",cheeks="blush")
    elif temp_name == "Mudblood":
        if her_whoring >= 21:
            call her_main("A{w=0.5}...{w=0.5} {size=+6}{b}{cps=20}mud{w=0.5}blood{/cps}{/b}?!{/size}", "shock","wide")
            call her_main("Did I hear you right, [genie_name]?!", "normal","wide_stare")
            menu:
                "-Confirm-":
                    pass
                "-!!!{b}ABORT ABORT ABORT{/b}!!!-":
                    g4 "What? Of course not!"
                    m "I said.."
                    g4 "(I have to think fast)"
                    menu:
                        "-Mass flood-":
                            g4 "I said mass flood!"
                            call her_main("Mass flood?", "soft","base")
                            m "Are you deaf or something?"
                            if raining:
                                call her_main("I was pretty sure you said-...", "open","base")
                                call her_main("", "normal","baseL")
                                m "Look outside the window, its raining is it not?"
                                call her_main("I{w=0.5}... {w=0.5}Yes, you are right [genie_name].", "normal","closed")
                                m "Of course I am."
                                call her_main("So what did you want to talk about?", "base","base")
                            else:
                                call her_main("[genie_name], but its not raining..", "normal","closed")
                                call her_main("", "disgust","down_raised", cheeks="blush")
                                g9 "Last time I had my dick in you it felt like a mass flood."
                                call her_main("[genie_name]...", "disgust","closed", cheeks="blush")
                                g9 "What? Its true, I swear!"
                                call her_main("...", "soft","down", cheeks="blush")
                        "-Mad stud-":
                            g4 "I said mad stud!"
                            call her_main("Mad stud?", "soft","base")
                            g9 "My dick, your ass, bud."
                            call her_main("really...", "disgust","glance", cheeks="blush")
                            call her_main("You can be so childish sometimes, [genie_name]...", "annoyed","glanceL", cheeks="blush")
                        #"-Leaf bud-":
                        #    jump hermione_talk
                    jump hermione_talk
            call her_main("Why would you even suggest calling me such a thing..", "scream","frown")
            call her_main("It's like the most offensive thing you could call someone like...", "shock","frown", tears="soft")
            call her_main("like...", "open","worriedCl", tears="soft_blink")
            call her_main("Someone like...", "open","down", tears="mascara_crying")
            call her_main("me...", "disgust","down", tears="mascara_soft")
            call her_main("", "disgust","worriedCl", tears="mascara")
            menu:
                "-Try to calm her down-":
                    call her_main("", "disgust","concerned", tears="mascara")
                    m "Now, now, there's no need to cry."
                    m "Do you know why I call you these things miss granger?"
                    call her_main("...no?", "disgust","concerned", tears="mascara")
                    m "It's so that you'll come to know that words are just words and they only hurt if you let them."
                    call her_main("...", "normal","concerned", tears="mascara")
                    m "Once you truly understand that nothing will hold you back."
                    g9 "And you'll be at your utmost potential."
                    call her_main("You really think so?", "open","concerned", tears="mascara")
                    call her_main("", "normal","concerned", tears="mascara")
                    m "Yes, in fact I do."
                    call her_main("Thank you, [genie_name].", "normal","closed", tears="mascara")
                    call her_main("I can do it, I know I can.", "base","concerned", tears="mascara")
                    $ her_mood = 0
                "-Tell her she deserves it-":
                    g4 "You deserve to be called a slut, a whore and a mudblood... just look at you."
                    call her_main("...", "scream","worriedCl", tears="mascara_soft_blink")
                    call her_main("", "disgust","worriedCl", tears="mascara_soft")
                    g4 "You walk into my office and sell your body for the soul reason that it will make Gryffindor happy to win the house cup."
                    call her_main("...", "open","worriedCl", tears="mascara_soft_blink")
                    call her_main("", "disgust","worriedCl", tears="mascara_soft")
                    g4 "Bending over onto my desk and let yourself be taken like a some common harlot..."
                    call her_main("I...", "disgust","concerned", tears="mascara_soft")
                    g4 "Letting your headmaster thrust himself upon you and taking my load like your life depended on it..."
                    call her_main("...", "normal","worriedCl", tears="mascara_soft")
                    call her_main("", "normal","concerned", tears="mascara")
                    m "I bet you don't even care about the points anymore..."
                    call her_main("Well...", "normal","down", tears="mascara")
                    call her_main("", "normal","ahegao", tears="mascara")
                    m "You are nothing more than a whore..."
                    call her_main("", "base","ahegao", tears="mascara")
                    g9 "{size=+4}{b}MY{/b}{/size} whore!"
                    call her_main("", "base","ahegao_raised", tears="mascara")
                    m "And I {b}will{/b} call you however I want!"
                    call her_main("Yes, [genie_name], I understand.", "silly","ahegao_raised", tears="mascara")
                    call her_main("I am your toy{w=0.6}, your fuckslut{w=0.6}, your cocksleeve, your -...", "grin","dead", tears="mascara")
                    m "Yes, that you are but its enough..."
                    call her_main("I fully belong to you... [genie_name].", "silly","dead", tears="mascara")
                    call her_main("", "grin","dead", tears="mascara")
                    $ her_mood = 0
    $ hermione_name = temp_name
    jump hermione_talk

label hermione_change_fail:
    if temp_name == "Girl":
        call her_main("I would prefer if we kept using our formal names and titles, [genie_name].","open","closed")
        call her_main("","normal","base")
    elif temp_name == "Nerd":
        call her_main("I would prefer if you didn't, [genie_name].","open","angryCl")
        call her_main("{size=-4}And I'm not a nerd...{/size}","annoyed","worried")
        if her_whoring >= 1:
            call her_main("\"I think...\"","annoyed","worriedL")
    elif temp_name == "Good Girl":
        call her_main("I'm not letting you call me that, [genie_name]!","open","angryCl")
        if her_whoring >= 3:
            call her_main("\"Although its kinda cute he said that...\"","base","baseL")
    elif temp_name == "Little Girl":
        call her_main("I won't let you call me that, [genie_name]!","open","angryCl")
        if her_whoring >= 5:
            call her_main("\"I hope they'd grow out more...\"","disgust","down")
            call her_main("*sigh*","annoyed","closed")
            call her_main("","normal","baseL")
    elif temp_name == "Bad Girl":
        call her_main("I am not a [temp_name]!","open","angry")
        if her_whoring >= 7:
            call her_main("\"Or am I...?\"","disgust","baseL")
            call her_main("","normal","baseL")
    elif temp_name == "Princess":
        call her_main("This is inappropriate, [genie_name]!","open","angry")
        if her_whoring >= 9:
            call her_main("\"It sounds nice though...\"","base","baseL")
    elif temp_name == "Pet":
        call her_main("Are you joking, [genie_name]?","open","worried")
        if her_whoring >= 11:
            call her_main("\"Why would he even suggest that?\"","annoyed","baseL")
    else:
        call her_main("I won't let you call me that!","shock","angryCl")
        call her_main("","normal","angry")
    jump hermione_talk
