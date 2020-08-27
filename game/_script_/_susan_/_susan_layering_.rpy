
screen susan_main():
    tag susan_main
    zorder susan_zorder
    sensitive False

    fixed:
        at main_sprite_position(susan_xpos, susan_ypos, susan_flip, 2)

        add susan_hair
        add susan_l_arm
        add susan_r_arm
        add susan_base
        add susan_breasts

        add susan_eye_bg
        add susan_pupil
        add susan_eye
        add susan_eyebrow

        add susan_mouth
        add susan_cheeks
        add susan_tears

        if susan_wear_top and susan_wear_outfit:
            # Outfit
            for i in susan_outfit_GLBL.outfit_layers:
                add "characters/susan/clothes/"+i+".webp"
        else:
            # Clothes
            if susan_wear_bra and not (susan_wear_top and (sus_top in ["top_1","top_2","top_3"] or sus_bra in ["bra_chain"])):
                add susan_bra
            if susan_wear_panties and not susan_wear_bottom:
                add susan_panties
            if susan_wear_garterbelt:
                add susan_garterbelt
            if susan_wear_stockings:
                add susan_stockings
            if susan_wear_onepiece and not susan_wear_top and not susan_wear_robe:
                add susan_onepiece
            if susan_wear_bottom:
                add susan_bottom
            if susan_wear_top:
                add susan_top
            if susan_wear_accs:
                add susan_accs
            if susan_wear_neckwear:
                add susan_neckwear

        add susan_hair_shadow

        # Hat
        if susan_wear_hat:
            add susan_hat

        # Cum
        if susan_face_covered:
            add susan_face_cum
        if susan_body_covered:
            add susan_body_cum
        if susan_aftersperm:
            add susan_clothes_cum

        # Robe
        if susan_wear_robe:
            add susan_robe
