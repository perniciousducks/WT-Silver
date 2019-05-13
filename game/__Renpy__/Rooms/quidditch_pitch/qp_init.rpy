init:
    default qp_mob = 0
    $ qp_mob_reaction = [None, None, None]
    $ qp_spotlight = False

screen quidditch_pitch():
    tag quidditch_pitch
    zorder 0
    add "images/rooms/quidditch_pitch/bg.png"
    if qp_mob != 0:
        add "images/rooms/quidditch_pitch/mob_%s.png" % qp_mob
    add "images/rooms/quidditch_pitch/hoops.png"
    add "images/rooms/quidditch_pitch/tower.png"
    add "images/rooms/quidditch_pitch/bench.png" # object
    add "images/rooms/quidditch_pitch/podium_bottom.png"
    if qp_spotlight:
        add "images/rooms/quidditch_pitch/spotlight.png"
    
screen quidditch_pitch_overlay():
    tag quidditch_pitch_overlay
    zorder 5
    add "images/rooms/quidditch_pitch/podium_top.png"
    if qp_spotlight:
        add "images/rooms/quidditch_pitch/spotlight_front.png"
    add "images/rooms/quidditch_pitch/tower_overlay.png"
    if qp_spotlight:
        add "images/rooms/quidditch_pitch/fade.png"
    add qp_mob_reaction[0] xpos 570 ypos 220
    add qp_mob_reaction[1] xpos 700 ypos 150
    add qp_mob_reaction[2] xpos 1000 ypos 150