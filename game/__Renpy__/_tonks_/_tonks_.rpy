

label check_tonks_cs_inventory:

    $ tonks_cs_inventory_list = []
    if hg_cheer_g_OBJ.unlocked:
        $ tonks_cs_inventory_list.append(hg_cheer_g_sexy_OBJ)
    if hg_cheer_s_OBJ.unlocked:
        $ tonks_cs_inventory_list.append(hg_cheer_s_sexy_OBJ)
    if hg_cheer_r_OBJ.unlocked:
        $ tonks_cs_inventory_list.append(hg_cheer_r_sexy_OBJ)
    if hg_cheer_h_OBJ.unlocked:
        $ tonks_cs_inventory_list.append(hg_cheer_h_sexy_OBJ)

    if ag_lazy_OBJ.unlocked:
        $ tonks_cs_inventory_list.append(ag_lazy_short_OBJ)

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
