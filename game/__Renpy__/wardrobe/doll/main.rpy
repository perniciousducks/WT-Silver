init python:
    class Doll(DollMethods):
        def __init__(self, name, clothes, face, body):
            self.wardrobe = {}
            self.wardrobe_list = []
            self.blacklist = []
            self.outfits = []
            self.name = name
            self.clothes = clothes
            self.face = DollFace(self, face)
            self.body = DollBody(self, body)
            
            self.rebuild_image()
        
        def rebuild(self, *args):
            """Rebuild all character images. Useful for debugging."""
            self.body.rebuild_image()
            self.face.rebuild_image()
            for o in self.wardrobe_list:
                o.rebuild_image()
                o.build_icon()
            for o in self.outfits:
                o.rebuild_image()
            self.rebuild_image()
            
        def build_image(self):
            # Add body, face, clothes, masks
            masks = []
            armfix = []
            sprites = [[self.body.get_image(), 0], [self.face.get_image(), 1]]
            
            for o in self.clothes.itervalues():
                if o[0] and o[2]:
                    sprites.append([o[0].get_image(), o[0].zorder])
                    if o[0].back:
                        sprites.extend([x, -100+n+o[0].zorder] for n, x in enumerate(o[0].get_back()))
                        if o[0].back_outline:
                            sprites.append([o[0].back_outline, -100+o[0].zorder+o[0].layers])
                    if o[0].front:
                        sprites.extend([x, 100+n+o[0].zorder] for n, x in enumerate(o[0].get_front()))
                        if o[0].front_outline:
                            sprites.append([o[0].front_outline, 100+o[0].zorder+o[0].layers])
                    if o[0].armfix:
                        sprites.extend([["{}armleft/{}_fix.png".format(self.body.imagepath, self.body.get_part("armleft")), o[0].zorder+0.5], ["{}armright/{}_fix.png".format(self.body.imagepath, self.body.get_part("armright")), o[0].zorder+0.5]])
                    if o[0].mask:
                        masks.append([o[0].mask, o[0].zorder-1])
                        
            # Apply alpha mask
            if masks:
                for m in masks:
                    for s in sprites:
                        if m[1] > s[1] >= 0:
                            s[0] = AlphaMask(s[0], m[0])
            
            sprites.sort(key=lambda x: x[1], reverse=False)
            sprites = tuple(itertools.chain.from_iterable(((0,0), x[0]) for x in sprites))
            return sprites
            
        def equip(self, obj):
            """Takes DollCloth or DollOutfit object to equip."""
            if isinstance(obj, DollCloth):
                self.clothes[obj.type][0], self.clothes[obj.type][2] = obj, True
            elif isinstance(obj, DollOutfit):
                self.unequip("all")
                for i in obj.group:
                    self.clothes[i.type][0] = i.parent
                    self.clothes[i.type][0].set_color(i.color)
            self.rebuild_image()
            
        def unequip(self, *args):
            """Takes argument(s) containing string cloth type(s) to unequip."""
            if "all" in args:
                for k, v in self.clothes.iteritems():
                    if not k.startswith(self.blacklist_unequip):
                        v[0], v[2] = None, True
            else:
                global test
                test = args
                for arg in args:
                    self.clothes[arg][0] = None
            self.rebuild_image()
            
        def get_equipped(self, type):
            """Takes argument containing string cloth type. Returns equipped object for cloth type."""
            return self.clothes[type][0]
                    
        def strip(self, *args):
            """Takes argument(s) containing string cloth type(s) to temporarily displace (hide)."""
            if "all" in args:
                for k, v in self.clothes.iteritems():
                    if not k.startswith(self.blacklist_toggles):
                        v[2] = False
            else:
                for arg in args:
                    if arg.startswith(self.blacklist_toggles):
                        for k in self.clothes.iterkeys():
                            if k.startswith(arg):
                                self.clothes[k][2] = False
                    else:
                        self.clothes[arg][2] = False
            self.rebuild_image()
                    
        def wear(self, *args):
            """Takes argument(s) containing string cloth type(s) to put on (unhide)."""
            if "all" in args:
                for v in self.clothes.itervalues():
                    v[2] = True
            else:
                for arg in args:
                    if arg.startswith(self.blacklist_toggles):
                        for k in self.clothes.iterkeys():
                            if k.startswith(arg):
                                self.clothes[k][2] = True
                    else:
                        self.clothes[arg][2] = True
            self.rebuild_image()
            
        def toggle_wear(self, type):
            """Takes argument containing string cloth type to toggle visibility (hide/unhide). Used in wardrobe."""
            if type.startswith(self.blacklist_toggles):
                for k, v in self.clothes.iteritems():
                    if k.startswith(type):
                        v[2] = not v[2]
            else:
                self.clothes[type][2] = not self.clothes[type][2]
            self.rebuild_image()
            
        def is_worn(self, type):
            """Takes argument containing string cloth type. Returns True if worn, False if hidden, None if not equipped at all."""
            if type.startswith(self.blacklist_toggles):
                for k, v in self.clothes.iteritems():
                    if k.startswith(type) and v[0] and v[2]:
                        return True
            else:
                if self.clothes[type][0]:
                    return True if self.clothes[type][2] else False
            return None
            
        def set_face(self, **kwargs):
            """Takes keyword argument(s) with the string name of expression file(s)."""
            for arg, value in kwargs.iteritems():
                if value not in (self.face.face[str(arg)][0], False):
                    self.face.face[str(arg)][0] = value
            self.face.rebuild_image()
            self.rebuild_image()
            
        def set_body(self, **kwargs):
            """Takes keyword argument(s) with the string name of body part file(s)."""
            for arg, value in kwargs.iteritems():
                if value != self.body.body[str(arg)][0]:
                    self.body.body[str(arg)][0] = value
            self.body.rebuild_image()
            self.rebuild_image()
            
        def reset_blacklist(self, unequip=True):
            """Resets wardrobe blacklist based on worn clothes. Takes optional argument that causes blacklisted clothes to be unequipped."""
            self.blacklist = []
            for v in self.clothes.itervalues():
                if v[0] and v[0].blacklist:
                    self.blacklist.extend(x for x in v[0].blacklist if x not in self.blacklist)
            if unequip and self.blacklist:
                self.unequip(*self.blacklist)
                    
        def is_blacklisted(self, type):
            """Takes string cloth type. Returns True if cloth type is blacklisted."""
            return True if type in self.blacklist else False
            
        def create_outfit(self):
            """Creates a copy of the current character clothes and stores it."""
            return DollOutfit([x[0] for x in self.clothes.itervalues() if x[0]], True)