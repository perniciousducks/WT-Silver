
define update_available = check_for_updates()

init python:
    config.after_load_callbacks.append(update_savefile)

init -1 python:
    import urllib2

    def check_for_updates():
        if persistent.lastupdatechecktime == None:
            persistent.lastupdatechecktime = __import__('time').time()

        if persistent.lastupdatechecktime+86400.0 < __import__('time').time():
            updt_website = urllib2.Request(binascii.unhexlify("68747470733a2f2f706173746562696e2e636f6d2f7261772f424e354261647639"))
            try:
                updt_website2 = urllib2.urlopen(updt_website, timeout=5)
                version_check = updt_website2.read()
                return False if float(config.version) >= float(version_check) else True
            except:
                pass
        return False

    # Groundwork for future save compatibility patches
    def check_save_compatibility(slot, page=None):
        save_version = FileJson(slot, "_version", missing=0, page=page)
        if save_version is not None:
            try:
                return float(save_version) >= compatible_version
            except ValueError: # (Old version fallback with letters)
                return False
        else:
            return True # Slot is empty

    # Save compatibility patches
    def update_savefile():
        # Check for version variable
        global save_internal_version
        try:
            if save_internal_version:
                pass
        except NameError:
            save_internal_version = 1.38

        # Apply update to old save

        if float(save_internal_version) < 1.381:

            ton_top_corset.blacklist=["bra"]
            ast_stockings_ann.blacklist=["bottom"]

            reset_variables("ll_pf_masturbate", "ll_pf_blowjob")

            for i, e in enumerate(ll_favor_list):
                if e.title == "Suck it!":
                    ll_favor_list[i] = ll_pf_blowjob
                elif e.title == "Masturbate for me!":
                    ll_favor_list[i] = ll_pf_masturbate

            save_internal_version = 1.381

        if float(save_internal_version) < 1.382:
            save_internal_version = 1.382

        if float(save_internal_version) < 1.383:
            save_internal_version = 1.383

        if float(save_internal_version) < 1.384:

            ag_se_imperio_sb.change_icon() # Fill all half hearts

            # Add neck layer to Tonks chibi
            tonks_chibi.layers_order = ["fix", "base", "bottom", "shoes", "top", "robe", "gloves", "neck"]
            tonks_chibi.layers["neck"] = None

            # Replace current/default hair on Tonks doll
            reset_variables("tonks_haircolor")
            ton_outfit_default.group[0] = ton_hair_base_new.clone()
            ton_outfit_last.group[0] = ton_hair_base_new.clone()
            tonks.equip(ton_hair_base_new)

            # Valuefix
            if renpy.store.twins_profit > 1.2:
                renpy.store.twins_profit = 1.2

            # Clothes
            reset_variables("outfit_linking", "hermione_outfits_list")
            her_tattoo3_lockhart.categories = ("legs", "tattoos")
            her_outfit_bikini1.price = 350
            her_outfit_bikini2.price = 350
            her_outfit_bunny.price = 350
            her_outfit_latex_dress.price = 350
            her_outfit_nightie.price = 350
            her_outfit_yennefer.price = 400
            her_outfit_bioshock.price = 400
            her_outfit_egypt.price = 400
            her_outfit_maid.price = 450
            her_outfit_poker.price = 450
            cho_panties_sport1.armfix = True
            cho_panties_sport1.rebuild_image()
            cho.rebuild_image()

            achievement_fix()

            save_internal_version = 1.384

        if float(save_internal_version) < 1.385:

            hermione.rebuild()
            cho.rebuild()
            astoria.rebuild()
            tonks.rebuild()

            if her_whoring < 18 and hermione.is_equipped("tattoo3") and hermione.get_equipped("tattoo3").id == "lockhart_tattoo":
                if hg_pr_flirt.is_event_complete(2, 2):
                    hermione.unequip("tattoo3")

            save_internal_version = 1.385

            renpy.block_rollback()
