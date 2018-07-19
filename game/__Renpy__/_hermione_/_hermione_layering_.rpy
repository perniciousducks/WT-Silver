

### Hermione Main ###

screen hermione_main:
    tag hermione_main

    #Behind body
    if hermione_wear_buttplug:
        add hermione_buttplug xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    if hermione_wear_ears:
        if h_ears == "cat_ears":
            add "characters/hermione/accessories/ears/"+str(h_ears)+"_tail_"+str(h_hair_color)+".png" xpos hermione_xpos ypos hermione_ypos


    ### BODY LAYERS ###

    #Body & Legs
    add hermione_base xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio) #Add the base body
    add hermione_legs xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    #Hair
    add hermione_hair_a xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    #Right Arm
    #if hermione_action and h_action_show_arms:
    #    add hermione_action_right_arm xpos hermione_xpos ypos hermione_ypos
    #elif not hermione_action:
    add hermione_right_arm xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    #Breasts
    add hermione_breasts xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    #Left Arm
    #if hermione_action and h_action_show_arms:
    #    add hermione_action_left_arm xpos hermione_xpos ypos hermione_ypos
    #elif not hermione_action:
    add hermione_left_arm xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    #Pubic Hair
    add hermione_pubic_hair xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    #Face
    add hermione_cheeks xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    add hermione_eyes xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    #add hermione_eyebrows xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    add hermione_tears xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    add hermione_mouth xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    #Tattoos
    if hermione_wear_tattoos:
        use hermione_tattoos

    #Body Fluids
    if hermione_dribble:
        add "characters/hermione/body/legs/dripping.png" xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    if hermione_squirt:
        add "characters/hermione/body/legs/squirting.png" xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    #Penis
    if hermione_futa and not hermione_wear_bottom and not hermione_wear_panties:
        add "characters/hermione/body/legs/dick.png" xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    #Piercings
    if hermione_wear_piercings:
        add hermione_ear_piercing xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
        add hermione_nipple_piercing xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
        add hermione_belly_piercing xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
        add hermione_intimate_piercing xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    ### CLOTHING LAYERS ###

    #Uniform
    if not hermione_costume:
        use hermione_uniform

    #Costume
    if hermione_costume:
        if hermione_wear_top:
            use hermione_costume
        else:
            use hermione_uniform

    ### ACCESORIES LAYERS ###

    #Glasses
    if hermione_wear_glasses:
        add hermione_glasses xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    add hermione_hair_b xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    #Hat
    if hermione_wear_hat:
        add hermione_hat xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    #Ears
    if hermione_wear_ears:
        if h_ears == "elf_ears" and h_hair_style == "A": #Doesn't get added to normal hair
            pass
        else:
            add hermione_ears xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    #Makeup
    if hermione_wear_makeup:
        use hermione_makeup


    ### SPERM LAYERS ###

    if uni_sperm:
        add u_sperm xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "characters/hermione/face/auto_02.png" xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    elif aftersperm: #Shows cum stains on Hermione's uniform.
        add "characters/hermione/face/auto_03.png" xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)


    ### EMOTES ###
    add hermione_emote xpos hermione_xpos ypos hermione_ypos


    zorder hermione_zorder



### HERMIONE UNIFORM ###

