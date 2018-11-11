

screen tonks_main:
    ### BASE IMAGE
    add tonks_base xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) #Add the base body
    add tonks_l_arm xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) #Add the arms
    add tonks_r_arm xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) #Add the arms
    add tonks_boobs xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) #Add the base body

    ### FACE
    add tonks_eye_bg xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) #Add the eye white
    add tonks_pupil xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) #Add the pupil
    add tonks_eye xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) #Add the eye outline

    add tonks_eyebrow xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) #Add the eyebrow
    #add tonks_hair_shadow xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) #Add the hair shadow
    if tonks_wear_pubic_hair:
        add tonks_pubic_hair xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)
    add tonks_mouth xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) #Add the mouth

    add tonks_cheeks xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) #Add the extras
    add tonks_tears xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) #Add the extras
    add tonks_extra xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) #Add the extras

    ### CLOTHES

    #Uniform
    if not tonks_wear_outfit:
        use tonks_uniform

    #Outfit
    if tonks_wear_outfit:
        if tonks_wear_top:
            use tonks_outfit
        else:
            use tonks_uniform

    ### ACCESORIES LAYERS ###

    #Hair+
    if not (tonks_wear_hat and ton_hat in ["paper_bag_1","paper_bag_2","paper_bag_3"] ):
        add tonks_hair xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)

    #Hat
    if tonks_wear_hat:
        add tonks_hat xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)

    #Cum layers.
    if tonks_face_covered:
        add tonks_face_cum xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)
    if tonks_body_covered:
        add tonks_body_cum xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)
    if tonks_aftersperm:
        add tonks_clothes_cum xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)

    ### ZORDER
    zorder tonks_zorder


screen tonks_uniform:
    tag tonks_main

    ### Piercings
    if tonks_wear_piercings:
        add tonks_ear_piercing xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)
        add tonks_nipple_piercing xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)
        add tonks_belly_piercing xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)
        add tonks_intimate_piercing xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)

    ### CLOTHES
    if tonks_wear_robe:
        add tonks_robe_back xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) # Add the coat back
    if tonks_wear_bra and not (tonks_wear_robe or tonks_wear_top):
        add tonks_bra xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) # Add the bra
    if tonks_wear_panties:
        add tonks_panties xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) # Add the panties
    if tonks_wear_stockings:
        add tonks_stockings xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) # Add the stockings
    if tonks_wear_top:
        add tonks_top xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) # Add the top
    if tonks_wear_bottom and not tonks_wear_robe:
        add tonks_bottom xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) # Add the skirt

    add tonks_l_hand  xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)

    if tonks_wear_accs:
        add tonks_accs xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) # Add the accessory
    if tonks_wear_neckwear:
        add tonks_neckwear xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)
    if tonks_wear_robe:
        add tonks_robe xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) # Add the coat
    if tonks_wear_gloves:
        add tonks_gloves xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)

    ### ZORDER
    zorder tonks_zorder


screen tonks_outfit:
    tag tonks_main

    for i in tonks_outfit_GLBL.getOutfitLayers():
        add "characters/tonks/clothes/custom/"+i xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)

    ### ZORDER
    zorder tonks_zorder
