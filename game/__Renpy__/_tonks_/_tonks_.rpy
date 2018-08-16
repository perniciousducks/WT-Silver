

label check_tonks_clothing_upgrades:

    $ upgradable_clothing = []
    if hg_cheer_g_OBJ.unlocked and not hg_cheer_g_sexy_OBJ.unlocked:
        $ upgradable_clothing.append(hg_cheer_g_sexy_OBJ)
    if hg_cheer_s_OBJ.unlocked and not hg_cheer_s_sexy_OBJ.unlocked:
        $ upgradable_clothing.append(hg_cheer_s_sexy_OBJ)
    if hg_cheer_r_OBJ.unlocked and not hg_cheer_r_sexy_OBJ.unlocked:
        $ upgradable_clothing.append(hg_cheer_r_sexy_OBJ)
    if hg_cheer_h_OBJ.unlocked and not hg_cheer_h_sexy_OBJ.unlocked:
        $ upgradable_clothing.append(hg_cheer_h_sexy_OBJ)

    if ag_lazy_OBJ.unlocked and not ag_lazy_short_OBJ.unlocked:
        $ upgradable_clothing.append(ag_lazy_short_OBJ)

    if upgradable_clothing != []:
        $ clothing_unlock =upgradable_clothing[ renpy.random.randint(0,len(upgradable_clothing)-1)]

    return


label set_ton_astoria_name:
    if one_of_five == 1:
        $ ton_astoria_name = "Cutie"
    if one_of_five == 2:
        $ ton_astoria_name = "Kitty"
    if one_of_five == 3:
        $ ton_astoria_name = "Princess"
    if one_of_five == 4:
        $ ton_astoria_name = "Little Girl"
    if one_of_five == 5:
        $ ton_astoria_name = "Honey"

    return


label set_tonks_action(action=""):
    hide screen tonks_main

    if action in ["",None]:
        $ ton_request_wear_coat = True
        $ ton_request_wear_top = True
        $ ton_request_wear_bra = True
        $ ton_request_wear_bottom = True
        $ ton_request_wear_panties = True
        $ ton_request_wear_stockings = True
        $ ton_request_wear_accs = True

    if action in ["strip","naked","strip_naked"]:
        $ ton_request_wear_coat = False
        $ ton_request_wear_top = False
        $ ton_request_wear_bra = False
        $ ton_request_wear_bottom = False
        $ ton_request_wear_panties = False
        $ ton_request_wear_stockings = False
        $ ton_request_wear_accs = False

    call load_tonks_cloathing_saves
    call update_tonks_body

    return


label load_tonks_cloathing_saves:

    if ton_request_wear_coat:
        $ tonks_wear_coat = True
    else:
        $ tonks_wear_coat = False
    if ton_request_wear_top:
        $ tonks_wear_top = True
    else:
        $ tonks_wear_top = False
    if ton_request_wear_bra:
        $ tonks_wear_bra = True
    else:
        $ tonks_wear_bra = False
    if ton_request_wear_bottom:
        $ tonks_wear_bottom = True
    else:
        $ tonks_wear_bottom = False
    if ton_request_wear_panties:
        $ tonks_wear_panties = True
    else:
        $ tonks_wear_panties = False
    if ton_request_wear_stockings:
        $ tonks_wear_stockings = True
    else:
        $ tonks_wear_stockings = False
    if ton_request_wear_accs:
        $ tonks_wear_accs = True
    else:
        $ tonks_wear_accs = False

    return


label update_tonks_body:

    if tonks_wear_coat:# or tonks_wear_top or tonks_wear_bra:
        $ tonks_boobs = "characters/tonks/body/base/boobs_0.png"
    else:
        if tonks_wear_top:
            $ tonks_boobs = "characters/tonks/body/base/boobs_2.png"
        else:
            $ tonks_boobs = "characters/tonks/body/base/boobs_1.png"

    return
