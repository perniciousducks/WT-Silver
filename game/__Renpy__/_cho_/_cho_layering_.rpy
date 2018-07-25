

screen cho_chang:
    ### BASE IMAGE
    add cc_arms xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) #Add the arms
    add cc_base xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) #Add the base body
    add cc_hair_shadow xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) #Add the hair shadow
    ### EMOTIONS
    add cc_eye xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) #Add the eye outline
    add cc_pupil xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) #Add the pupil
    add cc_eyebrow xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) #Add the eyebrow
    add cc_hair xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) #Add the hair shadow
    ###MOUTH
    add cc_mouth xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) #Add the mouth
    ###TEARS for fears
    add cc_tears xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) #Add the tears
    ### CLOTHES 
    if cc_wear_bra and not cc_wear_top:
        add cc_bra xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) # Add the bra
    if cc_wear_panties and not cc_wear_skirt:
        add cc_panties xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) # Add the panties
    if cc_wear_skirt:
        add cc_skirt xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) # Add the skirt
    if cc_wear_top:
        add cc_top xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) # Add the top
    if cc_wear_acc:
        add cc_acc xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) # Add the accessory
    if cc_wear_vest:
        add cc_vest xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) # Add the vest
    if cc_wear_stockings:
        add cc_stock xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) # Add the stockings
    ### OTHER
    add cc_l_hand xpos cc_xpos ypos cc_ypos xzoom cc_flip zoom (1.0/scaleratio) # Add the left hand
    ### ZORDER
    zorder cc_zorder



init python: ###Method Definition for new characters
    def changeCho(  cho_eye=None,
                    cho_eyebrow=None, 
                    cho_pupil=None, 
                    cho_mouth=None, 
                    x_pos=None, 
                    y_pos=None): # Cho
        ###DEFINE GLOBAL VARIABLES
        global cc_xpos
        global cc_ypos
        global cc_base
        global cc_cheeks
        global cc_eye
        global cc_pupil
        #global cc_eyebrow
        global cc_mouth
        global cc_eyebrow
        ###CHANGE INTS TO STRING
        cho_eye = str(cho_eye)
        cho_eyebrow = str(cho_eyebrow)
        cho_pupil = str(cho_pupil)
        cho_mouth = str(cho_mouth)
        ###HIDE OLD SCREEN
        #renpy.hide_screen("cho_chang")
        ###MANUAL POSITION CONTROL
        if x_pos is not None:
            cc_xpos = x_pos
        else:
            cc_xpos = cc_xpos
        if y_pos is not None:
            cc_ypos = cc_ypos
        else:
            cc_ypos = cc_ypos

        ###EMOTION CONTROL
        if cho_eye is not None:
            if cho_eye == "0":
                cc_eye = "characters/blank.png"
            else:
                cc_eye = "characters/cho/eye/"+cho_eye+".png" 

        if cho_eyebrow is not None:
            if cho_eyebrow == "0":
                cc_eyebrow = "characters/blank.png"
            else:
                cc_eyebrow = "characters/cho/eyebrow/"+cho_eyebrow+".png" 

        if cho_pupil is not None:
            if cho_pupil == "0":
                cc_pupil = "characters/blank.png"
            else:
                cc_pupil = "characters/cho/pupil/"+cho_pupil+".png" 

        if cho_mouth is not None:
            if cho_mouth == "0":
                cc_mouth = "characters/blank.png"
            else:
                cc_mouth = "characters/cho/mouth/"+cho_mouth+".png" 
            
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("cho_chang")
        renpy.with_statement(Dissolve(0.3))
        