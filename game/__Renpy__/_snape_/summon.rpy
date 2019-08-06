

label summon_snape:

    call play_sound("door")

    call sna_chibi("stand","mid","base")

    call sna_main("Yes, what is it?","snape_01",xpos="base",ypos="base")

    label snape_ready:
        pass

    menu:

        # Talk
        "-Talk-":
            if not chitchated_with_snape:
                $ chitchated_with_snape = True
                call snape_chitchat

            menu:
                "-Talk about the ministry letter-" if letter_curse_complaint_OBJ.read and not astoria_unlocked:
                    #You tell Snape about the curses.
                    if hermione_on_the_lookout: #Already talked to Hermione.
                        $ hermione_finds_astoria = True
                        $ ag_event_pause = 2 # Event happens in 2 days.
                    if snape_on_the_lookout:
                        call sna_main("I'm still on the lookout, Genie.","snape_01")
                        call sna_main("If I find the little maggot that casts those spells,...","snape_10")
                        call sna_main("I will crush his bones!","snape_16")
                        jump snape_ready
                    $ snape_busy = True
                    $ snape_on_the_lookout = True
                    jump letter_intro_snape

                "-Ask for a spellbook-" if (third_curse_got_cast or spells_unlocked) and not snape_gave_spellbook:
                    $ snape_gave_spellbook = True
                    jump snape_book_intro

                "-Never mind":
                    jump snape_ready


        # Fireplace Chats
        "-Let's hang-" if wine_ITEM.number >= 1 and not daytime:
            jump snape_hangout

        "{color=#858585}-Let's hang-{/color}" if wine_ITEM.number < 1 or daytime:
            if daytime:
                m "(I'm not sharing my booze with Snape while he still has to teach classes...)"
                m "(I better ask him during the evening to get drunk...)"
            elif wine_ITEM.number < 1:
                m "(I don't have any more wine...)"
            jump snape_ready


        # Potions
        "-Get a potion-" if her_whoring > 10:
            jump snape_potion_menu


        # Cardgame
        "-Let's Duel- {image=interface/cards.png}" if deck_unlocked:
            jump snape_duel_menu


        # Dismiss
        "-Never mind-":
            stop music fadeout 1.0

            if daytime:
                sna "Alright, back to work then..."
            else:
                sna "Goodnight then."

            call play_sound("door")

            $ snape_busy = True

            jump main_room


