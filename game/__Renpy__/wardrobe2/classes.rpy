init python:
    def get_character_object(key):
        return character_list.get(key)
            
    def set_clipboard(txt):
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, txt.encode("utf-8"))
        
    def get_clipboard():
        clipboard = pygame.scrap.get(pygame.scrap.SCRAP_TEXT)
        if clipboard:
            return clipboard
        return None
        
    def evaluate(txt):
        return __import__('ast').literal_eval(txt)
            
    class outfit_class(object):
        
        def __init__(self, **kwargs):
            self.name = None
            self.price = 0
            self.desc = ""
            self.unlocked = False
            self.group = []
            self.cached = False
            
            self.sprite = "empty"
            self.__dict__.update(**kwargs)
            
            if self.name == None:
                raise Exception('Outfit: "name" was not defined in outfit_class.')
            
            if self.group < 1:
                raise Exception('Outfit: "group" list was not defined in outfit_class.')
            
            if self.unlocked:
                # Unlock outfit object properly using unlock method
                self.unlocked = False
                self.unlock()
                
        def outfit_export(self, tofile=True, filename="exported"):
            exported = [self.group[0].char]
            
            for item in self.group:
                exported.append([item.id, item.color])
                
            if tofile:
                renpy.screenshot(config.basedir+"/game/outfits/"+filename+".png")
                img = pygame.image.load(config.basedir+"/game/outfits/"+filename+".png")
                img = pygame.transform.smoothscale(img, (1080, 600))
                subsurface = img.subsurface((384, 63, 309, 470))
                pygame.image.save(subsurface, config.basedir+"/game/outfits/"+filename+".png")
                _image_payload.encode(filename, str(exported))
                #export_file = open(config.basedir+"/game/"+filename+".txt", "w")
                #export_file.write(str(exported))
                #export_file.close()
            else:
                set_clipboard(str(exported))
            renpy.show_screen("popup_window", "Export successful!")
        
        def outfit_import(self, fromfile=True, filename="exported"):            
            imported = None
            group = []
            
            if fromfile:
                try:
                    #import_file = open(config.basedir+"/game/"+filename+".txt", "r")
                    #imported = import_file.read()
                    #import_file.close()
                    if renpy.loadable("/outfits/"+filename+".png"):
                        imported = _image_payload.decode(filename)
                    else:
                        renpy.block_rollback()
                        return (False, renpy.show_screen("popup_window", "File doesn't exist!"))
                except:
                    if _image_payload._file:
                        _image_payload._file.close()
                    renpy.block_rollback()
                    return (False, renpy.show_screen("popup_window", "Corrupted file!"))
            else:
                imported = get_clipboard()
            
            if imported != "":
                try:
                    imported = evaluate(imported)
                except:
                    renpy.block_rollback()
                    return (False, renpy.show_screen("popup_window", "Corrupted file!"))

                for item in imported:
                    if not isinstance(item, basestring):
                        for object in character_clothes_list:
                            if item[0] == object.id:
                                if object.char == char_active.char:
                                    if not cheats_active:
                                        if not object.unlocked:
                                            renpy.block_rollback()
                                            return (False, renpy.show_screen("popup_window", "Items locked!"))
                                    item[0] = object.clone()
                                    item[0].color = item[1]
                                    item[0].cached = False
                                    group.append(item[0])
                if len(group) > 0:
                    renpy.show_screen("popup_window", "Import successful!")     
                    renpy.block_rollback()
                    return outfit_class(name="", desc="", unlocked=True, group=group)
            renpy.block_rollback()
            return (False, renpy.show_screen("popup_window", "Import failed!"))
                    
        def unlock(self):
            if not self.unlocked:
                self.unlocked = True
                get_character_object(self.group[0].char).outfits.append(self)
                # Mark each clothing piece from the group as unlocked/locked by default
                for item in self.group:
                    item.unlock()
            
        def save(self):
            char = self.group[0].char
            self.group = []
            clothing = get_character_object(char).clothing
            for key in clothing:
                if not clothing[key][0] == None:
                    self.group.append(clothing[key][0])
            self.cached = False
            return
                
        def get_image(self):
            if not self.cached:
                self.cached = True
                # Create sprite list
                sprite_list = []
                
                char = get_character_object(self.group[0].char)
                
                # Add body to sprite list
                body = char.get_bodyparts()
                for i in xrange(len(body)):
                    item = [body[i][0], body[i][1]]
                    sprite_list.append(item)
                
                # Add clothing to sprite list
                for i in xrange(len(self.group)):
                    item = [self.group[i], char.clothing[self.group[i].type][1]]
                    sprite_list.append(item)
                    sprite_list.append([self.group[i].get_skin(), 5])
                    
                    if self.group[i].bodyfix != None:
                        for k, v in self.group[i].bodyfix.iteritems():
                            sprite_list = [v if isinstance(x[0], basestring) and k in x[0] else x for x in sprite_list]
                            
                    if self.group[i].layerfix != {}:
                        for k, v in self.group[i].layerfix.iteritems():
                            if k == "outline_above":
                                sprite_list.append([v[0], 150])
                            elif k == "outline_below":
                                sprite_list.append([v[0], -150])
                            else:
                                if v[1] == 1:
                                    sprite_list.append([self.group[i].get_layerfix(k), 100+k])
                                else:
                                    sprite_list.append([self.group[i].get_layerfix(k), -100+k])
                        
                # Sort sprite list by zorder based on character clothing zorder
                sprite_list.sort(key=lambda x: x[1], reverse=False)

                # Armfix
                armfix = []
                
                # Build image
                self.sprite = Image("characters/dummy.png")
                for sprite in sprite_list:                        
                    if isinstance(sprite[0], basestring):
                        self.sprite = Composite(
                                (1010, 1200),
                                (0,0), self.sprite,
                                (0,0), im.MatrixColor(Image(sprite[0]), im.matrix.desaturate()))
                    elif isinstance(sprite[0], (im.Image, im.MatrixColor)):
                        self.sprite = Composite(
                                (1010, 1200),
                                (0,0), self.sprite,
                                (0,0), Image(sprite[0]))
                    else:
                        self.sprite = Composite(
                                (1010, 1200),
                                (0,0), self.sprite,
                                (0,0), sprite[0].get_image())
                                    
                        if sprite[0].armfix:
                            # add fixes WITH a hand image
                            if armfix == []:
                                armfix.append(sprite[0].get_armfix(True, False)[0]) # Lefthand
                                armfix.append(sprite[0].get_armfix(True, False)[1]) # Righthand
                            else:
                                # add fixes WITHOUT hand image
                                armfix.append(sprite[0].get_armfix(True, True)[0]) # L
                                armfix.append(sprite[0].get_armfix(True, True)[1]) # R
                    
                if armfix > 0:
                    for item in armfix:
                        self.sprite = Composite(
                            (1010, 1200),
                            (0,0), self.sprite,
                            (0,0), item)
            return self.sprite
            
            
    class cloth_class(object):

        def __init__(self, **kwargs):
            self.char = None # astoria, cho, hermione, luna, susan, tonks
            self.category = None
            self.subcat = None
            self.type = None
            self.id = None
            self.layers = None
            self.color = []
            self.color_default = []
            self.skinlayer = "characters/dummy.png"
            self.extralayer = "characters/dummy.png"
            self.overlayer = "characters/dummy.png"
            self.outline = None
            self.unlocked = True
            self.cloned = False
            self.cached = False
            self.zorder = None # None - use pre-defined zorder, int - object zorder
            
            self.bodyfix = None
            self.incompatible = None
            self.mask = None
            
            self.layerfix = {}
            
            self.armfix = False
            self.armfix_L = []
            self.armfix_Lx = ""
            self.armfix_R = []
            self.armfix_Rx = ""
            
            self.sprite_ico = None

            self.name = ""
            self.desc = ""
            self.whoring = 0
            
            self.pose = ""

            self.imagepath = ""
            
            self.__dict__.update(**kwargs)
            
            if self.char == None:
                raise Exception('Clothing: "char" was not defined in cloth_class.')
                
            if self.category == None:
                raise Exception('Clothing: "category" was not defined in cloth_class.')
                
            if self.subcat == None:
                raise Exception('Clothing: "subcat" was not defined in cloth_class.')
                
            if self.type == None:
                raise Exception('Clothing: "type" was not defined in cloth_class.')
                
            if self.id == None:
                raise Exception('Clothing: "id" was not defined in cloth_class.')
                
            if self.layers == None:
                raise Exception('Clothing: "layers" number was not defined in cloth_class.')
                
            if len(self.color) < self.layers:
                for i in xrange(len(self.color), self.layers):
                    self.color.append([255, 255, 255, 255])
                    
            for i in xrange(len(self.color)):
                self.color_default.append(list(self.color[i]))
                
            if self.layers != len(self.color):
                raise Exception('Clothing: "color" list does not match the number of layers in cloth_class.')
            
            # Check if clothing folder is a category, subcategory or a type
            if renpy.loadable("characters/"+self.char+"/clothes/"+self.category+"/"+self.id+"/0.png"):
                self.imagepath = "characters/"+self.char+"/clothes/"+self.category+"/"+self.id+"/"
            elif renpy.loadable("characters/"+self.char+"/clothes/"+self.subcat+"/"+self.id+"/0.png"):
                self.imagepath = "characters/"+self.char+"/clothes/"+self.subcat+"/"+self.id+"/"
            else:
                self.imagepath = "characters/"+self.char+"/clothes/"+self.type+"/"+self.id+"/"
            
            # Check if skin layer exists
            if renpy.loadable(self.imagepath+"skin.png"):
                self.skinlayer = self.imagepath+"skin.png"
            
            # Check if extra layer exists
            if renpy.loadable(self.imagepath+"extra.png"):
                self.extralayer = self.imagepath+"extra.png"
                
            if renpy.loadable(self.imagepath+"overlay.png"):
                self.overlayer = self.imagepath+"overlay.png"
                
            if renpy.loadable(self.imagepath+"mask.png"):
                self.mask = self.imagepath+"mask.png"
                
            # Check if bodyfix exists
            if self.bodyfix != None and not self.cloned:
                imagepath = "characters/"+self.char+"/body/"
                
                for key, value in self.bodyfix.iteritems():
                    if key in ("armleft", "armright", "handleft", "handright"):
                        self.bodyfix[key][0] = imagepath+"arms/"+value[0]+".png"
                    else:
                        self.bodyfix[key][0] = imagepath+key+"/"+value[0]+".png"
                
            # Check if armfix layers exist
            self.set_armfix()
            
            self.set_layerfix()
            
            # Set outline layer path
            self.outline = self.imagepath+"outline.png"

            if not self.cloned:
                if self.unlocked:
                    # Unlock cloth object properly using unlock method
                    self.unlocked = False
                    self.unlock()
                
                # Add cloth object to a stored list
                if not hasattr(renpy.store, 'character_clothes_list'):
                    renpy.store.character_clothes_list = []
                renpy.store.character_clothes_list.append(self)
            
            # Initialize icon crop calculations A.K.A threading A.k.A lazyload
            layers = [] # This is NOT a class variable
            for i in xrange(self.layers):
                layers.append(self.get_imagelayer(i))
            layers.append(self.extralayer)
            layers.append(self.outline)
                
            self.sprite_ico = lazyload(layers, self.color, self.layers+1, self.layers)
                
        def unlock(self):
            if not self.unlocked:
                self.unlocked = True
                # Add cloth object to the character's clothing data
                get_character_object(self.char).clothing_dictlist.setdefault(self.category, {}).setdefault(self.subcat, []).append(self)
            
        def clone(self):
            color = []
            for c in self.color:
                color.append(list(c))
            return cloth_class(char=self.char, category=self.category, subcat=self.subcat, type=self.type, id=self.id, layers=self.layers, color=color, unlocked=self.unlocked, cloned=True, name=self.name, desc=self.desc, armfix=self.armfix, layerfix=self.layerfix, whoring=self.whoring, bodyfix=self.bodyfix, incompatible=self.incompatible, mask=self.mask, zorder=self.zorder)
                
        def set_pose(self, pose):
            if pose == None:
                self.pose = ""
                self.outline = self.imagepath+"outline.png"
                if renpy.loadable(self.imagepath+"skin.png"):
                    self.skinlayer = self.imagepath+"skin.png"
                else:
                    self.skinlayer = "characters/dummy.png"
                if renpy.loadable(self.imagepath+"extra.png"):
                    self.extralayer = self.imagepath+"extra.png"
                else:
                    self.extralayer = "characters/dummy.png"
                if renpy.loadable(self.imagepath+"overlay.png"):
                    self.overlayer = self.imagepath+"overlay.png"
                else:
                    self.overlayer = "characters/dummy.png"
                if renpy.loadable(self.imagepath+"mask.png"):
                    self.mask = self.imagepath+"mask.png"
                else:
                    self.mask = None
                self.set_armfix()
                self.cached = False
                return None
            if renpy.loadable(self.imagepath+"/"+pose+"/0.png"):
                self.pose = pose
                self.outline = self.imagepath+"/"+pose+"/outline.png"
                if renpy.loadable(self.imagepath+"/"+pose+"/skin.png"):
                    self.skinlayer = self.imagepath+"/"+pose+"/skin.png"
                else:
                    self.skinlayer = "characters/dummy.png"
                if renpy.loadable(self.imagepath+"/"+pose+"/extra.png"):
                    self.extralayer = self.imagepath+"/"+pose+"/extra.png"
                else:
                    self.extralayer = "characters/dummy.png"
                if renpy.loadable(self.imagepath+"/"+pose+"/overlay.png"):
                    self.overlayer = self.imagepath+"/"+pose+"/overlay.png"
                else:
                    self.overlayer = "characters/dummy.png"
                self.set_armfix(True)
                self.cached = False
                return True
            return False
            
        def set_layerfix(self, anim=False):
            pose = self.pose
            if anim:
                pose += "/"+self.pose+"/"
                
            self.layerfix = {}
            for layer in xrange(self.layers):
                # Coloured Layer above all else
                if renpy.loadable(self.imagepath+pose+str(layer)+"_above.png"):
                    self.layerfix[layer] = [self.imagepath+pose+str(layer)+"_above.png", 1]
                    
                # Coloured Layer below all else
                if renpy.loadable(self.imagepath+pose+str(layer)+"_below.png"):
                    self.layerfix[layer] = [self.imagepath+pose+str(layer)+"_below.png", 0]
                    
            if renpy.loadable(self.imagepath+pose+"outline_above.png"):
                self.layerfix['outline_above'] = [self.imagepath+pose+"outline_above.png", 2]
                
            if renpy.loadable(self.imagepath+pose+"outline_below.png"):
                self.layerfix['outline_below'] = [self.imagepath+pose+"outline_below.png", 2]
            return
            
        def set_armfix(self, anim=False):
            pose = self.pose
            if anim:
                pose += "/"+self.pose+"/"
                
            self.armfix_L = []
            self.armfix_R = []
            if self.armfix:
                for layer in xrange(self.layers):
                    if renpy.loadable(self.imagepath+pose+str(layer)+"_armL.png"):
                        self.armfix_L.append(self.imagepath+pose+str(layer)+"_armL.png")
                        
                    if renpy.loadable(self.imagepath+pose+str(layer)+"_armR.png"):
                        self.armfix_R.append(self.imagepath+pose+str(layer)+"_armR.png")
                        
                if renpy.loadable(self.imagepath+pose+"outline_armL.png"):
                    self.armfix_Lx = self.imagepath+pose+"outline_armL.png"
                else:
                    self.armfix_Lx = ""
                    
                if renpy.loadable(self.imagepath+pose+"outline_armR.png"):
                    self.armfix_Rx = self.imagepath+pose+"outline_armR.png"
                else:
                    self.armfix_Rx = ""
            return

        def get_matrixcolor(self, layer):
            return im.matrix.tint(float(self.color[layer][0])/255.0, float(self.color[layer][1])/255.0, float(self.color[layer][2])/255.0)

        def get_color(self, layer):
            return (float(self.color[layer][0])/255.0, float(self.color[layer][1])/255.0, float(self.color[layer][2])/255.0, float(self.color[layer][3])/255.0)
            
        def get_color_hex(self, layer):
            return '#%02x%02x%02x' % (self.color[layer][0], self.color[layer][1], self.color[layer][2])

        def get_alpha(self, layer):
            return self.color[layer][3]/255.0
            
        def set_color_alt(self, l):
            for i in xrange(len(l)):
                self.color[i] = list(l[i])
            self.sprite_ico.cached = False
            self.cached = False

        def set_color(self, layer):
            if config.developer or cheat_wardrobe_alpha:
                if self.type != "hair":
                    self.color[layer] = color_picker(self.color[layer], True, "Cloth layer "+str(layer+1), pos_xy=[20, 130])
                else:
                    self.color[layer] = color_picker(self.color[layer], False, "Cloth layer "+str(layer+1), pos_xy=[20, 130])
            else:
                self.color[layer] = color_picker(self.color[layer], False, "Cloth layer "+str(layer+1), pos_xy=[20, 130])
            self.sprite_ico.cached = False
            self.cached = False
            
        def reset_color(self):
            for i in xrange(len(self.color)):
                self.color[i] = list(self.color_default[i])
            self.sprite_ico.cached = False
            self.cached = False
        
        def get_imagelayer(self, layer):
            return self.imagepath+str(layer)+".png" if self.pose == "" else self.imagepath+"/"+self.pose+"/"+str(layer)+".png"

        def get_imagelayer_color(self, layer):
            return im.MatrixColor(self.get_imagelayer(layer), self.get_matrixcolor(layer) * im.matrix.opacity(self.get_alpha(layer)))
            
        def get_skin(self):
            return self.skinlayer
                    
        def get_image(self):
            
            # Keep used clothes images in cache
            #renpy.start_predict(self.imagepath)
            
            self.sprite = self.get_imagelayer_color(0)
            
            for i in xrange(1, self.layers):
                self.sprite = Composite(
                       (1010, 1200),
                       (0,0), self.sprite,
                       (0,0), self.get_imagelayer_color(i))
                       
            self.sprite = Composite(
                    (1010, 1200),
                    (0,0), self.sprite,
                    (0,0), self.extralayer,
                    (0,0), self.outline,
                    (0,0), self.overlayer)
            return self.sprite
            
        def get_armfix(self, skingray=False, nohand=False):
            armL = Image("characters/"+self.char+"/body/arms/armfixL.png")
            armR = Image("characters/"+self.char+"/body/arms/armfixR.png")
            
            if nohand or self.pose != "":
                armL = Image("characters/dummy.png")
                armR = Image("characters/dummy.png")
            
            # Used in mannequin generation
            if skingray:
                armL = im.MatrixColor(armL, im.matrix.desaturate())
                armR = im.MatrixColor(armR, im.matrix.desaturate())
            
            # Add armfix with proper colors
            if self.armfix_L > 0:
                for i in xrange(len(self.armfix_L)):
                    armL = Composite(
                           (1010, 1200),
                           (0,0), armL,
                           (0,0), im.MatrixColor(self.armfix_L[i], self.get_matrixcolor(i)))
                           
            if self.armfix_R > 0:
                for i in xrange(len(self.armfix_R)):
                    armR = Composite(
                           (1010, 1200),
                           (0,0), armR,
                           (0,0), im.MatrixColor(self.armfix_R[i], self.get_matrixcolor(i)))
                       
            # Add armfix outline    
            if self.armfix_Lx != "":
                armL = Composite(
                        (1010, 1200),
                        (0,0), armL,
                        (0,0), self.armfix_Lx)
                        
            if self.armfix_Rx != "":
                armR = Composite(
                        (1010, 1200),
                        (0,0), armR,
                        (0,0), self.armfix_Rx)
            return (armL, armR)
            
        def get_layerfix(self, layer):
            return Image(im.MatrixColor(self.layerfix[layer][0], self.get_matrixcolor(layer) * im.matrix.opacity(self.get_alpha(layer))))
            
        def get_icon(self):
            return self.sprite_ico.get_image()
            
    class char_class(object):

        def __init__(self, **kwargs):
            self.char = None
            
            self.stats = stats_class() # Initialize stats object instance
            
            self.cached = False
            self.cache_override = False
            
            self.body = {}
            self.face = {}
            self.clothing = {}
            self.clothing_dictlist = {}
            self.outfits = []
            self.other = {}
            
            self.incompatible_wardrobe = []
            
            self.pose = ""
            
            self.sprite = "empty"
            self.mannequin_sprite = None

            self.__dict__.update(**kwargs)
            
            if self.char == None:
                raise Exception('Character: "char" was not defined in char_class.')
            
            # Add a pointer to a global var
            globals()[self.char+'_stats'] = self.stats

            # Add the character to a stored list
            if not hasattr(renpy.store, 'character_list'):
                renpy.store.character_list = {}
            renpy.store.character_list.update({self.char: self})
                
        def get_object(self, dict, key):
            return dict.get(key)[0]
            
        def update_zorder(self, layer, value):
            try:
                self.clothing[layer][1] = value
                self.cached = False
                return layer+" zorder changed to "+str(value)
            except KeyError:
                return 'Warning: layer "'+str(layer)+'" not found.'
            
        def update_paths(self, *args):
            symbol = "/"
            
            if 'body' in args:
                imagepath = "characters/"+self.char+"/body/"
                
                for key, value in self.body.iteritems():
                    if value[0] != None and not symbol in value[0]:
                        if key in ("armleft", "armright", "handleft", "handright"):
                            self.body[key][0] = imagepath+"arms/"+value[0]+".png"
                        else:
                            self.body[key][0] = imagepath+key+"/"+value[0]+".png"
            if 'face' in args:
                imagepath = "characters/"+self.char+"/face/"
                
                for key, value in self.face.iteritems():
                    if value[0] != None and not symbol in value[0]:
                        if key in ("tears", "cheeks"):
                            self.face[key][0] = imagepath+"extras/"+value[0]+".png"
                        elif key == "whites":
                            self.face[key][0] = imagepath+"eyes/"+value[0]+".png"
                        else:
                            self.face[key][0] = imagepath+key+"/"+value[0]+".png"
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
                if value:
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
            
        def set_body(self, **kwargs):
            for arg, value in kwargs.iteritems():
                try:
                    self.body[str(arg)][0] = value
                    self.body[str(arg)][4] = False
                except KeyError:
                    raise Exception('Character: "'+str(arg)+'" body part was not defined for "'+self.char+'" character class.')
            self.update_paths("body")
            self.cached = False
            return
            
        def set_pose(self, pose, offset):
            if not pose == None:
                self.pose = pose
                for key, value in self.body.iteritems():
                    self.body[key][4] = True
                for key, value in self.face.iteritems():
                    self.face[key][2] = offset[0]
                    self.face[key][3] = offset[1]
                self.body['animation'][0] = pose
                self.body['animation'][4] = False
            else:
                self.pose = ""
                for key, value in self.body.iteritems():
                    self.body[key][4] = False
                for key, value in self.face.iteritems():
                    self.face[key][2] = 0
                    self.face[key][3] = 0
                self.body['animation'][0] = None
            self.update_paths("body")
            self.cached = False
            
        def animation(self, anim, offset=(0,0)):
            for key, value in self.clothing.iteritems():
                if self.clothing[key][0]:
                    if self.clothing[key][0].set_pose(anim) == False:
                        self.clothing[key][4] = True
                    else:
                        self.clothing[key][4] = False
            self.set_pose(anim, offset)
            self.cached = False
            
        def get_cloth(self, type):
            return self.get_object(self.clothing, type)
            
        def get_category_list(self, category):
            return self.clothing_dictlist.get(category)
            
        def get_clothing_list(self, category, subcategory):
            return self.clothing_dictlist.get(category).get(subcategory)
            
        def get_equipped(self, category, subcategory, item=0):
            if not self.get_cloth(self.get_clothing_list(category, subcategory)[item].type) == None:
                return self.get_cloth(self.get_clothing_list(category, subcategory)[item].type).id
            return None
            
        def get_score(self):
            score = 0
            for key, item in self.clothing.iteritems():
                if item[0] != None:
                    if not item[0].type in ("tattoo0", "tattoo1", "piercing0", "piercing1", "buttplug"):
                        score += item[0].whoring
                else:
                    if key == "top":
                        score += 30
                        if not self.get_worn("bra"):
                            score += 25
                            if self.get_worn("piercing1"):
                                score += 10
                            if self.get_worn("tattoo1"):
                                score += self.get_cloth("tattoo1").whoring
                    elif key == "bra" and self.get_worn("top"):
                        score += 10
                    elif key == "bottom":
                        score += 30
                        if self.get_worn("buttplug"):
                            score += 10
                        if not self.get_worn("panties"):
                            score += 25
                            if self.get_worn("buttplug"):
                                score += 25
                            if self.get_worn("piercing0"):
                                score += 10
                            if self.get_worn("tattoo0"):
                                score += self.get_cloth("tattoo0").whoring
                    elif key == "panties" and self.get_worn("bottom"):
                        score += 15
            return score
            
        def clothes_compatible(self, unequip=True):
            result = True
            for key in self.clothing:
                if self.clothing[key][0] != None and self.clothing[key][0].incompatible != None:
                    for item in self.clothing[key][0].incompatible:
                        if self.clothing[item][0] != None:
                            if unequip:
                                self.unequip(item)
                            result = False
            return result
            
        def reset_compatibility(self):
            self.incompatible_wardrobe = []
            for value in self.clothing.itervalues():
                if value[0] and value[0].incompatible != None:
                    for key in value[0].incompatible:
                        if key not in self.incompatible_wardrobe:
                            self.incompatible_wardrobe.append(key)
                        
        def get_cloth_object(self, category, subcat, id):
            for object in self.clothing_dictlist[category][subcat]:
                if object.id == id:
                    return object
            return None
            
        def equip(self, object):
            if isinstance(object, outfit_class):
                self.unequip("all")
                for item in object.group:
                    self.clothing[item.type][0] = self.get_cloth_object(item.category, item.subcat, item.id)
                    self.clothing[item.type][4] = False
                    self.clothing[item.type][0].set_color_alt(item.color)
                self.reset_compatibility()
            else:
                if self.clothing[object.type][0] == object and object.type != "hair":
                    self.unequip(object.type)
                else:
                    # Check if item is compatible with other clothing pieces  
                    if object.type not in self.incompatible_wardrobe:
                        if self.clothing[object.type][0] and self.clothing[object.type][0].incompatible != None:
                            for key in self.clothing[object.type][0].incompatible:
                                if key in self.incompatible_wardrobe:
                                    self.incompatible_wardrobe.remove(key)
                        if object.incompatible != None:
                            for key in object.incompatible:
                                # Unequip incompatible item types
                                if key not in self.incompatible_wardrobe:
                                    self.incompatible_wardrobe.append(key)
                                self.unequip(key)
                        self.clothing[object.type][0] = object
                        self.clothing[object.type][4] = False
            self.cached = False
            update_chibi_image(self.char)
            
        def unequip(self, *args):
            if 'all' in args:
                for key in self.clothing:
                    if not key == "hair":
                        self.clothing[key][0] = None
                self.incompatible_wardrobe = []
            else:
                for arg in args:
                    try:
                        if self.clothing[str(arg)][0] and self.clothing[str(arg)][0].incompatible != None:
                            for key in self.clothing[str(arg)][0].incompatible:
                                if key in self.incompatible_wardrobe:
                                    self.incompatible_wardrobe.remove(key)
                        self.clothing[str(arg)][0] = None
                    except KeyError:
                        raise Exception('Character: "'+str(arg)+'" clothing type was not defined for "'+self.char+'" character class.')
            self.cached = False
            update_chibi_image(self.char)
            
        def strip(self, *args):
            if 'all' in args:
                for key in self.clothing:
                    if not key in ("hair", "pubes", "piercing0", "piercing1", "piercing2", "piercing3", "piercing4", "makeup0",  "makeup1", "makeup2", "makeup3", "makeup4", "tattoo0", "tattoo1", "tattoo2", "tattoo3", "tattoo4"):
                        self.clothing[key][4] = True
            else:
                for arg in args:
                    if arg in ("makeup", "accessory", "piercing", "tattoo"):
                        for key in self.clothing.iterkeys():
                            if arg in key:
                                self.clothing[key][4] = True
                    else:
                        try:
                            self.clothing[str(arg)][4] = True
                        except KeyError:
                            raise Exception('Character: "'+str(arg)+'" clothing type was not defined for "'+self.char+'" character class.')
            self.cached = False
            update_chibi_image(self.char)
            
        def wear(self, *args):
            if 'all' in args:
                for key in self.clothing:
                    self.clothing[key][4] = False
            else:
                for arg in args:
                    if arg in ("makeup", "accessory", "piercing", "tattoo"):
                        for key in self.clothing.iterkeys():
                            if arg in key:
                                self.clothing[key][4] = False
                    else:
                        try:
                            self.clothing[str(arg)][4] = False
                        except KeyError:
                            raise Exception('Character: "'+str(arg)+'" clothing type was not defined for "'+self.char+'" character class.')
            self.cached = False
            update_chibi_image(self.char)
            
        def toggle_wear(self, type):
            if type in ("makeup", "accessory", "piercing", "tattoo"):
                for key in self.clothing.iterkeys():
                    if type in key:
                        self.clothing[key][4] = not self.clothing[key][4]
            else:
                try:
                    self.clothing[str(type)][4] = not self.clothing[str(type)][4]
                except KeyError:
                    raise Exception('Character: "'+str(type)+'" clothing type was not defined for "'+self.char+'" character class.')
            self.cached = False
            
        def get_worn(self, type):
            if type in ("makeup", "accessory", "piercing", "tattoo"):
                for key in self.clothing.iterkeys():
                    if type in key:
                        if self.clothing[key][0] and not self.clothing[key][4]:
                            return True
            else:
                if not self.clothing[type][0]:
                    return None
                if not self.clothing[type][4]:
                    return True
            return False

        def create_outfit(self, name, desc, unlock=True):
            clothes = []
            clothing = self.clothing
            for key in clothing:
                if not clothing[key][0] == None:
                    clothes.append(clothing[key][0].clone())
            return outfit_class(name=name, desc=desc, unlocked=unlock, group=clothes)
                
        def say(self, string, **kwargs):
            if kwargs:
                self.expression(**kwargs)
            if string:
                renpy.say(eval(self.char[:3]), string)
                
        def get_bodyparts(self):
            bodyparts = []
            for key, value in self.body.iteritems():
                if self.body[key][0]:
                    bodyparts.append(value) 
            return bodyparts
            
        def get_mannequin(self):
            if not self.mannequin_sprite:
                
                # Create sprite list
                sprite_list = []
                
                for key, value in self.body.iteritems():
                    if self.body[key][0] and not self.body[key][4]:
                        sprite_list.append(value)
                        
                # Sort sprite list by zorder based on zorder
                sprite_list.sort(key=lambda x: x[1], reverse=False)

                # Armfix
                armfix = []
                
                # Build image
                self.mannequin_sprite = Image("characters/dummy.png")
                for sprite in sprite_list:                        
                    self.mannequin_sprite = Composite(
                            (1010, 1200),
                            (0,0), self.mannequin_sprite,
                            (0,0), im.MatrixColor(Image(sprite[0]), im.matrix.desaturate()))
            return self.mannequin_sprite
            
        def get_image(self):
            if not self.cached or self.cache_override:                
                self.cached = True
                
                # Keep character images in cache
                #renpy.start_predict("characters/"+self.char+"/body/*.*")
                #renpy.start_predict("characters/"+self.char+"/face/*.*")
                
                # Create sprite list
                sprite_list = []
                
                # Add body to sprite list
                for key, value in self.body.iteritems():
                    if value[0] and not value[4]:
                        sprite_list.append(value)
                        
                # Add face to sprite list
                for key, value in self.face.iteritems():
                    if value[0] and not value[4]:
                        sprite_list.append(value)
                
                # Add other to sprite list        
                for key, value in self.other.iteritems():
                    if value[0] and not value[4]:
                        sprite_list.append(value)
                        
                # Add clothing to sprite list 
                for key, value in self.clothing.iteritems():
                    if value[0] and not value[4]:
                        # Perform an additional check for body parts modifications
                        if value[0].bodyfix != None:
                            # Iterate through all body fixes
                            for k, v in value[0].bodyfix.iteritems():
                                # Temporarily replace a body part using list comprehension 
                                sprite_list = [v if isinstance(x[0], basestring) and k in x[0] else x for x in sprite_list]
                        # Check if cloth requires layers below or above everything (such as hair locks, capes etc.)
                        if value[0].layerfix != {}:
                            for k, v in value[0].layerfix.iteritems():
                                if k == "outline_above":
                                    sprite_list.append([v[0], 150, 0, 0, False])
                                elif k == "outline_below":
                                    sprite_list.append([v[0], -150, 0, 0, False])
                                else:
                                    if v[1] == 1:
                                        sprite_list.append([value[0].get_layerfix(k), 100+k, 0, 0, False])
                                    else:
                                        sprite_list.append([value[0].get_layerfix(k), -100+k, 0, 0, False])
                        # check if clothing piece uses non-standard zorder
                        if value[0].zorder != None:
                            sprite_list.append([value[0], value[0].zorder, value[2], value[3], value[4]])
                        else:
                            sprite_list.append(value)
                        sprite_list.append([value[0].get_skin(), 5, 0, 0, False])
                        
                # Sort sprite list by zorder
                sprite_list.sort(key=lambda x: x[1], reverse=False)
                
                if self.pose == "":
                    width = 1010
                    height = 1200
                else:
                    width = 1920
                    height = 1440
                
                # Armfix and alpha mask lists
                armfix = []
                mask = []
                
                # Build image
                self.sprite = Image("characters/dummy.png")
                if sprite_list:
                    for sprite in sprite_list:
                        # Check if sprite is an imagepath or an object
                        if isinstance(sprite[0], (basestring, im.Image, im.MatrixColor)):
                            self.sprite = Composite(
                                    (width, height),
                                    (0,0), self.sprite,
                                    (sprite[2],sprite[3]), Image(sprite[0]))
                        else:
                            self.sprite = Composite(
                                    (width, height),
                                    (0,0), self.sprite,
                                    (sprite[2],sprite[3]), sprite[0].get_image())
                                    
                            if sprite[0].armfix:
                                # add fixes WITH a hand image
                                if armfix == []:
                                    armfix.append(sprite[0].get_armfix(False, False)[0]) # Lefthand
                                    armfix.append(sprite[0].get_armfix(False, False)[1]) # Righthand
                                else:
                                    # add fixes WITHOUT hand image
                                    armfix.append(sprite[0].get_armfix(False, True)[0]) # L
                                    armfix.append(sprite[0].get_armfix(False, True)[1]) # R
                                    
                            if sprite[0].mask:
                                mask.append(sprite[0].mask)
                    
                    if armfix > 0:
                        for item in armfix:
                            self.sprite = Composite(
                                (width, height),
                                (0,0), self.sprite,
                                (0,0), item)
                                 
                    # Apply AlphaMask for problematic clothing layers such as bras with visible nipples.
                    if mask != []:
                        if len(mask) > 1:
                            # Combine alpha masks
                            m = AlphaMask(mask[0], mask[1])
                            for i in xrange(2, len(mask)):
                                m = AlphaMask(mask[i], mask[i+1])
                            self.sprite = AlphaMask(self.sprite, m)
                        else:
                            self.sprite = AlphaMask(self.sprite, mask[0])
                    
                    # Fixes alpha change issues during transitions
                    self.sprite = Flatten(self.sprite)
            return self.sprite