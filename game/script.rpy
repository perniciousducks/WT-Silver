# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init python:
    config.after_load_callbacks.append(start_image_crop)

# The game starts here.
label start:
    $ init_variables()
    
    $ save_internal_version = config.version
    
    $ start_image_crop()
    #scene black
    jump start_wt

label after_load:
    $ init_variables()
    return


init:

    $ commentaries = False # In the GALLERY turns commentaries ON and OFF.
    
    ### Disposable flags ###
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    $ d_flag_04 = False
    $ d_flag_05 = False
    $ d_flag_06 = False
    $ d_flag_07 = False
    $ d_flag_08 = False
    $ d_flag_09 = False

    $ d_points = 0

    ### MENU PLACEMENT ###
    $ menu_x = 0.5
    $ menu_y = 0.5

    $ teleport = ImageDissolve("id_teleport.png", 1.0, 0)

    $ renpy.music.register_channel("bg_sounds", "sfx", True)
    $ renpy.music.register_channel("weather", "sfx", True)

    # Define some new transitions here.
    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    $ flashbulb2 = Fade(1, 0.5, 1, color='#fff')
    $ flashbb = Fade(0.2, 0.0, 0.8, color='#000')
    $ flashblood = Fade(0.2, 0.0, 0.8, color='#f02424')
    $ kissiris = Fade(0.2, 0.0, 0.8, color='#fb8dc8')

    #NVLE STUFF
    $ config.adv_nvl_transition = dissolve
    $ config.nvl_adv_transition = dissolve


    $ config.keymap['hide_windows'].remove('mouseup_2')
    $ config.keymap['hide_windows'].remove('h')
    #$ config.keymap['hide_windows'].remove('joy_hide')

#    init python:
#        def callback(event, **kwargs):
#            if event == "show":
#                renpy.music.play("beep5.mp3", loop="True", channel="sound")
#            elif event == "slow_done" or event == "end":
#                renpy.music.stop(channel="sound")

    # Define some new transitions here.
    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    $ flashbb = Fade(0.2, 0.0, 0.8, color='#000')
    $ flashblood = Fade(0.2, 0.0, 0.8, color='#f02424')
    $ kissiris = Fade(0.2, 0.0, 0.8, color='#fb8dc8')
    $ black_magic = Fade(0.2, 0.0, 0.5, color='#7f3590')
    $ blackfade = Fade(0.9, 0.5, 1, color='#000000')


    # MUSIC / SOUNDS
    $ galm = "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3"
    $ JafarsHour = "music/JafarsHour.mp3"
    $ mark = "music/Marketplace.mp3"
    $ palace = "music/EasternJourneybyPike270.mp3"
    $ mrm = "music/PartOfYourWorld.mp3"
    $ wnd = "music/TheEasternWindbyroensb.mp3"
    $ kiss = "music/TheKiss.mp3"
    $ sillyc = "music/SillyCatbyMaverlyn.mp3"
    $ xf = "music/TheXFiles.mp3"
    $ freedom = "music/outlawstarostfreedom.mp3"
    $ palace2 = "music/GoingtoKillMe.mp3"
    $ title = "music/RollIntheLeaves.mp3"
    $ swat = "music/025SWAT.mp3"
    $ hemanmusic = "music/HeMan.mp3"


###TRANSITIONS###########
define d1 = Dissolve(0.1)
define d2 = Dissolve(0.2)
define d3 = Dissolve(0.3)
define d4 = Dissolve(0.4)
define d5 = Dissolve(0.5)
define d6 = Dissolve(0.6)
define d7 = Dissolve(0.7)
define d8 = Dissolve(0.8)
define d9 = Dissolve(0.9)


# Music
define ms_arabian_nights = "music/Arabian_Nights.mp3"
define ms_bushwick = "music/Bushwick_Tarantella_Loop.mp3"
define ms_croft_manor = "music/Croft_Manor.mp3"
define ms_dice_game = "music/Dice_Game.mp3"
define ms_gtkm = "music/Going_to_Kill_Me.mp3"
define ms_gorilla = "music/Gorilla_Theme.mp3"
define ms_india = "music/India's_Different.mp3"
define ms_jafar = "music/Jafar's_Hour.mp3"
define ms_kabul = "music/Kabul_Flight_Jumpstart.mp3"
define ms_manatees = "music/Music for Manatees.mp3"
define ms_marketplace = "music/Marketplace.mp3"
define ms_outlaw_star = "music/Outlaw_Star_Freedom.mp3"
define ms_ozone = "music/Ozone.ogg"
define ms_sleep_walking = "music/Sleep_Walking.mp3"
define ms_tension = "music/Tension.mp3"
define ms_the_calm_before = "music/The_Calm_Before.mp3"
define ms_the_eastern_wind = "music/The_Eastern_Wind.mp3"
define ms_the_kiss = "music/The_Kiss.mp3"
define ms_the_xfiles = "music/The_X-Files.mp3"
define ms_vision = "music/Vision.mp3"

