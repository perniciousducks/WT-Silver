init python:
    # Temporal function
    # TODO: Create a chibi class instead.
    def update_chibi_image(name):
        if name == "cho":
            imagepath = "characters/cho/chibis/"
            animation = "_"+cho_chibi_animation if cho_chibi_animation else ""
            status = "_"+cho_chibi_status if cho_chibi_status else ""
            global cho_chibi_fix, cho_chibi_gloves, cho_chibi_top, cho_chibi_bottom, cho_chibi_robe, cho_chibi_shoes, cho_chibi_walk_shoes, cho_chibi_stand, cho_chibi_walk
            cho_chibi_fix, cho_chibi_gloves, cho_chibi_top, cho_chibi_bottom, cho_chibi_robe, cho_chibi_shoes, cho_chibi_walk_shoes, cho_chibi_stand, cho_chibi_walk, cho_chibi_shoes = "blank", "blank", "blank", "blank", "blank", "blank", "blank", "ch_cho blink", "ch_cho walk", "ch_cho walk_shoes"

            if cho_chibi_animation == "fly":
                cho_chibi_stand = "ch_cho fly_idle"
                cho_chibi_walk = "ch_cho fly"

            if cho_class.get_worn("top"):
                if cho_class.get_cloth("top").id == "top_sweater_1":
                    cho_chibi_top = imagepath+"cc_sweater"+animation+status+".png" if animation else imagepath+"cc_sweater.png"
                else:
                    cho_chibi_top = imagepath+"cc_top"+animation+status+".png" if animation else imagepath+"cc_top.png"

            if cho_class.get_worn("bottom"):
                if cho_class.get_cloth("bottom").id in ("pants_long_2", "pants_short_4"):
                    if not status == "_move":
                        cho_chibi_bottom = imagepath+"cc_trousers"+animation+".png"
                    else:
                        if animation:
                            cho_chibi_bottom = imagepath+"cc_trousers"+animation+status+".png"
                        else:
                            if status == "_move":
                                cho_chibi_bottom = "ch_cho trousers"
                            else:
                                cho_chibi_bottom = imagepath+"cc_trousers.png"
                else:
                    cho_chibi_bottom = imagepath+"cc_skirt"+animation+status+".png" if animation else imagepath+"cc_skirt.png"

            if cho_class.get_worn("gloves"):
                if cho_class.get_cloth("gloves").id == "quidditch":
                    cho_chibi_gloves = imagepath+"cc_gloves"+animation+status+".png" if animation else imagepath+"cc_gloves.png"

            if cho_class.get_worn("robe"):
                if cho_class.get_cloth("robe").id == "robe_quidditch_1":
                    cho_chibi_robe = imagepath+"cc_quid_robe"+animation+status+".png" if animation else imagepath+"cc_quid_robe.png"
                    if not animation:
                        cho_chibi_fix = imagepath+"cc_quid_robe_fix.png"
                else:
                    cho_chibi_robe = imagepath+"cc_robe"+animation+status+".png" if animation else imagepath+"cc_robe.png"

            if cho_class.get_worn("bottom") or cho_class.get_worn("stockings"):
                if cho_class.get_worn("gloves") and cho_class.get_cloth("gloves").id == "quidditch":
                    if not animation and status == "_move":
                        cho_chibi_shoes = "ch_cho walk_quid_shoes"
                    else:
                        cho_chibi_shoes = imagepath+"cc_quid_shoes"+animation+status+".png"
                else:
                    if not status == "_move":
                        cho_chibi_shoes = imagepath+"cc_shoes"+animation+".png"
                    else:
                        if animation:
                            cho_chibi_shoes = imagepath+"cc_shoes"+animation+".png"
            else:
                cho_chibi_shoes = "blank"
        elif name == "tonks":
            imagepath = "characters/tonks/chibis/"
            animation = "_"+ton_chibi_animation if ton_chibi_animation else ""
            status = "_"+ton_chibi_status if ton_chibi_status else ""
            global ton_chibi_fix, ton_chibi_gloves, ton_chibi_top, ton_chibi_bottom, ton_chibi_robe, ton_chibi_shoes, ton_chibi_walk_shoes, ton_chibi_stand, ton_chibi_walk
            ton_chibi_fix, ton_chibi_gloves, ton_chibi_top, ton_chibi_bottom, ton_chibi_robe, ton_chibi_shoes, ton_chibi_walk_shoes, ton_chibi_stand, ton_chibi_walk, ton_chibi_shoes = "blank", "blank", "blank", "blank", "blank", "blank", "blank", "ch_ton blink", "ch_ton walk", "ch_ton walk_shoes"

            if tonks_class.get_worn("top"):
                ton_chibi_top = imagepath+"nt_top"+animation+status+".png" if animation else imagepath+"nt_top.png"

            if tonks_class.get_worn("bottom"):
                if tonks_class.get_cloth("bottom").subcat == "trousers":
                    if not status == "_move":
                        ton_chibi_bottom = imagepath+"nt_trousers"+animation+".png"
                    else:
                        if animation:
                            ton_chibi_bottom = imagepath+"nt_trousers"+animation+status+".png"
                        else:
                            if status == "_move":
                                ton_chibi_bottom = "ch_ton trousers"
                            else:
                                ton_chibi_bottom = imagepath+"nt_trousers.png"
                else:
                    ton_chibi_bottom = imagepath+"nt_skirt"+animation+status+".png" if animation else imagepath+"nt_skirt.png"

            if tonks_class.get_worn("gloves"):
                ton_chibi_gloves = imagepath+"nt_gloves"+animation+status+".png" if animation else imagepath+"nt_gloves.png"

            if tonks_class.get_worn("robe"):
                ton_chibi_robe = imagepath+"nt_robe"+animation+status+".png" if animation else imagepath+"nt_robe.png"

            if tonks_class.get_worn("bottom") or tonks_class.get_worn("stockings"):
                if not status == "_move":
                    ton_chibi_shoes = imagepath+"nt_shoes"+animation+".png"
                else:
                    if animation:
                        ton_chibi_shoes = imagepath+"nt_shoes"+animation+".png"
            else:
                ton_chibi_shoes = "blank"
        elif name == "astoria":
            imagepath = "characters/astoria/chibis/"
            animation = "/"+ast_chibi_animation+"/" if ast_chibi_animation else ""
            status = "_"+ast_chibi_status if ast_chibi_status else ""
            global ast_chibi_gloves, ast_chibi_top, ast_chibi_bottom, ast_chibi_robe, ast_chibi_shoes, ast_chibi_walk_shoes, ast_chibi_stand, ast_chibi_walk
            ast_chibi_gloves, ast_chibi_top, ast_chibi_bottom, ast_chibi_robe, ast_chibi_shoes, ast_chibi_walk_shoes, ast_chibi_stand, ast_chibi_walk, ast_chibi_shoes = "blank", "blank", "blank", "blank", "blank", "blank", "ch_ast blink", "ch_ast walk", "ch_ast walk_shoes"
            
            if ast_chibi_animation == "wand":
                ast_chibi_stand = "ch_ast wand_stand"
                #ast_chibi_walk = "ch_ast walk"
            elif ast_chibi_animation == "wand_casting":
                ast_chibi_stand = "ch_ast wand_casting"
                #ast_chibi_walk = "ch_ast walk"
            elif ast_chibi_animation == "wand_imperio":
                ast_chibi_stand = "ch_ast wand_imperio"
                #ast_chibi_walk = "ch_ast walk"

            if astoria_class.get_worn("top"):
                ast_chibi_top = imagepath+animation+"ag_top"+status+".png" if animation else imagepath+"ag_top.png"

            if astoria_class.get_worn("bottom") or astoria_class.get_cloth("top").id == astoria_cloth_topann.id: # # #
                ast_chibi_bottom = imagepath+animation+"ag_skirt"+status+".png" if animation else imagepath+"ag_skirt.png"

            if astoria_class.get_worn("robe") and not animation:
                ast_chibi_robe = imagepath+animation+"ag_robe"+status+".png" if animation else imagepath+"ag_robe.png"

            if astoria_class.get_worn("bottom") or astoria_class.get_worn("stockings"):
                if not status == "_move":
                    if ast_chibi_animation == "wand_imperio":
                        ast_chibi_shoes = "ch_ast imperio_shoes"
                    else:
                        ast_chibi_shoes = imagepath+animation+"ag_shoes.png"
                else:
                    if animation:
                        if ast_chibi_animation == "wand_imperio":
                            ast_chibi_shoes = "ch_ast imperio_shoes"
                        else:
                            ast_chibi_shoes = imagepath+animation+"ag_shoes.png"
            else:
                ast_chibi_shoes = "blank"
        return