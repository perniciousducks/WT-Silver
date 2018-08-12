

label update_persistants:

    if not hasattr(renpy.store,'reset_1_4'): # Reset/update vars for this specific update here!
        $ reset_1_4 = False
        $ reset_her_clothing = True
        $ wr_outfits = []
        $ wr_costumes = []
        $ wr_dresses = []

        python:
            for i in cs_existing_stock:
                gold += 200

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

    return
