screen color_picker(color, alpha, title, pos_xy):
    tag color_picker
    zorder 9
    modal True

    # Screen variables
    default rgba = color
    default hue = 0
    default saturation = 0
    default value = 0
    default _alpha = 0 # Avoid name conflict with 'alpha' screen variable in other active screens

    # Set HSVA variables based on RGBA when screen shows
    on "show" action Function(color_picker_update_hsva)

    frame:
        area (pos_xy[0], pos_xy[1], 500, 350)
        padding (6, 6)

        if interface_color == "gold":
            background "#e9ca7f"
        else:
            background "#7c716a"

        add "interface/color_picker/"+str(interface_color)+"/frame.png" pos (-10, -10)

        text title xalign 0.5 text_align 0.5

        # 2D color map
        frame:
            area (25, 25, 255, 255)
            background Solid(tuple([x * 255 for x in colorsys.hsv_to_rgb(1 - hue, 1, 1)]))
        imagebutton:
            area (25, 25, 255, 255)
            #idle im.MatrixColor(SVGradientImage(size=(255,255)), color_matrix.hue((1- hue) * 360))
            idle Frame("interface/color_picker/saturation_value_gradient.png")
            focus_mask None
            keyboard_focus False
            key_events False
            # Offset is frame position + padding + image position, size is image size
            action Function(color_picker_clicked, offset=(pos_xy[0] + 25 + 6, pos_xy[1] + 25 + 6), size=(255, 255))
        draggroup:
            # Allow cursor to extend 8 pixels outside map
            area (25 - 8, 25 - 8, 255 + 16,  255 + 16)
            drag:
                pos (int(saturation * 253), int((1 - value) * 253))
                anchor (0, 0)
                child "interface/color_picker/"+str(interface_color)+"/cursor_sq.png"
                focus_mask None
                activated color_picker_dragged
                dragged color_picker_dragged

        # Hue slider
        vbar:
            area (290, 25, 30, 255)
            value ScreenVariableValue("hue", range=1.0, step=0.01, action=Function(color_picker_update_rgba))
            base_bar HueGradientImage(size=(30,255))
            thumb Image("interface/color_picker/"+str(interface_color)+"/cursor_h.png", xalign=0.5)
            thumb_offset 0
            top_gutter 0
            bottom_gutter 0

        if alpha:
            # Alpha slider
            add "interface/color_picker/"+str(interface_color)+"/alpha.png" xpos 22 ypos 287
            add Frame("interface/color_picker/checker.png", tile=True, ysize=30, xsize=255) xpos 25 ypos 290
            bar:
                area (25, 290, 255, 30)
                value ScreenVariableValue("_alpha", range=1.0, step=0.01, action=Function(color_picker_update_rgba))
                base_bar im.MatrixColor(AlphaGradientImage(size=(255,30)), im.matrix.colorize(rgba, rgba))
                thumb Image("interface/color_picker/"+str(interface_color)+"/cursor_v.png", xalign=0.5)
                thumb_offset 0
                top_gutter 0
                bottom_gutter 0

        # Selected color
        add Frame("interface/color_picker/checker.png", tile=True, ysize=100, xsize=100) xpos 360 ypos 180
        frame:
            area (360, 180, 100, 100)
            background Solid(rgba)

        # Text input
        vbox:
            pos (355, 25)
            spacing 6
            textbutton "Red: " + str(int(rgba[0])):
                style btn_style text_style txt_style
                size_group "rgba"
                xsize 110
                clicked Return(["input", 0])
            textbutton "Green: " + str(int(rgba[1])):
                style btn_style text_style txt_style
                size_group "rgba"
                clicked Return(["input", 1])
            textbutton "Blue: " + str(int(rgba[2])):
                style btn_style text_style txt_style
                size_group "rgba"
                clicked Return(["input", 2])
            if alpha:
                textbutton "Alpha: " + str(int(rgba[3])):
                    style btn_style text_style txt_style
                    size_group "rgba"
                    clicked Return(["input", 3])

        # Window buttons
        hbox: 
            align (1.0, 1.0)
            xoffset -3
            spacing 6
            textbutton "Cancel":
                style btn_style text_style txt_style
                clicked Return("cancel")
            textbutton "Apply":
                style btn_style text_style txt_style
                clicked Return(["apply", rgba])

default picking_color = None

