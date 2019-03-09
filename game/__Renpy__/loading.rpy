transform rotateAnim:
    subpixel True
    rotate None
    linear 3.0 rotate absolute(359.0)
    repeat
    
screen loading_screen:
    tag loading
    zorder 100
    
    default currently_loading = ""
    
    button xsize 1080 ysize 600 action NullAction() style "empty"
    
    add "interface/loading_0.jpg" zoom 0.5
    add "interface/loading.png" ypos 48 xpos 1032 xanchor 0.5 yanchor 0.5 zoom 0.5 at rotateAnim
    text "{color=#FFF}[threads_task_count]{/color}" xalign 0.53 yanchor 0.5 ypos 560