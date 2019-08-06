

# Hermione Screens.

screen hermione_main():
    tag hermione_main

    #Behind body
    if hermione_wear_buttplug:
        add hermione_buttplug xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    if hermione_wear_ears:
        if h_ears == "cat_ears":
            add "characters/hermione/clothes/ears/"+str(h_ears)+"_tail_"+str(h_hair_color)+".png" xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)


    ### BODY LAYERS ###

    #Body & Legs
    add hermione_base xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio) #Add the base body
    add hermione_legs xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Hair
    if hermione_wear_mask:
        add hermione_mask xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    else:
        add hermione_hair_base xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Right Arm
    add hermione_right_arm xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Breasts
    add hermione_breasts xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Left Arm
    add hermione_left_arm xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Pubic Hair
    add hermione_pubic_hair xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Face
    add hermione_cheeks xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    add hermione_eyes xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    #add hermione_eyebrows xpos hermione_xpos ypos hermione_ypos zoom (1.0/hermione_scaleratio)
    add hermione_tears xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    if hermione_wear_gag:
        add hermione_gag xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    else:
        add hermione_mouth xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Tattoos
    if hermione_wear_tattoos:
        use hermione_tattoos

    #Body Fluids
    if hermione_dribble:
        add "characters/hermione/body/legs/dripping.png" xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    if hermione_squirt:
        add "characters/hermione/body/legs/squirting.png" xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Penis
    if hermione_futa and not hermione_wear_bottom and not hermione_wear_panties:
        add "characters/hermione/body/legs/dick.png" xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Piercings
    if hermione_wear_piercings:
        add hermione_ear_piercing xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
        add hermione_nipple_piercing xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
        add hermione_belly_piercing xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
        add hermione_genital_piercing xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    ### CLOTHING LAYERS ###

    #Uniform
    if not hermione_wear_outfit:
        use hermione_uniform

    #Costume
    if hermione_wear_outfit:
        if hermione_wear_top:
            use hermione_outfit
        else:
            use hermione_uniform

    ### ACCESORIES LAYERS ###

    #Glasses
    if hermione_wear_glasses:
        add hermione_glasses xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Hair Overlay
    if hermione_wear_mask == False:
        add hermione_hair_top xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Hat
    if hermione_wear_hat:
        add hermione_hat xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Ears
    if hermione_wear_ears:
        if h_ears == "elf_ears" and h_hair_style == "curly": #Doesn't get added to normal hair
            pass
        else:
            add hermione_ears xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Makeup
    if hermione_wear_makeup:
        use hermione_makeup


    ### SPERM LAYERS ###

    if uni_sperm:
        add u_sperm xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    elif sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "characters/hermione/face/auto_02.png" xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    elif aftersperm: #Shows cum stains on Hermione's uniform.
        add "characters/hermione/face/auto_03.png" xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)


    ### EMOTES ###
    add hermione_emote xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip #zoom (1.0/hermione_scaleratio)


    zorder hermione_zorder



### HERMIONE UNIFORM ###

