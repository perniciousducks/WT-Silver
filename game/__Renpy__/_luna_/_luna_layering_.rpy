
screen luna_main():
    tag luna_main
    zorder luna_zorder
    
    fixed:
        at transform:
            xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)

        add luna_base

        add "characters/luna/body/arms/left_"+str(luna_l_arm)+".png"
        add luna_breasts
        add "characters/luna/body/arms/right_"+str(luna_r_arm)+".png"

        add luna_hair
        add luna_mouth
        add "characters/luna/face/eyes/_white_.png"
        add luna_pupil
        add luna_eye
        add luna_eyebrow
        add luna_cheeks
        add luna_tears
        add luna_hair_shadow

        if luna_wear_cum_under:
            add "characters/luna/body/cum/cum_"+str(luna_cum)+".png"

        if luna_wear_outfit and luna_wear_top:
            # Outfit
            for i in luna_outfit_GLBL.getOutfitLayers():
                add "characters/luna/clothes/"+i+".png" alpha lun_outfit_transp
        else:
            # Clothes
            if luna_wear_bra and not luna_wear_top:
                add luna_bra alpha lun_bra_transp
            if luna_wear_panties:
                add luna_panties alpha lun_panties_transp
            if luna_wear_onepiece and not luna_wear_top and not luna_wear_bottom:
                add luna_onepiece alpha lun_onepiece_transp
            if luna_wear_stockings:
                add luna_stockings alpha lun_stockings_transp
            if luna_wear_bottom:
                add luna_bottom alpha lun_bottom_transp
            if luna_wear_top:
                add luna_top alpha lun_top_transp
            if luna_wear_neckwear:
                add luna_neckwear alpha lun_top_transp

        # Accessories
        if luna_wear_hat:
            add luna_hat
        if luna_wear_glasses:
            add luna_glasses
        if luna_wear_ears:
            add luna_ears
        if luna_wear_accs:
            add luna_accs

        add "characters/luna/body/arms/left_"+str(luna_l_arm)+"_2.png" # Left arm
        add "characters/luna/body/arms/right_"+str(luna_r_arm)+"_2.png" # Right arm

        if luna_wear_cum:
            add "characters/luna/body/cum/cum_"+str(luna_cum)+".png"

    # Extra stuff
    if genie_base == "characters/genie/base/hard.png":
        # Genie's dick
        add "characters/genie/dick_1.png" xpos genie_xpos ypos genie_ypos
        if not luna_wear_bottom and not luna_wear_panties:
            # Add the right leg cover for the dick. What's a thigh job called again?
            add "characters/luna/body/legs/right_1.png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/luna_scaleratio)
        if luna_wear_cum:
            # Cumshot
            add "characters/luna/body/arms/right_4_2.png" xpos 390 ypos 0 xzoom luna_flip zoom (1.0/luna_scaleratio)