screen hermione_uniform:
    tag hermione_main

    #Panties
    if hermione_wear_panties:
        add hermione_panties xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)
        add hermione_panties_overlay xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    #Garterbelt
    if hermione_wear_garterbelt:
        add hermione_garterbelt xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)

    #Stockings
    if hermione_wear_stockings:
        add hermione_stockings xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)

    #Bottom #Behind top layer.
    if hermione_wear_bottom:

        if hermione_wear_onepiece and (h_onepiece in h_onepieces_list): #Skirt or Pants gets added later
            pass
        else:
            if hermione_action == "none" or hermione_action == "hold_book": #Other actions use the layer below!
                add hermione_skirt xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)
            if hermione_action == "lift_top" and h_top in h_lift_top_list: #Bottom gets added later, after the top!
                pass
            else: #Bottom gets added now, before the top!
                add hermione_skirt xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)

    #Action/Pose Fix A (layer above skirt)
    add hermione_action_a xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    #Bra
    if hermione_wear_bra and not (h_top in h_top_remove_bra_list and hermione_wear_top):
        add hermione_bra xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)

    #One-Piece
    if hermione_wear_onepiece:
        if not h_onepiece in h_onepieces_nighties_list:
            add hermione_onepiece xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)
        else: #Nighties
            if hermione_wear_top or hermione_wear_bottom:
                pass
            else:
                add hermione_onepiece xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)
        if hermione_wear_bottom and h_onepiece in h_onepieces_list:
            add hermione_skirt xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)

    #Gloves
    if hermione_wear_gloves:
        add hermione_gloves xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)

    #Top
    if hermione_wear_top:
        add hermione_top xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)

    #Bottom #on top of top layer. #Most skirts get added here!
    if hermione_wear_bottom:
        if hermione_action != "none" and hermione_action != "hold_book" and hermione_action != "lift_top":
            add hermione_skirt xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)
        elif hermione_action == "lift_top":
            if h_top in h_lift_top_list:
                add hermione_skirt xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)
        else:
            pass

    #Badges & Belts
    if hermione_wear_body_accs:
        use hermione_body_accs

    #Action/Pose Fix B (layer above top)
    #add hermione_action_a xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    add hermione_action_b xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    #Robe
    if hermione_wear_robe:
        add hermione_robe xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)

    #Neckwear
    if hermione_wear_neckwear:
        add hermione_neckwear xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)

    zorder hermione_zorder


screen hermione_face:
    tag hermione_head

    #Face
    add hermione_cheeks xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    add hermione_eyes xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    #add hermione_eyebrows xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    add hermione_mouth xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    add hermione_tears xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)

    add hermione_hair_b xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    if face_on_cg and ccg_folder == "herm_sex":
        add "images/28_cg/herm_sex/genie_hand.png" zoom (1.0/scaleratio) #Genies hand on head.

    ### EMOTES ###
    add hermione_emote xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)

    zorder 5


### HERMIONE HEAD ###

screen hermione_head:
    tag hermione_head


    #Behind Body
    if hermione_wear_ears:
        if h_ears == "cat_ears":
            add "characters/hermione/accessories/ears/"+str(h_ears)+"_tail_"+str(h_hair_color)+".png" xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio) # add cat ears


    ### BODY LAYERS ###

    #Body & Legs
    add hermione_base xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    add hermione_legs xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)

    #Hair
    add hermione_hair_a xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)

    #Right Arm
    add hermione_right_arm xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)

    #Breasts
    add hermione_breasts xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)

    #Left Arm
    add hermione_left_arm xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)

    #Tattoos
    if hermione_wear_tattoos:
        use hermione_head_tattoos

    #Face
    add hermione_cheeks xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    add hermione_eyes xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    #add hermione_eyebrows xpos hermione_head_xpos ypos hermione_head_ypos
    add hermione_mouth xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    add hermione_tears xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)

    #Piercings
    if hermione_wear_piercings:
        add hermione_ear_piercing xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
        add hermione_nipple_piercing xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
        add hermione_belly_piercing xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
        add hermione_intimate_piercing xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)


    ### CLOTHING LAYERS ###

    #Uniform
    if not hermione_costume:
        use hermione_head_uniform

    #Costume
    else:
        if hermione_wear_top:
            use hermione_head_costume
        else:
            use hermione_head_uniform

    ### ACCESORIES LAYERS ###

    #Glasses
    if hermione_wear_glasses:
        add hermione_glasses xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)

    add hermione_hair_b xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)

    #Hat
    if hermione_wear_hat:
        add hermione_hat xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)

    #Ears
    if hermione_wear_ears:
        if h_ears == "elf_ears" and h_hair_style == "A": #Doesn't get added to normal hair
            pass
        else:
            add hermione_ears xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)

    #Makeup
    if hermione_wear_makeup:
        use hermione_head_makeup


    ### SPERM LAYERS ###
    if uni_sperm:
        add u_sperm xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "characters/hermione/face/auto_02.png" xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    elif aftersperm: #Shows cum stains on Hermione's uniform.
        add "characters/hermione/face/auto_03.png" xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)


    ### EMOTES ###
    add hermione_emote xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)


    zorder hermione_head_zorder #Should be 8.


