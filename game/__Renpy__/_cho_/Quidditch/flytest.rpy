transform flytest_anim0:
    subpixel True
    
    on show, appear, start:
        parallel:
            xoffset -600
            easeout_quad 3.0 xoffset absolute(0)
            easein_quad 3.0 xoffset absolute(600)
            repeat
        parallel:
            zoom 0.01
            easeout_quad 3.0 zoom 0.5
            easein_quad 3.0 zoom 0.01
            repeat
        parallel:
            rotate 4
            linear 3.0 rotate -4
            linear 3.0 rotate 4
            repeat

transform flytest_anim1:
    subpixel True
    
    on show, appear, start:
        parallel:
            xoffset -600
            linear 1.5 xoffset absolute(-300)
            linear 1.5 xoffset absolute(0)
            linear 1.5 xoffset absolute(300)
            linear 1.5 xoffset absolute(600)
            repeat
        parallel:
            zoom 0.01
            easeout_quad 1.5 zoom 0.5
            linear 1.5 zoom 0.10
            easeout_quad 1.5 zoom 0.5
            linear 1.5 zoom 0.01
            repeat
            
transform flytest_anim2:
    subpixel True
    
    on show, appear, start:
        parallel:
            xoffset -600
            zoom 0.25
            easeout_quad 3.0 xoffset absolute(0)
            easein_quad 3.0 xoffset absolute(600)
            repeat
        parallel:
            yoffset 50
            ease_cubic 2.0 yoffset absolute(-50)
            ease_cubic 2.0 yoffset absolute(50)
            repeat
        parallel:
            rotate 2
            linear 1.0 rotate -2
            linear 1.0 rotate 2
            repeat
            
transform flytest_anim3:
    subpixel True
    
    on show, appear, start:
        parallel:
            zoom 0.05
            xoffset -600
            easeout_quad 3.0 xoffset absolute(0)
            easein_quad 2.0 xoffset absolute(70)
            pause(1.0)
            repeat
        parallel:
            yoffset -200
            pause(0.5)
            easeout_quint 2.5 yoffset absolute(200) zoom 0.25
            pause(3.0)
            repeat
        parallel:
            rotate 0
            easeout_quint 2.5 rotate 80
            easeout_quint 0.5 rotate 15
            pause(1.0)
            easeout_expo 0.5 rotate 0
            pause(1.5)
            repeat
            
transform flytest_anim4:
    subpixel True
    
    on show, appear, start:
        zoom 0.25
        around (config.screen_width/2, config.screen_height/2)
        anchor (0.5, 0.5)
        angle 0
        radius 200
        rotate 0
        linear 3.0 radius 200 clockwise circles 1 rotate 360
        repeat
            
transform flytest_anim5:
    subpixel True
    
    on show, appear, start:
        parallel:
            zoom 0.25
            around (config.screen_width/2, config.screen_height/2)
            anchor (0.5, 0.5)
            angle 0
            radius 200
            rotate 0
            linear 3.0 radius 200 clockwise circles 1 rotate 360
            repeat
        parallel:
            xoffset -300
            linear 1.5 xoffset absolute(300)
            linear 1.5 xoffset absolute(-300)
            repeat
            
transform flytest_anim6:
    subpixel True
    
    on show, appear, start:
        parallel:
            zoom 0.25
            xoffset -600
            around (config.screen_width/2, config.screen_height/2)
            anchor (0.5, 0.5)
            angle 0
            radius 200
            #rotate 0
            easeout_quad 1.5 xoffset absolute(0)
            linear 1.5 radius 200 clockwise circles 1 rotate 360
            rotate 0
            easein_quad 2.0 xoffset absolute(600)
            repeat
        parallel:
            rotate 0
            linear 1.5 rotate 10 yoffset absolute(30)
            pause 1.5
            linear 2.0 rotate -15 yoffset absolute(0)
            repeat

transform flytest_anim7:
    subpixel True
    
    on show, appear, start:
        zoom 0.25
        yoffset 0
        easein_back 0.5 yoffset absolute(-100) rotate -15
        easein_back 0.5 yoffset absolute(0) rotate 0
        easein_back 0.5 yoffset absolute(100) rotate 15
        easein_back 0.5 yoffset absolute(0) rotate 0
        repeat
            
