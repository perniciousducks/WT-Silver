

### Cho Chang ###

label cho_main(text="", mouth=None, eye=None, eyebrow=None, pupil=None, xpos=None, ypos=None, trans=None):
    hide screen cho_chang

    #Reset
    #if cheeks == None:
    #    $ cheeks = "blank"
    #if tears == None:
    #    $ tears = "blank"

    #Positioning
    if xpos != None:
        if xpos in ["base","default"]: #All the way to the right.
            $ cho_xpos = 640
            $ menu_x = 0.1 #Don't add ypos!
        elif xpos == "mid":                     #Centered.
            $ cho_xpos = 300
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos == "right":                   #Bit more to the right.
            $ cho_xpos = 400
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos in ["wardrobe","close"]:
            $ cho_xpos = 540
        else:
            $ cho_xpos = int(xpos)

    if ypos != None:
        if ypos in ["base","default"]:
            $ cho_ypos = 0
        elif ypos == "head":
            $ cho_ypos = 400 #Not the correct number!
            #ADD zorder change to be in front of textbox!
        else:
            $ cho_ypos = int(ypos)

    $ changeCho(mouth, eye, eyebrow, pupil, cho_xpos, cho_ypos)

    show screen cho_chang
    show screen bld1

    #Transitions
    call transition(trans)

    if text != "":
        $ renpy.say(cho, text)

    return




label end_cho_event:
    hide screen cho_chang
    with d3

    call cho_outfit(None)
    call load_cho_clothing_saves #Resets Cho's clothing.

    #Add more cho screens to hide here.
    #Do not add transitions!

    $ cho_busy = True

    jump main_room