# Potion Menu
label snape_potion_menu:
    hide screen snape_main
    with fade

    call sna_main("I notice you're making a bit of progress on Miss Granger.","snape_37", ypos="head")
    call sna_main("I've got some potions here that normally aren't available to students.","snape_47")
    call sna_main("These might help speed up the process...","snape_47")

    menu:
        "-Lactantium-" if potion_inv.has("p_milk_potion"):
            ">You already have a Lactantium potion."
            jump snape_ready
        "-Lactantium-" if not potion_inv.has("p_milk_potion"):
            if potion_scene_11_progress < 1:
                call sna_main("Ah yes, a unique concoction of mine. I have a bottle on hand at all times.","snape_37")
                call sna_main("Just in case...","snape_41")
                call sna_main("Here, take it!","snape_02")
                ">Snape quickly pushes the milky potion into your hands."
                ">Milking potion received!"
                $ potion_inv.add("p_milk_potion")
            elif potion_scene_11_progress == 1:
                call sna_main("Good work on getting her to take it.","snape_37")
                call sna_main("Her breasts did look magnificently full in class.","snape_41")
                call sna_main("mmmm, and I think she was even leaking a little...","snape_41")
                call sna_main("Get her to take another!","snape_46")
                call sna_main("Here, I'll even give you a milker for the slut!","snape_02")
                ">Snape hands you an odd leather and metal harness."
                m "What is-"
                ">Snape quickly pushes another milky potion into your hands."
                ">Milking potion received!"
                call sna_main("Don't worry about it, just get her to put it on. It's enchanted so it will handle the rest...","snape_40")
                call sna_main("but I want it back before you leave!","snape_34")
                call sna_main("I spent a fortune on the self cleaning model...","snape_46")
                $ potion_inv.add("p_milk_potion")
            else:
                call sna_main("Mmmm, I wish I could be there to see you milk her...","snape_41")
                m "..."
                m "(That's probably not a good idea...)"
                call sna_main("All that {b}delicious{/b} milk...","snape_40")
                m "(definitely not a good idea.)"
                call sna_main("...","snape_41")
                call sna_main("Well anyway, I was wondering...","snape_37")
                call sna_main("Want me to augment the potion?","snape_37")
                m "Augmented?"
                m "I never asked for this..."
                call sna_main("I know... I'm offering it...","snape_34")
                m "Oh yeah, sorry. What sort of augmentation?"
                call sna_main("Well I can leave the potion as it is...","snape_38")
                call sna_main("Or I can add an extra little something to it.","snape_40")
                m "Such as?"
                call sna_main("Well...","snape_37")
                label snape_potion_choice:
                    pass
                menu:
                    "-Normal potion-":
                        call sna_main("Here you are Mr. Adventurous...","snape_35")
                        $ potion_version = 1
                    "-futa potion-":
                        call sna_main("What? Are you sure you want this one?","snape_44")
                        call sna_main("I mean I figured you were a bit of a pervert...","snape_02")
                        call sna_main("but I didn't think...","snape_45")
                        call sna_main("Oh well, if you want it, it's yours...","snape_02")
                        menu:
                            "-give it to me-":
                                call sna_main("really?","snape_44")
                                call sna_main("you're more Adventurous than I thought!","snape_02")
                                call sna_main("Here, I'll even give you an extra attachment for the milker!","snape_46")
                                ">Snape hands you a different cannister with a soft plastic opening in the bottom. It looks almost like an anus."
                                call sna_main("I also put an undetectable extension charm on the cannister... Promise to tell me what happens!","snape_45")
                            "-no-":
                                  call sna_main("Too bad...","snape_35")
                                  jump snape_potion_choice

                        $ potion_version = 2
                    "-Permanent breast expansion-":
                        call sna_main("The milk production will still only last a day...","snape_02")
                        call sna_main("But her big boobs will be permanent...","snape_37")
                        call sna_main("Are you sure you want this?","snape_02")
                        call sna_main("She might not like it...","snape_46")
                        menu:
                            "-yes-":
                                call sna_main("Fantastic!!!","snape_45")
                            "-no-":
                                  call sna_main("Too bad...","snape_35")
                                  jump snape_potion_choice

                        $ potion_version = 3
                ">Snape quickly pushes the milky potion into your hands."
                ">Milking potion received!"
                $ potion_inv.add("p_milk_potion")
            jump snape_ready

        "-Veritaserum-" if potion_inv.has("p_veritaserum"):
            ">You already have a Veritaserum potion."
            jump snape_ready
        "-Veritaserum-" if not potion_inv.has("p_veritaserum"):
            call sna_main("Truth potion.","snape_01")
            call sna_main("This is dangerous stuff Genie...","snape_01")
            call sna_main("Use it to make anyone tell the truth.","snape_47")
            call sna_main("Just not me!","snape_36")
            ">Snape hands you the tiny vial filled with a strange gold liquid."
            ">Veritaserum received!"
            $ potion_inv.add("p_veritaserum")
            jump snape_ready

        "-Voluptatem-" if potion_inv.has("p_voluptatem"):
            ">You already a bottle of Voluptatem."
            jump snape_ready
        "-Voluptatem-" if not potion_inv.has("p_voluptatem"):
            m "Volupwhatem?"
            call sna_main("This is actually an experimental potion of mine...","snape_01")
            call sna_main("I'm not sure if this is ready for testing on humans yet.","snape_35")
            ">Snape hands you the small bottle filled with a swirling pink and purple liquid."
            ">Voluptatem received!"
            $ potion_inv.add("p_voluptatem")
            jump snape_ready

        "\"Never mind.\"":
            jump snape_ready
