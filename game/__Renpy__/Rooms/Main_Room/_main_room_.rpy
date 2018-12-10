
screen main_room:
    if daytime:
        add "images/rooms/main_room/main_room_day.png"
    else:
        add "images/rooms/main_room/main_room_night.png"

    #Door
    add "images/rooms/main_room/door.png" at Position(xpos=898, ypos=315, xanchor="center", yanchor="center")

    #Cupboard
    add "images/rooms/main_room/cupboard_w_shadow.png" at Position(xpos=260, ypos=280, xanchor="center", yanchor="center")

    #Fireplace #Fire gets added separately
    add "images/rooms/main_room/fireplace_w_shadow.png" at Position(xpos=693, ypos=277, xanchor="center", yanchor="center")

    #Candles
    add "images/rooms/main_room/candle.png" at Position(xpos=350, ypos=160, xanchor="center", yanchor="center")
    add "images/rooms/main_room/candle.png" at Position(xpos=833, ypos=225, xanchor="center", yanchor="center")
    if not daytime:
        add "candle_fire_01" xpos 240 ypos 43
        add "candle_fire_02" xpos 723 ypos 108

    #Phoenix #Food & Feather gets added separately.
    add "images/rooms/main_room/phoenix.png" at Position(xpos=540, ypos=225, xanchor="center", yanchor="center")

    zorder 0


### Main Room Menu Screen ###
screen main_room_menu:
    tag room_screen
    imagebutton: # DOOR
        xpos 898
        ypos 315
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/rooms/main_room/door.png"
        hover "images/rooms/main_room/door_hover.png"
        action [Hide("main_room_menu"), Jump("door")]


    if renpy.variant('android'):
        imagemap:
            xpos 260
            ypos 280
            xanchor "center"
            yanchor "center"
            ground "images/rooms/main_room/cupboard/idle_hat.png"
            hover "images/rooms/main_room/cupboard/hover_hat.png"
            hotspot(77, 50, 70, 76) action [Hide("main_room_menu"), Jump("options_menu")]
    else:
        imagebutton: # CUPBOARD HAT
            xpos 260
            ypos 280
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle "images/rooms/main_room/cupboard/idle_hat.png"
            hover "images/rooms/main_room/cupboard/hover_hat.png"
            action [Hide("main_room_menu"), Jump("options_menu")]

    #Scrolls
    if renpy.variant('android'):
        imagemap:
            xpos 260
            ypos 280
            xanchor "center"
            yanchor "center"
            ground "images/rooms/main_room/cupboard/idle_scroll.png"
            hover "images/rooms/main_room/cupboard/hover_scroll.png"
            hotspot(77, 81, 70, 76) action [Hide("main_room_menu"), Jump("read_scroll_menu")]
    else:
        imagebutton: # CUPBOARD SCROLL
            xpos 260
            ypos 280
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle "images/rooms/main_room/cupboard/idle_scroll.png"
            hover "images/rooms/main_room/cupboard/hover_scroll.png"
            action [Hide("main_room_menu"), Jump("read_scroll_menu")]

    #Cupboard
    if renpy.variant('android'):
        imagemap:
           xpos 260
           ypos 280
           xanchor "center"
           yanchor "center"
           ground "images/rooms/main_room/cupboard/idle_cabinet.png"
           hover "images/rooms/main_room/cupboard/hover_cabinet.png"
           hotspot(73, 156, 72, 133) action [Hide("main_room_menu"), Jump("cupboard")]
    else:
        imagebutton:
            xpos 260
            ypos 280
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle "images/rooms/main_room/cupboard/idle_cabinet.png"
            hover "images/rooms/main_room/cupboard/hover_cabinet.png"
            action [Hide("main_room_menu"), Jump("cupboard")]


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
            xpos 400
            ypos 235
            xanchor "center"
            yanchor "center"
            idle "images/rooms/main_room/owl_06.png"
            hover "images/rooms/main_room/owl_06_2.png"
            #hovered [Show("gui_tooltip", my_picture="hoot", my_tt_xpos=250, my_tt_ypos=180) ]
            #unhovered [Hide("gui_tooltip")]
            action [Hide("main_room_menu"), Hide("package"), Jump("get_package")]

    if letter_queue_list != []:
        imagebutton:
            xpos 455
            ypos 270
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle "owl_with_letter_blink"
            hover "images/rooms/main_room/owl_04.png"
            action [Hide("main_room_menu"), Jump("read_letter")]

    #Genie
    if renpy.variant('android'):
        imagemap: # GENIE
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
        xpos 540
        ypos 225
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "pho_01"
        if not phoenix_is_petted:
            hover "images/rooms/main_room/phoenix_hover.png"
            action [Hide("main_room_menu"), Jump("phoenix")]

    #Fireplace
    imagebutton:
        xpos 693
        ypos 277
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/rooms/main_room/fireplace.png"
        hover "images/rooms/main_room/fireplace_hover.png"
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


    zorder 1
