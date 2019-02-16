

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
    $ cho_class.cache_override = True
    $ current_clothing = cho_class.get_cloth("top")
    show screen cloth_test

    $ _return = ui.interact()

    hide screen cloth_test

    if _return[0] == "change_color":
        $ active_layer = _return[1]
        show screen cloth_test()
        $ current_clothing.set_color(_return[1])
        hide screen cloth_test
        $ cho_class.cache_override = False
    elif _return == "reset":
        $ current_clothing.reset_color()

    jump color_cloth_test


screen cloth_test:
    python:
        if not color_preview == None:
            current_clothing.color[active_layer] = color_preview

    zorder 100
    add cho_class.get_image() xpos 700 yalign 0.5 zoom 0.5 xanchor 0.5 yanchor 0.5

    vbox:
        xpos 850
        ypos 300
        spacing 5
        frame background get_hex_string_tuple(current_clothing.get_color(0)) xsize 50 ysize 50
        frame background get_hex_string_tuple(current_clothing.get_color(1)) xsize 50 ysize 50
        frame background get_hex_string_tuple(current_clothing.get_color(2)) xsize 50 ysize 50
        frame background get_hex_string_tuple(current_clothing.get_color(3)) xsize 50 ysize 50
    vbox:
        xpos 900
        ypos 300
        spacing 5
        textbutton "Channel 1" action Return(["change_color", 0])
        textbutton "Channel 2" action Return(["change_color", 1])
        textbutton "Channel 3" action Return(["change_color", 2])
        textbutton "Channel 4" action Return(["change_color", 3])
        textbutton "Default" action Return("reset")

#label change_color(layer):
    #$ cho_top_school_CLOTH.set_color(layer)

# Equip label from the new wardrobe.
label equip_cho_item(item): # ('_return', will be the id of the clothing item.)

    return

# Toggle 'test_clothing_colors' to True to torn this screen on for Cho.
screen cho_uniform_test:
    tag cho_main

    ### CLOTHES
    if cho_class.get_cloth("bra"):
        add t_cho_bra.get_image() xpos cho_xpos ypos cho_ypos alpha cho_bra_transp xzoom cho_flip zoom (1.0/cho_scaleratio)
    #if cho_wear_stockings:
    #    add t_cho_stockings xpos cho_xpos ypos cho_ypos alpha cho_stockings_transp xzoom cho_flip zoom (1.0/cho_scaleratio)
    #if cho_wear_garterbelt:
    #    add t_cho_garterbelt xpos cho_xpos ypos cho_ypos alpha cho_panties_transp xzoom cho_flip zoom (1.0/cho_scaleratio)
    if cho_wear_panties:
        add t_cho_panties.get_image() xpos cho_xpos ypos cho_ypos alpha cho_panties_transp xzoom cho_flip zoom (1.0/cho_scaleratio)
    if cho_wear_bottom:
        add t_cho_bottom.get_image() xpos cho_xpos ypos cho_ypos alpha cho_bottom_transp xzoom cho_flip zoom (1.0/cho_scaleratio)

    # Tops
    # One image for the torso, one for the left side sleeve layer if the item has sleeves. Sleeves will be ignored if they're set to blank.
    if cho_wear_top:
        # Add left side arm sleeve here, before the torso layer.
        if t_cho_top_L.id in ["top_sweater_1"]: # Automate this process so we don't have to manually add ids to that list. Maybe add a variable to the class or check if the layers start with an 'L_' or 'R_' in the folder.
            add t_cho_top_L.get_image() xpos cho_xpos ypos cho_ypos alpha cho_top_transp xzoom cho_flip zoom (1.0/cho_scaleratio)
        add t_cho_top_mid.get_image() xpos cho_xpos ypos cho_ypos alpha cho_top_transp xzoom cho_flip zoom (1.0/cho_scaleratio)


    # left side glove layer.
    if cho_wear_gloves:
        add cho_gloves xpos cho_xpos ypos cho_ypos alpha cho_gloves_transp xzoom cho_flip zoom (1.0/cho_scaleratio) # 'L'

    # robe torso and left side sleeve that gets put on top of her left side glove, sleeves, and arm.
    #if cho_wear_robe: # Robes will also need the torso and sleeve layers for the different arms.
    #    if t_cho_robe_L != "blank": # left side sleeve.
    #        add t_cho_robe_L xpos cho_xpos ypos cho_ypos alpha cho_robe_transp xzoom cho_flip zoom (1.0/cho_scaleratio) # Sleeve 'L'
    #    add t_cho_robe_mid xpos cho_xpos ypos cho_ypos alpha cho_robe_transp xzoom cho_flip zoom (1.0/cho_scaleratio) # Torso 'mid'



    # right side arm and hand layer, that gets layered on top of her bottom and top items.
    add cho_l_hand xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio) # Arm 'R'

    # right side sleeve layer for the top that gets put on top of her hand.
    if cho_wear_top:
        if t_cho_top_L.id in ["top_sweater_1"]: # right side sleeve.
           add t_cho_top_L.get_image() xpos cho_xpos ypos cho_ypos alpha cho_robe_transp xzoom cho_flip zoom (1.0/cho_scaleratio) # Sleeve 'R'

    # right side glove layer that gets put on top of her hand and top item, but below the robe.
    #if cho_wear_gloves:
    #    add cho_gloves xpos cho_xpos ypos cho_ypos alpha cho_gloves_transp xzoom cho_flip zoom (1.0/cho_scaleratio) # Gloves 'R'

    # right side sleeve for the robe that gets put on top of gloves, sleeves, and her arm.
    #if cho_wear_robe:
    #    add cho_robe xpos cho_xpos ypos cho_ypos alpha cho_robe_transp xzoom cho_flip zoom (1.0/cho_scaleratio) # Robe Sleeve 'R'



    #if cho_wear_neckwear:
    #    add cho_neckwear xpos cho_xpos ypos cho_ypos xzoom cho_flip zoom (1.0/cho_scaleratio)

    ### ZORDER
    zorder cho_zorder