screen hermione_head_uniform:
    tag hermione_head

    #Bra
    if hermione_wear_bra and not (h_top in h_top_remove_bra_list and hermione_wear_top):
        add hermione_bra xpos hermione_head_xpos ypos hermione_head_ypos alpha transparency zoom (1.0/scaleratio)

    #One-Piece
    if hermione_wear_onepiece:
        if not h_onepiece in h_onepieces_nighties_list:
            add hermione_onepiece xpos hermione_head_xpos ypos hermione_head_ypos alpha transparency zoom (1.0/scaleratio)

        #Nighties
        else:
            if hermione_wear_top or hermione_wear_bottom:
                pass
            else:
                add hermione_onepiece xpos hermione_head_xpos ypos hermione_head_ypos alpha transparency zoom (1.0/scaleratio)

    #Gloves
    if hermione_wear_gloves:
        add hermione_gloves xpos hermione_head_xpos ypos hermione_head_ypos alpha transparency zoom (1.0/scaleratio)

    #Top
    if hermione_wear_top:
        add hermione_top xpos hermione_head_xpos ypos hermione_head_ypos alpha transparency zoom (1.0/scaleratio)

    #Body Accessories
    if hermione_wear_body_accs:
        use hermione_head_body_accs

    #Action/Pose Fixes
    if hermione_action != "none":
        add hermione_action_a xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
        add hermione_action_b xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)

    #Robe
    if hermione_wear_robe:
        add hermione_robe xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)

    #Neckwear
    if hermione_wear_neckwear:
        add hermione_neckwear xpos hermione_head_xpos ypos hermione_head_ypos alpha transparency zoom (1.0/scaleratio)

    zorder hermione_head_zorder #Should be 8.



#Uniform Update

