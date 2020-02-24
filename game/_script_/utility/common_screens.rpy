screen blkfade():
    tag blkfade
    zorder 20
    add Color("#000")

screen whitefade():
    tag whitefade
    zorder 20
    add Color("#fff")

screen blktone(alpha=0.5):
    tag blktone
    zorder 10
    add Color("#000", alpha=alpha)

screen blktone5(): #For narrator. (label nar) #Don't add tag blktone!
    zorder 20
    add Color("#000", alpha=0.5)

screen white():
    zorder 20
    add Color("#fff")
    
screen bld1():
    zorder 10
    if not current_room == "quidditch_stands":
        add "interface/bld.png"

screen bld2():
    zorder 10
    add im.Flip("interface/bld.png", vertical=True)

screen notes():
    add "notes" xpos 320+140 ypos 330
    zorder 1

screen gift(win=False):
    zorder 30
    if win:
        use notes
        on "show" action Play("sound", "sounds/win2.mp3")
    add the_gift align (0.5, 0.4) zoom get_zoom(the_gift, 320,320)

screen clothing_unlock():
    zorder 30
    add "interface/panels/"+str(interface_color)+"/clothing_panel.png" at Position(xalign=0.5, ypos=100)
    add mannequin_preview xalign 0.47 ypos 52 zoom 0.6/scaleratio
