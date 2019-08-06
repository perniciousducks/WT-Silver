#Night Start.
label night_start:
    call play_music("night_theme")
    show screen blkfade

    #    $ renpy.set_style_preference("dialog", "Night")
    # $ textColor = "#1e1008"

    $ daytime = False
    $ interface_color = "gray"

    $ temp_name = "Day - "+str(day)+"\nWhoring - "+str(her_whoring)
    $ save_name = temp_name

    ###RESET STUFF
    call room(hide_screens=True)

    call reset_day_and_night_flags

    # Hermione
    call reset_hermione

    #Luna
    call reset_luna

    #Astoria
    call update_astoria

    #Susan
    call update_susan

    #Cho
    call update_cho

    #Tonks
    call update_tonks

    #Snape
    call update_snape

    #Genie
    call update_genie


    scene black

    ### WEATHER ###
    stop bg_sounds #Stops playing the fire SFX.
    stop weather #Stops playing the rain SFX.
    $ show_weather()

    call room("main_room", hide_screens=False) #Screens already get hidden above.

    hide screen blkfade
    with fade

    call points_changes #Makes house points changes.



    ### NIGHT EVENTS ###

    # Start Quests
    jump quests

    label night_resume:

    # Owl
    $ random_number = renpy.random.randint(1, 5)
    if random_number in [1]:
        $ owl_away = False
    if letter_queue_list != [] and not owl_away:
        call play_sound("owl")
        show screen owl
        with d3

    # Favors
    python:
        for i in nt_requests_list:
            if i.inProgress:
                i.inProgress = False
                i.start()

        for i in cc_requests_list:
            if i.inProgress:
                i.inProgress = False
                i.start()

        for i in hg_requests_list:
            if i.inProgress:
                i.inProgress = False
                i.start()
        for i in hg_ps_list: #Call any public shaming event if it's in progress
            if i.inProgress:
                renpy.jump(i.complete_label)


    # Hermione Events.
    if current_job == 1:
        jump maid_responses
    if current_job == 2:
        jump barmaid_responses
    if current_job == 3:
        jump gryffindor_cheer_responses
    if current_job == 4:
        jump slytherin_cheer_responses
    if current_job == 5:
        jump hermione_helping_selling_cards

    #Hermione Potions return.
    # if cat_ears_potion_return:
        # jump potion_scene_1_1_2  <--- Missing label
    if transparent_quest:
        $ transparent_quest = False
        jump potion_scene_4_2
    # if addicted == True:
        # jump potion_scene_3_1_2  <--- Missing label

    if milking == -1:
        call potion_scene_11_1_2 #Returns
    #if milking == -3:
        #call potion_scene_11_3_2 <- label does not exist


    #Atoria / Tonks event return.
    if astoria_tonks_event_in_progress:
        jump astoria_tonks_event #These do not return to 'night_resume'!



label night_main_menu:
    ### MENU PLACEMENT ###
    call reset_menu_position

    call hide_characters
    call gen_chibi("sit_behind_desk")
    with d3

    call screen main_room_menu
