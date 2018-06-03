

screen susan_main:
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
    if susan_wear_panties and not susan_wear_bottom:
        add susan_panties xpos susan_xpos ypos susan_ypos # Add the panties
    if susan_wear_garterbelt:
        add susan_garterbelt xpos susan_xpos ypos susan_ypos
    if susan_wear_onepiece and not susan_wear_top and not susan_wear_robe:
        add susan_onepiece xpos susan_xpos ypos susan_ypos
    if susan_wear_bottom:
        add susan_skirt xpos susan_xpos ypos susan_ypos # Add the skirt
    if susan_wear_top:
        add susan_top xpos susan_xpos ypos susan_ypos # Add the top
    if susan_wear_accs:
        add susan_accs xpos susan_xpos ypos susan_ypos # Add the accessory
    if susan_wear_stockings:
        add susan_stockings xpos susan_xpos ypos susan_ypos # Add the stockings
    if susan_wear_robe:
        add susan_robe xpos susan_xpos ypos susan_ypos
    ### ZORDER
    zorder susan_zorder

    
label sus_main(text="",eye=None, eyebrow=None, pupil=None, mouth=None, base=None, extra_1=None, extra_2=None, extra_3=None, xpos=None, ypos=None, trans=None):
    hide screen susan_main
    
    
    #Positioning
    if xpos != None:
        if xpos in ["base","default"]: #All the way to the right.
            $ susan_xpos = 640
            $ menu_x = 0.1 #Don't add ypos!
        elif xpos == "mid":                     #Centered.
            $ susan_xpos = 300
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos == "right":                   #Bit more to the right.
            $ susan_xpos = 400
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos == "wardrobe":
            $ susan_xpos = 540
        else:
            $ susan_xpos = int(xpos)

    if ypos != None:
        if ypos == "base" or ypos == "default":
            $ susan_ypos = 0
        elif ypos == "head":
            $ susan_ypos = 400 #Not the correct number!
            #ADD zorder change to be in front of textbox!
        else:
            $ susan_ypos = int(ypos)
            
    $ changeSusan(eye, eyebrow, pupil, mouth, susan_xpos, susan_ypos, base, extra_1, extra_2, extra_3)
    
    show screen susan_main
    show screen bld1
    
    #Transitions
    if trans != None:         #d3 is default.
        if trans == "d1":
            with d1
        elif trans == "d3": #Default anyways.
            with d3
        elif trans == "d5":
            with d5
        elif trans == "d7":
            with d7
        elif trans == "d9":
            with d9

        elif trans == "fade":
            with fade
        elif trans == "hpunch":
            with hpunch
        elif trans == "vpunch":
            with vpunch

        #Skip Transitions
        elif trans == "none" or trans == "skip":
            pass
        else: #for typos and preventing crashes...
            with d3
            
    #Default transition.
    else:
        if not wardrobe_active:
            with d3
            
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
            susan_eyebrow     = "characters/susan/face/eyes/brow_"+eyebrow+".png" 
        if pupil is not None:
            susan_pupil       = "characters/susan/face/eyes/pupil_"+pupil+".png" 
        if mouth is not None:
            susan_mouth       = "characters/susan/face/mouth/"+mouth+".png" 
        ###POSITION CONTROL
        if x_pos is not None:
            susan_xpos        = x_pos
        if y_pos is not None:
            susan_ypos        = y_pos
        #BODY CONTROL
        if base is not None:
            susan_base        = "characters/susan/base/"+base+".png" 
        if extra_1 is not None:
            susan_extra_1     = "characters/susan/extras/"+extra_1+".png" 
        if extra_2 is not None:
            susan_extra_2     = "characters/susan/extras/"+extra_2+".png" 
        if extra_3 is not None:
            susan_extra_3     = "characters/susan/extras/"+extra_3+".png" 