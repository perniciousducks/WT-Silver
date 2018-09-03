

label summon_hermione:
    call play_sound("door") #Sound of a door opening.

    ### RANDOM CLOTHING EVENTS ###
    call hermione_random_clothing

    label hermione_requests:

    $ hermione_busy = True
    $ wardrobe_active = False

    $ menu_y = 0.5 #Menu is moved to the middle. #Don't add xpos!

    menu:
        "-Talk-":
            if not chitchated_with_her:
                if mad <= 7:
                    $ chitchated_with_her = True
                    call chit_chat
                    jump hermione_talk
                else:
                    her "I have nothing to say to you sir..."
                    jump hermione_requests
            else:
                jump hermione_talk

        "-Tutoring-" if not daytime and v_tutoring < 14: #13 is last level.
            if mad >=1 and mad < 3:
                her "I'm sorry, maybe tomorrow..."
                jump hermione_requests
            elif mad >=3 and mad < 10:
                her "I am not in the mood today..."
                jump hermione_requests
            elif mad >= 10 and mad < 20:
                her "Absolutely not, [genie_name]"
                her "I {i}might{/i} consider it once you've said sorry"
                jump hermione_requests
                # Question: What to do between 9 and 20? Only "jump l_tutoring_check"?
            elif mad >=20:
                her "After what you did, [genie_name]?"
                her "I don't think so..."
                jump hermione_requests
            else:
                jump l_tutoring_check

        "-Buy sexual favours-" if hermione_favors:
            if mad >=1 and mad < 3:
                her "I'm sorry, [genie_name], Maybe some other time..."
                jump hermione_requests
            elif mad >=  3 and mad < 10:
                her "I don't feel like it today..."
                her "Maybe in a couple of days..."
                jump hermione_requests
            elif mad >= 10 and mad < 20:
                her "No thank you...."
                jump hermione_requests
            elif mad >= 20 and mad < 30:
                her "After what you did, [genie_name]?"
                her "I don't think so..."
                jump hermione_requests
            elif mad >= 30 and mad < 40:
                her "You can't be serious!"
                jump hermione_requests
            elif mad >= 40:
                her "Is this some twisted joke to you, sir?!"
                her "After what you did I don't feel like doing this ever again!"
                jump hermione_requests
            else:
                jump silver_requests

        "-Wardrobe-":
            $ active_girl = "hermione"

            call load_hermione_clothing_saves

            call reset_wardrobe_vars
            call update_wr_color_list

            $ wardrobe_active = True
            call her_main(xpos="wardrobe",ypos="base")
            call screen wardrobe

        #"-Ending \"Your whore\"-":
        #    $ public_whore_ending = False
        #    jump your_whore

        #"-Ending \"Public whore\"-":
        #    $ public_whore_ending = True #If TRUE the game will end with "Public Whore Ending".
        #    jump your_whore

        "-Dismiss her-":
            if daytime:
                if mad >=3 and mad < 7:
                    her "..............................."
                elif mad >=7:
                    her "*Humph!*..."
                else:
                    her "Oh, alright. I will go to classes then."
            else:
                if mad >=3 and mad < 7:
                    her "..............................."
                elif mad >=7:
                    her "Tch..."
                else:
                    her "Oh, alright. I will go to bed then."

            call play_sound("door")

            $ hermione_busy = True

            jump main_room



