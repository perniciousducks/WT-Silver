

label update_persistants:

    if not hasattr(renpy.store,'reset_1_4'): # Reset/update old vars for a specific update here! To make it compatible with older saves/prevent crashes!
        $ reset_1_4 = False

        $ reset_her_clothing = True
        call her_init #Defines newly added variables. Resets variables after creating a new game.
        call her_clothing_init #Defines newly added variables. Resets variables after creating a new game.
        
        $ wr_outfits = []
        $ wr_costumes = []
        $ wr_dresses = []

        $ hg_maid_OBJ.unlocked = False
        $ hg_maid_OBJ.unlockable = False
        $ hg_heartDancer_OBJ.unlocked = False
        $ hg_heartDancer_OBJ.unlockable = False
        $ hg_pirate_OBJ.unlocked = False
        $ hg_pirate_OBJ.unlockable = False
        $ hg_powerGirl_OBJ.unlocked = False
        $ hg_powerGirl_OBJ.unlockable = False
        $ hg_msMarvel_OBJ.unlocked = False
        $ hg_msMarvel_OBJ.unlockable = False
        $ hg_harleyQuinn_OBJ.unlocked = False
        $ hg_harleyQuinn_OBJ.unlockable = False
        $ hg_ballDress_OBJ.unlocked = False
        $ hg_ballDress_OBJ.unlockable = False
        $ hg_christmas_OBJ.unlocked = False
        $ hg_christmas_OBJ.unlockable = False
        $ hg_laraCroft_OBJ.unlocked = False
        $ hg_laraCroft_OBJ.unlockable = False
        $ hg_tifa_OBJ.unlocked = False
        $ hg_tifa_OBJ.unlockable = False
        $ hg_present_OBJ.unlocked = False
        $ hg_present_OBJ.unlockable = False
        $ hg_japan_OBJ.unlocked = False
        $ hg_japan_OBJ.unlockable = False
        $ hg_witch_OBJ.unlocked = False
        $ hg_witch_OBJ.unlockable = False
        $ hg_bio_OBJ.unlocked = False
        $ hg_bio_OBJ.unlockable = False
        $ hg_yenn_OBJ.unlocked = False
        $ hg_yenn_OBJ.unlockable = False

        if reward_her_red_lipstick: #Old lipstick from event.
            $ pink_lipstick_OBJ.unlocked = True #Unlocks pink lipstick.

    return
