# Quest Items
default gen_quest_items_list = []
default her_quest_items_list = []
default lun_quest_items_list = []
default ast_quest_items_list = []
default sus_quest_items_list = []
default cho_quest_items_list = []
default ton_quest_items_list = []

#Update lists
label update_quest_items:

    ### Genie ###

    #Tentacle Scroll
    if sealed_scroll_ITEM.unlocked and not tentacle_owned:
        if sealed_scroll_ITEM not in gen_quest_items_list:
            $ gen_quest_items_list.append(sealed_scroll_ITEM)
            $ sealed_scroll_ITEM.number = 1 #Makes it clickable in the inventory UI.
    else:
        if sealed_scroll_ITEM in gen_quest_items_list:
            pass # Don't remove the item, the player may think it can no longer be used
            #$ gen_quest_items_list.remove(sealed_scroll_ITEM)

    #Puzzle Box
    if puzzle_box_ITEM.unlocked and unlocked_7th == False:
        if puzzle_box_ITEM not in gen_quest_items_list:
            $ gen_quest_items_list.append(puzzle_box_ITEM)
            $ puzzle_box_ITEM.number = 1 #Makes it clickable in the inventory UI.
    else:
        if puzzle_box_ITEM in gen_quest_items_list:
            $ gen_quest_items_list.remove(puzzle_box_ITEM)
            
    # Lootbox
    if lootbox_quest_ITEM.number > 0:
        if lootbox_quest_ITEM not in gen_quest_items_list:
            $ gen_quest_items_list.append(lootbox_quest_ITEM)
    else:
        if lootbox_quest_ITEM in gen_quest_items_list:
            $ gen_quest_items_list.remove(lootbox_quest_ITEM)

    ### Hermione ###
    if tentacle_owned:
        if sealed_scroll_ITEM not in her_quest_items_list:
            $ her_quest_items_list.append(sealed_scroll_ITEM)
            $ sealed_scroll_ITEM.number = 1 #Makes it clickable in the gift UI.
    else:
        if sealed_scroll_ITEM in her_quest_items_list:
            $ her_quest_items_list.remove(sealed_scroll_ITEM)

    if collar == 0 and her_whoring >= 24:
        if collar_quest_ITEM not in her_quest_items_list:
            $ her_quest_items_list.append(collar_quest_ITEM)
            $ collar_quest_ITEM.number = 1 #Makes it clickable in the gift UI.
    else:
        if collar_quest_ITEM in her_quest_items_list:
            $ her_quest_items_list.remove(collar_quest_ITEM)

    return

label examine_sealed_scroll:
    if tentacle_owned:
        m "I should use this on [hermione_name]."
    else:
        m "It's missing the key ingredient."
    jump main_room
