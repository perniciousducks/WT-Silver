

screen susan_main:
    tag susan_main

    ### BASE IMAGE
    add susan_l_arm xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) #Add the arms
    add susan_r_arm xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) #Add the arms
    add susan_hair xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) #Add the hair base
    add susan_base xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) #Add the base body
    add susan_boobs xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) #Add the base body

    ### FACE
    add susan_eye_bg xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) #Add the eye white
    add susan_pupil xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) #Add the pupil
    add susan_eye xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) #Add the eye outline

    add susan_eyebrow xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) #Add the eyebrow
    add susan_mouth xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) #Add the mouth

    add susan_cheeks xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) #Add the extras
    add susan_tears xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) #Add the extras
    add susan_extra xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) #Add the extras

    ### CLOTHING LAYERS ###

    #Uniform
    if not susan_wear_outfit:
        use susan_uniform

    #Outfit
    if susan_wear_outfit:
        if susan_wear_top:
            use susan_outfit
        else:
            use susan_uniform

    ### ACCESORIES LAYERS ###

    #Hair+
    add susan_hair_shadow xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) #Add the hair shadow

    #Hat
    if susan_wear_hat:
        add susan_hat xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) # Add the accessory

    #Cum layers.
    if susan_face_covered:
        add susan_face_cum xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio)
    if susan_body_covered:
        add susan_body_cum xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio)
    if susan_aftersperm:
        add susan_clothes_cum xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio)

    #Robe
    if susan_wear_robe:
        add susan_robe xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio)

    ### ZORDER
    zorder susan_zorder


screen susan_uniform:
    tag susan_main

    ### CLOTHES
    if susan_wear_bra and not susan_wear_top:
        add susan_bra xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) # Add the bra
    if susan_wear_panties and not susan_wear_bottom:
        add susan_panties xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) # Add the panties
    if susan_wear_garterbelt:
        add susan_garterbelt xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio)
    if susan_wear_stockings:
        add susan_stockings xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) # Add the stockings
    if susan_wear_onepiece and not susan_wear_top and not susan_wear_robe:
        add susan_onepiece xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio)
    if susan_wear_bottom:
        add susan_skirt xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) # Add the skirt
    if susan_wear_top:
        add susan_top xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) # Add the top
    if susan_wear_accs:
        add susan_accs xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio) # Add the accessory
    if susan_wear_neckwear:
        add susan_neckwear xpos susan_xpos ypos susan_ypos xzoom susan_flip zoom (1.0/scaleratio)

    ### ZORDER
    zorder susan_zorder


screen susan_outfit:
    tag susan_main

    for i in susan_outfit_GLBL.getOutfitLayers():
        add "characters/susan/clothes/custom/"+i xpos susan_xpos ypos susan_ypos alpha transparency zoom (1.0/scaleratio)

    ### ZORDER
    zorder susan_zorder



label sus_main(text="", mouth=None,eye=None, eyebrow=None, pupil=None, base=None, cheeks=None, tears=None, extra=None, xpos=None, ypos=None, trans=None):
    hide screen susan_main

    #Reset
    if cheeks == None:
        $ cheeks = "blank"
    if tears == None:
        $ tears = "blank"

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
        elif xpos in ["wardrobe","close"]:
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

    $ changeSusan(mouth, eye, eyebrow, pupil, susan_xpos, susan_ypos, base, cheeks, tears, extra)

    show screen susan_main
    show screen bld1

    #Transitions
    call transition(trans)

    if text != "":
        $ renpy.say(sus, text)

    return


init python:
    def changeSusan(    mouth=None,
                        eye=None,
                        eyebrow=None,
                        pupil=None,
                        x_pos=None,
                        y_pos=None,
                        base=None,
                        cheeks=None,
                        tears=None,
                        extra=None):
        ###DEFINE GLOBAL VARIABLES
        global susan_mouth
        global susan_eye
        global susan_eye_bg
        global susan_eyebrow
        global susan_pupil
        global susan_xpos
        global susan_ypos
        global susan_base
        global susan_cheeks
        global susan_tears
        global susan_extra
        ###EMOTION CONTROL
        if mouth is not None:
            susan_mouth       = "characters/susan/face/mouth/"+mouth+".png"
        if eye is not None:
            susan_eye         = "characters/susan/face/eyes/eye_"+eye+".png"
            susan_eye_bg      = "characters/susan/face/eyes/eye_"+eye+"_bg.png"
        if eyebrow is not None:
            susan_eyebrow     = "characters/susan/face/brow/"+eyebrow+".png"
        if pupil is not None:
            susan_pupil       = "characters/susan/face/eyes/pupil_"+pupil+".png"
        ###POSITION CONTROL
        if x_pos is not None:
            susan_xpos        = x_pos
        if y_pos is not None:
            susan_ypos        = y_pos
        #BODY CONTROL
        if base is not None:
            susan_base        = "characters/susan/base/"+base+".png"
        if cheeks is not None:
            susan_cheeks     = "characters/susan/face/extras/"+cheeks+".png"
        if tears is not None:
            susan_tears     = "characters/susan/face/extras/"+tears+".png"
        if extra is not None:
            susan_extra     = "characters/susan/face/extras/"+extra+".png"
