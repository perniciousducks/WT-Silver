
define update_available = check_for_updates()

init python:
    config.after_load_callbacks.append(update_savefile)

init -1 python:
    import urllib2

    def check_for_updates():
        return False

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
        return True

        save_version = FileJson(slot, "_version", missing=0, page=page)
        if save_version is not None:
            return float(save_version) >= compatible_version # float(config.version)
        else:
            return True # Slot is empty

    # Save compatibility patches
    def update_savefile():
        return

        # Check for version variable
        global save_internal_version
        try:
            if save_internal_version:
                pass
        except NameError:
            save_internal_version = 1.37

        # Compare&perform an update

        # Achievements update
        if persistent.achievements.get("busted") == None: # 1.37
            persistent.achievements['pantiesfap'] == ["Characters", "I sneezed on them...", "Rubbed one out on Hermione's panties.", False, "characters/genie/chibis/jerk_off/02.png", False]
            persistent.achievements['pantiesfapcho'] == ["Characters", "Exercise is important", "Rubbed one out on Cho's panties.", False, "characters/genie/chibis/jerk_off/02.png", False]
            persistent.achievements['busted'] = ["Characters", "BUSTED!", "... a nut when got busted for busting a nut.", False, "interface/icons/head/head_hermione_2.png", False]
            persistent.achievements['herstrip'] = ["Characters", "Dance lessons", "Even elephants have more grace when they're moving, girl.. -Severus Snape", False, "interface/icons/head/head_hermione_2.png", False]
            persistent.achievements['hertits'] = ["Characters", "Boobs Lover", "*ahem* I mean.. books, yes, books lover!", False, "interface/icons/head/head_hermione_2.png", False]
            persistent.achievements['headlib'] = ["Characters", "Head Librarian", "Did she just swallow it?", False, "interface/icons/head/head_hermione_2.png", False]
            persistent.achievements['nerdgasm'] = ["Characters", "Nerdgasm", "Had a very fulfilling moment with Hermione.", False, "interface/icons/head/head_hermione_2.png", False]

        if float(save_internal_version) < 1.371:
            owl_OBJ.idle_image = "owl_letter"
            tonks_cloth_garterbase = tonks_cloth_stockingsbase

            achievement_fix()

            save_internal_version = 1.371

        if float(save_internal_version) < 1.372:
            global ton_mood
            ton_mood = 0

            save_internal_version = 1.372

        if float(save_internal_version) < 1.373:
            save_internal_version = 1.373

        if float(save_internal_version) < 1.374:
            reset_variables("potion_lib")

            if fireplace_xmas_ITEM not in misc_deco_list:
                misc_deco_list.append(fireplace_xmas_ITEM)

            if phoenix_xmas_ITEM not in misc_deco_list:
                misc_deco_list.append(phoenix_xmas_ITEM)

            if owl_xmas_ITEM not in misc_hat_list:
                misc_hat_list.append(owl_xmas_ITEM)

            save_internal_version = 1.374

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
