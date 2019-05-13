init python:
    import urllib2

    def check_for_updates():
        updt_website = urllib2.Request(binascii.unhexlify("68747470733a2f2f706173746562696e2e636f6d2f7261772f424e354261647639"))
        try:
            updt_website2 = urllib2.urlopen(updt_website, timeout=5)
            version_check = updt_website2.read()
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
        
    # Work in progress
    #def update_savefile():
        #variables_global = []
        #variables = ["test1", "test2", "test3"]
        
        #for var in variables:
        #    variables_global.append("global "+var)
        
        #for i in xrange(len(variables)):
        #    try:
        #        exec(statement)
        #    except NameError:
        #        exec(statement2)
        
    #config.after_load_callbacks.append(update_savefile)