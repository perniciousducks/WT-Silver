label cheats:
    menu:
        "-Hermione Cheats-":
            label cheats_hermione:
            menu:
                "-Reset Hermione's mood-":
                    $ mad = 0
                    ">Hermione is no longer mad at you."
                    jump cheats
                "-Max Whoring-":
                    $ whoring = 24
                    ">Hermione is now a giant slut."
                    jump cheats_hermione

                "-Increase Whoring-":
                    if whoring >= 24:
                        ">Hermione's whoring is at the max level and can't be increased any further!"
                    else:
                        $ whoring += 1
                        ">Hermione became more depraved..."
                    jump cheats_hermione
                "-Decrease Whoring-":
                    if whoring <= 0:
                        "Hermione's whoring can't be decreased any further!"
                    else:
                        $ whoring -= 1
                        "Hermione recovered some of her dignity"
                    jump cheats_hermione

                "-Unlock public favours-":
                    $ force_unlock_pub_favors = True
                    $ touched_by_boy = True
                    $ lock_public_favors = False
                    ">Public favours unlocked!"
                    jump cheats_hermione

                "-Unlock all purchasable outfits & sets-":
                    python:
                        for i in hermione_outfits_list:
                            if not i.unlockable:
                                i.unlocked = True
                        for i in hermione_clothing_sets_list:
                            if not i.unlockable:
                                i.unlocked = True
                    ">All of Hermione's purchasable outfits and clothing sets have been unlocked."
                    jump cheats

                "-Toggle Breast Expansion-":
                    if hermione_perm_expand or hermione_perm_expand_breasts or hermione_expand_breasts:
                        $ hermione_perm_expand_breasts = False
                        $ hermione_expand_breasts = False
                        $ hermione_perm_expand = False
                        "Hermione's breasts shrink..."
                    else:
                        $ hermione_perm_expand_breasts = True
                        "Hermione's breasts grow..."
                    jump cheats

                "-Toggle Futa Hermione-":
                    if hermione_futa:
                        $ hermione_futa = False
                        "Hermione's cock shrinks away..."
                    else:
                        $ hermione_futa = True
                        "Hermione's grows a... dick!"
                    jump cheats
                "-never mind-":
                    jump cheats

        "-Luna Cheats-":
            label cheats_luna:
            menu:
                "-Reset ALL Luna content-":
                    $ reset_luna_content = True
                    call luna_progress_init
                    $ reset_luna_content = False
                    ">Luna content reset!"
                    jump cheats
                "-never mind-":
                    jump cheats

        "-Cho Cheats-":
            label cheats_cho:
            menu:
                "-Reset Cho's mood-":
                    $ cho_mad = 0
                    ">Cho is no longer mad at you."
                    jump cheats
                "-Reset ALL Cho content-":
                    $ reset_cho_content = True
                    call cho_progress_init
                    $ reset_cho_content = False
                    ">Cho content reset!"
                    jump cheats
                "-never mind-":
                    jump cheats

        "-Book Cheats-":
            label cheats_books:
            menu:
                "-Max Imagination":
                    $ imagination = 5
                    "Your imagination grows!"
                    jump cheats_books
                "-Cheat Reading ([cheat_reading])-":
                    $ cheat_reading = not cheat_reading
                    jump cheats_books
                "-All Books-" if day >= 16:
                    python:
                        for book in Books_OBJ.get_all():
                            book.purchased = True
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

        "-Solve the slider puzzle-" if found_puzzle_1 and unlocked_7th:
            $ unlocked_7th = False
            jump open_pyzzle_box

        "-Add Gold-":
            $ gold += 500
            "You've obtained 500g."
            jump cheats

        "-Add Slytherin Points-":
            $ slytherin += 200
            "200 points to Slytherin!"
            jump cheats

        "-Map-" if day >= 5 and not cataloug_found:
            "The marauder's map has been added to your inventory!"
            $ cataloug_found = True
            jump cheats

        "-Never mind-":
            jump day_main_menu
