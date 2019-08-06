

### Genie ###

label gen_main(text="", face=None, xpos=None, ypos=None, flip=True, trans=None):
    hide screen genie_main

    #Flip
    if flip == False:
        $ genie_flip = -1
    if flip == True:
        $ genie_flip = 1 # Default, facing right.

    #Positioning
    if xpos != None:
        if xpos in ["base","default"]:     # All the way to the left.
            $ genie_xpos = 130
        elif xpos == "mid":                # Centered.
            $ genie_xpos = 300
        elif xpos == "right":              # Bit more to the right.
            $ genie_xpos = 400
        elif xpos in ["wardrobe","close"]:
            $ genie_flip = -1 # Facing left.
            $ genie_xpos = 575
        else:
            $ genie_xpos = int(xpos)

    if ypos != None:
        if ypos in ["base","default"]:
            $ genie_ypos = 0
            $ genie_scaleratio = 2
            $ genie_zorder = 4
            $ use_genie_head = False
        elif ypos in ["head"]:
            # Use ypos="head" to activate her head position.
            # Use ypos="base" to disable it.
            # Use ypos="200" or any other number to move her head up or down.
            $ use_genie_head = True
            $ genie_scaleratio = 2

            if genie_flip == -1: # Flipped
                $ genie_xpos = 590
            else:
                $ genie_xpos = 620
            $ genie_ypos = 230
            $ genie_zorder = 8
        else:
            $ genie_ypos = int(ypos)

        if xpos in ["wardrobe"]:
            $ genie_zorder = 5

    if face != None:
        $ genie_face = "characters/genie/face/"+str(face)+".png"

    show screen genie_main
    show screen bld1

    call transition(trans, True)

    if text != "":
        $ renpy.say(gen, text)

    if use_genie_head:
        hide screen genie_main

    return



# Genie Screens.

screen genie_main():
    tag genie_main

    add genie_base xpos genie_xpos ypos genie_ypos xzoom genie_flip zoom (1.0/genie_scaleratio)#Add the base body
    add genie_face xpos genie_xpos ypos genie_ypos xzoom genie_flip zoom (1.0/genie_scaleratio)#Add genie expression

    zorder genie_zorder



label update_genie:

    $ genie_flip = 1
    $ genie_scaleratio = 2 #Reset
    $ genie_zorder = 4 #Needs to stay behind other sprites, namely Hermione & Luna (zorder 5)
    $ use_genie_head = False
    call update_gen_chibi

    return
