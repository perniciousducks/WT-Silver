default cheats_active = False
default cheat_reading = False
default cheat_wardrobe_alpha = False

default skip_duel = False
default skip_to_hermione = False

label cheats:
    menu:
        "-Hermione Cheats-{icon=interface/icons/small/hermione.png}" if hermione_unlocked:
            label .hermione:
            menu:
                "-Reset Hermione's mood-" if her_mood != 0:
                    $ her_mood = 0
                    ">Hermione is no longer mad at you."
                    jump cheats.hermione
                "-Max Whoring-" if her_whoring < 24:
                    $ her_whoring = 24
                    ">Hermione is now a giant slut."
                    jump cheats.hermione

                "-Increase Whoring-" if her_whoring < 24:
                    $ her_whoring += 1
                    ">Hermione became more depraved..."
                    jump cheats.hermione
                "-Decrease Whoring-" if her_whoring > 0:
                    $ her_whoring += -1
                    "Hermione recovered some of her dignity"
                    jump cheats.hermione

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
                    jump cheats.hermione

                "-Back-":
                    jump cheats

        "-Astoria Cheats-{icon=interface/icons/small/astoria.png}" if astoria_unlocked:
            label .astoria:
            menu:
                "-Reset Astoria's mood-" if ast_mood != 0:
                    $ ast_mood = 0
                    ">Astoria is no longer mad at you."
                    jump cheats.astoria
                "-Max Affection-" if ast_affection < 24:
                    $ ast_affection = 24
                    ">Astoria has hots for you."
                    jump cheats.astoria

                "-Increase Affection-" if ast_affection < 24:
                    $ ast_affection += 1
                    ">Astoria likes you more..."
                    jump cheats.astoria
                "-Decrease Affection-" if ast_affection > 0:
                    $ ast_affection += -1
                    "Astoria likes you less..."
                    jump cheats.astoria
                "-Back-":
                    jump cheats

        "-Luna Cheats-{icon=interface/icons/small/luna.png}" if luna_unlocked:
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

        "-Cho Cheats-{icon=interface/icons/small/cho.png}" if cho_unlocked:
            label .cho:
            menu:
                "-Reset Cho's mood-":
                    $ cho_mood = 0
                    ">Cho is no longer mad at you."
                    jump cheats.cho
                "-Unlock Wardrobe-" if not cho_wardrobe_unlocked:
                    $ cho_wardrobe_unlocked = True
                    $ cc_muggle_hot_ITEM.unlocked = True
                    ">Cho's wardrobe is now accessible."
                    jump cheats.cho
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
                    jump cheats.cho
                "-Reset ALL Cho content-":
                    call reset_cho_progress
                    ">Cho content reset!"
                    jump cheats.cho
                "-Back-":
                    jump cheats

        "-Book Cheats-{icon=interface/icons/small/book.png}" if store_intro_done:
            label .books:
            menu:
                "-Max Imagination":
                    $ imagination = 8
                    $ bdsm_imagination = 2
                    "Your imagination grows!"
                    jump cheats.books
                "-Cheat Reading ([cheat_reading])-":
                    $ cheat_reading = not cheat_reading
                    jump cheats.books
                "-All Books-" if day >= 16:
                    python:
                        for book in book_list.get_all():
                            book.unlockable = False
                            book.unlocked = True
                    "Obtained All Books."
                    jump cheats.books
                "-Back-":
                    jump cheats

        "-Potion Cheats-{icon=interface/icons/small/potion.png}":
            label cheats_potions:
            menu:
                "-Add all normal potions-":
                    $ potion_inv.extend(["p_cum_addiction","p_ass_expansion","p_breast_expansion","p_cat_transformation","p_luna_transformation","p_transparency","p_hypno"])
                    ">All potions added (Does not include Snape's potions)"
                    jump cheats_potions
                "-Back-":
                    jump cheats

        "-Solve the slider puzzle-" if puzzle_box_ITEM.unlocked == True and unlocked_7th == False:
            $ unlocked_7th = True
            jump open_puzzle_box

        "-Add Gold-{icon=interface/icons/small/gold.png}":
            $ gold += 500
            "You've obtained 500g."
            jump cheats

        "-Add Slytherin Points-{icon=interface/icons/small/slyt.png}":
            $ slytherin += 200
            call house_points
            "Two hundred points to Slytherin!"
            jump cheats

        "-Wardrobe transparency-{icon=interface/icons/small/wardrobe.png}":
            $ cheat_wardrobe_alpha = not cheat_wardrobe_alpha
            if cheat_wardrobe_alpha:
                "Wardrobe transparency slider is enabled."
            else:
                "Wardrobe transparency slider is disabled."
            jump cheats

        "-{color=#7a0000}DEVROOM{/color}-" if config.developer:
            label .devroom:
            menu:
                "-Unlock all characters-{icon=interface/icons/small/condom.png}":
                    $ snape_unlocked = True
                    $ tonks_unlocked = True
                    $ hermione_unlocked = True
                    $ cho_unlocked = True
                    $ astoria_unlocked = True
                    $ susan_unlocked = True
                    $ luna_unlocked = True
                    # ginny_unlocked = True
                    # voldermort_unlocked = True
                    # hagrid_unlocked = True
                    jump cheats.devroom
                "-Unlock all characters wardrobe-{icon=interface/icons/small/wardrobe.png}":
                    $ tonks_wardrobe_unlocked = True
                    $ hermione_wardrobe_unlocked = True
                    $ cho_wardrobe_unlocked = True
                    $ astoria_wardrobe_unlocked = True
                    $ susan_wardrobe_unlocked = True
                    $ luna_wardrobe_unlocked = True
                    # ginny_wardrobe_unlocked = True
                    # voldemort_wardrobe_unlocked = True
                    # hagrid_wardrobe_unlocked = True
                    jump cheats.devroom
                "-Unlock all characters clothes-{icon=interface/icons/small/wardrobe.png}":
                    python:
                        for i in ("hermione", "cho", "astoria", "tonks"):
                            for x in getattr(renpy.store, i).wardrobe_list:
                                x.unlocked = True
                    jump cheats.devroom
                "-Get 100 of all gift items-{icon=interface/icons/small/gift.png}":
                    python:
                        for i in candy_gift_list:
                            i.number = 100
                        for i in drink_gift_list:
                            i.number = 100
                        for i in mag_gift_list:
                            i.number = 100
                        for i in toy_gift_list:
                            i.number = 100
                    jump cheats.devroom
                "-Get all scrolls-{icon=interface/icons/small/spell.png}":
                    python:
                        for i in scroll_list_A:
                            i.unlocked = True
                        for i in scroll_list_B:
                            i.unlocked = True
                        for i in scroll_list_C:
                            i.unlocked = True
                        sealed_scroll_ITEM.unlocked = True
                    jump cheats.devroom
                "-Get all books-{icon=interface/icons/small/book.png}":
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
                    jump cheats.devroom
                "-Get all decorations-{icon=interface/icons/small/gold.png}":
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
                    jump cheats.devroom
                "-Read Hermione's Diary-{icon=interface/icons/small/hermione.png}":
                    call book_handle(book=hermione_diary)
                    jump cheats.devroom
                "Gallery test":
                    jump open_gallery
                "Lootbox":
                    call card_lootbox
                    jump cheats.devroom
                "-Back-":
                    jump cheats

        "-Never mind-":
            jump main_room_menu