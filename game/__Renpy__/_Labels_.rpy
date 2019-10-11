# Hide all character images (not chibi)
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
    # Do not add transitions. Use one after return.
    return

label hide_screens:
    # Remove all displayables on layer 'screens'
    $ renpy.scene("screens")

    # Screens that are never hidden
    if not renpy.variant('android'):
        show screen mouse_tooltip

    return

label update_interface_color(color=None):
    if color in ["gold", "gray"]:
        $ interface_color = color
    elif not persistent.nightmode and daytime:
        $ interface_color = "gold"
    else:
        $ interface_color = "gray"
    if interface_color == "gold":
        $ txt_style = "day_text"
        $ btn_style = "daybtn"
        $ btn_hover = "#e3ba7140"
    else:
        $ txt_style = "night_text"
        $ btn_style = "nightbtn"
        $ btn_hover = "#7d75aa40"
    return

label stop_sound_effects:
    stop bg_sounds fadeout 0.5
    stop weather fadeout 0.5
    return

label fireplace_sound:
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 0.5 fadein 0.5 if_changed
    else:
        stop bg_sounds fadeout 0.5
    return

# Set the scene for a given room
label room(room=None, hide_screens=True, stop_sound=True):

    # Hide all screens (only room related screens are shown)
    if hide_screens:
        call hide_screens

    # Stop sound effects (necessary when changing rooms)
    if stop_sound:
        call stop_sound_effects

    if room in ["main_room", "main"]:
        $ current_room = "main_room"

        # Update sound effects
        call weather_sound
        call fireplace_sound

        # Show main_room and (optional) objects
        show screen main_room
        show screen chair_right
        show screen fireplace

        if fire_in_fireplace:
            show screen fireplace_fire
        else:
            hide screen fireplace_fire

        if phoenix_is_fed:
            show screen phoenix_food
        else:
            hide screen phoenix_food

        if letter_queue_list != [] and not owl_away:
            show screen owl
        else:
            hide screen owl

        if package_is_here:
            show screen package
        else:
            hide screen package

        show screen genie

        # User interface
        call house_points
        show screen ui_top_bar

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


# Return to main_room at resume point (after quests, before events)
# Used to return from event sequences
label main_room:
    call room("main_room", stop_sound=False)
    with d3

    call reset_menu_position
    call music_block

    if daytime:
        jump day_resume
    else:
        jump night_resume


# Return to main_room at menu point (after quests and events)
# Used to return from main room interactions
label main_room_menu:
    call room("main_room", stop_sound=False)
    with d3

    call reset_menu_position
    call music_block

    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu


label setup_fireplace_hangout(char=None):

    if not daytime: # Night time
        show screen blkfade

        $ fire_in_fireplace = True

        call hide_characters
        call gen_chibi("hide")
        call sna_chibi("hide")
        call ton_chibi("hide")
        hide screen chair_right
        show screen desk

        show screen fireplace_fire
    else: # Daytime
        stop bg_sounds
        show screen blkfade

        $ fire_in_fireplace = False

        call hide_characters
        call gen_chibi("hide")
        call sna_chibi("hide")
        call ton_chibi("hide")
        hide screen chair_right
        show screen desk

    # Proceed as usual
    if char == "snape":
        show screen with_snape(ani=True)
    elif char == "tonks":
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


