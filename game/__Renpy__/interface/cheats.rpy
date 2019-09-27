default cheats_active = False
default cheat_reading = False
default cheat_wardrobe_alpha = False

default skip_duel = False
default skip_to_hermione = False

label cheats:
    menu:
        "-Hermione Cheats-" if hermione_unlocked:
            label cheats_hermione:
            menu:
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
                    $ unlock_clothing_compat(hg_gamble_slut_ITEM) # Gambler outfit is not included in above lists
                    call update_deco_items # Call needed to update gambler outfit image
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
                    call reset_luna_progress
                    ">Luna content reset!"
                    jump cheats
                "-never mind-":
                    jump cheats

        "-Mail ministry letter-" if her_whoring >= 2 and not letter_min_curses.read:
            $ letter_min_curses.mailLetter()
            ">Letter sent."
            jump cheats
        # "-Astoria & Susan Cheats-" if astoria_unlocked:
            # label cheats_astoria:
            # menu:
                # "-Unlock all outfits & sets-":
                    # python:
                        # for item in astoria_outfits_list:
                            # unlock_clothing_compat(item)
                        # for item in astoria_costumes_list:
                            # unlock_clothing_compat(item)
                        # for item in astoria_dresses_list:
                            # unlock_clothing_compat(item)
                        # for item in astoria_clothing_sets_list:
                            # unlock_clothing_compat(item)
                    # ">All of Astoria's outfits and clothing sets have been unlocked."
                    # jump cheats_astoria

                # "-never mind-":
                    # jump cheats

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
                        cho_outfit_cheerleader.unlock()
                    ">All of Cho's outfits and clothing sets have been unlocked."
                    jump cheats_cho
                "-Reset ALL Cho content-":
                    call reset_cho_progress
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
            jump open_puzzle_box

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

        "-Wardrobe transparency-":
            $ cheat_wardrobe_alpha = not cheat_wardrobe_alpha
            if cheat_wardrobe_alpha:
                "Wardrobe transparency slider is enabled."
            else:
                "Wardrobe transparency slider is disabled."
            jump cheats
            
        "-{color=#7a0000}DEVROOM{/color}-" if config.developer:
            label devroom:
            menu:
                "-Unlock all characters-":
                    $ snape_unlocked = True
                    $ tonks_unlocked = True
                    $ hermione_unlocked = True
                    $ cho_unlocked = True
                    $ astoria_unlocked = True
                    $ susan_unlocked = True
                    $ luna_unlocked = True
                    # ginny_unlocked = True
                    jump devroom
                "-Unlock all characters wardrobe-":
                    $ tonks_wardrobe_unlocked = True
                    $ hermione_wardrobe_unlocked = True
                    $ cho_wardrobe_unlocked = True
                    $ astoria_wardrobe_unlocked = True
                    $ susan_wardrobe_unlocked = True
                    $ luna_wardrobe_unlocked = True
                    # ginny_wardrobe_unlocked = True
                    jump devroom
                "-Get 100 of all gift items-":
                    python:
                        for i in candy_gift_list:
                            i.number = 100
                        for i in drink_gift_list:
                            i.number = 100
                        for i in mag_gift_list:
                            i.number = 100
                        for i in toy_gift_list:
                            i.number = 100
                    jump devroom
                "-Get all scrolls-":
                    python:
                        for i in scroll_list_A:
                            i.unlocked = True
                        for i in scroll_list_B:
                            i.unlocked = True
                        for i in scroll_list_C:
                            i.unlocked = True
                        sealed_scroll_ITEM.unlocked = True
                    jump devroom
                "-Get all books-":
                    python:
                        for i in book_list.read_books:
                            i.unlocked = True
                            i.unlockable = False
                        for i in book_list.write_books:
                            i.unlocked = True
                            i.unlockable = False
                        for i in book_list.fiction_books:
                            i.unlocked = True
                            i.unlockable = False
                    jump devroom
                "-Get all decorations-":
                    python:
                        for i in wall_deco_list:
                            i.unlocked = True
                        for i in fireplace_deco_list:
                            i.unlocked = True
                        for i in cupboard_deco_list:
                            i.unlocked = True
                        for i in misc_deco_list:
                            i.unlocked = True
                        for i in misc_hat_list:
                            i.unlocked = True
                    jump devroom
                "-Read Hermione's Diary-":
                    call her_whoring_pages
                    call cheat_append_all_pages
                    call book_handle(book=hermione_diary)
                    jump devroom
                "Gallery test":
                    jump open_gallery
                "Lootbox":
                    call card_lootbox
                    jump devroom
                "Return":
                    jump cheats

        "-Never mind-":
            jump main_room_menu
