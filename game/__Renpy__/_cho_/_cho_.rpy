

### Cho Chang ###

label cho_main(text="", mouth=False, eyes=False, eyebrows=False, pupils=False, cheeks=False, tears=False, extra=False, emote=False, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):

    #Flip
    if flip == False:
        $ cho_flip = 1 #Default
    if flip == True:
        $ cho_flip = -1

    #Positioning
    if xpos != None:
        if xpos in ["base","default"]:     # All the way to the right.
            $ cho_xpos = 640
        elif xpos == "left":
            $ cho_xpos = 200
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
                $ cho_xpos = -50
            else:
                $ cho_xpos = 660
            $ cho_ypos = 200
            $ cho_zorder = 8
        else:
            $ cho_ypos = int(ypos)

    if face:
        if not mouth:
            call set_cho_face(mouth = face)
        if not eyes:
            call set_cho_face(eyes = face)
        if not eyebrows:
            call set_cho_face(eyebrows = face)
        if not pupils:
            call set_cho_face(pupils = face)

    if animation != False:
        $ cho_animation = animation

    python:
        cho.set_face(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)
        #cho_class.special(emote=emote)

    if not renpy.get_screen("wardrobe_menu"):
        show screen cho_main()
    show screen bld1

    if trans:
        with trans

    if text:
        $ renpy.say(cho, text)

    if use_cho_head:
        hide screen cho_main

    return

label update_cho:

    # Chibi Update
    $ cho_chibi.update()
    $ cho_chibi.position(flip=False)
    $ cho_flip = 1
    hide screen cho_cloth_pile

    return

label end_cho_event:
    call cho_chibi("hide")
    hide screen cho_main
    with d3
    pause.5

    call update_cho

    $ active_girl = None
    $ cho_busy = True

    call music_block
    jump main_room

screen cho_main():
    tag cho_main
    zorder cho_zorder
    default cho_img = cho.get_image()
    if cho_animation != None:
        add cho_img xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) at cho_animation
    else:
        add cho_img xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio)
    
    on ("show", "replace") action Function(apply_doll_transition, cho, "cho_main", "cho_img", use_cho_head)

