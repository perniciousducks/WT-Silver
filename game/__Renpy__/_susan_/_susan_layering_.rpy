screen susan_bones:
    ### BASE IMAGE
    add susan_l_arm xpos susan_xpos ypos susan_ypos #Add the arms
    add susan_r_arm xpos susan_xpos ypos susan_ypos #Add the arms
    add susan_hair xpos susan_xpos ypos susan_ypos #Add the hair base
    add susan_base xpos susan_xpos ypos susan_ypos #Add the base body
    add susan_boobs xpos susan_xpos ypos susan_ypos #Add the base body
    ### EMOTIONS
    add susan_eye xpos susan_xpos ypos susan_ypos #Add the eye outline
    add susan_pupil xpos susan_xpos ypos susan_ypos #Add the pupil
    add susan_eyebrow xpos susan_xpos ypos susan_ypos #Add the eyebrow
    add susan_hair_shadow xpos susan_xpos ypos susan_ypos #Add the hair shadow
    ###MOUTH
    add susan_mouth xpos susan_xpos ypos susan_ypos #Add the mouth
    ### FACE
    add susan_tears xpos susan_xpos ypos susan_ypos #Add the tears
    add susan_blush xpos susan_xpos ypos susan_ypos #Add the tears
    ### CLOTHES 
    if susan_wear_bra and not susan_wear_top:
        add susan_bra xpos susan_xpos ypos susan_ypos # Add the bra
    if susan_wear_panties and not susan_wear_skirt:
        add susan_panties xpos susan_xpos ypos susan_ypos # Add the panties
    if susan_wear_skirt:
        add susan_skirt xpos susan_xpos ypos susan_ypos # Add the skirt
    if susan_wear_top:
        add susan_top xpos susan_xpos ypos susan_ypos # Add the top
    if susan_wear_acc:
        add susan_acc xpos susan_xpos ypos susan_ypos # Add the accessory
    if susan_wear_stockings:
        add susan_stock xpos susan_xpos ypos susan_ypos # Add the stockings
    ### ZORDER
    zorder susan_zorder

label sus_main(text="",eye=None, eyebrow=None, pupil=None, mouth=None, xpos=None, ypos=None, base=None, extra_1=None, extra_2=None, extra_3=None):
    $ changesusan(eye, eyebrow, pupil, mouth, xpos, ypos, base, extra_1, extra_2, extra_3)
    if text != "":
        $ renpy.say(sus, text)
    return

init python:
    def changeSusan(  eye=None,
                        eyebrow=None, 
                        pupil=None, 
                        mouth=None, 
                        x_pos=None, 
                        y_pos=None,
                        base=None,
                        extra_1=None,
                        extra_2=None,
                        extra_3=None): 
        ###DEFINE GLOBAL VARIABLES
        global susan_eye
        global susan_eyebrow
        global susan_pupil
        global susan_mouth
        global susan_xpos
        global susan_ypos
        global susan_base
        global susan_extra_1
        global susan_extra_2
        global susan_extra_3
        ###EMOTION CONTROL
        if eye is not None:
            susan_eye         = "characters/susan/face/eyes/eye_"+eye+".png" 
        if eyebrow is not None:
            susan_eyebrow     = "characters/susan/face/eyes/eyebrow_"+eyebrow+".png" 
        if pupil is not None:
            susan_pupil       = "characters/susan/face/eyes/pupil_"+pupil+".png" 
        if mouth is not None:
            susan_mouth       = "characters/susan/face/mouth/mouth_"+mouth+".png" 
        ###POSITION CONTROL
        if x_pos is not None:
            susan_xpos        = x_pos
        if y_pos is not None:
            susan_ypos        = ypos
        #BODY CONTROL
        if base is not None:
            susan_base        = "characters/susan/base/"+base+".png" 
        if extra_1 is not None:
            susan_extra_1     = "characters/susan/extras/"+extra_1+".png" 
        if extra_2 is not None:
            susan_extra_2     = "characters/susan/extras/"+extra_2+".png" 
        if extra_3 is not None:
            susan_extra_3     = "characters/susan/extras/"+extra_3+".png" 
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("susan_bones")
        renpy.with_statement(Dissolve(0.3))