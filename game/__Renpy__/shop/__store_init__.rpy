label store_init:

    #Update 1.3
    if not hasattr(renpy.store,'clothes_intro_done') or reset_persistants:
        $ clothes_intro_done = False
        $ outfit_order_placed = False
        $ outfit_ready = False
        $ outfit_wait_time = 0
        $ outfit_order = None


        $ cs_stock_inventory = []
        $ micro_skirt = False
        $ glasses = False
        $ wear_shirts = True
        $ wear_skirts = True
        $ gave_tinyminiskirt = False
        $ cs_accessories = [False,False,False]
        $ cs_existing_stock = [False,False,False,False,False]
        $ cs_existing_stock_gifted = []

    #Update 1.4
    if not hasattr(renpy.store,'cs_show_misc') or reset_persistants: #important!
        $ mannequin_preview = "hg_mannequin.png"
        $ cs_inventory_list = []
        $ clothes_store_category = ""

        $ clothes_store_order_choice = None
        $ clothes_store_selection = None

        $ cs_show_clothing = True
        $ cs_show_accs = True
        $ cs_show_dyes = True
        $ cs_show_misc = True

    return