label hermione_talk:
    menu:
        "-Working-":
            label working_menu:
            menu:
                "-Work as a maid-" if daytime and hg_maid_OBJ.unlocked:
                    jump job_1

                "-Work as a maid-" if daytime and not hg_maid_OBJ.unlocked:
                    m "(I'll need an outfit for hermione if I want her to work.)"
                    jump working_menu

                "{color=#858585}-Work as a maid-{/color}" if not daytime:
                    "This job is only available during the day."
                    jump working_menu

                "-Work as a cheerleader for Gryffindor-" if daytime and (hg_cheer_g_OBJ.unlocked or hg_cheer_g_sexy_OBJ.unlocked):
                     jump job_3

                "-Work as a cheerleader for Gryffindor-" if daytime and not (hg_cheer_g_OBJ.unlocked or hg_cheer_g_sexy_OBJ.unlocked):
                    m "(I'll need an outfit for hermione if I want her to work.)"
                    jump working_menu

                "{color=#858585}-Work as a cheerleader for Gryffindor-{/color}" if not daytime:
                    "This job is only available during the day."
                    jump working_menu

                "-Work as a cheerleader for Slytherin-" if daytime and (hg_cheer_s_OBJ.unlocked or hg_cheer_s_sexy_OBJ.unlocked):
                    jump job_4

                "-Work as a cheerleader for Slytherin-" if daytime and not (hg_cheer_s_OBJ.unlocked or hg_cheer_s_sexy_OBJ.unlocked):
                    m "(I'll need an outfit for hermione if I want her to work.)"
                    jump working_menu

                "{color=#858585}-Work as a cheerleader for Slytherin-{/color}" if not daytime:
                    "This job is only available during the day."
                    jump working_menu

                "-Never mind-":
                    jump hermione_talk

        "-Ask for a new student-" if hat_known and not luna_known:
            call luna_init
            $ luna_known = True
            jump hat_intro_2

        "-Talk about the ministry letter-" if ministry_letter_received and not astoria_unlocked:
            #You tell Hermione about the curses.
            if snape_on_the_lookout: #Already talked to Snape.
                $ hermione_finds_astoria = True
                $ days_without_an_event = 0 #So the event won't happen right after.
            if hermione_on_the_lookout:
                call her_main("I'm still looking for that student, [genie_name]!","open","closed")
                call her_main("Trust in me, I will find that slytherin scum!","angry","angry")
                jump hermione_talk
            $ hermione_takes_classes = True
            $ hermione_on_the_lookout = True
            jump letter_intro_hermione

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
                    if whoring >=5:
                        $ genie_name = "Genie"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-My Lord-":
                    if whoring >=7:
                        $ genie_name = "My Lord"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Darling-":
                    if whoring >=10:
                        $ genie_name = "Darling"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Lord Voldemort-":
                    if whoring >=15:
                        $ genie_name = "Lord Voldemort"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Daddy-":
                    if whoring >=20:
                        $ genie_name = "Daddy"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Master-":
                    if whoring >=20:
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
                    if whoring >=20:
                        $ genie_name = temp_name
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Never mind-":
                    jump hermione_talk

        "-From now on I will refer to you as-":
            menu:
                "-Miss Granger-":
                    $ hermione_name = "Miss Granger"
                    jump hermione_change
                "-Girl-":
                    $ hermione_name = "Girl"
                    jump hermione_change
                "-Good Girl-":
                    if whoring >=5:
                        $ hermione_name = "Good Girl"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Slave-":
                    if whoring >=10:
                        $ hermione_name = "Slave"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Princess-":
                    if whoring >=10:
                        $ hermione_name = "Princess"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Whore-":
                    if whoring >=15:
                        $ hermione_name = "Whore"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Little Girl-":
                    if whoring >=15:
                        $ hermione_name = "Little Girl"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Slytherin Slut-":
                    if whoring >=18:
                        $ hermione_name = "Slytherin Slut"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Mudblood-":
                    if whoring >=20:
                        $ hermione_name = "Mudblood"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if hermione_name == "":
                        $ hermione_name = "Miss granger"
                    if whoring >=20:
                        $ hermione_name = temp_name
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Never mind-":
                    jump hermione_talk

        "-Start the Ending-" if her_dress_wearable: #Starts the ending of the game.
            jump start_end_events

        "-Never mind":
            jump hermione_requests


label genie_change:
    call her_main("Ok, from now on I'll call you [genie_name].","base","base")
    jump hermione_talk

label genie_change_fail:
    call her_main("I'm not calling you that!","scream","angryCl")
    jump hermione_talk

label hermione_change:
    if whoring >= 20:
        call her_main("You can call me whatever you want, [genie_name]!","base","glance")
    else:
        call her_main("Sure, [genie_name]. I like that name.","base","base")
    jump hermione_talk

label hermione_change_fail:
    call her_main("I'm not letting you call me that!","scream","angryCl")
    jump hermione_talk
