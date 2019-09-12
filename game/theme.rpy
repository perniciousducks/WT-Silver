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
        frame = "#5d5151", #ConditionSwitch("interface_color == \"gold\"", "#ac8d5a", "True", "#5d5151"),

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

    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.
    
    
    #renpy.register_style_preference("text2", "day", style.button_text, "color", "#f9d592")
    #renpy.register_style_preference("text2", "night", style.button_text, "color", "#9b8d84")

    style.window.background = Frame(ConditionSwitch("interface_color == \"gold\"", "interface/frames/gold/frame.png","True","interface/frames/gray/frame.png"))
    
    #style.pref_button.background = Frame(ConditionSwitch("interface_color == \"gold\"", "#FFF", "True", "#000"),15,15)
    
    style.button.background = "#5d5151E6"#ConditionSwitch("interface_color == \"gold\"", "#ac8d5aE6", "True", "#5d5151E6")
    style.button.hover_background = "#897e75"#ConditionSwitch("interface_color == \"gold\"", "#97681f", "True", "#897e75")
    style.button.insensitive_background = "#463b3bE6"#ConditionSwitch("interface_color == \"gold\"", "#917442E6", "True", "#463b3bE6")
    style.button.selected_background = "#766a6aE6"#ConditionSwitch("interface_color == \"gold\"", "#e5c48dE6", "True", "#766a6aE6")
    style.button.selected_hover_background = "#897e75"#ConditionSwitch("interface_color == \"gold\"", "#97681f", "True", "#897e75")
    
    style.button_text.color = "#9b8d84" #If(interface_color == "gold", "#f9d592", "#9b8d84")
    style.button_text.hover_color = "#ffffff"
    style.button_text.insensitive_color = "#50443c"
    style.button_text.selected_color = "#eedfd5"
    style.button_text.selected_hover_color = "#FFFFFF"
    style.button_text.outlines = [(1, "#00000080", 1, 0)]

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    # style.window.left_margin = 6
    ##style.window.right_margin = 280
    style.window.top_margin = 22
    # style.window.bottom_margin = 6

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 250 #200
    style.window.right_padding = 250
    style.window.top_padding = 40

    #Backup/Original
    #style.window.left_padding = 65
    #style.window.right_padding = 70
    #style.window.top_padding = 40
    # style.window.bottom_padding = 6

    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.window.yminimum = 143


    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    style.default.font = "interface/CREABBB.TTF"

    ## The default size of text.
    style.default.size = 16
    style.default.color = "#402313"

    #renpy.register_style_preference("dialog", "Day", style.say_dialogue, "font", "interface/CREABBB.TTF")
    #renpy.register_style_preference("dialog", "Day", style.say_dialogue, "size", 18)
    #renpy.register_style_preference("dialog", "Day", style.say_dialogue, "color", "#402313")

    #renpy.register_style_preference("dialog", "Night", style.say_dialogue, "font", "interface/CREABBB.TTF")
    #renpy.register_style_preference("dialog", "Night", style.say_dialogue, "size", 18)
    #renpy.register_style_preference("dialog", "Night", style.say_dialogue, "color", "#211109")

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    ## Sounds that are used when button and imagemaps are clicked.

    style.button.activate_sound = "interface/click3.mp3"
    style.imagemap.activate_sound = "interface/click3.mp3"

    ##Modifies the Menu Choice's BG
    #style.menu_choice_button.background = Frame("choice_bg_idle.jpg",28,9)
    #style.menu_choice_button.hover_background = Frame("choice_bg_hover.jpg",28,9)
    # style.name_button.selected_background = Frame("choice_bg_idle.jpg",28,9)
    # style.name_button.selected_hover_background = Frame("choice_bg_idle.jpg",28,9)
    # style.name_button.insensitive_background = Frame("choice_bg_idle.jpg",28,9)
    # style.menu_choice_button.yminimum = 39 #Sets height, recommended to be the exact height of your image

    ##Modifies the Menu Choice's Text
    #style.menu_choice.color = "#000"
    #style.menu_choice.size = 18
    #style.menu_choice.outlines = [(2, "#000", 0, 0)]
    style.menu_choice.hover_color = "#e9d570"
    style.menu_choice.hover_outlines = [(2, "#402313", 0, 0)]

    #style.file_picker_button.color = "#c25fb9"
 ########################################################################################

    style.say_who_window.background = Frame(ConditionSwitch("interface_color == \"gold\"", "interface/frames/gold/PinkBox.png","True","interface/frames/gray/PinkBox.png"), 15, 15)

    #style.say_who_window.background = Frame("interface/PinkBox.png", 15, 15) #Background skin
    style.say_who_window.xalign = 0.0
    style.say_who_window.yalign = 1.0
    style.say_who_window.xpos = 227 #For precise placement
    style.say_who_window.ypos = 125 #For precise placement
    style.say_who_window.left_padding = 20
    style.say_who_window.top_padding = 15
    style.say_who_window.right_padding = 20
    style.say_who_window.bottom_padding = 15
    style.say_who_window.xminimum = 150
    style.say_who_window.yminimum = 10
    style.say_who_window.xfill = False

    # Override Styles
    style.input.color = "#5c321b"
