
### Misc Labels ###
label hide_all_screens:

    #Sprites
    call hide_characters

    #Chibis
    call her_chibi("hide")
    call lun_chibi("hide")
    call sus_chibi("hide")
    call cho_chibi("hide")
    call sna_chibi("hide")
    call gen_chibi("hide")

    #CGs
    hide screen cg
    hide screen ccg
    hide screen blkback

    #Main Room
    hide screen main_room
    hide screen main_room_overlay
    hide screen weather
    hide screen new_window #Hiding clear sky bg.

    hide screen desk
    hide screen chair_left
    hide screen chair_right

    hide screen fireplace
    hide screen fireplace_fire
    hide screen fireplace_glow

    hide screen phoenix_food
    hide screen animation_feather

    hide screen with_snape #Genie hangs out with Snape in front of the fireplace.
    hide screen with_snape_animated #Genie hangs out with Snape in front of the fireplace.
    hide screen with_tonks_animated
    hide screen done_reading
    hide screen done_reading_near_fire

    hide screen package
    hide screen owl

    #Weasley Store
    hide screen weasley_store_room

    #Clothing Store
    hide screen clothing_store_room

    #Potions Room
    hide screen potions_room

    #7th Floor
    hide screen floor_7th_door
    hide screen room_of_req_door
    hide screen floor_7th_screen
    hide screen floor_7th_menu

    #Room of Requirement
    hide screen room_of_requirement
    hide screen room_of_requirement_menu
    hide screen room_of_requirement_overlay
    hide screen candle_light_1
    hide screen candle_light_2
    hide screen whose_points_screen

    #Quidditch pitch
    hide screen quidditch_pitch
    hide screen quidditch_pitch_overlay

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

    #Sounds
    stop bg_sounds #Stops playing the fire SFX.

    return


label hide_characters:

    hide screen hermione_main
    hide screen hermione_ass
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
        show screen main_room_overlay
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

        call house_points
        show screen points

        call gen_chibi("sit_behind_desk")

    if room in ["weasley_store"]:
        $ current_room = "weasley_store"

        show screen weasley_store_room

    if room in ["potions_room","potions_classroom"]:
        $ current_room = "potions_classroom"

        show screen potions_room

    if room in ["clothing_store", "clothe_store"]:
        $ current_room = "clothing_store"

        show screen clothing_store_room

    if room in ["7th floor"]:
        $ current_room = "7th_floor"

        show screen floor_7th_door
        show screen room_of_req_door
        show screen floor_7th_screen

    if room in ["room_of_requirement","ror"]:
        $ current_room = "room_of_requirement"

        show screen room_of_requirement

    if room in ["quidditch_pitch", "quid", "qp"]:
        $ current_room = "quidditch_pitch"

        show screen quidditch_pitch
        show screen quidditch_pitch_overlay

    return



label main_room:
    show screen blkfade

    #Predict and cache all often used images for the room
    #$ renpy.start_predict("interface/desk/*.*")
    #$ renpy.start_predict("interface/map/*.*")
    #$ renpy.start_predict("interface/icons/*.*")
    #$ renpy.start_predict("interface/frames/*.*")
    #$ renpy.start_predict("images/rooms/_objects_/*.*")
    #$ renpy.start_predict("images/rooms/_weather_/*.*")
    #$ renpy.start_predict("characters/genie/chibis/working/*.*")
    #$ renpy.start_predict("images/animation/rum_*.*")
    #$ renpy.start_predict("characters/genie/chibis/reading/*.*")
    #$ renpy.start_predict("characters/genie/chibis/masturbating/desk_*.*")

    call room("main_room")

    hide screen blkfade
    with d3

    call reset_menu_position

    if daytime:
        call play_music("day_theme")
    else:
        call play_music("night_theme")

    pause.5

    if daytime:
        jump day_resume
    else:
        jump night_resume



label setup_fireplace_hangout(char=None):
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0
    show screen blkfade

    $ fire_in_fireplace = True

    call hide_characters
    call gen_chibi("hide")
    call sna_chibi("hide")
    hide screen chair_right
    show screen desk

    show screen fireplace_fire
    if char == "snape":
        show screen with_snape_animated
    if char == "tonks":
        show screen with_tonks_animated

    hide screen bld1
    hide screen blkfade
    with fade

    return



# Reset menu
label reset_menu_position:

    $ menu_x = 0.5
    $ menu_y = 0.6

    return


label reset_day_flags:
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

    return



label reset_day_and_night_flags:

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



label bld(action=None):
    if action == "hide":
        hide screen bld1
    else:
        show screen bld1
    with d3

    return

label blktone:
    show screen bld1 #Making sure it's active. Blktone looks stupid without.
    show screen blktone
    with d5

    return

label hide_blktone:
    hide screen blktone
    with d5

    return

label blkfade:
    hide screen bld1
    hide screen blktone
    show screen blkfade
    with d5
    pause.2

    return

label hide_blkfade:
    hide screen blkfade
    with d5

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
    if spell in ["revelio","imperio"]:

        stop music fadeout 2.0
        call play_sound("spell")
        show screen white
        pause.1
        hide screen white
        with hpunch

    return


