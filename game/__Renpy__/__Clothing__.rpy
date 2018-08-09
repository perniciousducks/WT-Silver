label __init_variables:


    #if not hasattr(renpy.store,'ag_lazy_town_OBJ'):
    #    $ hg_muggle_rainy_OBJ = clothing_unlocks()

    # Setup for 1.5
    # Since we probably have to change the outfits, all purchased outfits will get an .unlocked = True variable,
    # And those outfits will get added to the "unlocked_clothing_list",
    # with which we can unlock all outfits again in the next update if needed, so people don't have to buy and wait for outfits againself.

    python:
        for i in hermione_outfits_list:
            if i.purchased: #.purchased is not in use anymore. Replaced with .unlocked
                i.unlocked = True

        #Outfits
        for i in hermione_outfits_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)
        for i in astoria_outfits_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)

        #Sets
        for i in hermione_clothing_sets_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)
        for i in astoria_clothing_sets_list:
            if i.unlocked and i not in unlocked_clothing_list:
                unlocked_clothing_list.append(i)

        #Items



    return

init -2 python:

    # outfit unlocks/purchases are the only dynamic value we care about so they have been separated into their own dict
    if not hasattr(renpy.store,'unlocked_clothing_list'):
        unlocked_clothing_list = []
