init python:            
    class DollCloth(DollMethods): 
        def __init__(self, name, categories, type, id, color, zorder=None, unlocked=False, level=0, blacklist=None, parent=None, armfix=False, modpath=""):
            self.name = name
            self.char = eval(name)
            self.categories = categories
            self.type = type
            self.id = id
            self.color = color
            self.color_default = [x[:] for x in color]
            self.unlocked = unlocked
            self.layers = len(color)
            self.parent = parent
            self.ico = None
            self.blacklist = blacklist
            self.level = level
            self.modpath = modpath
            self.armfix = armfix
            
            # Inherit zorder from character if needed
            self.zorder = zorder if zorder else self.char.clothes[type][1]
            
            # Detect folder path
            for x in (categories[0], categories[1], type):
                if renpy.loadable("{}/characters/{}/clothes/{}/{}/".format(modpath, name, x, id)):
                    self.imagepath = "{}/characters/{}/clothes/{}/{}/".format(modpath, name, x, id)
                    break
            
            # Detect special layers and define them
            for x in self.layers_special:
                path = "{}{}.png".format(self.imagepath, x)
                self.__dict__[x] = path if renpy.loadable(path) else None
                
            # Detect back and front layers and define them
            for x in self.layers_additional:
                self.__dict__[x] = []
                for i in xrange(self.layers):
                    path = "{}{}_{}.png".format(self.imagepath, i, x)
                    if renpy.loadable(path):
                        self.__dict__[x].append(path)
                if self.__dict__[x]:
                    path = "{}outline_{}.png".format(self.imagepath, x)
                    self.__dict__[x+"_outline"] = path if renpy.loadable(path) else None
                
            # Add to character wardrobe and unordered list
            if not parent:
                self.char.wardrobe.setdefault(self.categories[0], {}).setdefault(self.categories[1], []).append(self)
                self.char.wardrobe_list.append(self)
                
            self.rebuild_image()
            self.build_icon()
            
        def build_image(self):
            sprites = []
            
            # Add colorable layers and color them
            sprites.extend((self.apply_color("{}{}.png".format(self.imagepath, x), x), x) for x in xrange(self.layers))

            # Add extra layers if exist
            for n, x in enumerate(self.layers_extra):
                path = "{}{}.png".format(self.imagepath, x)
                if renpy.loadable(path):
                    sprites.append((path, self.layers+n))
            
            sprites.sort(key=lambda x: x[1], reverse=False)
            sprites = tuple(itertools.chain.from_iterable(((0,0), x[0]) for x in sprites))
            return sprites
            
        def build_icon(self):
            sprites = []
            sprites.extend((self.apply_color("{}{}.png".format(self.imagepath, x), x), x) for x in xrange(self.layers))
            sprites.extend((self.apply_color(x, n), n-50) for n, x in enumerate(self.back))
            sprites.extend((self.apply_color(x, n), 50+n) for n, x in enumerate(self.front))
            
            for n, x in enumerate(self.layers_extra):
                path = "{}{}.png".format(self.imagepath, x)
                if renpy.loadable(path):
                    sprites.append((path, self.layers+n))
                    
            bounds = "{}outline.png".format(self.imagepath) if renpy.loadable("{}outline.png".format(self.imagepath)) else "{}0.png".format(self.imagepath)
                    
            sprites.sort(key=lambda x: x[1], reverse=False)
            sprites = tuple(itertools.chain.from_iterable(((0,0), x[0]) for x in sprites))
            self.ico = CroppedImage(sprites, bounds)
            
        def get_back(self):
            """Returns a list of layers displayed in the back of object/character"""
            return [self.apply_color(x, n) for n, x in enumerate(self.back)]
        
        def get_front(self):
            """Returns a list of layers displayed in the front of object/character"""
            return [self.apply_color(x, n) for n, x in enumerate(self.front)]
            
        def get_icon(self):
            """Returns cropped Composite displayable"""
            return self.ico.get_image()
            
        def apply_color(self, img, n):
            """Takes image and int layer number. Used internally."""
            c = im.matrix.tint(self.color[n][0]/255.0, self.color[n][1]/255.0, self.color[n][2]/255.0)
            a = im.matrix.opacity(self.color[n][3]/255.0)
            return im.MatrixColor(img, c*a)
            
        def set_color(self, n):
            """Takes int layer number for manual color picking or a list to replace the cloth color in its entirety."""
            if isinstance(n, int):
                self.char.override, self.override = True, True
                x = bool(not self.type.startswith(self.blacklist_unequip) and (config.developer or cheat_wardrobe_alpha))
                self.color[n] = color_picker(self.color[n], x, "Colour channel {}".format(n+1), pos_xy=(40, 85), color_default=self.color_default[n])
                self.char.override, self.override = False, False
            elif isinstance(n, list):
                self.color = [x[:] for x in n]
            self.rebuild_image()
            self.char.rebuild_image()
            self.build_icon()
            
        def reset_color(self, n=None):
            """Reset cloth color. Takes optional int layer number to reset only specific layer color."""
            if n:
                self.color[n] = [x for x in self.color_default]
            else:
                self.color = [x[:] for x in self.color_default]
            self.rebuild_image()
            self.char.rebuild_image()
            self.build_icon()
            
        def clone(self):
            """Creates a clone of this cloth object. Since it requires a parent object it should be used internally only to avoid object depth issue."""
            return DollCloth(self.name, self.categories, self.type, self.id, [x[:] for x in self.color], self.zorder, self.unlocked, self.level, self.blacklist, self)