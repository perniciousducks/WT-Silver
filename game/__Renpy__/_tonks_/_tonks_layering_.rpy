

screen tonks_main:
    ### BASE IMAGE
    add tonks_l_arm xpos tonks_xpos ypos tonks_ypos #Add the arms
    add tonks_r_arm xpos tonks_xpos ypos tonks_ypos #Add the arms
    add tonks_hair xpos tonks_xpos ypos tonks_ypos #Add the hair base
    add tonks_base xpos tonks_xpos ypos tonks_ypos #Add the base body
    add tonks_boobs xpos tonks_xpos ypos tonks_ypos #Add the base body
    ### EMOTIONS
    add tonks_white xpos tonks_xpos ypos tonks_ypos #Add the white of her eye
    add tonks_pupil xpos tonks_xpos ypos tonks_ypos #Add the pupil
    add tonks_eye xpos tonks_xpos ypos tonks_ypos #Add the eye outline
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
    if tonks_wear_panties and not tonks_wear_bottom:
        add tonks_panties xpos tonks_xpos ypos tonks_ypos # Add the panties
    if tonks_wear_bottom:
        add tonks_skirt xpos tonks_xpos ypos tonks_ypos # Add the skirt
    if tonks_wear_top:
        add tonks_top xpos tonks_xpos ypos tonks_ypos # Add the top
    if tonks_wear_accs:
        add tonks_accs xpos tonks_xpos ypos tonks_ypos # Add the accessory
    if tonks_wear_stockings:
        add tonks_stockings xpos tonks_xpos ypos tonks_ypos # Add the stockings
    if tonks_wear_coat:
        add tonks_coat xpos tonks_xpos ypos tonks_ypos # Add the coat
    ### ZORDER
    zorder tonks_zorder

label ton_main(text="",mouth=None,eye=None, eyebrow=None, pupil=None, base=None, extra_1=None, extra_2=None, extra_3=None, xpos=None, ypos=None, trans=None):
    hide screen tonks_main
    
    #Positioning
    if xpos != None:
        if xpos in ["base","default"]: #All the way to the right.
            $ tonks_xpos = 640
            $ menu_x = 0.1 #Don't add ypos!
        elif xpos == "mid":                     #Centered.
            $ tonks_xpos = 300
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos == "right":                   #Bit more to the right.
            $ tonks_xpos = 400
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos == "wardrobe":
            $ tonks_xpos = 540
        else:
            $ tonks_xpos = int(xpos)

    if ypos != None:
        if ypos == "base" or ypos == "default":
            $ tonks_ypos = 0
        elif ypos == "head":
            $ tonks_ypos = 400 #Not the correct number!
            #ADD zorder change to be in front of textbox!
        else:
            $ tonks_ypos = int(ypos)
            

    $ changeTonks(mouth, eye, eyebrow, pupil, tonks_xpos, tonks_ypos, base, extra_1, extra_2, extra_3)
    
    show screen tonks_main
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
        $ renpy.say(ton, text)
        
    return

    
init python:
    def changeTonks(    mouth=None,
                        eye=None,
                        eyebrow=None, 
                        pupil=None,  
                        x_pos=None, 
                        y_pos=None,
                        base=None,
                        extra_1=None,
                        extra_2=None,
                        extra_3=None): 
        ###DEFINE GLOBAL VARIABLES
        global tonks_mouth
        global tonks_eye
        global tonks_eyebrow
        global tonks_pupil
        global tonks_xpos
        global tonks_ypos
        global tonks_base
        global tonks_extra_1
        global tonks_extra_2
        global tonks_extra_3
        ###EMOTION CONTROL
        if mouth is not None:
            tonks_mouth       = "characters/tonks/face/mouth/"+mouth+".png"
        if eye is not None:
            tonks_eye         = "characters/tonks/face/eyes/eye_"+eye+".png" 
        if eyebrow is not None:
            tonks_eyebrow     = "characters/tonks/face/eyes/brow_"+eyebrow+".png" 
        if pupil is not None:
            tonks_pupil       = "characters/tonks/face/eyes/pupil_"+pupil+".png"  
        ###POSITION CONTROL
        if x_pos is not None:
            tonks_xpos        = x_pos
        if y_pos is not None:
            tonks_ypos        = y_pos
        #BODY CONTROL
        if base is not None:
            tonks_base        = "characters/tonks/base/"+base+".png" 
        if extra_1 is not None:
            tonks_extra_1     = "characters/tonks/extras/"+extra_1+".png" 
        if extra_2 is not None:
            tonks_extra_2     = "characters/tonks/extras/"+extra_2+".png" 
        if extra_3 is not None:
            tonks_extra_3     = "characters/tonks/extras/"+extra_3+".png" 