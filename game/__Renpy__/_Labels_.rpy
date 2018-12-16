
### Misc Labels ###
label hide_all_screens:

    #Sprites
    call hide_characters

    #Chibis
    call her_chibi("hide")
    call lun_chibi("hide")
    call sus_chibi("hide")
    call sna_chibi("hide")
    call gen_chibi("hide")

    #CGs
    hide screen ccg
    hide screen end_u_1
    hide screen end_u_3

    #Main Room
    hide screen main_room
    hide screen main_room_deco
    hide screen weather
    hide screen new_window #Hiding clear sky bg.

    hide screen chair_left
    hide screen chair_right

    hide screen fireplace
    hide screen fireplace_fire
    hide screen fireplace_glow

    hide screen phoenix_food
    hide screen animation_feather

    hide screen with_snape #Genie hangs out with Snape in front of the fireplace.
    hide screen with_snape_animated #Genie hangs out with Snape in front of the fireplace.
    hide screen done_reading
    hide screen done_reading_near_fire

    hide screen package
    hide screen owl

    #Weasley Store
    hide screen weasley_store_room

    #7th Floor
    hide screen floor_7th_door
    hide screen room_of_req_door
    hide screen floor_7th_screen
    hide screen floor_7th_menu

    #Room of Requirement
    hide screen room_of_requirement
    hide screen room_of_requirement_menu
    hide screen candle_light_1
    hide screen candle_light_2
    hide screen whose_points_screen

    #A Dark Room (minigame)
    hide screen dark_room
    hide screen DRgame_blktone

    #General
    hide screen main_room_menu
    hide screen points
    hide screen notes

    #Filters
    hide screen blktone
    hide screen bld1



    return


label hide_characters:

    hide screen hermione_main
    hide screen hermione_main_ass
    hide screen luna_main
    hide screen cho_chang
    hide screen astoria_main
    hide screen susan_main

    hide screen tonks_main
    hide screen snape_main
    hide screen genie_main

    #Do not add transitions. Use one after return.

    return



label room(room=None, hide_screens=True):

    if hide_screens:
        call hide_all_screens

    if room in ["main_room", "main"]:
        $ current_room = "main_room"

        show screen weather
        show screen main_room
        show screen main_room_deco
        show screen chair_right
        hide screen fireplace_fire
        if fire_in_fireplace:
            play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0
            show screen fireplace_fire
        show screen animation_feather
        hide screen phoenix_food
        if phoenix_is_fed:
            show screen phoenix_food
        hide screen owl
        if letter_queue_list != []:
            show screen owl
        hide screen package
        if package_is_here:
            show screen package

        show screen points

        call gen_chibi("sit_behind_desk")

    if room in ["weasley_store"]:
        $ current_room = "weasley_store"

        show screen weasley_store_room
        show screen points

    if room in ["potions_room","potions_room"]:
        $ current_room = "potions_classroom"

        show screen weasley_store_room #Temporary
        show screen points

    if room in ["clothing_store", "clothe_store"]:
        $ current_room = "clothing_store"

        show screen weasley_store_room #Temporary
        show screen points

    if room in ["7th floor"]:
        show screen floor_7th_door
        show screen room_of_req_door
        show screen floor_7th_screen

    if room in ["room_of_requirement","ror"]:
        show screen room_of_requirement

    return



label main_room:
    show screen blkfade

    call room("main_room")

    hide screen blkfade
    with d3

    $ menu_x = 0.5
    $ menu_y = 0.5

    if daytime:
        call play_music("day_theme")
    else:
        call play_music("night_theme")

    pause.5

    if daytime:
        jump day_resume
    else:
        jump night_resume



label reset_day_flags:
    $ fire_in_fireplace = False
    $ phoenix_is_fed = False
    $ phoenix_is_petted = False
    $ searched  = False #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.

    return

label reset_day_and_night_flags:
    $ her_random_number = renpy.random.randint(1, 5) #Used for Map screen. Gets defined once during day and night.
    call set_her_map_location()

    $ lun_random_number = renpy.random.randint(1, 5) #Used for Map screen. Gets defined once during day and night.
    call set_lun_map_location()

    $ ast_random_number = renpy.random.randint(1, 5) #Used for Map screen. Gets defined once during day and night.
    call set_ast_map_location()

    $ sus_random_number = renpy.random.randint(1, 5) #Used for Map screen. Gets defined once during day and night.
    call set_sus_map_location()

    $ cho_random_number = renpy.random.randint(1, 5) #Used for Map screen. Gets defined once during day and night.
    call set_cho_map_location()

    return


label bld:
    show screen bld1
    with d3

    return

label blktone:
    show screen bld1 #Making sure it's active. Blktone looks stupid without.
    show screen blktone
    with d3

    return

label hide_blktone:
    hide screen blktone
    with d3

    return

label blkfade:
    hide screen bld1
    hide screen blktone
    show screen blkfade
    with d3
    pause.2

    return

label hide_blkfade:
    hide screen blkfade
    with d3

    return

label ctc:
    show screen ctc
    with d3
    pause
    hide screen ctc
    with d1

    return



label cum_block:
    show screen white
    pause.1
    hide screen white
    pause.2
    show screen white
    pause.1
    hide screen white
    with hpunch

    return

label slap_her:
    call play_sound("slap") #SLAP!
    show screen white
    with hpunch
    pause.08
    hide screen white

    return

label kiss_her:
    call play_sound("kiss") #Kiss!
    with hpunch
    pause.08

    return

label spit_on_her:
    call play_sound("spit") #Kiss!
    show screen white
    pause.2
    hide screen white
    with hpunch
    pause.08

    return

label cast_spell(spell=""):
    if spell == "imperio":

        stop music fadeout 2.0
        call play_sound("spell")
        show screen white
        pause.1
        hide screen white
        with hpunch

    return


