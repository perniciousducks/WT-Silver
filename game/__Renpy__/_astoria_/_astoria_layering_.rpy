

screen astoria_greengrass:
    ### BASE IMAGE
    add astoria_l_arm xpos astoria_xpos ypos astoria_ypos #Add the arms
    add astoria_r_arm xpos astoria_xpos ypos astoria_ypos #Add the arms
    add astoria_hair xpos astoria_xpos ypos astoria_ypos #Add the hair base
    add astoria_base xpos astoria_xpos ypos astoria_ypos #Add the base body
    ### EMOTIONS
    add astoria_eye xpos astoria_xpos ypos astoria_ypos #Add the eye outline
    add astoria_pupil xpos astoria_xpos ypos astoria_ypos #Add the pupil
    add astoria_eyebrow xpos astoria_xpos ypos astoria_ypos #Add the eyebrow
    add astoria_hair_shadow xpos astoria_xpos ypos astoria_ypos #Add the hair shadow
    ###MOUTH
    add astoria_mouth xpos astoria_xpos ypos astoria_ypos #Add the mouth
    ### FACE
    add astoria_extra_1 xpos astoria_xpos ypos astoria_ypos #Add the extras
    add astoria_extra_2 xpos astoria_xpos ypos astoria_ypos #Add the extras
    add astoria_extra_3 xpos astoria_xpos ypos astoria_ypos #Add the extras
    ### CLOTHES 
    if astoria_wear_bra and not astoria_wear_top:
        add astoria_bra xpos astoria_xpos ypos astoria_ypos # Add the bra
    if astoria_wear_panties and not astoria_wear_skirt:
        add astoria_panties xpos astoria_xpos ypos astoria_ypos # Add the panties
    if astoria_wear_skirt:
        add astoria_skirt xpos astoria_xpos ypos astoria_ypos # Add the skirt
    if astoria_wear_top:
        add astoria_top xpos astoria_xpos ypos astoria_ypos # Add the top
    if astoria_wear_acc:
        add astoria_acc xpos astoria_xpos ypos astoria_ypos # Add the accessory
    if astoria_wear_stockings:
        add astoria_stock xpos astoria_xpos ypos astoria_ypos # Add the stockings
    ### OTHER
    add astoria_l_hand xpos astoria_xpos ypos astoria_ypos # Add the left hand
    add astoria_r_hand xpos astoria_xpos ypos astoria_ypos # Add the left hand
    ### ZORDER
    zorder astoria_zorder

label ast_main(text="",eye=None, eyebrow=None, pupil=None, mouth=None, xpos=None, ypos=None, base=None, extra_1=None, extra_2=None, extra_3=None):
    $ changeAstoria(eye, eyebrow, pupil, mouth, xpos, ypos, base, extra_1, extra_2, extra_3)
    if text != "":
        $ renpy.say(ast, text)
    return

init python:
    def changeAstoria(  eye=None,
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
        global astoria_eye
        global astoria_eyebrow
        global astoria_pupil
        global astoria_mouth
        global astoria_xpos
        global astoria_ypos
        global astoria_base
        global astoria_extra_1
        global astoria_extra_2
        global astoria_extra_3
        ###EMOTION CONTROL
        if eye is not None:
            astoria_eye         = "characters/astoria/face/eyes/eye_"+eye+".png" 
        if eyebrow is not None:
            astoria_eyebrow     = "characters/astoria/face/eyes/brow_"+eyebrow+".png" 
        if pupil is not None:
            astoria_pupil       = "characters/astoria/face/eyes/pupil_"+pupil+".png" 
        if mouth is not None:
            astoria_mouth       = "characters/astoria/face/mouth/"+mouth+".png" 
        ###POSITION CONTROL
        if x_pos is not None:
            astoria_xpos        = x_pos
        if y_pos is not None:
            astoria_ypos        = ypos
        #BODY CONTROL
        if base is not None:
            astoria_base        = "characters/astoria/base/"+base+".png" 
        if extra_1 is not None:
            astoria_extra_1     = "characters/astoria/extras/"+extra_1+".png" 
        if extra_2 is not None:
            astoria_extra_2     = "characters/astoria/extras/"+extra_2+".png" 
        if extra_3 is not None:
            astoria_extra_3     = "characters/astoria/extras/"+extra_3+".png" 
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("astoria_greengrass")
        renpy.with_statement(Dissolve(0.3))