screen hermione_uniform():
    tag hermione_main

    #Panties
    if hermione_wear_panties:
        add hermione_panties xpos hermione_xpos ypos hermione_ypos alpha her_panties_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)
        add hermione_panties_overlay xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Garterbelt
    if hermione_wear_garterbelt:
        add hermione_garterbelt xpos hermione_xpos ypos hermione_ypos alpha her_garter_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Stockings
    if hermione_wear_stockings:
        add hermione_stockings xpos hermione_xpos ypos hermione_ypos alpha her_stockings_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Bottom #Behind top layer.
    if hermione_wear_bottom:

        if hermione_wear_onepiece and (h_onepiece in h_onepieces_list): #Skirt or trousers gets added later
            pass
        else:
            if hermione_action == "none" or hermione_action == "hold_book": #Other actions use the layer below!
                add hermione_bottom xpos hermione_xpos ypos hermione_ypos alpha her_bottom_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)
            if hermione_action == "lift_top" and h_top in h_lift_top_list: #Bottom gets added later, after the top!
                pass
            else: #Bottom gets added now, before the top!
                add hermione_bottom xpos hermione_xpos ypos hermione_ypos alpha her_bottom_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Action/Pose Fix A (layer above skirt)
    add hermione_action_a xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Bra
    if hermione_wear_bra and hermione_use_action and hermione_action in ["lift_top"]:
        add hermione_bra xpos hermione_xpos ypos hermione_ypos alpha her_bra_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    elif hermione_wear_bra and not (h_top in h_top_remove_bra_list and hermione_wear_top):
        add hermione_bra xpos hermione_xpos ypos hermione_ypos alpha her_bra_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #One-Piece
    if hermione_wear_onepiece:
        if not h_onepiece in h_onepieces_nighties_list:
            add hermione_onepiece xpos hermione_xpos ypos hermione_ypos alpha her_onepiece_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)
        else: #Nighties
            if hermione_wear_top or hermione_wear_bottom:
                pass
            else:
                add hermione_onepiece xpos hermione_xpos ypos hermione_ypos alpha her_onepiece_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)
        if hermione_wear_bottom and h_onepiece in h_onepieces_list:
            add hermione_bottom xpos hermione_xpos ypos hermione_ypos alpha her_bottom_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Gloves
    if hermione_wear_gloves:
        add hermione_gloves xpos hermione_xpos ypos hermione_ypos alpha her_gloves_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Top
    if hermione_wear_top:
        add hermione_top xpos hermione_xpos ypos hermione_ypos alpha her_top_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Bottom #on top of top layer. #Most skirts get added here!
    if hermione_wear_bottom:
        if hermione_action != "none" and hermione_action != "hold_book" and hermione_action != "lift_top":
            if hermione_action == "lift_skirt" and (h_bottom in h_skirts_list or h_bottom in h_pants_list):
                add hermione_bottom xpos hermione_xpos ypos hermione_ypos alpha her_bottom_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)
            else:
                pass
        elif hermione_action == "lift_top":
            if h_top in h_lift_top_list:
                add hermione_bottom xpos hermione_xpos ypos hermione_ypos alpha her_bottom_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)
        else:
            pass

    #Badges & Belts
    if hermione_wear_body_accs:
        use hermione_body_accs

    #Action/Pose Fix B (layer above top)
    #add hermione_action_a xpos hermione_xpos ypos hermione_ypos zoom (1.0/hermione_scaleratio)
    add hermione_action_b xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Robe
    if hermione_wear_robe:
        add hermione_robe xpos hermione_xpos ypos hermione_ypos alpha her_robe_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    #Neckwear
    if hermione_wear_neckwear:
        add hermione_neckwear xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    zorder hermione_zorder


screen hermione_face():
    tag hermione_main

    #Face
    add hermione_cheeks xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    add hermione_eyes   xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    add hermione_mouth  xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    add hermione_tears  xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    if face_on_cg and ccg_folder == "herm_sex":
        add "images/CG/herm_sex/hair.png"

    ### EMOTES ###
    add hermione_emote xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip #zoom (1.0/hermione_scaleratio)

    zorder hermione_zorder



#Uniform Update

