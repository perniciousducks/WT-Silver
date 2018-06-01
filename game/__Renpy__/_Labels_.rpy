
### Misc Labels ###

label hide_characters:
    
    hide screen hermione_main
    #hide screen luna #Needs testing her events.
    #hide screen cho_chang #Needs testing her events.
    hide screen astoria_greengrass
    hide screen susan_bones
    hide screen nymphadora_tonks
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



label play_sound(sound=""):

    if sound == "knocking":
        $ renpy.play('sounds/knocking.mp3')

    if sound == "door":
        $ renpy.play('sounds/door.mp3')

    if sound == "owl":
        play sound "sounds/owl.mp3"  #Quiet...

    if sound == "glass_break" or sound == "glass":
        $ renpy.play('sounds/glass_break.mp3')

    if sound == "slap" or sound == "slapping":
        $ renpy.play('sounds/slap_02.mp3')

    if sound == "kiss" or sound == "kissing":
        $ renpy.play('sounds/kiss.mp3')
        
    if sound == "spell":
        $ renpy.play('sounds/magic2.mp3')
        
    if sound == "magic":
        $ renpy.play('sounds/magic4.mp3')
        
    return

label play_music(music=""): 

    if music == "dark_fog" or music == "snape_theme":
        play music "music/Dark Fog.mp3" fadein 1 fadeout 1 

    if music == "chipper_doodle" or music == "hermione_theme":
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 

    if music == "playful_tension" or music == "playful":
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 

    if music == "brittle_rille" or music == "day_theme":
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1

    if music == "manatees" or music == "night_theme":
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1

    if music == "hitman":
        play music "music/hitman.mp3" fadein 1 fadeout 1

    if music == "boss_theme":
        play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1

    if music == "sad" or music == "grape_soda":
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

