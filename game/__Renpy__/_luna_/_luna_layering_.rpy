

# Luna Screens.

screen luna_main():
    tag luna_main
    zorder luna_zorder

    ### BASE IMAGE
    add luna_base xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)

    #Arms
    if (luna_wear_top and lun_top in luna_arms_up_list) or (luna_wear_outfit and luna_outfit_GLBL.id in luna_arms_up_list): #Temporary. Needs a call label similar to "update_her_body"
        $ luna_l_arm = "2"
        $ luna_r_arm = "2"
    else:
        pass

    add "characters/luna/body/arms/left_"+str(luna_l_arm)+".png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)#Add the left arm
    add luna_breasts xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)
    add "characters/luna/body/arms/right_"+str(luna_r_arm)+".png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)#Add the right arm

    ### FACE
    add luna_hair xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)#Add the hair base

    add luna_mouth xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)#Add the mouth
    add "characters/luna/face/eyes/_white_.png"  xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)
    add luna_pupil xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)#Add the pupil
    add luna_eye xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)#Add the eye outline
    add luna_eyebrow xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)#Add the eyebrow
    #add luna_cheeks xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)#Add her blush to base
    add luna_tears xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)
    add luna_hair_shadow xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio) #add the hair overlayer

    if luna_wear_cum_under: #Luna cum but under clothes
        add "characters/luna/body/cum/cum_"+str(luna_cum)+".png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)# Add the top

    ### CLOTHING LAYERS ###

    #Uniform
    if not luna_wear_outfit:
        use luna_uniform

    #Outfit
    if luna_wear_outfit:
        if luna_wear_top:
            use luna_outfit
        else:
            use luna_uniform

    ### ACCESORIES LAYERS ###

    if luna_wear_hat:
        add luna_hat xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)
    if luna_wear_glasses:
        add luna_glasses xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)
    if luna_wear_ears:
        add luna_ears xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)
    if luna_wear_accs:
        add luna_accs xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)


    ### ARM OVERLAYS
    add "characters/luna/body/arms/left_"+str(luna_l_arm)+"_2.png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)#Add the left arm
    add "characters/luna/body/arms/right_"+str(luna_r_arm)+"_2.png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)#Add the right arm

    if luna_wear_cum:
        add "characters/luna/body/cum/cum_"+str(luna_cum)+".png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)

    if genie_base == "characters/genie/base/hard.png": #add genies dick for licking/sucking
        add "characters/genie/dick_1.png" xpos genie_xpos ypos genie_ypos
    if genie_base == "characters/genie/base/hard.png" and not luna_wear_bottom and not luna_wear_panties: #add leg
        add "characters/luna/body/legs/right_1.png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)#Add the right leg cover for the dick. What's a thigh job called again?

    if luna_wear_cum and genie_base == "characters/genie/base/hard.png":
        add "characters/luna/body/arms/right_4_2.png" xpos 390 ypos 0 xzoom luna_flip zoom (1.0/luna_scaleratio)


screen luna_uniform():
    tag luna_main

    ### CLOTHES
    if luna_wear_bra and not luna_wear_top:
        add luna_bra xpos luna_xpos ypos luna_ypos alpha lun_bra_transp xzoom luna_flip zoom (1.0/luna_scaleratio)
    if luna_wear_panties:
        add luna_panties xpos luna_xpos ypos luna_ypos alpha lun_panties_transp xzoom luna_flip zoom (1.0/luna_scaleratio)

    #One-Piece
    if luna_wear_onepiece:
        if luna_wear_top or luna_wear_bottom:
            pass
        else:
            add luna_onepiece xpos luna_xpos ypos luna_ypos alpha lun_onepiece_transp xzoom luna_flip zoom (1.0/luna_scaleratio)

    if luna_wear_stockings:
        add luna_stockings xpos luna_xpos ypos luna_ypos alpha lun_stockings_transp xzoom luna_flip zoom (1.0/luna_scaleratio)
    if luna_wear_bottom:
        add luna_bottom xpos luna_xpos ypos luna_ypos alpha lun_bottom_transp xzoom luna_flip zoom (1.0/luna_scaleratio)
    if luna_wear_top:
        add luna_top xpos luna_xpos ypos luna_ypos alpha lun_top_transp xzoom luna_flip zoom (1.0/luna_scaleratio)
    if luna_wear_neckwear:
        add luna_neckwear xpos luna_xpos ypos luna_ypos alpha lun_top_transp xzoom luna_flip zoom (1.0/luna_scaleratio)

    ### ZORDER
    zorder luna_zorder


screen luna_outfit():
    tag luna_main

    for i in luna_outfit_GLBL.getOutfitLayers():
        add "characters/luna/clothes/"+i+".png" xpos luna_xpos ypos luna_ypos alpha lun_outfit_transp xzoom luna_flip zoom (1.0/luna_scaleratio)

    ### ZORDER
    zorder luna_zorder
