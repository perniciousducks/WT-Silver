

### HERMIONE GRANGER ###

label her_main(text="", mouth=None, eye=None, cheeks=None, tears=None, extra=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None):
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
        if xpos in ["base","default"]:      # All the way to the right.
            $ hermione_xpos = 640
        elif xpos == "left":
            $ hermione_xpos = 200
        elif xpos == "mid":                 # Centered.
            $ hermione_xpos = 300
        elif xpos == "right":               # Bit more to the right.
            $ hermione_xpos = 400
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

        elif ypos in ["head"]:
            # Use ypos="head" to activate her head position.
            # Use ypos="base" to disable it.
            # Use ypos="200" or any other number to move her head up or down.
            $ use_hermione_head = True
            $ hermione_scaleratio = 2

            if face_on_cg: #Only her face is visible. Face gets placed on top of the CG screen.
                if ccg_folder == "herm_sex":
                    $ hermione_flip = -1 #Flipped.
                    $ hermione_scaleratio = 1.75
                    $ hermione_xpos = 277
                    $ hermione_ypos = 122
                $ hermione_zorder = 5

            else:
                if hermione_flip == -1: #Flipped
                    $ hermione_xpos = -70 #Left side of screen!
                else:
                    $ hermione_xpos = 640
                $ hermione_ypos = 230
                $ hermione_zorder = 8

        elif ypos in ["suck"]:
            $ use_hermione_head = True
            $ hermione_scaleratio = 1.4
            $ hermione_xpos = 500
            $ hermione_ypos = 100
            $ hermione_zorder = 8

        else:
            $ hermione_ypos = int(ypos)

    if face != None:
        if mouth == None:
            call set_her_face(mouth = face)
        if eye == None:
            call set_her_face(eyes = face)

    $ changeHermione(mouth, eye, cheeks, tears, extra, emote, hermione_xpos, hermione_ypos)

    if use_hermione_head and face_on_cg: #Only her face. Used in CG scenes.
        show screen hermione_face
    else:
        show screen hermione_main

    show screen bld1 #Should be active anyways.

    call transition(trans, True)

    if text != "":
        $ renpy.say(her, text)

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

    call transition(trans, True)

    #Text
    if text != "":
        $ renpy.say(her,text)

    return




label update_hermione:

    $ hermione_flip = 1
    $ her_chibi_flip = 1
    $ use_hermione_head = False

    call update_her_uniform
    call update_her_body

    return

label reset_hermione:

    #Hermione clothing save state
    call load_hermione_clothing_saves

    $ hermione_expand_breasts = False
    $ hermione_expand_ass = False
    $ no_blinking      = False #When True - blinking animation is not displayed.
    $ hermione_dribble = False
    $ hermione_squirt  = False
    $ aftersperm       = False #Show cum stains on Hermione's uniform.
    $ uni_sperm        = False
    $ sperm_on_tits    = False #Sperm on tits when Hermione pulls her shirt up.

    if hermione_action != "none":
        call set_her_action("none","update")

    call update_hermione

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
