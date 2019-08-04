### Tonks###

label ton_main(text="", mouth=None, eyes=None, eyebrows=None, pupils=None, hair=None, cheeks=None, tears=None, extra=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):

    #Flip
    if flip == False:
        $ tonks_flip = 1 #Default
    if flip == True:
        $ tonks_flip = -1

    #Reset
    if cheeks == None:
        $ cheeks = "blank"
    if tears == None:
        $ tears = "blank"
    if extra == None:
        $ extra = "blank"
    if emote == None:
        $ emote = "blank"
    if hair == None:
        $ tonks_class.get_cloth("hair").color = tonks_haircolor

    #Positioning
    if xpos != None:
        if xpos in ["base","default"]:     # All the way to the right.
            $ tonks_xpos = 640
        elif xpos == "left":
            $ tonks_xpos = 200
        elif xpos == "mid":                # Centered.
            $ tonks_xpos = 300
        elif xpos == "right":              # Bit more to the right.
            $ tonks_xpos = 400
        elif xpos in ["wardrobe","close"]:
            $ tonks_xpos = 540
        else:
            $ tonks_xpos = int(xpos)

    if ypos != None:
        if ypos in ["base","default"]:
            $ tonks_ypos = 0
            $ tonks_scaleratio = 2
            $ tonks_zorder = 5
            $ use_tonks_head = False
        elif ypos in ["head"]:
            $ use_tonks_head = True
            $ tonks_scaleratio = 2

            if tonks_flip == -1: #Flipped
                $ tonks_xpos = -50
            else:
                $ tonks_xpos = 590
            $ tonks_ypos = 200
            $ tonks_zorder = 8
        else:
            $ tonks_ypos = int(ypos)

    if face != None:
        if mouth == None:
            call set_ton_face(mouth = face)
        if eyes == None:
            call set_ton_face(eyes = face)
        if eyebrows == None:
            call set_ton_face(eyebrows = face)
        if pupils == None:
            call set_ton_face(pupils = face)
        if hair == None:
            call set_ton_face(hair = face)

    # Hair color changes
    if hair != None:
        if hair in ("red", "angry", "furious"):
            $ tonks_class.get_cloth("hair").color = [[164, 34, 34, 255]]
        elif hair in ("orange", "upset", "annoyed"):
            $ tonks_class.get_cloth("hair").color = [[228, 93, 34, 255]]
        elif hair in ("yellow", "happy", "cheerful"):
            $ tonks_class.get_cloth("hair").color = [[240, 240, 50, 255]]
        elif hair in ("green", "disgusted"):
            $ tonks_class.get_cloth("hair").color = [[111, 205, 75, 255]]
        elif hair in ("blue", "sad"):
            $ tonks_class.get_cloth("hair").color = [[64, 75, 205, 255]]
        elif hair in ("purple"):
            $ tonks_class.get_cloth("hair").color = [[205, 75, 205, 255]]
        elif hair in ("white", "scared"):
            $ tonks_class.get_cloth("hair").color = [[238, 238, 241, 255]]
        elif hair in ("pink", "horny"):
            $ tonks_class.get_cloth("hair").color = [[242, 126, 168, 255]]
        else: # RANDOM limited from 50 to 235 for better outcome
            $ tonks_class.get_cloth("hair").color = [[random.randint(50, 235), random.randint(50, 235), random.randint(50, 235), 255]]
        # Clear cache and redraw
        $ tonks_class.get_cloth("hair").cached = False

    if animation != False:
        $ tonks_animation = animation

    python:
        tonks_class.expression(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)
        tonks_class.special(emote=emote)

    show screen tonks_main()
    show screen bld1

    call transition(trans, True)

    $ tonks_class.say(text)

    if use_tonks_head:
        hide screen tonks_main

    return



label update_tonks:
    return
    # Chibi Update
    #$ update_chibi_image("tonks")
    #$ tonks_flip = 1
    #$ tonks_cloth_pile = False
    return


label end_tonks_event:
    #call tonks_chibi("hide")
    hide screen tonks_main
    with d3
    pause.5

    call update_tonks

    $ active_girl = None
    $ tonks_busy = True

    jump main_room

screen tonks_main():
    tag tonks_main
    zorder tonks_zorder
    if tonks_animation != None:
        add tonks_class.get_image() xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) at tonks_animation
    else:
        add tonks_class.get_image() xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)
