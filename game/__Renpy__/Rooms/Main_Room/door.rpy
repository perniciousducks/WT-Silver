label door:
    hide screen main_room_menu

    if day == 1:
        if not door_examined:
            $ door_examined = True
            jump examine_door
        jump day_main_menu

    # #Updates
    # $ summon_list = []
    # $ summon_list.append(["hermione", 0 if hermione_busy else 1]) if hermione_unlocked else 0
    # $ summon_list.append(["luna", 0 if luna_busy else 1]) if luna_unlocked else 0
    # $ summon_list.append(["astoria", 0 if astoria_busy else 1]) if astoria_unlocked else 0
    # $ summon_list.append(["susan", 0 if susan_busy else 1]) if susan_unlocked else 0
    # $ summon_list.append(["cho", 0 if cho_busy else 1]) if cho_unlocked else 0
    # $ summon_list.append(["snape", 0 if snape_busy else 1]) if snape_unlocked else 0
    # $ summon_list.append(["tonks", 0 if tonks_busy else 1]) if tonks_unlocked else 0

    call update_character_map_locations

    #Screens
    call play_sound("scroll")
    jump door_menu
    #show screen door_menu
    #with d1

    $_return = ui.interact()

    hide screen door_menu
    #Do NOT add a transition here!


    #Hermione
    if _return == "hermione":
        if hermione_busy:
            if daytime:
                call nar(">Hermione is taking classes.")
                jump day_main_menu
            call nar(">Hermione is already asleep.")
            jump night_main_menu
                
        if her_map_location == "forest":
            jump hermione_map_BJ
        jump summon_hermione


    #Luna
    elif _return == "luna":
        if luna_busy:
            if daytime:
                call nar(">Luna is taking classes.")
                jump day_main_menu
            call nar(">Luna is already asleep.")
            jump night_main_menu
        if not luna_reverted:
            call play_music("dark_fog") # LUNA'S THEME (placeholder probably)
        else:
            call play_music("chipper_doodle") # LUNA'S THEME (placeholder probably)
        jump summon_luna


    #Astoria
    elif _return == "astoria":
        if astoria_busy:
            if daytime:
                call nar(">Astoria is taking classes.")
                jump day_main_menu
            call nar(">Astoria is already asleep.")
            jump night_main_menu
        call play_music("chipper_doodle")
        jump summon_astoria


    #Susan
    elif _return == "susan":
        if susan_busy:
            if daytime:
                call nar(">Susan is taking classes.")
                jump day_main_menu
            call nar(">Susan is already asleep.")
            jump night_main_menu
        jump summon_susan


    #Cho
    elif _return == "cho":
        if cho_busy:
            if daytime:
                call nar(">Cho is taking classes.")
                jump day_main_menu
            call nar(">Cho is already asleep.")
            jump night_main_menu
        call play_music("cho_theme")
        jump summon_cho


    #Snape
    elif _return == "snape":
        if snape_busy:
            call nar(">Professor Snape is unavailable.")
            if daytime:
                jump day_main_menu
            jump night_main_menu
        call play_music("dark_fog") # SNAPE'S THEME
        jump summon_snape


    #Tonks
    elif _return == "tonks":
        if tonks_busy:
            call nar(">Tonks is unavailable.")
            if daytime:
                jump day_main_menu
            jump night_main_menu
        jump summon_tonks

    #Close
    else:
        jump day_main_menu

    $ renpy.jump(_return)

screen door_menu_old():
    zorder 8
    button style "empty" action [Return("Close")]
    use top_bar_close_button
    use character_select_menu(summon_list, "-Summon-", 812, 40)

#Day 1 room interact quest.
label examine_door:
    $ door_examined = True
    show screen chair_left
    show screen chair_right
    show screen desk
    call gen_chibi("stand","door","base")
    with d5

    m "A sturdy looking door..."
    m "I wonder what's behind it."
    label examining_the_door:
    menu:
        "-Knock on the door-":
            show screen blktone8
            with d3
            call play_sound("knocking")
            "*Knock-knock-knock*"
            "..................."
            hide screen blktone8
            with d3
            m "No reply..."
            jump examining_the_door
        "-Put your ear on it-":
            show screen blktone8
            with d3
            ">You put your ear on the door and listen intently..."
            m "I don't hear anything."
            hide screen blktone8
            with d3
            jump examining_the_door
        "-Kick the door-":
            show screen blktone8
            with d3
            $ renpy.play('sounds/kick.ogg')
            pause.2
            with hpunch
            "*Thump!*"
            ".............................."
            hide screen blktone8
            with d3
            m "This door could take a thousand kicks like that and it still wouldn't break..."
            m "It doesn't look like it's locked though..."
            jump examining_the_door
        "-Leave it alone-":
            m "Who knows what kind of dangers could be lurking behind that door?"
            m "I think I'll let it be for now..."
            pass

    call gen_chibi("sit_behind_desk")
    with d3

    jump day_main_menu
