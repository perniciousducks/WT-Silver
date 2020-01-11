screen blkfade():
    tag blkfade
    zorder 6
    add "interface/blackfade.png"

screen whitefade():
    tag whitefade
    zorder 6
    add "interface/whitefade.png"

screen blktone():
    tag blktone
    zorder 4 # behind character sprites.
    add im.Alpha("interface/blackfade.png", 0.5)

screen blktone2():
    zorder 4
    add im.Alpha("interface/blackfade.png", 0.2)

screen blktone5(): #For narrator. (label nar) #Don't add tag blktone!
    zorder 5
    add im.Alpha("interface/blackfade.png", 0.5)

screen blktone8():
    zorder 4
    add im.Alpha("interface/blackfade.png", 0.8)

screen whitetone8():
    zorder 5
    add im.Alpha("interface/white.jpg", 0.8)

screen white():
    zorder 5
    add "interface/white.jpg"
    
screen blkback():
    zorder 1
    add "interface/blackfade.png"
    
screen bld1():
    tag bld1
    if not current_room == "quidditch_pitch":
        add "interface/bld.png"
    zorder 4

screen bld2():
    tag bld2
    add im.Flip("interface/bld.png", vertical=True)
    zorder 4