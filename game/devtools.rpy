init python hide:v
    if not config.developer:
        config.missing_image_callback = missing_image_func
        config.missing_label_callback = missing_label_func

init -2 python:
    rpy_version = int('%d%d%d%d' % renpy.version_tuple)
    
    if rpy_version >= 720000:
        pass
    else:
        raise Exception("Your Ren'Py launcher is outdated, the current minimal requirement is 7.2.0+\nPlease perform an update or use official game executable instead.")
        
    def missing_image_func(path):
        global systemerror
        systemerror = ["Missing image", path]
        return im.Image("blank.png")
        
    def missing_label_func(name):
        global systemerror
        systemerror = ["Missing label", name]
        return "missing_label"
        
    # If you're reading this it probably means you've got the warning message about old unusable files, since there has been hundreds of changes I cant guarantee if the game will work correctly if you decide to delete just the files listed below, make your life easier and simply delete the game and unpack it into new empty folder instead. -LoafyLemon
    def check_for_old_files():
        path = "__Renpy__/_cho_/"
        oldfiles = ["_cho_layering_.rpy", "_cho_layering_.rpyc", "_equip_labels_.rpy", "_equip_labels_.rpyc", "cho_private_favours.rpy", "cho_private_favours.rpyc", "quidditch.rpy", "quidditch.rpyc"]
        
        for item in oldfiles:
            if renpy.exists(path+item):
                return True
        return False

        
label missing_label():
    $ renpy.choice_for_skipping()
    $ err_msg1 = systemerror[0]
    $ err_msg2 = systemerror[1]
    "{color=#7a0000}System{/color}" "Uh-oh. Looks like you've encountered a bug. Don't worry, we will try to return you back to the office after displaying the error message, your save file won't be affected."
    "{color=#7a0000}System{/color}" "{color=#7a0000}Error:{/color} [err_msg1] '{color=#7a0000}[err_msg2]{/color}'\n\n\n{size=-4}You can report this bug on our {a=https://discord.gg/7PD57yt}discord{/a}.{/size}"
    if active_girl:
        $ active_girl = None
    $ systemerror = [None, None]
    jump main_room