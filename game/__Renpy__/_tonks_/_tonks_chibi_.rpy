

screen with_tonks_animated():
    tag tonks_chibi
    add "genie_toast_goblet" at Position(xpos=435, ypos=200)
    add "snape_toast_goblet" at Position(xpos=618, ypos=200) # TODO: Add correct Chibi images.

    zorder 3

screen tonks_chibi_large(xx=nxpos, yy=nypos):
    tag tonks_chibi
    add "characters/tonks/chibis/nt_walk_large.png" xpos xx ypos yy zoom (1.0/scaleratio)
    zorder 3
