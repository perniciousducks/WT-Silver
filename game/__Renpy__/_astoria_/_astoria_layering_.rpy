

screen astoria_main:
    tag astoria_main

    ### BASE IMAGE
    add astoria_hair xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)#Add the hair base
    add astoria_l_arm xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)#Add the arms
    add astoria_r_arm xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)#Add the arms
    add astoria_base xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)#Add the base body

    ### FACE
    add astoria_eye_bg xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)#Add the eye white
    add astoria_pupil xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)#Add the pupil
    add astoria_eye xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)#Add the eye outline

    add astoria_eyebrow xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)#Add the eyebrow
    add astoria_mouth xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)#Add the mouth

    add astoria_cheeks xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)#Add the extras
    add astoria_tears xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)#Add the extras
    add astoria_extra xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)#Add the extras

    ### CLOTHING LAYERS ###

    #Uniform
    if not astoria_wear_outfit:
        use astoria_uniform

    #Outfit
    if astoria_wear_outfit:
        if astoria_wear_top:
            use astoria_outfit
        else:
            use astoria_uniform

    ### ACCESORIES LAYERS ###

    #Robe
    if astoria_wear_robe:
        add astoria_robe xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)

    #Hair+
    add astoria_hair_shadow xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)#Add the hair shadow

    #Hat
    if astoria_wear_hat:
        add astoria_hat xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)

    add astoria_l_hand xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)# Add the left hand
    add astoria_r_hand xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)# Add the left hand

    ### ZORDER
    zorder astoria_zorder


screen astoria_uniform:
    tag astoria_main

    ### CLOTHES
    if astoria_wear_bra and not astoria_wear_top:
        add astoria_bra xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)# Add the bra
    if astoria_wear_panties and not astoria_wear_bottom:
        add astoria_panties xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)# Add the panties
    if astoria_wear_garterbelt:
        add astoria_garterbelt xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)
    if astoria_wear_stockings:
        add astoria_stockings xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio) # Add the stockings
    if astoria_wear_onepiece and not astoria_wear_top and not astoria_wear_robe:
        add astoria_onepiece xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)
    if astoria_wear_bottom and not astoria_wear_robe:
        add astoria_bottom xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)# Add the skirt
    if astoria_wear_top and not astoria_wear_robe:
        add astoria_top xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)# Add the top
    if astoria_wear_accs:
        add astoria_accs xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio) # Add the accessory
    if astoria_wear_neckwear:
        add astoria_neckwear xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)

    ### ZORDER
    zorder astoria_zorder


screen astoria_outfit:
    tag astoria_main

    for i in astoria_outfit_GLBL.getOutfitLayers():
        add "characters/astoria/clothes/custom/"+i xpos astoria_xpos ypos astoria_ypos xzoom astoria_flip zoom (1.0/astoria_scaleratio)

    ### ZORDER
    zorder astoria_zorder