label update_her_uniform:

    if hermione_action != "none":
        call update_her_action

    ### Uniform ###


    #Top
    if hermione_perm_expand_breasts or hermione_expand_breasts: #Expanded Breasts
        $ hermione_top = "characters/hermione/clothes/tops/large_breasts/"+str(h_action_top)+""+str(h_top)+".png"
    else:
        $ hermione_top = "characters/hermione/clothes/tops/"+str(h_action_top)+""+str(h_top)+".png"

    #Bottom
    $ hermione_bottom = "characters/hermione/clothes/bottoms/"+str(h_action_bottom)+""+str(h_bottom)+".png"


    ### Underwear ###
    #Bra
    if hermione_perm_expand_breasts or hermione_expand_breasts: #Expanded Breasts
        $ hermione_bra = "characters/hermione/clothes/bras/large_breasts/"+str(h_bra)+".png"
    else:
        $ hermione_bra = "characters/hermione/clothes/bras/"+str(h_bra)+".png"

    #Panties
    $ hermione_panties = "characters/hermione/clothes/panties/"+str(h_panties)+".png"
    if hermione_wetpanties:
        $ hermione_panties_overlay = "characters/hermione/clothes/panties/pantystain.png"
    else:
        $ hermione_panties_overlay = "characters/hermione/clothes/panties/blank.png"

    #Onepiece
    if hermione_perm_expand_breasts or hermione_expand_breasts: #Expanded Breasts
        $ hermione_onepiece = "characters/hermione/clothes/onepieces/large_breasts/"+str(h_onepiece)+".png"
    else:
        $ hermione_onepiece = "characters/hermione/clothes/onepieces/"+str(h_onepiece)+".png"

    #Garterbelt
    $ hermione_garterbelt = "characters/hermione/clothes/garterbelts/"+str(h_garterbelt)+".png"


    ### Other Clothing ###
    $ hermione_neckwear = "characters/hermione/clothes/neckwear/"+str(h_neckwear)+".png"
    $ hermione_gloves = "characters/hermione/clothes/gloves/"+str(h_gloves)+".png"
    $ hermione_stockings = "characters/hermione/clothes/stockings/"+str(h_stockings)+".png"
    $ hermione_robe = "characters/hermione/clothes/robe/"+str(h_robe)+".png"


    #Accessories
    $ hermione_glasses = "characters/hermione/clothes/glasses/"+str(h_glasses)+".png"

    if h_ears == "cat_ears":
        if h_hair_style in ["curly","updo","bobcut"]:
            $ hermione_ears = "characters/hermione/clothes/ears/hair_"+str(h_hair_style)+"/"+str(h_ears)+"_"+str(h_hair_color)+".png"
        else:
            $ hermione_ears = "characters/hermione/clothes/ears/hair_curly/"+str(h_ears)+"_"+str(h_hair_color)+".png"
    else:
        $ hermione_ears = "characters/hermione/clothes/ears/"+str(h_ears)+".png"

    if h_hair_style in ["curly","updo","bobcut"]:
        $ hermione_hat = "characters/hermione/clothes/hats/hair_"+str(h_hair_style)+"/"+str(h_hat)+".png"
    else:
        $ hermione_hat = "characters/hermione/clothes/hats/hair_curly/"+str(h_hat)+".png"


    #Miscellaneous
    $ hermione_buttplug            = "characters/hermione/clothes/plugs/"+str(h_buttplug)+".png"
    $ hermione_mask                = "characters/hermione/clothes/hats/"+str(h_mask)+"/.png"
    $ hermione_gag                 = "characters/hermione/face/mouth/"+str(h_lipstick)+"/"+str(h_gag)+".png"

    #Piercings
    $ hermione_ear_piercing        = "characters/hermione/clothes/piercings/"+str(h_ear_piercing)+".png"
    if hermione_perm_expand_breasts or hermione_expand_breasts: #Expanded Breasts
        $ hermione_nipple_piercing = "characters/hermione/clothes/piercings/large_breasts/"+str(h_nipple_piercing)+".png"
    else:
        $ hermione_nipple_piercing = "characters/hermione/clothes/piercings/"+str(h_nipple_piercing)+".png"
    $ hermione_belly_piercing      = "characters/hermione/clothes/piercings/"+str(h_belly_piercing)+".png"
    $ hermione_genital_piercing    = "characters/hermione/clothes/piercings/"+str(h_genital_piercing)+".png"


    #Costume Action/Pose
    $ hermione_costume_action_a = "characters/hermione/clothes/custom/"+str(h_action_a)+""

    call update_chibi_uniform
    call update_her_body

    return



#Action/Pose Update

