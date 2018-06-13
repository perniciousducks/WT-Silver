

label tonks_init:

    if not hasattr(renpy.store,'tonks_base') or reset_persistants:

        #Body
        $ tonks_base                = "characters/tonks/body/base/base_01.png" 
        $ tonks_boobs               = "characters/tonks/body/base/boobs_0.png" 
        $ tonks_l_arm               = "characters/tonks/body/arms/l_arm.png" 
        $ tonks_r_arm               = "characters/tonks/body/arms/r_arm.png" 
        $ tonks_hair                = "characters/tonks/body/hair/hair_1_base.png" 
        $ tonks_hair_shadow         = "characters/tonks/body/hair/hair_1_top.png" 
        $ tonks_xpos                = 600
        $ tonks_ypos                = 0
        $ tonks_zorder              = 5
        $ tonks_flip                = 1

        #Face
        $ tonks_mouth               = "characters/tonks/face/mouth/base.png" 
        
        $ tonks_eye                 = "characters/tonks/face/eyes/eye_base.png" 
        $ tonks_eye_bg              = "characters/tonks/face/eyes/white.png" 
        $ tonks_pupil               = "characters/tonks/face/eyes/pupil_base.png"
        
        $ tonks_eyebrow             = "characters/tonks/face/brow/base.png"  
        
        $ tonks_cheeks              = "characters/tonks/face/extras/blank.png" 
        $ tonks_tears               = "characters/tonks/face/extras/blank.png" 
        $ tonks_extra               = "characters/tonks/face/extras/blank.png"

        #Clothes
        $ tonks_coat                = "characters/tonks/clothes/auror/coat.png" 
        $ tonks_coat_back           = "characters/tonks/clothes/auror/coat_back.png" 
        $ tonks_top                 = "characters/tonks/clothes/auror/undershirt.png" 
        $ tonks_accs                = "characters/tonks/clothes/auror/earing.png" 
        $ tonks_skirt               = "characters/tonks/clothes/auror/pants.png" 
        $ tonks_stockings           = "characters/tonks/clothes/blank.png" 
        $ tonks_bra                 = "characters/tonks/clothes/blank.png"  
        $ tonks_panties             = "characters/tonks/clothes/blank.png" 

        $ tonks_wear_coat           = True
        $ tonks_wear_top            = True
        $ tonks_wear_bra            = True
        $ tonks_wear_bottom         = True
        $ tonks_wear_panties        = True
        $ tonks_wear_stockings      = True 
        $ tonks_wear_accs           = True

    #if not hasattr(renpy.store,'ADD') or reset_persistants:

    return


label tonks_progress_init:

    if not hasattr(renpy.store,'tonks_level') or reset_persistants:

        ##Favour stuff
        $ tonks_level = 0
        
        ##Flags
        $ tonks_busy = False
        $ tonks_unlocked = False
        $ chitchated_with_tonks = False
        
        ##Names
        $ tonks_name = "Tonks"
        $ ton_genie_name = "Professor"
        $ ton_astoria_name = "Cutie"
        
    
    return