label play_sound(sound=""):

    if sound in ["knocking"]:
        $ renpy.play('sounds/knocking.mp3')

    if sound in ["door"]:
        $ renpy.play('sounds/door.mp3')

    if sound in ["owl"]:
        play sound "sounds/owl.mp3"  #Quiet...

    if sound in ["glass_break","glass"]:
        $ renpy.play('sounds/glass_break.mp3')

    if sound in ["scratch"]:
        $ renpy.play('sounds/scratch.wav')

    if sound in ["slap","slapping"]:
        $ renpy.play('sounds/slap_02.mp3')

    if sound in ["kick","bump"]:
        $ renpy.play('sounds/kick.ogg')

    if sound in ["kiss","kissing"]:
        $ renpy.play('sounds/kiss.mp3')

    if sound in ["bottle","pop"]:
        $ renpy.play('sounds/bottle.mp3')

    if sound in ["spell"]:
        $ renpy.play('sounds/magic2.mp3')

    if sound in ["magic"]:
        $ renpy.play('sounds/magic4.mp3')

    if sound in ["walking_on_grass","grass"]:
        $ renpy.play('sounds/steps_grass.mp3')

    if sound in ["scroll"]:
        $ renpy.play('sounds/scroll.mp3')

    return


label play_music(music=""):

    if music in ["stop","pause"]:
        stop music fadeout 1.0

    if music in ["hedwigs_theme"]:
        play music "music/01 Prologue.mp3" fadein 1 fadeout 1

    if music in ["dark_fog","snape_theme"]:
        play music "music/Dark Fog.mp3" fadein 1 fadeout 1

    if music in ["chipper_doodle","hermione_theme"]:
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1

    if music in ["playful_tension","playful"]:
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1

    if music in ["silly_fun_loop","silly","fun"]:
        play music "music/silly_fun_loop.mp3" fadein 1 fadeout 1

    if music in ["brittle_rille","day_theme"]:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1

    if music in ["manatees","night_theme"]:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1

    if music in ["outside_night","night_outside"]:
        play music "sounds/night.mp3" fadein 1 fadeout 1

    if music in ["hitman"]:
        play music "music/hitman.mp3" fadein 1 fadeout 1

    if music in ["boss_theme"]:
        play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1

    if music in ["sad","grape_soda"]:
        play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1

    return



#Adds star next to personal favours if you can gain her_whoring points.
label update_hints:

    #Does not add star to hardcore difficulty (3+)!
    #Favour 1
    if her_whoring < 3 and game_difficulty <= 2:
        $ hg_pf_TalkToMe_OBJ.progress_hint = True
    else:
        $ hg_pf_TalkToMe_OBJ.progress_hint = False

    #Favour 2
    if her_whoring < 3 and game_difficulty <= 2:
        $ hg_pf_NicePanties_OBJ.progress_hint = True
    else:
        $ hg_pf_NicePanties_OBJ.progress_hint = False

    #Favour 3
    if her_whoring >= 3 and her_whoring < 6 and game_difficulty <= 2:
        $ hg_pf_BreastMolester_OBJ.progress_hint = True
    else:
        $ hg_pf_BreastMolester_OBJ.progress_hint = False

    #Favour 4
    if her_whoring >= 3 and her_whoring < 9 and game_difficulty <= 2:
        $ hg_pf_ButtMolester_OBJ.progress_hint = True
    elif her_whoring >= 9 and not cho_known:
        $ hg_pf_ButtMolester_OBJ.progress_hint = True
    else:
        $ hg_pf_ButtMolester_OBJ.progress_hint = False

    #Favour 5
    if her_whoring >= 6 and her_whoring < 9 and game_difficulty <= 2:
        $ hg_pf_ShowThemToMe_OBJ.progress_hint = True
    else:
        $ hg_pf_ShowThemToMe_OBJ.progress_hint = False

    #Favour 6
    if her_whoring >= 9 and her_whoring < 12 and game_difficulty <= 2:
        $ hg_pf_DanceForMe_OBJ.progress_hint = True
    else:
        $ hg_pf_DanceForMe_OBJ.progress_hint = False

    #Favour 7
    if her_whoring >= 12 and her_whoring < 15 and game_difficulty <= 2:
        $ hg_pf_ShowMeYourAss_OBJ.progress_hint = True
    else:
        $ hg_pf_ShowMeYourAss_OBJ.progress_hint = False

    #Favour 8
    if her_whoring >= 12 and her_whoring < 15 and game_difficulty <= 2:
        $ hg_pf_TouchMe_OBJ.progress_hint = True
    else:
        $ hg_pf_TouchMe_OBJ.progress_hint = False

    #Favour 9
    if her_whoring >= 15 and her_whoring < 18 and game_difficulty <= 2:
        $ hg_pf_TitJob_OBJ.progress_hint = True
    else:
        $ hg_pf_TitJob_OBJ.progress_hint = False

    #Favour 10
    if her_whoring >= 15 and her_whoring < 18 and game_difficulty <= 2:
        $ hg_pf_SuckIt_OBJ.progress_hint = True
    else:
        $ hg_pf_SuckIt_OBJ.progress_hint = False

    #Favour 11
    if her_whoring >= 18 and her_whoring < 21 and game_difficulty <= 2:
        $ hg_pf_LetsHaveSex_OBJ.progress_hint = True
    else:
        $ hg_pf_LetsHaveSex_OBJ.progress_hint = False

    #Favour 12
    if her_whoring >= 21 and her_whoring < 24 and game_difficulty <= 2:
        $ hg_pf_TimeForAnal_OBJ.progress_hint = True
    else:
        $ hg_pf_TimeForAnal_OBJ.progress_hint = False

    return
