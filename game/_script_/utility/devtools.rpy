
init python:
    if not config.developer:
        config.missing_image_callback = missing_image_func
        config.missing_label_callback = missing_label_func
    else:
        config.lint_hooks.append(lint_char_main_calls)

init -1 python:
    if renpy.version_tuple < (7,3,5,606):
        raise Exception("Your Ren'Py launcher is outdated, the current minimal requirement is 7.3.5+\nPlease perform an update and try launching the game again.")

    def missing_image_func(path):
        global systemerror
        systemerror = ["Missing image", path]
        return Null()

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

    def lint_char_main_calls():
        """
        Checks character calls that use the doll system.
        """
        renpy.execute_default_statement(False)
        char_lookup = {
            "ast_main": astoria,
            "cho_main": cho,
            "her_main": hermione,
            "ton_main": tonks
        }

        calls = [i for i in renpy.game.script.all_stmts if isinstance(i, renpy.ast.Call) and i.label in char_lookup]
        calls.sort(key=lambda i: (i.filename, i.linenumber))

        for c in calls:
            named_args = {}
            try:
                args, kwargs = c.arguments.evaluate(renpy.store.__dict__)
                node = renpy.game.script.lookup(c.label)
                named_args = node.parameters.apply(args, kwargs)
            except NameError:
                continue # Linting with undefined variables is difficult
            except Exception as e:
                print
                print "{}:{} {}".format(c.filename, c.linenumber, e)
                continue

            if named_args["face"] is not None:
                pass # Linting random face expressions is difficult

            char = char_lookup[c.label]

            # Reset face to default first, to avoid persisting errors from previous calls
            char.set_face(mouth="base", eyes="base", eyebrows="base", pupils="mid")
            char.set_face(
                mouth=named_args["mouth"],
                eyes=named_args["eyes"],
                eyebrows=named_args["eyebrows"],
                pupils=named_args["pupils"],
                cheeks=named_args["cheeks"],
                tears=named_args["tears"],
            )
            img = char.get_image()
            what = "Call to {}".format(c.label)
            renpy.lint.report_node = c
            renpy.lint.check_displayable(what, img)

    def save_whitespace(mode=0):
        """
        Saves whitespace information to whitespace file.
        mode = 0 - Whitespace_dict
        mode = 1 - file crawler
        """
        file = config.basedir+"/game/images.whitespace"
        with open(file, "w") as fp:
            if mode == 0:
                for key, value in whitespace_dict.iteritems():
                    fp.write("{}:{},{},{},{}\n".format(key, value[0], value[1], value[2], value[3]))
            elif mode == 1:
                print "This might take a while... If your game freezes, that's normal."
                time.sleep(3)
                for dp, dn, fn in system.walk(config.basedir+"/game/"):
                    for i in [f for f in fn if f.endswith(".png")]:
                        img = system.path.join(dp, i).replace("\\", "/").split("/game/")[1]
                        box = crop_whitespace(img)
                        fp.write("{}:{},{},{},{}\n".format(img, box[0], box[1], box[2], box[3]))
        return "Saved successfuly"

label missing_label():
    $ renpy.choice_for_skipping()
    $ err_msg1 = systemerror[0]
    $ err_msg2 = systemerror[1]
    "{color=#7a0000}System{/color}" "Uh-oh. Looks like you've encountered a glitch. Shit's broken yo!"
    "{color=#7a0000}System{/color}" "{color=#7a0000}Error:{/color} [err_msg1] '{color=#7a0000}[err_msg2]{/color}'"
    if active_girl:
        $ active_girl = None
    $ systemerror = [None, None]
    jump main_room
