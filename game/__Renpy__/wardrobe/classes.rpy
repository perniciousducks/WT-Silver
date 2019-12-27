init python:  
    class outfit_class(object):
        def __init__(self, **kwargs):
            self.name = None
            self.price = 0
            self.desc = ""
            self.unlocked = False
            self.group = []
            self.sprite = None
            self.cached = False
            self.schedule = [False]*6 # 0=day, 1=night, 2=cloudy, 3=rainy, 4=snowing, 5=school
            
            self.__dict__.update(**kwargs)
            
            self.char = get_character_object(self.group[0].char)
            
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
            renpy.notify("Export successful!")
        
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
                        return (False, renpy.notify("File doesn't exist!"))
                except:
                    if _image_payload._file:
                        _image_payload._file.close()
                    renpy.block_rollback()
                    return (False, renpy.notify("Corrupted file!"))
            else:
                imported = get_clipboard()
            
            if imported != "":
                try:
                    imported = evaluate(imported)
                except:
                    renpy.block_rollback()
                    return (False, renpy.notify("Corrupted file!"))

                for item in imported:
                    if not isinstance(item, basestring):
                        for object in character_clothes_list:
                            if item[0] == object.id:
                                if object.char == char_active.char:
                                    if not cheats_active:
                                        if not object.unlocked:
                                            renpy.block_rollback()
                                            return (False, renpy.notify("Items locked!"))
                                    item[0] = object.clone()
                                    item[0].color = item[1]
                                    item[0].cached = False
                                    group.append(item[0])
                if len(group) > 0:
                    renpy.notify("Import successful!")     
                    renpy.block_rollback()
                    return outfit_class(name="", desc="", unlocked=True, group=group)
            renpy.block_rollback()
            return (False, renpy.notify("Import failed!"))
                    
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
                mask_list = []
                armfix_list = []
                
                # Add body to sprite list
                for i in self.char.get_bodyparts():
                    sprite_list.append(i)
                
                # Add clothing to sprite list
                for i in self.group:
                    if i.bodyfix:
                        for k, v in i.bodyfix.iteritems():
                            sprite_list = [v if isinstance(x[0], basestring) and k in x[0] else x for x in sprite_list]
                            
                    if i.layerfix:
                        for k, v in i.layerfix.iteritems():
                            if k == "outline_above":
                                sprite_list.append([v[0], 150])
                            elif k == "outline_below":
                                sprite_list.append([v[0], -150])
                            else:
                                if v[1] == 1:
                                    sprite_list.append([i.get_layerfix(k), 100+k])
                                else:
                                    sprite_list.append([i.get_layerfix(k), -100+k])
                                    
                    if i.zorder:
                        sprite_list.append([i, i.zorder])
                        if i.mask:
                            mask_list.append([i.mask, i.zorder,])
                    else:
                        sprite_list.append([i, self.char.clothing[i.type][1]])
                        if i.mask:
                            mask_list.append([i.mask, self.char.clothing[i.type][1]])
                            
                    # Check if clothing has armfix layers
                    if i.armfix:
                        if armfix_list:
                            armfix_list.append(i.get_armfix(True, True)[0])
                            armfix_list.append(i.get_armfix(True, True)[1])
                        else:
                            armfix_list.append(i.get_armfix(True, False)[0])
                            armfix_list.append(i.get_armfix(True, False)[1])
                                    
                    if i.skinlayer:
                        sprite_list.append([i.get_skin(), 5])
                                    
                # Sort sprite list by zorder based on character clothing zorder
                sprite_list.sort(key=lambda x: x[1], reverse=False)
                
                # Build image
                self.sprite = Null()
                for sprite in sprite_list:                        
                    if isinstance(sprite[0], cloth_class):
                        layer = sprite[0].get_image()
                        
                        # Apply alpha masking
                        for mask in mask_list:
                            if sprite[1] < mask[1]:
                                layer = AlphaMask(layer, mask[0])
                    else:
                        layer = im.MatrixColor(Image(sprite[0]), im.matrix.desaturate())
                        
                    self.sprite = Composite(
                            (1010, 1200),
                            (0,0), self.sprite,
                            (0,0), layer)
                    
                for armfix in armfix_list:
                    self.sprite = Composite(
                        (1010, 1200),
                        (0,0), self.sprite,
                        (0,0), armfix)

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
            self.skinlayer = None
            self.extralayer = None
            self.overlayer = None
            self.outline = None
            self.unlocked = True
            self.cloned = False
            self.cached = False
            self.is_wet = False
            self.zorder = None # None - use pre-defined zorder, int - object zorder
            
            self.bodyfix = None
            self.incompatible = None
            self.mask = None
            self.wet_mask = None
            
            self.layerfix = {}
            
            self.armfix = False
            self.armfixList = [[], []]
            self.armfix_Lx = ""
            self.armfix_Rx = ""
            
            self.sprite_ico = None

            self.name = ""
            self.desc = ""
            self.whoring = 0
            
            self.pose = ""

            self.imagepath = ""
            self.modpath = ""
            
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
                    self.color.append([255, 0, 203, 255])

            self.color_default = [x[:] for x in self.color]
            
            # Check if clothing folder is a category, subcategory or a type
            if renpy.loadable(self.modpath+"characters/"+self.char+"/clothes/"+self.category+"/"+self.id+"/0.png"):
                self.imagepath = self.modpath+"characters/"+self.char+"/clothes/"+self.category+"/"+self.id+"/"
            elif renpy.loadable(self.modpath+"characters/"+self.char+"/clothes/"+self.subcat+"/"+self.id+"/0.png"):
                self.imagepath = self.modpath+"characters/"+self.char+"/clothes/"+self.subcat+"/"+self.id+"/"
            else:
                self.imagepath = self.modpath+"characters/"+self.char+"/clothes/"+self.type+"/"+self.id+"/"
            
            if renpy.loadable(self.imagepath+"skin.png"):
                self.skinlayer = self.imagepath+"skin.png"
            if renpy.loadable(self.imagepath+"extra.png"):
                self.extralayer = self.imagepath+"extra.png"
            if renpy.loadable(self.imagepath+"overlay.png"):
                self.overlayer = self.imagepath+"overlay.png"
            if renpy.loadable(self.imagepath+"mask.png"):
                self.mask = self.imagepath+"mask.png"
            if renpy.loadable(self.imagepath+"wet_mask.png"):
                self.wet_mask = self.imagepath+"wet_mask.png"
                
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
            boundryIndex = 0 if "tattoo" in self.type or "makeup" in self.type else self.layers+1 # Tattoos and makeup can't use the outlines for image crop calculation.
            for i in xrange(self.layers):
                layers.append(self.get_imagelayer(i))
            layers.append(self.extralayer)
            layers.append(self.outline)

            self.sprite_ico = lazyload(layers, self.color, boundryIndex, self.layers)
                
        def unlock(self):
            if not self.unlocked:
                self.unlocked = True
                # Add cloth object to the character's clothing data
                get_character_object(self.char).clothing_dictlist.setdefault(self.category, {}).setdefault(self.subcat, []).append(self)
            
        def clone(self):
            color = [x[:] for x in self.color]
            return cloth_class(char=self.char, category=self.category, subcat=self.subcat, type=self.type, id=self.id, layers=self.layers, color=color, unlocked=self.unlocked, cloned=True, name=self.name, desc=self.desc, armfix=self.armfix, layerfix=self.layerfix, whoring=self.whoring, bodyfix=self.bodyfix, incompatible=self.incompatible, mask=self.mask, zorder=self.zorder)
                
        def set_pose(self, pose):
            self.pose = pose if pose else ""
            self.outline = self.imagepath+"outline.png"
            
            path = self.imagepath+self.pose+"skin.png"
            self.skinlayer = path if renpy.loadable(path) else None
            
            path = self.imagepath+self.pose+"extra.png"
            self.skinlayer = path if renpy.loadable(path) else None
            
            path = self.imagepath+self.pose+"overlay.png"
            self.skinlayer = path if renpy.loadable(path) else None
            
            path = self.imagepath+self.pose+"mask.png"
            self.skinlayer = path if renpy.loadable(path) else None

            self.set_armfix()
            self.cached = False
            return
            
        def set_layerfix(self, anim=False):
            pose = self.pose
            if anim:
                pose += "/"+self.pose+"/"
                
            self.layerfix = {}
            for layer in xrange(self.layers):
                path = self.imagepath+pose+str(layer)+"_above.png"
                if renpy.loadable(path):
                    self.layerfix[layer] = [path, 1]
                    
                path = self.imagepath+pose+str(layer)+"_below.png"
                if renpy.loadable(path):
                    self.layerfix[layer] = [path, 0]
                    
            path = self.imagepath+pose+"outline_above.png"
            if renpy.loadable(path):
                self.layerfix['outline_above'] = [path, 2]
                
            path = self.imagepath+pose+"outline_below.png"
            if renpy.loadable(path):
                self.layerfix['outline_below'] = [path, 2]
            return
            
        def set_armfix(self, anim=False):
            pose = self.pose
            if anim:
                pose += "/"+self.pose+"/"
                
            self.armfixList = [[], []]
            if self.armfix:
                for layer in xrange(self.layers):
                    path = self.imagepath+pose+str(layer)+"_armL.png"
                    if renpy.loadable(path):
                        self.armfixList[0].append(path)
                        
                    path = self.imagepath+pose+str(layer)+"_armR.png"
                    if renpy.loadable(path):
                        self.armfixList[1].append(path)
                        
                path = self.imagepath+pose+"outline_armL.png"
                self.armfix_Lx = path if renpy.loadable(path) else ""
                
                path = self.imagepath+pose+"outline_armR.png"
                self.armfix_Rx = path if renpy.loadable(path) else ""
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
            self.color = [x[:] for x in l]
            self.sprite_ico.color = self.color
            self.sprite_ico.cached = False
            self.cached = False

        def set_color(self, layer):
            x = bool(self.type != "hair" and (config.developer or cheat_wardrobe_alpha))
            self.color[layer] = color_picker(self.color[layer], x, "Colour channel "+str(layer+1), pos_xy=[40, 85], color_default=list(self.color_default[layer]))
            self.sprite_ico.color = self.color
            self.sprite_ico.cached = False
            self.cached = False
            
        def reset_color(self):
            self.color = [x[:] for x in self.color_default]
            self.sprite_ico.color = self.color
            self.sprite_ico.cached = False
            self.cached = False
        
        def get_imagelayer(self, layer):
            return self.imagepath+str(layer)+".png" if self.pose == "" else self.imagepath+"/"+self.pose+"/"+str(layer)+".png"

        def get_imagelayer_color(self, layer):
            return im.MatrixColor(self.get_imagelayer(layer), self.get_matrixcolor(layer) * im.matrix.opacity(self.get_alpha(layer)))
            
        def get_skin(self):
            return self.skinlayer
                    
        def get_image(self):            
            self.sprite = self.get_imagelayer_color(0)
            for i in xrange(1, self.layers):
                self.sprite = Composite((1010, 1200), (0,0), self.sprite, (0,0), self.get_imagelayer_color(i))
                
            # Extra layer
            if self.extralayer:           
                self.sprite = Composite((1010, 1200), (0,0), self.sprite, (0,0), self.extralayer)
                
            # Outline
            self.sprite = Composite((1010, 1200), (0,0), self.sprite, (0,0), self.outline)
            
            # Overlay
            if self.overlayer:           
                self.sprite = Composite((1010, 1200), (0,0), self.sprite, (0,0), self.overlayer)
                    
            # Apply alpha mask simulating cloth wetness (transparency)
            if self.is_wet and self.wet_mask:
                self.sprite = AlphaMask(self.sprite, self.wet_mask)
            return self.sprite
            
        def get_armfix(self, skingray=False, nohand=False):
            if skingray:
                armL = Null() if nohand or bool(self.pose) else im.MatrixColor(Image("characters/"+self.char+"/body/arms/armfixL.png"), im.matrix.desaturate())
                armR = Null() if nohand or bool(self.pose) else im.MatrixColor(Image("characters/"+self.char+"/body/arms/armfixR.png"), im.matrix.desaturate())
            else:
                armL = Null() if nohand or bool(self.pose) else Image("characters/"+self.char+"/body/arms/armfixL.png")
                armR = Null() if nohand or bool(self.pose) else Image("characters/"+self.char+"/body/arms/armfixR.png")
            
            # Add armfix with proper colors
            for i, layer in enumerate(self.armfixList[0]):
                armL = Composite((1010, 1200), (0,0), armL, (0,0), im.MatrixColor(layer, self.get_matrixcolor(i)))
            for i, layer in enumerate(self.armfixList[1]):
                armR = Composite((1010, 1200), (0,0), armR, (0,0), im.MatrixColor(layer, self.get_matrixcolor(i)))
                       
            # Add armfix outline    
            if self.armfix_Lx != "":
                armL = Composite((1010, 1200), (0,0), armL, (0,0), self.armfix_Lx)                        
            if self.armfix_Rx != "":
                armR = Composite((1010, 1200), (0,0), armR, (0,0), self.armfix_Rx)
            return (armL, armR)
            
        def get_layerfix(self, layer):
            return Image(im.MatrixColor(self.layerfix[layer][0], self.get_matrixcolor(layer)*im.matrix.opacity(self.get_alpha(layer))))
            
        def get_icon(self):
            return self.sprite_ico.get_image()
            
    class char_class(object):
        def __init__(self, **kwargs):
            self.char = None
            
            self.stats = stats_class() # Initialize stats object instance
            
            self.body = {}
            self.face = {}
            self.clothing = {}
            self.clothing_dictlist = {}
            self.outfits = []
            self.outfits_schedule = {True: [], False:[]} # True=day, false=night 
            self.other = {}
            
            self.incompatible_wardrobe = []
            
            self.pose = ""
            
            self.sprite = None
            self.mannequin_sprite = None
            
            self.cached = False
            self.cache_override = False

            self.__dict__.update(**kwargs)
            
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
            s = ".png"
            
            if 'body' in args:
                imagepath = "characters/"+self.char+"/body/"
                
                for key, value in self.body.iteritems():
                    if value[0] and not value[0].endswith(s):
                        x = bool(key in ("armleft", "armright", "handleft", "handright"))
                        value[0] = imagepath+"arms/"+value[0]+".png" if x else imagepath+key+"/"+value[0]+".png"
                            
            if 'face' in args:
                imagepath = "characters/"+self.char+"/face/"
                
                for key, value in self.face.iteritems():
                    if value[0] and not value[0].endswith(s):
                        if key in ("tears", "cheeks"):
                            value[0] = imagepath+"extras/"+value[0]+".png"
                        elif key == "whites":
                            value[0] = imagepath+"eyes/"+value[0]+".png"
                        else:
                            value[0] = imagepath+key+"/"+value[0]+".png"
                            
            if 'other' in args:
                emote = self.get_object(self.other, 'emote')
                cum = self.get_object(self.other, 'cum')
                
                imagepath = "characters/emotes/"
                if emote and not emote.endswith(s):
                    self.other['emote'][0] = imagepath+emote+".png"
                    
                imagepath = "characters/"+self.char+"/cum/"
                if cum and not cum.endswith(s):
                    self.other['cum'][0] = imagepath+cum+".png"
            self.cached = False
            
        def update_outfits_schedule(self, obj=None, all=False):
            if all:
                self.outfits_schedule = {True: [], False:[]}
                
                for outfit in self.outfits:
                    if outfit.schedule[0] == True:
                        self.outfits_schedule[True].append(outfit)
                    elif outfit.schedule[1] == True:
                        self.outfits_schedule[False].append(outfit)
                return
                
            if obj.schedule[0] == True:
                if not obj in self.outfits_schedule[True]:
                    self.outfits_schedule[True].append(obj)
            else:
                if obj in self.outfits_schedule[True]:
                    self.outfits_schedule[True].remove(obj)
                    
            if obj.schedule[1] == True:
                if not obj in self.outfits_schedule[False]:
                    self.outfits_schedule[False].append(obj)
            else:
                if obj in self.outfits_schedule[False]:
                    self.outfits_schedule[False].remove(obj)
            return
                    
        def expression(self, **kwargs):
            for arg, value in kwargs.iteritems():
                if value:
                    self.face[str(arg)][0] = value
            self.update_paths("face")
            self.cached = False
            
        def special(self, **kwargs):
            for arg, value in kwargs.iteritems():
                self.other[str(arg)][0] = value
            self.update_paths("other")
            self.cached = False
            
        def set_body(self, **kwargs):
            for arg, value in kwargs.iteritems():
                self.body[str(arg)][0] = value
                self.body[str(arg)][4] = False
            self.update_paths("body")
            self.cached = False
            return
            
        def set_pose(self, pose, offset):
            if not pose == None:
                self.pose = pose
                for key, value in self.body.iteritems():
                    value[4] = True
                for key, value in self.face.iteritems():
                    value[2] = offset[0]
                    value[3] = offset[1]
                self.body['animation'][0] = pose
                self.body['animation'][4] = False
            else:
                self.pose = ""
                for key, value in self.body.iteritems():
                    value[4] = False
                for key, value in self.face.iteritems():
                    value[2] = 0
                    value[3] = 0
                self.body['animation'][0] = None
            self.update_paths("body")
            self.cached = False
            
        def animation(self, anim, offset=(0,0)):
            for key, value in self.clothing.iteritems():
                if value[0]:
                    if value[0].set_pose(anim) == False:
                        value[4] = True
                    else:
                        value[4] = False
            self.set_pose(anim, offset)
            self.cached = False
            
        def action(self, action):
            """Unfinished, added for future reference.
            Known issues:
            - Incompatible with dynamic zorder
            - Incompatible with alpha masking
            - poses require additional artwork for each cloth affected by the arms movement (bottoms, tops, gloves, bras, accessories, piercings, tattoos) (Not viable in the long run)"""
            # Hardcoded for testing purposes
            if action in (None, "default", "reset"):
                if self.char == "hermione":
                    self.set_body(armright="arm_down_r" ,armleft="arm_down_l")
            elif action == "lift_skirt":
                if self.char == "hermione":
                    self.set_body(armright=None ,armleft="lift_skirt")
                    self.body["armleft"][1] = 20
            for key, value in self.clothing.iteritems():
                if value[0]:
                    value[0].set_pose(action)
            self.cached = False
            return
            
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

        def clothes_compatible(self, unequip=True):
            result = True
            for value in self.clothing.itervalues():
                if value[0] and value[0].incompatible:
                    for itemtype in value[0].incompatible:
                        if self.clothing[itemtype][0]:
                            if unequip:
                                self.unequip(itemtype)
                            result = False
            return result
            
        def reset_compatibility(self):
            self.incompatible_wardrobe = []
            for value in self.clothing.itervalues():
                if value[0] and value[0].incompatible != None:
                    for key in value[0].incompatible:
                        if key not in self.incompatible_wardrobe:
                            self.incompatible_wardrobe.append(key)
            
        def equip(self, object):
            if isinstance(object, outfit_class):
                self.unequip("all")
                for item in object.group:
                    self.clothing[item.type][0] = item
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
            update_chibi(self.char)
            
        def unequip(self, *args):
            if 'all' in args:
                for key in self.clothing:
                    if not key == "hair":
                        self.clothing[key][0] = None
                self.incompatible_wardrobe = []
            else:
                for arg in args:
                    if self.clothing[str(arg)][0] and self.clothing[str(arg)][0].incompatible != None:
                        for key in self.clothing[str(arg)][0].incompatible:
                            if key in self.incompatible_wardrobe:
                                self.incompatible_wardrobe.remove(key)
                    self.clothing[str(arg)][0] = None
            self.cached = False
            update_chibi(self.char)
            
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
                        self.clothing[str(arg)][4] = True
            self.cached = False
            update_chibi(self.char)
            
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
                        self.clothing[str(arg)][4] = False
            self.cached = False
            update_chibi(self.char)
            
        def toggle_wear(self, type):
            if type in ("makeup", "accessory", "piercing", "tattoo"):
                for key in self.clothing.iterkeys():
                    if type in key:
                        self.clothing[key][4] = not self.clothing[key][4]
            else:
                self.clothing[str(type)][4] = not self.clothing[str(type)][4]
            self.cached = False
            
        def get_worn(self, type):
            """Returns either True, False or None depending if cloth is equipped at all (None) and if it's currently visible (True/False)"""
            if type in ("makeup", "accessory", "piercing", "tattoo"):
                for key in self.clothing.iterkeys():
                    if type in key:
                        if self.clothing[key][0] and not self.clothing[key][4]:
                            return True
            else:
                if self.clothing[type][0]:
                    return True if not self.clothing[type][4] else False
            return None

        def create_outfit(self, name, desc, unlock=True):
            clothes = [x[0].clone() for x in self.clothing.itervalues() if x[0]]
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
                
                # Build image
                self.mannequin_sprite = Null()
                for sprite in sprite_list:                        
                    self.mannequin_sprite = Composite((1010, 1200), (0,0), self.mannequin_sprite, (0,0), im.MatrixColor(Image(sprite[0]), im.matrix.desaturate()))
            return self.mannequin_sprite
            
        def get_image(self):
            if not self.cached or self.cache_override:                
                self.cached = True
                
                # Keep character images in cache
                #renpy.start_predict("characters/"+self.char+"/body/*.*")
                #renpy.start_predict("characters/"+self.char+"/face/*.*")
                
                # Create sprite list
                sprite_list = []
                mask_list = []
                armfix_list = []
                
                #### Character blinking prototype ####
                # Image cannot be defined in the class init phase (Flatten overrides animation)
                # TODO: find a way to fix that or create a new function if can't be fixed
                ######################################

                if not "Cl" in self.face["eyes"][0]:
                    sprite_list.append([renpy.get_registered_image("spr_{} blink".format(self.char)), 8.5, 0, 0, False])
                
                # Add body to sprite list
                for value in self.body.itervalues():
                    if value[0] and not value[4]:
                        sprite_list.append(value)
                        
                # Add face to sprite list
                for value in self.face.itervalues():
                    if value[0] and not value[4]:
                        sprite_list.append(value)
                
                # Add other to sprite list        
                for value in self.other.itervalues():
                    if value[0] and not value[4]:
                        sprite_list.append(value)
                        
                # Add clothing to sprite list 
                for value in self.clothing.itervalues():
                    if value[0] and not value[4]:
                    
                        # Perform an additional check for body parts modifications
                        if value[0].bodyfix:
                            # Iterate through all body fixes
                            for k, v in value[0].bodyfix.iteritems():
                                # Temporarily replace a body part using list comprehension 
                                sprite_list = [v if isinstance(x[0], basestring) and k in x[0] else x for x in sprite_list]
                                
                        # Check if cloth requires layers below or above everything (such as hair locks, capes etc.)
                        if value[0].layerfix:
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
                        if value[0].zorder:
                            sprite_list.append([value[0], value[0].zorder, value[2], value[3], value[4]])
                            if value[0].mask:
                                mask_list.append([value[0].mask, value[0].zorder, value[2], value[3], value[4]])
                        else:
                            sprite_list.append(value)
                            if value[0].mask:
                                mask_list.append([value[0].mask, value[1], value[2], value[3], value[4]])
                                
                        # Check if clothing has armfix layers
                        if value[0].armfix:
                            if armfix_list:
                                armfix_list.append(value[0].get_armfix(False, True)[0])
                                armfix_list.append(value[0].get_armfix(False, True)[1])
                            else:
                                armfix_list.append(value[0].get_armfix(False, False)[0])
                                armfix_list.append(value[0].get_armfix(False, False)[1])

                        if value[0].skinlayer:
                            sprite_list.append([value[0].get_skin(), 5, 0, 0, False])
                        
                # Sort sprite list by zorder
                sprite_list.sort(key=lambda x: x[1], reverse=False)
                
                if not self.pose:
                    width, height = 1010, 1200
                else:
                    width, height = 1920, 1440
                
                # Build image
                self.sprite = Null()
                for sprite in sprite_list:
                    # Check if sprite is an object or an imagepath
                    if isinstance(sprite[0], cloth_class):
                        layer = sprite[0].get_image()
                        
                        # Apply alpha masking
                        for mask in mask_list:
                            if sprite[1] < mask[1]:
                                layer = AlphaMask(layer, mask[0])
                    elif isinstance(sprite[0], basestring):
                        layer = Image(sprite[0])
                    else:
                        layer = sprite[0]

                    self.sprite = Composite(
                            (width, height),
                            (0,0), self.sprite,
                            (sprite[2],sprite[3]), layer)
                            
                for armfix in armfix_list:
                    self.sprite = Composite(
                        (width, height),
                        (0,0), self.sprite,
                        (0,0), armfix)
                    
                # Fixes alpha change issues during transitions
                self.sprite = Flatten(self.sprite)
            return self.sprite