label update_her_uniform:

    if hermione_action != "none":
        call update_her_action

    ### Uniform ###


    #Top
    if hermione_perm_expand or hermione_perm_expand_breasts or hermione_expand_breasts: #Expanded Breasts
        if h_top in h_top_has_no_recolor_list:
            $ hermione_top = "characters/hermione/clothes/tops/base/large_breasts/"+str(h_action_top)+""+str(h_top)+".png"
        else:
            $ hermione_top = "characters/hermione/clothes/tops/"+h_top_color+"/large_breasts/"+str(h_action_top)+""+str(h_top)+".png"
    else:
        if h_top in h_top_has_no_recolor_list:
            $ hermione_top = "characters/hermione/clothes/tops/base/"+str(h_action_top)+""+str(h_top)+".png"
        else:
            $ hermione_top = "characters/hermione/clothes/tops/"+h_top_color+"/"+str(h_action_top)+""+str(h_top)+".png"

    #Bottom
    $ hermione_skirt = "characters/hermione/clothes/bottoms/"+h_skirt_color+"/"+str(h_action_bottom)+""+str(h_skirt)+".png"


    ### Underwear ###
    #Bra
    if hermione_perm_expand or hermione_perm_expand_breasts or hermione_expand_breasts: #Expanded Breasts
        $ hermione_bra = "characters/hermione/clothes/underwear/"+h_bra_color+"/large_breasts/"+str(h_bra)+".png"
    else:
        $ hermione_bra = "characters/hermione/clothes/underwear/"+h_bra_color+"/"+str(h_bra)+".png"

    #Panties
    $ hermione_panties = "characters/hermione/clothes/underwear/"+h_panties_color+"/"+str(h_panties)+".png"
    if hermione_wetpanties:
        $ hermione_panties_overlay = "characters/hermione/clothes/underwear/pantystain.png"
    else:
        $ hermione_panties_overlay = "characters/hermione/clothes/underwear/00_blank.png"

    #Onepiece
    if hermione_perm_expand or hermione_perm_expand_breasts or hermione_expand_breasts: #Expanded Breasts
        $ hermione_onepiece = "characters/hermione/clothes/onepieces/"+h_onepiece_color+"/large_breasts/"+str(h_onepiece)+".png"
    else:
        $ hermione_onepiece = "characters/hermione/clothes/onepieces/"+h_onepiece_color+"/"+str(h_onepiece)+".png"

    #Garterbelt
    $ hermione_garterbelt = "characters/hermione/clothes/underwear/"+h_garterbelt_color+"/"+str(h_garterbelt)+".png"


    ### Other Clothing ###
    $ hermione_neckwear = "characters/hermione/clothes/neckwear/"+h_neckwear_color+"/"+str(h_neckwear)+".png"
    $ hermione_gloves = "characters/hermione/clothes/gloves/"+h_gloves_color+"/"+str(h_gloves)+".png"
    $ hermione_stockings = "characters/hermione/clothes/stockings/"+h_stockings_color+"/"+str(h_stockings)+".png"
    $ hermione_robe = "characters/hermione/clothes/robe/base/"+str(h_robe)+".png"


    #Accessories
    $ hermione_glasses = "characters/hermione/accessories/glasses/"+h_glasses_color+"/"+str(h_glasses)+".png"

    if h_ears == "cat_ears":
        $ hermione_ears = "characters/hermione/accessories/ears/hair_"+str(h_hair_style)+"/"+str(h_ears)+"_"+str(h_hair_color)+".png"
    else:
        $ hermione_ears = "characters/hermione/accessories/ears/"+str(h_ears)+".png"

    $ hermione_hat = "characters/hermione/accessories/hats/"+str(h_hat)+".png"


    #Miscellaneous
    $ hermione_buttplug            = "characters/hermione/accessories/plugs/"+str(h_buttplug)+".png"

    #Piercings
    $ hermione_ear_piercing        = "characters/hermione/accessories/piercings/"+str(h_ear_piercing_color)+"/"+str(h_ear_piercing)+".png"
    if hermione_perm_expand or hermione_perm_expand_breasts or hermione_expand_breasts: #Expanded Breasts
        $ hermione_nipple_piercing = "characters/hermione/accessories/piercings/"+str(h_nipple_piercing_color)+"/large_breasts/"+str(h_nipple_piercing)+".png"
    else:
        $ hermione_nipple_piercing = "characters/hermione/accessories/piercings/"+str(h_nipple_piercing_color)+"/"+str(h_nipple_piercing)+".png"
    $ hermione_belly_piercing      = "characters/hermione/accessories/piercings/"+str(h_belly_piercing_color)+"/"+str(h_belly_piercing)+".png"
    $ hermione_intimate_piercing   = "characters/hermione/accessories/piercings/"+str(h_intimate_piercing_color)+"/"+str(h_intimate_piercing)+".png"


    #Costume Action/Pose
    $ hermione_costume_action_a = "characters/hermione/clothes/custom/"+str(h_action_a)+""

    call update_chibi_uniform
    call h_update_body

    return



#Action/Pose Update

