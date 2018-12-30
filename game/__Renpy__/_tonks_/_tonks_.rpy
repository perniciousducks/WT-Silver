

### Tonks ###

label ton_main(text="",mouth=None,eye=None, brows=None, pupils=None, cheeks=None, tears=None, extra=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None):
    hide screen tonks_main

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

    #Positioning
    if xpos != None:
        if xpos in ["base","default"]: #All the way to the right.
            $ tonks_xpos = 640
            $ menu_x = 0.1 #Don't add ypos!
        elif xpos == "mid":                     #Centered.
            $ tonks_xpos = 300
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos == "right":                   #Bit more to the right.
            $ tonks_xpos = 400
            $ menu_x = 0.5 #Don't add ypos!
        elif xpos == "wardrobe":
            $ tonks_xpos = 540
        else:
            $ tonks_xpos = int(xpos)

    if ypos != None:
        if ypos in ["base","default"]:
            $ tonks_ypos = 0
            $ tonks_scaleratio = 2
            $ tonks_zorder = 5
            $ use_tonks_head = False
        elif ypos in ["head"]: #Use ypos="head" to activate her head position. Use ypos="base" to disable it. Use ypos="200" or any other number to move her head up or down.
            $ use_tonks_head = True
            $ tonks_scaleratio = 2 #Reset

            if tonks_flip == -1: #Flipped
                $ tonks_xpos = 620
            else:
                $ tonks_xpos = 590
            $ tonks_ypos = 230
            $ tonks_zorder = 8
        else:
            $ tonks_ypos = int(ypos)

    if face != None:
        if mouth == None:
            call set_ton_face(mouth = face)
        if eye == None:
            call set_ton_face(eyes = face)
        if brows == None:
            call set_ton_face(brows = face)
        if pupils == None:
            call set_ton_face(pupils = face)

    call update_tonks_tongue_piercing(mouth)
    $ changeTonks(mouth, eye, brows, pupils, cheeks, tears, extra, emote)

    show screen tonks_main
    show screen bld1

    #Transitions
    call transition(trans)

    if text != "":
        $ renpy.say(ton, text)

    if use_tonks_head:
        hide screen tonks_main

    return

label update_tonks_tongue_piercing(mouth=None):
    if mouth != None:
        if mouth in ["open","horny","open_wide_tongue"]: #Tongue is visible.
            $ tonks_tongue_piercing = "characters/tonks/accessories/piercings/base/mouth/" +str(ton_tongue_piercing)+ "_" +str(mouth)+ ".png"
        else:
            $ tonks_tongue_piercing = "blank.png"
    if ton_tongue_piercing == "blank":
        $ tonks_tongue_piercing = "blank.png"

    return

label update_tonks:

    $ tonks_flip = 1
    $ use_tonks_head = False

    return


label check_tonks_clothing_upgrades:

    $ upgradable_clothing = []
    if hg_cheer_g_ITEM.unlocked and not hg_cheer_g_sexy_ITEM.unlocked:
        $ upgradable_clothing.append(hg_cheer_g_sexy_ITEM)
    if hg_cheer_s_ITEM.unlocked and not hg_cheer_s_sexy_ITEM.unlocked:
        $ upgradable_clothing.append(hg_cheer_s_sexy_ITEM)
    if hg_cheer_r_ITEM.unlocked and not hg_cheer_r_sexy_ITEM.unlocked:
        $ upgradable_clothing.append(hg_cheer_r_sexy_ITEM)
    if hg_cheer_h_ITEM.unlocked and not hg_cheer_h_sexy_ITEM.unlocked:
        $ upgradable_clothing.append(hg_cheer_h_sexy_ITEM)

    if ag_costume_lazy_town_ITEM.unlocked and not ag_costume_lazy_town_short_ITEM.unlocked:
        $ upgradable_clothing.append(ag_costume_lazy_town_short_ITEM)

    if upgradable_clothing != []:
        $ clothing_unlock = upgradable_clothing[ renpy.random.randint(0,len(upgradable_clothing)-1)]

    return


label set_ton_astoria_name:
    if one_of_five == 1:
        $ ton_astoria_name = "Cutie"
    if one_of_five == 2:
        $ ton_astoria_name = "Kitty"
    if one_of_five == 3:
        $ ton_astoria_name = "Princess"
    if one_of_five == 4:
        $ ton_astoria_name = "Little Girl"
    if one_of_five == 5:
        $ ton_astoria_name = "Honey"

    return



init python:
    def changeTonks(    mouth=None,
                        eye=None,
                        brows=None,
                        pupils=None,
                        cheeks=None,
                        tears=None,
                        extra=None,
                        emote=None):

        ### GLOBAL VARIABLES ###
        global tonks_mouth
        global tonks_eye
        global tonks_eyebrow
        global tonks_pupil
        global tonks_cheeks
        global tonks_tears
        global tonks_extra
        global tonks_emote

        ### FACE CONTROL
        if mouth is not None:
            tonks_mouth       = "characters/tonks/face/mouth/"+mouth+".png"
        if eye is not None:
            tonks_eye         = "characters/tonks/face/eyes/"+eye+".png"
            tonks_eye_bg      = "characters/tonks/face/eyes/_white_.png"
        if brows is not None:
            tonks_eyebrow     = "characters/tonks/face/brow/"+brows+".png"
        if pupils is not None:
            tonks_pupil       = "characters/tonks/face/pupil/"+pupils+".png"
        if cheeks is not None:
            tonks_cheeks      = "characters/tonks/face/extras/"+cheeks+".png"
        if tears is not None:
            tonks_tears       = "characters/tonks/face/extras/"+tears+".png"
        if extra is not None:
            tonks_extra       = "characters/tonks/face/extras/"+extra+".png"
        if emote is not None:
            tonks_emote       = "characters/emotes/"+str(emote)+".png"
