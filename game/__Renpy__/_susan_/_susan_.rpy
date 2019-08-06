

### Susan Bones ###

label sus_main(text="", mouth=None, eye=None, brows=None, pupils=None, cheeks=None, tears=None, extra=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None):
    hide screen susan_main

    #Flip
    if flip == False:
        $ susan_flip = 1 #Default
    if flip == True:
        $ susan_flip = -1

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
            $ susan_xpos = 640
        elif xpos == "mid":                # Centered.
            $ susan_xpos = 300
        elif xpos == "right":              # Bit more to the right.
            $ susan_xpos = 400
        elif xpos in ["wardrobe","close"]:
            $ susan_xpos = 540
        else:
            $ susan_xpos = int(xpos)

    if ypos != None:
        if ypos in ["base","default"]:
            $ susan_ypos = 0
            $ susan_scaleratio = 2
            $ susan_zorder = 5
            $ use_susan_head = False
        elif ypos in ["head"]:
            # Use ypos="head" to activate her head position.
            # Use ypos="base" to disable it.
            # Use ypos="200" or any other number to move her head up or down.
            $ use_susan_head = True
            $ susan_scaleratio = 2

            if susan_flip == -1: #Flipped
                $ susan_xpos = 620
            else:
                $ susan_xpos = 590
            $ susan_ypos = 230
            $ susan_zorder = 8
        else:
            $ susan_ypos = int(ypos)

    if face != None:
        if mouth == None:
            call set_sus_face(mouth = face)
        if eye == None:
            call set_sus_face(eyes = face)
        if brows == None:
            call set_sus_face(brows = face)
        if pupils == None:
            call set_sus_face(pupils = face)

    $ changeSusan(mouth, eye, brows, pupils, cheeks, tears, extra, emote)

    show screen susan_main
    show screen bld1

    call transition(trans, True)

    if text != "":
        $ renpy.say(sus, text)

    if use_susan_head:
        hide screen susan_main

    return



label update_susan:
    $ susan_flip = 1
    $ use_susan_head = False

    call update_sus_uniform

    return



init python:
    def changeSusan(    mouth=None,
                        eye=None,
                        brows=None,
                        pupils=None,
                        cheeks=None,
                        tears=None,
                        extra=None,
                        emote=None):

        ### GLOBAL VARIABLES ###
        global susan_mouth
        global susan_eye
        global susan_eyebrow
        global susan_pupil
        global susan_cheeks
        global susan_tears
        global susan_extra
        global susan_emote

        ### FACE CONTROL ###
        if mouth is not None:
            susan_mouth       = "characters/susan/face/mouth/"+mouth+".png"
        if eye is not None:
            susan_eye         = "characters/susan/face/eyes/"+eye+".png"
        if brows is not None:
            susan_eyebrow     = "characters/susan/face/brow/"+brows+".png"
        if pupils is not None:
            susan_pupil       = "characters/susan/face/pupil/"+pupils+".png"
        if cheeks is not None:
            susan_cheeks      = "characters/susan/face/extras/"+cheeks+".png"
        if tears is not None:
            susan_tears       = "characters/susan/face/extras/"+tears+".png"
        if extra is not None:
            susan_extra       = "characters/susan/face/extras/"+extra+".png"
        if emote is not None:
            susan_emote       = "characters/emotes/"+str(emote)+".png"
