

### Astoria Greengrass ###

label ast_main(text="", mouth=None, eye=None, eyebrow=None, pupil=None, cheeks=None, tears=None, extra=None, emote=None, xpos=None, ypos=None, flip=None, trans=None):
    hide screen astoria_main

    #Flip
    if flip == False:
        $ astoria_flip = 1 #Default
    if flip == True:
        $ astoria_flip = -1

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
        if xpos in ["base","default"]: #All the way to the right.
            $ astoria_xpos = 640
            $ menu_x = 0.1 #Don't add ypos!
        elif xpos == "mid":                     #Centered.
            $ astoria_xpos = 300
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos == "right":                   #Bit more to the right.
            $ astoria_xpos = 400
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos in ["wardrobe","close"]:
            $ astoria_xpos = 540
        else:
            $ astoria_xpos = int(xpos)

    if ypos != None:
        if ypos in ["base","default"]:
            $ astoria_ypos = 0
            $ astoria_scaleratio = 2
            $ astoria_zorder = 5
            $ use_astoria_head = False
        elif ypos in ["head"]: #Use ypos="head" to activate her head position. Use ypos="base" to disable it. Use ypos="200" or any other number to move her head up or down.
            $ use_astoria_head = True
            $ astoria_scaleratio = 2 #Reset

            if astoria_flip == -1: #Flipped
                $ astoria_xpos = 620
            else:
                $ astoria_xpos = 590
            $ astoria_ypos = 230
            $ astoria_zorder = 8
        else:
            $ astoria_ypos = int(ypos)

    $ changeAstoria(mouth, eye, eyebrow, pupil, cheeks, tears, extra, emote)

    show screen astoria_main
    show screen bld1

    #Transitions
    call transition(trans)

    if text != "":
        $ renpy.say(ast, text)

    if use_astoria_head:
        hide screen astoria_main

    return



label update_astoria:

    $ astoria_flip = 1
    $ use_astoria_head = False

    return


label set_ast_susan_name:
    $ ast_susan_name = renpy.random.choice(["Susy","Cow","Cow Tits","Milk Bag","Slut","Whore","Piggy","Pig","Bessie","Moo Moo"])
    return

label set_ast_tonks_name:
    $ ast_tonks_name = renpy.random.choice(["Hag","Old Hag","Punk","Dyke","Lesbo"])
    return



init python:
    def changeAstoria(  mouth=None,
                        eye=None,
                        eyebrow=None,
                        pupil=None,
                        cheeks=None,
                        tears=None,
                        extra=None,
                        emote=None):

        ###DEFINE GLOBAL VARIABLES
        global astoria_mouth
        global astoria_eye
        global astoria_eye_bg
        global astoria_eyebrow
        global astoria_pupil
        global astoria_cheeks
        global astoria_tears
        global astoria_extra
        global astoria_emote

        ### FACE CONTROL ###
        if mouth is not None:
            astoria_mouth       = "characters/astoria/face/mouth/"+mouth+".png"
        if eye is not None:
            astoria_eye         = "characters/astoria/face/eyes/"+eye+".png"
            astoria_eye_bg      = "characters/astoria/face/eyes/"+eye+"_bg.png"
        if eyebrow is not None:
            astoria_eyebrow     = "characters/astoria/face/brow/"+eyebrow+".png"
        if pupil is not None:
            astoria_pupil       = "characters/astoria/face/pupil/"+pupil+".png"
        if cheeks is not None:
            astoria_cheeks      = "characters/astoria/face/extras/cheeks_"+cheeks+".png"
        if tears is not None:
            astoria_tears       = "characters/astoria/face/extras/tears_"+tears+".png"
        if extra is not None:
            astoria_extra       = "characters/astoria/face/extras/"+extra+".png"
        if emote is not None:
            astoria_emote       = "characters/emotes/"+str(emote)+".png"
