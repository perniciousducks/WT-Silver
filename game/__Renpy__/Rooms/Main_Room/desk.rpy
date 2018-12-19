label desk:
    hide screen main_room_menu

    if day == 1:
        if not desk_examined:
            menu:
                "-Examine the desk-":
                    $ desk_examined = True
                    m "A desk of some sort..."
        jump day_main_menu

    #Updates
    $ summon_list = []
    $ summon_list.append(["hermione", 0 if hermione_busy else 1]) if hermione_unlocked else 0
    $ summon_list.append(["luna", 0 if luna_busy else 1]) if luna_unlocked else 0
    $ summon_list.append(["astoria", 0 if astoria_busy else 1]) if astoria_unlocked else 0
    $ summon_list.append(["susan", 0 if susan_busy else 1]) if susan_unlocked else 0
    $ summon_list.append(["cho", 0 if cho_busy else 1]) if cho_unlocked else 0
    $ summon_list.append(["snape", 0 if snape_busy else 1]) if snape_unlocked else 0
    $ summon_list.append(["tonks", 0 if tonks_busy else 1]) if tonks_unlocked else 0

    call update_character_map_locations


    #Screens
    call play_sound("scroll")
    show screen desk_menu
    hide screen points
    with d1

    $_return = ui.interact()

    hide screen desk_menu
    show screen points
    #Do NOT add a transition here!


    #Hermione
    if _return == "hermione" and hermione_busy:
        if daytime:
            call nar(">Hermione is taking classes.")
            jump day_main_menu
        else:
            call nar(">Hermione is already asleep.")
            jump night_main_menu
    elif _return == "hermione" and not hermione_busy:
        if her_map_location == "forest":
            jump hermione_map_BJ

        jump summon_hermione


    #Luna
    elif luna_known and _return == "luna" and luna_busy:
        if daytime:
            call nar(">Luna is taking classes.")
            jump day_main_menu
        else:
            call nar(">Luna is already asleep.")
            jump night_main_menu
    elif luna_known and _return == "luna" and not luna_busy:
        if not luna_reverted:
            call play_music("dark_fog") # LUNA'S THEME (placeholder probably)
        else:
            call play_music("chipper_doodle") # LUNA'S THEME (placeholder probably)
        jump summon_luna


    #Astoria
    elif astoria_busy and _return == "astoria":
        if daytime:
            call nar(">Astoria is taking classes.")
            jump day_main_menu
        else:
            call nar(">Astoria is already asleep.")
            jump night_main_menu
    elif not astoria_busy and _return == "astoria": #Summoning after intro events done.
        call play_music("chipper_doodle")
        jump summon_astoria


    #Susan
    elif _return == "susan" and susan_busy:
        if daytime:
            call nar(">Susan is taking classes.")
            jump day_main_menu
        else:
            call nar(">Susan is already asleep.")
            jump night_main_menu
    elif _return == "susan" and not susan_busy:
        jump summon_susan


    #Cho
    elif _return == "cho" and cho_busy:
        if daytime:
            call nar(">Cho is taking classes.")
            jump day_main_menu
        else:
            call nar(">Cho is already asleep.")
            jump night_main_menu
    elif _return == "cho" and not cho_busy:
        call play_music("chipper_doodle") # CHO'S THEME (placeholder probably)
        jump summon_cho


    #Snape
    elif _return == "snape" and snape_busy:
        call nar(">Professor Snape is unavailable.")
        if daytime:
            jump day_main_menu
        else:
            jump night_main_menu
    elif _return == "snape" and not snape_busy:
        call play_music("dark_fog") # SNAPE'S THEME
        jump summon_snape


    #Tonks
    elif _return == "tonks" and tonks_busy:
        call nar(">Tonks is unavailable.")
        if daytime:
            jump day_main_menu
        else:
            jump night_main_menu
    elif _return == "tonks" and not tonks_busy:
        jump summon_tonks


    #Close
    elif _return == "Close":
        jump day_main_menu

    $ renpy.jump(_return)



screen desk_menu:
    zorder 8

    add "images/backgrounds/desk.png"
    use close_button

    if map_unlocked:
        use map_screen
        use map_screen_characters

    imagebutton:
        xpos -5
        ypos 100
        focus_mask True
        idle "interface/map/desk_book_idle.png"
        hover "interface/map/desk_book_hover.png"
        action Return("read_book_menu")

    imagebutton:
        xpos -40
        ypos 260
        focus_mask True
        idle "interface/map/desk_letters_idle.png"
        if letter_paperwork_unlock_OBJ.read: #Work unlocked
            hover "interface/map/desk_letters_hover.png"
            action Return("paperwork")




### PAPERWORK ###
label paperwork:
    if finished_report >= 6 and (letter_paperwork_report_OBJ not in letter_queue_list):
        m "I've completed six reports this week already."
        jump desk
    elif letter_paperwork_report_OBJ in letter_queue_list:
        m "I need to get paid first."
        jump desk
    else:
        pass

    stop music fadeout 1.0
    if daytime:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else:
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...

    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        stop bg_sounds


    hide screen genie
    show screen paperwork
    with Dissolve(0.3)
    ">You do some paperwork."

    call finished_working_chapter #Chapter finished. $ report_chapters += 1

    call report_chapters_check #Checks whether or not the completed chapter was the final one.

    if not daytime and (1 < weather_gen < 4): # FULL MOON
        call f_moon_bonus

    call report_chapters_check #Checks whether or not the completed chapter was the final one.

    ### SPEEDWRITING CHECK ###========================================================================
    if speed_writing == 1:
        $ speedwriting_check = renpy.random.randint(1, 3) #"\"Speedwriting for dummies.\"" # 1/10 chance
        if speedwriting_check == 1:
            call speedwriting_label
    if speed_writing == 2:
        $ speedwriting_check = renpy.random.randint(1, 3) #"\"Speedwriting for beginners.\"" # 1/8 chance of it to pop up.
        if speedwriting_check > 1:
            call speedwriting_label
    if speed_writing == 3:
            call speedwriting_label
    if speed_writing >= 4:
            call speedwriting_label
            call concentration_label
#    if speed_writing == 5:
#        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for experts.\"" # 1/2 chance of it to pop up.
#        if speedwriting_check == 1:
#            call speedwriting_label
#    if speed_writing == 6:
#        call speedwriting_label #""\"Speedwriting for maniacs.\"" # 1 (sure) chance of it to pop up.

    call report_chapters_check #Checks whether or not the completed chapter was the final one.


    show screen genie
    hide screen paperwork



    if daytime:
        jump night_start
    else:
        jump day_start

###
label report_chapters_check:
    if report_chapters >= 4:
        ">You've completed a report."
        $ report_chapters = 0
        $ finished_report += 1
    return
### FULL MOON BONUS ###
label f_moon_bonus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">The Full moon makes you feel more productive.\n>You finished [report_chapters] chapters so far."
    return
###
label finished_working_chapter:
    $ report_chapters += 1
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">You finished [report_chapters] chapters so far."
    return
### CONCENTRATION
label concentration_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">You maintain perfect concentration during your work.\n>And finish another chapter of the report.\n>You finished [report_chapters] chapters so far."
    return
### SPEEDWRITING
label speedwriting_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">You use your Speedwriting skills.\n>And finish another chapter of the report.\n>You finished [report_chapters] chapters so far."
    return
