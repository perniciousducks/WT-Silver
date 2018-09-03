

label update_persistants:

    if not hasattr(renpy.store,'update_1_33'): # Reset/update old vars for a specific update here! To make it compatible with older saves/prevent crashes!
        $ update_1_33 = "2018-Aug-21"

        $ reset_her_clothing = True
        call her_init
        call her_clothing_init #Defines newly added variables. Resets variables after creating a new game.

        $ wr_outfits = []
        $ wr_costumes = []
        $ wr_dresses = []

        python:
            for i in hermione_outfits_list:
                i.unlocked = False
                i.unlockable = False

        if reward_her_red_lipstick: #Old lipstick from event.
            $ pink_lipstick_OBJ.unlocked = True #Unlocks pink lipstick.

    if not hasattr(renpy.store,'update_1_33b'): # Reset/update old vars for a specific update here! To make it compatible with older saves/prevent crashes!
        $ update_1_33b = "2018-Sep-03"

        $ reset_cho_clothing = True
        call cho_init

        if cho_met:
            $ cho_unlocked = True
        if hanging_with_snape:
            $ snape_unlocked = True
        if summoning_hermione_unlocked:
            $ hermione_unlocked = True
        if buying_favors_from_hermione_unlocked:
            $ hermione_favors = True

    return



init python:
    #This does nothing. Needs to stay or it will corrupt 1.33 saves :(
    class cs_gui_outfit_class(object): #ToDo remove this when cleaning up classes!!!!!!!
        name = "I fucked up..."
        signed = "Merlin"
