init python hide:
    config.load_failed_label = "load_failed"
    config.after_load_callbacks.append(scan_and_fix_stack)
    if not config.developer:
        config.missing_image_callback = missing_image_func
        config.missing_label_callback = missing_label_func

init -2 python:
    rpy_version = int('%d%d%d%d' % renpy.version_tuple)
    
    if rpy_version >= 730000:
        pass
    else:
        raise Exception("Your Ren'Py launcher is outdated, the current minimal requirement is 7.3.0+\nPlease perform an update or use official game executable instead.")
        
    def missing_image_func(path):
        global systemerror
        systemerror = ["Missing image", path]
        return im.Image("blank.png")
        
    def missing_label_func(name):
        global systemerror
        systemerror = ["Missing label", name]
        return "missing_label"
        
    # If you're reading this it probably means you've got the warning message about old unusable files, since there has been hundreds of changes I cant guarantee if the game will work correctly if you decide to delete just the files/labels listed below, make your life easier and simply delete the game and unpack it into new empty folder instead. -LoafyLemon
    def check_for_old_files():
        path = "__Renpy__/_cho_/"
        oldfiles = ["cho_wear_buttplug", "update_cho_uniform", "set_cho_hair", "set_cho_hat", "set_cho_top", "set_cho_bottom", "set_cho_bra", "set_cho_onepiece", "set_cho_panties", "set_cho_garterbelt", "set_cho_neckwear", "set_cho_body_accessory", "set_cho_gloves", "set_cho_stockings", "set_cho_robe", "set_cho_gag", "set_cho_piercing", "set_cho_outfit", "set_cho_transparency", "update_cho_quidditch_outfit", "load_cho_clothing_saves", "cho_favor_1", "cho_favor_1_1", "cho_favor_1_2", "cho_favor_1_3", "jerk_off_to_cho", "cho_quidd_intro", "cho_quidd_1_1", "cho_quidd_1_2", "cho_quidd_1_3", "cho_quidd_2_1", "cho_quidd_2_2", "cho_quidd_2_3", "new_custom_request", "custom_request_wrapup", "shaming_intro", "shaming_event", "shaming", "shaming_night", "rcement", "heritic_intro", "heritic_event", "heretic", "heretic_night"]
        
        for item in oldfiles:
            if renpy.has_label(item):
                return True
        return False
        
    def TBA_message(msg="Currently unavailable, check in later versions of the game."):
        renpy.show_screen("blktone5")
        renpy.with_statement(d3)
        renpy.say(sil, msg)
        renpy.hide_screen("blktone5")
        renpy.with_statement(d3)
        return

    def reset_variables(*args):
        """Resets the given variables to their default values."""
        # Refer to renpy.ast.Default.set_default for implementation details
        defaults_set = renpy.store._defaults_set
        changed_set = renpy.store.__dict__.ever_been_changed
        for arg in args:
            if arg in defaults_set:
                if arg in changed_set:
                    defaults_set.remove(arg)
                    changed_set.remove(arg)
            elif config.developer:
                raise Exception("The variable `{}` was not previously set with a default value.".format(arg))
        renpy.execute_default_statement(False)

    def scan_and_fix_stack():
        # Scan the call stack for missing labels
        # If a label is missing, assume a fatal error will occur eventually
        # Then wipe the stack and jump to config.load_failed_label to prevent the error
        context = renpy.game.context()
        script = renpy.game.script
        for i in xrange(-1, -len(context.return_stack)-1, -1):
            node = None

            if script.has_label(context.return_stack[i]):
                node = script.lookup(context.return_stack[i])
            elif script.has_label(context.call_location_stack[i]):
                node = script.lookup(context.call_location_stack[i]).next

            if node is None:
                # Clean up similar to RollbackLog.load_failed
                while renpy.exports.call_stack_depth():
                    renpy.exports.pop_call()
                
                renpy.game.contexts[0].force_checkpoint = True
                renpy.game.contexts[0].goto_label(renpy.config.load_failed_label)

                raise renpy.game.RestartTopContext()
                return
        
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

label load_failed:
    $ renpy.block_rollback() # Prevent rollback to broken past
    $ active_girl = None
    show screen blktone5
    "Something went wrong while loading your save, but all is not lost! You will be back in the office with the same progress as when you saved the game. However, you can't rollback to a time before that moment."
    hide screen blktone5
    with d5
    $ renpy.block_rollback() # Prevent rollback to this message
    jump main_room
