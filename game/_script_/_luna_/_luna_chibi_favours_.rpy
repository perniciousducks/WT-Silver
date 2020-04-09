
# Sets up a chibi scene with Luna and Genie in it
label lun_chibi_scene(action="reset", xpos="mid", ypos="base"):
    hide screen bld1
    hide screen blkfade

    call lun_chibi("hide")
    call gen_chibi("hide")

    if action == "reset":
        $ menu_y = 0.5
        call lun_chibi("stand", xpos, ypos)
        call gen_chibi("sit_behind_desk")

    elif action in ("sit_on_lap", "sit_on_lap_grope"):
        show screen luna_chibi_sit_on_lap("ch_lun_scene " + action)

    return

screen luna_chibi_sit_on_lap(img):
    tag luna_chibi_scene
    zorder desk_zorder

    add img pos (218, 205) # Same position as genie_behind_desk
