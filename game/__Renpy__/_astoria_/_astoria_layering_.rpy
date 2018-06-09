

screen astoria_main:
    ### BASE IMAGE
    add astoria_l_arm xpos astoria_xpos ypos astoria_ypos #Add the arms
    add astoria_r_arm xpos astoria_xpos ypos astoria_ypos #Add the arms
    add astoria_hair xpos astoria_xpos ypos astoria_ypos #Add the hair base
    add astoria_base xpos astoria_xpos ypos astoria_ypos #Add the base body
    
    ### FACE
    add astoria_eye_bg xpos astoria_xpos ypos astoria_ypos #Add the eye white
    add astoria_pupil xpos astoria_xpos ypos astoria_ypos #Add the pupil
    add astoria_eye xpos astoria_xpos ypos astoria_ypos #Add the eye outline
    
    add astoria_eyebrow xpos astoria_xpos ypos astoria_ypos #Add the eyebrow
    add astoria_hair_shadow xpos astoria_xpos ypos astoria_ypos #Add the hair shadow
    add astoria_mouth xpos astoria_xpos ypos astoria_ypos #Add the mouth
    
    add astoria_cheeks xpos astoria_xpos ypos astoria_ypos #Add the extras
    add astoria_tears xpos astoria_xpos ypos astoria_ypos #Add the extras
    add astoria_extra xpos astoria_xpos ypos astoria_ypos #Add the extras
    
    ### CLOTHES 
    if astoria_wear_bra and not astoria_wear_top:
        add astoria_bra xpos astoria_xpos ypos astoria_ypos # Add the bra
    if astoria_wear_panties and not astoria_wear_bottom:
        add astoria_panties xpos astoria_xpos ypos astoria_ypos # Add the panties
    if astoria_wear_garterbelt:
        add astoria_garterbelt xpos astoria_xpos ypos astoria_ypos
    if astoria_wear_onepiece and not astoria_wear_top and not astoria_wear_robe:
        add astoria_onepiece xpos astoria_xpos ypos astoria_ypos
    if astoria_wear_bottom and not astoria_wear_robe:
        add astoria_skirt xpos astoria_xpos ypos astoria_ypos # Add the skirt
    if astoria_wear_top and not astoria_wear_robe:
        add astoria_top xpos astoria_xpos ypos astoria_ypos # Add the top
    if astoria_wear_accs:
        add astoria_accs xpos astoria_xpos ypos astoria_ypos # Add the accessory
    if astoria_wear_stockings:
        add astoria_stockings xpos astoria_xpos ypos astoria_ypos # Add the stockings
    if astoria_wear_neckwear:
        add astoria_neckwear xpos astoria_xpos ypos astoria_ypos
    if astoria_wear_robe:
        add astoria_robe xpos astoria_xpos ypos astoria_ypos
        
    ### OTHER
    add astoria_l_hand xpos astoria_xpos ypos astoria_ypos # Add the left hand
    add astoria_r_hand xpos astoria_xpos ypos astoria_ypos # Add the left hand
    
    ### ZORDER
    zorder astoria_zorder

    
    
label ast_main(text="", mouth=None,eye=None, eyebrow=None, pupil=None, base=None, cheeks=None, tears=None, extra=None, xpos=None, ypos=None, trans=None):
    hide screen astoria_main
    
    #Reset
    if cheeks == None:
        $ cheeks = "blank"
    if tears == None:
        $ tears = "blank"
        
    #Positioning
    if xpos != None:
        if xpos in ["base","default"]: #All the way to the right.
            $ astoria_xpos = 640
            $ menu_x = 0.1 #Don't add ypos!
        elif xpos == "mid":                     #Centered.
            $ astoria_xpos = 300
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos == "right":                   #Bit more to the right.
            $ astoria_xpos = 400
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos == "wardrobe":
            $ astoria_xpos = 540
        else:
            $ astoria_xpos = int(xpos)

    if ypos != None:
        if ypos == "base" or ypos == "default":
            $ astoria_ypos = 0
        elif ypos == "head":
            $ astoria_ypos = 400 #Not the correct number!
            #ADD zorder change to be in front of textbox!
        else:
            $ astoria_ypos = int(ypos)
            

            
    $ changeAstoria(mouth, eye, eyebrow, pupil, astoria_xpos, astoria_ypos, base, cheeks, tears, extra)
    
    show screen astoria_main
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
        $ renpy.say(ast, text)
        
    return
    

init python:
    def changeAstoria(  mouth=None,
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
        global astoria_mouth
        global astoria_eye
        global astoria_eye_bg
        global astoria_eyebrow
        global astoria_pupil
        global astoria_xpos
        global astoria_ypos
        global astoria_base
        global astoria_cheeks
        global astoria_tears
        global astoria_extra
        ###EMOTION CONTROL
        if mouth is not None:
            astoria_mouth       = "characters/astoria/face/mouth/"+mouth+".png" 
        if eye is not None:
            astoria_eye         = "characters/astoria/face/eyes/eye_"+eye+".png" 
            astoria_eye_bg      = "characters/astoria/face/eyes/eye_"+eye+"_bg.png"
        if eyebrow is not None:
            astoria_eyebrow     = "characters/astoria/face/brow/"+eyebrow+".png" 
        if pupil is not None:
            astoria_pupil       = "characters/astoria/face/eyes/pupil_"+pupil+".png" 
        ###POSITION CONTROL
        if x_pos is not None:
            astoria_xpos        = x_pos
        if y_pos is not None:
            astoria_ypos        = y_pos
        ###BODY CONTROL
        if base is not None:
            astoria_base        = "characters/astoria/base/"+base+".png" 
        if cheeks is not None:
            astoria_cheeks      = "characters/astoria/face/extras/"+cheeks+".png" 
        if tears is not None:
            astoria_tears       = "characters/astoria/face/extras/"+tears+".png" 
        if extra is not None:
            astoria_extra       = "characters/astoria/face/extras/"+extra+".png" 