

label wardrobe_init:

    if not hasattr(renpy.store,'cho_bg_color') or reset_persistants:

        $ hide_transitions = False
        $ active_girl = "hermione"

        $ wardrobe_page = 0
        $ wardrobe_page_choice = 0
        $ wardrobe_toggle_page = 0
        $ wardrobe_chitchat_active = True

        $ play_wardrobe_music = False
        $ wardrobe_music_active = False
        $ add_wardrobe_sound = False

        $ wr_her_action = "none"

        $ wardrobe_color_update = True
        $ wardrobe_color = "base"

        $ wardrobe_gift_item = 0
        $ wardrobe_costume_selection = 0
        $ wardrobe_uniform_selection = ""

        #Wardrobe Categories
        $ wardrobe_head_category = 0
        $ wardrobe_tops_category = 0
        $ wardrobe_bottoms_category = 0
        $ wardrobe_stockings_category = 0
        $ wardrobe_accessories_category = 0
        $ wardrobe_underwear_category = 0
        $ wardrobe_outfits_category = 0
        $ wardrobe_gifts_category = 0

        #Wardrobe Color Select
        $ wr_background_color            = ["base","red","green","blue"]
        $ wardrobe_hair_style            = "curly"
        $ wardrobe_head_color            = "base"
        $ wardrobe_uniform_color         = "base" #can be: base, red, greed, blue, or yellow.
        $ wardrobe_tops_color            = "base"
        $ wardrobe_bottoms_color         = "base"
        $ wardrobe_other_clothings_color = "base"
        $ wardrobe_accessories_color     = "base"
        $ wardrobe_underwear_color       = "base"
        $ wardrobe_outfits_color         = "base"

        #Wardrobe Icons
        $ icon_xpos_offset = 0
        $ icon_ypos_offset = 0

        $ wardrobe_load_custom_outfit = True

        $ cho_bg_color = [82,150,248,255]
        $ luna_bg_color = [82,150,248,255]

    return

label color_cloth_test:
    show screen cloth_test

    $ _return = ui.interact()

    hide screen cloth_test

    if _return[0] == "change_color":
        $ active_layer = _return[1]
        show screen cloth_test()
        $ cho_top_school_CLOTH.set_color(_return[1])
        hide screen cloth_test

    jump color_cloth_test


screen cloth_test:
    python:
        if not color_preview == None:
            cho_top_school_CLOTH.color[active_layer] = color_preview

    zorder 100
    add cho_top_school_CLOTH.get_image() xpos 700 yalign 0.5 zoom 0.5 xanchor 0.5 yanchor 0.5

    vbox:
        xpos 850
        ypos 300
        spacing 5
        frame background get_hex_string_tuple(cho_top_school_CLOTH.get_color(0)) xsize 50 ysize 50
        frame background get_hex_string_tuple(cho_top_school_CLOTH.get_color(1)) xsize 50 ysize 50
        frame background get_hex_string_tuple(cho_top_school_CLOTH.get_color(2)) xsize 50 ysize 50
        frame background get_hex_string_tuple(cho_top_school_CLOTH.get_color(3)) xsize 50 ysize 50
    vbox:
        xpos 900
        ypos 300
        spacing 5
        textbutton "Channel 1" action Return(["change_color", 0])
        textbutton "Channel 2" action Return(["change_color", 1])
        textbutton "Channel 3" action Return(["change_color", 2])
        textbutton "Channel 4" action Return(["change_color", 3])

#label change_color(layer):
    #$ cho_top_school_CLOTH.set_color(layer)

init:
    $ cho_top_school_CLOTH = cloth_class(char="cho", type="tops", id="school_1", layers=5, name="School top", desc="description") # Keep the 'type' plural please.
    #$ cho_top_school2_CLOTH = cloth_class(char="cho", type="top", id="school2", layers=4, name="School top", desc="description")

init -5 python:
    class cloth_class(object):
        char = "MISSING" # astoria, cho, hermione, luna, susan, tonks
        type = "MISSING" # same as folder names
        id = "MISSING"
        layers = 4
        color = []

        name = "NONE"
        desc = ""

        imagepath = ""

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
            self.imagepath = "characters/"+str(self.char)+"/clothes/"+str(self.type)+"/"
            for i in xrange(0, self.layers):
                self.color.append([100, 150, 200, 255])

        def get_character(self):
            return self.char

        def get_type(self):
            return self.type

        def get_id(self):
            return self.id

        def get_layers(self):
            return self.layers
            #im.matrix.desaturate()*
        def get_matrixcolor(self, layer):
            return im.matrix.tint(self.color[layer][0]/255.0, self.color[layer][1]/255.0, self.color[layer][2]/255.0)

        def get_color(self, layer):
            return (self.color[layer][0]/255.0, self.color[layer][1]/255.0, self.color[layer][2]/255.0, self.color[layer][3]/255.0)

        def get_alpha(self, layer):
            return self.color[layer][3]/255.0

        def set_color(self, layer):
            self.color[layer] = color_picker(self.color[layer], False, "Cloth layer "+str(layer), pos_xy=[50, 130])

        def get_name(self):
            return self.name

        def get_description(self):
            return self.desc

        def get_imagepath(self):
            return self.imagepath

        def get_imagelayer(self, layer):
            # Appears as (example):
            # characters/cho/bottoms/ (skirt_school_1) / (1) .png
            return self.imagepath+str(self.id)+"/"+str(layer)+".png"

        def get_image(self):
            if self.layers == 1:
                return im.MatrixColor(str(self.get_imagelayer(0)), self.get_matrixcolor(0))
            elif self.layers == 2:
                return Composite(
                    (1010, 1200),
                    (0, 0), im.MatrixColor(str(self.get_imagelayer(0)), self.get_matrixcolor(0)),
                    (0, 0), im.MatrixColor(str(self.get_imagelayer(1)), self.get_matrixcolor(1)))
            elif self.layers == 3:
                return Composite(
                    (1010, 1200),
                    (0, 0), im.MatrixColor(str(self.get_imagelayer(0)), self.get_matrixcolor(0)),
                    (0, 0), im.MatrixColor(str(self.get_imagelayer(1)), self.get_matrixcolor(1)),
                    (0, 0), im.MatrixColor(str(self.get_imagelayer(2)), self.get_matrixcolor(2)))
            elif self.layers == 4:
                return Composite(
                    (1010, 1200),
                    (0, 0), im.MatrixColor(str(self.get_imagelayer(0)), self.get_matrixcolor(0)),
                    (0, 0), im.MatrixColor(str(self.get_imagelayer(1)), self.get_matrixcolor(1)),
                    (0, 0), im.MatrixColor(str(self.get_imagelayer(2)), self.get_matrixcolor(2)),
                    (0, 0), im.MatrixColor(str(self.get_imagelayer(3)), self.get_matrixcolor(3)))
            elif self.layers == 5:
                return Composite(
                    (1010, 1200),
                    (0, 0), im.MatrixColor(str(self.get_imagelayer(0)), self.get_matrixcolor(0)),
                    (0, 0), im.MatrixColor(str(self.get_imagelayer(1)), self.get_matrixcolor(1)),
                    (0, 0), im.MatrixColor(str(self.get_imagelayer(2)), self.get_matrixcolor(2)),
                    (0, 0), im.MatrixColor(str(self.get_imagelayer(3)), self.get_matrixcolor(3)),
                    (0, 0), self.get_imagelayer(4))
