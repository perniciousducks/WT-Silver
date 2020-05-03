
screen quid_pitch_back():
    sensitive False
    zorder 0
    add "images/rooms/quidditch_pitch/back.png" zoom 0.5
    if weather == "cloudy":
        for i in xrange(random.randint(2, 5)):
            add "object" at OBJcloud
    add "images/rooms/quidditch_pitch/back_overlay.png" zoom 0.5

screen quid_pitch_mid():
    sensitive False
    zorder 2
    add "images/rooms/quidditch_pitch/mid.png" zoom 0.5

screen quid_pitch_front():
    sensitive False
    zorder 5
    add "images/rooms/quidditch_pitch/front.png" zoom 0.5
    for i in xrange(random.randint(1, 3)):
        add "object" at OBJbutterfly
