init python:
    import urllib2

    def check_for_updates():
        # Get the version from raw pastebin
        updt_website = urllib2.Request('https://pastebin.com/raw/VvEdS3Kx')
        try:
            updt_website2 = urllib2.urlopen(updt_website)
            version_check = updt_website2.read()
            # Compare version of the game with the online version
            return False if config.version == version_check else True
        except:
            return False
            
    update_available = check_for_updates() 