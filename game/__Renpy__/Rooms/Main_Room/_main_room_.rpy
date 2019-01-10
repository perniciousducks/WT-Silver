

#Main Room Screen
screen main_room:
    if daytime:
        add "images/rooms/_bg_/main_room_day.png"
    else:
        add "images/rooms/_bg_/main_room_night.png"

    #Door
    add door_OBJ.get_room_image() xpos door_OBJ.xpos ypos door_OBJ.ypos xanchor 0.5 yanchor 0.5

    #Cupboard
    add cupboard_OBJ.get_room_image() xpos cupboard_OBJ.xpos ypos cupboard_OBJ.ypos xanchor 0.5 yanchor 0.5

    #Fireplace #Fire gets added separately
    add fireplace_OBJ.get_room_image() xpos fireplace_OBJ.xpos ypos fireplace_OBJ.ypos xanchor 0.5 yanchor 0.5

    #Candles
    add candle_left_OBJ.get_room_image() xpos candle_left_OBJ.xpos ypos candle_left_OBJ.ypos xanchor 0.5 yanchor 0.5
    add candle_right_OBJ.get_room_image() xpos candle_right_OBJ.xpos ypos candle_right_OBJ.ypos xanchor 0.5 yanchor 0.5
    if not daytime:
        add "candle_fire_01" xpos candle_left_OBJ.xpos-110 ypos candle_left_OBJ.ypos-117
        add "candle_fire_02" xpos candle_right_OBJ.xpos-110 ypos candle_right_OBJ.ypos-117

    #Phoenix Food & Feather gets added separately.
    add phoenix_OBJ.get_room_image() xpos phoenix_OBJ.xpos ypos phoenix_OBJ.ypos xanchor 0.5 yanchor 0.5

    zorder 0


#Main Room Overlay - (layer is on top of main_room_menu screen)
screen main_room_overlay:
    tag room_overlay_screen

    #Decorations
    for i in deco_overlay_list:
        add i.get_room_image() xpos i.xpos ypos i.ypos xanchor 0.5 yanchor 0.5

    #Fireplace
    if day >= 25 and not daytime and (1 < weather_gen < 4) and (puzzle_box_ITEM.unlocked == False and unlocked_7th == False):
        use fireplace_glow

    zorder 3#2

### Main Room Menu Screen ###
screen main_room_menu:
    tag room_screen
    imagebutton: # DOOR
        xpos door_OBJ.xpos
        ypos door_OBJ.ypos
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle door_OBJ.get_idle_image()
        hover door_OBJ.get_hover_image()
        action [Hide("main_room_menu"), Jump("door")]

    #Scrolls
    if renpy.variant('android'):
        imagemap:
            xpos cupboard_top_OBJ.xpos
            ypos cupboard_top_OBJ.ypos
            xanchor "center"
            yanchor "center"
            ground cupboard_top_OBJ.get_idle_image()
            hover cupboard_top_OBJ.get_hover_image()
            hotspot(77, 81, 70, 76) action [Hide("main_room_menu"), Jump("read_scroll_menu")]
    else:
        imagebutton: # CUPBOARD SCROLL
            xpos cupboard_top_OBJ.xpos
            ypos cupboard_top_OBJ.ypos
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle cupboard_top_OBJ.get_idle_image()
            hover cupboard_top_OBJ.get_hover_image()
            action [Hide("main_room_menu"), Jump("read_scroll_menu")]

    #Cupboard
    if renpy.variant('android'):
        imagemap:
           xpos cupboard_OBJ.xpos
           ypos cupboard_OBJ.ypos
           xanchor "center"
           yanchor "center"
           ground cupboard_OBJ.get_idle_image()
           hover cupboard_OBJ.get_hover_image()
           hotspot(73, 156, 72, 133) action [Hide("main_room_menu"), Jump("cupboard")]
    else:
        imagebutton:
            xpos cupboard_OBJ.xpos
            ypos cupboard_OBJ.ypos
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle cupboard_OBJ.get_idle_image()
            hover cupboard_OBJ.get_hover_image()
            action [Hide("main_room_menu"), Jump("cupboard")]

    #Hat
    if renpy.variant('android'):
        imagemap:
            xpos hat_OBJ.xpos
            ypos hat_OBJ.ypos
            xanchor "center"
            yanchor "center"
            ground hat_OBJ.get_idle_image()
            hover hat_OBJ.get_hover_image()
            hotspot(77, 50, 70, 76) action [Hide("main_room_menu"), Jump("options_menu")]
    else:
        imagebutton:
            xpos hat_OBJ.xpos
            ypos hat_OBJ.ypos
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle hat_OBJ.get_idle_image()
            hover hat_OBJ.get_hover_image()
            action [Hide("main_room_menu"), Jump("options_menu")]

