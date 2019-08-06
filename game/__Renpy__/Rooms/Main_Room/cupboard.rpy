

### Cupboard ###

label cupboard:
    if not cupboard_examined:
        $ cupboard_examined = True
        $ searched = True
        show screen chair_left
        hide screen genie
        call gen_chibi("stand","behind_desk","base", flip=True)
        show screen desk
        with d5
        pause.2

        call bld
        m "Hm....."
        m "A cupboard..."
        m "Maybe I should rummage through this one later..."
        jump day_main_menu


    jump rummaging



label rummaging:

    $ searched = True # Resets every day/night.
    $ rum_times += 1  # Stat counter.

    hide screen genie
    show screen rum_screen
    with d3
    show screen bld1
    with d3

    ">You rummage through the cupboard for a while..."


    ### Intem Rewards ###
    $ random_percent = renpy.random.randint(1, 100)


    # Dueling Potion.
    if day <= 3 and rum_times in [1,2]:
        $ potions += 1
        call give_reward(">You found some sort of potion...","interface/icons/item_potion.png")

        jump main_room


    # Map.
    if hermione_favors and not map_unlocked:
        $ map_unlocked = True # Turns TRUE after you found the Dahr's oddities catalog in the cupboard.
        call give_reward(">You found a map of the school grounds...\n>You can now leave the office.","interface/icons/item_scroll.png")

        jump main_room


    # Dumbledore Card.
    if day >= 26 and deck_unlocked and random_percent <= 40 and not card_exist(unlocked_cards,card_dumbledore) :
        call give_reward("You have found a special card!", "images/cardgame/t1/special/dumbledore_v1.png")
        $ unlocked_cards += [card_dumbledore]

        jump main_room



    ##################################################
    ### Add your cupboard unlocks above this line. ###
    ##################################################

    # Wine/firewhisky.
    if firewhisky_ITEM.unlocked and firewhisky_ITEM.number < 1:
        call rum_block(firewhisky_ITEM)
    elif wine_ITEM.number < 1:
        call rum_block(wine_ITEM)

    elif random_percent <= 50:
        if firewhisky_ITEM.unlocked and random_percent <= 25:
            call rum_block(firewhisky_ITEM)
        else:
            call rum_block(wine_ITEM)

    # Gold.
    elif random_percent <= 60:
        call rum_block("gold")

    # Items.
    else:

        if game_difficulty <= 2: # Easy and Normal difficulty.

            if her_tier in [1]:
                $ random_choice = renpy.random.choice([lollipop_ITEM, plush_owl_ITEM, chocolate_ITEM])
            elif her_tier in [2]:
                $ random_choice = renpy.random.choice([science_mag_ITEM, lollipop_ITEM, chocolate_ITEM, butterbeer_ITEM, sexy_lingerie_ITEM])
            elif her_tier in [3]:
                $ random_choice = renpy.random.choice([girls_mag_ITEM, lollipop_ITEM, butterbeer_ITEM, krum_poster_ITEM])
            elif her_tier in [4]:
                $ random_choice = renpy.random.choice([adult_mag_ITEM, butterbeer_ITEM, pink_condoms_ITEM, krum_poster_ITEM])
            elif her_tier in [5]:
                $ random_choice = renpy.random.choice([porn_mag_ITEM, pink_condoms_ITEM, vibrator_ITEM, anal_lube_ITEM, anal_plugs_ITEM])
            else:
                $ random_choice = renpy.random.choice([broom_2000_ITEM, vibrator_ITEM, anal_lube_ITEM, anal_plugs_ITEM, testral_strapon_ITEM])

        else: # Hardcore difficulty. # Sex items only.

            $ random_choice = renpy.random.choice([adult_mag_ITEM, porn_mag_ITEM, butterbeer_ITEM, pink_condoms_ITEM, anal_lube_ITEM, sexy_lingerie_ITEM, anal_plugs_ITEM, sexdoll_ITEM])

        call rum_block(random_choice)

    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu


label rum_block(item = ""):
    if item == "gold":
        $ renpy.play('sounds/win2.mp3')
        $ the_gift = "interface/icons/gold.png"
        show screen gift
        with d3
        ">You found [random_gold] gold..."
        $ gold += random_gold

    else:
        $ renpy.play('sounds/win2.mp3')
        $ item.number += 1
        $ the_gift = item.get_image()
        show screen gift
        with d3
        if item == wine_ITEM:
            ">You found a bottle of wine from professor dumbledore's personal stash..."
        elif item == firewhisky_ITEM:
            ">You found a bottle of firewhisky from professor dumbledore's personal stash..."
        else:
            ">You found [item.name]..."
            ">[item.description]"

    hide screen gift
    with d3

    return
