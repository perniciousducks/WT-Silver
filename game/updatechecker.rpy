init python:
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
            
    update_available = check_for_updates() 
            
    # Groundwork for future save compatibility patches
    def check_save_compatibility(page, slot):
        if renpy.slot_json(page+"-"+slot) != None:
            try:
                save_version = renpy.slot_json(page+"-"+slot)['_version']
                
                if float(save_version) < 1.36: #float(config.version)
                    return False
                return True
            except:
                return False
        return None
        
    # Save compatibility patches
    def update_savefile():
        # Check for version variable
        global save_internal_version
        try:
            if save_internal_version:
                pass
        except NameError:
            save_internal_version = 1.36
            
        # Compare&perform an update
        if save_internal_version < 1.361:
            global genie_cum_chibi_xpos, genie_cum_chibi_ypos
            try:
                if genie_cum_chibi_xpos:
                    pass
                if genie_cum_chibi_ypos:
                    pass
            except NameError:
                genie_cum_chibi_xpos = -45
                genie_cum_chibi_ypos = -5
                
            if "head_9" in persistent.achievements['unlocksna'][4]:
                persistent.achievements['unlocksna'][4] = "interface/icons/head/head_snape_1.png"
                persistent.achievements['bros'][4] = "interface/icons/head/head_snape_1.png"
                achievement.achievements['unlocksna'][4] = "interface/icons/head/head_snape_1.png"
                achievement.achievements['bros'][4] = "interface/icons/head/head_snape_1.png"

            save_internal_version = 1.361
            
        if save_internal_version < 1.362:
            ll_pf_sex = event_class(title = "Let's have sex!", start_label = "ll_pf_sex", start_tier = 4, events = [[["ll_pf_sex_T1_intro"],["ll_pf_sex_T1_E1"],["ll_pf_sex_T1_E2"],["ll_pf_sex_T1_E3"]]],iconset = [["heart_empty", "heart_blue"]])
            
            save_internal_version = 1.362
            
        # Temporal dev bugfix
        if persistent.achievements.get("busted") == None:
            persistent.achievements['pantiesfap'] == ["Characters", "I sneezed on them...", "Rubbed one out on Hermione's panties.", False, "characters/genie/chibis/masturbating/02.png", False]
            persistent.achievements['pantiesfapcho'] == ["Characters", "Exercise is important", "Rubbed one out on Cho's panties.", False, "characters/genie/chibis/masturbating/02.png", False]
            persistent.achievements['busted'] = ["Characters", "BUSTED!", "... a nut when got busted for busting a nut.", False, "interface/icons/head/head_hermione_2.png", False]
            persistent.achievements['herstrip'] = ["Characters", "Dance lessons", "Even elephants have more grace when they're moving, girl.. -Severus Snape", False, "interface/icons/head/head_hermione_2.png", False]
            persistent.achievements['hertits'] = ["Characters", "Boobs Lover", "*ahem* I mean.. books, yes, books lover!", False, "interface/icons/head/head_hermione_2.png", False]
            persistent.achievements['headlib'] = ["Characters", "Head Librarian", "Did she just swallow it?", False, "interface/icons/head/head_hermione_2.png", False]
            persistent.achievements['nerdgasm'] = ["Characters", "Nerdgasm", "Had a very fulfilling moment with Hermione.", False, "interface/icons/head/head_hermione_2.png", False]
        
    config.after_load_callbacks.append(update_savefile)