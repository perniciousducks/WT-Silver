
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
            return float(save_version) >= compatible_version # float(config.version)
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
            save_internal_version = 1.384

            ag_se_imperio_sb.change_icon() # Fill all half hearts
