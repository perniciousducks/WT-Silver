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
    xpadding 10
    background Frame(DynamicDisplayable("'interface/frames/[interface_color]/namebox.png'"), 6, 6)
    xpos 235
    ypos 48
    text_align 0.5

style say_label:
    bold False
    text_align 0.5
    xalign 0.5
    yalign 0.5

# TODO Remove temporary styles day_text/night_text
#style day_text is day_button_text

#style night_text is night_button_text

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

# Choice menu styles
style menu_text is default:
    text_align 0.5
    outlines [(1, "#00000080", 1, 0)]

style day_menu_text:
    color "#f9d592"
    hover_color "#fff"
    insensitive_color "#444"

style night_menu_text:
    color "#9b8d84"
    hover_color "#fff"
    insensitive_color "#444"

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

# btn_hover day: (#edc48240|#e3ba7140) night: #7d75aa40