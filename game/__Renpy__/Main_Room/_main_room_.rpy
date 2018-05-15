




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
        action [Hide("main_room_menu"), Show("hermione_main"), Jump("stat_hermione")]
     
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

### Stat Screens ###


###MO SCREENS
label stat_hermione:
    $ hermione_xpos=400
    hide screen luna
    call updateHermioneWords
    call update_her_uniform
    call screen select_stat_character("HERMIONE")
    jump day_main_menu

label stat_luna:
    $ luna_xpos=540
    hide screen hermione_main
    call screen select_stat_character("LUNA")
    jump day_main_menu
    
screen select_stat_character(charName):
    $ indexSize = 0 # just update this after each button and copy the code bellow and the button will automaticlig find the correct position in the index. The icon image need to be 200*210 pixel
    add "interface/stat_select/CharacterStats.png" xpos 0 ypos 0
    text "-Character Select-" xpos 40 ypos 115 size 14 
    
    imagebutton:
        xpos 40 + ( 85 * (indexSize%2))
        ypos 140 + ( 90 * ((indexSize/2) - ((indexSize / 2)% 1)))
        idle Transform("interface/stat_select/CharacterIcon/HermioneIcon.png", zoom=.40) 
        hover Transform("interface/stat_select/CharacterIcon/HermioneIcon_Hover.png", zoom=.40) 
        action [Hide("select_stat_character"), Show("hermione_main"), Jump("stat_hermione")]
    $ indexSize += 1 
    
    if luna_unlocked == True:
        imagebutton:
            xpos 40 + ( 85 * (indexSize%2))
            ypos 140 + ( 90 * ((indexSize/2) - ((indexSize / 2)% 1)))
            idle Transform("interface/stat_select/CharacterIcon/LunaIcon.png", zoom=.40) 
            hover Transform("interface/stat_select/CharacterIcon/LunaIcon_Hover.png", zoom=.40) 
            action [Hide("select_stat_character"), Show("luna"), Jump("stat_luna")]
        $ indexSize += 1 

    
    if charName == "HERMIONE":
        text charName xalign 0.8 ypos 75 size 24
        
        text "-Whoring-" xalign 0.375 ypos 50+68 size 30 bold 0.2
        text "-Mood-" xalign 0.39 ypos 225+68 size 30 bold 0.2
        text "-Reputation-" xalign 0.375 ypos 400+68 size 30 bold 0.2
        
        text "-"+whoringWord+"-" xalign 0.375 ypos 50+130 size 20 
        text "-"+moodWord+"-" xalign 0.39 ypos 225+130 size 20
        text "-"+reputationWord+"-" xalign 0.375 ypos 400+130 size 20 
        
        add "interface/stat_select/StatBar_Empty.png" xpos 250 ypos 150
        add "interface/stat_select/StatBar_Empty.png" xpos 250 ypos 325
        add "interface/stat_select/StatBar_Empty.png" xpos 250 ypos 500
        
        add LiveCrop((0, 0, (int(whoring/2.4)*36), 600), "interface/stat_select/StatBar_Full.png") xpos 250 ypos 150
        add LiveCrop((0, 0, (madValue*36), 600), "interface/stat_select/StatBar_Full.png") xpos 250 ypos 325
        add LiveCrop((0, 0, (int(whoring/2.4)*36), 600), "interface/stat_select/StatBar_Full.png") xpos 250 ypos 500
        
        add "interface/stat_select/PageBreak.png" xpos 250 ypos 237
        add "interface/stat_select/PageBreak.png" xpos 250 ypos 412

        imagebutton: # X
            xpos 1013
            ypos 13
            idle "interface/map/close_ground.png"
            hover "interface/map/close_hover.png"
            action [Hide("select_stat_character"), Hide("hermione_main"), Jump("day_main_menu")]
    
    elif charName == "LUNA":
        text charName xalign 0.775 ypos 75 size 24
        
        text "-Corruption-" xalign 0.375 ypos 50+ 68 size 30 bold 0.2
        text "-Dom points-" xalign 0.375 ypos 225+ 68 size 30 bold 0.2
        text "-Sub points-" xalign 0.375 ypos 400+ 68 size 30 bold 0.2

        text "-"+str(luna_corruption)+"-" xalign 0.39 ypos 50+130 size 20 
        text "-"+str(luna_dom)+"-" xalign 0.39 ypos 225+130 size 20
        text "-"+str(luna_sub)+"-" xalign 0.39 ypos 400+130 size 20 
        
        #When the max amount of the diffrent stats add the full bare with crop
        add "interface/stat_select/StatBar_Empty.png" xpos 250 ypos 150
        add "interface/stat_select/StatBar_Empty.png" xpos 250 ypos 325
        add "interface/stat_select/StatBar_Empty.png" xpos 250 ypos 500
        
        add "interface/stat_select/PageBreak.png" xpos 250 ypos 237
        add "interface/stat_select/PageBreak.png" xpos 250 ypos 412
        
        imagebutton: # X
            xpos 1013
            ypos 13
            idle "interface/map/close_ground.png"
            hover "interface/map/close_hover.png"
            action [Hide("select_stat_character"), Hide("luna"), Jump("day_main_menu")]
        
