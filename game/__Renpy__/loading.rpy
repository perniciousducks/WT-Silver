transform rotateAnim:
    subpixel True
    rotate None
    linear 3.0 rotate absolute(359.0)
    repeat
    
screen loading_screen:
    tag loading
    zorder 100

    add "interface/loading.png" ypos 48 xpos 1032 xanchor 0.5 yanchor 0.5 zoom 0.5 at rotateAnim