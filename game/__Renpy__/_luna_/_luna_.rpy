

### Luna Lovegood ###

label lun_main(text="", mouth=None, eye=None, brows=None, pupils=None, cheeks=None, tears=None, extra=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None):
    hide screen luna_main

    #Flip
    if flip == False:
        $ luna_flip = 1 #Default
    if flip == True:
        $ luna_flip = -1

    #Reset
    if cheeks == None:
        $ cheeks = "blank"
    if tears == None:
        $ tears = "blank"
    if extra == None:
        $ extra = "blank"
    if emote == None:
        $ emote = "blank"

    #Positioning
    if xpos != None:
        if xpos in ["base","default"]:     # All the way to the right.
            $ luna_xpos = 640
        elif xpos == "mid":                # Centered.
            $ luna_xpos = 300
        elif xpos == "right":              # Bit more to the right.
            $ luna_xpos = 400
        elif xpos in ["wardrobe","close"]:
            $ luna_xpos = 540
        else:
            $ luna_xpos = int(xpos)

    if ypos != None:
        if ypos in ["base","default"]:
            $ luna_ypos = 0
            $ luna_scaleratio = 2
            $ luna_zorder = 5
            $ use_luna_head = False
        elif ypos in ["head"]:
            # Use ypos="head" to activate her head position.
            # Use ypos="base" to disable it.
            # Use ypos="200" or any other number to move her head up or down.
            $ use_luna_head = True
            $ luna_scaleratio = 2

            if luna_flip == -1: #Flipped
                $ luna_xpos = 620
            else:
                $ luna_xpos = 590
            $ luna_ypos = 230
            $ luna_zorder = 8
        else:
            $ luna_ypos = int(ypos)

    call update_luna_chibi_uniform

    if face != None:
        if mouth == None:
            call set_lun_face(mouth = face)
        if eye == None:
            call set_lun_face(eyes = face)
        if brows == None:
            call set_lun_face(brows = face)
        if pupils == None:
            call set_lun_face(pupils = face)

    $ changeLuna(mouth, eye, brows, pupils, cheeks, tears, extra, emote)

    show screen luna_main
    show screen bld1

    call transition(trans, True)

    if text != "":
        $ renpy.say(lun, text)

    if use_luna_head:
        hide screen luna_main

    return



label luna_away:
    call reset_luna
    call gen_chibi("sit_behind_desk")

    if luna_chibi_xpos_name in ["desk"]:
        call lun_chibi("stand","desk","base")
    elif luna_chibi_xpos_name in ["mid"]:
        call lun_chibi("stand","mid","base")
    else:
        call lun_chibi("hide")

    hide screen blkfade
    with d3

    if luna_chibi_xpos_name in ["desk"]:
        call lun_walk("desk","leave",2.7)
    if luna_chibi_xpos_name in ["mid"]:
        call lun_walk("mid","leave",2)

    $ luna_busy = True

    jump main_room



label end_luna_event:

    call hide_characters
    call lun_chibi("hide")
    call gen_chibi("sit_behind_desk")
    hide screen blkfade
    hide screen blktone
    hide screen bld1
    with d3

    call reset_luna

    $ luna_busy = True

    jump main_room


label reset_luna:

    call load_luna_clothing_saves

    $ luna_wear_cum = False
    $ luna_wear_cum_under = False

    call update_luna

    return


label update_luna:
    $ luna_flip = 1
    $ use_luna_head = False
    $ luna_l_arm             = 1
    $ luna_r_arm             = 1

    call update_lun_uniform
    call update_luna_chibi_uniform

    return





label luna_no_money:
    call lun_main("You expect me to do it for free?", "angry", "mad", "mad", "R")
    call lun_main("Hmph!", "angry", "mad", "mad", "R")
    jump luna_away


#LUNA PLOT
#Turned into a bitchy Slytherin by the sorting hat. Willing to do anything for money/fame/status. Incredibly vain

#Don't forget to incorporate the quibbler
###PLOT###--------------------------------------------------------
#After the sex favour, Luna will either return to normal if you choose the sub route or she will become a slytherin dom if you go the dom route
#All the private favours will then have a 4th level unlocked, tailored to either the sub or dom option









init python: ###Method Definition for new characters
    def changeLuna( mouth=None,
                    eye=None,
                    brows=None,
                    pupils=None,
                    cheeks=None,
                    tears=None,
                    extra=None,
                    emote=None):

        ### DEFINE GLOBAL VARIABLES ###
        global luna_mouth
        global luna_eye
        global luna_eyebrow
        global luna_pupil
        global luna_cheeks
        global luna_tears
        global luna_extra
        global luna_emote

        ### FACE CONTROL ###
        if mouth is not None:
            luna_mouth       = "characters/luna/face/mouth/"+str(mouth)+".png"
        if eye is not None:
            luna_eye         = "characters/luna/face/eyes/"+str(eye)+".png"
        if brows is not None:
            luna_eyebrow     = "characters/luna/face/brow/"+str(brows)+".png"
        if pupils is not None:
            luna_pupil       = "characters/luna/face/pupil/"+str(luna_pupil_color)+"/"+str(pupils)+".png"
        if cheeks is not None:
            luna_cheeks      = "characters/luna/face/extras/cheeks_"+str(cheeks)+".png"
        if tears is not None:
            luna_tears       = "characters/luna/face/extras/tears_"+str(tears)+".png"
        if extra is not None:
            luna_extra       = "characters/luna/face/extras/"+str(extra)+".png"
        if emote is not None:
            luna_emote       = "characters/emotes/"+str(emote)+".png"
