default qp_mob = 0
default qp_mob_reaction = [None, None, None]
default qp_spotlight = False
default qp_hole = False
default qp_bludger_hit_commentator = False
default qp_rain = False
default qp_cloudy = False
default qp_fire = False
default qp_puddles = False

image qp_rain:
    zoom 0.5
    
    "images/rooms/quidditch_stands/rain/0.png"
    pause.09
    "images/rooms/quidditch_stands/rain/1.png"
    pause.09
    "images/rooms/quidditch_stands/rain/2.png"
    pause.09
    repeat
    
image qp_rain_surface:
    "images/rooms/quidditch_stands/rain/on_surface/0.png"
    pause.1
    "images/rooms/quidditch_stands/rain/on_surface/1.png"
    pause.1
    "images/rooms/quidditch_stands/rain/on_surface/2.png"
    pause.1
    repeat
    
image qp_rain_surface_overlay:
    "images/rooms/quidditch_stands/rain/on_surface/0o.png"
    pause.1
    "images/rooms/quidditch_stands/rain/on_surface/1o.png"
    pause.1
    "images/rooms/quidditch_stands/rain/on_surface/2o.png"
    pause.1
    repeat
    
image qp_fire:
    "images/rooms/quidditch_stands/fire/0.png"
    pause.5
    "images/rooms/quidditch_stands/fire/1.png"
    pause.5    
    repeat

screen quidditch_stands():
    tag quidditch_stands
    zorder 0
    sensitive False

    if qp_cloudy:
        add "images/rooms/quidditch_stands/bg_cloudy.png"
    else:
        add "images/rooms/quidditch_stands/bg.png"
        
    if qp_fire:
        add "qp_fire"
        
    if qp_mob != 0:
        add "images/rooms/quidditch_stands/mob_%s.png" % qp_mob
    if qp_puddles:
        add "images/rooms/quidditch_stands/puddles.png"
        
    add "images/rooms/quidditch_stands/hoops.png"
    add "images/rooms/quidditch_stands/tower.png"
    add "images/rooms/quidditch_stands/bench.png" # object
    add "images/rooms/quidditch_stands/podium_bottom.png"
    if qp_spotlight:
        add "images/rooms/quidditch_stands/spotlight.png"
        
    if qp_rain:
        add "qp_rain_surface"
    
screen quidditch_stands_overlay():
    tag quidditch_stands_overlay
    zorder 5
    sensitive False

    add "images/rooms/quidditch_stands/podium_top.png"
    if qp_spotlight:
        add "images/rooms/quidditch_stands/spotlight_front.png"
    add "images/rooms/quidditch_stands/tower_overlay.png"
    if qp_spotlight:
        add "images/rooms/quidditch_stands/fade.png"
    if qp_bludger_hit_commentator:
        add "smoke"
    if qp_hole:
        add "images/rooms/quidditch_stands/hole.png"
        
    if qp_rain:
        add "qp_rain"
        add "qp_rain_surface_overlay"
        add "#282b3026"
    add qp_mob_reaction[0] xpos 570 ypos 220
    add qp_mob_reaction[1] xpos 700 ypos 150
    add qp_mob_reaction[2] xpos 1000 ypos 150