screen stat_screen_hermione:
    zorder hermione_main_zorder-1

    #add "interface/map/stat_base.png" xpos 275

    add "interface/map/stat_empty.png" xpos -20 ypos -175+30
    add LiveCrop((0, 0, 350+(int(whoring/2.4)*40), 600), "interface/map/stat_full.png") xpos -20 ypos -175+30

    add "interface/map/stat_empty.png" xpos -20 ypos 0+30
    add LiveCrop((0, 0, 750-(madValue*40), 600), "interface/map/stat_full.png") xpos -20 ypos 0+30

    add "interface/map/stat_empty.png" xpos -20 ypos 175+30 
    add LiveCrop((0, 0, 350+(int(whoring/2.4)*40), 600), "interface/map/stat_full.png") xpos -20 ypos 175+30

    text "-Whoring-" xalign 0.485 ypos 50+38 size 30 bold 0.2
    text "-Mood-" xalign 0.485 ypos 225+38 size 30 bold 0.2
    text "-Reputation-" xalign 0.485 ypos 400+38 size 30 bold 0.2

    text "-"+whoringWord+"-" xalign 0.485 ypos 50+110 size 20 
    text "-"+moodWord+"-" xalign 0.485 ypos 225+110 size 20
    text "-"+reputationWord+"-" xalign 0.485 ypos 400+110 size 20 

    #text "[hermione_name]" xalign 0.9 ypos 80 size 20 

    imagebutton: # X
        xpos 1013
        ypos 13
        idle "interface/map/close_ground.png"
        hover "interface/map/close_hover.png"
        action [Hide("stat_screen_hermione"), Hide("hermione_main"), Jump("day_main_menu")]

    imagebutton: # STAT MENU SWAP
        xpos 894
        ypos 72
        xanchor "center"
        yanchor "center"
        idle "interface/points/points_03.png"
        hover "interface/points/points_04.png"
        action [Hide("main_room_menu"), Show("luna"), Jump("stat_luna")]

screen stat_screen_luna:
    zorder zorder_character-1

    #add "interface/map/stat_base.png" xpos 275

    add "interface/map/stat_empty.png" xpos -20 ypos -175+30

    add "interface/map/stat_empty.png" xpos -20 ypos 0+30

    add "interface/map/stat_empty.png" xpos -20 ypos 175+30 

    text "-Corruption-" xalign 0.485 ypos 50+38 size 30 bold 0.2
    text "-Dom points-" xalign 0.485 ypos 225+38 size 30 bold 0.2
    text "-Sub points-" xalign 0.485 ypos 400+38 size 30 bold 0.2

    text "-"+str(luna_corruption)+"-" xalign 0.485 ypos 50+110 size 20 
    text "-"+str(luna_dom)+"-" xalign 0.485 ypos 225+110 size 20
    text "-"+str(luna_sub)+"-" xalign 0.485 ypos 400+110 size 20 

    #text "[hermione_name]" xalign 0.9 ypos 80 size 20 

    imagebutton: # X
        xpos 1013
        ypos 13
        idle "interface/map/close_ground.png"
        hover "interface/map/close_hover.png"
        action [Hide("stat_screen_hermione"), Hide("luna"), Jump("day_main_menu")]

    imagebutton: # STAT MENU SWAP
        xpos 894
        ypos 72
        xanchor "center"
        yanchor "center"
        idle "interface/points/points_03.png"
        hover "interface/points/points_04.png"
        action [Hide("main_room_menu"), Show("hermione_main"), Jump("stat_hermione")]


label updateHermioneWords:
    $ whoringWords = ["Pure", "Naive", "Curious", "Naughty", "Perverse", "Immoral", "Slutty", "Shameless", "Cumslut", "Total Cumslut", "Shameless Cumslut"] 
    $ madWords = ["Happy", "Slightly upset", "annoyed", "upset", "very upset", "mad", "angry", "hateful", "despises you", "Furious", "Absolutely Furious"] 
    $ whoreWords = ["Teacher's pet", "School star", "good girl", "minx", "slutty schoolgirl", "easy lay", "whore", "slut for sex", "gryffindor whore", "school cumdump", "mudblood cumdump"] 
    $ slutWords = ["Teacher's pet", "School star", "good girl", "principal's pet", "slutty schoolgirl", "slut", "principal's slut", "daddy's girl", "gryffindor slut", "Dumbledore's whore", "Dumbledore's cumdump"]

    $ whoringWord = whoringWords[int(whoring/2.4)]

    if mad > 9:
        $ moodWord = "Blind rage"
        $ madValue = 10
    else:
        $ moodWord = madWords[mad]
        $ madValue = mad

    if lock_public_favors:
        $ reputationWord = slutWords[int(whoring/2.4)]
    else:
        $ reputationWord = whoreWords[int(whoring/2.4)]

    return


### Weather Screens ###


screen new_window: #WEATHER BG. CLEAR SKY. #тут тоже просто — делаем zorder -2, чтобы заглушка была ниже остальных скринов — ведь облако должно плыть между ней и комнатой 
    zorder -2
    add "images/main_room/weather/sunny.png"
    
screen cloud: # zorder -1, т.к. должно быть выше заглушки, но ниже комнаты
    zorder -1
    add "images/main_room/weather/cloud_small.png" at cloud_move # это значит, что изображение подчиняется методу движения cloud_move, который прописан дальше

screen cloud_night_01: 
    #zorder -1
    add "images/main_room/weather/night_cloud_02.png" at cloud_night_move_01
    
screen cloud_night_02: 
    #zorder -1
    add "images/main_room/weather/night_cloud_01.png" at cloud_night_move_02
    
screen cloud_night_03: 
    #zorder -1
    add "images/main_room/weather/night_cloud_03.png" at cloud_night_move_03



    