label update_her_action:

    #No Arm Change
    $ h_right_arm        = "right_1"
    $ h_left_arm         = "left_1"

    #No Folder Change    #(like "lift_top/")
    $ h_action_top       = ""
    $ h_action_bottom    = ""
    $ h_action_gloves    = "" #No in use yet.

    $ hermione_action_a = "characters/hermione/body/arms/left/00_blank.png"
    $ hermione_action_b = "characters/hermione/body/arms/left/00_blank.png"
    $ hermione_costume_action_a = "characters/hermione/clothes/custom/00_blank.png"


    if hermione_use_action:

        #Always Hide
        $ hermione_wear_onepiece     = False #Hide until art edits are made

        $ hermione_wear_neckwear     = False
        $ hermione_wear_body_accs    = False
        $ hermione_wear_gloves       = False #Hide until art edits are made.
        $ hermione_wear_robe         = False

    #Costume Action/Pose
    if hermione_use_action and hermione_costume:
        if hermione_action in hermoine_outfit_GLBL.actions:
            $ h_action_a = hermoine_outfit_GLBL.ActionImage
        else:
            $ hermione_use_action = False
            $ h_action_a = "00_blank.png"

        return


    #Lift Skirt
    if hermione_use_action and hermione_action == "lift_skirt":

        if hermione_wear_top and hermione_wear_bottom:
            if h_skirt in h_skirts_list:
                $ h_right_arm        = "00_blank"
                $ h_left_arm         = "lift_skirt"
                $ h_action_top       = "lift_skirt/"
            if h_skirt in h_pants_list:
                $ h_right_arm        = "right_1"
                $ h_left_arm         = "pants_down"
                $ h_action_top       = "pants_down/"
            $ h_action_bottom    = "lift_skirt/"

        elif hermione_wear_bottom:
            if h_skirt in h_skirts_list:
                $ h_right_arm        = "00_blank"
                $ h_left_arm         = "lift_skirt"
            if h_skirt in h_pants_list:
                $ h_right_arm        = "00_blank"
                $ h_left_arm         = "pants_down"
            $ h_action_bottom    = "lift_skirt/"

        else:
            $ h_right_arm        = "right_1"
            $ h_left_arm         = "left_1"


    #Lift Top
    if hermione_use_action and hermione_action == "lift_top":

        $ hermione_wear_bra = False #Hide until art edits are made.

        if hermione_wear_top:
            if h_top in h_lift_top_list:
                $ h_right_arm        = "00_blank"
                $ h_left_arm         = "lift_top"
            elif h_top == "uni_top_5":
                $ h_right_arm        = "00_blank"
                $ h_left_arm         = "00_blank"
            else:
                $ h_right_arm        = "right_1"
                $ h_left_arm         = "left_1"
            $ h_action_top       = "lift_top/"

        else:
            if whoring >= 12:
                $ h_right_arm        = "00_blank"
                if hermione_perm_expand or hermione_perm_expand_breasts or hermione_expand_breasts:
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

        $ h_right_arm        = "00_blank"

        if hermione_wear_top:
            $ h_left_arm         = "hold_book"
            $ h_action_top       = "hold_book/"

            if transparency < 1: #Doesn't work, won't add book fix when transparent?!
                $ hermione_action_a  = "characters/hermione/body/arms/left/hold_book_fix.png" #Arm layer fix on top of skirts/pants

        else:
            if hermione_perm_expand or hermione_perm_expand_breasts or hermione_expand_breasts: #Expanded Breasts
                $ h_left_arm         = "hold_book_large"
            else:
                $ h_left_arm         = "hold_book"
            $ hermione_action_a  = "characters/hermione/body/arms/left/hold_book_fix.png" #Arm layer fix on top of skirts/pants


    #Lift Breasts
    if hermione_use_action and hermione_action == "lift_breasts":

        $ hermione_wear_top = False #
        $ hermione_wear_bra = False #Hide until art edits are made.

        $ h_right_arm        = "00_blank"

        if hermione_perm_expand or hermione_perm_expand_breasts or hermione_expand_breasts:
            $ h_left_arm         = "lift_breasts_large"
        else:
            $ h_left_arm         = "lift_breasts"


    #Naked Actions
    if hermione_use_action and hermione_action == "hands_behind" or hermione_action == "covering" or hermione_action == "fingering" or hermione_action == "covering_top" or hermione_action == "pinch" or hermione_action == "hands_cuffed" or hermione_action == "milk_breasts":

        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        $ hermione_wear_bottom = False
        $ hermione_wear_panties = False

        if hermione_action == "hands_behind":

            $ h_right_arm        = "00_blank"
            $ h_left_arm         = "behind"
            #$ hermione_action_a  = "characters/hermione/body/arms/left/behind.png"

        if hermione_action == "covering":

            $ h_right_arm        = "00_blank"
            $ h_left_arm         = "covering"
            #$ hermione_action_a  = "characters/hermione/body/arms/both/covering.png"
            #$ hermione_breasts   = "characters/hermione/body/breasts/breasts_nipfix.png"

        if hermione_action == "fingering":

            $ h_right_arm        = "right_1"
            $ h_left_arm         = "fingering"
            $ hermione_action_a  = "characters/hermione/body/arms/left/fingering.png"

        if hermione_action == "covering_top":

            $ h_right_arm        = "right_1"
            $ h_left_arm         = "finger"
            $ hermione_action_a  = "characters/hermione/body/arms/left/finger.png"

        if hermione_action == "pinch":

            $ h_right_arm        = "00_blank"
            $ h_left_arm         = "fingering_and_pinching"
            $ hermione_action_a  = "characters/hermione/body/arms/both/fingering_and_pinching.png"
            #$ hermione_breasts   = "characters/hermione/body/breasts/breasts_nonips.png"

        if hermione_action == "hands_cuffed":

            $ h_right_arm        = "00_blank"
            $ h_left_arm         = "cuffed"

        if hermione_action == "milk_breasts":

            $ h_right_arm        = "right_1"
            $ h_left_arm         = "left_1"

            $ hermione_action_b  = "characters/hermione/clothes/milk/milk_"+str(milking)+".png"

    return