label update_her_action:

    #No Arm Change
    $ h_right_arm        = "right_1"
    $ h_left_arm         = "left_1"

    #No Folder Change    #(like "lift_top/")
    $ h_action_top       = ""
    $ h_action_bottom    = ""

    $ hermione_action_a = "characters/hermione/body/arms/left/blank.png"
    $ hermione_action_b = "characters/hermione/body/arms/left/blank.png"
    $ hermione_costume_action_a = "characters/hermione/clothes/custom/blank.png"


    if hermione_use_action:

        #Always Hide
        $ hermione_wear_onepiece     = False #Hide until art edits are made

        $ hermione_wear_neckwear     = False
        $ hermione_wear_body_accs    = False
        $ hermione_wear_gloves       = False #Hide until art edits are made.
        $ hermione_wear_robe         = False

    #Costume Action/Pose
    if hermione_use_action and hermione_wear_outfit:
        if hermione_action in hermoine_outfit_GLBL.actions:
            $ h_action_a = hermoine_outfit_GLBL.ActionImage
        else:
            $ hermione_use_action = False
            $ h_action_a = "blank.png"

        return


    #Lift Skirt
    if hermione_use_action and hermione_action == "lift_skirt":

        if hermione_wear_top and hermione_wear_bottom:
            if h_bottom in h_skirts_list:
                $ h_right_arm        = "blank"
                $ h_left_arm         = "lift_skirt"
                $ h_action_top       = "lift_skirt/"
                $ h_action_bottom    = "lift_skirt/"
            elif h_bottom in h_pants_list:
                $ h_right_arm        = "right_1"
                $ h_left_arm         = "pants_down"
                $ h_action_top       = "pants_down/"
                $ h_action_bottom    = "lift_skirt/"
            else: #Skirt 7
                pass

        elif hermione_wear_bottom:
            if h_bottom in h_skirts_list:
                $ h_right_arm        = "blank"
                $ h_left_arm         = "lift_skirt"
                $ h_action_bottom    = "lift_skirt/"
            elif h_bottom in h_pants_list:
                $ h_right_arm        = "blank"
                $ h_left_arm         = "pants_down"
                $ h_action_bottom    = "lift_skirt/"
            else: #Skirt 7
                pass

        else:
            $ h_right_arm        = "right_1"
            $ h_left_arm         = "left_1"


    #Lift Top
    if hermione_use_action and hermione_action == "lift_top":

        #$ hermione_wear_bra = False #Hide until art edits are made.

        if hermione_wear_top:
            if h_top in h_lift_top_list:
                $ h_right_arm        = "blank"
                $ h_left_arm         = "lift_top"
            elif h_top == "top_5_g":
                $ h_right_arm        = "blank"
                $ h_left_arm         = "blank"
            else:
                $ h_right_arm        = "right_1"
                $ h_left_arm         = "left_1"
            $ h_action_top       = "lift_top/"

        else:
            if her_whoring >= 12:
                $ h_right_arm        = "blank"
                if hermione_perm_expand_breasts or hermione_expand_breasts:
                    $ h_left_arm         = "lift_breasts_large"
                else:
                    $ h_left_arm         = "lift_breasts"
            else:
                $ h_right_arm        = "right_1"
                $ h_left_arm         = "left_1"
            $ h_action_top       = ""


    #Hold Book
    if hermione_use_action and hermione_action == "hold_book":

        $ hermione_wear_bra = False #Hide until art edits are made.

        $ h_right_arm        = "blank"

        if hermione_wear_top:
            $ h_left_arm         = "hold_book"
            $ h_action_top       = "hold_book/"

            if (her_top_transp or her_bra_transp or her_onepiece_transp) < 1: #Doesn't work, won't add book fix when transparent?!
                $ hermione_action_a  = "characters/hermione/body/arms/left/hold_book_fix.png" #Arm layer fix on top of skirts/pants

        else:
            if hermione_perm_expand_breasts or hermione_expand_breasts: #Expanded Breasts
                $ h_left_arm         = "hold_book_large"
            else:
                $ h_left_arm         = "hold_book"
            $ hermione_action_a  = "characters/hermione/body/arms/left/hold_book_fix.png" #Arm layer fix on top of skirts/pants


    #Lift Breasts
    if hermione_use_action and hermione_action == "lift_breasts":

        $ hermione_wear_top = False #
        $ hermione_wear_bra = False #Hide until art edits are made.

        $ h_right_arm        = "blank"

        if hermione_perm_expand_breasts or hermione_expand_breasts:
            $ h_left_arm         = "lift_breasts_large"
        else:
            $ h_left_arm         = "lift_breasts"


    #Naked Actions
    if hermione_use_action and hermione_action in ["hands_behind","covering","covering_uniform","covering_cloak","fingering","covering_top","pinch","hands_cuffed","milk_breasts"]:

        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        $ hermione_wear_bottom = False
        $ hermione_wear_garterbelt = False
        $ hermione_wear_panties = False
        if h_stockings in ["stockings_pantyhose"]:
            $ hermione_wear_stockings = False

        if hermione_action == "hands_behind":

            $ h_right_arm        = "blank"
            $ h_left_arm         = "behind"
            #$ hermione_action_a  = "characters/hermione/body/arms/left/behind.png"

        if hermione_action == "covering":

            $ h_right_arm        = "blank"
            $ h_left_arm         = "covering"
            #$ hermione_action_a  = "characters/hermione/body/arms/both/covering.png"
            #$ hermione_breasts   = "characters/hermione/body/breasts/breasts_nipfix.png"

        if hermione_action == "covering_uniform":

            $ h_right_arm        = "blank"
            $ h_left_arm         = "covering_uniform"

        if hermione_action == "covering_cloak":

            $ h_right_arm        = "blank"
            $ h_left_arm         = "covering_cloak"

        if hermione_action == "fingering":

            $ h_right_arm        = "right_1"
            $ h_left_arm         = "fingering"
            $ hermione_action_a  = "characters/hermione/body/arms/left/fingering.png"

        if hermione_action == "covering_top":

            $ h_right_arm        = "right_1"
            $ h_left_arm         = "finger"
            $ hermione_action_a  = "characters/hermione/body/arms/left/finger.png"

        if hermione_action == "pinch":

            $ h_right_arm        = "blank"
            $ h_left_arm         = "fingering_and_pinching"
            $ hermione_action_a  = "characters/hermione/body/arms/both/fingering_and_pinching.png"
            #$ hermione_breasts   = "characters/hermione/body/breasts/breasts_nonips.png"

        if hermione_action == "hands_cuffed":

            $ h_right_arm        = "blank"
            $ h_left_arm         = "cuffed"

        if hermione_action == "milk_breasts":

            $ h_right_arm        = "right_1"
            $ h_left_arm         = "left_1"

            $ hermione_action_b  = "characters/hermione/clothes/milk/milk_"+str(milking)+".png"

    return



