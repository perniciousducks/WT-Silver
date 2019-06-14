

label cupboard:
    menu:
        "-Examine the cupboard-" if not cupboard_examined:
            $ cupboard_examined = True
            $ searched = True
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

    if day > 1:
        jump rummaging

label rummaging:
    $ searched = True #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.
    $ rum_times += 1 # Counts how many times have you rummaged the cupboard. +1 every time you do that. Needed to make to grand 2 potions before the fight.

    hide screen genie
    show screen rum_screen
    with d3
    show screen bld1
    with d3
    ">You rummage through the cupboard for a while..."

    if day <= 3:
        if rum_times in [1,2]:
            $ potions += 1
            call give_reward(">You found some sort of potion...","interface/icons/item_potion.png")

            show screen genie
            hide screen rum_screen
            hide screen bld1
            with d3

            jump main_room

    if rum_times >= 7 and not map_unlocked:
        $ map_unlocked = True # Turns TRUE after you found the Dahr's oddities catalog in the cupboard.
        call give_reward(">You found a map of the school grounds...\n>You can now leave the office.","interface/icons/item_scroll.png")

        show screen genie
        hide screen rum_screen
        hide screen bld1
        with d3

        if daytime:
            jump day_main_menu
        else:
            jump night_main_menu

    # Item Reward.
    $ random_number = renpy.random.randint(1, 5)

    if day >= 26 and deck_unlocked and random_number in [5] and not card_exist(unlocked_cards,card_dumbledore) :
        call give_reward("You have found a special card!", "images/cardgame/t1/special/dumbledore_v1.png")
        $ unlocked_cards += [card_dumbledore]

        show screen genie
        hide screen rum_screen
        hide screen bld1
        with d3

        if daytime:
            jump day_main_menu
        else:
            jump night_main_menu

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