# Sounds
define sd_boing1 = "sounds/boing.mp3"
define sd_boing2 = "sounds/boing02.mp3"
define sd_boing3 = "sounds/boing03.mp3"
define sd_burp = "sounds/burp.mp3"
define sd_door = "sounds/door.mp3"
define sd_door2 = "sounds/door2.mp3"
define sd_door3 = "sounds/door3.mp3"
define sd_fall = "sounds/fall.wav"
define sd_glitch = "sounds/gltch.mp3"
define sd_iris_run = "sounds/iris_run.mp3"
define sd_kungfupunch = "sounds/kung-fu-punch.mp3"
define sd_magic4 = "sounds/magic4.ogg"
define sd_monster = "sounds/mon.wav"
define sd_monster_dead = "sounds/mondead.wav"
define sd_pistol2 = "sounds/pistol2.mp3"
define sd_pop1 = "sounds/pop01.mp3"
define sd_pop2 = "sounds/pop02.mp3"
define sd_pop3 = "sounds/pop03.mp3"
define sd_punch1 = "sounds/punch01.mp3"
define sd_punch2 = "sounds/punch02.mp3"
define sd_rustling = "sounds/rustling.mp3"
define sd_scratch = "sounds/scratch.wav"
define sd_slap = "sounds/slap.mp3"
define sd_spit = "sounds/spit.mp3"
define sd_win2 = "sounds/win2.mp3"


## ANIMATIONS
        ### INTRO MOVIE ANIMATIONS ###
image title_ani: #Main title animation.
    contains:
        "title/00.png"
        pause 3
        "title/01.png"
        pause.1
        "title/02.png"
        pause.1
        "title/01.png"
        pause.1
        "title/00.png"
        pause 6
        "title/01.png"
        pause.1
        "title/02b.png"
        pause.1
        "title/01b.png"
        pause.1
        "title/00b.png"
        pause 3
        "title/01b.png"
        pause.1
        "title/02b.png"
        pause.1
        "title/01b.png"
        pause.1
        "title/00b.png"
        pause 6
        "title/01b.png"
        pause.1
        "title/02b.png"
        pause.1
        "title/02.png"
        pause.1
        "title/01.png"
        pause.1
        repeat
        
    contains:
        xpos -17
        ypos -151
        zoom 2.0
        "candle_fire_01"
        
    contains:
        xpos -255
        ypos 100
        zoom 0.8
        "title/fire00.png"
        pause.1
        "title/fire01.png"
        pause.1
        "title/fire02.png"
        pause.1
        "title/fire03.png"
        pause.1
        "title/fire04.png"
        pause.1
        "title/fire05.png"
        pause.1
        "title/fire06.png"
        pause.1
        "title/fire07.png"
        pause.1
        repeat
        
    #sparkle
    contains:
        subpixel True
        xpos 798
        ypos 200
        xanchor 0.5
        yanchor 0.5
        zoom 0.0
        "title/sparkle.png"
        linear 0.8 zoom 1.0
        linear 0.5 zoom 0.0
        pause 5
        repeat
        
    #shine silver (synchronized)
    contains:
        subpixel True
        xpos 848
        ypos 230
        xanchor 0.5
        yanchor 0.5
        zoom 0.0
        "title/sparkle.png"
        pause 1.3
        linear 0.5 zoom 1.0
        linear 0.5 zoom 0.0
        
        xpos 870
        ypos 205
        linear 0.5 zoom 1.0
        linear 0.5 zoom 0.0
        
        xpos 914
        ypos 227
        linear 0.5 zoom 1.0
        linear 0.5 zoom 0.0
        
        xpos 948
        ypos 233
        linear 0.5 zoom 1.0
        linear 0.5 zoom 0.0
        
        xpos 999
        ypos 226
        linear 0.5 zoom 1.0
        linear 0.5 zoom 0.0
        pause 12.6
        repeat
        
        
        
image menu_ani:
    contains:
        "title/00b.png"
        
    contains:
        alpha 0.8
        "images/rooms/_bg_/color/black.png"

#############################################

