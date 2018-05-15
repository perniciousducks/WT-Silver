### THIS IS WHERE WE DECLARE VARIABLES AND STUFF FOR 4 HOUSES

label sus_init:

    #Body 
    $ sus_base               = "characters/susan/base/base_01.png" 
    $ sus_hair               = "characters/susan/base/hair_01.png"
    $ sus_breast             = "characters/susan/base/breasts_02.png" 
    $ sus_legs               = "characters/susan/base/legs_01.png"
    $ sus_arms               = "characters/susan/base/arm_01.png" 
    $ sus_arm_2              = "characters/susan/base/blank.png" 
    $ sus_left_arm           = "characters/susan/base/l_arm_01.png" 
    $ sus_arm_base           = "characters/susan/base/arm_base.png" 
    $ sus_hair_shadow        = "characters/susan/base/hair_shadow.png" 
    $ sus_xpos               = 300
    $ sus_ypos               = 0
    $ sus_zorder             = 5

    #Face
    $ sus_mouth              = "characters/susan/mouth/mouth_01.png" 
    $ sus_eye                = "characters/susan/eye/eye_01.png" 
    $ sus_eyebrow            = "characters/susan/eye/eyebrow_01.png" 
    $ sus_pupil              = "characters/susan/eye/pupil_01.png"

    #Clothes
    $ sus_vest               = "characters/susan/clothes/uniform/vest.png" 
    $ sus_top                = "characters/susan/clothes/uniform/top.png" 
    $ sus_asus               = "characters/susan/clothes/uniform/tie.png" 
    $ sus_skirt              = "characters/susan/clothes/uniform/skirt.png" 
    $ sus_stock              = "characters/susan/clothes/uniform/stockings.png" 

    $ sus_wear_top           = True
    $ sus_wear_bra           = True
    $ sus_wear_skirt         = True
    $ sus_wear_panties       = True
    $ sus_wear_stockings     = True 
    $ sus_wear_vest          = True
    $ sus_wear_acc           = True

    return


label sus_progress_init:

    $ sus_known = False
    $ sus_met = False

    #Susan's scene stats:
    $ sus_anger = 0
    $ sus_boredom = 0
    $ sus_arousal = 0

    #Susan's general stats:
    $ sus_corruption = 0 
    $ sus_obedience = 0

    return


