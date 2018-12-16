

label cupboard:
    menu:
        "-Examine the cupboard-" if not cupboard_examined:
            $ cupboard_examined = True
            show screen chair_left #Empty chair near the desk.
            hide screen genie
            call gen_chibi("stand","behind_desk","base",flip=True)
            show screen desk
            with Dissolve(0.5)

            m "Hm....."
            m "A cupboard..."
            m "Maybe I should rummage through this one later..."
            show screen genie
            hide screen genie_stand
            hide screen chair_left #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu

        "-Rummage through the cupboard-" if not searched and not day == 1:
            jump rummaging
        "{color=#858585}-Rummage through the cupboard-{/color}" if searched and not day == 1:
            call already_did #Message that says that you have searched the cupboard today already.
            jump cupboard

        "-Tentacle Scroll-" if tentacle_owned:
            ">Should I use this scroll..."
            menu:
                "\"(Yes, let's do it!)\"":
                    jump tentacle_scene_intro
                "\"(Not right now.)\"":
                    jump possessions
        "-Tentacle Scroll-" if sealed_scroll_ITEM.unlocked and not tentacle_owned:
            m "It's missing the key ingredient."
            jump possessions

        "Box with a puzzle on it" if found_puzzle_1 == True:
            jump start_slide_puzzle

        #Temporary!
        "-Doze off-" if daytime and day != 1:
            jump night_start
        "-Go to sleep-" if not daytime and day != 1:
            jump day_start

        "-Jerk Off-" if not day == 1:
            jump jerk_off

        "-Never mind-":
            jump day_main_menu

label options_menu:
    menu:
        "-Save and Load-":
            call screen save()

        "-Change Save Name-":
            jump custom_save

        "-Options-":
            menu:
                "-Change Game Difficulty-" if game_difficulty <= 2:
                    menu:
                        "-Enable Easy Difficulty-":
                            $ game_difficulty = 1
                            $ cheat_reading = True
                            "Game set to easy difficulty!"
                            "Increased gold reward from reports and other sources!"
                            "Rummaging through your cupboard is more rewarding!"
                            "Snape will be more generous with Slytherin-points!"
                            "Hermione won't stay mad at you for as long!"
                            jump day_main_menu
                        "-Enable Normal Difficulty-":
                            $ game_difficulty = 2
                            $ cheat_reading = False
                            "Game set to normal difficulty!"
                            jump day_main_menu
                        "-Back-":
                            jump day_main_menu
                "-Replace Chibis with Sprites-" if not use_cgs:
                    ">The last two personal favours will use sprites now."
                    $ use_cgs = True
                    jump options_menu
                "-Replace Sprites with Chibis-" if use_cgs:
                    ">The last two personal favours will use chibi animations again."
                    $ use_cgs = False
                    jump options_menu
                "-Back-":
                    jump options_menu

        "-Cheats-" if cheats_active and game_difficulty <= 2 and day > 1:
            jump cheats

        "-Bugfix-":
            menu:
                "-Reset Everyone's Appearance-":
                    call reset_hermione_base
                    call reset_hermione_clothing
                    call reset_luna_base
                    call reset_luna_clothing
                    call reset_astoria_clothing
                    call reset_susan_clothing
                    call reset_cho_clothing
                    call reset_tonks_clothing
                    ">Appearance of each girl set back to default."
                    jump options_menu
                "-Reset ALL Luna content-" if hat_known:
                    $ reset_luna_content = True
                    call luna_init
                    call luna_progress_init
                    $ reset_luna_content = False
                    ">Luna content reset!"
                    jump options_menu
                "-Never mind-":
                    jump options_menu

        "-Decorate-" if day != 1:
            label decorate_room_menu:
            menu:
                ">Decorate your place..."
                "-Xmas decorations-":
                    pause.5
                    hide screen main_room_deco
                    $ room_deco = "_deco_1"
                    $ gen_outfit = "_santa"
                    show screen main_room_deco
                    with d9
                    pause.5
                "-Cupboard pinup girl-":
                    $ cupboard_deco = "_deco_1"
                    ">Pinup girl added! You'll see it when rummaging through the cupboard."
                "-Remove deco-":
                    pause.5
                    hide screen main_room_deco
                    $ room_deco = ""
                    $ cupboard_deco = ""
                    $ gen_outfit = ""
                    show screen main_room_deco
                    with d5
                    pause.5
                "-All done-":
                    jump day_main_menu
            jump decorate_room_menu

        "-Display Characters-" if day != 1:
            jump summon_characters

        "-Never mind-":
            jump day_main_menu

label custom_save:
    $ temp_name = renpy.input("(Please enter the save name.)")
    $ temp_name = temp_name.strip()
    if temp_name == "":
        $ temp_name = "Day - "+str(day)+"\nWhoring - "+str(her_whoring)
    $ save_name = temp_name
    "Done."
    jump options_menu



