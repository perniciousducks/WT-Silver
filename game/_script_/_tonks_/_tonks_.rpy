define ton_face = {
    "mouth":
        {
        "neutral":      ["base"],
        "happy":        ["base", "smile"],
        "naughty":      ["horny","base"],
        "horny":        ["horny","base"],
        "annoyed":      ["upset"],
        "disgusted":    ["angry","upset"],
        "angry":        ["angry"]
        },

    "eyes":
        {
        "neutral":      ["base"],
        "happy":        ["base"],
        "naughty":      ["base"],
        "horny":        ["base"],
        "annoyed":      ["base"],
        "disgusted":    ["base"],
        "angry":        ["base"]
        },

    "eyebrows":
        {
        "neutral":      ["base"],
        "happy":        ["base","raised"],
        "naughty":      ["base","raised","angry"],
        "horny":        ["base","raised","angry"],
        "annoyed":      ["base","angry"],
        "disgusted":    ["raised","worried"],
        "angry":        ["angry"]
        },

    "pupils":
        {
        "neutral":      ["mid"],
        "happy":        ["mid","L","R"],
        "naughty":      ["mid","up","ahegao"],
        "horny":        ["mid","up","ahegao"],
        "annoyed":      ["mid","L","R"],
        "disgusted":    ["mid","down"],
        "angry":        ["mid"]
        }
    }

label ton_main(text="", mouth=False, eyes=False, eyebrows=False, pupils=False, hair=None, cheeks=None, tears=None, extra=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):
    if renpy.predicting():
        ton "predict"

    python:

        if flip != None:
            tonks_flip = -1 if flip else 1

        if animation != False:
            tonks_animation = animation

        if xpos:
            tonks_xpos = int(sprite_pos["x"].get(xpos, xpos))

        if ypos:
            if ypos == "head":
                use_tonks_head = True
            elif ypos in ("base", "default"):
                use_tonks_head = False

            tonks_ypos = int(sprite_pos["y"].get(ypos, ypos))

        target_color = None
        if hair:
            if hair in ("neutral", "basic", "reset"):
                target_color = tonks_haircolor
            elif hair in ("red", "angry", "furious"):
                target_color = [[164, 34, 34, 255]]
            elif hair in ("orange", "upset", "annoyed"):
                target_color = [[228, 93, 34, 255]]
            elif hair in ("yellow", "happy", "cheerful"):
                target_color = [[255, 213, 23, 255]]
            elif hair in ("green", "disgusted"):
                target_color = [[111, 205, 75, 255]]
            elif hair in ("blue", "sad"):
                target_color = [[64, 75, 205, 255]]
            elif hair in ("purple"):
                target_color = [[205, 75, 205, 255]]
            elif hair in ("white", "scared"):
                target_color = [[238, 238, 241, 255]]
            elif hair in ("pink", "horny"):
                target_color = [[242, 126, 168, 255]]
            else: # RANDOM limited from 50 to 235 for better outcome
                target_color = [[random.randint(50, 235), random.randint(50, 235), random.randint(50, 235), 255]]

        tonks.set_face(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)

        if face:
            if not mouth:
                tonks.set_face(mouth=renpy.random.choice(ton_face["mouth"].get(face, None)))
            if not eyes:
                tonks.set_face(eyes=renpy.random.choice(ton_face["eyes"].get(face, None)))
            if not eyebrows:
                tonks.set_face(eyebrows=renpy.random.choice(ton_face["eyebrows"].get(face, None)))
            if not pupils:
                tonks.set_face(pupils=renpy.random.choice(ton_face["pupils"].get(face, None)))

        if target_color and target_color != tonks.get_equipped("hair").color:
            tonks.get_equipped("hair").set_color(target_color)

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

    $ tonks.get_equipped("hair").set_color(tonks_haircolor)
    return

label check_tonks_clothing_upgrades:

    $ upgradable_clothing = []
    # Hermione
    # if hg_cheer_g_ITEM.unlocked and not hg_cheer_g_sexy_ITEM.unlocked:
        # $ upgradable_clothing.append(hg_cheer_g_sexy_ITEM)
    # if hg_cheer_s_ITEM.unlocked and not hg_cheer_s_sexy_ITEM.unlocked:
        # $ upgradable_clothing.append(hg_cheer_s_sexy_ITEM)
    # if hg_cheer_r_ITEM.unlocked and not hg_cheer_r_sexy_ITEM.unlocked:
        # $ upgradable_clothing.append(hg_cheer_r_sexy_ITEM)
    # if hg_cheer_h_ITEM.unlocked and not hg_cheer_h_sexy_ITEM.unlocked:
        # $ upgradable_clothing.append(hg_cheer_h_sexy_ITEM)
    # if hg_witch_ITEM.unlocked and not hg_witch_skimpy_ITEM.unlocked:
        # $ upgradable_clothing.append(hg_witch_skimpy_ITEM)

    # Luna
    if ll_stewardess_ITEM.unlocked and not ll_stewardess_short_ITEM.unlocked:
        $ upgradable_clothing.append(ll_stewardess_short_ITEM)

    # tonks
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
    $ tonks.wear("all")

    $ renpy.stop_predict(tonks.get_image())
    $ renpy.stop_predict("characters/tonks/face/*.png")

    call music_block
    jump main_room


screen tonks_main():
    tag tonks_main
    zorder tonks_zorder
    sensitive False

    default tonks_img = tonks.get_image()
    if tonks_animation != None:
        add tonks_img xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio) at tonks_animation
    else:
        add tonks_img xpos tonks_xpos ypos tonks_ypos xzoom tonks_flip zoom (1.0/tonks_scaleratio)

    on ("show", "replace") action Function(apply_doll_transition, tonks, "tonks_main", "tonks_img", use_tonks_head)
