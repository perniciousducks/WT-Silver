

### HERMIONE GRANGER ###

label her_main(text="", mouth=h_mouth, eyes=h_eyes, cheeks=None, tears=None, emote=None, trans="", xpos=hermione_xpos, ypos=hermione_ypos):   
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

    call h_update from _call_h_update_2


    #Positioning
    if xpos != hermione_xpos:
        if xpos in ["base","default"]: #All the way to the right.
            $ hermione_xpos = 640
            $ menu_x = 0.1 #Don't add ypos!
        elif xpos == "mid":                     #Centered.
            $ hermione_xpos = 300
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos == "right":                   #Bit more to the right.
            $ hermione_xpos = 400
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos in ["wardrobe","close"]:
            $ hermione_xpos = 540
        else:
            $ hermione_xpos = xpos

    if ypos != hermione_ypos:
        if ypos == "base" or ypos == "default":
            $ hermione_ypos = 0
        else:
            $ hermione_ypos = ypos

            
    #Transitions
    show screen bld1 #Should be active anyways.
    show screen hermione_main
    
    if trans != "":         #d3 is default.
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

    else: #Default Transition
        if not wardrobe_active:
            with d3


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

    call h_update from _call_h_update_3

    $ hermione_head_xpos = 605
    $ hermione_head_ypos = 235

    if xpos != hermione_head_xpos:
        if xpos == "base" or xpos == "default":
            $ hermione_head_xpos = 605
        else:
            $ hermione_head_xpos = xpos

    if ypos != hermione_head_ypos:
        if ypos == "base" or ypos == "default":
            $ hermione_head_ypos = 235
        elif ypos == "up" or ypos == "high": #Use this for "lift_top" pose.
            $ hermione_head_ypos = 195
        else:
            $ hermione_head_ypos = ypos

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

    call h_update from _call_h_update_4

    show screen hermione_kneel #h_head2

    if text != "":
        $ renpy.say(her,text)

    return



#Hermione Action

label set_hermione_action(action="", update=""):
    hide screen hermione_main
    call h_action(action,update) from _call_h_action_78

    show screen hermione_main
    with d3

    return
    
    
