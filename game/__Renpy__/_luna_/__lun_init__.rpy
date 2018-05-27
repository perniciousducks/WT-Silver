

label luna_init:
    
    if not hasattr(renpy.store,'luna_base') or reset_persistants:

        #Body
        $ luna_base              = "characters/luna/body/base/base_01.png" 
        $ luna_cheeks            = "characters/luna/body/face/cheeks/cheeks_1.png" 
        $ luna_hair              = 1
        $ luna_l_arm             = 1
        $ luna_r_arm             = 1
        $ luna_xpos              = 600
        $ luna_ypos              = 0
        $ luna_zorder            = 5
        $ luna_flip              = 1

        #Face
        $ luna_mouth             = "characters/luna/body/face/mouth/mouth_1.png" 
        $ luna_eye               = "characters/luna/body/face/eye/eye_1.png" 
        $ luna_eyebrow           = "characters/luna/body/face/eyebrow/eyebrow_1.png" 
        $ luna_pupil             = "characters/luna/body/face/pupil/pupil_1.png"
        $ luna_tears             = 0 

        #Clothes
        $ luna_glasses           = "characters/luna/misc/glasses.png" 
        $ luna_top               = "characters/luna/clothes/uniform/top_1.png" 
        $ luna_acc               = "characters/luna/misc/jewel.png" 
        $ luna_skirt             = "characters/luna/clothes/uniform/skirt_1.png" 
        $ luna_panties           = "characters/luna/clothes/underwear/panties.png" 
        $ luna_bra               = "characters/luna/clothes/underwear/bra.png" 
        $ luna_cum               = 1
        $ luna_wear_cum          = False
        $ luna_wear_cum_under    = False

        $ luna_wear_glasses      = False
        $ luna_wear_bra          = True
        $ luna_wear_panties      = True
        $ luna_wear_skirt        = True
        $ luna_wear_top          = True
        $ luna_wear_acc          = True

        #Chibi
        $ luna_chibi_image       = "characters/luna/chibis/luna_stand.png" 
        $ luna_chibi_xpos        = 500
        $ luna_chibi_ypos        = 250
        $ luna_chibi_zorder      = 4
    
        #CG
        $ hermione_kneel_leg     = False
        $ hermione_kneel_cock    = False

    #if not hasattr(renpy.store,'ADD') or reset_persistants:

    return



label luna_progress_init:
    
    if not hasattr(renpy.store,'luna_known') or reset_persistants:

        $ hat_known = False
        $ luna_known = False
        $ luna_busy = False
        $ luna_unlocked = False
        $ l_genie_name = "Old man"
        $ luna_name = "Miss Lovegood"

        $ luna_dom = 0
        $ luna_sub = 0
        $ luna_gold = 0
        $ luna_skirt_level = 1
        $ luna_top_level = 1
        $ luna_corruption = 0
        $ luna_arousal = 0

        $ luna_reverted = False
        $ luna_addicted = False
        $ luna_herm_talk = False

    #if not hasattr(renpy.store,'ADD') or reset_persistants:

    return

