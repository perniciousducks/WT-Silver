
### Misc Labels ###

label hide_characters:

    hide screen hermione_main
    #hide screen luna #Needs testing her events.
    hide screen cho_chang
    hide screen astoria_main
    hide screen susan_main
    hide screen tonks_main
    hide screen snape_main

    #Do not add transitions. Use one after return.

    return


label main_room:
    call hide_characters
    show screen blkfade
    with d3

    hide screen chair_left
    hide screen desk
    hide screen jerking_off_01 #Hermione topless. Genie jerking off.
    hide screen bld1
    hide screen blktone
    call her_chibi("hide")
    call sna_chibi("hide")
    call gen_chibi("hide")

    pause.2

    show screen genie
    call hide_blkfade

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

    return

label play_music(music=""):

    if music in ["stop","pause"]:
        stop music fadeout 1.0

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

    if music in ["hitman"]:
        play music "music/hitman.mp3" fadein 1 fadeout 1

    if music in ["boss_theme"]:
        play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1

    if music in ["sad","grape_soda"]:
        play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1

    return



#Narrator
label nar(text="",action=""):

    if action != "end": #Narration ended, blktone was already active.
        show screen blktone5
        with d3

    if text != "":
        $ renpy.say(s,text)

    if action != "start": #Narration just started, blktone won't get hidden.
        hide screen blktone5
        with d3

    return

#Adds star next to personal favours if you can gain whoring points.
label update_hints:

    #Does not add star to hardcore difficulty (3+)!
    #Favour 1
    if whoring < 3 and game_difficulty <= 2:
        $ hg_pf_TalkToMe_OBJ.progress_hint = True
    else:
        $ hg_pf_TalkToMe_OBJ.progress_hint = False

    #Favour 2
    if whoring < 3 and game_difficulty <= 2:
        $ hg_pf_NicePanties_OBJ.progress_hint = True
    else:
        $ hg_pf_NicePanties_OBJ.progress_hint = False

    #Favour 3
    if whoring >= 3 and whoring < 6 and game_difficulty <= 2:
        $ hg_pf_BreastMolester_OBJ.progress_hint = True
    else:
        $ hg_pf_BreastMolester_OBJ.progress_hint = False

    #Favour 4
    if whoring >= 3 and whoring < 6 and game_difficulty <= 2:
        $ hg_pf_ButtMolester_OBJ.progress_hint = True
    elif whoring >= 9 and not cho_known:
        $ hg_pf_ButtMolester_OBJ.progress_hint = True
    else:
        $ hg_pf_ButtMolester_OBJ.progress_hint = False

    #Favour 5
    if whoring >= 6 and whoring < 9 and game_difficulty <= 2:
        $ hg_pf_ShowThemToMe_OBJ.progress_hint = True
    else:
        $ hg_pf_ShowThemToMe_OBJ.progress_hint = False

    #Favour 6
    if whoring >= 9 and whoring < 12 and game_difficulty <= 2:
        $ hg_pf_DanceForMe_OBJ.progress_hint = True
    else:
        $ hg_pf_DanceForMe_OBJ.progress_hint = False

    #Favour 7
    if whoring >= 9 and whoring < 12 and game_difficulty <= 2:
        $ hg_pf_ShowMeYourAss_OBJ.progress_hint = True
    else:
        $ hg_pf_ShowMeYourAss_OBJ.progress_hint = False

    #Favour 8
    if whoring >= 9 and whoring < 12 and game_difficulty <= 2:
        $ hg_pf_LetMeTouchThem_OBJ.progress_hint = True
    else:
        $ hg_pf_LetMeTouchThem_OBJ.progress_hint = False

    #Favour 9
    if whoring >= 12 and whoring < 15 and game_difficulty <= 2:
        $ hg_pf_TouchMe_OBJ.progress_hint = True
    else:
        $ hg_pf_TouchMe_OBJ.progress_hint = False

    #Favour 10
    if whoring >= 15 and whoring < 18 and game_difficulty <= 2:
        $ hg_pf_TitJob_OBJ.progress_hint = True
    else:
        $ hg_pf_TitJob_OBJ.progress_hint = False

    #Favour 11
    if whoring >= 15 and whoring < 18 and game_difficulty <= 2:
        $ hg_pf_SuckIt_OBJ.progress_hint = True
    else:
        $ hg_pf_SuckIt_OBJ.progress_hint = False

    #Favour 12
    if whoring >= 18 and whoring < 21 and game_difficulty <= 2:
        $ hg_pf_LetsHaveSex_OBJ.progress_hint = True
    else:
        $ hg_pf_LetsHaveSex_OBJ.progress_hint = False

    #Favour 13
    if whoring >= 21 and whoring < 24 and game_difficulty <= 2:
        $ hg_pf_TimeForAnal_OBJ.progress_hint = True
    else:
        $ hg_pf_TimeForAnal_OBJ.progress_hint = False

    return