#    imagebutton: # CUPBOARD LEFT
#        xpos 120+140
#        ypos 280
#        focus_mask True
#        xanchor "center"
#        yanchor "center"
#        idle "images/rooms/main_room/cupboard/idle_lower_left.png"
#        hover "images/rooms/main_room/cupboard/hover_lower_left.png"
#        action [Hide("main_room_menu"), Hide("animation_feather"), Jump("cupboard")]

#    imagebutton: # CUPBOARD RIGHT
#        xpos 120+140
#        ypos 280
#        focus_mask True
#        xanchor "center"
#        yanchor "center"
#        idle "images/rooms/main_room/cupboard/idle_lower_right.png"
#        hover "images/rooms/main_room/cupboard/hover_lower_right.png"
#        action [Hide("main_room_menu"), Hide("animation_feather"), Jump("cupboard")]

    # imagebutton: # OLD CUPBOARD
        # xpos 120+140
        # ypos 280
        # focus_mask True
        # xanchor "center"
        # yanchor "center"
        # idle "images/rooms/main_room/02_cupboard.png"
        # hover "images/rooms/main_room/02_cupboard_02.png"
        # action [Hide("main_room_menu"), Hide("animation_feather"), Jump("cupboard")]

    #Mail
    if package_is_here:
        imagebutton: # THE PACKAGE
            xpos package_OBJ.xpos
            ypos package_OBJ.ypos
            xanchor "center"
            yanchor "center"
            idle package_OBJ.get_idle_image()
            hover package_OBJ.get_hover_image()
            action [Hide("main_room_menu"), Hide("package"), Jump("get_package")]

    if letter_queue_list != []:
        imagebutton:
            xpos owl_OBJ.xpos
            ypos owl_OBJ.ypos
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle owl_OBJ.get_idle_image()
            hover owl_OBJ.get_hover_image()
            action [Hide("main_room_menu"), Jump("read_letter")]

    #Genie
    if renpy.variant('android'):
        imagemap:
            xpos 370
            ypos 336
            xanchor "center"
            yanchor "center"
            ground "newanimation"
            hover "images/rooms/main_room/11_genie_02.png"
            hotspot(49, 28, 188, 219) hovered [Show("gui_tooltip", my_picture="exclaim_01", my_tt_xpos=195+140, my_tt_ypos=210) ]
            hotspot(49, 28, 188, 219) unhovered [Hide("gui_tooltip")]
            hotspot(49, 28, 188, 219) action [Hide("main_room_menu"), Jump("desk")]
    else:
        imagebutton:
            xpos 370
            ypos 336
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle "newanimation"
            hover "images/rooms/main_room/11_genie_02.png"
            hovered [Show("gui_tooltip", my_picture="exclaim_01", my_tt_xpos=195+140, my_tt_ypos=210) ]
            unhovered [Hide("gui_tooltip")]
            action [Hide("main_room_menu"), Jump("desk")]

    #Phoenix
    imagebutton:
        xpos phoenix_OBJ.xpos
        ypos phoenix_OBJ.ypos
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle phoenix_OBJ.get_idle_image()
        if not phoenix_is_petted:
            hover phoenix_OBJ.get_hover_image()
            action [Hide("main_room_menu"), Jump("phoenix")]

    #Fireplace
    imagebutton:
        xpos fireplace_OBJ.xpos
        ypos fireplace_OBJ.ypos
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle fireplace_OBJ.get_idle_image()
        hover fireplace_OBJ.get_hover_image()
        action [Hide("main_room_menu"), Jump("fireplace")]

    #Stats
    imagebutton:
        xpos 830
        ypos 16
        xanchor "center"
        yanchor "center"
        idle "interface/points/Stats_Button.png"
        hover "interface/points/Stats_Button_Hover.png"
        action [Hide("main_room_menu"), Jump("open_stat_menu")]


    #Inventory
    imagebutton:
        xpos 830+77
        ypos 16
        xanchor "center"
        yanchor "center"
        idle "interface/points/Inventory_Button.png"
        hover "interface/points/Inventory_Button_Hover.png"
        action [Hide("main_room_menu"), Jump("open_inventory_menu")]

    zorder 1