#Body Update

label update_her_body:

    #Expanded Breasts
    if hermione_perm_expand_breasts or hermione_expand_breasts: #Expanded Breasts

        #Large Breasts Shadow Fix
        $ hermione_base        = "characters/hermione/body/base/hermione_base_large_breasts.png"
        $ hermione_right_arm   = "characters/hermione/body/arms/right/large_breasts/"+str(h_right_arm)+".png"

        if hermione_wear_top:

            if hermione_wear_bra:
                if h_top in h_top_remove_bra_list:
                    $ h_breasts = "breasts_expanded_large_nipfix"
                elif h_bra in h_bra_nipfix_list:
                    $ h_breasts = "breasts_expanded_large_nipfix"
                elif h_bra in h_bra_pressed_list:
                    $ h_breasts = "breasts_expanded_large_nipfix"
                elif h_top in h_top_nipfix_list:
                    $ h_breasts = "breasts_expanded_large_nipfix"
                else:
                    $ h_breasts = "breasts_expanded_large"
            else:
                if hermione_use_action and hermione_action == "lift_top":
                    $ h_breasts = "breasts_expanded_large"
                else:
                    if h_top in h_top_remove_bra_list:
                        $ h_breasts = "breasts_expanded_large_nipfix"
                    elif h_top in h_top_nipfix_list:
                        $ h_breasts = "breasts_expanded_large_nipfix"
                    else:
                        $ h_breasts = "breasts_expanded_large"

        else:

            if hermione_wear_bra:
                if h_bra in h_bra_nipfix_list:
                    $ h_breasts = "breasts_expanded_large_nipfix"
                elif h_bra in h_bra_pressed_list:
                    $ h_breasts = "breasts_expanded_large_nipfix"
                else:
                    $ h_breasts = "breasts_expanded_large"
            else:
                $ h_breasts = "breasts_expanded_large"


    #Normal Breasts
    else:

        #Normal Breast Shadow
        $ hermione_base        = "characters/hermione/body/base/hermione_base.png"
        $ hermione_right_arm   = "characters/hermione/body/arms/right/"+str(h_right_arm)+".png"

        if hermione_wear_top:

            if hermione_wear_bra:
                if h_top in h_top_remove_bra_list:
                    $ h_breasts = "breasts_nipfix"
                elif h_bra in h_bra_nipfix_list:
                    $ h_breasts = "breasts_nipfix"
                elif h_bra in h_bra_pressed_list:
                    $ h_breasts = "breasts_normal_pressed"
                elif h_top in h_top_nipfix_list:
                    $ h_breasts = "breasts_normal_pressed"
                else:
                    $ h_breasts = "breasts_normal"
            else:
                if hermione_use_action and hermione_action == "lift_top":
                    $ h_breasts = "breasts_normal"
                else:
                    if h_top in h_top_remove_bra_list:
                        $ h_breasts = "breasts_nipfix"
                    elif h_top in h_top_nipfix_list:
                        $ h_breasts = "breasts_normal_pressed"
                    else:
                        $ h_breasts = "breasts_normal"

        else:

            if hermione_wear_bra:
                if h_bra in h_bra_nipfix_list:
                    $ h_breasts = "breasts_nipfix"
                elif h_bra in h_bra_pressed_list:
                    $ h_breasts = "breasts_normal_pressed"
                else:
                    $ h_breasts = "breasts_normal"
            else:
                $ h_breasts = "breasts_normal" # normal breasts


    if hermione_wear_outfit:
        if hermione_wear_top:
            $ h_breasts = hermoine_outfit_GLBL.breast_layer


    #Transparency Fix
    if (hermione_wear_top and her_top_transp < 1) or (hermione_wear_bra and her_bra_transp < 1):
        if hermione_perm_expand_breasts or hermione_expand_breasts:
            $ h_breasts = "breasts_normal_pressed"
        else:
            $ h_breasts = "breasts_normal_pressed"


    #Hermione Actions
    if hermione_use_action and hermione_action == "milk_breasts":
        $ h_breasts = "breasts_expanded_xlarge"

    $ hermione_breasts = "characters/hermione/body/breasts/"+str(h_breasts)+".png"

    $ hermione_left_arm = "characters/hermione/body/arms/left/"+str(h_left_arm)+".png"
    $ hermione_right_arm = "characters/hermione/body/arms/right/"+str(h_right_arm)+".png"

    #Hermione Ass
    if hermione_perm_expand_ass or hermione_expand_ass: #Expanded Ass
        if not hermione_wear_bottom and not hermione_wear_panties:
            $ hermione_legs = "characters/hermione/body/legs/expanded_ass.png"
        else:
            $ hermione_legs = "characters/hermione/body/legs/legs_1.png"
    else:
        $ hermione_legs = "characters/hermione/body/legs/legs_1.png"

    return