init -1 python:
    import colorsys

    def color_picker(color=[0,0,0,0], alpha=True, title="Pick a colour", pos_xy=(240, 130)):
        global picking_color
        picking_color = color # Color object (list) to be updated live
        start_color = list(color) # Keep a copy

        renpy.show_screen("color_picker", tuple(color), alpha, title, pos_xy)
        while True:
            _return = ui.interact()
            
            if _return[0] == "input":
                color_picker_input(_return[1])

            elif _return == "cancel":
                renpy.hide_screen("color_picker")
                update_picking_color(start_color) # Reset live color object
                picking_color = None
                return start_color

            elif _return[0] == "apply":
                renpy.hide_screen("color_picker")
                picking_color = None
                return color # Return live color object instead of _return tuple

    def update_picking_color(rgba):
        global picking_color
        for (i, x) in enumerate(rgba):
            picking_color[i] = x

    def color_picker_input(comp):
        scope = renpy.get_screen("color_picker").scope
        x = renpy.input(["Red", "Green", "Blue", "Alpha"][comp], str(scope["rgba"][comp]), "0123456789", length=3)
        x = max(0, min(255, int(x)))
        tuplist = list(scope["rgba"])
        tuplist[comp] = x
        scope["rgba"] = tuple(tuplist)
        color_picker_update_hsva()
        update_picking_color(scope["rgba"])

    def color_picker_update_hsva():
        scope = renpy.get_screen("color_picker").scope
        (r, g, b, a) = scope["rgba"]
        (h, s, v) = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
        scope["hue"] = 1 - h
        scope["saturation"] = s
        scope["value"] = v
        scope["_alpha"] = a / 255.0

    def color_picker_update_rgba():
        scope = renpy.get_screen("color_picker").scope
        (r, g, b) = colorsys.hsv_to_rgb(1 - scope["hue"], scope["saturation"], scope["value"])
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)
        a = int(scope["_alpha"] * 255)
        scope["rgba"] = (r, g, b, a)
        update_picking_color(scope["rgba"])
        renpy.restart_interaction()

    def color_picker_clicked(offset, size):
        # Mouse screen position to local position
        (x, y) = renpy.get_mouse_pos()
        x = max(0, min(x - offset[0], size[0]))
        y = max(0, min(y - offset[1], size[1]))
        # Update screen variables
        scope = renpy.get_screen("color_picker").scope
        scope["saturation"] = float(x) / size[0]
        scope["value"] = 1 - float(y) / size[1]
        color_picker_update_rgba()

    def color_picker_dragged(drags, drop=None):
        # Compensate for draggable area
        width = drags[0].parent_width - drags[0].w
        height = drags[0].parent_height - drags[0].h
        x = drags[0].x
        y = drags[0].y
        # Update screen variables
        scope = renpy.get_screen("color_picker").scope
        scope["saturation"]  = float(x) / width
        scope["value"] = 1 - float(y) / height
        color_picker_update_rgba()

    class GradientImageBase(im.ImageBase):
        def __init__(self, **properties):
            super(GradientImageBase, self).__init__(**properties)
            self.size = properties.get('size')

    class AlphaGradientImage(GradientImageBase):
        def load(self):
            # Generate a horizontal alpha gradient
            width = self.size[0]
            surf = renpy.display.pgrender.surface((width, 1), True)
            for x in xrange(width):
                color = (255, 255, 255, x)
                surf.set_at((x, 0), color)
            surf = renpy.display.pgrender.transform_scale(surf, self.size)
            return surf

    class HueGradientImage(GradientImageBase):
        def load(self):
            # Generate a vertical hue gradient
            height = self.size[1]
            surf = renpy.display.pgrender.surface((1, height), False)
            for y in xrange(height):
                hue = float(y) / height
                (r, g, b) = colorsys.hsv_to_rgb(hue, 1, 1)
                color = (r * 255, g * 255, b * 255)
                surf.set_at((0, y), color)
            surf = renpy.display.pgrender.transform_scale(surf, self.size)
            return surf

    class SVGradientImage(GradientImageBase):
        def load(self):
            # Generate a 2D saturation-value gradient
            (width, height) = self.size
            surf = renpy.display.pgrender.surface(self.size, True)
            for y in xrange(height):
                val = 1 - float(y) / height
                for x in xrange(width):
                    sat = float(x) / width
                    (r, g, b) = colorsys.hsv_to_rgb(0, sat, val)
                    color = (r * 255, g * 255, b * 255)
                    surf.set_at((x, y), color)
            return surf
