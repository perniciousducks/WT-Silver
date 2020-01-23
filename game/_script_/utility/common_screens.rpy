screen blkfade():
    tag blkfade
    zorder 20
    add Color("#000")

screen whitefade():
    tag whitefade
    zorder 20
    add Color("#fff")

screen blktone():
    tag blktone
    zorder 10
    add Color("#000", alpha=0.5)

screen blktone2():
    zorder 10
    add Color("#000", alpha=0.2)

screen blktone5(): #For narrator. (label nar) #Don't add tag blktone!
    zorder 20
    add Color("#000", alpha=0.5)

screen blktone8():
    zorder 10
    add Color("#000", alpha=0.8)

screen whitetone8():
    zorder 20
    add Color("#fff", alpha=0.8)

screen white():
    zorder 20
    add Color("#fff")
    
screen blkback():
    zorder 1
    add Color("#000")
    
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
    zorder 20
    if win:
        use notes
        on "show" action Play("sound", "sounds/win2.mp3")
    # add "interface/frames/"+str(interface_color)+"/reward_background.png" xalign 0.5 yalign 0.547
    add the_gift align (0.5, 0.4) zoom get_zoom(the_gift, 320,320)

screen clothing_unlock():
    zorder 20
    add "interface/panels/"+str(interface_color)+"/clothing_panel_B.png" at Position(xalign=0.5, ypos=100)
    add mannequin_preview xalign 0.47 ypos 52 zoom 0.6/scaleratio