init:
    # Cho basic clothing layers (those are the ones that will be used on her clothing screen!)
    # The 't_' stands for test to not interfere with Cho's old uniform clothing screen. Remove it when it gets replaced.
    $ t_cho_top_mid  = cloth_class(char="cho", type="tops", id="top_school_1", layers=5)   # I need a way to add 'mid_' in front of the layer number!
    $ t_cho_top_L    = cloth_class(char="cho", type="tops", id="top_school_1", layers=5)   # I need a way to add 'L_' in front of the layer number!
    $ t_cho_top_R    = cloth_class(char="cho", type="tops", id="top_school_1", layers=5)   # I need a way to add 'R_' in front of the layer number!

    $ t_cho_bottom   = cloth_class(char="cho", type="bottoms", id="skirt_short_1", layers=2)
    $ t_cho_bra      = cloth_class(char="cho", type="bras",    id="sport_bra_1", layers=3)
    $ t_cho_panties  = cloth_class(char="cho", type="panties", id="sport_panties_1", layers=3)

    $ cho_top_school_CLOTH = cloth_class(char="cho", type="tops", id="top_school_1", layers=5, color=[[200, 100, 100, 255], [100, 200, 100, 255], [100, 100, 200, 255], [150, 50, 150, 255]], name="School top", desc="description") # Keep the 'type' plural please.
    #$ cho_top_school2_CLOTH = cloth_class(char="cho", type="top", id="school2", layers=4, name="School top", desc="description")
    $ cho_test_cloth = cloth_class(char="cho", type="tops", id="top_school_1", layers=5, color=[[200, 100, 100, 255], [100, 200, 100, 255], [100, 100, 200, 255], [150, 50, 150, 255]], name="School top", desc="description")
    
    
    python:
        if not hasattr(renpy.store,'cho_class'): #important!
            cho_class = char_class(char="cho")
        
        if not hasattr(renpy.store,'cho_body'): #important!
            cho_class.body = {
                        "hair":        ["ponytail_blue_top", 12, 0, 0, False],
                        "hairshadow":  ["ponytail_blue_base", 11, 0, 0, False],
                        "armleft":     ["arm_down_l", 17, 0, 0, False],
                        "armright":    ["arm_down_r", 1, 0, 0, False],
                        "breasts":     ["breasts_bikini_tan", 3, 0, 0, False],
                        "base":        ["base_01", 2, 0, 0, False],
                        "legs":        [None, 5, 1, 0, False]}
        if not hasattr(renpy.store,'cho_face'): #important!
            cho_class.face = {
                        "tears":       [None, 11, 0, 0, False],
                        "cheeks":      [None, 10, 0, 0, False],
                        "eyebrows":    ["base", 9, 0, 0, False],
                        "eyes":        ["base", 8, 1, 0, False],
                        "pupils":      ["mid", 7, 0, 0, False],
                        "whites":      ["_white_", 6, 0, 0, False],
                        "mouth":       ["base", 5, 0, 0, False]}
        if not hasattr(renpy.store,'cho_other'): #important!
            cho_class.other = {
                        "cum":         [None, 15, 0, 0, False],
                        "emote":       [None, 30, 0, 0, False]}
                        
            cho_class.update_paths("body", "face", "other")
        if not hasattr(renpy.store,'cho_clothing'): #important!
            cho_class.clothing = {
                        "hat":        [None, 24, 0, 0, False],
                        "neckwear":   [None, 23, 0, 0, False],
                        "badge":      [None, 22, 0, 0, False],
                        "robe":       [None, 21, 0, 0, False],
                        "gloves":     [None, 20, 0, 0, False],
                        "top":        [cho_test_cloth, 19, 0, 0, False],
                        "bra":        [t_cho_bra, 18, 0, 0, False],
                        "belt":       [None, 17, 0, 0, False],
                        "bottom":     [t_cho_bottom, 16, 0, 0, False],
                        "garter":     [None, 15, 0, 0, False],
                        "panties":    [t_cho_panties, 14, 0, 0, False],
                        "stockings":  [None, 13, 0, 0, False],
                        "plug":       [None, 0, 0, 0, False]}

