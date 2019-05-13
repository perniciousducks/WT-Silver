

label sna_main(text="", face="", xpos=None, ypos=None, flip=False, trans=None, remove=False, wand=False):
    hide screen snape_main
    hide screen snape_head

    #Flip
    if flip == False:
        $ snape_flip = 1 #Default
    if flip == True:
        $ snape_flip = -1

    if remove == True:
        hide screen bld1
        pause 0.1
        return

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
            $ snape_zorder = 5
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
            $ snape_zorder = 8
        else:
            $ snape_ypos = int(ypos)

    if face != "":
        $ s_sprite = "characters/snape/main/"+str(face)+".png"

    show screen snape_main(wand=wand)
    show screen bld1

    call transition(trans)

    if text != "":
        if "[hermione_name]" in text or "[genie_name]" in text:
            if "[genie_name]" in text:
                $ text = text.replace("[genie_name]",genie_name)
            if "[hermione_name]" in text:
                $ text = text.replace("[hermione_name]",hermione_name)
        sna "[text]"

    if use_snape_head:
        hide screen snape_main

    return


label sna_head(text="",face="",xpos=snape_head_xpos ,ypos=snape_head_ypos):
    hide screen snape_main
    hide screen snape_head
    show screen bld1

    if xpos != snape_head_xpos:
        if xpos == "base" or xpos == "default":
            $ snape_head_xpos = 540
        else:
            $ snape_head_xpos = xpos

    if ypos != snape_head_ypos:
        if ypos == "base" or ypos == "default":
            $ snape_head_ypos = 380
        else:
            $ snape_head_ypos = ypos

    if face != "":
        $ s_sprite = "characters/snape/main/"+str(face)+".png"

    show screen snape_head
    with d3

    if text != "":
        sna "[text]"
    hide screen snape_head
    with d3

    return



label update_snape:

    $ snape_flip = 1
    $ use_snape_head = False
    call update_sna_chibi

    return



### SNAPE FULL
screen snape_main(wand=False):
    tag big_snape

    add s_sprite xpos snape_xpos ypos snape_ypos xzoom snape_flip zoom (1.0/snape_scaleratio)#tt_xpos+140 ypos tt_ypos
    if wand:
        add "characters/snape/main/wand.png" xpos snape_xpos ypos snape_ypos xzoom snape_flip zoom (1.0/snape_scaleratio)
    zorder snape_zorder

screen snape_picture_frame():
    add "characters/snape/main/picture_frame.png" xpos snape_xpos ypos snape_ypos xzoom snape_flip zoom (1.0/snape_scaleratio)
    zorder snape_zorder+1



### SNAPE HEAD
screen snape_head():
    tag big_snape

    add s_sprite xpos snape_head_xpos ypos snape_head_ypos zoom (1.0/snape_scaleratio)

    zorder 8 #In front of text box.


### SNAPE EMOTIONS
screen s_emo_01(): #Closed eyes and closed mouth.
    tag semo

    add "characters/snape/main/s_emo_01.png" xpos tt_xpos ypos tt_ypos xzoom snape_flip zoom (1.0/snape_scaleratio)

    zorder 4
