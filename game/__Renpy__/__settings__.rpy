init:
    # Set defaults
    if persistent.text_color_day == None:
        $ persistent.text_color_day = "#402313"
        $ persistent.text_color_night = "#341c0f"
        $ persistent.text_outline = "#00000000"
        $ persistent.nightmode = False

label saybox_color(day=True):
    show screen preferences
    if day:
        $ persistent.text_color_day = color_picker(get_rgb_list(persistent.text_color_day), False, "Day Text Colour")
        $ persistent.text_color_day = get_hex_string(persistent.text_color_day[0]/255.0, persistent.text_color_day[1]/255.0, persistent.text_color_day[2]/255.0)
    else:
        $ persistent.text_color_night = color_picker(get_rgb_list(persistent.text_color_night), False, "Night Text Colour")
        $ persistent.text_color_night = get_hex_string(persistent.text_color_night[0]/255.0, persistent.text_color_night[1]/255.0, persistent.text_color_night[2]/255.0)
    return