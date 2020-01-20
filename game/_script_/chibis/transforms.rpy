
# Transforms used by the chibi class or chibi images

transform chibi_base(position, flip, scale):
    pos position
    anchor (0.0, 1.0)
    xzoom (-1 if flip else 1)
    zoom (0.5 * scale)

transform chibi_walk(start, end, speed):
    pos start
    linear speed pos end

transform chibi_fly:
    pos position
    block:
        yoffset absolute(0)
        ease 2 yoffset absolute(-10)
        ease 2 yoffset absolute(10)
        ease 2 yoffset absolute(0)
        repeat

transform chibi_fly_move(start, end, speed):
    parallel:
        pos start
        ease_quad speed pos end

    parallel:
        yoffset absolute(0)
        ease 2 yoffset absolute(-10)
        ease 2 yoffset absolute(10)
        ease 2 yoffset absolute(0)
        repeat

transform chibi_wand:
    xoffset -72 # Note: Offset seems to be applied after zoom

transform random_blink(close_image, open_image=Null()):
    close_image
    pause .08
    open_image
    choice:
        pause 6
    choice:
        pause 3
    choice:
        # Double blink
        close_image
        pause .08
        open_image
        pause 5
    repeat

transform emote_effect():
    alpha 0.0
    on show:
        zoom 0.8
        linear .2 zoom 1.0 alpha 1.0
    on hide:
        linear .2 zoom 1.2 alpha 0.0
