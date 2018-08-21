

label update_persistants:

    if not hasattr(renpy.store,'update_1_33'): # Reset/update old vars for a specific update here! To make it compatible with older saves/prevent crashes!
        $ update_1_33 = False

        $ reset_her_clothing = True
        call her_init #Defines newly added variables. Resets variables after creating a new game.
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

    return
