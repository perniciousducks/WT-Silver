
### Misc Labels ###

label hide_characters:
    
    hide screen hermione_main
    #hide screen luna #Needs testing her events.
    #hide screen cho_chang #Needs testing her events.
    hide screen astoria_main
    hide screen susan_main
    hide screen tonks_main
    hide screen snape_main
    
    #Do not add transitions. Use one after return.
    
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
        
    if sound in ["spell"]:
        $ renpy.play('sounds/magic2.mp3')
        
    if sound in ["magic"]:
        $ renpy.play('sounds/magic4.mp3')
        
    return

label play_music(music=""): 

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
        $ renpy.say(nar,text)

    if action != "start": #Narration just started, blktone won't get hidden.
        hide screen blktone5
        with d3

    return

