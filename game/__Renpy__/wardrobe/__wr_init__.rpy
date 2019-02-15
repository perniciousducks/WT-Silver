

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
        $ cho_class.top.set_color(_return[1])
        hide screen cloth_test
    elif _return == "reset":
        $ cho_class.top.reset_color()

    jump color_cloth_test


screen cloth_test:
    python:
        if not color_preview == None:
            cho_class.top.color[active_layer] = color_preview

    zorder 100
    add cho_class.get_image() xpos 700 yalign 0.5 zoom 0.5 xanchor 0.5 yanchor 0.5

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
    if cho_wear_bra:
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
    
    
    
    
    
    $ cho_class = char_class(   char="cho", 
                                head="ponytail_blue", 
                                arms="arm_down_l", 
                                breasts="breasts_bikini_tan", 
                                base="base_01", 
                                legs="blank",
                                mouth="base",
                                eyes="base",
                                eyebrows="base",
                                pupils="mid",
                                cheeks="blank",
                                tears="blank",
                                extras="blank",
                                emote="blank",
                                top=cho_top_school_CLOTH, 
                                bottom=t_cho_bottom, 
                                bra=t_cho_bra, 
                                panties=t_cho_panties)
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

        imagepath = ""

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
            return self.imagepath+self.id+"/"+str(layer)+".png"
                    
        def get_image(self):
            self.sprite = Image(self.skinlayer)

            for i in xrange(0, self.layers):
                    self.sprite = Composite(
                           (1010, 1200),
                           (0,0), self.sprite,
                           (0,0), im.MatrixColor(str(self.get_imagelayer(i)), self.get_matrixcolor(i)))
            return self.sprite
            
    class char_class(object):
        char = None
        pose = None
        
        # Clothing, accessory & tattoos
        hat = None
        neckwear = None
        badge = None
        robe = None
        gloves = None
        top = None
        bra = None
        belt = None
        bottom = None
        garter = None
        panties = None
        stockings = None
        
        body_accessory = []
        accessory = []
        tattoo = []
        
        # Body
        head = None
        arms = None
        breasts = None
        base = None
        legs = None
        
        # Face
        mouth = None
        eyes = None
        eyebrows = None
        pupils = None
        cheeks = None
        tears = None
        extras = None
        emote = None
        
        # Flags
        stripped = False
        
        imagepath = ""
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
            
            if self.char == None:
                raise Exception('Character: "char" was not defined in char_class.')
                
            if self.head == None:
                raise Exception('Character: "head" was not defined in char_class.\n Or should I say, characters head is missing. :P')
                
            if self.arms == None:
                raise Exception('Character: "arms" was not defined in char_class.')
                
            if self.breasts == None:
                raise Exception('Character: "breasts" was not defined in char_class.\n Error 404, boobs not found.')
                
            if self.base == None:
                raise Exception('Character: "base" was not defined in char_class.')
                
            if self.legs == None:
                raise Exception('Character: "legs" was not defined in char_class.\nLEGS, MY LEGS AAAAAAAAAA!!!!')
            
            # Init body
            self.imagepath = "characters/"+self.char+"/body/"
            
            self.head = self.imagepath+"/head/"+self.head+".png"
            self.arms = self.imagepath+"/arms/"+self.arms+".png"
            self.breasts = self.imagepath+"/breasts/"+self.breasts+".png"
            self.base = self.imagepath+"/base/"+self.base+".png"
            self.legs = self.imagepath+"/legs/"+self.legs+".png" # Some characters are missing legs images
            
            # Init face
            self.imagepath = "characters/"+self.char+"/face/"
            
            self.mouth = self.imagepath+"/mouth/"+self.mouth+".png"
            self.whites = self.imagepath+"/eyes/_white_.png" # Is it really needed?
            self.eyes = self.imagepath+"/eyes/"+self.eyes+".png"
            self.eyebrows = self.imagepath+"/brow/"+self.eyebrows+".png"
            self.pupils = self.imagepath+"/pupil/"+self.pupils+".png"
            self.cheeks = self.imagepath+"/extras/"+self.cheeks+".png"
            self.tears = self.imagepath+"/extras/"+self.tears+".png"
            self.extras = self.imagepath+"/extras/"+self.extras+".png"
            self.emote = "characters/emotes/"+self.emote+".png"
            
        def face(self, **kwargs):
            self.imagepath = "characters/"+self.char+"/face/"
            
            if len(kwargs) <= 0:
                self.mouth = self.imagepath+"/mouth/base.png"
                self.eyes = self.imagepath+"/eyes/base.png"
                self.eyebrows = self.imagepath+"/brow/base.png"
                self.pupils = self.imagepath+"/pupil/mid.png"
                self.cheeks = "characters/dummy.png"
                self.tears = "characters/dummy.png"
                self.extras = "characters/dummy.png"
                self.emote = "characters/dummy.png"
            else:
                self.__dict__.update(**kwargs)
            
                if 'mouth' in kwargs:
                    self.mouth = self.imagepath+"/mouth/"+self.mouth+".png"
                
                if 'eyes' in kwargs:
                    self.eyes = self.imagepath+"/eyes/"+self.eyes+".png"
                
                if 'eyebrows' in kwargs:
                    self.eyebrows = self.imagepath+"/brow/"+self.eyebrows+".png"
                
                if 'pupils' in kwargs:
                    self.pupils = self.imagepath+"/pupil/"+self.pupils+".png"
            
                if 'cheeks' in kwargs:
                    self.cheeks = self.imagepath+"/extras/cheeks_"+self.cheeks+".png"
                
                if 'tears' in kwargs:
                    self.tears = self.imagepath+"/extras/tears_"+self.tears+".png"
                
                if 'extras' in kwargs:
                    self.extras = self.imagepath+"/extras/"+self.extras+".png"
                
                if 'emote' in kwargs:
                    self.emote = "characters/emotes/"+self.emote+".png"
            
        def strip(self, **kwargs):
            if len(kwargs) <= 0:
                self.hat = None
                self.neckwear = None
                self.badge = None
                self.robe = None
                self.gloves = None
                self.top = None
                self.bra = None
                self.belt = None
                self.bottom = None
                self.garter = None
                self.panties = None
                self.stockings = None
            else:
                self.__dict__.update(**kwargs)
                
        def toggle_clothes(self):
            self.stripped = not self.stripped
            
        def say(self, string, **kwargs):
            if len(kwargs) > 0:
                self.face(**kwargs)
                
            renpy.say(self.char, string)
            
        def get_image(self):
            self.sprite = Composite(
                    (1010, 1200),
                    (0,0), self.legs,
                    (0,0), self.base,
                    (0,0), self.breasts,
                    (0,0), self.arms,
                    (0,0), self.head)
            self.sprite = Composite(
                    (1010, 1200),
                    (0,0), self.sprite,
                    (0,0), self.mouth,
                    (0,0), self.whites,
                    (0,0), self.eyes,
                    (0,0), self.eyebrows,
                    (0,0), self.pupils,
                    (0,0), self.cheeks,
                    (0,0), self.tears,
                    (0,0), self.extras,
                    (0,0), self.emote)
            if len(self.tattoo) > 0:
                for i in xrange(0, len(tattoo)):
                    self.sprite = Composite(
                            (1010, 1200),
                            (0,0), self.sprite,
                            (0,0), self.tattoo[i].get_image())
            if len(self.body_accessory) > 0:
                for i in xrange(0, len(body_accessory)):
                    self.sprite = Composite(
                            (1010, 1200),
                            (0,0), self.sprite,
                            (0,0), self.body_accessory[i].get_image())
            if not self.stripped:
                if not self.stockings == None:                    
                    self.sprite = Composite(
                        (1010, 1200),
                        (0,0), self.sprite,
                        (0,0), self.stockings.get_image())
                if not self.panties == None:
                    self.sprite = Composite(
                        (1010, 1200),
                        (0,0), self.sprite,
                        (0,0), self.panties.get_image())
                if not self.garter == None:
                    self.sprite = Composite(
                        (1010, 1200),
                        (0,0), self.sprite,
                        (0,0), self.garter.get_image())
                if not self.bottom == None:
                    self.sprite = Composite(
                        (1010, 1200),
                        (0,0), self.sprite,
                        (0,0), self.bottom.get_image(),
                        (0,0), self.arms) # Arm fix
                if not self.belt == None:
                    self.sprite = Composite(
                        (1010, 1200),
                        (0,0), self.sprite,
                        (0,0), self.belt.get_image())
                if not self.bra == None:
                    self.sprite = Composite(
                        (1010, 1200),
                        (0,0), self.sprite,
                        (0,0), self.bra.get_image())
                if not self.top == None:
                    self.sprite = Composite(
                        (1010, 1200),
                        (0,0), self.sprite,
                        (0,0), self.top.get_image())
                if not self.gloves == None:
                    self.sprite = Composite(
                        (1010, 1200),
                        (0,0), self.sprite,
                        (0,0), self.gloves.get_image())
                if not self.robe == None:
                    self.sprite = Composite(
                        (1010, 1200),
                        (0,0), self.sprite,
                        (0,0), self.robe.get_image())
                if not self.neckwear == None:
                    self.sprite = Composite(
                        (1010, 1200),
                        (0,0), self.sprite,
                        (0,0), self.neckwear.get_image())
                if not self.hat == None:
                    self.sprite = Composite(
                        (1010, 1200),
                        (0,0), self.sprite,
                        (0,0), self.hat.get_image())
            return self.sprite