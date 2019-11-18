# Main script file
init python:
    config.after_load_callbacks.append(start_image_crop)

    renpy.music.register_channel("bg_sounds", "sfx", True)
    renpy.music.register_channel("weather", "sfx", True)

# The game starts here
label start:
    call temporary_post_default_init

    $ save_internal_version = config.version
    $ achievement_fix()

    $ restart_achievements_thread()

    $ start_image_crop()
    #scene black
    jump start_wt

label after_load:
    call temporary_post_default_init
    return

#TODO Remove the necessity for post-default-init calls by fixing code
label temporary_post_default_init:
    call default_hermione_class_init
    call default_cho_class_init
    call default_astoria_class_init
    call default_tonks_class_init

# Turns commentaries on/off in gallery
default commentaries = False

default txt_style = "night_text"
default btn_style = "night_button"
default btn_hover = "#7d75aa40"
default mnu_style = "menu_choice_night"
default mnu_btn_style = "menu_choice_nightbutton"

# Menu placement
default menu_x = 0.5
default menu_y = 0.5

# Transitions
define d1 = Dissolve(0.1)
define d2 = Dissolve(0.2)
define d3 = Dissolve(0.3)
define d4 = Dissolve(0.4)
define d5 = Dissolve(0.5)
define d6 = Dissolve(0.6)
define d7 = Dissolve(0.7)
define d8 = Dissolve(0.8)
define d9 = Dissolve(0.9)

define teleport = ImageDissolve("id_teleport.png", 1.0, 0)

define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
define flashbb = Fade(0.2, 0.0, 0.8, color='#000')
define flashblood = Fade(0.2, 0.0, 0.8, color='#f02424')
define kissiris = Fade(0.2, 0.0, 0.8, color='#fb8dc8')
define black_magic = Fade(0.2, 0.0, 0.5, color='#7f3590')
define blackfade = Fade(0.9, 0.5, 1, color='#000000')

# Main title background animation
image title_ani: 
    contains:
        zoom 0.5
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
        xanchor 1.0
        xalign 1.0
        zoom 0.9
        ypos 12
        xoffset -2
        "logo/title.png"

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

# Other game menu background
image menu_ani:
    contains:
        zoom 0.5
        "title/00b.png"

    contains:
        alpha 0.8
        "images/rooms/_bg_/color/black.png"
