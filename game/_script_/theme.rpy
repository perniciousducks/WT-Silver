
################################################
##                  Styling                   ##
##       For information please refer to:     ##
##  https://www.renpy.org/doc/html/style.html ##
################################################

style quick_button:
    is default
    activate_sound "sounds/click3.mp3"
    background None
    xpadding 8
    ypadding 8

style quick_button_text:
    is default
    size 10
    idle_color "#8888"
    hover_color "#ccc"
    selected_idle_color "#cc08"
    selected_hover_color "#cc0"
    insensitive_color "#4448"

style yesno_button:
    size_group "yesno"

style yesno_label_text:
    text_align 0.5
    layout "subtitle"

style soundtest_button:
    xalign 1.0

style gm_nav_button:
    size_group "gm_nav"

style mm_button:
    size_group "mm"

# Common control styles
style default:
    font "fonts/CREABBB.TTF"
    size 16
    color "#402313"
    outline_scaling "linear"

style button:
    activate_sound "sounds/click3.mp3"
    background "#5d5151e6"
    hover_background "#897e75"
    insensitive_background "#463b3be6"
    selected_background "#766a6ae6"
    selected_hover_background "#897e75"
    #padding (5, 5, 5, 5)

style button_text:
    color "#9b8d84"
    hover_color "#fff"
    insensitive_color "#50443c"
    selected_color "#eedfd5"
    selected_hover_color "#fff"
    outlines [(1, "#00000080", 1, 0)]

style imagemap:
    activate_sound "sounds/click3.mp3"

style input:
    color "#5c321b"

# Dialogue styles
style say_window:
    background ConditionSwitch(
        "interface_style == 'night'", "interface/frames/gray/frame.png",
        "True", "interface/frames/gold/frame.png"
    )
    ysize 143
    padding (250, 40, 250, 0)
    top_margin 22
    yalign 1.0

style say_who_window is default:
    background ConditionSwitch(
        "interface_style == 'night'", Frame("interface/frames/gray/namebox.png", 6, 6),
        "True", Frame("interface/frames/gold/namebox.png", 6, 6)
    )
    xpadding 15
    pos (-15, -50)
    ysize 32
    xminimum 164
    text_align 0.5

style say_label:
    bold False
    text_align 0.5
    xalign 0.5
    yalign 0.5

# Day/night button styles
style day_button:
    background "#ac8d5ae6"
    hover_background "#97681f"
    insensitive_background "#d1a02eb3"
    padding (5, 5, 5, 5)

style night_button:
    background "#5d5151e6"
    hover_background "#897e75"
    insensitive_background "#9e8449"
    padding (5, 5, 5, 5)

style day_button_text is default: # Don't inherit from button_text
    color "#f9d592"
    outlines [(1, "#00000080", 1, 0)]
    hover_color "#fff"
    insensitive_color "#50443c"
    selected_color "#eedfd5"
    selected_hover_color "#fff"

style night_button_text is default: # Don't inherit from button_text
    color "#9b8d84"
    outlines [(1, "#00000080", 1, 0)]
    hover_color "#fff"
    insensitive_color "#50443c"
    selected_color "#eedfd5"
    selected_hover_color "#fff"

#TODO btn_hover day: (#edc48240|#e3ba7140) night: #7d75aa40

# Choice menu styles
style menu_text is default:
    text_align 0.5
    outlines [(1, "#00000080", 1, 0)]

style day_menu_text:
    color "#f9d592"
    hover_color "#fff"
    insensitive_color "#ae9566"

style night_menu_text:
    color "#9b8d84"
    hover_color "#fff"
    insensitive_color "#6c625c"

style menu_button is default:
    activate_sound "sounds/click3.mp3"

style day_menu_button:
    background "#ac8d5ae6"
    hover_background "#97681f"
    insensitive_background "#d1a02eB3"

style night_menu_button:
    background "#5d5151e6"
    hover_background "#897e75"
    insensitive_background "#9e8449"

style day_dropdown:
    ysize 24

style day_dropdown_text:
    yalign 0.5
    first_indent 26
    size 12
    color "#f9d592"
    hover_color "#FFF"
    insensitive_color "#ae9566"
    outlines [(1, "#00000080", 1, 0)]

style night_dropdown:
    ysize 24

style night_dropdown_text:
    yalign 0.5
    first_indent 26
    size 12
    color "#9b8d84"
    hover_color "#FFF"
    insensitive_color "#6c625c"
    outlines [(1, "#00000080", 1, 0)]

style tooltip_text is default:
    color "#fff"
    size 12
    outlines [(1, "#00000080", 1, 0)]

# Hyperlinks
style hyperlink_text:
    underline False
    hover_color "#4cf"
    idle_color "#08f"