label rummaging:

    $ searched = True #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.

    $ rum_times += 1 # Counts how many times have you rummaged the cupboard. +1 every time you do that. Needed to make to grand 2 potions before the fight.

    hide screen genie
    show screen rum_screen
    with d3
    show screen bld1
    with d3
    ">You rummage through the cupboard for a while..."

    if day <= 4:
        if rum_times in [1,2,3]:
            $ potions += 1
            call give_reward(">You found some sort of potion...","interface/icons/item_potion.png")

            show screen genie
            hide screen rum_screen
            hide screen bld1
            with d3

            if daytime:
                jump night_start
            else:
                jump day_start

    if rum_times >= 7 and not map_unlocked:
        $ map_unlocked = True # Turns TRUE after you found the Dahr's oddities catalog in the cupboard.
        call give_reward(">You found a map of the school grounds...\n>You can now leave the office.","interface/icons/item_scroll.png")

        show screen genie
        hide screen rum_screen
        hide screen bld1
        with d3

        if daytime:
            jump night_start
        else:
            jump day_start

    # Item Reward.
    $ random_number = renpy.random.randint(1, 5)

    if game_difficulty >= 2:               #Normal and hardcore difficulty
        if random_number in [1,2,3,4]: # Found something. 80% chance.
            jump rum_rewards
        else:
            ">...You find nothing of value."
            show screen genie
            hide screen rum_screen

            hide screen bld1
            with d3

            if daytime:
                jump day_main_menu
            else:
                jump night_main_menu
    else:                                  #Easy difficulty
        jump rum_rewards

label rum_rewards:
    $ random_number = renpy.random.randint(1, 20)

    if game_difficulty <= 2: #Easy and Normal difficulty.

        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            if random_number in [1,2]:
                call rum_block(lollipop_ITEM)
            elif random_number in [3]:
                call rum_block(plush_owl_ITEM)
            elif random_number in [4,5]:
                call rum_block(chocolate_ITEM)
            elif random_number in [6]:
                call rum_block(sexy_lingerie_ITEM)
            else:
                if random_number <= 12:
                    call rum_block("gold1")
                else:
                    call rum_block("wine")

        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            if random_number in [1,2]:
                call rum_block(lollipop_ITEM)
            elif random_number in [3]:
                call rum_block(porn_mag_ITEM)
            elif random_number in [4]:
                call rum_block(sexy_lingerie_ITEM)
            elif random_number in [5]:
                call rum_block(chocolate_ITEM)
            elif random_number in [6]:
                call rum_block(krum_poster_ITEM)
            else:
                if random_number <= 14:
                    call rum_block("gold2")
                else:
                    call rum_block("wine")

        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            if random_number in [1]:
                call rum_block(vibrator_ITEM)
            elif random_number in [2,3]:
                call rum_block(pink_condoms_ITEM)
            elif random_number in [4,5]:
                call rum_block(butterbeer_ITEM)
            elif random_number in [6]:
                call rum_block(krum_poster_ITEM)
            else:
                if random_number <= 16:
                    call rum_block("gold3")
                else:
                    call rum_block("wine")

        if her_whoring >= 18: # Lv 7+
            if random_number in [1]:
                call rum_block(broom_2000_ITEM)
            elif random_number in [2,3,4]:
                call rum_block(butterbeer_ITEM)
            elif random_number in [5]:
                call rum_block(chocolate_ITEM)
            elif random_number in [6]:
                call rum_block(krum_poster_ITEM)
            elif random_number in [7]:
                call rum_block(anal_plugs_ITEM)
            elif random_number in [8]:
                call rum_block(testral_strapon_ITEM)
            else:
                if random_number <= 18:
                    call rum_block("gold4")
                else:
                    call rum_block("wine")

    else: # Hardcore difficulty. # Sex items only.

        if random_number in [1]:
            call rum_block(porn_mag_ITEM)
        elif random_number in [2]:
            call rum_block(vibrator_ITEM)
        elif random_number in [3]:
            call rum_block(sexy_lingerie_ITEM)
        elif random_number in [4]:
            call rum_block(pink_condoms_ITEM)
        elif random_number in [5]:
            call rum_block(anal_plugs_ITEM) #Butt Plug
        elif random_number in [6]:
            call rum_block(anal_beads_ITEM) #Snek
        elif random_number in [7]:
            call rum_block(anal_lube_ITEM)
        elif random_number in [8]:
            call rum_block(testral_strapon_ITEM)
        elif random_number in [9]:
            call rum_block(ballgag_and_cuffs_ITEM)
        elif random_number in [10]:
            call rum_block(sexdoll_ITEM)
        else:
            if her_whoring >= 21: # Lv 7+
                call rum_block(butterbeer_ITEM)
            else:
                call rum_block("wine")

    show screen genie
    hide screen rum_screen

    hide screen bld1
    with d3

    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu

label rum_block(item = ""):
    if item == "wine":
        $ renpy.play('sounds/win2.mp3')   #Not loud.
        $ wine += 1
        $ the_gift = "interface/icons/item_wine.png" # WINE
        show screen gift
        with d3
        ">You found a bottle of wine from professor dumbledore's personal stash..."
        hide screen gift
        with d3
    elif item in ["gold1","gold2","gold3","gold4"]: #Gold
            if item == "gold1":
                $ tmp_gold = gold1
            if item == "gold2":
                $ tmp_gold = gold2
            if item == "gold3":
                $ tmp_gold = gold3
            if item == "gold4":
                $ tmp_gold = gold4
            $ renpy.play('sounds/win2.mp3')   #Not loud.
            $ the_gift = "interface/icons/gold.png" # GOLD.
            show screen gift
            with d3
            ">You found [tmp_gold] gold..."
            $ gold += tmp_gold
            hide screen gift
            with d3
    else:
        $ renpy.play('sounds/win2.mp3')   #Not loud.
        $ item.number += 1
        $ the_gift = item.get_image()
        show screen gift
        with d3
        ">You found [item.name]..."
        ">[item.description]"
        hide screen gift
        with d3
    return



######################
label already_did:
    show screen bld1
    with d3
    m "I already did that today..."
    hide screen bld1
    with d3
    return
