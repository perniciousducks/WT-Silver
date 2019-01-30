

### Quest Items ###

#Init
label quest_items_init:

    if not hasattr(renpy.store,'gen_quest_items_list'):
        $ gen_quest_items_list = []
        $ her_quest_items_list = []
        $ lun_quest_items_list = []
        $ ast_quest_items_list = []
        $ sus_quest_items_list = []
        $ cho_quest_items_list = []
        $ ton_quest_items_list = []

    return


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
            $ gen_quest_items_list.remove(sealed_scroll_ITEM)

    #Puzzle Box
    if puzzle_box_ITEM.unlocked and unlocked_7th == False:
        if puzzle_box_ITEM not in gen_quest_items_list:
            $ gen_quest_items_list.append(puzzle_box_ITEM)
            $ puzzle_box_ITEM.number = 1 #Makes it clickable in the inventory UI.
    else:
        if puzzle_box_ITEM in gen_quest_items_list:
            $ gen_quest_items_list.remove(puzzle_box_ITEM)


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