label h_action(action =  "", update=""):
    
    if action == "" or action == "none" or action == "None" or action == 0:

        $ hermione_action = "none"
        $ hermione_use_action = False

        $ h_right_arm        = "right_1"
        $ h_left_arm         = "left_1"
        $ h_action_top = ""
        $ h_action_bottom = ""
        $ h_action_gloves = ""

        $ h_action_a = "00_blank.png"
        $ h_action_b = "00_blank.png"
        $ hermione_action_a = "characters/hermione/body/arms/left/00_blank.png"
        $ hermione_action_b = "characters/hermione/body/arms/left/00_blank.png"
        $ hermione_costume_action_a = "characters/hermione/clothes/custom/00_blank.png"
        $ milking           = 0


        if update != "skip_update":
        
            call load_hermione_clothing_saves from _call_load_hermione_clothing_saves_3

    else:

        if hermione_costume:
            if action in hermoine_outfit_GLBL.actions:
                $ hermione_use_action = True
                $ h_action_a = hermoine_outfit_GLBL.getActionImage(action)
            else:
                $ hermione_use_action = False
                $ h_action_a = "00_blank.png"

        else:

            ### LIFT SKIRT ###
            if action == "lift_skirt":
                $ hermione_action = "lift_skirt"
                $ hermione_use_action = True

            ### LIFT TOP ###
            if action == "lift_top":
                $ hermione_action = "lift_top"
                $ hermione_use_action = True
            
            ### HOLD BOOK ###
            if action == "hold_book":
                $ hermione_action = "hold_book"
                $ hermione_use_action = True
            
            ### LIFT BREASTS ###
            if action == "lift_breasts" or action == "lift_breasts_large":
                $ hermione_action = "lift_breasts"
                $ hermione_use_action = True

                if action == "lift_breasts_large":
                    $ hermione_expand_breasts = True

                

            ### NAKED ACTIONS ###

            #Lift breasts
            if action == "lift_breasts_naked" or action == "lift_breasts_large_naked":
                $ hermione_action = "lift_breasts"
                $ hermione_use_action = True

                $ hermione_wear_bottom = False
                $ hermione_wear_panties = False
                $ hermione_wear_garterbelt = False
                $ hermione_wear_stockings = False

                if action == "lift_breasts_large_naked":
                    $ hermione_expand_breasts = True

            #Hands Behind
            if action == "hands_behind":
                $ hermione_action = "hands_behind"
                $ hermione_use_action = True
                
            #Covering
            if action == "covering":
                $ hermione_action = "covering"
                $ hermione_use_action = True

            #Fingering
            if action == "fingering":
                $ hermione_action = "fingering"
                $ hermione_use_action = True

            #Covering Top
            if action == "covering_top":
                $ hermione_action = "covering_top"
                $ hermione_use_action = True
                
            #Pinch
            if action == "pinch":
                $ hermione_action = "pinch"
                $ hermione_use_action = True
            
            #Hands Cuffed
            if action == "hands_cuffed":
                $ hermione_action = "hands_cuffed"
                $ hermione_use_action = True

            #Milk Breasts
            if action == "milk_breasts":
                $ hermione_action = "milk_breasts"
                $ hermione_use_action = True


            ### NO hermione_action CHANGE ###

            #Temporarily expand Hermione #Resets after 5 days.
            if action == "expand_breasts":
                $ hermione_expand_breasts_counter = 5
                $ hermione_expand_breasts = True
            
            if action == "expand_ass":
                $ hermione_expand_ass_counter = 5
                $ hermione_expand_ass = True

            if action == "expand_all":
                $ hermione_expand_breasts_counter = 5
                $ hermione_expand_ass_counter = 5
                $ hermione_expand_breasts = True
                $ hermione_expand_ass = True

            #Strip Naked
            if action == "hands_free" or action == "naked" or action == "strip":
                $ hermione_wear_top = False
                $ hermione_wear_bra = False
                $ hermione_wear_bottom = False
                $ hermione_wear_panties = False
                $ hermione_wear_garterbelt = False
                $ hermione_wear_neckwear = False
                $ hermione_wear_body_accs = False
                $ hermione_wear_gloves = False
                $ hermione_wear_stockings = False
                $ hermione_wear_robe = False
           
        
    call update_her_uniform from _call_update_her_uniform_94            #calls update_her_action, update_chibi_uniform, and h_update_body;

    return
    
label set_h_action_vars:
    $ hermione_action_right_arm = "characters/hermione/body/arms/right/"+str(h_action_right_arm)
    $ hermione_action_left_arm = "characters/hermione/body/arms/left/"+(h_action_left_arm)
    $ hermione_action_a = "characters/hermione/clothes/uniform/action/"+str(h_action_a)
    $ hermione_action_b = "characters/hermione/clothes/uniform/action/"+str(h_action_b)
    $ hermione_costume_action_a = "characters/hermione/clothes/custom/"+str(h_action_a)
    return
    
    
label reset_hermione_main:
    show screen hermione_blank_main
    show screen hermione_blank_head
    show screen hermione_blank_chibi
    hide screen hermione_blank_main
    hide screen hermione_blank_head
    hide screen hermione_blank_chibi

    #Hermione clothing save state
    call load_hermione_clothing_saves from _call_load_hermione_clothing_saves_4
    
    $ hermione_dribble = False
    $ hermione_squirt = False
    $ aftersperm = False #Show cum stains on Hermione's uniform.
    
    hide screen hermione_main
    #call h_outfit_OBJ(None)
    if hermione_action != "none":
        call h_action("none") from _call_h_action_79
    call update_her_uniform from _call_update_her_uniform_95
    call h_update_body from _call_h_update_body_4
    call h_update_hair from _call_h_update_hair_11
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

    return

    
    
    
    
    