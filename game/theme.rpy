init python hide:
    theme.threeD(
        ## Theme: 3D
        ## Color scheme: Muted Horror

        ## The color of an idle widget face.
        widget = "#5d5151",

        ## The color of a focused widget face.
        widget_hover = "#897e75",

        ## The color of the text in a widget.
        widget_text = "#9b8d84",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#FFFFFF",

        ## The color of a disabled widget face.
        disabled = "#463b3b",

        ## The color of disabled widget text.
        disabled_text = "#50443c",

        ## The color of informational labels.
        label = "#9b8d84",

        ## The color of a frame containing widgets.
        frame = "#5d5151",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "title_ani",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "menu_ani",


        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
    )

# Common control styles
style default:
    font "fonts/CREABBB.TTF"
    size 16
    color "#402313"

style button:
    activate_sound "sounds/click3.mp3"
    background "#5d5151E6" # ConditionSwitch("interface_color == \"gold\"", "#ac8d5aE6", "True", "#5d5151E6")
    hover_background "#897e75" # ConditionSwitch("interface_color == \"gold\"", "#97681f", "True", "#897e75")
    insensitive_background "#463b3bE6" # ConditionSwitch("interface_color == \"gold\"", "#917442E6", "True", "#463b3bE6")
    selected_background "#766a6aE6" # ConditionSwitch("interface_color == \"gold\"", "#e5c48dE6", "True", "#766a6aE6")
    selected_hover_background "#897e75" # onditionSwitch("interface_color == \"gold\"", "#97681f", "True", "#897e75")
    # padding (5, 5, 5, 5)

style button_text:
    color "#9b8d84" #If(interface_color == "gold", "#f9d592", "#9b8d84")
    hover_color "#ffffff"
    insensitive_color "#50443c"
    selected_color "#eedfd5"
    selected_hover_color "#FFFFFF"
    outlines [(1, "#00000080", 1, 0)]

style imagemap:
    activate_sound "sounds/click3.mp3"

style input:
    color "#5c321b"

# Dialogue styles
style say_window:
    background Frame(DynamicDisplayable("'interface/frames/[interface_color]/frame.png'"))
    top_margin 22
    left_padding 250
    right_padding 250
    top_padding 40
    yminimum 143

style say_who_window:
    is default
    xminimum 164
    ysize 32
    background Frame(DynamicDisplayable("'interface/frames/[interface_color]/namebox.png'"), 6, 6)
    xpos 235
    ypos 48
    text_align 0.5

style say_label:
    bold False
    text_align 0.5
    xalign 0.5
    yalign 0.5

# Day/night text styles
style day_text:
    color "#f9d592"
    hover_color "#FFFFFF"
    insensitive_color "#50443c"
    selected_color "#eedfd5"
    selected_hover_color "#FFFFFF"
    outlines [ (1, "#00000080", 1, 0) ]

style night_text:
    color "#9b8d84"
    hover_color "#FFFFFF"
    insensitive_color "#50443c"
    selected_color "#eedfd5"
    selected_hover_color "#FFFFFF"
    outlines [ (1, "#00000080", 1, 0) ]

# Day/night button styles
style day_button:
    background "#ac8d5aE6"
    hover_background "#97681f"
    insensitive_background "#d1a02eB3"
    padding (5, 5, 5, 5)

style night_button:
    background "#5d5151E6"
    hover_background "#897e75"
    insensitive_background "#9e8449"
    padding (5, 5, 5, 5)

# Choice menu styles
style menu_choice:
    hover_color "#e9d570"
    hover_outlines [(2, "#402313", 0, 0)]

style menu_choice_day:
    size 18
    xalign 0.5
    text_align 0.5
    color "#f9d592"
    hover_color "#ffffff"
    insensitive_color "#444"
    outlines [ (1, "#00000080", 1, 0) ]

style menu_choice_night:
    size 18
    xalign 0.5
    text_align 0.5
    color "#9b8d84"
    hover_color "#ffffff"
    insensitive_color "#444"
    outlines [ (1, "#00000080", 1, 0) ]

style menu_choice_daybutton:
    yminimum 28
    xsize int(config.screen_width * 0.5)
    background "#ac8d5aE6"
    hover_background "#97681f"
    insensitive_background "#d1a02eB3"
    activate_sound "sounds/click3.mp3"

style menu_choice_nightbutton:
    yminimum 28
    xsize int(config.screen_width * 0.5)
    background "#5d5151E6"
    hover_background "#897e75"
    insensitive_background "#9e8449"
    activate_sound "sounds/click3.mp3"

style say_two_window_vbox:
    yalign 1.0
