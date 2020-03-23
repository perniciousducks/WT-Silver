

### Cupboard ###

label cupboard:
    if not cupboard_examined:
        $ cupboard_examined = True
        $ searched = True
        show screen chair_left
        call gen_chibi("stand","behind_desk","base", flip=False)
        show screen desk
        with d5
        pause.2

        call bld
        m "Hm....."
        m "A cupboard..."
        m "Maybe I should rummage through this one later..."
        jump main_room_menu

    jump rummaging


label rummaging:

    $ searched = True # Resets every day/night.
    $ rum_times += 1  # Stat counter.

    show screen chair_left
    show screen desk
    show screen cupboard_open
    call gen_chibi("rummage", 160, 110+349, flip=False) # Note: Flip is inconsistent
    with d3
    show screen bld1
    with d3

    ">You rummage through the cupboard for a while..."

    $ random_percent = renpy.random.randint(1, 100)

    # Dueling Potion.
    if day <= 3 and rum_times in [1,2]:
        $ potions += 1
        call give_reward(">You found some sort of healing potion...","interface/icons/item_potion.png")

        jump main_room_menu

    # Map and wine (Prologue Only).
    if not map_unlocked:
        if hermione_favors:
            $ map_unlocked = True
            call give_reward(">You found a map of the school grounds...\n>You can now leave the office.","interface/icons/item_scroll.png")

            jump main_room_menu
        elif wine_ITEM.number < 1:
            call rum_block(wine_ITEM)

            jump main_room_menu
        elif firewhisky_ITEM.unlocked and firewhisky_ITEM.number < 1:
            call rum_block(firewhisky_ITEM)

            jump main_room_menu

    # Dumbledore Card.
    if day >= 26 and deck_unlocked and random_percent <= 40 and not card_exist(unlocked_cards,card_dumbledore) :
        call give_reward("You have found a special card!", "images/cardgame/t1/special/dumbledore_v1.png")
        $ unlocked_cards += [card_dumbledore]

        jump main_room_menu

    ##################################################
    ### Add your cupboard unlocks above this line. ###
    ##################################################

    $ drop_list = [lollipop_ITEM, chocolate_ITEM, plush_owl_ITEM, butterbeer_ITEM, science_mag_ITEM, girls_mag_ITEM, adult_mag_ITEM, porn_mag_ITEM, krum_poster_ITEM, sexy_lingerie_ITEM, sexy_stockings_ITEM, pink_condoms_ITEM, vibrator_ITEM, anal_lube_ITEM, ballgag_and_cuffs_ITEM, anal_plugs_ITEM, testral_strapon_ITEM, broom_2000_ITEM, sexdoll_ITEM, anal_beads_ITEM, firewhisky_ITEM, wine_ITEM]

    $ _dr = max(rum_times-day, 0)*2

    #
    # Easy (with soft diminishing returns, more rubber banding. Guaranteed item drop.)
    #
    if game_difficulty == 1:
        if firewhisky_ITEM.unlocked and firewhisky_ITEM.number < 1:
            call rum_block(firewhisky_ITEM)
        elif wine_ITEM.number < 1:
            call rum_block(wine_ITEM)
        elif gold < int(170*math.log(day)) and random_percent <= 56-_dr:
            call rum_block(int(math.log(her_tier+cho_tier+ton_tier+lun_tier+day)*random_gold))
        else:
            $ _filtered_list = filter(lambda x: x.number <= 5, drop_list)
            $ _item = renpy.random.choice(_filtered_list if _filtered_list else drop_list)

            call rum_block(_item)
    #
    # Normal (with fair diminishing returns, soft rubber banding. High chance for item drop.) (Recommended)
    #
    elif game_difficulty == 2:
        if gold < int(120*math.log(day)) and random_percent <= 38-_dr:
            call rum_block(int(math.log(her_tier+cho_tier+ton_tier+lun_tier+day)*random_gold))
        else:
            $ _filtered_list = filter(lambda x: x.number <= 3, drop_list) # Filter out owned items with quantity higher than 2.
            $ _item = renpy.random.choice(_filtered_list if _filtered_list else drop_list)

            if int(120*math.log(day))/3 < _item.cost:
                $ _chance = max(6-(_item.number*5), 1)
            elif gold > _item.cost:
                $ _chance = max(65-(_item.number*15), 5)
            else:
                $ _chance = max(95-(_item.number*10), 15)

            if random_percent <= _chance-_dr:
                call rum_block(_item)
            else:
                call rum_block("nothing")
    #
    # Hardcore (with more harsh diminishing returns, no rubber banding. Chance for item drop.)
    #
    elif game_difficulty == 3:
        if gold < int(90*math.log(day)) and random_percent <= 33-_dr:
            call rum_block(int(math.log(her_tier+cho_tier+ton_tier+lun_tier+day)*random_gold))
        else:
            $ _item = renpy.random.choice(drop_list)

            if int(90*math.log(day))/3 < _item.cost:
                $ _chance = max(3-(_item.number*5), 1)
            elif gold > _item.cost:
                $ _chance = max(40-(_item.number*15), 0)
            else:
                $ _chance = max(75-(_item.number*10), 5)

            if random_percent <= _chance-_dr:
                call rum_block(_item)
            else:
                call rum_block("nothing")

    jump main_room_menu


label rum_block(item):
    if isinstance(item, int):
        $ the_gift = "interface/icons/gold.png"
        show screen gift(True)
        with d3
        $ gold += item
        ">You found [item] gold..."
    elif item == "nothing":
        ">You found nothing of value..."
    else:
        $ item.number += 1
        $ the_gift = item.get_image()
        show screen gift(True)
        with d3
        if item == wine_ITEM:
            ">You found a bottle of wine from professor Dumbledore's personal stash..."
        elif item == firewhisky_ITEM:
            ">You found a bottle of firewhisky from professor Dumbledore's personal stash..."
        else:
            ">You found [item.name]..."
            ">[item.description]"

        call tutorial("inventory")

    hide screen gift
    with d3

    return