init -5 python:
    class cloth_class(object):
        char = None # astoria, cho, hermione, luna, susan, tonks
        type = None # same as folder names
        id = None
        layers = None
        color = []
        color_default = []
        skinlayer = "characters/dummy.png"

        name = ""
        desc = ""
        
        pose = ""

        imagepath = ""
        imagepath_original = ""
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
            
            if self.char == None:
                raise Exception('Clothing: "char" was not defined in cloth_class.')
                
            if self.type == None:
                raise Exception('Clothing: "type" was not defined in cloth_class.')
                
            if self.id == None:
                raise Exception('Clothing: "id" was not defined in cloth_class.')
                
            if self.layers == None:
                raise Exception('Clothing: "layers" number was not defined in cloth_class.')
                
            self.imagepath = "characters/"+self.char+"/clothes/"+self.type+"/"
            self.imagepath_original = self.imagepath
                
            if len(self.color) < self.layers:
                for i in xrange(len(self.color), self.layers):
                    self.color.append([255, 255, 255, 255])
                    
            self.color_default = [] # DO NOT DELETE !!!
            for i in xrange(0, len(self.color)):
                self.color_default.append(self.color[i])
                
            if self.layers > len(self.color):
                raise Exception('Clothing: "color" list does not match the number of layers in cloth_class.')
  
            if renpy.exists(self.imagepath+self.id+"/skin.png"):
                self.skinlayer = self.imagepath+self.id+"/skin.png"
                
        def set_pose(self, pose):
            if renpy.exists(self.imagepath+self.id+"/"+pose+"_0.png"):
                self.pose = pose
                return True
            return False
            
        def get_character(self):
            return self.char

        def get_type(self):
            return self.type

        def get_id(self):
            return self.id

        def get_layers(self):
            return self.layers

        def get_matrixcolor(self, layer):
            return im.matrix.tint(self.color[layer][0]/255.0, self.color[layer][1]/255.0, self.color[layer][2]/255.0)

        def get_color(self, layer):
            return (self.color[layer][0]/255.0, self.color[layer][1]/255.0, self.color[layer][2]/255.0, self.color[layer][3]/255.0)

        def get_alpha(self, layer):
            return self.color[layer][3]/255.0

        def set_color(self, layer):
            self.color[layer] = color_picker(self.color[layer], False, "Cloth layer "+str(layer+1), pos_xy=[50, 130])
            
        def reset_color(self):
            for i in xrange(0, len(self.color)):
                self.color[i] = self.color_default[i]

        def get_name(self):
            return self.name

        def get_description(self):
            return self.desc

        def get_imagepath(self):
            return self.imagepath

        def get_imagelayer(self, layer):
            return self.imagepath+self.id+"/"+str(layer)+".png" if self.pose == "" else self.imagepath+self.id+"/"+self.pose+"_"+str(layer)+".png"
                    
        def get_image(self):
            self.sprite = Image(self.skinlayer)
            
            # Keep used clothes images in cache
            renpy.start_predict("characters/"+self.char+"/clothes/"+self.type+"/"+self.id+"/*.*")

            for i in xrange(0, self.layers):
                    self.sprite = Composite(
                           (1010, 1200),
                           (0,0), self.sprite,
                           (0,0), im.MatrixColor(str(self.get_imagelayer(i)), self.get_matrixcolor(i)))
            return self.sprite
            
    class char_class(object):
        char = None
        
        cached = False
        cache_override = False
        
        body = {}
        face = {}
        clothing = {}
        other = {}
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
            
            if self.char == None:
                raise Exception('Character: "char" was not defined in char_class.')
                
        def get_object(self, dict, *keys):
            for key in keys:
                try:
                    dict = dict[key][0]
                except KeyError:
                    return None
            return dict
            
        def get_cloth(self, cloth):
            return self.get_object(self.clothing, cloth)
            
        def update_paths(self, *args):
            symbol = "/"
            
            if 'body' in args:
                imagepath = "characters/"+self.char+"/body/"
                
                hair = self.get_object(self.body, 'hair')
                hairshadow = self.get_object(self.body, 'hairshadow')
                armleft = self.get_object(self.body, 'armleft')
                armright = self.get_object(self.body, 'armright')
                breasts = self.get_object(self.body, 'breasts')
                base = self.get_object(self.body, 'base')
                legs = self.get_object(self.body, 'legs')
                
                if hair and symbol not in hair :
                    self.body['hair'][0] = imagepath+"hair/"+hair+".png"
                if hairshadow and symbol not in hairshadow :
                    self.body['hairshadow'][0] = imagepath+"hair/"+hairshadow+".png"
                if armleft and symbol not in armleft:
                    self.body['armleft'][0] = imagepath+"arms/"+armleft+".png"
                if armright and symbol not in armright:
                    self.body['armright'][0] = imagepath+"arms/"+armright+".png"
                if breasts and symbol not in breasts:
                    self.body['breasts'][0] = imagepath+"breasts/"+breasts+".png"
                if base and symbol not in base:
                    self.body['base'][0] = imagepath+"base/"+base+".png"
                if legs and symbol not in legs:
                    self.body['legs'][0] = imagepath+"legs/"+legs+".png"
            if 'face' in args:
                imagepath = "characters/"+self.char+"/face/"
                
                tears = self.get_object(self.face, 'tears')
                cheeks = self.get_object(self.face, 'cheeks')
                eyebrows = self.get_object(self.face, 'eyebrows')
                eyes = self.get_object(self.face, 'eyes')
                pupils = self.get_object(self.face, 'pupils')
                whites = self.get_object(self.face, 'whites')
                mouth = self.get_object(self.face, 'mouth')
                
                if tears and symbol not in tears:
                    self.face['tears'][0] = imagepath+"extras/"+tears+".png"
                if cheeks and symbol not in cheeks:
                    self.face['cheeks'][0] = imagepath+"extras/"+cheeks+".png"
                if eyebrows and symbol not in eyebrows:
                    self.face['eyebrows'][0] = imagepath+"brow/"+eyebrows+".png"
                if eyes and symbol not in eyes:
                    self.face['eyes'][0] = imagepath+"eyes/"+eyes+".png"
                if pupils and symbol not in pupils:
                    self.face['pupils'][0] = imagepath+"pupil/"+pupils+".png"
                if whites and symbol not in whites:
                    self.face['whites'][0] = imagepath+"eyes/"+whites+".png"
                if mouth and symbol not in mouth:
                    self.face['mouth'][0] = imagepath+"mouth/"+mouth+".png"
            if 'other' in args:
                imagepath = "characters/emotes/"
                
                emote = self.get_object(self.other, 'emote')
                cum = self.get_object(self.other, 'cum')
                
                if emote and symbol not in emote:
                    self.other['emote'][0] = imagepath+emote+".png"
                    
                imagepath = "characters/"+self.char+"/cum/"
                
                if cum and symbol not in cum:
                    self.other['cum'][0] = imagepath+cum+".png"
            self.cached = False
            
        def expression(self, **kwargs):
            for arg, value in kwargs.iteritems():
                try:
                    self.face[str(arg)][0] = value
                except KeyError:
                    raise Exception('Character: "'+str(arg)+'" expression type was not defined for "'+self.char+'" character class.')

            self.update_paths("face")
            self.cached = False
            
        def special(self, **kwargs):
            for arg, value in kwargs.iteritems():
                try:
                    self.other[str(arg)][0] = value
                except KeyError:
                    raise Exception('Character: "'+str(arg)+'" other type was not defined for "'+self.char+'" character class.')

            self.update_paths("other")
            self.cached = False
            
        def equip(self, **kwargs):
            for arg, value in kwargs.iteritems():
                try:
                    self.clothing[str(arg)][0] = value
                    self.clothing[str(arg)][4] = False
                except KeyError:
                    raise Exception('Character: "'+str(arg)+'" clothing type was not defined for "'+self.char+'" character class.')
            self.cached = False
            
        def unequip(self, *args):
            for arg in args.iteritems():
                try:
                    self.clothing[str(arg)][0] = None
                except KeyError:
                    raise Exception('Character: "'+str(arg)+'" clothing type was not defined for "'+self.char+'" character class.')
            self.cached = False
            
        def strip(self, *args):
            if 'all' in args:
                for key in self.clothing:
                    self.clothing[key][4] = True
            else:
                for arg in args:
                    try:
                        self.clothing[str(arg)][4] = True
                    except KeyError:
                        raise Exception('Character: "'+str(arg)+'" clothing type was not defined for "'+self.char+'" character class.')
            self.cached = False
            
        def wear(self, *args):
            if 'all' in args:
                for key in self.clothing:
                    self.clothing[key][4] = False
            else:
                for arg in args:
                    try:
                        self.clothing[str(arg)][4] = False
                    except KeyError:
                        raise Exception('Character: "'+str(arg)+'" clothing type was not defined "'+self.char+'" character class.')
            self.cached = False
                
        def say(self, string, **kwargs):
            if kwargs:
                self.expression(**kwargs)
            if string:
                renpy.say(self.char, string)
            
        def get_image(self):
            if not self.cached or self.cache_override:                
                self.cached = True
                
                # Keep character images in cache
                renpy.start_predict("characters/"+self.char+"/body/*.*")
                renpy.start_predict("characters/"+self.char+"/face/*.*")
                
                # Create sprite list
                sprite_list = []
                
                # Add body to sprite list
                for key, value in self.body.iteritems():
                    if self.body[key][0] and not self.body[key][4]:
                        sprite_list.append(value)
                        
                # Add face to sprite list
                for key, value in self.face.iteritems():
                    if self.face[key][0] and not self.face[key][4]:
                        sprite_list.append(value)
                
                # Add other to sprite list        
                for key, value in self.other.iteritems():
                    if self.other[key][0] and not self.other[key][4]:
                        sprite_list.append(value)
                        
                # Add clothing to sprite list        
                for key, value in self.clothing.iteritems():
                    if self.clothing[key][0] and not self.clothing[key][4]:
                        sprite_list.append(value)
                        
                # Sort sprite list by zorder
                sprite_list.sort(key=lambda x: x[1], reverse=False)
                
                # Build image
                self.sprite = Image("characters/dummy.png")
                if sprite_list:
                    for sprite in sprite_list:
                        # Check if sprite is an imagepath or an object
                        if isinstance(sprite[0], basestring):
                            self.sprite = Composite(
                                    (1010, 1200),
                                    (0,0), self.sprite,
                                    (sprite[2],sprite[3]), Image(sprite[0]))
                        else:
                            self.sprite = Composite(
                                    (1010, 1200),
                                    (0,0), self.sprite,
                                    (sprite[2],sprite[3]), sprite[0].get_image())
            return self.sprite