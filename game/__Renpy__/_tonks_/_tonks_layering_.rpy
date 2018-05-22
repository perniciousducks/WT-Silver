screen nymphadora_tonks:
    ### BASE IMAGE
    add tonks_l_arm xpos tonks_xpos ypos tonks_ypos #Add the arms
    add tonks_r_arm xpos tonks_xpos ypos tonks_ypos #Add the arms
    add tonks_hair xpos tonks_xpos ypos tonks_ypos #Add the hair base
    add tonks_base xpos tonks_xpos ypos tonks_ypos #Add the base body
    add tonks_boobs xpos tonks_xpos ypos tonks_ypos #Add the base body
    ### EMOTIONS
    add tonks_eye xpos tonks_xpos ypos tonks_ypos #Add the eye outline
    add tonks_pupil xpos tonks_xpos ypos tonks_ypos #Add the pupil
    add tonks_eyebrow xpos tonks_xpos ypos tonks_ypos #Add the eyebrow
    add tonks_hair_shadow xpos tonks_xpos ypos tonks_ypos #Add the hair shadow
    ###MOUTH
    add tonks_mouth xpos tonks_xpos ypos tonks_ypos #Add the mouth
    ### FACE
    add tonks_tears xpos tonks_xpos ypos tonks_ypos #Add the tears
    add tonks_blush xpos tonks_xpos ypos tonks_ypos #Add the tears
    ### CLOTHES 
    if tonks_wear_coat:
        add tonks_coat_back xpos tonks_xpos ypos tonks_ypos # Add the coat back
    if tonks_wear_bra and not tonks_wear_top:
        add tonks_bra xpos tonks_xpos ypos tonks_ypos # Add the bra
    if tonks_wear_panties and not tonks_wear_skirt:
        add tonks_panties xpos tonks_xpos ypos tonks_ypos # Add the panties
    if tonks_wear_skirt:
        add tonks_skirt xpos tonks_xpos ypos tonks_ypos # Add the skirt
    if tonks_wear_top:
        add tonks_top xpos tonks_xpos ypos tonks_ypos # Add the top
    if tonks_wear_acc:
        add tonks_acc xpos tonks_xpos ypos tonks_ypos # Add the accessory
    if tonks_wear_stockings:
        add tonks_stock xpos tonks_xpos ypos tonks_ypos # Add the stockings
    if tonks_wear_coat:
        add tonks_coat xpos tonks_xpos ypos tonks_ypos # Add the coat
    ### ZORDER
    zorder tonks_zorder

label ton_main(text="",eye=None, eyebrow=None, pupil=None, mouth=None, xpos=None, ypos=None, base=None, extra_1=None, extra_2=None, extra_3=None):
    $ changetonks(eye, eyebrow, pupil, mouth, xpos, ypos, base, extra_1, extra_2, extra_3)
    if text != "":
        $ renpy.say(ton, text)
    return

init python:
    def changeTonks(  eye=None,
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
        global tonks_eye
        global tonks_eyebrow
        global tonks_pupil
        global tonks_mouth
        global tonks_xpos
        global tonks_ypos
        global tonks_base
        global tonks_extra_1
        global tonks_extra_2
        global tonks_extra_3
        ###EMOTION CONTROL
        if eye is not None:
            tonks_eye         = "characters/tonks/face/eyes/eye_"+eye+".png" 
        if eyebrow is not None:
            tonks_eyebrow     = "characters/tonks/face/eyes/eyebrow_"+eyebrow+".png" 
        if pupil is not None:
            tonks_pupil       = "characters/tonks/face/eyes/pupil_"+pupil+".png" 
        if mouth is not None:
            tonks_mouth       = "characters/tonks/face/mouth/mouth_"+mouth+".png" 
        ###POSITION CONTROL
        if x_pos is not None:
            tonks_xpos        = x_pos
        if y_pos is not None:
            tonks_ypos        = ypos
        #BODY CONTROL
        if base is not None:
            tonks_base        = "characters/tonks/base/"+base+".png" 
        if extra_1 is not None:
            tonks_extra_1     = "characters/tonks/extras/"+extra_1+".png" 
        if extra_2 is not None:
            tonks_extra_2     = "characters/tonks/extras/"+extra_2+".png" 
        if extra_3 is not None:
            tonks_extra_3     = "characters/tonks/extras/"+extra_3+".png" 
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("tonks_greengrass")
        renpy.with_statement(Dissolve(0.3))