#Body Update

label h_update_body:

    #Expanded Breasts
    if hermione_perm_expand or hermione_perm_expand_breasts or hermione_expand_breasts: #Expanded Breasts

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


    if hermione_costume:
        if hermione_wear_top:
            $ h_breasts = hermoine_outfit_GLBL.breast_layer


    #Transparency Fix
    if transparency < 1:
        if hermione_perm_expand:

            if hermione_use_action and hermione_action == "lift_top":
                $ h_breasts = "breasts_expanded_large"
            if hermione_wear_top or hermione_wear_onepiece and not hermione_use_action:
                $ h_breasts = "breasts_normal_pressed"
            else:
                $ h_breasts = "breasts_expanded_large"

        else:

            if hermione_use_action and hermione_action == "lift_top":
                $ h_breasts = "breasts_normal"
            if hermione_wear_top or hermione_wear_onepiece and not hermione_use_action:
                $ h_breasts = "breasts_normal_pressed"
            else:
                $ h_breasts = "breasts_normal"


    #Hermione Actions
    if hermione_use_action and hermione_action == "milk_breasts":
        $ h_breasts = "breasts_expanded_xlarge"

    $ hermione_breasts = "characters/hermione/body/breasts/"+str(h_breasts)+".png"

    $ hermione_left_arm = "characters/hermione/body/arms/left/"+str(h_left_arm)+".png"

    #Hermione Ass
    if hermione_perm_expand or hermione_perm_expand_ass or hermione_expand_ass: #Expanded Ass
        if not hermione_wear_bottom and not hermione_wear_panties:
            $ hermione_legs = "characters/hermione/body/legs/expanded_ass.png"
        else:
            $ hermione_legs = "characters/hermione/body/legs/legs_1.png"
    else:
        $ hermione_legs = "characters/hermione/body/legs/legs_1.png"

    return



#Face Update
label h_update:
    if face_on_cg and ccg_folder == "herm_sex": #Flipped face!
        $ hermione_mouth = im.Flip("characters/hermione/face/mouth/"+str(h_lipstick)+"/"+str(h_mouth)+".png", horizontal=True)
        $ hermione_eyes  = im.Flip("characters/hermione/face/eyes/"+str(h_eye_color)+"/"+str(h_eyes)+".png", horizontal=True)
        #$ hermione_eyebrows = im.Flip("characters/hermione/face/eyebrows/"+str(h_hair_color)+"/"+str(h_eyes)+".png", horizontal=True)
        $ hermione_cheeks = im.Flip("characters/hermione/face/cheeks/"+str(h_cheeks)+".png", horizontal=True)
        $ hermione_tears = im.Flip("characters/hermione/face/tears/"+str(h_tears)+".png", horizontal=True)
        $ hermione_emote = im.Flip("characters/emotes/"+str(h_emote)+".png", horizontal=True)
        $ hermione_hair_b = im.Flip("characters/hermione/body/head/A_1_2.png", horizontal=True) #ADD hair-color as soon as there are different hair-colors for the CGs. For now leave it brown!
    else:
        $ hermione_mouth = "characters/hermione/face/mouth/"+str(h_lipstick)+"/"+str(h_mouth)+".png"
        $ hermione_eyes  = "characters/hermione/face/eyes/"+str(h_eye_color)+"/"+str(h_eyes)+".png"
        #$ hermione_eyebrows = "characters/hermione/face/eyebrows/"+str(h_hair_color)+"/"+str(h_eyes)+".png"
        $ hermione_cheeks = "characters/hermione/face/cheeks/"+str(h_cheeks)+".png"
        $ hermione_tears = "characters/hermione/face/tears/"+str(h_tears)+".png"
        $ hermione_emote = "characters/emotes/"+str(h_emote)+".png"

    return

