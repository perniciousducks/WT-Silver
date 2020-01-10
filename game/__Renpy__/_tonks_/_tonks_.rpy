### Tonks###

label ton_main(text="", mouth=False, eyes=False, eyebrows=False, pupils=False, hair=None, cheeks=False, tears=False, extra=False, emote=False, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):

    $ target_color = None

    #Flip
    if flip == False:
        $ tonks_flip = 1 #Default
    if flip == True:
        $ tonks_flip = -1

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
                $ tonks_xpos = -80
            else:
                $ tonks_xpos = 650
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
        $ target_color = None
        if hair in ("neutral", "basic", "reset"):
            $ target_color = tonks_haircolor # player
        elif hair in ("red", "angry", "furious"):
            $ target_color = [[164, 34, 34, 255]]
        elif hair in ("orange", "upset", "annoyed"):
            $ target_color = [[228, 93, 34, 255]]
        elif hair in ("yellow", "happy", "cheerful"):
            $ target_color = [[255, 213, 23, 255]]
        elif hair in ("green", "disgusted"):
            $ target_color = [[111, 205, 75, 255]]
        elif hair in ("blue", "sad"):
            $ target_color = [[64, 75, 205, 255]]
        elif hair in ("purple"):
            $ target_color = [[205, 75, 205, 255]]
        elif hair in ("white", "scared"):
            $ target_color = [[238, 238, 241, 255]]
        elif hair in ("pink", "horny"):
            $ target_color = [[242, 126, 168, 255]]
        else: # RANDOM limited from 50 to 235 for better outcome
            $ target_color = [[random.randint(50, 235), random.randint(50, 235), random.randint(50, 235), 255]]

    if animation != False:
        $ tonks_animation = animation

    python:
        tonks.set_face(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)
        #tonks_class.special(emote=emote)

    # Hair transition, performs only when applying new colour
    if target_color != None and target_color != tonks.get_equipped("hair").color:
        $ tonks.get_equipped("hair").color = target_color
        $ tonks.rebuild()

    if not renpy.get_screen("wardrobe_menu"):
        show screen tonks_main()
    show screen bld1

    if trans:
        with trans

    if text:
        $ renpy.say(ton, text)

    if use_tonks_head:
        hide screen tonks_main

    return



label update_tonks:

    # Chibi Update
    $ tonks_chibi.update()
    $ tonks_chibi.position(flip=False)
    $ tonks_flip = 1
    hide screen ton_cloth_pile

    # Reset temporal hair colour
    $ tonks.get_equipped("hair").color = tonks_haircolor
    $ tonks.get_equipped("hair").cached = False

    return
    
label check_tonks_clothing_upgrades:

    $ upgradable_clothing = []
    # Hermione
    if hg_cheer_g_ITEM.unlocked and not hg_cheer_g_sexy_ITEM.unlocked:
        $ upgradable_clothing.append(hg_cheer_g_sexy_ITEM)
    if hg_cheer_s_ITEM.unlocked and not hg_cheer_s_sexy_ITEM.unlocked:
        $ upgradable_clothing.append(hg_cheer_s_sexy_ITEM)
    if hg_cheer_r_ITEM.unlocked and not hg_cheer_r_sexy_ITEM.unlocked:
        $ upgradable_clothing.append(hg_cheer_r_sexy_ITEM)
    if hg_cheer_h_ITEM.unlocked and not hg_cheer_h_sexy_ITEM.unlocked:
        $ upgradable_clothing.append(hg_cheer_h_sexy_ITEM)
    if hg_witch_ITEM.unlocked and not hg_witch_skimpy_ITEM.unlocked:
        $ upgradable_clothing.append(hg_witch_skimpy_ITEM)

    # Luna
    if ll_stewardess_ITEM.unlocked and not ll_stewardess_short_ITEM.unlocked:
        $ upgradable_clothing.append(ll_stewardess_short_ITEM)

    # Astoria
    #if ag_costume_lazy_town_ITEM.unlocked and not ag_costume_lazy_town_short_ITEM.unlocked:
        #$ upgradable_clothing.append(ag_costume_lazy_town_short_ITEM)

    if upgradable_clothing != []:
        $ clothing_unlock = upgradable_clothing[ renpy.random.randint(0,len(upgradable_clothing)-1)]

    return

label end_tonks_event:
    call ton_chibi("hide")
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
    default tonks_img = tonks.get_image()
    if tonks_animation != None:
        add tonks_img xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) at tonks_animation
    else:
        add tonks_img xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)

    on ("show", "replace") action Function(apply_doll_transition, tonks, "tonks_main", "tonks_img", use_tonks_head)
