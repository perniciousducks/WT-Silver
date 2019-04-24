init python:
    import urllib2

    def check_for_updates():
        # Get the version from raw pastebin
        updt_website = urllib2.Request('https://pastebin.com/raw/BN5Badv9')
        try:
            updt_website2 = urllib2.urlopen(updt_website, timeout=5)
            version_check = updt_website2.read()
            # Compare version of the game with the online version
            return False if config.version == version_check else True
        except:
            return False
            
    update_available = check_for_updates() 
            
    # Groundwork for future save compatibility patches
    def check_save_compatibility(page, slot):
        if renpy.slot_json(page+"-"+slot) != None:
            save_version = renpy.slot_json(page+"-"+slot)['_version']
            if float(save_version) < float(config.version):
                return False
            return True
        return None