label play_sound(sound=""):

    # Objects
    if sound in ["knock", "knocking"]:
        $ renpy.play('sounds/knocking.mp3')
    if sound in ["door"]:
        $ renpy.play('sounds/door.mp3')
    if sound in ["lock","unlock"]:
        $ renpy.play('sounds/09_lock.wav')
    if sound in ["desk","climb_desk"]:
        $ renpy.play('sounds/08_hop_on_desk.mp3')
    if sound in ["owl"]:
        play sound "sounds/owl.mp3"

    # Ambience
    if sound in ["applause"]:
        $ renpy.play('sounds/applause01.ogg')

    # Affection
    if sound in ["gulp", "gulping", "swallow", "swallowing"]:
        $ renpy.play('sounds/gulp.mp3')
    if sound in ["slap", "slapping"]:
        $ renpy.play('sounds/slap_02.mp3')
    if sound in ["spit", "spitting"]:
        $ renpy.play('sounds/spit.mp3')
    if sound in ["kick", "kicking", "bump"]:
        $ renpy.play('sounds/kick.ogg')
    if sound in ["kiss", "kissing"]:
        $ renpy.play('sounds/kiss.mp3')
    if sound in ["insert", "inserting", "goo"]:
        $ renpy.play('sounds/gltch.mp3')
    if sound in ["boing"]:
        $ renpy.play('sounds/boing.mp3')
    if sound in ["pop", "bottle"]:
        $ renpy.play('sounds/bottle.mp3')

    # Magic
    if sound in ["spell"]:
        $ renpy.play('sounds/magic2.mp3')
    if sound in ["magic"]:
        $ renpy.play('sounds/magic4.ogg')

    # Movement
    if sound in ["footsteps"]:
        $ renpy.play('sounds/footsteps.mp3')
    if sound in ["walking"]:
        $ renpy.play('sounds/run_04.mp3')
    if sound in ["running"]:
        $ renpy.play('sounds/run_03.mp3')
    if sound in ["sprinting"]:
        $ renpy.play('sounds/run_02.mp3')
    if sound in ["walking_on_grass", "grass"]:
        $ renpy.play('sounds/steps_grass.mp3')

    # Interface
    if sound in ["scroll"]:
        $ renpy.play('sounds/scroll.mp3')
    if sound in ["equip", "equip_inventory"]:
        $ renpy.play('sounds/cloth_sound.mp3')

    # Misc
    if sound in ["scratch"]:
        $ renpy.play('sounds/scratch.wav')
    if sound in ["shatter"]:
        $ renpy.play('sounds/glass_shatter.mp3')
    if sound in ["glass_break","glass"]:
        $ renpy.play('sounds/glass_break.mp3')

    return



label play_music(music=""):
    if music in ["stop","pause"]:
        stop music fadeout 1.0

    # Harry Potter
    if music in ["hedwigs_theme", "hogwarts"]:
        play music "music/01 Prologue.mp3" fadein 1 fadeout 1 if_changed
    if music in ["ball_theme", "ball"]:
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 if_changed
    if music in ["festive", "xmas"]:
        play music "music/07 Introducing Colin2.mp3" fadein 1 fadeout 1 if_changed

    # Character Music
    if music in ["snape", "snape_theme", "dark_fog"]:
        play music "music/Dark Fog.mp3" fadein 1 fadeout 1 if_changed
    if music in ["hermione", "hermione_theme", "chipper_doodle"]:
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 if_changed
    if music in ["cho", "cho_theme", "happy_adventure"]:
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 if_changed #Placeholder
    if music in ["playful", "playful_tension"]:
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 if_changed
    if music in ["silly", "fun", "silly_fun_loop"]:
        play music "music/silly_fun_loop.mp3" fadein 1 fadeout 1 if_changed

    # Store Music
    if music in ["weasley_store"]:
        play music "music/weasley_store.mp3" fadein 1 fadeout 1 if_changed
    if music in ["clothing_store"]:
        play music "music/clothing_store.mp3" fadein 1 fadeout 1 if_changed

    # Background Music
    if music in ["day", "day_theme", "brittle_rille"]:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 if_changed
    if music in ["night", "night_theme", "manatees"]:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 if_changed
    if music in ["night_outside", "outside_night"]:
        play music "sounds/night.mp3" fadein 1 fadeout 1 if_changed
    if music in ["jazz_take"]:
        play music "sounds/jazz take 2.mp3" fadein 1 fadeout 1 if_changed

    # Interface
    if music in ["my_immortal"]:
        play music "music/Spring_In_My_Step.mp3" fadein 0.2 fadeout 0.2 if_changed

    # Misc
    if music in ["hitman"]:
        play music "music/hitman.mp3" fadein 1 fadeout 1 if_changed
    if music in ["boss_theme"]:
        play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1 if_changed
    if music in ["boss_card_theme"]:
        play music "music/Juhani_Junkala.mp3" fadein 1 fadeout 1 if_changed
    if music in ["sad","grape_soda"]:
        play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 0.2 fadeout 0.5 if_changed
    if music in ["anguish"]:
        play music "music/Anguish.mp3" fadein 1 fadeout 1 if_changed

    return

### MUSIC BLOCK ###
label music_block:
    if daytime:
        call play_music("day_theme")
    else:
        call play_music("night_theme")
    return

### YOU LUCK IMAGINATION ###
label vague_idea:

    call nar(">You lack imagination for an idea of this caliber.")

    return
