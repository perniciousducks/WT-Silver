###SCREEN CODE FOR GENIE
screen genie_main:
    tag genie_main

    add genie_base xpos genie_xpos ypos genie_ypos xzoom genie_flip zoom (1.0/genie_scaleratio)#Add the base body
    add genie_face xpos genie_xpos ypos genie_ypos xzoom genie_flip zoom (1.0/genie_scaleratio)#Add genie expression

    zorder genie_zorder

label gen_main(text="", face=None, xpos=None, ypos=None, trans=None):
    hide screen genie_main

    #Positioning
    if xpos != None:
        if xpos in ["base","default"]: #All the way to the left.
            $ genie_xpos = 130
        elif xpos == "mid":                     #Centered.
            $ genie_xpos = 300
        elif xpos == "right":                   #Bit more to the right.
            $ genie_xpos = 400
        elif xpos in ["wardrobe","close"]:
            $ genie_xpos = 540
        else:
            $ genie_xpos = int(xpos)

    if ypos != None:
        if ypos in ["base","default"]:
            $ genie_ypos = 0
            $ genie_zorder = 5
        elif ypos == "head":
            $ genie_ypos = 400 #Not the correct number!
            #$ genie_zorder = 8 #ADD zorder change to be in front of textbox!
        else:
            $ genie_ypos = int(ypos)
            $ genie_zorder = 5

    if face != None:
        $ genie_face = "characters/genie/face/"+str(face)+".png"

    show screen genie_main
    show screen bld1

    #Transitions
    call transition(trans)

    if text != "":
        $ renpy.say(msp,text)

    return
