

### Cho Chang ###

label cho_main(text="", mouth=None, eyes=None, eyebrows=None, pupils=None, cheeks=None, tears=None, extra=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None):

    #Flip
    if flip == False:
        $ cho_flip = 1 #Default
    if flip == True:
        $ cho_flip = -1

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
            $ cho_xpos = 640
        elif xpos == "mid":                # Centered.
            $ cho_xpos = 300
        elif xpos == "right":              # Bit more to the right.
            $ cho_xpos = 400
        elif xpos in ["wardrobe","close"]:
            $ cho_xpos = 540
        else:
            $ cho_xpos = int(xpos)

    if ypos != None:
        if ypos in ["base","default"]:
            $ cho_ypos = 0
            $ cho_scaleratio = 2
            $ cho_zorder = 5
            $ use_cho_head = False
        elif ypos in ["head"]:
            # Use ypos="head" to activate her head position.
            # Use ypos="base" to disable it.
            # Use ypos="200" or any other number to move her head up or down.
            $ use_cho_head = True
            $ cho_scaleratio = 2

            if cho_flip == -1: #Flipped
                $ cho_xpos = 620
            else:
                $ cho_xpos = 590
            $ cho_ypos = 230
            $ cho_zorder = 8
        else:
            $ cho_ypos = int(ypos)

    if face != None:
        if mouth == None:
            call set_cho_face(mouth = face)
        if eyes == None:
            call set_cho_face(eyes = face)
        if eyebrows == None:
            call set_cho_face(eyebrows = face)
        if pupils == None:
            call set_cho_face(pupils = face)

    python:
        cho_class.expression(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)
        cho_class.special(emote=emote)

    show screen cho_chang
    show screen bld1

    #Transitions
    call transition(trans)

    $ cho_class.say(text)

    if use_cho_head:
        hide screen cho_chang

    return

label end_cho_event:
    call play_sound("door")
    hide screen cho_chang
    pause.5
    $ active_girl = None
    jump main_room

screen cho_chang():
    tag cho_main
    zorder cho_zorder
    add cho_class.get_image() xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) at moveFade
