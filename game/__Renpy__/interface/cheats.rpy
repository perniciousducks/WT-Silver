label cheats:
    menu:
        "-Hermione Cheats-" if hermione_unlocked:
            label cheats_hermione:
            menu:
                "-Read Hermione's Diary-":
                    call her_whoring_pages
                    call cheat_append_all_pages
                    call book_handle(book=hermione_diary)
                    jump cheats_hermione
                "-Reset Hermione's mood-" if her_mood != 0:
                    $ her_mood = 0
                    ">Hermione is no longer mad at you."
                    jump cheats_hermione
                "-Max Whoring-" if her_whoring < 24:
                    $ her_whoring = 24
                    ">Hermione is now a giant slut."
                    jump cheats_hermione

                "-Increase Whoring-" if her_whoring < 24:
                    $ her_whoring += 1
                    ">Hermione became more depraved..."
                    jump cheats_hermione
                "-Decrease Whoring-" if her_whoring > 0:
                    $ her_whoring += -1
                    "Hermione recovered some of her dignity"
                    jump cheats_hermione

                "-Unlock all outfits & sets-":
                    python:
                        for item in hermione_outfits_list:
                            unlock_clothing_compat(item)
                        for item in hermione_costumes_list:
                            unlock_clothing_compat(item)
                        for item in hermione_dresses_list:
                            unlock_clothing_compat(item)
                        for item in hermione_clothing_sets_list:
                            unlock_clothing_compat(item)
                    ">All of Hermione's outfits and clothing sets have been unlocked."
                    jump cheats_hermione

                "-Toggle Breast Expansion-":
                    if hermione_perm_expand_breasts or hermione_expand_breasts:
                        $ hermione_perm_expand_breasts = False
                        $ hermione_expand_breasts = False
                        "Hermione's breasts shrink..."
                    else:
                        $ hermione_perm_expand_breasts = True
                        "Hermione's breasts grow..."
                    jump cheats_hermione

                "-Toggle Futa Hermione-":
                    if hermione_futa:
                        $ hermione_futa = False
                        "Hermione's cock shrinks away..."
                    else:
                        $ hermione_futa = True
                        "Hermione's grows a... dick!"
                    jump cheats_hermione
                "-never mind-":
                    jump cheats

        "-Luna Cheats-" if luna_unlocked:
            label cheats_luna:
            menu:
                "-Unlock all outfits & sets-":
                    python:
                        for item in luna_outfits_list:
                            unlock_clothing_compat(item)
                        for item in luna_costumes_list:
                            unlock_clothing_compat(item)
                        for item in luna_dresses_list:
                            unlock_clothing_compat(item)
                        for item in luna_clothing_sets_list:
                            unlock_clothing_compat(item)
                    ">All of Luna's outfits and clothing sets have been unlocked."
                    jump cheats_luna

                "-Sub Luna-":
                    $ lun_sub = 8
                    $ lun_whoring = 10
                    "Set to Sub Luna"
                    jump cheats_luna
                "-Dom Luna-":
                    $ lun_dom = 8
                    $ lun_whoring = 10
                    "Set to Dom Luna"
                    jump cheats_luna

                "-Reset ALL Luna content-":
                    $ reset_luna_content = True
                    call luna_progress_init
                    $ reset_luna_content = False
                    ">Luna content reset!"
                    jump cheats
                "-never mind-":
                    jump cheats

        "-Mail ministry letter-" if her_whoring >= 2 and not letter_curse_complaint_OBJ.read:
            $ letter_curse_complaint_OBJ.mailLetter()
            ">Letter sent."
            jump cheats
        "-Astoria & Susan Cheats-" if astoria_unlocked:
            label cheats_astoria:
            menu:
                "-Unlock all outfits & sets-":
                    python:
                        for item in astoria_outfits_list:
                            unlock_clothing_compat(item)
                        for item in astoria_costumes_list:
                            unlock_clothing_compat(item)
                        for item in astoria_dresses_list:
                            unlock_clothing_compat(item)
                        for item in astoria_clothing_sets_list:
                            unlock_clothing_compat(item)
                    ">All of Astoria's outfits and clothing sets have been unlocked."
                    jump cheats_astoria

                "-Unlock first spell-":
                    $ ast_affection = 2
                    $ astoria_tonks_1_completed = True
                    $ astoria_tonks_2_completed = True

                    $ ag_cs_imperio_sb.points = 3
                    ">Astoria can now use the first spell!"
                    jump cheats_astoria
                "-never mind-":
                    jump cheats

        "-Cho Cheats-" if cho_unlocked:
            label cheats_cho:
            menu:
                "-Reset Cho's mood-":
                    $ cho_mood = 0
                    ">Cho is no longer mad at you."
                    jump cheats_cho
                "-Unlock Wardrobe-" if not cho_wardrobe_unlocked:
                    $ cho_wardrobe_unlocked = True
                    $ cc_muggle_hot_ITEM.unlocked = True
                    ">Cho's wardrobe is now accessible."
                    jump cheats_cho
                "-Unlock all outfits & sets-":
                    python:
                        for item in cho_outfits_list:
                            unlock_clothing_compat(item)
                        for item in cho_costumes_list:
                            unlock_clothing_compat(item)
                        for item in cho_dresses_list:
                            unlock_clothing_compat(item)
                        for item in cho_clothing_sets_list:
                            unlock_clothing_compat(item)
                    ">All of Cho's outfits and clothing sets have been unlocked."
                    jump cheats_cho
                "-Reset ALL Cho content-":
                    $ reset_cho_content = True
                    call cho_progress_init
                    $ reset_cho_content = False
                    ">Cho content reset!"
                    jump cheats_cho
                "-never mind-":
                    jump cheats

        "-Book Cheats-" if store_intro_done:
            label cheats_books:
            menu:
                "-Max Imagination":
                    $ imagination = 8
                    $ bdsm_imagination = 2
                    "Your imagination grows!"
                    jump cheats_books
                "-Cheat Reading ([cheat_reading])-":
                    $ cheat_reading = not cheat_reading
                    jump cheats_books
                "-All Books-" if day >= 16:
                    python:
                        for book in book_list.get_all():
                            book.unlockable = False
                            book.unlocked = True
                    "Obtained All Books."
                    jump cheats_books
                "-never mind-":
                    jump cheats

        "-Potion Cheats-":
            label cheats_potions:
            menu:
                "-Add all normal potions-":
                    $ potion_inv.extend(["p_cum_addiction","p_ass_expansion","p_breast_expansion","p_cat_transformation","p_luna_transformation","p_transparency","p_hypno"])
                    ">All potions added (Does not include Snape's potions)"
                    jump cheats_potions
                "-never mind-":
                    jump cheats

        "-Solve the slider puzzle-" if puzzle_box_ITEM.unlocked == True and unlocked_7th == False:
            $ unlocked_7th = True
            jump open_pyzzle_box

        "-Add Gold-":
            $ gold += 500
            "You've obtained 500g."
            jump cheats

        "-Add Slytherin Points-":
            $ slytherin += 200
            call house_points
            "200 points to Slytherin!"
            jump cheats

        "-Map-" if day >= 5 and not map_unlocked:
            "The marauder's map has been added to your inventory!"
            $ map_unlocked = True
            jump cheats

        "-Never mind-":
            jump day_main_menu

