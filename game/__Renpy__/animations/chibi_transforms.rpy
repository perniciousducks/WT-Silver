transform chibi_base(position, flip):
    pos position
    # anchor (0.5, 1.0)
    xzoom (-1 if flip else 1)
    zoom (1.0/scaleratio)

transform chibi_walk(start, end, flip, speed):
    pos start
    # anchor (0.5, 1.0)
    xzoom (-1 if flip else 1)
    zoom (1.0/scaleratio)
    linear speed pos end

transform chibi_fly(position, flip):
    pos position
    # anchor (0.5, 1.0)
    xzoom (-1 if flip else 1)
    zoom (1.0/scaleratio)
    block:
        yoffset absolute(0)
        ease 2 yoffset absolute(-10)
        ease 2 yoffset absolute(10)
        ease 2 yoffset absolute(0)
        repeat

transform chibi_fly_move(start, end, flip, speed):
    # anchor (0.5, 1.0)
    xzoom (-1 if flip else 1)
    zoom (1.0/scaleratio)
    parallel:
        pos start
        ease_quad speed pos end

    parallel:
        yoffset absolute(0)
        ease 2 yoffset absolute(-10)
        ease 2 yoffset absolute(10)
        ease 2 yoffset absolute(0)
        repeat

transform chibi_wand(position, flip):
    pos position
    xoffset -72 # Note: Offset seems to be applied after zoom
    xzoom (-1 if flip else 1)
    zoom (1.0/scaleratio)

# Old chibi transforms

transform gen_walk_trans(x, x2, y, y2):
    xpos x
    ypos y
    linear gen_speed xpos x2 ypos y2 # linear

transform sna_walk_trans(x, x2, y, y2):
    xpos x
    ypos y
    linear sna_speed xpos x2 ypos y2 # linear

transform her_walk_trans(x, x2, y, y2):
    xpos x
    ypos y
    linear her_speed xpos x2 ypos y2 # linear
