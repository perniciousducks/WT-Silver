### Main Room Menu Screen ###
screen main_room_menu:
    tag room_screen
    imagebutton: # DOOR
        xpos 758+140
        ypos 315
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/main_room/01_door.png"
        hover "images/main_room/01_door_02.png"
        action [Hide("main_room_menu"), Hide("animation_feather"), Jump("door")]
        
    
#    imagebutton: # CUPBOARD HAT
#        xpos 120+140
#        ypos 280
#        focus_mask True
#        xanchor "center"
#        yanchor "center"
#        idle "images/main_room/cupboard/idle_hat.png"
#        hover "images/main_room/cupboard/hover_hat.png"
#        action [Hide("main_room_menu"), Hide("animation_feather"), Jump("cupboard")]
    
    imagebutton: # CUPBOARD SCROLL
        xpos 120+140
        ypos 280
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/main_room/cupboard/idle_scroll.png"
        hover "images/main_room/cupboard/hover_scroll.png"
        action [Hide("main_room_menu"), Hide("animation_feather"), Jump("scrolls_menu")]
    
    imagebutton: # CUPBOARD CABINET
        xpos 120+140
        ypos 280
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/main_room/cupboard/idle_cabinet.png"
        hover "images/main_room/cupboard/hover_cabinet.png"
        action [Hide("main_room_menu"), Hide("animation_feather"), Jump("cupboard")]
    
#    imagebutton: # CUPBOARD LEFT
#        xpos 120+140
#        ypos 280
#        focus_mask True
#        xanchor "center"
#        yanchor "center"
#        idle "images/main_room/cupboard/idle_lower_left.png"
#        hover "images/main_room/cupboard/hover_lower_left.png"
#        action [Hide("main_room_menu"), Hide("animation_feather"), Jump("cupboard")]
    
#    imagebutton: # CUPBOARD RIGHT
#        xpos 120+140
#        ypos 280
#        focus_mask True
#        xanchor "center"
#        yanchor "center"
#        idle "images/main_room/cupboard/idle_lower_right.png"
#        hover "images/main_room/cupboard/hover_lower_right.png"
#        action [Hide("main_room_menu"), Hide("animation_feather"), Jump("cupboard")]
        
    # imagebutton: # OLD CUPBOARD
        # xpos 120+140
        # ypos 280
        # focus_mask True
        # xanchor "center"
        # yanchor "center"
        # idle "images/main_room/02_cupboard.png"
        # hover "images/main_room/02_cupboard_02.png"
        # action [Hide("main_room_menu"), Hide("animation_feather"), Jump("cupboard")]
        
    if package_is_here:
        imagebutton: # THE PACKAGE
                xpos 260+140
                ypos 235
                xanchor "center"
                yanchor "center"
                idle "images/main_room/owl_06.png" 
                hover "images/main_room/owl_06_2.png"
                #hovered [Show("gui_tooltip", my_picture="hoot", my_tt_xpos=250, my_tt_ypos=180) ] 
                #unhovered [Hide("gui_tooltip")]
                action [Hide("main_room_menu"), Hide("package"), Jump("get_package")]


    imagebutton: # GENIE
        xpos 230+140
        ypos 336
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "newanimation"
        hover "images/main_room/11_genie_02.png"
        hovered [Show("gui_tooltip", my_picture="exclaim_01", my_tt_xpos=195+140, my_tt_ypos=210) ] 
        #hovered [Show("config_afterchoices_skip_idle.png", xpos=46, ypos=518) ]
        unhovered [Hide("gui_tooltip")]
        action [Hide("main_room_menu"), Hide("animation_feather"), Jump("desk")]
    
    imagebutton: # PHOENIX
        xpos 400+140
        ypos 225
        #focus_mask True
        xanchor "center"
        yanchor "center"
        idle "pho_01" 
        hover "images/main_room/06_phoenix_02.png"
        #hovered [Show("gui_tooltip", my_picture="exclaim_01", my_tt_xpos=195, my_tt_ypos=210) ] 
        #hovered [Show("config_afterchoices_skip_idle.png", xpos=46, ypos=518) ]
        #unhovered [Show("gui_tooltip", my_picture="feather", my_tt_xpos=360, my_tt_ypos=140, xanchor="center", yanchor="center") ]
        action [Hide("main_room_menu"), Hide("animation_feather"), Jump("phoenix")]
        
    imagebutton: # FIREPLACE
        xpos 553+140
        ypos 277
        #focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/main_room/03_fireplace_02.png" 
        hover "images/main_room/03_fireplace_03.png"
        action [Hide("main_room_menu"), Jump("fireplace")]

    imagebutton: # STAT MENU
        xpos 830
        ypos 16
        xanchor "center"
        yanchor "center"
        idle "interface/points/Stats_Button.png"
        hover "interface/points/Stats_Button_Hover.png"
        action [Hide("main_room_menu"), Show("hermione_main"), Jump("open_stat_menu")]
     
    if letters >= 1: #Adds one letter in waiting list to be read. Displays owl with envelope.:
        imagebutton: # OWL
            xpos 315+140
            ypos 270
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle "owl_01" 
            hover "images/main_room/owl_04.png"
            #hovered [Show("gui_tooltip", my_picture="hoot", my_tt_xpos=250, my_tt_ypos=180) ] 
            #unhovered [Hide("gui_tooltip")]
            action [Hide("main_room_menu"), Jump("mail")]
    
    imagebutton: #Quest Guide
        xpos 128
        ypos 15
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "interface/check_07.png"
        hover "interface/check_08.png"
        action [Hide("main_room_menu"), Hide("animation_feather"), Jump("open_guide")]