#TODO One keyword per theme (use == instead of x in [..] checks, possibly define everything in a dictionary to simplify code further)
label play_music(music=""):
    if music in ["stop","pause"]:
        stop music fadeout 1.0
        return

    # Harry Potter
    if music in ["hedwigs_theme", "hogwarts"]:
        play music "music/01 Prologue.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["ball_theme", "ball"]:
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["festive", "xmas"]:
        play music "music/07 Introducing Colin2.mp3" fadein 1 fadeout 1 if_changed
    elif music == "quidditch":
        play music "music/11 The Quidditch Match_original.mp3" fadein 1 fadeout 1 if_changed
    # Character Music
    elif music in ["snape", "snape_theme", "dark_fog"]:
        # Snape
        play music "music/Dark Fog.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["hermione", "hermione_theme", "chipper_doodle"]:
        # Hermione
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["cho", "cho_theme", "happy_adventure"]:
        # Cho
        play music "music/fuzzball-parade-by-kevin-macleod.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["astoria", "astoria_theme"]:
        # Astoria
        play music "music/KMcL_OpenThoseBrightEyes.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["susan", "susan_theme"]:
        # Susan
        play music "music/teddy-bear-waltz-by-kevin-macleod.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["tonks", "tonks_theme"]:
        # Tonks
        play music "music/scheming-weasel-slower-version-by-kevin-macleod.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["luna", "luna_theme"]:
        # Luna
        play music "music/wallpaper-by-kevin-macleod.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["playful", "playful_tension"]:
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["silly", "fun", "silly_fun_loop"]:
        play music "music/silly_fun_loop.mp3" fadein 1 fadeout 1 if_changed

    # Store Music
    elif music in ["weasley_store"]:
        play music "music/weasley_store.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["clothing_store"]:
        play music "music/clothing_store.mp3" fadein 1 fadeout 1 if_changed

    # Background Music
    elif music in ["day", "day_theme", "brittle_rille"]:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["night", "night_theme", "manatees"]:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["night_outside", "outside_night"]:
        play music "sounds/night.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["jazz_take"]:
        play music "sounds/jazz take 2.mp3" fadein 1 fadeout 1 if_changed

    # Interface
    elif music in ["my_immortal"]:
        play music "music/Spring_In_My_Step.mp3" fadein 0.2 fadeout 0.2 if_changed

    # Misc
    elif music in ["hitman"]:
        play music "music/hitman.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["boss_theme"]:
        play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["boss_card_theme"]:
        play music "music/Juhani_Junkala.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["sad","grape_soda"]:
        play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 0.2 fadeout 0.5 if_changed
    elif music in ["anguish"]:
        play music "music/Anguish.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["trance"]:
        play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1 if_changed
    elif music in ["despair"]:
        play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 if_changed

    else:
        python:
            try:
                renpy.music.play(filenames="music/"+music+".mp3", channel="music", loop=True, fadeout=1.0, fadein=1.0)
            except IOError:
                pass
    return

# Play day/night theme
label music_block:
    if daytime:
        call play_music("day_theme")
    else:
        call play_music("night_theme")
    return

label vague_idea:
    call nar(">You lack imagination for an idea of this caliber.")
    return

label increase_house_points(house="Add house", points=0):
    call bld
    $ renpy.play('sounds/win_04.mp3')
    show screen notes
    if house in ["gryffindor","g","gryff"]:
        $ gryffindor += points
        ">Gryffindor has received [points] house points today!"
    elif house in ["hufflepuff","h","huffl"]:
        $ hufflepuff += points
        ">Hufflepuff has received [points] house points today!"
    elif house in ["ravenclaw","r","raven"]:
        $ ravenclaw += points
        ">Ravenclaw has received [points] house points today!"
    else:
        $ slytherin += points
        ">Slytherin has received [points] house points today!"
    hide screen notes

    return


label chibi_walk_desk_blkfade(char=None):

    call hide_characters
    hide screen blktone
    hide screen bld1
    with d3
    pause.2

    if char == "hermione":
        call her_walk(xpos="desk", ypos="base", speed=2, loiter=False, redux_pause=2)
    elif char == "tonks":
        call ton_walk(xpos="desk", ypos="base", speed=2, loiter=False, redux_pause=2)

    call blkfade

    return

label adjust_game_difficulty(dif=None):
    if 1 <= dif <= 3:
        $ game_difficulty = dif

    if game_difficulty <= 1:
        $ cheat_reading = True
        $ wine_ITEM.cost = 40
        $ firewhisky_ITEM.cost = 60
    elif game_difficulty == 2:
        $ cheat_reading = False
        $ wine_ITEM.cost = 60
        $ firewhisky_ITEM.cost = 80
    else:
        $ cheat_reading = False
        $ wine_ITEM.cost = 140
        $ firewhisky_ITEM.cost = 160
    return
