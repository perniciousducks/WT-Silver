default room_menu_active = False

# Main room menu screen (used to capture user interaction)
screen main_room_menu():
    tag room_menu
    on "show" action SetVariable("room_menu_active", True)
    on "hide" action SetVariable("room_menu_active", False)

# Main room screen
screen main_room(interact=True):
    tag room
    zorder 0

    # Hotkeys
    if room_menu_active and day > 1 and not renpy.variant('android'):
        use hotkeys_main
    
    use weather
    
    # Walls
    if daytime:
        add "images/rooms/_bg_/main_room_day.png" zoom 0.5
    else:
        add "images/rooms/_bg_/main_room_night.png" zoom 0.5

    # Poster
    if poster_OBJ.room_image:
        add poster_OBJ.get_room_image() xpos poster_OBJ.xpos ypos poster_OBJ.ypos xanchor 0.5 yanchor 0.5

    # Trophy
    if trophy_OBJ.room_image:
        add trophy_OBJ.get_room_image() xpos trophy_OBJ.xpos ypos trophy_OBJ.ypos xanchor 0.5 yanchor 0.5

    # Candles
    add candle_left_OBJ.get_room_image() xpos candle_left_OBJ.xpos ypos candle_left_OBJ.ypos xanchor 0.5 yanchor 0.5 zoom 0.5
    add candle_right_OBJ.get_room_image() xpos candle_right_OBJ.xpos ypos candle_right_OBJ.ypos xanchor 0.5 yanchor 0.5 zoom 0.5
    if not daytime:
        add "candle_fire_01" xpos candle_left_OBJ.xpos-110 ypos candle_left_OBJ.ypos-117
        add "candle_fire_02" xpos candle_right_OBJ.xpos-110 ypos candle_right_OBJ.ypos-117

    # Door
    imagebutton:
        focus_mask True
        xanchor "center"
        yanchor "center"
        if daytime:
            xpos door_OBJ.xpos
            ypos door_OBJ.ypos
            idle door_OBJ.get_idle_image()
            hover door_OBJ.get_hover_image()
        else:
            xpos door_night_OBJ.xpos
            ypos door_night_OBJ.ypos
            idle door_night_OBJ.get_idle_image()
            hover door_night_OBJ.get_hover_image()
        if door_examined:
            tooltip "Summon"
        else:
            tooltip "Examine Door"
        action Jump("door")
        sensitive room_menu_active

    # Cupboard
    add cupboard_OBJ.get_room_image() xpos cupboard_OBJ.xpos ypos cupboard_OBJ.ypos xanchor 0.5 yanchor 0.5 zoom 0.5

    # Scrolls (interactive overlay)
    if renpy.variant('android'):
        imagemap:
            xpos cupboard_top_OBJ.xpos
            ypos cupboard_top_OBJ.ypos
            xanchor "center"
            yanchor "center"
            ground cupboard_top_OBJ.get_idle_image()
            if store_intro_done:
                hover cupboard_top_OBJ.get_hover_image()
                hotspot (77, 81, 70, 76):
                    action Jump("read_scroll_menu")
                    sensitive room_menu_active
    else:
        imagebutton:
            xpos cupboard_top_OBJ.xpos
            ypos cupboard_top_OBJ.ypos
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle cupboard_top_OBJ.get_idle_image()
            if store_intro_done:
                hover cupboard_top_OBJ.get_hover_image()
                tooltip "Scrolls"
                action Jump("read_scroll_menu")
                sensitive room_menu_active

    # Cupboard (interactive overlay)
    if renpy.variant('android'):
        imagemap:
            xpos cupboard_OBJ.xpos
            ypos cupboard_OBJ.ypos
            xanchor "center"
            yanchor "center"
            ground cupboard_OBJ.get_idle_image()
            if not searched:
                hover cupboard_OBJ.get_hover_image()
                hotspot (73, 156, 72, 133):
                    action Jump("cupboard")
                    sensitive room_menu_active
    else:
        imagebutton:
            xpos cupboard_OBJ.xpos
            ypos cupboard_OBJ.ypos
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle cupboard_OBJ.get_idle_image()
            if not searched:
                hover cupboard_OBJ.get_hover_image()
                if cupboard_examined:
                    tooltip "Rummage"
                else:
                    tooltip "Examine Cupboard"
                action Jump("cupboard")
                sensitive room_menu_active

    #TODO Move phoenix to separate screen (check if usage needed in mirror stories)
    # Phoenix
    imagebutton:
        xpos phoenix_OBJ.xpos
        ypos phoenix_OBJ.ypos
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle phoenix_OBJ.get_idle_image()
        if not phoenix_is_petted:
            hover phoenix_OBJ.get_hover_image()
            if bird_examined:
                if not phoenix_is_fed:
                    tooltip "Feed"
                else:
                    tooltip "Pet"
            else:
                tooltip "Examine the bird"
            action Jump("phoenix")
            sensitive room_menu_active

    # Phoenix deco
    if phoenix_deco_OBJ.room_image:
        add phoenix_deco_OBJ.get_room_image() xpos phoenix_deco_OBJ.xpos ypos phoenix_deco_OBJ.ypos xanchor 0.5 yanchor 0.5 #xpos 410 ypos 75

    use phoenix_feather

    # Decorations
    # for i in deco_overlay_list:
    #    add deco_overlay_list[i].get_room_image() xpos i.xpos ypos i.ypos xanchor 0.5 yanchor 0.5


