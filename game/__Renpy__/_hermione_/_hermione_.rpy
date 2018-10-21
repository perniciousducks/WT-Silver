

### HERMIONE GRANGER ###

label her_main(text="", mouth=h_mouth, eyes=h_eyes, cheeks=None, tears=None, emote=None, trans=None, xpos=hermione_xpos, ypos=hermione_ypos):
    hide screen hermione_head
    hide screen hermione_main

    #Face
    if mouth!= "":
        $ h_mouth = mouth
    if eyes != "":
        $ h_eyes = eyes

    if cheeks != None:
        $ h_cheeks = cheeks
    else:
        $ h_cheeks = "00_blank"
    if tears != None:
        $ h_tears = tears
    else:
        $ h_tears = "00_blank"
    if emote != None:
        $ h_emote = emote
    else:
        $ h_emote = "00_blank"

    call h_update


    #Positioning
    if xpos != hermione_xpos:
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

    if ypos != hermione_ypos:
        if ypos == "base" or ypos == "default":
            $ hermione_ypos = 0
        else:
            $ hermione_ypos = int(ypos)


    #Transitions
    show screen bld1 #Should be active anyways.
    show screen hermione_main

    call transition(trans)

    #Text
    if text != "":
        $ renpy.say(her,text)

    return


label her_head(text="", mouth=h_mouth, eyes=h_eyes, cheeks=None, tears=None, emote=None, xpos = hermione_head_xpos, ypos = hermione_head_ypos):
    hide screen hermione_main
    hide screen hermione_head

    #Face
    if mouth!= "":
        $ h_mouth = mouth
    if eyes != "":
        $ h_eyes = eyes

    if cheeks != None:
        $ h_cheeks = cheeks
    else:
        $ h_cheeks = "00_blank"
    if tears != None:
        $ h_tears = tears
    else:
        $ h_tears = "00_blank"
    if emote != None:
        $ h_emote = emote
    else:
        $ h_emote = "00_blank"

    call h_update

    $ hermione_head_xpos = 605
    $ hermione_head_ypos = 235

    if xpos != hermione_head_xpos:
        if xpos == "base" or xpos == "default":
            $ hermione_head_xpos = 605
        else:
            $ hermione_head_xpos = int(xpos)

    if ypos != hermione_head_ypos:
        if ypos == "base" or ypos == "default":
            $ hermione_head_ypos = 235
        elif ypos == "up" or ypos == "high": #Use this for "lift_top" pose.
            $ hermione_head_ypos = 195
        else:
            $ hermione_head_ypos = int(ypos)

    if face_on_cg:
        if ccg_folder == "herm_sex":
            $ hermione_head_xpos = 305
            $ hermione_head_ypos = 87
            hide screen hermione_face
            show screen hermione_face
            with d3

    else:
        show screen bld1 #Should be active anyways.
        show screen hermione_head
        with d3

    if text != "":
        $ renpy.say(her2,text)

    if not face_on_cg:
        hide screen hermione_head

    return


label her_kneel(text="", mouth=h_mouth, eyes=h_eyes, cheeks=None, tears=None, emote=None):
    hide screen hermione_kneel

    #Face
    if mouth!= "":
        $ h_mouth = mouth
    if eyes != "":
        $ h_eyes = eyes

    if cheeks != None:
        $ h_cheeks = cheeks
    else:
        $ h_cheeks = "00_blank"
    if tears != None:
        $ h_tears = tears
    else:
        $ h_tears = "00_blank"
    if emote != None:
        $ h_emote = emote
    else:
        $ h_emote = "00_blank"

    call h_update

    show screen hermione_kneel #h_head2

    if text != "":
        $ renpy.say(her,text)

    return





label reset_hermione_main:
    show screen hermione_blank_main
    show screen hermione_blank_head
    show screen hermione_blank_chibi
    hide screen hermione_blank_main
    hide screen hermione_blank_head
    hide screen hermione_blank_chibi
    hide screen hermione_main

    #Hermione clothing save state
    call load_hermione_clothing_saves

    $ hermione_dribble = False
    $ hermione_squirt = False
    $ aftersperm = False #Show cum stains on Hermione's uniform.

    if hermione_action != "none":
        call h_action("none","update")
    call update_her_uniform
    call h_update_body
    call h_update_hair
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
        $ hermione_costume = True
    else:
        $ hermione_costume = False

    return
