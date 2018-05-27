




#From 19_my_screens.rpy
### HERMIONE MAIN ###
screen hermione_main_old: #Screen that shows a full sprite of HERMIONE.
    #tag big_hermione
    
    if custom_outfit_old == 7 or custom_outfit_old == 7.2:
        add "images/23_clothes_store/costumes/power_hair.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 9:
        add "images/23_clothes_store/costumes/harley_hair.png" xpos h_xpos ypos h_ypos
    elif hair_color >= 0:
        add "characters/hermione/face/body/head/"+str(hair_style)+"_"+str(hair_color)+".png" xpos h_xpos ypos h_ypos
    if ears == True and hair_color >= 0:
        add "images/25_mo/ears_"+str(hair_color)+".png" xpos h_xpos ypos h_ypos #The hair. 
    
    add "characters/hermione/face/body/hermione_base.png" xpos h_xpos ypos h_ypos
    
    if lift_shirt == True or book_hold == True or skirt_up == True or fingering == True:
        pass
    else:
        add "characters/hermione/face/body/arms/left/left_0.png" xpos h_xpos ypos h_ypos
        add "characters/hermione/face/body/arms/right/right_0.png" xpos h_xpos ypos h_ypos
    
    if transparency < 1 or not wear_shirts or lift_shirt:
        add "characters/hermione/face/body/breasts/breasts_1.png" xpos h_xpos ypos h_ypos
    elif wear_shirts:
        add "characters/hermione/face/body/breasts/breasts_0.png" xpos h_xpos ypos h_ypos
        
    
    
    # if lift_shirt == True or book_hold == True or skirt_up == True or fingering == True:
        # add "characters/hermione/face/customs/base_3.png" xpos h_xpos ypos h_ypos #Add her base 
    # elif transparency < 1 or not wear_shirts:
        # add "characters/hermione/face/customs/base.png" xpos h_xpos ypos h_ypos #Add her base 
    # elif transparency == 1:
        # add "characters/hermione/face/customs/base_2.png" xpos h_xpos ypos h_ypos #Add her base 

    if collar >= 1 and not badges:
        if collar == 1:
            add "characters/hermione/face/customs/collar_1.png" xpos h_xpos ypos h_ypos
        if collar == 2:
            add "characters/hermione/face/customs/collar_2.png" xpos h_xpos ypos h_ypos
        if collar == 3:
            add "characters/hermione/face/customs/collar_3.png" xpos h_xpos ypos h_ypos

    add h_body xpos h_xpos ypos h_ypos #Add her emotion

    if freckles == True:
        add "images/25_mo/freckles.png" xpos h_xpos ypos h_ypos

    if not only_upper:
        add "characters/hermione/face/legs/base_01.png" xpos h_xpos ypos h_ypos #Add her legs

    if stockings == 1:
        add "images/23_clothes_store/costumes/maid_stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 2:
        add "images/23_clothes_store/costumes/cheer_stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 3:
        add "images/25_mo/stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 4:
        add "images/23_clothes_store/costumes/s_cheer_stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 5:
        add "images/23_clothes_store/costumes/h_cheer_stockings_2.png" xpos h_xpos ypos h_ypos
    else:
        if ne: # Desplays a fishnets in hermione_main screen.
            if ne_01:
                add "characters/hermione/face/nets.png" xpos h_xpos ypos h_ypos # FISHNETS.
    if fingering == True:
        add "characters/hermione/face/shirts/arm.png" xpos h_xpos ypos h_ypos
    if not only_upper:
        if whoring <= 12 or custom_bra >0 and panties:
            if custom_bra == 1:
                add im.Alpha("images/25_mo/lace_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_bra == 2:
                add im.Alpha("images/25_mo/cup_panties.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_bra == 3:
                add im.Alpha("images/25_mo/silk_pants.png", transparency) xpos h_xpos ypos h_ypos
            else:
                add im.Alpha("characters/hermione/face/legs/pants.png", transparency) xpos h_xpos ypos h_ypos

        if custom_skirt >= 1 or custom_outfit_old >= 1 and custom_outfit_old <= 19 and not skirt_up:
            if custom_outfit_old == 1:
                add im.Alpha("images/23_clothes_store/costumes/maid_skirt.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 2:
                add im.Alpha("images/23_clothes_store/costumes/cheer_pants.png", transparency) xpos h_xpos ypos h_ypos            
            elif custom_outfit_old == 3:
                add im.Alpha("images/23_clothes_store/costumes/s_cheer_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 4:
                add im.Alpha("images/23_clothes_store/costumes/heart_legs.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 5:
                add im.Alpha("images/23_clothes_store/costumes/h_cheer_pants_2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 8:
                add im.Alpha("images/23_clothes_store/costumes/marvel_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 9:
                add im.Alpha("images/23_clothes_store/costumes/harley_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 10:
                add im.Alpha("images/23_clothes_store/costumes/ball_dress_skirt.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 11:
                add im.Alpha("images/23_clothes_store/costumes/christmas_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 12:
                add im.Alpha("images/23_clothes_store/costumes/lara_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 1 and custom_outfit_old == 0:
                add im.Alpha("images/25_mo/jeans.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 2:
                add im.Alpha("images/25_mo/ass_exp1.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 3:
                add im.Alpha("images/25_mo/ass_exp2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 4:
                add im.Alpha("images/25_mo/snake.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 5 and custom_outfit_old == 0:
                add im.Alpha("images/23_clothes_store/existing_stock/jeans_short.png", transparency) xpos h_xpos ypos h_ypos
        elif wear_skirts and not skirt_up and custom_outfit_old <= 19:
            if whoring <= 5:
                add im.Alpha("characters/hermione/face/legs/legs_01.png", transparency) xpos h_xpos ypos h_ypos
            elif whoring >= 6 and whoring <= 11: #Mini skirt.
                add im.Alpha("characters/hermione/face/legs/legs_02.png", transparency) xpos h_xpos ypos h_ypos
            elif whoring >= 12 and whoring <= 19: #Micro skirt.
                add im.Alpha("characters/hermione/face/legs/legs_03.png", transparency) xpos h_xpos ypos h_ypos
            elif whoring >= 20 and whoring <= 23: #Mini Micro skirt.
                add im.Alpha("characters/hermione/face/legs/legs_04.png", transparency) xpos h_xpos ypos h_ypos
            else: #Mini Mini Micro skirt.
                add im.Alpha("characters/hermione/face/legs/legs_05.png", transparency) xpos h_xpos ypos h_ypos
    if autograph:
        add "characters/hermione/face/auto.png" xpos h_xpos ypos h_ypos #Displays an autograph on her leg.
    if aftersperm: #Shows cum stains on Hermione's uniform.
        add "characters/hermione/face/auto_03.png" xpos h_xpos ypos h_ypos #Displays sperm.

    if custom_bra >=1 and badges and custom_outfit_old <= 0:
        if custom_bra == 1:
            add im.Alpha("images/25_mo/lace_bra.png", transparency) xpos h_xpos ypos h_ypos
        elif custom_bra == 2:
            add im.Alpha("images/25_mo/cup_bra.png", transparency) xpos h_xpos ypos h_ypos
        elif custom_bra == 3 and wear_shirts:
            add im.Alpha("images/25_mo/silk_bra.png", transparency) xpos h_xpos ypos h_ypos
        elif custom_bra == 3:
            add im.Alpha("images/25_mo/silk_bra_2.png", transparency) xpos h_xpos ypos h_ypos
    if display_h_tears:
        add u_tears_pic xpos h_xpos ypos h_ypos #Universal tears layer.

    if skirt_up == True:
        if wear_shirts and badges:
            add "characters/hermione/face/shirts/skirt_up.png" xpos h_xpos ypos h_ypos #Displays sperm.
        elif fingering == True:
            add "characters/hermione/face/shirts/skirt_up_3.png" xpos h_xpos ypos h_ypos #Displays sperm.
        else:
            add "characters/hermione/face/shirts/skirt_up_2.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif fingering == True and not wear_shirts:
        add "characters/hermione/face/shirts/fingering_06.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif book_hold and not wear_shirts:
        add "characters/hermione/face/shirts/book_04.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif badges and wear_shirts: #Determine what top she will wear
        if custom_shirt == True or custom_outfit_old >= 1 or custom_breast >= 1:
            if custom_outfit_old == 1 and not robeon:
                add im.Alpha("images/23_clothes_store/costumes/maid_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 2:
                add im.Alpha("images/23_clothes_store/costumes/cheer_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 3:
                add im.Alpha("images/23_clothes_store/costumes/s_cheer_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 4:
                add im.Alpha("images/23_clothes_store/costumes/heart_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 5:
                add im.Alpha("images/23_clothes_store/costumes/h_cheer_top_2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 6:
                add im.Alpha("images/25_mo/jumper.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 7:
                add im.Alpha("images/23_clothes_store/costumes/power_costume.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 7.2:
                add im.Alpha("images/23_clothes_store/costumes/power_costume_2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 8:
                add im.Alpha("images/23_clothes_store/costumes/marvel_top.png", transparency) xpos h_xpos ypos h_ypos
                add im.Alpha("images/23_clothes_store/costumes/marvel_sash.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 9:
                add im.Alpha("images/23_clothes_store/costumes/harley_top.png", transparency) xpos h_xpos ypos h_ypos
                add im.Alpha("images/23_clothes_store/costumes/harley_collar.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 10:
                add im.Alpha("images/23_clothes_store/costumes/ball_dress_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 11:
                add im.Alpha("images/23_clothes_store/costumes/christmas_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 12:
                add im.Alpha("images/23_clothes_store/costumes/lara_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_breast == 1:
                add "images/25_mo/tit_exp_1.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 2:
                add "images/25_mo/tit_exp_2.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 3:
                add "images/25_mo/tit_exp_3.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 4:
                add "images/25_mo/tit_exp_1.png" xpos h_xpos ypos h_ypos
                add "images/25_mo/expanded_shirt.png" xpos h_xpos ypos h_ypos
        else: 
            if book_hold == True and wear_shirts:
                if whoring <= 10:
                    add "characters/hermione/face/shirts/book_01.png" xpos h_xpos ypos h_ypos #Displays sperm.
                else:
                    add "characters/hermione/face/shirts/book_02.png" xpos h_xpos ypos h_ypos #Displays sperm.
            elif whoring <= 3:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_00.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_01.png" xpos h_xpos ypos h_ypos
            elif whoring >= 4 and whoring <= 7:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_01.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_02.png" xpos h_xpos ypos h_ypos
            elif whoring >= 8 and whoring <= 14:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_02.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_03.png" xpos h_xpos ypos h_ypos
            elif whoring >= 15 and whoring <= 20:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_03.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_04.png" xpos h_xpos ypos h_ypos
            elif whoring >= 21:
                if day_random <= 4:
                    if not fingering:
                        add im.Alpha("characters/hermione/face/shirts/shirt_04.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                    else:  
                        add "characters/hermione/face/shirts/fingering_05.png" xpos h_xpos ypos h_ypos    
                if day_random >= 5:
                    if not fingering:
                        add im.Alpha("characters/hermione/face/shirts/shirt_05.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
                    else:  
                        add "characters/hermione/face/shirts/fingering_00.png" xpos h_xpos ypos h_ypos   
                    if day_random >= 7 and lock_public_favors == False:
                        add "characters/hermione/face/auto_03.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif lift_shirt == True:
        add "characters/hermione/face/shirts/shirt_up.png" xpos h_xpos ypos h_ypos
    if collar >= 1 and badges:
        if collar == 1:
            add "characters/hermione/face/customs/collar_1.png" xpos h_xpos ypos h_ypos
        if collar == 2:
            add "characters/hermione/face/customs/collar_2.png" xpos h_xpos ypos h_ypos
        if collar == 3:
            add "characters/hermione/face/customs/collar_3.png" xpos h_xpos ypos h_ypos


    if custom_outfit_old == 7 or custom_outfit_old == 7.2:
        add "images/23_clothes_store/costumes/power_hair_2.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 9:
        add "images/23_clothes_store/costumes/harley_hair_2.png" xpos h_xpos ypos h_ypos
    elif hair_color >= 0:
        add "characters/hermione/face/body/head/"+str(hair_style)+"_"+str(hair_color)+"_2.png" xpos h_xpos ypos h_ypos
    
    
    if ears == True and hair_color >= 0:
        add "images/25_mo/ears_"+str(hair_color)+"_2.png" xpos h_xpos ypos h_ypos #The hair.  

    if glasses_worn:
        add "characters/hermione/face/glasses.png" xpos h_xpos ypos h_ypos #The glasses.

    if custom_outfit_old == 1:
        add "images/23_clothes_store/costumes/maid_hat.png" xpos h_xpos ypos h_ypos
        add "images/23_clothes_store/costumes/maid_gloves.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 4:
        add "images/23_clothes_store/costumes/heart_collar.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 8:
        add "images/23_clothes_store/costumes/marvel_gloves.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 9:
        add "images/23_clothes_store/costumes/harley_gloves.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 11:
        add "images/23_clothes_store/costumes/christmas_gloves.png" xpos h_xpos ypos h_ypos
        add "images/23_clothes_store/costumes/christmas_antlers.png" xpos h_xpos ypos h_ypos
        add "images/23_clothes_store/costumes/christmas_collar.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 12:
        add im.Alpha("images/23_clothes_store/costumes/lara_gloves.png", transparency) xpos h_xpos ypos h_ypos


    if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "characters/hermione/face/auto_02.png" xpos h_xpos ypos h_ypos #Displays sperm.
    if uni_sperm:
        add u_sperm xpos h_xpos ypos h_ypos #Universal sperm.        
    if badges and not robeon and custom_outfit_old == 0 and wear_shirts:
        if ba_01 and whoring <= 12:
            add "characters/hermione/face/badge.png" xpos h_xpos ypos h_ypos #The Robe.
        elif ba_01 and whoring >= 13:
            add "images/25_mo/cum_badge.png" xpos h_xpos ypos h_ypos
    if robeon:
        add "characters/hermione/face/robe.png" xpos h_xpos ypos h_ypos #The Robe.
    if robe == 1:
        add im.Alpha("characters/hermione/face/shirts/robe_00.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    elif robe == 2:
        add im.Alpha("characters/hermione/face/shirts/robe_01.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    elif robe == 3:
        add im.Alpha("characters/hermione/face/shirts/robe_02.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    elif robe == 4:
        add im.Alpha("characters/hermione/face/shirts/robe_03.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    if tentacle_cosmetic == True:
        add "images/25_mo/tentacles.png" xpos h_xpos ypos h_ypos #The Tentacles.
    
    
    if h_body.split("/")[-1].replace(".png","") in anger or emote_anger:
        add "characters/hermione/face/body/emote/00.png" xpos h_xpos ypos h_ypos #Custom
    if h_body.split("/")[-1].replace(".png","") in exclam or emote_exclam:
        add "characters/hermione/face/body/emote/01.png" xpos h_xpos ypos h_ypos #Custom
    if h_body.split("/")[-1].replace(".png","") in hearts or emote_hearts:
        add "characters/hermione/face/body/emote/02.png" xpos h_xpos ypos h_ypos #Custom
    if h_body.split("/")[-1].replace(".png","") in question or emote_question:
        add "characters/hermione/face/body/emote/03.png" xpos h_xpos ypos h_ypos #Custom
    if h_body.split("/")[-1].replace(".png","") in sweat or emote_sweat:
        add "characters/hermione/face/body/emote/04.png" xpos h_xpos ypos h_ypos #Custom
    if h_body.split("/")[-1].replace(".png","") in suprize or emote_suprize:
        add "characters/hermione/face/body/emote/05.png" xpos h_xpos ypos h_ypos #Custom
    
    zorder hermione_main_zorder #(5) Otherwise candle light is shown on top.


#From 19_my_screens.rpy
screen hermione_main2:
    
    add "characters/hermione/face/body/hermione_base.png" xpos h_xpos ypos h_ypos
    
    
    
    if custom_outfit_old == 7 or custom_outfit_old == 7.2:
        add "images/25_mo/power_hair.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 9:
        add "images/25_mo/harley_hair.png" xpos h_xpos ypos h_ypos
    elif hair_color >= 0:
        add "characters/hermione/face/body/head/"+str(hair_style)+"_"+str(hair_color)+".png" xpos h_xpos ypos h_ypos
    if ears == True and hair_color >= 0:
        add "images/25_mo/ears_"+str(hair_color)+".png" xpos h_xpos ypos h_ypos #The hair. 
    
    
    if leg_pos >= 0:
        add "characters/hermione/face/body/legs/legs_"+str(leg_pos)+".png" xpos h_xpos ypos h_ypos
    
    
    
    if right_arm_pos >= 0:
        add "characters/hermione/face/body/arms/right/right_"+str(right_arm_pos)+".png" xpos h_xpos ypos h_ypos
    
    
    
    if left_arm_pos >= 0:
        add "characters/hermione/face/body/arms/left/left_"+str(left_arm_pos)+".png" xpos h_xpos ypos h_ypos
    
    
    
    if her_breasts >= 0:
        add "characters/hermione/face/body/breasts/breasts_"+str(her_breasts)+".png" xpos h_xpos ypos h_ypos
    
    
    
    add h_body xpos h_xpos ypos h_ypos #Add her emotion
    
    

    
    
    # if lift_shirt == True or book_hold == True or skirt_up == True or fingering == True:
        # add "characters/hermione/face/customs/base_3.png" xpos h_xpos ypos h_ypos #Add her base 
    # elif transparency < 1 or not wear_shirts:
        # add "characters/hermione/face/customs/base.png" xpos h_xpos ypos h_ypos #Add her base 
    # elif transparency == 1:
        # add "characters/hermione/face/customs/base_2.png" xpos h_xpos ypos h_ypos #Add her base 

    if collar >= 1 and not badges:
        if collar == 1:
            add "characters/hermione/face/customs/collar_1.png" xpos h_xpos ypos h_ypos
        if collar == 2:
            add "characters/hermione/face/customs/collar_2.png" xpos h_xpos ypos h_ypos
        if collar == 3:
            add "characters/hermione/face/customs/collar_3.png" xpos h_xpos ypos h_ypos


    if freckles == True:
        add "images/25_mo/freckles.png" xpos h_xpos ypos h_ypos

    if not only_upper:
        add "characters/hermione/face/legs/base_01.png" xpos h_xpos ypos h_ypos #Add her legs

    if stockings == 1:
        add "images/25_mo/maid_stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 2:
        add "images/25_mo/cheer_stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 3:
        add "images/25_mo/stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 4:
        add "images/25_mo/s_cheer_stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 5:
        add "images/25_mo/h_cheer_stockings_2.png" xpos h_xpos ypos h_ypos
    else:
        if ne: # Desplays a fishnets in hermione_main screen.
            if ne_01:
                add "characters/hermione/face/nets.png" xpos h_xpos ypos h_ypos # FISHNETS.
                if not legs_02 and not only_upper and not legs_03: # Long skirt is on.
                    add "characters/hermione/face/patch.png" xpos h_xpos ypos h_ypos # Patch
    if fingering == True:
        add "characters/hermione/face/shirts/arm.png" xpos h_xpos ypos h_ypos
    if not only_upper:
        if whoring <= 12 or custom_bra >0 and panties:
            if custom_bra == 1:
                add im.Alpha("images/25_mo/lace_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_bra == 2:
                add im.Alpha("images/25_mo/cup_panties.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_bra == 3:
                add im.Alpha("images/25_mo/silk_pants.png", transparency) xpos h_xpos ypos h_ypos
            else:
                add im.Alpha("characters/hermione/face/legs/pants.png", transparency) xpos h_xpos ypos h_ypos

        if custom_skirt >= 1 or custom_outfit_old >= 1 and custom_outfit_old <= 19 and not skirt_up:
            if custom_outfit_old == 1:
                add im.Alpha("images/25_mo/maid_skirt.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 2:
                add im.Alpha("images/25_mo/cheer_pants.png", transparency) xpos h_xpos ypos h_ypos            
            elif custom_outfit_old == 3:
                add im.Alpha("images/25_mo/s_cheer_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 4:
                add im.Alpha("images/25_mo/heart_legs.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 5:
                add im.Alpha("images/25_mo/h_cheer_pants_2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 8:
                add im.Alpha("images/25_mo/marvel_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 9:
                add im.Alpha("images/25_mo/harley_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 10:
                add im.Alpha("images/25_mo/ball_dress_skirt.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 11:
                add im.Alpha("images/25_mo/christmas_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 12:
                add im.Alpha("images/25_mo/lara_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 1 and custom_outfit_old == 0:
                add im.Alpha("images/25_mo/jeans.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 2:
                add im.Alpha("images/25_mo/ass_exp1.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 3:
                add im.Alpha("images/25_mo/ass_exp2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 4:
                add im.Alpha("images/25_mo/snake.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 5 and custom_outfit_old == 0:
                add im.Alpha("images/23_clothes_store/existing_stock/jeans_short.png", transparency) xpos h_xpos ypos h_ypos
        elif not skirt_up and custom_outfit_old <= 19:
            if whoring <= 5:
                add im.Alpha("characters/hermione/face/legs/legs_01.png", transparency) xpos h_xpos ypos h_ypos
            elif whoring >= 6 and whoring <= 11: #Mini skirt.
                add im.Alpha("characters/hermione/face/legs/legs_02.png", transparency) xpos h_xpos ypos h_ypos
            elif whoring >= 12 and whoring <= 19: #Micro skirt.
                add im.Alpha("characters/hermione/face/legs/legs_03.png", transparency) xpos h_xpos ypos h_ypos
            elif whoring >= 20 and whoring <= 23: #Mini Micro skirt.
                add im.Alpha("characters/hermione/face/legs/legs_04.png", transparency) xpos h_xpos ypos h_ypos
            else: #Mini Mini Micro skirt.
                add im.Alpha("characters/hermione/face/legs/legs_05.png", transparency) xpos h_xpos ypos h_ypos
    if autograph:
        add "characters/hermione/face/auto.png" xpos h_xpos ypos h_ypos #Displays an autograph on her leg.
    if aftersperm: #Shows cum stains on Hermione's uniform.
        add "characters/hermione/face/auto_03.png" xpos h_xpos ypos h_ypos #Displays sperm.

    if custom_bra >=1 and badges and custom_outfit_old <= 0:
        if custom_bra == 1:
            add im.Alpha("images/25_mo/lace_bra.png", transparency) xpos h_xpos ypos h_ypos
        elif custom_bra == 2:
            add im.Alpha("images/25_mo/cup_bra.png", transparency) xpos h_xpos ypos h_ypos
        elif custom_bra == 3 and wear_shirts:
            add im.Alpha("images/25_mo/silk_bra.png", transparency) xpos h_xpos ypos h_ypos
        elif custom_bra == 3:
            add im.Alpha("images/25_mo/silk_bra_2.png", transparency) xpos h_xpos ypos h_ypos
    if display_h_tears:
        add u_tears_pic xpos h_xpos ypos h_ypos #Universal tears layer.

    if skirt_up == True:
        if wear_shirts and badges:
            add "characters/hermione/face/shirts/skirt_up.png" xpos h_xpos ypos h_ypos #Displays sperm.
        elif fingering == True:
            add "characters/hermione/face/shirts/skirt_up_3.png" xpos h_xpos ypos h_ypos #Displays sperm.
        else:
            add "characters/hermione/face/shirts/skirt_up_2.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif fingering == True and not wear_shirts:
        add "characters/hermione/face/shirts/fingering_06.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif book_hold and not wear_shirts:
        add "characters/hermione/face/shirts/book_04.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif badges and wear_shirts: #Determine what top she will wear
        if custom_shirt == True or custom_outfit_old >= 1 or custom_breast >= 1:
            if custom_outfit_old == 1 and not robeon:
                add im.Alpha("images/25_mo/maid_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 2:
                add im.Alpha("images/25_mo/cheer_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 3:
                add im.Alpha("images/25_mo/s_cheer_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 4:
                add im.Alpha("images/25_mo/heart_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 5:
                add im.Alpha("images/25_mo/h_cheer_top_2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 6:
                add im.Alpha("images/25_mo/jumper.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 7:
                add im.Alpha("images/25_mo/power_costume.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 7.2:
                add im.Alpha("images/25_mo/power_costume_2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 8:
                add im.Alpha("images/25_mo/marvel_top.png", transparency) xpos h_xpos ypos h_ypos
                add im.Alpha("images/25_mo/marvel_sash.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 9:
                add im.Alpha("images/25_mo/harley_top.png", transparency) xpos h_xpos ypos h_ypos
                add im.Alpha("images/25_mo/harley_collar.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 10:
                add im.Alpha("images/25_mo/ball_dress_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 11:
                add im.Alpha("images/25_mo/christmas_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 12:
                add im.Alpha("images/25_mo/lara_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_breast == 1:
                add "images/25_mo/tit_exp_1.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 2:
                add "images/25_mo/tit_exp_2.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 3:
                add "images/25_mo/tit_exp_3.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 4:
                add "images/25_mo/tit_exp_1.png" xpos h_xpos ypos h_ypos
                add "images/25_mo/expanded_shirt.png" xpos h_xpos ypos h_ypos
        else: 
            if book_hold == True and wear_shirts:
                if whoring <= 10:
                    add "characters/hermione/face/shirts/book_01.png" xpos h_xpos ypos h_ypos #Displays sperm.
                else:
                    add "characters/hermione/face/shirts/book_02.png" xpos h_xpos ypos h_ypos #Displays sperm.
            elif whoring <= 3:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_00.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_01.png" xpos h_xpos ypos h_ypos
            elif whoring >= 4 and whoring <= 7:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_01.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_02.png" xpos h_xpos ypos h_ypos
            elif whoring >= 8 and whoring <= 14:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_02.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_03.png" xpos h_xpos ypos h_ypos
            elif whoring >= 15 and whoring <= 20:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_03.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_04.png" xpos h_xpos ypos h_ypos
            elif whoring >= 21:
                if day_random <= 4:
                    if not fingering:
                        add im.Alpha("characters/hermione/face/shirts/shirt_04.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                    else:  
                        add "characters/hermione/face/shirts/fingering_05.png" xpos h_xpos ypos h_ypos    
                if day_random >= 5:
                    if not fingering:
                        add im.Alpha("characters/hermione/face/shirts/shirt_05.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
                    else:  
                        add "characters/hermione/face/shirts/fingering_00.png" xpos h_xpos ypos h_ypos   
                    if day_random >= 7 and lock_public_favors == False:
                        add "characters/hermione/face/auto_03.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif lift_shirt == True:
        add "characters/hermione/face/shirts/shirt_up.png" xpos h_xpos ypos h_ypos
    if collar >= 1 and badges:
        if collar == 1:
            add "characters/hermione/face/customs/collar_1.png" xpos h_xpos ypos h_ypos
        if collar == 2:
            add "characters/hermione/face/customs/collar_2.png" xpos h_xpos ypos h_ypos
        if collar == 3:
            add "characters/hermione/face/customs/collar_3.png" xpos h_xpos ypos h_ypos


    if custom_outfit_old == 7 or custom_outfit_old == 7.2:
        add "images/25_mo/power_hair_2.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 9:
        add "images/25_mo/harley_hair_2.png" xpos h_xpos ypos h_ypos
    elif hair_color >= 0:
        add "characters/hermione/face/body/head/"+str(hair_style)+"_"+str(hair_color)+"_2.png" xpos h_xpos ypos h_ypos
    
    
    if ears == True and hair_color >= 0:
        add "images/25_mo/ears_"+str(hair_color)+"_2.png" xpos h_xpos ypos h_ypos #The hair. 
    
    
    if glasses_worn:
        add "characters/hermione/face/glasses.png" xpos h_xpos ypos h_ypos #The glasses.

    if custom_outfit_old == 1:
        add "images/25_mo/maid_hat.png" xpos h_xpos ypos h_ypos
        add "images/25_mo/maid_gloves.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 4:
        add "images/25_mo/heart_collar.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 8:
        add "images/25_mo/marvel_gloves.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 9:
        add "images/25_mo/harley_gloves.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 11:
        add "images/25_mo/christmas_gloves.png" xpos h_xpos ypos h_ypos
        add "images/25_mo/christmas_antlers.png" xpos h_xpos ypos h_ypos
        add "images/25_mo/christmas_collar.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 12:
        add im.Alpha("images/25_mo/lara_gloves.png", transparency) xpos h_xpos ypos h_ypos

    if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "characters/hermione/face/auto_02.png" xpos h_xpos ypos h_ypos #Displays sperm.
    if uni_sperm:
        add u_sperm xpos h_xpos ypos h_ypos #Universal sperm.        
    if badges and not robeon and custom_outfit_old == 0 and wear_shirts:
        if ba_01 and whoring <= 12:
            add "characters/hermione/face/badge.png" xpos h_xpos ypos h_ypos #The Robe.
        elif ba_01 and whoring >= 13:
            add "images/25_mo/cum_badge.png" xpos h_xpos ypos h_ypos
    if robeon:
        add "characters/hermione/face/robe.png" xpos h_xpos ypos h_ypos #The Robe.
    if robe == 1:
        add im.Alpha("characters/hermione/face/shirts/robe_00.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    elif robe == 2:
        add im.Alpha("characters/hermione/face/shirts/robe_01.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    elif robe == 3:
        add im.Alpha("characters/hermione/face/shirts/robe_02.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    elif robe == 4:
        add im.Alpha("characters/hermione/face/shirts/robe_03.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    if tentacle_cosmetic == True:
        add "images/25_mo/tentacles.png" xpos h_xpos ypos h_ypos #The Tentacles.
    
    if face_exp in anger or emote_anger:
        add "characters/hermione/face/body/emote/00.png" xpos main_scr_xpos ypos main_scr_ypos #Custom
    if face_exp in exclam or emote_exclam:
        add "characters/hermione/face/body/emote/01.png" xpos main_scr_xpos ypos main_scr_ypos #Custom
    if face_exp in hearts or emote_hearts:
        add "characters/hermione/face/body/emote/02.png" xpos main_scr_xpos ypos main_scr_ypos #Custom
    if face_exp in question or emote_question:
        add "characters/hermione/face/body/emote/03.png" xpos main_scr_xpos ypos main_scr_ypos #Custom
    if face_exp in sweat or emote_sweat:
        add "characters/hermione/face/body/emote/04.png" xpos main_scr_xpos ypos main_scr_ypos #Custom
    if face_exp in suprize or emote_suprize:
        add "characters/hermione/face/body/emote/05.png" xpos main_scr_xpos ypos main_scr_ypos #Custom
        
    zorder hermione_main_zorder #(5) Otherwise candle light is shown on top.
#

#From 19_my_screens

### HERMIONE HEAD ONLY ###
screen h_head: #Screen that shows a full sprite of HERMIONE.
    tag head
    if not only_upper:
        add "characters/hermione/face/legs_01.png" xpos h_xpos ypos h_ypos
    
    if custom_outfit_old == 7 or custom_outfit_old == 7.2:
        add "images/25_mo/power_hair.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 9:
        add "images/25_mo/harley_hair.png" xpos h_xpos ypos h_ypos
    elif hair_color == 0:
        add "characters/hermione/face/hair/hair_00.png" xpos h_xpos ypos h_ypos #The hair.    
    elif hair_color == 1:
        add "characters/hermione/face/hair/hair_01.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 2:
        add "characters/hermione/face/hair/hair_02.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 3:
        add "characters/hermione/face/hair/hair_03.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 4:
        add "characters/hermione/face/hair/hair_04.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 5:
        add "characters/hermione/face/hair/hair_05.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 6:
        add "characters/hermione/face/hair/hair_06.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 7:
        add "characters/hermione/face/hair/hair_07.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 8:
        add "characters/hermione/face/hair/hair_08.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 9:
        add "characters/hermione/face/hair/hair_09.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 10:
        add "characters/hermione/face/hair/hair_10.png" xpos h_xpos ypos h_ypos #The hair.

    if ears == True and hair_color == 0:
        add "images/25_mo/ears_0.png" xpos h_xpos ypos h_ypos #The hair.    
    
    if ears == True and hair_color == 1:
        add "images/25_mo/ears_1.png" xpos h_xpos ypos h_ypos #The hair.   
    
    if ears == True and hair_color == 2:
        add "images/25_mo/ears_2.png" xpos h_xpos ypos h_ypos #The hair.   

    if ears == True and hair_color == 3:
        add "images/25_mo/ears_3.png" xpos h_xpos ypos h_ypos #The hair.   

    if ears == True and hair_color == 6:
        add "images/25_mo/ears_6.png" xpos h_xpos ypos h_ypos #The hair.   

    if transparency < 1 and badges or not wear_shirts:
        add "characters/hermione/face/customs/base.png" xpos h_xpos ypos h_ypos #Add her base 

    if collar >= 1 and badges:
        if collar == 1:
            add "characters/hermione/face/customs/collar_1.png" xpos h_xpos ypos h_ypos
        if collar == 2:
            add "characters/hermione/face/customs/collar_2.png" xpos h_xpos ypos h_ypos
        if collar == 3:
            add "characters/hermione/face/customs/collar_3.png" xpos h_xpos ypos h_ypos

    add h_body xpos h_xpos ypos h_ypos

    if freckles == True:
        add "images/25_mo/freckles.png" xpos h_xpos ypos h_ypos

    if display_h_tears:
        add u_tears_pic xpos h_xpos ypos h_ypos #Universal tears layer.
    if not badges and level == "01":
        add "characters/hermione/face/shirts/shirt_00.png" xpos h_xpos ypos h_ypos #The shirts.
    if badges and wear_shirts: #Determine what top she will wear
        if custom_shirt == True or custom_outfit_old >= 1 or custom_breast >= 1:
            if custom_outfit_old == 1 and not robeon:
                add im.Alpha("images/25_mo/maid_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 2:
                add im.Alpha("images/25_mo/cheer_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 3:
                add im.Alpha("images/25_mo/s_cheer_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 4:
                add im.Alpha("images/25_mo/heart_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 5:
                add im.Alpha("images/25_mo/h_cheer_top_2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 6:
                add im.Alpha("images/25_mo/jumper.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 7:
                add im.Alpha("images/25_mo/power_costume.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 8:
                add im.Alpha("images/25_mo/marvel_top.png", transparency) xpos h_xpos ypos h_ypos
                add im.Alpha("images/25_mo/marvel_sash.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 9:
                add im.Alpha("images/25_mo/harley_top.png", transparency) xpos h_xpos ypos h_ypos
                add im.Alpha("images/25_mo/harley_collar.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 10:
                add im.Alpha("images/25_mo/ball_dress_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 11:
                add im.Alpha("images/25_mo/christmas_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit_old == 12:
                add im.Alpha("images/25_mo/lara_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_breast == 1:
                add "images/25_mo/tit_exp_1.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 2:
                add "images/25_mo/tit_exp_2.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 3:
                add "images/25_mo/tit_exp_3.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 4:
                add "images/25_mo/tit_exp_1.png" xpos h_xpos ypos h_ypos
                add "images/25_mo/expanded_shirt.png" xpos h_xpos ypos h_ypos
        else: 
            if book_hold == True and wear_shirts:
                if whoring <= 10:
                    add "characters/hermione/face/shirts/book_01.png" xpos h_xpos ypos h_ypos #Displays sperm.
                else:
                    add "characters/hermione/face/shirts/book_02.png" xpos h_xpos ypos h_ypos #Displays sperm.
            elif whoring <= 3:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_00.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_01.png" xpos h_xpos ypos h_ypos
            elif whoring >= 4 and whoring <= 7:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_01.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_02.png" xpos h_xpos ypos h_ypos
            elif whoring >= 8 and whoring <= 14:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_02.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_03.png" xpos h_xpos ypos h_ypos
            elif whoring >= 15 and whoring <= 20:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_03.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_04.png" xpos h_xpos ypos h_ypos
            elif whoring >= 21:
                if day_random <= 4:
                    if not fingering:
                        add im.Alpha("characters/hermione/face/shirts/shirt_04.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                    else:  
                        add "characters/hermione/face/shirts/fingering_05.png" xpos h_xpos ypos h_ypos    
                if day_random >= 5:
                    if not fingering:
                        add im.Alpha("characters/hermione/face/shirts/shirt_05.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
                    else:  
                        add "characters/hermione/face/shirts/fingering_00.png" xpos h_xpos ypos h_ypos   
                    if day_random >= 7 and lock_public_favors == False:
                        add "characters/hermione/face/auto_03.png" xpos h_xpos ypos h_ypos #Displays sperm.
    if collar >= 1 and badges:
        if collar == 1:
            add "characters/hermione/face/customs/collar_1.png" xpos h_xpos ypos h_ypos
        if collar == 2:
            add "characters/hermione/face/customs/collar_2.png" xpos h_xpos ypos h_ypos
        if collar == 3:
            add "characters/hermione/face/customs/collar_3.png" xpos h_xpos ypos h_ypos
    if custom_outfit_old == 1:
        add "images/25_mo/maid_hat.png" xpos h_xpos ypos h_ypos
        add "images/25_mo/maid_gloves.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 4:
        add "images/25_mo/heart_collar.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 8:
        add "images/25_mo/marvel_gloves.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 9:
        add "images/25_mo/harley_gloves.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 11:
        add "images/25_mo/christmas_gloves.png" xpos h_xpos ypos h_ypos
        add "images/25_mo/christmas_antlers.png" xpos h_xpos ypos h_ypos
        add "images/25_mo/christmas_collar.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 12:
        add im.Alpha("images/25_mo/lara_gloves.png", transparency) xpos h_xpos ypos h_ypos

    if robeon:
        add "characters/hermione/face/robe.png" xpos h_xpos ypos h_ypos #The Robe.
    if badges:
        if ba_01 and whoring <= 12:
            add "characters/hermione/face/badge.png" xpos h_xpos ypos h_ypos #The Robe.
        elif ba_01 and whoring >= 13:
            add "images/25_mo/cum_badge.png" xpos h_xpos ypos h_ypos

    if custom_outfit_old == 7 or custom_outfit_old == 7.2:
        add "images/25_mo/power_hair_2.png" xpos h_xpos ypos h_ypos
    elif custom_outfit_old == 9:
        add "images/25_mo/harley_hair_2.png" xpos h_xpos ypos h_ypos
    elif hair_color == 0:
        add "characters/hermione/face/hair/hair_00_2.png" xpos h_xpos ypos h_ypos #The hair.    
    elif hair_color == 1:
        add "characters/hermione/face/hair/hair_01_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 2:
        add "characters/hermione/face/hair/hair_02_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 3:
        add "characters/hermione/face/hair/hair_03_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 4:
        add "characters/hermione/face/hair/hair_04_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 5:
        add "characters/hermione/face/hair/hair_05_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 6:
        add "characters/hermione/face/hair/hair_06_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 7:
        add "characters/hermione/face/hair/hair_07_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 8:
        add "characters/hermione/face/hair/hair_08_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 9:
        add "characters/hermione/face/hair/hair_09_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 10:
        add "characters/hermione/face/hair/hair_10_2.png" xpos h_xpos ypos h_ypos #The hair.    

    if glasses_worn:
        add "characters/hermione/face/glasses.png" xpos h_xpos ypos h_ypos #The glasses.
    if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "characters/hermione/face/auto_02.png" xpos h_xpos ypos h_ypos #Displays sperm.
    if aftersperm: #Shows cum stains on Hermione's uniform.
        add "characters/hermione/face/auto_03.png" xpos h_xpos ypos h_ypos #Displays sperm.
    if uni_sperm:
        add u_sperm xpos h_xpos ypos h_ypos #Universal sperm.
    if ne: # Desplays a fishnets in hermione_main screen.
        if ne_01:
            add "characters/hermione/face/nets.png" xpos h_xpos ypos h_ypos #The Robe.

    if tiara:
        add "characters/hermione/face/auto_09.png" xpos h_xpos ypos h_ypos # Tiara
    if tentacle_cosmetic == True:
        add "images/25_mo/tentacles.png" xpos h_xpos ypos h_ypos #The Tentacles.
        
    
    if h_body.split("/")[-1].replace(".png","") in anger or emote_anger:
        add "characters/hermione/face/body/emote/00.png" xpos her_head_xpos ypos her_head_ypos #Custom
    if h_body.split("/")[-1].replace(".png","") in exclam or emote_exclam:
        add "characters/hermione/face/body/emote/01.png" xpos her_head_xpos ypos her_head_ypos #Custom
    if h_body.split("/")[-1].replace(".png","") in hearts or emote_hearts:
        add "characters/hermione/face/body/emote/02.png" xpos her_head_xpos ypos her_head_ypos #Custom
    if h_body.split("/")[-1].replace(".png","") in question or emote_question:
        add "characters/hermione/face/body/emote/03.png" xpos her_head_xpos ypos her_head_ypos #Custom
    if h_body.split("/")[-1].replace(".png","") in sweat or emote_sweat:
        add "characters/hermione/face/body/emote/04.png" xpos her_head_xpos ypos her_head_ypos #Custom
    if h_body.split("/")[-1].replace(".png","") in suprize or emote_suprize:
        add "characters/hermione/face/body/emote/05.png" xpos her_head_xpos ypos her_head_ypos #Custom
    
        
        
    zorder 8
    
#

#From 19_my_screens
 
screen h_head2: #Screen that shows Hermione's head.
    tag head
    if custom_outfit_old == 7 or custom_outfit_old == 7.2:
        add "images/25_mo/power_hair.png" xpos her_head_xpos ypos her_head_ypos
    elif custom_outfit_old == 9:
        add "images/25_mo/harley_hair.png" xpos her_head_xpos ypos her_head_ypos
    elif hair_color >= 0:
        add "characters/hermione/face/body/head/"+str(hair_style)+"_"+str(hair_color)+".png" xpos her_head_xpos ypos her_head_ypos
    if ears == True and hair_color >= 0:
        add "images/25_mo/ears_"+str(hair_color)+".png" xpos her_head_xpos ypos her_head_ypos #The hair. 
    

    if transparency < 1 and badges:
        add "characters/hermione/face/customs/base.png" xpos her_head_xpos ypos her_head_ypos #Add her base 

    if transparency == 1 and badges:
        add "characters/hermione/face/customs/base_2.png" xpos her_head_xpos ypos her_head_ypos #Add her base 

    if collar >= 1 and not badges:
        if collar == 1:
            add "characters/hermione/face/customs/collar_1.png" xpos her_head_xpos ypos her_head_ypos
        if collar == 2:
            add "characters/hermione/face/customs/collar_2.png" xpos her_head_xpos ypos her_head_ypos
        if collar == 3:
            add "characters/hermione/face/customs/collar_3.png" xpos her_head_xpos ypos her_head_ypos

    add h_body xpos her_head_xpos ypos her_head_ypos #Add her emotion

    if freckles == True:
        add "images/25_mo/freckles.png" xpos her_head_xpos ypos her_head_ypos

    if not only_upper:
        add "characters/hermione/face/legs/base_01.png" xpos her_head_xpos ypos her_head_ypos #Add her legs

    if stockings == 1:
        add "images/25_mo/maid_stockings.png" xpos her_head_xpos ypos her_head_ypos
    elif stockings == 2:
        add "images/25_mo/cheer_stockings.png" xpos her_head_xpos ypos her_head_ypos
    elif stockings == 3:
        add "images/25_mo/stockings.png" xpos her_head_xpos ypos her_head_ypos
    else:
        if ne: # Desplays a fishnets in hermione_main screen.
            if ne_01:
                add "characters/hermione/face/nets.png" xpos her_head_xpos ypos her_head_ypos # FISHNETS.
                ##if not legs_02 and not only_upper and not legs_03: # Long skirt is on.
                ##    add "characters/hermione/face/patch.png" xpos her_head_xpos ypos her_head_ypos # Patch
    
    if not only_upper:
        if whoring <= 12 or custom_bra >=0:
            if custom_bra == 1:
                add im.Alpha("images/25_mo/lace_pants.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_bra == 3:
                add im.Alpha("images/25_mo/silk_pants.png", transparency) xpos her_head_xpos ypos her_head_ypos
            else:
                add im.Alpha("characters/hermione/face/legs/pants.png", transparency) xpos her_head_xpos ypos her_head_ypos
        if custom_skirt >= 1 or custom_outfit_old >= 1:
            if custom_outfit_old == 1:
                add im.Alpha("images/25_mo/maid_skirt.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit_old == 2:
                add im.Alpha("images/25_mo/cheer_pants.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_skirt == 1 and custom_outfit_old == 0:
                add im.Alpha("images/25_mo/jeans.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_skirt == 2:
                add im.Alpha("images/25_mo/jeans_2.png", transparency) xpos her_head_xpos ypos her_head_ypos
        else:
            if whoring <= 5:
                add im.Alpha("characters/hermione/face/legs/legs_01.png", transparency) xpos her_head_xpos ypos her_head_ypos
            if whoring >= 6 and whoring <= 11: #Mini skirt.
                add im.Alpha("characters/hermione/face/legs/legs_02.png", transparency) xpos her_head_xpos ypos her_head_ypos
            if whoring >= 12 and whoring <= 19: #Micro skirt.
                add im.Alpha("characters/hermione/face/legs/legs_03.png", transparency) xpos her_head_xpos ypos her_head_ypos
            if whoring >= 20: #Mini Micro skirt.
                add im.Alpha("characters/hermione/face/legs/legs_04.png", transparency) xpos her_head_xpos ypos her_head_ypos
    if autograph:
        add "characters/hermione/face/auto.png" xpos her_head_xpos ypos her_head_ypos #Displays an autograph on her leg.
    if aftersperm: #Shows cum stains on Hermione's uniform.
        add "characters/hermione/face/auto_03.png" xpos her_head_xpos ypos her_head_ypos #Displays sperm.


    if custom_bra >=1 and badges and custom_outfit_old <= 0:
        if custom_bra == 1:
            add im.Alpha("images/25_mo/lace_bra.png", transparency) xpos her_head_xpos ypos her_head_ypos
        elif custom_bra == 2:
            add im.Alpha("characters/hermione/face/shirts/bra_01.png", transparency) xpos her_head_xpos ypos her_head_ypos
        elif custom_bra == 3:
            add im.Alpha("images/25_mo/silk_bra.png", transparency) xpos her_head_xpos ypos her_head_ypos
    if display_h_tears:
        add u_tears_pic xpos her_head_xpos ypos her_head_ypos #Universal tears layer.


    if badges and wear_shirts: #Determine what top she will wear
        if custom_shirt == True or custom_outfit_old >= 1 or custom_breast >= 1:
            if custom_outfit_old == 1 and not robeon:
                add im.Alpha("images/25_mo/maid_top.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit_old == 2:
                add im.Alpha("images/25_mo/cheer_top.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit_old == 3:
                add im.Alpha("images/25_mo/s_cheer_top.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit_old == 4:
                add im.Alpha("images/25_mo/heart_top.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit_old == 5:
                add im.Alpha("images/25_mo/h_cheer_top_2.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit_old == 6:
                add im.Alpha("images/25_mo/jumper.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit_old == 7:
                add im.Alpha("images/25_mo/power_costume.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit_old == 8:
                add im.Alpha("images/25_mo/marvel_top.png", transparency) xpos her_head_xpos ypos her_head_ypos
                add im.Alpha("images/25_mo/marvel_sash.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit_old == 9:
                add im.Alpha("images/25_mo/harley_top.png", transparency) xpos her_head_xpos ypos her_head_ypos
                add im.Alpha("images/25_mo/harley_collar.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit_old == 10:
                add im.Alpha("images/25_mo/ball_dress_top.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit_old == 11:
                add im.Alpha("images/25_mo/christmas_top.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit_old == 12:
                add im.Alpha("images/25_mo/lara_top.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_breast == 1:
                add "images/25_mo/tit_exp_1.png" xpos her_head_xpos ypos her_head_ypos
            elif custom_breast == 2:
                add "images/25_mo/tit_exp_2.png" xpos her_head_xpos ypos her_head_ypos
            elif custom_breast == 3:
                add "images/25_mo/tit_exp_3.png" xpos her_head_xpos ypos her_head_ypos
            elif custom_breast == 4:
                add "images/25_mo/tit_exp_1.png" xpos her_head_xpos ypos her_head_ypos
                add "images/25_mo/expanded_shirt.png" xpos her_head_xpos ypos her_head_ypos
        else: 
            if book_hold == True and wear_shirts:
                if whoring <= 10:
                    add "characters/hermione/face/shirts/book_01.png" xpos her_head_xpos ypos her_head_ypos #Displays sperm.
                else:
                    add "characters/hermione/face/shirts/book_02.png" xpos her_head_xpos ypos her_head_ypos #Displays sperm.
            elif whoring <= 3:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_00.png", transparency) xpos her_head_xpos ypos her_head_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_01.png" xpos her_head_xpos ypos her_head_ypos
            elif whoring >= 4 and whoring <= 7:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_01.png", transparency) xpos her_head_xpos ypos her_head_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_02.png" xpos her_head_xpos ypos her_head_ypos
            elif whoring >= 8 and whoring <= 14:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_02.png", transparency) xpos her_head_xpos ypos her_head_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_03.png" xpos her_head_xpos ypos her_head_ypos
            elif whoring >= 15 and whoring <= 20:
                if not fingering:
                    add im.Alpha("characters/hermione/face/shirts/shirt_03.png", transparency) xpos her_head_xpos ypos her_head_ypos #The shirts.
                else:  
                    add "characters/hermione/face/shirts/fingering_04.png" xpos her_head_xpos ypos her_head_ypos
            elif whoring >= 21:
                if day_random <= 4:
                    if not fingering:
                        add im.Alpha("characters/hermione/face/shirts/shirt_04.png", transparency) xpos her_head_xpos ypos her_head_ypos #The shirts.
                    else:  
                        add "characters/hermione/face/shirts/fingering_05.png" xpos her_head_xpos ypos her_head_ypos    
                if day_random >= 5:
                    if not fingering:
                        add im.Alpha("characters/hermione/face/shirts/shirt_05.png", transparency) xpos her_head_xpos ypos her_head_ypos #The shirts. 
                    else:  
                        add "characters/hermione/face/shirts/fingering_00.png" xpos her_head_xpos ypos her_head_ypos   
                    if day_random >= 7 and lock_public_favors == False:
                        add "characters/hermione/face/auto_03.png" xpos her_head_xpos ypos her_head_ypos #Displays sperm.
    if collar >= 1 and badges:
        if collar == 1:
            add "characters/hermione/face/customs/collar_1.png" xpos her_head_xpos ypos her_head_ypos
        if collar == 2:
            add "characters/hermione/face/customs/collar_2.png" xpos her_head_xpos ypos her_head_ypos
        if collar == 3:
            add "characters/hermione/face/customs/collar_3.png" xpos her_head_xpos ypos her_head_ypos

    if custom_outfit_old == 7 or custom_outfit_old == 7.2:
        add "images/25_mo/power_hair_2.png" xpos her_head_xpos ypos her_head_ypos
    elif custom_outfit_old == 9:
        add "images/25_mo/harley_hair_2.png" xpos her_head_xpos ypos her_head_ypos
    elif hair_color >= 0:
        add "characters/hermione/face/body/head/"+str(hair_style)+"_"+str(hair_color)+"_2.png" xpos her_head_xpos ypos her_head_ypos
    
    
    if ears == True and hair_color >= 0:
        add "images/25_mo/ears_"+str(hair_color)+"_2.png" xpos her_head_xpos ypos her_head_ypos #The hair.  
   

    if glasses_worn:
        add "characters/hermione/face/glasses.png" xpos her_head_xpos ypos her_head_ypos #The glasses.

    if custom_outfit_old == 1:
        add "images/25_mo/maid_hat.png" xpos her_head_xpos ypos her_head_ypos
        add "images/25_mo/maid_gloves.png" xpos her_head_xpos ypos her_head_ypos
    elif custom_outfit_old == 4:
        add "images/25_mo/heart_collar.png" xpos her_head_xpos ypos her_head_ypos
    elif custom_outfit_old == 8:
        add "images/25_mo/marvel_gloves.png" xpos her_head_xpos ypos her_head_ypos
    elif custom_outfit_old == 9:
        add "images/25_mo/harley_gloves.png" xpos her_head_xpos ypos her_head_ypos
    elif custom_outfit_old == 11:
        add "images/25_mo/christmas_gloves.png" xpos her_head_xpos ypos her_head_ypos
        add "images/25_mo/christmas_antlers.png" xpos her_head_xpos ypos her_head_ypos
        add "images/25_mo/christmas_collar.png" xpos her_head_xpos ypos her_head_ypos
    elif custom_outfit_old == 12:
        add im.Alpha("images/25_mo/lara_pants.png", transparency) xpos her_head_xpos ypos her_head_ypos
        
    if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "characters/hermione/face/auto_02.png" xpos her_head_xpos ypos her_head_ypos #Displays sperm.
    if uni_sperm:
        add u_sperm xpos her_head_xpos ypos her_head_ypos #Universal sperm.        
    if badges and not robeon and custom_outfit_old == 0:
        if ba_01 and whoring <= 12:
            add "characters/hermione/face/badge.png" xpos her_head_xpos ypos her_head_ypos #The Robe.
        elif ba_01 and whoring >= 13:
            add "images/25_mo/cum_badge.png" xpos her_head_xpos ypos her_head_ypos
    if robeon:
        add "characters/hermione/face/robe.png" xpos her_head_xpos ypos her_head_ypos #The Robe.
    if tentacle_cosmetic == True:
        add "images/25_mo/tentacles.png" xpos her_head_xpos ypos her_head_ypos #The Tentacles.
    
    
    if h_body.split("/")[-1].replace(".png","") in anger or emote_anger:
        add "characters/hermione/face/body/emote/00.png" xpos her_head_xpos+140 ypos her_head_ypos #Custom
    if h_body.split("/")[-1].replace(".png","") in exclam or emote_exclam:
        add "characters/hermione/face/body/emote/01.png" xpos her_head_xpos+140 ypos her_head_ypos #Custom
    if h_body.split("/")[-1].replace(".png","") in hearts or emote_hearts:
        add "characters/hermione/face/body/emote/02.png" xpos her_head_xpos+140 ypos her_head_ypos #Custom
    if h_body.split("/")[-1].replace(".png","") in question or emote_question:
        add "characters/hermione/face/body/emote/03.png" xpos her_head_xpos+140 ypos her_head_ypos #Custom
    if h_body.split("/")[-1].replace(".png","") in sweat or emote_sweat:
        add "characters/hermione/face/body/emote/04.png" xpos her_head_xpos+140 ypos her_head_ypos #Custom
    if h_body.split("/")[-1].replace(".png","") in suprize or emote_suprize:
        add "characters/hermione/face/body/emote/05.png" xpos her_head_xpos+140 ypos her_head_ypos #Custom
    
    zorder 8  
    
#

#From 19_my_screens
screen custom_character_1: #Screen that shows a full sprite of Susan
    #tag susan_main
    add "images/24_custom_characters/custom_character_1/hair/hair_00.png" xpos h_xpos+140 ypos h_ypos #Add the hair.
    add custom_character_1_emo xpos h_xpos+140 ypos h_ypos #Add the emotion.
    if not only_upper:
        add "images/24_custom_characters/custom_character_1/legs/base_01.png" xpos h_xpos+140 ypos h_ypos #Add the legs.
        add "images/24_custom_characters/custom_character_1/legs/legs_02.png" xpos h_xpos+140 ypos h_ypos #Add the legs.
    add "images/24_custom_characters/custom_character_1/shirts/shirt_00.png" xpos h_xpos+140 ypos h_ypos #Add the shirt.
    zorder 5 #(5) Otherwise candle light is shown on top.
 
screen custom_character_2: #Screen that shows a full sprite of Cho
    #tag cho_main
    add "images/24_custom_characters/custom_character_2/hair/hair_00.png" xpos h_xpos+140 ypos h_ypos #Add the hair.
    add custom_character_2_emo xpos h_xpos+140 ypos h_ypos #Add the emotion.
    if not only_upper:
        add "images/24_custom_characters/custom_character_2/legs/base_01.png" xpos h_xpos+140 ypos h_ypos #Add the legs.
        add "images/24_custom_characters/custom_character_2/legs/legs_03.png" xpos h_xpos+140 ypos h_ypos #Add the legs.
    add "images/24_custom_characters/custom_character_2/shirts/shirt_00.png" xpos h_xpos+140 ypos h_ypos #Add the shirt.
    zorder 5 #(5) Otherwise candle light is shown on top.
   
screen custom_character_3: #Screen that shows a full sprite of Astoria
    #tag astoria_main
    add "images/24_custom_characters/custom_character_3/hair/hair_00.png" xpos h_xpos+140 ypos h_ypos #Add the hair.
    add custom_character_3_emo xpos h_xpos+140 ypos h_ypos #Add the emotion.
    if not only_upper:
        add "images/24_custom_characters/custom_character_3/legs/base_01.png" xpos h_xpos+140 ypos h_ypos #Add the legs.
        add "images/24_custom_characters/custom_character_3/legs/legs_04.png" xpos h_xpos+140 ypos h_ypos #Add the legs.
    add "images/24_custom_characters/custom_character_3/shirts/shirt_00.png" xpos h_xpos+140 ypos h_ypos #Add the shirt.
    zorder 5 #(5) Otherwise candle light is shown on top.
    
#




