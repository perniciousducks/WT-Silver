

screen cho_chang:
    tag cho_main

    ### BASE IMAGE
    add cho_base xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) #Add the base body
    add cho_arms xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) #Add the arms
    add cho_l_hand xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) # Add the left hand
    add cho_hair xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio)

    ### FACE
    add cho_eye_bg xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) #Add the eye white
    add cho_pupil xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) #Add the pupil
    add cho_eye xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) #Add the eye outline

    add cho_eyebrow xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) #Add the eyebrow
    add cho_mouth xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) #Add the mouth

    add cho_hair xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio)
    add cho_tears xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) #Add the tears

    ### CLOTHING LAYERS ###

    #Uniform
    if not cho_wear_outfit:
        use cho_uniform

    #Outfit
    if cho_wear_outfit:
        if cho_wear_top:
            use cho_outfit
        else:
            use cho_uniform

    ### OTHER
    add cho_hair_shadow xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) #Add the hair shadow

    ### ZORDER
    zorder cho_zorder


screen cho_uniform:
    tag cho_main

    ### CLOTHES
    if cho_wear_bra and not cho_wear_top:
        add cho_bra xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) # Add the bra
    if cho_wear_panties and not cho_wear_bottom:
        add cho_panties xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) # Add the panties
    if cho_wear_stockings:
        add cho_stockings xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) # Add the stockings
    if cho_wear_bottom:
        add cho_bottom xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) # Add the skirt/pants
    if cho_wear_top:
        add cho_top xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) # Add the top
    if cho_wear_accs:
        add cho_accs xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) # Add the accessory

    add cho_l_hand xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) # Add the left hand
    if cho_wear_gloves:
        add cho_gloves xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio)
    if cho_wear_neckwear:
        add cho_neckwear xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio)

    if cho_wear_robe:
        add cho_robe xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio)
    if cho_wear_gloves and c_gloves in ["quidditch"]: #On top of Quidditch robe.
        add cho_gloves xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio)

    ### ZORDER
    zorder cho_zorder

screen cho_outfit:
    tag cho_main

    for i in cho_outfit_GLBL.getOutfitLayers():
        add "characters/cho/clothes/custom/"+i xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio)

    ### ZORDER
    zorder cho_zorder
