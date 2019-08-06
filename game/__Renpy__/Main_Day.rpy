

#Day Start.

label day_start:
    call play_music("day_theme")
    show screen blkfade

    #$ renpy.set_style_preference("dialog", "Day")

    $ daytime = True #True when it is daytime. Turns False during nighttime.
    # Dont change UI if using nightmode
    if not persistent.nightmode:
        $ interface_color = "gold"

    $ temp_name = "Day - "+str(day)+"\nWhoring - "+str(her_whoring)
    $ save_name = temp_name

    ### RESETING STUFF ###
    call room(hide_screens=True)

    call reset_day_flags
    call reset_day_and_night_flags

    #Hermione Daily Flags.
    call reset_hermione

    #Luna Daily Flags.
    call reset_luna

    #Astoria Daily Flags.
    call update_astoria

    #Susan Daily Flags.
    call update_susan
    if susan_imperio_counter > 0:
        $ susan_imperio_counter -= 1            #Removes 1 at each new day.
        $ susan_imperio_influence = True
        if susan_imperio_counter <= 0:
            $ susan_imperio_influence = False
            call reset_susan_clothing

    #Cho Daily Flags.
    call update_cho

    #Tonks Daily Flags.
    call update_tonks

    #Snape Daily Flags.
    call update_snape

    #Genie Reset.
    call update_genie



    $ generating_snape_bonus = renpy.random.randint(1, 2) #Determines whether ot not Snape bonus will be added to the Slytherin house.
    $ generating_points = renpy.random.randint(1, 2) #Determines whether or not point will be awarded to Slytherin on this day. # MAKE NO CHANGES HERE. BEING USED AS "ONE_OUT_OF_TWO".
    $ generating_points_gryffindor = renpy.random.randint(1, 10)
    $ generating_points_hufflepuff = renpy.random.randint(1, 10)
    $ generating_points_ravenclaw = renpy.random.randint(1, 10)

    $ one_out_of_three = renpy.random.randint(1, 3)
    $ i_of_iv = renpy.random.randint(1, 4)
    $ one_of_five = renpy.random.randint(1, 5)
    $ i_of_vii = renpy.random.randint(1, 7)
    $ one_of_ten = renpy.random.randint(1, 10)
    $ one_of_tw = renpy.random.randint(1, 20)

    $ day_random = renpy.random.randint(0, 10)

    $ random_gold = renpy.random.randint(8, 120) # Money you find in the cupboard.



    scene black


    if day_of_week == 7: #Counts days of the week. Everyday +1. When day_of_week = 7 resets to zero.
        $ day_of_week = 0
        if finished_report >= 1:
            $ letter_paperwork_report_OBJ.mailLetter()
        if not first_random_twins:
            $ twins_interest = True

    $ day_of_week += 1

    $ day +=1


    ### WEATHER
    stop bg_sounds #Stops playing the fire SFX.
    stop weather #Stops playing the rain SFX.
    if day != 1:
        $ weather_gen = renpy.random.randint(1, 6)

    # Quidditch Matches
    if cc_event_pause == 0 and main_match_1_stage == "start":
        $ weather_gen = 1
    $ show_weather()



    # Package
    if deliveryQ.got_mail():
        $ package_is_here = True

    if clothing_mail_item != None:
        $ clothing_mail_timer -= 1

        if clothing_mail_timer <= 1:
            $ package_is_here = True

    call room("main_room", hide_screens=False) #Screens already get hidden above.

    hide screen blkfade
    with fade

    call points_changes #Makes house points changes.
    call house_points



    ### DAY EVENTS ###

    # Start Quests
    jump quests

    label day_resume:

    # Owl
    $ random_number = renpy.random.randint(1, 5)
    if random_number in [1]:
        $ owl_away = False
    if letter_queue_list != [] and not owl_away:
        call play_sound("owl")
        show screen owl
        with d3

    # Favors
    if hg_pr_sex_skip:#Hermione does not show up. This sends to label where she shows up next morning.
        $ hg_pr_sex.start() # hg_pr_sex_T1_intro_E2




    label day_main_menu:

    ### MENU PLACEMENT ###
    call reset_menu_position

    call hide_characters
    call gen_chibi("sit_behind_desk")
    with d3

    if bird_examined and desk_examined and cupboard_examined and door_examined and fireplace_examined and not genie_intro.E2_complete:
        jump genie_intro_E2

    call screen main_room_menu
