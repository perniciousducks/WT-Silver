# Common logic for day/night cycle

label common_start:
    call hide_all_screens
    show screen blkfade

    # Play a theme
    if daytime:
        call play_music("day_theme")
    else:
        call play_music("night_theme")

    # Set interface color
    if not persistent.nightmode and daytime:
        $ interface_color = "gold"
        $ txt_style = "day_text"
        $ btn_style = "daybtn"
        $ btn_hover = "#e3ba7140"
    else:
        $ interface_color = "gray"
        $ txt_style = "night_text"
        $ btn_style = "nightbtn"
        $ btn_hover = "#7d75aa40"

    # Set save filename
    $ temp_name = "Day - "+str(day)+"\nWhoring - "+str(her_whoring)
    $ save_name = temp_name

    # Update various time-based values
    if daytime:
        call update_day_values
    call update_day_and_night_values

    call points_changes # Calculates points
    call house_points   # Updates points

    # Reset character appearances (chibis, clothing, etc.)
    call reset_hermione
    call reset_luna
    call update_astoria
    call update_susan
    call update_cho
    call update_tonks
    call update_snape
    call update_genie

    scene black

    # Stop playing fire and weather sounds
    stop bg_sounds
    stop weather

    # Play owl arrival sound once per day/night start
    if letter_queue_list != [] and not owl_away:
        call play_sound("owl")

    $ show_weather()

    call room("main_room", hide_screens=False) # Screens already get hidden above

    hide screen blkfade
    with fade
    return

label update_day_values:
    $ fire_in_fireplace = False
    $ phoenix_is_fed = False
    $ phoenix_is_petted = False
    $ searched  = False #Turns true after you search the cupboard.
    $ owl_away = False

    # Snape
    if ss_event_pause > 0:
        $ ss_event_pause -= 1
    if ss_summon_pause > 0:
        $ ss_summon_pause -= 1

    # Tonks
    if nt_event_pause > 0:
        $ nt_event_pause -= 1
    if nt_summon_pause > 0:
        $ nt_summon_pause -= 1
    $ gave_tonks_gift    = False

    # Hermione
    if hg_event_pause > 0:
        $ hg_event_pause -= 1
    if hg_summon_pause > 0:
        $ hg_summon_pause -= 1
    $ gave_hermione_gift = False

    # Luna
    if ll_event_pause > 0:
        $ ll_event_pause -= 1
    if ll_summon_pause > 0:
        $ ll_summon_pause -= 1
    $ gave_luna_gift     = False

    # Cho
    if cc_event_pause > 0:
        $ cc_event_pause -= 1
    if cc_summon_pause > 0:
        $ cc_summon_pause -= 1
    $ gave_cho_gift      = False

    # Astoria
    if ag_event_pause > 0:
        $ ag_event_pause -= 1
    if ag_summon_pause > 0:
        $ ag_summon_pause -= 1
    $ gave_astoria_gift  = False

    # Susan
    if sb_event_pause > 0:
        $ sb_event_pause -= 1
    if sb_summon_pause > 0:
        $ sb_summon_pause -= 1
    $ gave_susan_gift    = False

    # Nicknames
    call set_random_nicknames

    # Mood
    if game_difficulty <= 1:   # Easy difficulty
        $ her_mood -= 3
        $ lun_mood -= 3
        $ cho_mood -= 3
        $ ast_mood -= 3
        $ sus_mood -= 3
    elif game_difficulty == 2: # Normal difficulty
        $ her_mood -= 2
        $ lun_mood -= 2
        $ cho_mood -= 2
        $ ast_mood -= 2
        $ sus_mood -= 2
        # Hardcore # Gifting items is required!

    if her_mood < 0:
        $ her_mood = 0
    if lun_mood < 0:
        $ lun_mood = 0
    if cho_mood < 0:
        $ cho_mood = 0
    if ast_mood < 0:
        $ ast_mood = 0
    if sus_mood < 0:
        $ sus_mood = 0

    # Set randomly awarded house points
    $ generating_snape_bonus = renpy.random.randint(1, 2) #Determines whether ot not Snape bonus will be added to the Slytherin house.
    $ generating_points = renpy.random.randint(1, 2) #Determines whether or not point will be awarded to Slytherin on this day. # MAKE NO CHANGES HERE. BEING USED AS "ONE_OUT_OF_TWO".
    $ generating_points_gryffindor = renpy.random.randint(1, 10)
    $ generating_points_hufflepuff = renpy.random.randint(1, 10)
    $ generating_points_ravenclaw = renpy.random.randint(1, 10)

    # Set random variables
    $ one_out_of_three = renpy.random.randint(1, 3)
    $ i_of_iv = renpy.random.randint(1, 4)
    $ one_of_five = renpy.random.randint(1, 5)
    $ i_of_vii = renpy.random.randint(1, 7)
    $ one_of_ten = renpy.random.randint(1, 10)
    $ one_of_tw = renpy.random.randint(1, 20)

    $ day_random = renpy.random.randint(0, 10)

    $ random_gold = renpy.random.randint(8, 120) # Money you find in the cupboard.

    # Count days of the week. Every day +1. When day_of_week = 7, reset to zero.
    if day_of_week == 7:
        $ day_of_week = 0
        if finished_report >= 1:
            call update_report_money
            $ letter_min_report.mailLetter()
        if not first_random_twins:
            $ twins_interest = True

    $ day_of_week += 1
    $ day +=1

    # Change the weather
    if day != 1:
        $ weather_gen = renpy.random.randint(1, 6)

    # Change the weather for Quidditch Matches
    if cc_event_pause == 0 and main_match_1_stage == "start":
        $ weather_gen = 1

    # Package delivery
    if deliveryQ.got_mail():
        $ package_is_here = True

    if clothing_mail_item != None:
        $ clothing_mail_timer -= 1

        if clothing_mail_timer <= 1:
            $ package_is_here = True

    return


label update_day_and_night_values:

    # Snape
    if ss_summon_pause == 0:
        $ snape_busy = False
    $ chitchated_with_snape = False

    # Tonks
    if nt_summon_pause == 0:
        $ tonks_busy = False
    $ chitchated_with_tonks = False

    # Hermione
    if hg_summon_pause == 0:
        $ hermione_busy = False
    $ chitchated_with_her = False
    $ hermione_door_event_happened = False
    $ her_random_number = renpy.random.randint(1, 5) #Used for Map screen. Gets defined once during day and night.
    call set_her_map_location()

    # Luna
    if ll_summon_pause == 0:
        $ luna_busy = False
    $ chitchated_with_luna = False
    $ lun_random_number = renpy.random.randint(1, 5) #Used for Map screen. Gets defined once during day and night.
    call set_lun_map_location()

    # Cho
    if cc_summon_pause == 0:
        $ cho_busy = False
    $ chitchated_with_cho = False
    $ cho_random_number = renpy.random.randint(1, 5) #Used for Map screen. Gets defined once during day and night.
    call set_cho_map_location()

    # Astoria
    if ag_summon_pause == 0:
        $ astoria_busy = False
    $ chitchated_with_astoria = False
    $ ast_random_number = renpy.random.randint(1, 5) #Used for Map screen. Gets defined once during day and night.
    call set_ast_map_location()

    # Susan
    if sb_summon_pause == 0:
        $ susan_busy = False
    $ chitchated_with_susan = False
    $ sus_random_number = renpy.random.randint(1, 5) #Used for Map screen. Gets defined once during day and night.
    call set_sus_map_location()

    return
