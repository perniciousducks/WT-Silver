transform popup_animation:
    subpixel True
    on show, appear, start:
        xoffset -200
        linear 0.5 xoffset absolute(0)
        pause 3.0
        linear 0.5 xoffset absolute(-200)

screen popup_window(string="", xpos=0, ypos=60):
    tag popup_window
    zorder 100
    
    frame:
        at popup_animation
        if daytime and not persistent.nightmode:
            style "say_who_window_day"
        else:
            style "say_who_window_night"
        pos (xpos, ypos)
        
        text string align (0.5, 0.5) size 12
    timer 4.0 action Hide("popup_window")