#Hair update.
label update_her_hair:
    if hermione_costume and hermoine_outfit_GLBL.hair_layer != "":
        $ hermione_hair_a = "characters/hermione/clothes/custom/"+hermoine_outfit_GLBL.hair_layer+".png"
        $ hermione_hair_b = "characters/hermione/clothes/custom/"+hermoine_outfit_GLBL.hair_layer+"_2.png"
    else:
        $ hermione_hair_a = "characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+".png"
        $ hermione_hair_b = "characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+"_2.png"
    return

#Hair Update
label h_update_hair:

    if hermione_costume and hermoine_outfit_GLBL.hair_layer != "":
        $ hermione_hair_a = "characters/hermione/clothes/custom/"+hermoine_outfit_GLBL.hair_layer+".png"
        $ hermione_hair_b = "characters/hermione/clothes/custom/"+hermoine_outfit_GLBL.hair_layer+"_2.png"
    else:
        $ hermione_hair_a = "characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+".png"
        $ hermione_hair_b = "characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+"_2.png"
    return








#Makeup
screen hermione_makeup:
    for i in range(0,len(hermione_makeup_list)):
        add "characters/hermione/accessories/makeup/"+str(hermione_makeup_list[i])+".png" xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    zorder hermione_zorder

screen hermione_head_makeup:
    for i in range(0,len(hermione_makeup_list)):
        add "characters/hermione/accessories/makeup/"+str(hermione_makeup_list[i])+".png" xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    zorder hermione_zorder


#Body Accessories
screen hermione_body_accs:
    for i in range(0,len(hermione_body_accs_list)):
        add "characters/hermione/accessories/body_accs/"+str(hermione_body_accs_list[i])+".png" xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    zorder hermione_zorder

screen hermione_head_body_accs:
    for i in range(0,len(hermione_body_accs_list)):
        add "characters/hermione/accessories/body_accs/"+str(hermione_body_accs_list[i])+".png" xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    zorder hermione_zorder


#Piercings
screen hermione_piercings:
    for i in range(0,len(hermione_piercings_list)):
        if hermione_perm_expand or hermione_perm_expand_breasts or hermione_expand_breasts: #Expanded Breasts
            add "characters/hermione/accessories/piercings/large_breasts/"+str(hermione_piercings_list[i])+".png" xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
        else:
            add "characters/hermione/accessories/piercings/"+str(hermione_piercings_list[i])+".png" xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    zorder hermione_zorder

screen hermione_head_piercings:
    for i in range(0,len(hermione_piercings_list)):
        if hermione_perm_expand or hermione_perm_expand_breasts or hermione_expand_breasts: #Expanded Breasts
            add "characters/hermione/accessories/piercings/large_breasts/"+str(hermione_piercings_list[i])+".png" xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
        else:
            add "characters/hermione/accessories/piercings/"+str(hermione_piercings_list[i])+".png" xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    zorder hermione_zorder


#TATTOOS
screen hermione_tattoos:
    for i in range(0,len(hermione_tattoos_list)):
        add "characters/hermione/body/tattoos/"+str(hermione_tattoos_list[i])+".png" xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    zorder hermione_zorder

screen hermione_head_tattoos:
    for i in range(0,len(hermione_tattoos_list)):
        add "characters/hermione/body/tattoos/"+str(hermione_tattoos_list[i])+".png" xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    zorder hermione_zorder


screen hermione_ass:
    tag hermione_ass

    add "characters/hermione/body/ass/hermione_ass_01.png" xpos 500 ypos 0 zoom (1.0/scaleratio)
    if hermione_ass_cum:
        add "characters/hermione/body/ass/ass_cum_01.png" xpos 500 ypos 0 zoom (1.0/scaleratio)
    zorder hermione_zorder

screen hermione_clone:
    tag hermione_clone

    $ hermione_clone_xpos = 500

    add hermione_base xpos hermione_clone_xpos ypos hermione_ypos zoom (1.0/scaleratio) #Add the base body
    add hermione_legs xpos hermione_clone_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    add hermione_right_arm xpos hermione_clone_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    add hermione_breasts xpos hermione_clone_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    add hermione_left_arm xpos hermione_clone_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    add "characters/hermione/body/head/B_2.png" xpos hermione_clone_xpos ypos hermione_ypos zoom (1.0/scaleratio) #Add the hair shadow
    add hermione_body xpos hermione_clone_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    add hermione_tears xpos hermione_clone_xpos ypos hermione_ypos zoom (1.0/scaleratio)

  ### CLOTHES
    add "characters/hermione/clothes/stockings/fishnet_a.png" xpos hermione_clone_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    add "characters/hermione/clothes/uniform/skirt_6.png" xpos hermione_clone_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    add "characters/hermione/clothes/uniform/top_5.png" xpos hermione_clone_xpos ypos hermione_ypos zoom (1.0/scaleratio)

    add "characters/hermione/body/head/B_2_2.png" xpos hermione_clone_xpos ypos hermione_ypos zoom (1.0/scaleratio) #Add the hair shadow
    ### ZORDER
    zorder hermione_zorder