#Makeup
screen hermione_makeup():
    for i in range(0,len(hermione_makeup_list)):
        add "characters/hermione/clothes/makeup/"+str(hermione_makeup_list[i])+".png" xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    zorder hermione_zorder


#Body Accessories
screen hermione_body_accs():
    for i in range(0,len(hermione_body_accs_list)):
        add "characters/hermione/clothes/accs/"+str(hermione_body_accs_list[i])+".png" xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    zorder hermione_zorder


#Piercings
screen hermione_piercings():
    for i in range(0,len(hermione_piercings_list)):
        if hermione_perm_expand_breasts or hermione_expand_breasts: #Expanded Breasts
            add "characters/hermione/clothes/piercings/large_breasts/"+str(hermione_piercings_list[i])+".png" xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
        else:
            add "characters/hermione/clothes/piercings/"+str(hermione_piercings_list[i])+".png" xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    zorder hermione_zorder

#TATTOOS
screen hermione_tattoos():
    for i in range(0,len(hermione_tattoos_list)):
        add "characters/hermione/body/tattoos/"+str(hermione_tattoos_list[i])+".png" xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    zorder hermione_zorder

screen hermione_ass():
    tag hermione_ass

    add "characters/hermione/body/ass/hermione_ass_01.png" xpos 500 ypos 0 zoom (1.0/hermione_scaleratio)
    if hermione_ass_cum:
        add "characters/hermione/body/ass/ass_cum_01.png" xpos 500 ypos 0 zoom (1.0/hermione_scaleratio)
    zorder 5

