

### HERMIONE GRANGER ###

label her_main(text="", mouth=None, eyes=None, eyebrows=None, pupils=None, cheeks=None, tears=None, extra=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):

    #Flip
    if flip == False: #Default
        $ hermione_flip = 1
    if flip == True: #Flipped
        $ hermione_flip = -1

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
        else:
            $ hermione_ypos = int(ypos)

    if face != None:
        if mouth == None:
            call set_her_face(mouth = face)
        if eyes == None:
            call set_her_face(eyes = face)
        if eyebrows == None:
            call set_her_face(eyebrows = face)
        if pupils == None:
            call set_her_face(pupils = face)

    if animation != False:
        $ hermione_animation = animation

    python:
        hermione_class.expression(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)
        hermione_class.special(emote=emote)

    if use_hermione_head and face_on_cg: #Only her face. Used in CG scenes.
        show screen hermione_face
    else:
        show screen hermione_main()
    show screen bld1

    call transition(trans, True)

    $ hermione_class.say(text)

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

    #TODO $ hermione_chibi.update()
    $ hermione_flip = 1
    $ use_hermione_head = False

    return

label end_her_event:
    call her_chibi("hide")
    hide screen hermione_main
    with d3
    pause.5

    call update_hermione

    $ active_girl = None
    $ hermione_busy = True

    call music_block
    jump main_room

screen hermione_main():
    tag hermione_main
    zorder hermione_zorder
    if hermione_animation != None:
        add hermione_class.get_image() xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio) at hermione_animation
    else:
        add hermione_class.get_image() xpos hermione_xpos ypos hermione_ypos xzoom hermione_flip zoom (1.0/hermione_scaleratio)
