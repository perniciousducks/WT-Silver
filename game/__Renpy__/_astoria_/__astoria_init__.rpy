

label astoria_init:

    if not hasattr(renpy.store,'astoria_base') or reset_persistants:

        #Body
        $ astoria_base                = "characters/astoria/body/base/base_01.png" 
        $ astoria_l_arm               = "characters/astoria/body/arms/hip_l.png" 
        $ astoria_r_arm               = "characters/astoria/body/arms/hip_r.png" 
        $ astoria_l_hand              = "characters/astoria/body/arms/hip_l_top.png" 
        $ astoria_r_hand              = "characters/astoria/body/arms/hip_r_top.png" 
        $ astoria_hair                = "characters/astoria/body/hair/hair_1_base.png" 
        $ astoria_hair_shadow         = "characters/astoria/body/hair/hair_1_top.png" 
        $ astoria_xpos                = 300
        $ astoria_ypos                = 0
        $ astoria_zorder              = 5

        #Face
        $ astoria_mouth               = "characters/astoria/face/mouth/c_smile.png" 
        $ astoria_eye                 = "characters/astoria/face/eyes/eye_averted.png" 
        $ astoria_eyebrow             = "characters/astoria/face/eyes/brow_averted.png" 
        $ astoria_pupil               = "characters/astoria/face/eyes/pupil_averted.png" 
        $ astoria_tears               = "characters/astoria/extras/blank.png" 
        $ astoria_blush               = "characters/astoria/extras/blank.png"
        $ astoria_extra_1             = "characters/astoria/extras/blank.png" 
        $ astoria_extra_2             = "characters/astoria/extras/blank.png" 
        $ astoria_extra_3             = "characters/astoria/extras/blank.png"

        #Clothes
        $ astoria_top                 = "characters/astoria/clothes/uniform/shirt_1.png" 
        $ astoria_acc                 = "characters/astoria/clothes/blank.png" 
        $ astoria_skirt               = "characters/astoria/clothes/uniform/skirt_1.png" 
        $ astoria_stock               = "characters/astoria/clothes/blank.png" 
        $ astoria_bra                 = "characters/astoria/clothes/underwear/lace_bra.png" 
        $ astoria_panties             = "characters/astoria/clothes/underwear/lace_panties.png" 
        
        $ astoria_wear_top            = True
        $ astoria_wear_bra            = True
        $ astoria_wear_skirt          = True
        $ astoria_wear_panties        = True
        $ astoria_wear_stockings      = True 
        $ astoria_wear_acc            = True
    
    if not hasattr(renpy.store,'astoria_extra_1') or reset_persistants: #Remove before update
        $ astoria_extra_1             = "characters/astoria/extras/blank.png" 
        $ astoria_extra_2             = "characters/astoria/extras/blank.png" 
        $ astoria_extra_3             = "characters/astoria/extras/blank.png" 

    return


label astoria_progress_init:

    if not hasattr(renpy.store,'astoria_spell_progress') or reset_persistants:

        ##Favour stuff

        ##Stats
        $ astoria_spell_progress = 0
        $ astoria_spell = 1 #Imperio
        $ astoria_points = 0

        ##Flags
        $ astoria_busy = False
        $ days_since_astoria = 0
        $ astoria_arrival_day = 30
        $ astoria_arrvial_whoring = 9

    #if not hasattr(renpy.store,'ADD') or reset_persistants:

    return
