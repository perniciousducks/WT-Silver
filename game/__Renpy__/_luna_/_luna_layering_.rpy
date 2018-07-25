
###SILVER STUFF
#screen luna:
#    ### BASE IMAGE
#    add luna_base xpos luna_xpos+140 ypos luna_ypos #Add the base body
#    add luna_hair xpos luna_xpos+140 ypos luna_ypos #Add the hair shadow
#    ### EMOTIONS
#    add luna_mouth xpos luna_xpos+140 ypos luna_ypos #Add the mouth
#    add "characters/luna/body/face/eye_white.png"  xpos luna_xpos+140 ypos luna_ypos
#    add luna_pupil xpos luna_xpos+140 ypos luna_ypos #Add the pupil
#    add luna_eye xpos luna_xpos+140 ypos luna_ypos #Add the eye outline
#    add luna_eyebrow xpos luna_xpos+140 ypos luna_ypos #Add the eyebrow
#    ### CLOTHES 
#    add luna_bra xpos luna_xpos+140 ypos luna_ypos # Add the bra
#    add luna_panties xpos luna_xpos+140 ypos luna_ypos # Add the panties
#    add luna_skirt xpos luna_xpos+140 ypos luna_ypos # Add the skirt
#    add luna_top xpos luna_xpos+140 ypos luna_ypos # Add the top
#    #add luna_acc xpos luna_xpos ypos luna_ypos # Add the accessory
#    ### ZORDER
#    zorder zorder_character


screen luna:
    ### BASE IMAGE
    add luna_base xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)#Add the base body
    add "characters/luna/body/arms/left_"+str(luna_l_arm)+".png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)#Add the left arm
    add "characters/luna/body/arms/right_"+str(luna_r_arm)+".png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)#Add the right arm
    add luna_cheeks xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)#Add her blush to base
    add "characters/luna/body/head/hair_"+str(luna_hair)+".png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)#Add the hair base
    ### EMOTIONS
    add luna_mouth xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)#Add the mouth
    add "characters/luna/body/face/eye_white.png"  xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)
    add luna_pupil xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)#Add the pupil
    add luna_eye xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)#Add the eye outline
    add luna_eyebrow xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)#Add the eyebrow
    add "characters/luna/body/face/tears/tears_"+str(luna_tears)+".png"  xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)
    add "characters/luna/body/head/hair_"+str(luna_hair)+"_2.png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio) #add the hair overlayer

    if luna_wear_cum_under: #Luna cum but under clothes
        add "characters/luna/misc/cum_"+str(luna_cum)+".png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)# Add the top
    ### CLOTHES 
    if luna_wear_glasses:
        add luna_glasses xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)# Add the glasses
    if luna_wear_bra and not luna_wear_top:
        add luna_bra xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)# Add the bra
    if luna_wear_panties:
        add luna_panties xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)# Add the panties
    if luna_wear_skirt:
        add luna_skirt xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)# Add the skirt
    if luna_wear_top:
        add luna_top xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)# Add the top
    if luna_wear_acc:
        add luna_acc xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)# Add the accessory (jewellery)

    ### ARM OVERLAYS
    add "characters/luna/body/arms/left_"+str(luna_l_arm)+"_2.png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)#Add the left arm
    add "characters/luna/body/arms/right_"+str(luna_r_arm)+"_2.png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)#Add the right arm

    if luna_wear_cum:
        add "characters/luna/misc/cum_"+str(luna_cum)+".png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)# Add the top

    if genie_sprite_base == "characters/genie/base_4.png": #add genies dick for licking/sucking
        add "characters/genie/dick_1.png" xpos genie_sprite_xpos ypos genie_sprite_ypos
    if genie_sprite_base == "characters/genie/base_4.png" and not luna_wear_skirt and not luna_wear_panties: #add leg
        add "characters/luna/body/legs/right_1.png" xpos luna_xpos ypos luna_ypos xzoom luna_flip zoom (1.0/scaleratio)#Add the right leg cover for the dick. What's a thigh job called again?
    
    if luna_wear_cum and genie_sprite_base == "characters/genie/base_4.png":
        add "characters/luna/body/arms/right_4_2.png" xpos 390 ypos 0 xzoom luna_flip zoom (1.0/scaleratio)
    ### ZORDER
    zorder luna_zorder

