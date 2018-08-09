

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

    return
