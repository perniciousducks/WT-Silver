
label sna_main(text="", face="", xpos=None, ypos=None, flip=False, trans=None, wand=False):

    #Flip
    if flip == False:
        $ snape_flip = 1 #Default
    if flip == True:
        $ snape_flip = -1

    #Positioning
    if xpos != None:
        if xpos in ["base","default"]:     # All the way to the left.
            $ snape_xpos = 525
        elif xpos == "mid":                # Centered.
            $ snape_xpos = 300
        elif xpos == "right":              # Bit more to the right.
            $ snape_xpos = 400
        elif xpos in ["wardrobe","close"]:
            $ snape_xpos = 495
        else:
            $ snape_xpos = int(xpos)

    if ypos != None:
        if ypos in ["base","default"]:
            $ snape_ypos = 0
            $ snape_scaleratio = 2
            $ snape_zorder = 15
            $ use_snape_head = False
        elif ypos in ["head"]:
            # Use ypos="head" to activate her head position.
            # Use ypos="base" to disable it.
            # Use ypos="200" or any other number to move her head up or down.
            $ use_snape_head = True
            $ snape_scaleratio = 2

            if snape_flip == -1: #Flipped #Head is on the left side.
                $ snape_xpos = -50
            else:
                $ snape_xpos = 615
            $ snape_ypos = 320
            $ snape_zorder = 18
        else:
            $ snape_ypos = int(ypos)

    $ old_s_sprite = s_sprite
    if face != "":
        $ s_sprite = "characters/snape/main/"+str(face)+".png"

    if not renpy.get_screen("snape_main"):
        $ old_s_sprite = s_sprite # Forget old sprite if screen is currently hidden

    show screen snape_main(old_s_sprite, s_sprite, wand)
    show screen bld1

    if trans:
        with trans

    if text:
        $ renpy.say(sna, text)

    if use_snape_head:
        hide screen snape_main

    return


label update_snape:
    $ snape_flip = 1
    $ use_snape_head = False
    return


screen snape_main(old_sprite=s_sprite, new_sprite=s_sprite, wand=False):
    tag big_snape
    zorder snape_zorder
    sensitive False

    add doll_transition(old_sprite, new_sprite):
        xpos snape_xpos ypos snape_ypos xzoom snape_flip zoom (1.0/snape_scaleratio)

    if wand:
        add "characters/snape/main/wand.png" xpos snape_xpos ypos snape_ypos xzoom snape_flip zoom (1.0/snape_scaleratio)

screen snape_picture_frame():
    add "characters/snape/main/picture_frame.png" xpos snape_xpos ypos snape_ypos xzoom snape_flip zoom (1.0/snape_scaleratio)
    zorder snape_zorder+1
