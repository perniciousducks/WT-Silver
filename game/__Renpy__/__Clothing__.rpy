label __init_variables:


    # outfit unlocks/purchases are the only dynamic value we care about so they have been separated into their own dict
    if not hasattr(renpy.store,'unlocked_clothing_list'):
        $ unlocked_clothing_list = []

    # Setup for 1.5
    # Since we probably have to change the outfits, all purchased outfits will get an .unlocked = True variable,
    # And those outfits will get added to the "unlocked_clothing_list",
    # with which we can unlock all outfits again in the next update if needed, so people don't have to buy and wait for outfits againself.

    python:

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


    #Todo
    #Remove everything below. Needs to stay for a crash fix, for now. (1.4)
    if not hasattr(renpy.store,'hg_clothing_saves'):
        $ hg_clothing_saves  = {}
        # this stores the state of the custom_outfit_objs for whenever .save() is called
        # b/c this is a basic dictionary it will also persist through reloads


    if not hasattr(renpy.store,'hg_clothing'):
        $ hg_clothing = custom_outfit_obj()
        # this is whats currently equipped to change to a diffrent outfit simply .load() it

    if not hasattr(renpy.store,'hg_clothing_save_01'):
        $ hg_clothing_save_01 = custom_outfit_obj()
        $ hg_clothing_save_02 = custom_outfit_obj()
        $ hg_clothing_save_03 = custom_outfit_obj()
        $ hg_clothing_save_04 = custom_outfit_obj()
        $ hg_clothing_save_05 = custom_outfit_obj()
        $ hg_clothing_save_06 = custom_outfit_obj()
        $ hg_clothing_save_07 = custom_outfit_obj()
        $ hg_clothing_save_08 = custom_outfit_obj()
        $ hg_clothing_save_09 = custom_outfit_obj()
        $ hg_clothing_save_10 = custom_outfit_obj()


    python:
        # this is an example of a devloper assigned static save
        hg_clothing_saves['example_static_save'] = {
            'name'          :'name_of_outfit/save',
            'top'           :'example_value_for_top',
            'top_color'     :'example_color',
            'panties'       :'example_value_for_panties',
            'wear_panties'  : False
        }

        # to load this save we would simply call hg_clothing.load('example_static_save')

    return



init -2 python:

    class custom_outfit_obj(object):
        # id = 0 #ID 0 is the default. Outfits you saved (with ID 1,2,...) override 0 when equipped.
        name = "defult" # replace id with unique name that could be taken as input, eaiser to track
        mannequin_layers = []

        hair = "A"
        hair_color = "base"

        top = "top_1" #the name of the item.
        top_color = "base" #which color folder the item is in.
        wear_top = True #if the item is currently worn.
        always_wear_top = True #if the item is worn on resetting the outfit.

        onepiece = "blank"
        onepiece_color = "base"
        wear_onepiece = False
        always_wear_onepiece = False

        bottom = "skirt_1"
        bottom_color = "base"
        wear_bottom = True
        always_wear_bottom = True

        bra = "bra_base"
        bra_color = "base"
        wear_bra = True
        always_wear_bra = True

        panties = "panties_base"
        panties_color = "base"
        wear_panties = True
        always_wear_panties = True

        graterbelt = "blank"
        garterbelt_color = "base"
        wear_garterbelt = False
        always_wear_garterbelt = False

        neckwear = "blank"
        neckwear_color = "base"
        wear_neckwear = False
        always_wear_neckwear = False

        gloves = "blank"
        gloves_color = "base"
        wear_gloves  = False
        always_wear_gloves  = False

        stockings = "blank"
        stockings_color = "base"
        wear_stockings  = False
        always_wear_stockings  = False

        robe = "robe_1"
        robe_color = "base"
        wear_robe = False
        always_wear_robe = False

        hat = "blank"
        hat_color = "base"
        wear_hat = False
        always_wear_hat = False

        glasses = "blank"
        glasses_color = "base"
        wear_glasses = False
        always_wear_glasses = False

        ears = "blank"
        wear_ears = True
        always_wear_ears = True

        makeup_lipstick = "nude"
        makeup_list = []
        wear_makeup = False
        always_wear_makeup = False

        accs = []
        wear_accs = False
        always_wear_accs = False

        buttplug = "blank"
        buttplug_color = "base"
        wear_buttplug  = False
        always_wear_buttplug  = False

        piercings_ears = "blank"
        piercings_ears_color = "base"
        piercings_nipples = "blank"
        piercings_nipples_color = "base"
        piercings_belly = "blank"
        piercings_belly_color = "base"
        piercings_genitals = "blank"
        piercings_genitals_color = "base"
        wear_piercings = False
        always_wear_piercings = False

        tattoos_forehead = "blank"
        tattoos_forehead_color = "base"
        tattoos_arm_left = "blank"
        tattoos_arm_left_color = "base"
        tattoos_arm_right = "blank"
        tattoos_arm_right_color = "base"
        tattoos_breasts = "blank"
        tattoos_breasts_color = "base"
        tattoos_waist = "blank"
        tattoos_waist_color = "base"
        tattoos_abdomen = "blank"
        tattoos_abdomen_color = "base"
        tattoos_leg_left = "blank"
        tattoos_leg_left_color = "base"
        tattoos_leg_right = "blank"
        tattoos_leg_right_color = "base"
        wear_tattoos = False
        always_wear_tattoos = False

        transparency = 1


        # saves and loads the state of this object to the dictionary 'hg_clothing_saves'

        def save(self, name):
            global hg_clothing_saves
            hg_clothing_saves[name] = self.__dict__
        def load(self, name):
            global hg_clothing_saves
            self.__dict__.update( hg_clothing_saves[name] )