screen hermione_outfit():
    tag hermione_main
    for i in hermoine_outfit_GLBL.getOutfitLayers():
        add "characters/hermione/clothes/"+i+".png" xpos hermione_xpos ypos hermione_ypos alpha her_outfit_transp xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    add hermione_hair_top xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    add hermione_costume_action_a xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    zorder hermione_zorder

screen hermione_kneel():
    tag hermione_kneel
    zorder hermione_zorder

    $ hermione_xpos = hermione_xpos
    $ hermione_ypos_offset = hermione_ypos-150

    if not hermione_kneel_leg:
        add "characters/hermione/body/kneel/kneel_base.png" xpos hermione_xpos ypos hermione_ypos_offset xzoom hermione_flip zoom (1.0/hermione_scaleratio) #Add the base body
    else:
        add "characters/hermione/body/kneel/kneel_base_2.png" xpos hermione_xpos ypos hermione_ypos_offset xzoom hermione_flip zoom (1.0/hermione_scaleratio) #Add the base body

    add hermione_cheeks xpos hermione_xpos ypos hermione_ypos_offset xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    add hermione_eyes xpos hermione_xpos ypos hermione_ypos_offset xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    #add hermione_eyebrows xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    add hermione_tears xpos hermione_xpos ypos hermione_ypos_offset xzoom hermione_flip zoom (1.0/hermione_scaleratio)
    add hermione_mouth xpos hermione_xpos ypos hermione_ypos_offset xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    add "characters/hermione/body/kneel/kneel_hair.png" xpos hermione_xpos ypos hermione_ypos_offset xzoom hermione_flip zoom (1.0/hermione_scaleratio) #Add the base body

    if uni_sperm:
        add u_sperm xpos hermione_xpos ypos hermione_ypos_offset xzoom hermione_flip zoom (1.0/hermione_scaleratio)

    if hermione_kneel_leg:
        add "characters/hermione/body/kneel/kneel_leg.png" xpos luna_xpos ypos 0 xzoom -1 zoom (1.0/hermione_scaleratio) #Add Luna's leg
        add "characters/hermione/body/kneel/kneel_arm.png" xpos luna_xpos ypos 0 zoom (1.0/hermione_scaleratio)

    if hermione_kneel_cock: #Need to redo this into a better system.
        add "characters/hermione/body/kneel/kneel_cock.png" xpos luna_xpos ypos luna_ypos zoom (1.0/hermione_scaleratio)
