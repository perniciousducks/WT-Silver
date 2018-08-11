

screen tonks_main:
    ### BASE IMAGE
    add tonks_base xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) #Add the base body
    add tonks_l_arm xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) #Add the arms
    add tonks_r_arm xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) #Add the arms
    add tonks_hair xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) #Add the hair base
    add tonks_boobs xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) #Add the base body

    ### FACE
    add tonks_eye_bg xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) #Add the eye white
    add tonks_pupil xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) #Add the pupil
    add tonks_eye xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) #Add the eye outline

    add tonks_eyebrow xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) #Add the eyebrow
    add tonks_hair_shadow xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) #Add the hair shadow
    add tonks_mouth xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) #Add the mouth

    add tonks_cheeks xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) #Add the extras
    add tonks_tears xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) #Add the extras
    add tonks_extra xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) #Add the extras

    ### CLOTHES
    if tonks_wear_coat:
        add tonks_coat_back xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) # Add the coat back
    if tonks_wear_bra and not tonks_wear_top:
        add tonks_bra xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) # Add the bra
    if tonks_wear_panties and not tonks_wear_bottom:
        add tonks_panties xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) # Add the panties
    if tonks_wear_bottom:
        add tonks_skirt xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) # Add the skirt
    if tonks_wear_top:
        add tonks_top xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) # Add the top
    if tonks_wear_accs:
        add tonks_accs xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) # Add the accessory
    if tonks_wear_stockings:
        add tonks_stockings xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) # Add the stockings
    if tonks_wear_coat:
        add tonks_coat xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/scaleratio) # Add the coat

    ### ZORDER
    zorder tonks_zorder



label ton_main(text="",mouth=None,eye=None, eyebrow=None, pupil=None, base=None, breasts=None, cheeks=None, tears=None, extra=None, xpos=None, ypos=None, trans=None):
    hide screen tonks_main

    #Reset
    if cheeks == None:
        $ cheeks = "blank"
    if tears == None:
        $ tears = "blank"

    #Positioning
    if xpos != None:
        if xpos in ["base","default"]: #All the way to the right.
            $ tonks_xpos = 525
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


    $ changeTonks(mouth, eye, eyebrow, pupil, tonks_xpos, tonks_ypos, base, breasts, cheeks, tears, extra)

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
                        breasts=None,
                        cheeks=None,
                        tears=None,
                        extra=None):
        ###DEFINE GLOBAL VARIABLES
        global tonks_mouth
        global tonks_eye
        global tonks_eyebrow
        global tonks_pupil
        global tonks_xpos
        global tonks_ypos
        global tonks_base
        global tonks_boobs
        global tonks_cheeks
        global tonks_tears
        global tonks_extra
        ###EMOTION CONTROL
        if mouth is not None:
            tonks_mouth       = "characters/tonks/face/mouth/"+mouth+".png"
        if eye is not None:
            tonks_eye         = "characters/tonks/face/eyes/eye_"+eye+".png"
            tonks_eye_bg      = "characters/tonks/face/eyes/white.png"
        if eyebrow is not None:
            tonks_eyebrow     = "characters/tonks/face/brow/"+eyebrow+".png"
        if pupil is not None:
            tonks_pupil       = "characters/tonks/face/eyes/pupil_"+pupil+".png"
        ###POSITION CONTROL
        if x_pos is not None:
            tonks_xpos        = x_pos
        if y_pos is not None:
            tonks_ypos        = y_pos
        #BODY CONTROL
        if base is not None:
            tonks_base        = "characters/tonks/body/base/"+base+".png"
        if breasts is not None:
            tonks_boobs       = "characters/tonks/body/base/"+breasts+".png"
        if cheeks is not None:
            tonks_cheeks      = "characters/tonks/face/extras/"+cheeks+".png"
        if tears is not None:
            tonks_tears       = "characters/tonks/face/extras/"+tears+".png"
        if extra is not None:
            tonks_extra       = "characters/tonks/face/extras/"+extra+".png"
