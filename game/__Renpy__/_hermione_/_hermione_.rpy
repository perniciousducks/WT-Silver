

### HERMIONE GRANGER ###

label her_main(text="", mouth=None, eye=None, cheeks=None, tears=None, extra=None, emote=None, xpos=None, ypos=None, flip=None, trans=None):
    hide screen hermione_main
    hide screen hermione_face

    #Flip
    if flip == False: #Default
        $ hermione_flip = 1
    if flip == True: #Flipped
        $ hermione_flip = -1

    if cheeks == None:
        $ cheeks = "blank"
    if tears == None:
        $ tears = "blank"
    if emote == None:
        $ emote = "blank"

    #Positioning
    if xpos != None:
        if xpos in ["base","default"]: #All the way to the right.
            $ hermione_xpos = 640
            $ menu_x = 0.1 #Don't add ypos!
        elif xpos == "left":
            $ hermione_xpos = 200
            $ menu_x = 0.5
        elif xpos == "mid":                     #Centered.
            $ hermione_xpos = 300
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos == "right":                   #Bit more to the right.
            $ hermione_xpos = 400
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos in ["wardrobe","close"]:
            $ hermione_xpos = 540
        else:
            $ hermione_xpos = int(xpos)

    if ypos != None:
        if ypos in ["base","default"]:
            $ hermione_ypos = 0
            $ hermione_scaleratio = 2
            $ hermione_zorder = 5
            $ use_hermione_head = False

        elif ypos in ["head"]: #Use ypos="head" to activate her head position. Use ypos="base" to disable it. Use ypos="200" or any other number to move her head up or down.
            $ use_hermione_head = True
            $ hermione_scaleratio = 2 #Reset

            if face_on_cg: #Only her face is visible. Face gets placed on top of the CG screen.
                if ccg_folder == "herm_sex":
                    $ hermione_flip = -1 #Flipped.
                    $ hermione_scaleratio = 1.75
                    $ hermione_xpos = 277
                    $ hermione_ypos = 122
                $ hermione_zorder = 5

            else:
                if hermione_flip == -1: #Flipped
                    $ hermione_xpos = 620
                else:
                    $ hermione_xpos = 590
                $ hermione_ypos = 230
                $ hermione_zorder = 8

        else:
            $ hermione_ypos = int(ypos)

    $ changeHermione(mouth, eye, cheeks, tears, extra, emote, hermione_xpos, hermione_ypos)

    if use_hermione_head and face_on_cg: #Only her face. Used in CG scenes.
        show screen hermione_face
    else:
        show screen hermione_main

    show screen bld1 #Should be active anyways.

    #Transitions
    call transition(trans)

    #Text
    if text != "":
        $ renpy.say(her,text)

    if use_hermione_head and not face_on_cg:
        hide screen hermione_main

    return



label her_kneel(text="", mouth=None, eye=None, cheeks=None, tears=None, extra=None, emote=None, xpos=None, ypos=None, trans=None):
    hide screen hermione_kneel

    if cheeks == None:
        $ cheeks = "blank"
    if tears == None:
        $ tears = "blank"
    if emote == None:
        $ emote = "blank"

    $ changeHermione(mouth, eye, cheeks, tears, extra, emote, hermione_xpos, hermione_ypos)

    show screen hermione_kneel #h_head2

    show screen bld1 #Should be active anyways.

    #Transitions
    call transition(trans)

    #Text
    if text != "":
        $ renpy.say(her,text)

    return




label update_hermione:

    $ hermione_flip = 1
    $ use_hermione_head = False

    call update_her_uniform
    call h_update_body
    call update_her_hair

    return

label reset_hermione:

    #Hermione clothing save state
    call load_hermione_clothing_saves

    $ hermione_dribble = False
    $ hermione_squirt  = False
    $ aftersperm       = False #Show cum stains on Hermione's uniform.
    $ uni_sperm        = False
    $ sperm_on_tits    = False #Sperm on tits when Hermione pulls her shirt up.

    if hermione_action != "none":
        call h_action("none","update")

    call update_hermione

    return


