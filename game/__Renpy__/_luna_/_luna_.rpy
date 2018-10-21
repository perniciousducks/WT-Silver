

### LUNA LOVEGOOD ###

label lun_main(text="", mouth=None, eye=None, eyebrow=None, pupil=None, cheeks=None, tears=None, extra=None, xpos=None, ypos=None, trans=None):
    hide screen luna_main

    #Reset
    if cheeks == None:
        $ cheeks = "blank"
    if tears == None:
        $ tears = "blank"
    if extra == None:
        $ extra = "blank"

    #Positioning
    if xpos != None:
        if xpos in ["base","default"]: #All the way to the right.
            $ luna_xpos = 640
            $ menu_x = 0.1 #Don't add ypos!
        elif xpos == "mid":                     #Centered.
            $ luna_xpos = 300
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos == "right":                   #Bit more to the right.
            $ luna_xpos = 400
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos in ["wardrobe","close"]:
            $ luna_xpos = 540
        else:
            $ luna_xpos = int(xpos)

    if ypos != None:
        if ypos in ["base","default"]:
            $ luna_ypos = 0
            $ luna_zorder = 5
        elif ypos == "head":
            $ luna_ypos = 400 #Not the correct number!
            #$ luna_zorder = 8 #ADD zorder change to be in front of textbox!
        else:
            $ luna_ypos = int(ypos)
            $ luna_zorder = 5


    call update_luna_chibi_uniform
    $ changeLuna(mouth, eye, eyebrow, pupil, luna_xpos, luna_ypos, cheeks, tears, extra)

    show screen luna_main
    show screen bld1

    #Transitions
    call transition(trans)

    if text != "":
        $ renpy.say(lun, text)

    return



label luna_away:
    call luna_reset
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



label luna_reset:
    $ luna_flip = 1

    call update_lun_uniform
    call load_luna_clothing_saves
    call update_luna_chibi_uniform

    $ luna_wear_cum = False
    $ luna_wear_cum_under = False

    return

label reset_luna_main: #Not in use (?)
    return

label luna_no_money:
    call lun_main("You expect me to do it for free?", "angry", "mad", "mad", "R")
    call lun_main("Hmph!", "angry", "mad", "mad", "R")
    jump luna_away










init python: ###Method Definition for new characters
    def changeLuna( mouth=None,
                    eye=None,
                    eyebrow=None,
                    pupil=None,
                    x_pos=None,
                    y_pos=None,
                    cheeks=None,
                    tears=None,
                    extra=None):

        ###DEFINE GLOBAL VARIABLES
        global luna_mouth
        global luna_eye
        global luna_eye_bg
        global luna_eyebrow
        global luna_pupil
        global luna_xpos
        global luna_ypos
        global luna_cheeks
        global luna_tears
        global luna_extra

        ###EMOTION CONTROL
        if mouth is not None:
            luna_mouth = "characters/luna/face/mouth/"+str(mouth)+".png"
        if eye is not None:
            luna_eye = "characters/luna/face/eye/"+str(eye)+".png"
        if eyebrow is not None:
            luna_eyebrow = "characters/luna/face/eyebrow/"+str(eyebrow)+".png"
        if pupil is not None:
            luna_pupil = "characters/luna/face/pupil/"+str(luna_pupil_color)+"/"+str(pupil)+".png"

        ###POSITION CONTROL
        if x_pos is not None:
            luna_xpos        = x_pos
        if y_pos is not None:
            luna_ypos        = y_pos

        ###BODY CONTROL
        if cheeks is not None:
            luna_cheeks      = "characters/luna/face/extras/cheeks_"+str(cheeks)+".png"
        if tears is not None:
            luna_tears       = "characters/luna/face/extras/tears_"+str(tears)+".png"
        if extra is not None:
            luna_extra       = "characters/luna/face/extras/"+str(extra)+".png"

#LUNA PLOT
#Turned into a bitchy Slytherin by the sorting hat. Willing to do anything for money/fame/status. Incredibly vain

#Don't forget to incorporate the quibbler
###PLOT###--------------------------------------------------------
#After the sex favour, Luna will either return to normal if you choose the sub route or she will become a slytherin dom if you go the dom route
#All the private favours will then have a 4th level unlocked, tailored to either the sub or dom option
