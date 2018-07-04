label __init_variables:
    if not hasattr(renpy.store,'clothes_intro_done'): #important!
        $ clothes_intro_done = False
    if not hasattr(renpy.store,'outfit_order_placed'): #important!
        $ outfit_order_placed = False
    if not hasattr(renpy.store,'outfit_ready'): #important!
        $ outfit_ready = False
    if not hasattr(renpy.store,'outfit_wait_time'): #important!
        $ outfit_wait_time = 0
    if not hasattr(renpy.store,'outfit_order'): #important!
        $ outfit_order = None

    $ clothes_store_order_choice = None
    $ clothes_store_selection = None

    if not hasattr(renpy.store,'cs_stock_inventory'): #important!
        $ cs_stock_inventory = []
    if not hasattr(renpy.store,'micro_skirt'): #important!
        $ micro_skirt = False
    if not hasattr(renpy.store,'glasses'): #important!
        $ glasses = False
    if not hasattr(renpy.store,'wear_shirts'): #important!
        $ wear_shirts = True
    if not hasattr(renpy.store,'wear_skirts'): #important!
        $ wear_skirts = True
    if not hasattr(renpy.store,'gave_tinyminiskirt'): #important!
        $ gave_tinyminiskirt = False
    if not hasattr(renpy.store,'cs_accessories'): #important!
        $ cs_accessories = [False,False,False]
    if not hasattr(renpy.store,'cs_existing_stock'): #important!
        $ cs_existing_stock = [False,False,False,False,False]
    if not hasattr(renpy.store,'cs_existing_stock_gifted'): #important!
        $ cs_existing_stock_gifted = []

    #Update 1.4
    if not hasattr(renpy.store,'mannequin_preview'): #important!
        $ mannequin_preview = "ball_dress_b.png"


    return