screen hermione_costume:
    tag hermione_main
    for i in hermoine_outfit_GLBL.getOutfitLayers():
        add i xpos hermione_xpos ypos hermione_ypos alpha transparency zoom (1.0/scaleratio)
    add hermione_hair_b xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    #add hermione_costume_e xpos hermione_xpos ypos hermione_ypos
    add hermione_costume_action_a xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    zorder hermione_zorder

screen hermione_head_costume:
    tag hermione_head
    for i in hermoine_outfit_GLBL.getOutfitLayers():
        add i xpos hermione_head_xpos ypos hermione_head_ypos alpha transparency zoom (1.0/scaleratio)
    add hermione_hair_b xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    #add hermione_costume_e xpos hermione_xpos ypos hermione_ypos
    add hermione_costume_action_a xpos hermione_head_xpos ypos hermione_head_ypos zoom (1.0/scaleratio)
    zorder hermione_head_zorder


screen hermione_action:
    tag hermione_main
    if h_action_show_skirt:
        add hermione_action_skirt xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    elif h_action_show_panties or h_request_wear_panties:
        add hermione_action_panties xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    if h_action_show_top:
        add hermione_action_top xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    elif h_action_show_bra:
        add hermione_action_bra xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    add hermione_hair_b xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    add hermione_action_a xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    add hermione_action_b xpos hermione_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    zorder hermione_zorder


screen hermione_kneel:
    tag hermione_kneel

    $ hermione_head_xpos = hermione_head_xpos
    $ hermione_head_ypos_offset = hermione_head_ypos-150

    if not hermione_kneel_leg:
        add "characters/hermione/body/kneel/kneel_base.png" xpos hermione_head_xpos ypos hermione_head_ypos_offset zoom (1.0/scaleratio) #Add the base body
    else:
        add "characters/hermione/body/kneel/kneel_base_2.png" xpos hermione_head_xpos ypos hermione_head_ypos_offset zoom (1.0/scaleratio) #Add the base body

    add hermione_cheeks xpos hermione_head_xpos ypos hermione_head_ypos_offset zoom (1.0/scaleratio)
    add hermione_eyes xpos hermione_head_xpos ypos hermione_head_ypos_offset zoom (1.0/scaleratio)
    #add hermione_eyebrows xpos hermione_head_xpos ypos hermione_ypos zoom (1.0/scaleratio)
    add hermione_tears xpos hermione_head_xpos ypos hermione_head_ypos_offset zoom (1.0/scaleratio)
    add hermione_mouth xpos hermione_head_xpos ypos hermione_head_ypos_offset zoom (1.0/scaleratio)

    add "characters/hermione/body/kneel/kneel_hair.png" xpos hermione_head_xpos ypos hermione_head_ypos_offset zoom (1.0/scaleratio) #Add the base body

    if uni_sperm:
        add u_sperm xpos hermione_head_xpos ypos hermione_head_ypos_offset zoom (1.0/scaleratio)

    if hermione_kneel_leg:
        add "characters/hermione/body/kneel/kneel_leg.png" xpos luna_xpos ypos 0 xzoom -1 zoom (1.0/scaleratio) #Add Luna's leg
        add "characters/hermione/body/kneel/kneel_arm.png" xpos luna_xpos ypos 0 zoom (1.0/scaleratio)

    if hermione_kneel_cock: #Need to redo this into a better system.
        add "characters/hermione/body/kneel/kneel_cock.png" xpos luna_xpos ypos luna_ypos zoom (1.0/scaleratio)

    ### ZORDER
    zorder luna_zorder+1