image heal:
    "magic/heal01.png"
    pause.06
    "magic/heal02.png"
    pause.06
    "magic/heal03.png"
    pause.06
    "magic/heal04.png"
    pause.06
    "magic/heal05.png"
    pause.06
    "magic/heal06.png"
    pause.06
    "magic/heal07.png"
    pause.06
    "magic/heal08.png"
    pause.06
    "magic/heal09.png"
    pause.06
    "magic/heal10.png"
    pause.06
    "magic/heal11.png"
    pause.06
    "magic/heal12.png"
    pause.06
    "magic/heal13.png"
    pause.06
    "magic/heal14.png"
    pause.06
    "magic/heal15.png"
    pause.06
    "magic/heal16.png"
    pause.06
    "magic/heal17.png"
    pause.06
    "magic/heal18.png"
    pause.06
    
image love_heart:
    "magic/love09.png"
    pause.06
    "magic/love10.png"
    pause.06
    "magic/love11.png"
    pause.06
    "magic/love12.png"
    pause.06
    "magic/love13.png"
    pause.06
    "magic/love14.png"
    pause.06
    "magic/love15.png"

############################################
#######EMOTIONS #^_^# ########################
############################################

image emo01:
    "characters/emotes/animated/ex01.png"
    pause.5
    "characters/emotes/animated/ex02.png"
    pause.5
    "characters/emotes/animated/ex03.png"
    pause.5
    "characters/emotes/animated/ex04.png"
    pause 1
    "characters/emotes/animated/ex01.png"
    pause.5
    "characters/emotes/animated/ex00.png"
    repeat

image emo02:
    "characters/emotes/animated/exl01.png"
    pause.5
    "characters/emotes/animated/exl02.png"
    pause.5
    "characters/emotes/animated/exl03.png"
    pause.5
    "characters/emotes/animated/exl04.png"
    pause.5
    "characters/emotes/animated/exl05.png"
    pause.5
    "characters/emotes/animated/exl06.png"
    repeat
    
image emo03:
    "characters/emotes/animated/sad_01.png"
    pause.4
    "characters/emotes/animated/sad_02.png"
    pause.4
    "characters/emotes/animated/sad_03.png"
    pause.4
    "characters/emotes/animated/sad_04.png"
    pause.4
    "characters/emotes/animated/sad_03.png"
    pause.4
    "characters/emotes/animated/sad_02.png"
    pause.4
    repeat
    
image emo04:
    "characters/emotes/animated/hoot_01.png"
    pause.4
    "characters/emotes/animated/hoot_02.png"
    pause.4
    "characters/emotes/animated/hoot_03.png"
    pause.4
    "characters/emotes/animated/hoot_04.png"
    pause.4
    "characters/emotes/animated/hoot_05.png"
    pause.4
    "characters/emotes/animated/hoot_06.png"
    pause.4
    "characters/emotes/animated/hoot_07.png"
    pause.4
    repeat

image emoq:
    "characters/emotes/animated/q1.png"
    pause.5
    "characters/emotes/animated/q2.png"
    pause.5
    "characters/emotes/animated/q3.png"
    pause.5
    "characters/emotes/animated/q4.png"
    pause.5
    "characters/emotes/animated/q1.png"
    pause.5
    "characters/emotes/animated/q2.png"
    pause.5
    "characters/emotes/animated/q3.png"
    pause.5
    "characters/emotes/animated/q4.png"
    repeat

image emom:
    "characters/emotes/animated/emo00.png"
    pause.08
    "characters/emotes/animated/emo01.png"

image excl:
    "characters/emotes/animated/excl01.png"
    pause.5
    "characters/emotes/animated/excl02.png"
    pause.5
    "characters/emotes/animated/excl03.png"
    pause.5
    "characters/emotes/animated/excl04.png"
    pause.5
    repeat
image qu:
    "characters/emotes/animated/que1.png"
    pause.5
    "characters/emotes/animated/que2.png"
    pause.5
    "characters/emotes/animated/que3.png"
    pause.5
    "characters/emotes/animated/que4.png"
    pause.5
    "characters/emotes/animated/que5.png"
    pause.5
    "characters/emotes/animated/que6.png"
    repeat

image an:
    "characters/emotes/animated/an1.png"
    pause.2
    "characters/emotes/animated/an2.png"
    pause.2
    "characters/emotes/animated/an3.png"
    pause.2
    "characters/emotes/animated/an2.png"
    pause.2
    repeat

image sal:
    "characters/emotes/animated/s1.png"
    pause.08
    "characters/emotes/animated/s2.png"
    pause.2
    "characters/emotes/animated/s3.png"
    pause.08
    "characters/emotes/animated/s4.png"
    pause.2
    "characters/emotes/animated/s5.png"
    pause.08
    "characters/emotes/animated/s6.png"
    pause 1
    "characters/emotes/animated/00.png"
    pause.08
    repeat