# Genie at desk
screen genie_desk(interact=True):
    tag genie_chibi # Uses same tag as chibi screens
    if renpy.variant('android'):
        add "newanimation" xpos 370 ypos 336 xanchor 0.5 yanchor 0.5
        imagemap:
            xpos 384
            ypos 370
            xanchor 0.5
            yanchor 0.5
            ground "images/rooms/main_room/desk_small_border.png"
            hover yellowTint("images/rooms/main_room/desk_small_border.png")
            hotspot (0, 10, 128, 160):
                action Jump("desk")
                sensitive room_menu_active
    else:
        imagebutton:
            xpos 370
            ypos 336
            focus_mask True
            xanchor 0.5
            yanchor 0.5
            idle "newanimation"
            hover "newanimation_hover"
            if desk_examined:
                tooltip "Open desk"
                hovered Show("gui_tooltip", img="exclaim_01", xx=195+140, yy=210)
            else:
                tooltip "Examine Desk"
                hovered Show("gui_tooltip", img="exclaim_01", xx=195+140, yy=210)
            unhovered Hide("gui_tooltip")
            action Jump("desk")
            sensitive room_menu_active

# Phoenix
screen phoenix_feather():
    tag feather
    add "feather" xpos phoenix_OBJ.xpos ypos phoenix_OBJ.ypos xanchor 0.5 yanchor 0.5
    zorder 2

screen phoenix_food():
    tag phoenix_food
    add "images/rooms/_objects_/phoenix/food.png" xpos phoenix_OBJ.xpos ypos phoenix_OBJ.ypos xanchor 0.5 yanchor 0.5
    zorder 2

# Fireplace
screen fireplace(interact=True):
    tag fireplace
    zorder 1
    if interact:
        imagebutton:
            xpos fireplace_OBJ.xpos
            ypos fireplace_OBJ.ypos
            focus_mask True
            xanchor 0.5
            yanchor 0.5
            idle fireplace_OBJ.get_idle_image()
            hover fireplace_OBJ.get_hover_image()
            if fireplace_examined:
                if day >= 25 and not daytime and (1 < weather_gen < 4) and (puzzle_box_ITEM.unlocked == False and unlocked_7th == False):
                    tooltip "What's that glimmer?"
                else:
                    if not fire_in_fireplace:
                        tooltip "Light fire"
                    else:
                        tooltip "Extinguish fire"
            else:
                tooltip "Examine fireplace"
            action Jump("fireplace")
            sensitive room_menu_active
    else:
        add fireplace_OBJ.get_room_image() xpos fireplace_OBJ.xpos ypos fireplace_OBJ.ypos xanchor 0.5 yanchor 0.5 zoom 0.5

    # Fireplace deco
    if fireplace_deco_OBJ.room_image:
        add fireplace_deco_OBJ.get_room_image() xpos fireplace_deco_OBJ.xpos ypos fireplace_deco_OBJ.ypos xanchor 0.5 yanchor 0.5

    # Puzzle box appears in fireplace
    if day >= 25 and not daytime and (1 < weather_gen < 4) and (puzzle_box_ITEM.unlocked == False and unlocked_7th == False):
        use fireplace_glow

screen fireplace_fire():
    tag fireplace_fire
    zorder 2
    add "fireplace_fire" xpos fireplace_OBJ.xpos ypos fireplace_OBJ.ypos+25 xanchor 0.5 yanchor 0.5

screen fireplace_glow():
    tag fireplace_glow
    zorder 3
    add "glow_effect" xpos 680 ypos 300 zoom 0.4 alpha 0.2

# Furniture
screen desk(xposistion=360): # Desk only
    tag desk
    zorder 2
    add "images/rooms/main_room/desk_with_shadow.png" xpos xposistion ypos 330 xanchor 0.5 yanchor 0.5 zoom 0.5

screen dumbledore(): # Dumbledore and desk
    tag dumbledore
    add "images/rooms/main_room/dum.png" xpos 370 ypos 336 xanchor 0.5 yanchor 0.5 zoom 0.5

screen chair_left():
    tag chair_left
    zorder 0 # Show main_room first for correct order
    add "images/rooms/main_room/chair_left_with_shadow.png" xpos 332 ypos 300 xanchor 0.5 yanchor 0.5 zoom 0.5

screen chair_right():
    tag chair_right
    zorder 0 # Show main_room first for correct order
    add "images/rooms/main_room/chair_right.png" xpos 793 ypos 300 xanchor 0.5 yanchor 0.5 zoom 0.5

# Owl
screen owl(interact=True):
    tag owl
    imagebutton:
        xpos owl_OBJ.xpos
        ypos owl_OBJ.ypos
        xanchor 0.5
        yanchor 1.0
        idle owl_OBJ.get_idle_image()
        hover owl_OBJ.get_hover_image()
        tooltip "Check mail\n{size=-4}"+num_to_word(len(letter_queue_list))+" new message(s){/size}"
        action Jump("read_letter")
        sensitive room_menu_active
    # add owl_OBJ.get_room_image() xpos owl_OBJ.xpos ypos owl_OBJ.ypos xanchor 0.5 yanchor 1.0

    # Owl deco
    if owl_deco_OBJ.room_image and renpy.get_screen("owl"):
        add owl_deco_OBJ.get_room_image() xpos owl_deco_OBJ.xpos ypos owl_deco_OBJ.ypos xanchor 0.5 yanchor 1.0

# Package
screen package(interact=True):
    tag package
    imagebutton:
        xpos package_OBJ.xpos
        ypos package_OBJ.ypos
        xanchor 0.5
        yanchor 1.0
        idle package_OBJ.get_idle_image()
        hover package_OBJ.get_hover_image()
        tooltip "Open package"
        action Jump("get_package")
        sensitive room_menu_active
    # add package_OBJ.get_room_image() xpos package_OBJ.xpos ypos package_OBJ.ypos xanchor 0.5 yanchor 1.0