label cheats_init:

    #Update 1.34
    if not hasattr(renpy.store,'cheats_active') or reset_persistants:
        label reset_cheats_init:

        $ cheats_active = False
        $ cheat_reading = False

        $ next_day = False
        $ skip_duel = False
        $ skip_to_hermione = False
        $ skip_after_hermione = False

        #Display Characters Screen
        $ character_choice = "hermione"
        $ summoned_character_list = []

        $ display_character_hermione = False
        $ display_character_luna = False
        $ display_character_astoria = False
        $ display_character_susan = False
        $ display_character_cho = False

        $ display_character_genie = False
        $ display_character_snape = False
        $ display_character_tonks = False

        $ display_background = False
        $ custom_bg_image = "images/rooms/_bg_/main_room_night.png"

    label update_display_characters_summon_list:
        $ character_summon_list = []
        if hermione_unlocked:
            $ character_summon_list.append("hermione")
        if luna_unlocked:
            $ character_summon_list.append("luna")
        if astoria_unlocked:
            $ character_summon_list.append("astoria")
        if susan_unlocked:
            $ character_summon_list.append("susan")
        if cho_unlocked:
            $ character_summon_list.append("cho")
        $ character_summon_list.append("genie")
        $ character_summon_list.append("snape")
        if tonks_unlocked:
            $ character_summon_list.append("tonks")
        $ character_summon_list.append("bg")

    return
