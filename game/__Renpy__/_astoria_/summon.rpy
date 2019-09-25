

label summon_astoria:

    call astoria_summon_setup

    $ active_girl = "astoria"
    $ astoria_busy = True

    label astoria_requests:

    $ hide_transitions = False

    menu:

        # Talk
        "-Talk-":
            if not chitchated_with_astoria:
                call astoria_chit_chat
                jump astoria_talk
            else:
                jump astoria_talk


        # Spells
        "-Spells-":
            jump astoria_spells


        # Wardrobe
        "-Wardrobe-" if astoria_wardrobe_unlocked:
            call ast_main(xpos="wardrobe", ypos="base", face="neutral")
            call expression 't_wardrobe' pass (return_label="astoria_requests", char_label="ast_main")

        "{color=#858585}-Hidden-{/color}" if not astoria_wardrobe_unlocked:
            call nar(">You haven't unlocked this feature yet.")
            jump astoria_requests


        # Gifts
        "-Gifts-" if not gave_astoria_gift:
            call expression 'gift_menu' pass (return_label="astoria_requests")

        "{color=#858585}-Gifts-{/color}" if gave_astoria_gift:
            m "I already gave her a gift today. Don't want to spoil her too much..."
            jump astoria_requests


        # Dismiss
        "-Dismiss her-":
            stop music fadeout 1.0

            if daytime:
                call ast_main("I will go back to classes then, [ast_genie_name].", face="neutral")
            else:
                call ast_main("Oh, alright. Good night, [ast_genie_name].", face="neutral")

            call play_sound("door")

            $ astoria_busy = True
            $ astoria_class.wear("all")

            jump main_room



label astoria_spells:
    call update_astoria_spells

    python:
        spell_menu = []

        for i in ag_spell_list:
            if not i.complete: # Not trained yet.
                if daytime and not tonks_busy:
                    spell_menu.append( (i.getMenuText(), i.start_label ) )
                else:
                    spell_menu.append( ("{color=#858585}"+i.getMenuText()+"{/color}","block") )

            else: # Spell trained and unlocked.
                spell_menu.append( (i.getMenuText(), i.start_label ) )


        spell_menu.append( ("-Never mind-", "nvm") )

        result = custom_menu(spell_menu)

    if result == "nvm":
        jump astoria_requests
    elif result == "block":
        call block_spell_training
        jump astoria_spells
    elif result == "vague":
        call spell_not_known
        jump astoria_spells
    elif result == "busy":
        call person_is_busy
        jump astoria_spells
    else:
        $ renpy.jump(result)


label block_spell_training:
    if not daytime:
        m "It's too late for that..."
    elif tonks_busy:
        m "I don't think Tonks has time for that right now..."
    return

label person_is_busy:
    if daytime:
        m "Looks like she's taking classes right now."
    else:
        m "Seems like she's already asleep."
    return

label spell_not_known:
    call nar("You haven't unlocked this spell yet.")
    return

label astoria_talk:
    menu:
        #"--":
        "-Address me only as-":
            menu:
                "-Sir-":
                    $ ast_genie_name = "Sir"
                    call ast_main("Very well, [ast_genie_name].", face="neutral")
                    jump astoria_talk
                "-Dumbledore-":
                    $ ast_genie_name = "Dumbledore"
                    call ast_main("Of course, [ast_genie_name].", face="neutral")
                    jump astoria_talk
                "-Professor-":
                    $ ast_genie_name = "Professor"
                    call ast_main("Of course, [ast_genie_name].", face="neutral")
                    jump astoria_talk
                "-Old man-":
                    $ ast_genie_name = "Old man"
                    call ast_main("Alrighty, [ast_genie_name].", face="neutral")
                    jump astoria_talk
                "-Genie-":
                    $ ast_genie_name = "Genie"
                    call ast_main("What?! You are a genie? For real?", face="happy")
                    call ast_main("That's so cool!", face="happy")
                    m "(Oh right. Nobody is supposed to know that.)"
                    m "It's just my name, [astoria_name]..."
                    call ast_main("Oh... ok, [ast_genie_name].", face="neutral")
                    jump astoria_talk
                "-Lord Voldemort-":
                    $ ast_genie_name = "Lord Voldemort"
                    call ast_main("Voldemort? Like that mean, evil wizard?", face="disgusted")
                    call ast_main("You aren't him, are you?", face="disgusted")
                    m "No, just roleplaying..."
                    call ast_main("Oh, alrighty then!", face="happy")
                    call ast_main("[ast_genie_name].", face="happy")
                    jump astoria_talk
                "-Daddy-":
                    $ ast_genie_name = "Daddy"
                    call ast_main("Daddy? Don't you think that's a little weird?", face="disgusted")
                    m "Not at all!"
                    call ast_main("Hmpf...", face="angry")
                    call ast_main("Alright, why not. Nobody knows about it anyways.", face="neutral")
                    jump astoria_talk
                "-Master-":
                    $ ast_genie_name = "Master"
                    call ast_main("Hahahaha-- you want me to call you master?", face="happy")
                    call ast_main("That's so silly!", face="happy")
                    m "(...)"
                    call ast_main("Well alright... M-master--", face="happy")
                    call ast_main("Hahahaha--", face="happy")
                    m "Are you done now?."
                    call ast_main("Yes... I'm sorry... I will try without laughing next time. Promised.", face="happy")
                    jump astoria_talk
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ ast_genie_name = "Sir"
                        call ast_main("I will just call you [ast_genie_name] again.", face="neutral")
                    else:
                        $ ast_genie_name = temp_name
                        call ast_main("Uhm... ok. I will call you [ast_genie_name].", face="neutral")
                    jump astoria_talk
                "-Never mind-":
                    jump astoria_talk


        "-From now on I will refer to you as-":
            menu:
                "-Miss Greengrass-":
                    $ astoria_name = "Miss Greengrass"
                    call ast_main("Sure, [ast_genie_name].", face="happy")
                    jump astoria_talk
                "-Girl-":
                    $ astoria_name = "Girl"
                    call ast_main("Ok, [ast_genie_name].", face="neutral")
                    jump astoria_talk
                "-Princess-":
                    $ astoria_name = "Princess"
                    call ast_main("I really do feel like a princess!", face="happy")
                    call ast_main("After all, I can do whatever I want!", face="angry")
                    jump astoria_talk
                "-Cutie-":
                    $ astoria_name = "Cutie"
                    call ast_main("Fine... If you really have to, [ast_genie_name].", face="disgusted")
                    jump astoria_talk
                "-Slave-":
                    $ astoria_name = "Slave"
                    call ast_main("I'm not your slave, [ast_genie_name]!", face="angry")
                    m "Of course you aren't! We are just playing a game, that's all..."
                    call ast_main("Oh I like games!", face="happy")
                    call ast_main("Alrighty then!", face="happy")
                    jump astoria_talk
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ astoria_name = "Miss Greengrass"
                    else:
                        $ astoria_name = temp_name
                        call ast_main("That's a bit much, don't you think, [ast_genie_name]?", face="disgusted")
                        m "Not at all!"
                        m "I will only call you that when we are alone, promised!"
                        call ast_main("Well,... Ok then...", face="neutral")
                    jump astoria_talk
                "-Never mind-":
                    jump astoria_talk


        "-Never mind":
            jump astoria_requests
