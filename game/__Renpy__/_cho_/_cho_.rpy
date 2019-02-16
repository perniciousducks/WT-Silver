

### Cho Chang ###

label cho_main(text="", mouth=None, eye=None, brows=None, pupils=None, cheeks=None, tears=None, extra=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None):
    hide screen cho_chang

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
            $ cho_scaleratio = 2
            $ cho_zorder = 5
            $ use_cho_head = False
        elif ypos in ["head"]: #Use ypos="head" to activate her head position. Use ypos="base" to disable it. Use ypos="200" or any other number to move her head up or down.
            $ use_cho_head = True
            $ cho_scaleratio = 2 #Reset

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
        if eye == None:
            call set_cho_face(eyes = face)
        if brows == None:
            call set_cho_face(brows = face)
        if pupils == None:
            call set_cho_face(pupils = face)

    $ changeCho(mouth, eye, brows, pupils, cheeks, tears, extra, emote) #<--- Legacy

    show screen cho_chang
    show screen bld1

    #Transitions
    call transition(trans)

    #if text != "":
        #$ renpy.say(cho, text) <--- Legacy
    
    # New class call for character say
    $ cho_class.say(text)

    if use_cho_head:
        hide screen cho_chang

    return



label update_cho:

    $ cho_flip = 1
    $ use_cho_head = False

    return


label end_cho_event:
    hide screen cho_chang
    with d3

    call set_cho_outfit(None)
    call load_cho_clothing_saves #Resets Cho's clothing.

    #Add more cho screens to hide here.
    #Do not add transitions!

    $ cho_busy = True

    jump main_room



init python: ###Method Definition for new characters
    def changeCho(  mouth=None,
                    eye=None,
                    brows=None,
                    pupils=None,
                    cheeks=None,
                    tears=None,
                    extra=None,
                    emote=None):

        ### DEFINE GLOBAL VARIABLES ###
        global cho_mouth
        global cho_eye
        global cho_eyebrow
        global cho_pupil
        global cho_cheeks
        global cho_tears
        global cho_extra
        global cho_emote

        ### FACE CONTROL ###
        if mouth is not None:
            cho_mouth         = mouth
        if eye is not None:
            cho_eye           = eye
        if brows is not None:
            cho_eyebrow       = brows
        if pupils is not None:
            cho_pupil         = pupils
        if cheeks is not None:
            cho_cheeks        = cheeks
        if tears is not None:
            cho_tears         = tears
        if extra is not None:
            cho_extra         = extra
        if emote is not None:
            cho_emote         = str(emote)
        
        # Use cho_class.expression to change expressions
        cho_class.expression(mouth=cho_mouth, eyes=cho_eye, eyebrows=cho_eyebrow, pupils=cho_pupil, cheeks=cho_cheeks, tears=cho_tears)
        cho_class.special(emote=cho_emote)
        #extras=cho_extra, emote=cho_emote
        
        
        
        
        #if mouth is not None:
        #    cho_mouth         = "characters/cho/face/mouth/"+mouth+".png"
        #if eye is not None:
        #    cho_eye           = "characters/cho/face/eyes/"+eye+".png"
        #if brows is not None:
        #    cho_eyebrow       = "characters/cho/face/brow/"+brows+".png"
        #if pupils is not None:
        #    cho_pupil         = "characters/cho/face/pupil/"+pupils+".png"
        #if cheeks is not None:
        #    cho_cheeks        = "characters/cho/face/extras/cheeks_"+cheeks+".png"
        #if tears is not None:
        #    cho_tears         = "characters/cho/face/extras/tears_"+tears+".png"
        #if extra is not None:
        #    cho_extra         = "characters/cho/face/extras/"+extra+".png"
        #if emote is not None:
        #    cho_emote         = "characters/emotes/"+str(emote)+".png"