image th:
    "characters/emotes/animated/t1.png"
    pause.2
    "characters/emotes/animated/t2.png"
    pause.2
    "characters/emotes/animated/t3.png"
    pause.2
    "characters/emotes/animated/t4.png"
    pause.2
    repeat

image emo7:
    "characters/emotes/animated/emotion00.png"
    pause.5
    "characters/emotes/animated/emotion01.png"
    pause.5
    "characters/emotes/animated/emotion00.png"
    pause.7
    "characters/emotes/animated/emotion01.png"
    pause.7
    "characters/emotes/animated/emotion00.png"
    pause.6
    "characters/emotes/animated/emotion01.png"
    pause.6
    repeat

image emo8:
    "characters/emotes/animated/emotion00.png"
    pause.7
    "characters/emotes/animated/emotion03.png"
    pause.7
    "characters/emotes/animated/emotion00.png"
    pause.6
    "characters/emotes/animated/emotion03.png"
    pause.6
    "characters/emotes/animated/emotion00.png"
    pause.5
    "characters/emotes/animated/emotion03.png"
    pause.5
    repeat

image sur:
    "characters/emotes/animated/sur1.png"
    pause.5
    "characters/emotes/animated/sur2.png"
    pause.5
    "characters/emotes/animated/sur3.png"
    pause.5
    "characters/emotes/animated/sur4.png"
    pause.5
    "characters/emotes/animated/sur5.png"
    pause.5
    "characters/emotes/animated/sur6.png"
    pause.5
    repeat

######
image magic = "magic/magic1.png"
image magic2 = "magic/magic2.png"
image magic3 = "magic/magic3.png"
image magic4 = "magic/magic4.png"
image magic5 = "magic/magic5.png"

image bld = "interface/bld.png"
image bld2 = "interface/bld2.png"
image white = "interface/white.jpg"
image white = "interface/white.jpg"
image blkfade = "interface/blackfade.png"
image blkfade = "interface/blackfade.png"
image whitefade = "interface/whitefade.png"
image whitefade = "interface/whitefade.png"
image con1 = "interface/cont1.png"
image blk50 = im.Alpha("interface/blackfade.png", 0.5)
image blk50 = im.Alpha("interface/blackfade.png", 0.5)

image ctc3 = Animation("interface/ctc00.png", 0.2, "interface/ctc01.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc03.png", 0.2, "interface/ctc04.png", 0.5, "interface/ctc03.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc01.png", 0.2, xpos=0.995, ypos=0.995, xanchor=1.0, yanchor=1.0)
image ctc4 = Animation("interface/ctc00.png", 0.2, "interface/ctc01.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc03.png", 0.2, "interface/ctc04.png", 0.5, "interface/ctc03.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc01.png", 0.2, xpos=0.99, ypos=0.995, xanchor=0.8, yanchor=1.0)
image ctc7 = Animation("interface/ctc00.png", 0.2, "interface/ctc01.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc03.png", 0.2, "interface/ctc04.png", 0.5, "interface/ctc03.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc01.png", 0.2)

## TRANSFORMATION

transform moveFade:
    subpixel True
    
    on show, appear, start:
        alpha 0.0
        xoffset 200
        easein_back 1.0 alpha 1.0 xoffset absolute(0)
    
    on hide:
        alpha 1.0
        xoffset 0
        easeout_back 1.0 alpha 0.0 xoffset absolute(200)

transform basicfade:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 1.5 alpha 0.0

transform basicfade2:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 1.2 alpha 0.0

transform basicfade3:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 0.8 alpha 0.0

transform basicfade4:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 1.2 alpha 0.0
            
transform fadeInOut:
    alpha 0.0
    linear 0.15 alpha 1.0
    on hide:
        linear 0.15 alpha 0.0
        
transform fadeOutOnly:
    on hide:
        linear 0.15 alpha 0.0
        
transform blink:
    on show:
        alpha 1.0
        pause 0.5
        alpha 0.0
        pause 0.5
        repeat
        
transform pulse:
    on show:
        xzoom 1.0
        yzoom 1.0
        linear 0.8 xzoom 1.2 yzoom 1.2
        linear 0.8 xzoom 1.0 yzoom 1.0
        repeat
        
transform moveto(start_x=0, start_y=0, target_x, target_y, duration=1.0):
    on show:
        xpos start_x
        ypos start_y
        linear duration xpos target_x ypos target_y