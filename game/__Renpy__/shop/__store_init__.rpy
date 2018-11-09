label store_init:

    #Update 1.3
    if not hasattr(renpy.store,'gift_order') or reset_persistants:

        #Shop
        $ order_placed = False #TRUE when and order has been placed on an item.
        $ days_in_delivery = 0 # +1 day, every day since the orer has been made (when order_placed = True).
        $ days_in_delivery2 = 0 # +1 day, every day since the orer has been made (when order_placed = True).
        $ package_is_here = False # Turns true when days_in_delivery >= 5. Package is displayed.

        $ cs_existing_stock = [False,False,False,False,False]

        $ gift_order = None
        $ order_quantity = 0
        $ tentacle_owned = False
        $ tent_scroll = False

    if not hasattr(renpy.store,'clothes_store_intro_done') or reset_persistants:
        $ clothes_store_intro_done = False
        $ outfit_order_placed = False
        $ outfit_ready = False
        $ outfit_wait_time = 0
        $ outfit_order = None


        $ cs_stock_inventory = []
        $ glasses = False
        $ gave_tinyminiskirt = False
        $ cs_accessories = [False,False,False]
        $ cs_existing_stock = [False,False,False,False,False]
        $ cs_existing_stock_gifted = []

    #Update 1.33
    if not hasattr(renpy.store,'cs_gui_OBJ') or reset_persistants: #important!
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
