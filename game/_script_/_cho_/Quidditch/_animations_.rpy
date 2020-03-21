screen hufflepuff_match_cho_chase(zoom1=0.5, zoom2=0.5):
    zorder 16
    tag cg
    add "images/rooms/quidditch_stands/sky.png"
    add "snitch" at snitch_chased(zoom1, zoom2)
    add "images/rooms/quidditch_stands/cho_chase/cho_chase.png" at sprite_zoom_fly(zoom1, zoom2)
    if cho.is_worn("panties"):
        add "images/rooms/quidditch_stands/cho_chase/cho_chase_panties.png" at sprite_zoom_fly(zoom1, zoom2)
    #TODO Check and wear goggles

image snitch:
    "images/rooms/quidditch_stands/cho_chase/snitch0.png"
    pause.01
    "images/rooms/quidditch_stands/cho_chase/snitch1.png"
    pause.01
    "images/rooms/quidditch_stands/cho_chase/snitch2.png"
    pause.01
    "images/rooms/quidditch_stands/cho_chase/snitch1.png"
    pause.01
    repeat

transform sprite_fly_idle:
    subpixel True

    on show, appear, start:
        yoffset absolute(110)
        ease_back 2.5 yoffset absolute(90)
        ease_back 2.5 yoffset absolute(110)
        repeat

transform sprite_zoom_fly(start, value):
    subpixel True

    on show, appear, start:
        parallel:
            zoom start
            linear 1.0 zoom value

        parallel:
            yoffset absolute(110)
            ease_back 1.5 yoffset absolute(90) zoom value+0.01
            ease_back 1.5 yoffset absolute(110) zoom value-0.01
            repeat

        parallel:
            xoffset absolute(110)
            ease_back 2.5 xoffset absolute(90)
            ease_back 2.5 xoffset absolute(110)
            repeat

transform snitch_chased(start, value):
    subpixel True

    on show, appear, start:
        parallel:
            zoom start
            linear 1.0 zoom value

        parallel:
            yoffset absolute(100)
            ease_back 0.5 yoffset absolute(-60) zoom value+0.25
            ease_back 0.5 yoffset absolute(100) zoom value-0.2
            repeat

        parallel:
            xoffset absolute(0)
            easein_quint 0.7 xoffset absolute(120)
            easein_quint 0.75 xoffset absolute(0)
            repeat
