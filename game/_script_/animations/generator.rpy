image object:
    Null()
    
transform OBJbutterfly(hue=random.randint(0, 359)):
    subpixel True
    zoom random.uniform(0.4, 0.85)
    
    choice:
        pause random.randint(1, 7)
        parallel:
            xzoom -1
            pos (-100, random.randint(0, 500))
            ease_quad random.randint(14, 20) pos (1200, random.randint(0, 500))
            repeat
        parallel:
            ease_bounce 3 yoffset absolute(-20)
            ease_bounce 3 yoffset absolute(20)
            ease_bounce 3 yoffset absolute(0)
            repeat
        parallel:
            rotate 15
            ease_circ 1.0 rotate 30
            ease_circ 1.0 rotate 15
            repeat
        parallel:
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/0.png", im.matrix.hue(hue)) with d3
            pause .3
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/1.png", im.matrix.hue(hue)) with d3
            pause .3
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/2.png", im.matrix.hue(hue)) with d3
            pause .3
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/1.png", im.matrix.hue(hue)) with d3
            pause .3
            repeat
    choice:
        pause random.randint(1, 7)
        parallel:
            xzoom 1
            pos (1200, random.randint(0, 500))
            ease_quad random.randint(14, 20) pos (-100, random.randint(0, 500))
            repeat
        parallel:
            ease_bounce 3 yoffset absolute(-20)
            ease_bounce 3 yoffset absolute(20)
            ease_bounce 3 yoffset absolute(0)
            repeat
        parallel:
            rotate -15
            ease_circ 1.0 rotate -30
            ease_circ 1.0 rotate -15
            repeat
        parallel:
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/0.png", im.matrix.hue(hue)) with d3
            pause .3
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/1.png", im.matrix.hue(hue)) with d3
            pause .3
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/2.png", im.matrix.hue(hue)) with d3
            pause .3
            im.MatrixColor("images/rooms/quidditch_pitch/butterfly/1.png", im.matrix.hue(hue)) with d3
            pause .3
            repeat
    repeat
            
transform OBJcloud(start=(random.randint(270, 800), random.randint(60, 130)), speed=random.randint(60, 180)):
    parallel:
        zoom random.uniform(0.6, 1.0)
        pos start
        "images/rooms/_weather_/cloud_small.png"
        linear speed xpos 800
        xpos 270
        linear speed xpos start[0]
        repeat