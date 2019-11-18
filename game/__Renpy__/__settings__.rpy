init:
    # Set defaults
    if persistent.text_color_day == None:
        $ persistent.text_color_day = "#402313"
        $ persistent.text_color_night = "#341c0f"
        $ persistent.text_outline = "#00000000"
        $ persistent.nightmode = False

init -1 python:
    def set_text_color(day=True):
        # This function must be invoked in a new context by preferences screen
        renpy.show_screen("preferences")
        # Temporarily change interface color
        tmp_color = renpy.store.interface_color
        renpy.call_in_new_context("update_interface_color", "gray")
        if day:
            persistent.text_color_day = color_picker(get_rgb_list(persistent.text_color_day), False, "Day Text Colour")
            persistent.text_color_day = get_hex_string(persistent.text_color_day[0]/255.0, persistent.text_color_day[1]/255.0, persistent.text_color_day[2]/255.0)
        else:
            persistent.text_color_night = color_picker(get_rgb_list(persistent.text_color_night), False, "Night Text Colour")
            persistent.text_color_night = get_hex_string(persistent.text_color_night[0]/255.0, persistent.text_color_night[1]/255.0, persistent.text_color_night[2]/255.0)
        # Reset interface color
        renpy.call_in_new_context("update_interface_color", tmp_color)
