

### Astoria Chibi ###

label ast_chibi(action = "", xpos=ast_chibi_xpos, ypos=ast_chibi_ypos, flip=False, animation=False):
    $ ast_chibi_status = ""
    $ update_chibi_image("astoria")

    if xpos != ast_chibi_xpos:
        if xpos == "mid":
            $ ast_chibi_xpos = 540 # 560
        elif xpos in ("wardrobe","center","base","default"): #Don't use these when there are other chibis around (like Hermione's). Use "mid" instead.
            $ ast_chibi_xpos = 530
        elif xpos == "desk":
            $ ast_chibi_xpos = 440
        elif xpos == "on_desk":
            $ ast_chibi_xpos = 350
        elif xpos == "door":
            $ ast_chibi_xpos = 750
        else:
            $ ast_chibi_xpos = int(xpos)

    if ypos != ast_chibi_ypos:
        if ypos in ("base","default"):
            $ ast_chibi_ypos = 250
        elif ypos == "on_desk":
            $ ast_chibi_ypos = 180
        else:
            $ ast_chibi_ypos = int(ypos)

    # Action command.
    if action == "hide":
        hide screen ast_stand
    elif action == "leave":
        call play_sound("door")
        hide screen ast_main
        hide screen bld1
        hide screen blktone
        hide screen ast_stand
        with d3
        pause .5
    else:
        if action == "reset":
            $ ast_chibi_animation = None
            $ update_chibi_image("astoria")

        if flip: #Same variable that the main sprite is using. #1 == Default
            $ ast_chibi_flip = -1
            show screen ast_stand
        else:
            $ ast_chibi_flip = 1
            show screen ast_stand

    if animation != False:
        $ ast_chibi_animation = animation

    return



### Astoria Chibi Walk ###

label ast_walk(xpos=walk_xpos, ypos=walk_ypos, speed=ast_speed, action="", loiter=True, redux_pause=0):
    call hide_characters
    call hide_chibi_effects
    hide screen bld1
    hide screen blktone
    with d3

    $ ast_chibi_status = "move"
    $ update_chibi_image("astoria")

    # Action command.
    if action == "enter":
        call play_sound("door")
        $ ast_chibi_xpos = 750
        $ ast_chibi_ypos = 250
        $ ast_chibi_flip = 1
    elif action == "leave":
        $ xpos = "door"
        $ ypos = "base"
        $ loiter = False

    # Start position.
    $ walk_xpos = ast_chibi_xpos
    $ walk_ypos = ast_chibi_ypos

    # Target location.
    if xpos == "mid":
        $ walk_xpos2 = 540 # 560
    elif xpos == "desk":
        $ walk_xpos2 = 440
    elif xpos == "door":
        $ walk_xpos2 = 750
    else:
        $ walk_xpos2 = int(xpos)

    if ypos in ("base","default"):
        $ walk_ypos2 = 250
    else:
        $ walk_ypos2 = int(ypos)

    $ ast_speed = speed #Speed of walking animation. (lower = faster)

    # Walk right to left
    if walk_xpos >= walk_xpos2:
        $ ast_chibi_flip = 1
        show screen ast_walk
        $ tmp = ast_speed - redux_pause
        $ renpy.pause(tmp)
        $ ast_chibi_xpos = walk_xpos2
        $ ast_chibi_ypos = walk_ypos2
        hide screen ast_walk
        if loiter:
            $ ast_chibi_status = ""
            $ update_chibi_image("astoria")
            show screen ast_stand

    # Walk left to right
    else:
        $ ast_chibi_flip = -1
        show screen ast_walk
        $ tmp = ast_speed - redux_pause
        $ renpy.pause(tmp)
        $ ast_chibi_xpos = walk_xpos2
        $ ast_chibi_ypos = walk_ypos2
        hide screen ast_walk
        if action == "leave":
            call play_sound("door")
            with d3
            pause.3
            $ ast_chibi_flip = 1
        else:
            if loiter:
                $ update_chibi_image("astoria")
                $ ast_chibi_status = ""
                show screen ast_stand

    return


label ast_walk_end_loiter(dissolveTime = 3):
    if dissolveTime > 0:
        hide screen ast_stand
        with Dissolve((dissolveTime/10))
    else:
        hide screen ast_stand
    return



### ASTORIA CHIBI SCREENS ###

screen ast_stand():
    tag ast_chibi
    zorder ast_chibi_zorder

    frame:
        style "empty"
        if ast_chibi_animation == "fly":
            at chibi_fly_idle
        add ast_chibi_fix      xpos ast_chibi_xpos ypos ast_chibi_ypos xzoom ast_chibi_flip zoom (1.0/scaleratio)
        add ast_chibi_stand    xpos ast_chibi_xpos ypos ast_chibi_ypos xzoom ast_chibi_flip zoom (1.0/scaleratio)
        add ast_chibi_bottom   xpos ast_chibi_xpos ypos ast_chibi_ypos xzoom ast_chibi_flip zoom (1.0/scaleratio)
        add ast_chibi_shoes    xpos ast_chibi_xpos ypos ast_chibi_ypos xzoom ast_chibi_flip zoom (1.0/scaleratio)
        add ast_chibi_top      xpos ast_chibi_xpos ypos ast_chibi_ypos xzoom ast_chibi_flip zoom (1.0/scaleratio)
        add ast_chibi_robe     xpos ast_chibi_xpos ypos ast_chibi_ypos xzoom ast_chibi_flip zoom (1.0/scaleratio)
        add ast_chibi_gloves     xpos ast_chibi_xpos ypos ast_chibi_ypos xzoom ast_chibi_flip zoom (1.0/scaleratio)
        if ast_cloth_pile:
            add "characters/chibis/cloth_pile_r.png" xpos ast_pile_xpos ypos ast_pile_ypos


screen ast_walk():
    tag ast_chibi
    zorder ast_chibi_zorder

    frame:
        style "empty"
        if ast_chibi_animation == "fly":
            at chibi_fly(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2, speed=ast_speed)
        else:
            at ast_walk_trans(walk_xpos, walk_xpos2, walk_ypos, walk_ypos2)
        add ast_chibi_fix          xzoom ast_chibi_flip zoom (1.0/scaleratio)
        add ast_chibi_walk         xzoom ast_chibi_flip zoom (1.0/scaleratio)
        add ast_chibi_bottom       xzoom ast_chibi_flip zoom (1.0/scaleratio)
        add ast_chibi_shoes        xzoom ast_chibi_flip zoom (1.0/scaleratio)
        add ast_chibi_top          xzoom ast_chibi_flip zoom (1.0/scaleratio)
        if "quid" in ast_chibi_shoes:
            add ast_chibi_shoes        xzoom ast_chibi_flip zoom (1.0/scaleratio)
        add ast_chibi_robe         xzoom ast_chibi_flip zoom (1.0/scaleratio)
        add ast_chibi_gloves       xzoom ast_chibi_flip zoom (1.0/scaleratio)
    if ast_cloth_pile:
        add "characters/chibis/cloth_pile_r.png" xpos ast_pile_xpos ypos ast_pile_ypos