transform flytest_anim8:
    subpixel True
    
    on show, appear, start:
        zoom 0.01
        xoffset -600
        yoffset -300
        rotate 45
        easeout_quad 3.0 zoom 0.25 xoffset absolute(-50) yoffset absolute(100) rotate 10
        easein_back 1.0 xoffset absolute(0) yoffset absolute(120) rotate 0
        ease_back 2.5 yoffset absolute(90)
        ease_back 2.5 yoffset absolute(110)
        ease_back 2.5 yoffset absolute(90)
        ease_back 2.5 yoffset absolute(110)
        ease_back 2.5 yoffset absolute(90)
        ease_back 2.5 yoffset absolute(110)
        #pause(3.0)
        repeat
            
transform flytest_anim9:
    subpixel True
    
    on show, appear, start:
        zoom 0.25
        yoffset absolute(110)
        ease_back 2.5 yoffset absolute(90)
        ease_back 2.5 yoffset absolute(110)
        repeat
            
transform flytest_anim10:
    subpixel True
    
    on show, appear, start:
        zoom 0.25
        xzoom 1.0
        around (config.screen_width/2, -400)
        anchor (0.5, 0.5)
        angle 0
        radius 700
        rotate 0
        linear 4.0 radius 700 clockwise circles 1 rotate 360
        xzoom -1.0
        linear 4.0 radius 700 counterclockwise circles 1 rotate 0
        repeat
            
transform flytest_anim11:
    subpixel True
    
    on show, appear, start:
        parallel:
            xoffset -700
            zoom 0.25
            xzoom 1.0
            easeout_quad 3.0 xoffset absolute(700)
            pause(1.0)
            xzoom -1.0
            easeout_quad 3.0 xoffset absolute(-700)
            repeat
        parallel:
            yoffset 70
            ease_back 3.0 yoffset absolute(-70)
            ease_back 3.0 yoffset absolute(70)
            repeat
        parallel:
            rotate 10
            linear 2.0 rotate -10
            linear 2.0 rotate 10
            repeat

label flytest_cho:
    show screen flytest
    pause
    
    hide screen flytest
    jump day_main_menu
    
screen flytest:
    tag flytest
    zorder 100
    
    add "images/rooms/quidditch_pitch/day.png"
    
    vbox:
        textbutton "inc +" xsize 200 ysize 40 action SetVariable("anim_number", clamp(anim_number+1, 0, 11))
        textbutton "dec -" xsize 200 ysize 40 action SetVariable("anim_number", clamp(anim_number-1, 0, 11))
        text "Animation [anim_number]"
    
    if anim_number == 0:
        add "images/flytest.png" align (0.5, 0.5) at flytest_anim0
    elif anim_number == 1:
        add "images/flytest.png" align (0.5, 0.5) at flytest_anim1
    elif anim_number == 2:
        add "images/flytest.png" align (0.5, 0.5) at flytest_anim2
    elif anim_number == 3:
        add "images/flytest.png" align (0.5, 0.5) at flytest_anim3
    elif anim_number == 4:
        add "images/flytest.png" align (0.5, 0.5) at flytest_anim4
    elif anim_number == 5:
        add "images/flytest.png" align (0.5, 0.5) at flytest_anim5
    elif anim_number == 6:
        add "images/flytest.png" align (0.5, 0.5) at flytest_anim6
    elif anim_number == 7:
        add "images/flytest.png" align (0.5, 0.5) at flytest_anim7
    elif anim_number == 8:
        add "images/flytest.png" align (0.5, 0.5) at flytest_anim8
    elif anim_number == 9:
        add "images/flytest.png" align (0.5, 0.5) at flytest_anim9
    elif anim_number == 10:
        add "images/flytest.png" align (0.5, 0.5) at flytest_anim10
    elif anim_number == 11:
        add "images/flytest.png" align (0.5, 0.5) at flytest_anim11