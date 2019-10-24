transform fade_in(x, y, speed):
    alpha 0
    xpos x
    ypos y
    linear speed alpha 1

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

transform move_in(x, speed):
    xpos x
    linear speed xpos 0
    pause speed

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
