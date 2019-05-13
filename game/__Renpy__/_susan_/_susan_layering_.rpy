

# Susan Screens.

screen susan_main():
    tag susan_main

    ### BASE IMAGE
    add susan_hair xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) #Add the hair base
    add susan_l_arm xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) #Add the arms
    add susan_r_arm xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) #Add the arms
    add susan_base xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) #Add the base body
    add susan_breasts xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) #Add the base body

    ### FACE
    add susan_eye_bg xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) #Add the eye white
    add susan_pupil xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) #Add the pupil
    add susan_eye xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) #Add the eye outline

    add susan_eyebrow xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) #Add the eyebrow
    add susan_mouth xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) #Add the mouth

    add susan_cheeks xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) #Add the extras
    add susan_tears xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) #Add the extras
    add susan_extra xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) #Add the extras

    ### CLOTHING LAYERS ###

    #Uniform
    if not susan_wear_outfit:
        use susan_uniform

    #Outfit
    if susan_wear_outfit:
        if susan_wear_top:
            use susan_outfit
        else:
            use susan_uniform

    ### ACCESORIES LAYERS ###

    #Hair+
    add susan_hair_shadow xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) #Add the hair shadow

    #Hat
    if susan_wear_hat:
        add susan_hat xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) # Add the accessory

    #Cum layers.
    if susan_face_covered:
        add susan_face_cum xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio)
    if susan_body_covered:
        add susan_body_cum xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio)
    if susan_aftersperm:
        add susan_clothes_cum xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio)

    #Robe
    if susan_wear_robe:
        add susan_robe xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio)

    ### ZORDER
    zorder susan_zorder


screen susan_uniform():
    tag susan_main

    ### CLOTHES
    if susan_wear_bra and not (susan_wear_top and (sus_top in ["top_1","top_2","top_3"] or sus_bra in ["bra_chain"]) ):
        add susan_bra xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) # Add the bra
    if susan_wear_panties and not susan_wear_bottom:
        add susan_panties xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) # Add the panties
    if susan_wear_garterbelt:
        add susan_garterbelt xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio)
    if susan_wear_stockings:
        add susan_stockings xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) # Add the stockings
    if susan_wear_onepiece and not susan_wear_top and not susan_wear_robe:
        add susan_onepiece xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio)
    if susan_wear_bottom:
        add susan_bottom xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) # Add the skirt
    if susan_wear_top:
        add susan_top xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) # Add the top
    if susan_wear_accs:
        add susan_accs xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio) # Add the accessory
    if susan_wear_neckwear:
        add susan_neckwear xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio)

    ### ZORDER
    zorder susan_zorder


screen susan_outfit():
    tag susan_main

    for i in susan_outfit_GLBL.getOutfitLayers():
        add "characters/susan/clothes/"+i+".png" xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/susan_scaleratio)

    ### ZORDER
    zorder susan_zorder
