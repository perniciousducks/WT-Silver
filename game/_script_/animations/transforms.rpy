
transform move_in(x, t):
    xpos x
    linear t xpos 0
    pause t

transform move_fade:
    subpixel True
    on show, appear, start:
        alpha 0.0
        xoffset 200
        easein_back 1.0 alpha 1.0 xoffset absolute(0)

    on hide:
        alpha 1.0
        xoffset 0
        easeout_back 1.0 alpha 0.0 xoffset absolute(200)

transform fade_show(t):
    alpha 0
    on show:
        linear t alpha 1

transform fade_show_hide(t):
    alpha 0
    linear t alpha 1
    on hide:
        linear t alpha 0

transform fade_hide(t):
    on hide:
        linear t alpha 0.0

transform blink:
    on show:
        alpha 1.0
        pause 0.5
        alpha 0.0
        pause 0.5
        repeat
        
transform sprite_blink(img):
    choice:
        pause 4
    choice:
        pause 3
    choice:
        pause 2
    alpha 0.0
    img
    linear 0.13 alpha 1.0
    pause.05
    linear 0.13 alpha 0.0
    repeat

transform pulse:
    on show:
        xzoom 1.0
        yzoom 1.0
        linear 0.8 xzoom 1.2 yzoom 1.2
        linear 0.8 xzoom 1.0 yzoom 1.0
        repeat

transform move_to(start_x=0, start_y=0, target_x, target_y, duration=1.0):
    on show:
        xpos start_x
        ypos start_y
        linear duration xpos target_x ypos target_y

transform notify_transform:
    xalign .02 yalign .015

    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