screen luna_chibi:
    add luna_chibi_image xpos luna_chibi_xpos ypos luna_chibi_ypos xzoom luna_flip zoom (1.0/scaleratio)  
    zorder luna_chibi_zorder


label luna_main(text="",eye=None, pupil=None, eyebrow=None, mouth=None):
    if eye!=None and pupil!=None and eyebrow!=None and mouth!=None:
        $ changeLuna(eye, pupil, eyebrow, mouth)
    if text != "":
        $ renpy.say(lun, text)
    return

init python: ###Method Definition for new characters
    def luna_chibi( l_chibi=None, 
                    l_xpos=None,
                    l_ypos=None):

        ###DEFINE GLOBAL VARIABLES
        global luna_chibi_image
        global luna_chibi_xpos
        global luna_chibi_ypos
        ###HIDE OLD SCREEN
        renpy.hide_screen("luna_chibi")
        renpy.with_statement(Dissolve(0.3))

        if l_xpos is not None:
            luna_chibi_xpos = l_xpos

        if l_ypos is not None:
            luna_chibi_ypos = l_ypos

        if l_chibi is not None:
            if l_chibi == "stand":
                luna_chibi_image = "characters/luna/chibis/luna_stand.png" 
            if l_chibi == "stand_topless":
                luna_chibi_image = "characters/luna/chibis/luna_stand_topless.png" 
            if l_chibi == "stand_naked":
                luna_chibi_image = "characters/luna/chibis/walk/l_walk_n_01.png" 
            else:
                luna_chibi_image = luna_chibi_image

        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("luna_chibi")
        renpy.with_statement(Dissolve(0.3))

    def changeLuna( l_eye=None, 
                    l_pupil=None, 
                    l_eyebrow=None, 
                    l_mouth=None, 
                    x_pos=None, 
                    y_pos=None): # Luna
        ###DEFINE GLOBAL VARIABLES
        global luna_xpos
        global luna_ypos
        global luna_base
        global luna_cheeks
        global luna_eye
        global luna_pupil
        global luna_eyebrow
        global luna_mouth
        global luna_eyebrow
        global luna_skirt 
        global luna_top
        ###HIDE OLD SCREEN
        #renpy.hide_screen("luna")
        #renpy.with_statement(Dissolve(0.5))
        ###UPDATE UNIFORM
        luna_skirt = "characters/luna/clothes/uniform/skirt_"+str(luna_skirt_level)+".png" 
        luna_top = "characters/luna/clothes/uniform/top_"+str(luna_top_level)+".png" 

        ###MANUAL POSITION CONTROL
        if x_pos is not None:
            luna_xpos = x_pos
        else:
            luna_xpos = luna_xpos
        if y_pos is not None:
            luna_ypos = luna_ypos
        else:
            luna_ypos = luna_ypos
        ###MANUAL EMOTION AND BASE IMAGE CONTROL
        # if l_cheeks is not None:
            # if l_cheeks == 1:
                # luna_cheeks = "characters/luna/base/cheeks_01.png"
            # elif l_cheeks == 2:
                # luna_cheeks = "characters/luna/base/cheeks_02.png"
            # else:
                # luna_cheeks = luna_cheeks

        if l_eye is not None:
            luna_eye = "characters/luna/body/face/eye/"+str(l_eye)+".png" 

        if l_pupil is not None and not luna_unlocked:
            luna_pupil = "characters/luna/body/face/pupil/"+str(l_pupil)+".png" 
        if l_pupil is not None and luna_unlocked:
            luna_pupil = "characters/luna/body/face/pupil/"+str(l_pupil)+"_G.png" 
        if l_pupil is not None and luna_reverted:
            luna_pupil = "characters/luna/body/face/pupil/"+str(l_pupil)+".png" 

        if l_eyebrow is not None:
            luna_eyebrow = "characters/luna/body/face/eyebrow/"+str(l_eyebrow)+".png" 

        if l_mouth is not None:
            luna_mouth = "characters/luna/body/face/mouth/"+str(l_mouth)+".png" 
            
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("luna")
        renpy.with_statement(Dissolve(0.3))
        
        
        
        
        