label load_hermione_clothing_saves:

    #Uniform & Underwear
    if h_request_wear_top:
        $ hermione_wear_top          = True
    else:
        $ hermione_wear_top          = False

    if h_request_wear_onepiece:
        $ hermione_wear_onepiece     = True
    else:
        $ hermione_wear_onepiece     = False

    if h_request_wear_bra:
        $ hermione_wear_bra          = True
    else:
        $ hermione_wear_bra          = False

    if h_request_wear_bottom:
        $ hermione_wear_bottom       = True
    else:
        $ hermione_wear_bottom       = False

    if h_request_wear_panties:
        $ hermione_wear_panties      = True
    else:
        $ hermione_wear_panties      = False

    if h_request_wear_garterbelt:
        $ hermione_wear_garterbelt   = True
    else:
        $ hermione_wear_garterbelt   = False

    #Other Clothing
    if h_request_wear_neckwear:
        $ hermione_wear_neckwear     = True
    else:
        $ hermione_wear_neckwear     = False

    if h_request_wear_body_accs:
        $ hermione_wear_body_accs    = True
    else:
        $ hermione_wear_body_accs    = False

    if h_request_wear_gloves:
        $ hermione_wear_gloves       = True
    else:
        $ hermione_wear_gloves       = False

    if h_request_wear_stockings:
        $ hermione_wear_stockings    = True
    else:
        $ hermione_wear_stockings    = False

    if h_request_wear_robe:
        $ hermione_wear_robe         = True
    else:
        $ hermione_wear_robe         = False

    #Head Accessories
    if h_request_wear_hat:
        $ hermione_wear_hat          = True
    else:
        $ hermione_wear_hat          = False

    if h_request_wear_glasses:
        $ hermione_wear_glasses      = True
    else:
        $ hermione_wear_glasses      = False

    if h_request_wear_ears:
        $ hermione_wear_ears         = True
    else:
        $ hermione_wear_ears         = False

    if h_request_wear_makeup:
        $ hermione_wear_makeup       = True
    else:
        $ hermione_wear_makeup       = False

    if h_request_wear_piercings:
        $ hermione_wear_piercings    = True
    else:
        $ hermione_wear_piercings    = False

    if h_request_wear_tattoos:
        $ hermione_wear_tattoos      = True
    else:
        $ hermione_wear_tattoos      = False

    if h_request_wear_outfit:
        $ hermione_wear_outfit = True
    else:
        $ hermione_wear_outfit = False

    return


init python:
    def changeHermione( mouth=None,
                        eye=None,
                        cheeks=None,
                        tears=None,
                        extra=None,
                        emote=None,
                        x_pos=None,
                        y_pos=None):

        ### DEFINE GLOBAL VARIABLES ###
        global hermione_mouth
        global hermione_eyes
        global hermione_cheeks
        global hermione_tears
        global hermione_extra
        global hermione_emote
        global hermione_xpos
        global hermione_ypos

        ### FACE CONTROL ###
        if mouth is not None:
            hermione_mouth       = "characters/hermione/face/mouth/"+str(h_lipstick)+"/"+str(mouth)+".png"
        if eye is not None:
            hermione_eyes        = "characters/hermione/face/eyes/"+str(h_eye_color)+"/"+str(eye)+".png"
        if cheeks is not None:
            hermione_cheeks      = "characters/hermione/face/extras/cheeks_"+str(cheeks)+".png"
        if tears is not None:
            hermione_tears       = "characters/hermione/face/extras/tears_"+str(tears)+".png"
        if extra is not None:
            hermione_extra       = "characters/hermione/face/extras/"+str(extra)+".png"
        if emote is not None:
            hermione_emote       = "characters/emotes/"+str(emote)+".png"

        ### POSITION CONTROL ###
        if x_pos is not None:
            hermione_xpos        = x_pos
        if y_pos is not None:
            hermione_ypos        = y_pos
