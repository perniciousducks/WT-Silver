init:
    if persistent.text_color_day == None:
        $ persistent.text_color_day = "#402313"
        $ persistent.text_color_night = "#402313"
        $ persistent.text_outline = "#00000000"

label saybox_color(day=True):
    if day:
        $ persistent.text_color_day = color_picker([255, 255, 255, 255], [255, 255, 255], False, "Day Text Colour")
        $ persistent.text_color_day = get_hex_string(persistent.text_color_day[0]/255, persistent.text_color_day[1]/255, persistent.text_color_day[2]/255)
    else:
        $ persistent.text_color_night = color_picker([255, 255, 255, 255], [255, 255, 255], False, "Night Text Colour")
        $ persistent.text_color_night = get_hex_string(persistent.text_color_night[0]/255, persistent.text_color_night[1]/255, persistent.text_color_night[2]/255)
    $ ShowMenu('preferences')