label chibi_test_scene:
    $ susan_chibi.position(x="mid",y="base")
    $ susan_chibi.do()
    $ susan_chibi.update()
    $ susan_chibi.show()
    pause 2
    $ susan_chibi.move(x="door")
    pause 2
    $ susan_chibi.hide()

    $ tonks_chibi.position(x="mid",y="base")
    $ tonks_chibi.do()
    $ tonks_chibi.update()
    $ tonks_chibi.show()
    pause 2
    $ tonks_chibi.move(x="door")
    pause 2
    $ tonks_chibi.hide()

    "The end..."
    return

screen chibi(chibi_object):
    zorder chibi_object.zorder
    fixed:
        at chibi_object.transform
        fit_first True
        for d in chibi_object.displayables():
            add d
        transclude # Allow additional content when used by another screen
        frame: # Debug frame
            background "#00ff0077"

define chibi_places = {
    "mid": (540, None),
    "desk": (440, None),
    "on_desk": (350, 180),
    "door": (750, None),
    "base": (None, 250),
}

#TODO Define a reasonable base speed
define chibi_base_speed = 100 # pixels/sec

init -1 python:
    from collections import OrderedDict
    import os.path

    class chibi(object):
        #TODO Document usage of chibi class
        """
            tag: name of the chibi (character name, use only letters)
            special: an action with its own set of layers (ie. images are loaded from a special directory)
            action: an action that uses the common set of layers (ie. images are loaded from the image path)
        """
        def __init__(self, tag, layers, update_callback, zorder=3, image_path=None):
            self.tag = tag
            if image_path:
                self.image_path = image_path
            else:
                self.image_path = "characters/{}/chibis".format(tag)
            self.layers = OrderedDict([(k, None) for k in layers])
            self.pos = (0,0)
            self.flip = False
            self.action = None
            self.special = None
            self.update_callback = update_callback
            self.zorder = zorder
            self.transform = None
            self.screen_tag = "{}_chibi".format(tag)
            # Define a screen for the chibi
            renpy.define_screen(self.screen_tag, chibi._screen, tag=self.screen_tag, zorder="chibi_object.zorder")

        @staticmethod
        def _screen(chibi_object, **kwargs):
            renpy.use_screen("chibi", chibi_object, _name=kwargs["_name"], _scope=kwargs["_scope"])

        def show(self):
            renpy.show_screen(self.screen_tag, chibi_object=self)

        def hide(self):
            renpy.hide_screen(self.screen_tag)
        
        def update(self):
            self.clear()
            self.special = None
            if self.update_callback:
                self.update_callback(self)

        def move(self, x=None, y=None, speed=1.0, pause=True):
            pos = self.resolve_position(x,y)
            dist = math.sqrt((self.pos[0] - pos[0])**2 + (self.pos[1] - pos[1])**2)
            time = dist / (float(chibi_base_speed) * speed)
            self.flip = self.pos[0] <= pos[0]
            if self.special in ("fly", "fly_move"):
                self.position()
                self.do("fly_move")
                self.transform = chibi_fly(self.pos[0], pos[0], self.pos[1], pos[1], time)
            else:
                self.position()
                self.do("walk")
                self.transform = chibi_walk(self.pos, pos, -1 if self.flip else 1, time)
            if pause:
                renpy.pause(time)
                if self.special == "fly_move":
                    self.do("fly")
                else:
                    self.do()
            self.position(pos[0], pos[1])

        def do(self, action=None):
            self.action = self.special = None
            if action != "walk":
                self.special = action
            else:
                self.action = action
            self.update()

        def position(self, x=None, y=None, flip=None):
            (x,y) = self.resolve_position(x,y)
            if flip != None:
                self.flip = flip
            self.pos = (x,y)
            self.transform = chibi_base(self.pos, -1 if self.flip else 1)
        
        def resolve_position(self, x=None, y=None):
            if not isinstance(x, int):
                if x == None:
                    x = self.pos[0]
                elif x in chibi_places:
                    x = chibi_places[x][0] or self.pos[0]
                else:
                    x = int(x)
            if not isinstance(y, int):
                if y == None:
                    y = self.pos[1]
                elif y in chibi_places:
                    y = chibi_places[y][1] or self.pos[1]
                else:
                    y = int(y)
            return (x,y)

        def displayables(self):
            return (d for d in self.layers.itervalues() if d)

        def clear(self):
            for k in self.layers.iterkeys():
                self.layers[k] = None

        def __getitem__(self, key):
            return self.layers[key]
        
        def __setitem__(self, key, value):
            if key not in self.layers:
                # Layer must be defined at construction
                raise KeyError(key)
            
            if isinstance(value, basestring) and '.' in value:
                # Assume value is a filename
                if value.startswith('~') or not self.special:
                    # Avoid special directory
                    value = os.path.join(self.image_path, value)
                else:
                    value = os.path.join(self.image_path, self.special, value)
            
            self.layers[key] = value

init python:
    # OLD CODE
    #TODO Replace usage of update_chibi_image with chibi class implementation
    def update_chibi_image(name):
        if name == "cho":
            imagepath = "characters/cho/chibis/"
            animation = "_"+cho_chibi_animation if cho_chibi_animation else ""
            status = "_"+cho_chibi_status if cho_chibi_status else ""
            global cho_chibi_fix, cho_chibi_gloves, cho_chibi_top, cho_chibi_bottom, cho_chibi_robe, cho_chibi_shoes, cho_chibi_walk_shoes, cho_chibi_stand, cho_chibi_walk
            cho_chibi_fix, cho_chibi_gloves, cho_chibi_top, cho_chibi_bottom, cho_chibi_robe, cho_chibi_shoes, cho_chibi_walk_shoes, cho_chibi_stand, cho_chibi_walk, cho_chibi_shoes = "blank", "blank", "blank", "blank", "blank", "blank", "blank", "ch_cho blink", "ch_cho walk", "ch_cho walk_shoes"

            if cho_chibi_animation == "fly":
                cho_chibi_stand = "ch_cho fly_idle"
                cho_chibi_walk = "ch_cho fly"

            if cho_class.get_worn("top"):
                if cho_class.get_cloth("top").id == "top_sweater_1":
                    cho_chibi_top = imagepath+"cc_sweater"+animation+status+".png" if animation else imagepath+"cc_sweater.png"
                else:
                    cho_chibi_top = imagepath+"cc_top"+animation+status+".png" if animation else imagepath+"cc_top.png"

            if cho_class.get_worn("bottom"):
                if cho_class.get_cloth("bottom").id in ("pants_long_2", "pants_short_4"):
                    if not status == "_move":
                        cho_chibi_bottom = imagepath+"cc_trousers"+animation+".png"
                    else:
                        if animation:
                            cho_chibi_bottom = imagepath+"cc_trousers"+animation+status+".png"
                        else:
                            if status == "_move":
                                cho_chibi_bottom = "ch_cho trousers"
                            else:
                                cho_chibi_bottom = imagepath+"cc_trousers.png"
                else:
                    cho_chibi_bottom = imagepath+"cc_skirt"+animation+status+".png" if animation else imagepath+"cc_skirt.png"

            if cho_class.get_worn("gloves"):
                if cho_class.get_cloth("gloves").id == "quidditch":
                    cho_chibi_gloves = imagepath+"cc_gloves"+animation+status+".png" if animation else imagepath+"cc_gloves.png"

            if cho_class.get_worn("robe"):
                if cho_class.get_cloth("robe").id == "robe_quidditch_1":
                    cho_chibi_robe = imagepath+"cc_quid_robe"+animation+status+".png" if animation else imagepath+"cc_quid_robe.png"
                    if not animation:
                        cho_chibi_fix = imagepath+"cc_quid_robe_fix.png"
                else:
                    cho_chibi_robe = imagepath+"cc_robe"+animation+status+".png" if animation else imagepath+"cc_robe.png"

            if cho_class.get_worn("bottom") or cho_class.get_worn("stockings"):
                if cho_class.get_worn("gloves") and cho_class.get_cloth("gloves").id == "quidditch":
                    if not animation and status == "_move":
                        cho_chibi_shoes = "ch_cho walk_quid_shoes"
                    else:
                        cho_chibi_shoes = imagepath+"cc_quid_shoes"+animation+status+".png"
                else:
                    if not status == "_move":
                        cho_chibi_shoes = imagepath+"cc_shoes"+animation+".png"
                    else:
                        if animation:
                            cho_chibi_shoes = imagepath+"cc_shoes"+animation+".png"
            else:
                cho_chibi_shoes = "blank"
        elif name == "tonks":
            imagepath = "characters/tonks/chibis/"
            animation = "_"+ton_chibi_animation if ton_chibi_animation else ""
            status = "_"+ton_chibi_status if ton_chibi_status else ""
            global ton_chibi_fix, ton_chibi_gloves, ton_chibi_top, ton_chibi_bottom, ton_chibi_robe, ton_chibi_shoes, ton_chibi_walk_shoes, ton_chibi_stand, ton_chibi_walk
            ton_chibi_fix, ton_chibi_gloves, ton_chibi_top, ton_chibi_bottom, ton_chibi_robe, ton_chibi_shoes, ton_chibi_walk_shoes, ton_chibi_stand, ton_chibi_walk, ton_chibi_shoes = "blank", "blank", "blank", "blank", "blank", "blank", "blank", "ch_ton blink", "ch_ton walk", "ch_ton walk_shoes"

            if tonks_class.get_worn("top"):
                ton_chibi_top = imagepath+"nt_top"+animation+status+".png" if animation else imagepath+"nt_top.png"

            if tonks_class.get_worn("bottom"):
                if tonks_class.get_cloth("bottom").subcat == "trousers":
                    if not status == "_move":
                        ton_chibi_bottom = imagepath+"nt_trousers"+animation+".png"
                    else:
                        if animation:
                            ton_chibi_bottom = imagepath+"nt_trousers"+animation+status+".png"
                        else:
                            if status == "_move":
                                ton_chibi_bottom = "ch_ton trousers"
                            else:
                                ton_chibi_bottom = imagepath+"nt_trousers.png"
                else:
                    ton_chibi_bottom = imagepath+"nt_skirt"+animation+status+".png" if animation else imagepath+"nt_skirt.png"

            if tonks_class.get_worn("gloves"):
                ton_chibi_gloves = imagepath+"nt_gloves"+animation+status+".png" if animation else imagepath+"nt_gloves.png"

            if tonks_class.get_worn("robe"):
                ton_chibi_robe = imagepath+"nt_robe"+animation+status+".png" if animation else imagepath+"nt_robe.png"

            if tonks_class.get_worn("bottom") or tonks_class.get_worn("stockings"):
                if not status == "_move":
                    ton_chibi_shoes = imagepath+"nt_shoes"+animation+".png"
                else:
                    if animation:
                        ton_chibi_shoes = imagepath+"nt_shoes"+animation+".png"
            else:
                ton_chibi_shoes = "blank"
        elif name == "astoria":
            imagepath = "characters/astoria/chibis/"
            animation = "/"+ast_chibi_animation+"/" if ast_chibi_animation else ""
            status = "_"+ast_chibi_status if ast_chibi_status else ""
            global ast_chibi_gloves, ast_chibi_top, ast_chibi_bottom, ast_chibi_robe, ast_chibi_shoes, ast_chibi_walk_shoes, ast_chibi_stand, ast_chibi_walk
            ast_chibi_gloves, ast_chibi_top, ast_chibi_bottom, ast_chibi_robe, ast_chibi_shoes, ast_chibi_walk_shoes, ast_chibi_stand, ast_chibi_walk, ast_chibi_shoes = "blank", "blank", "blank", "blank", "blank", "blank", "ch_ast blink", "ch_ast walk", "ch_ast walk_shoes"
            
            if ast_chibi_animation == "wand":
                ast_chibi_stand = "ch_ast wand_stand"
                #ast_chibi_walk = "ch_ast walk"
            elif ast_chibi_animation == "wand_casting":
                ast_chibi_stand = "ch_ast wand_casting"
                #ast_chibi_walk = "ch_ast walk"
            elif ast_chibi_animation == "wand_imperio":
                ast_chibi_stand = "ch_ast wand_imperio"
                #ast_chibi_walk = "ch_ast walk"

            if astoria_class.get_worn("top"):
                ast_chibi_top = imagepath+animation+"ag_top"+status+".png" if animation else imagepath+"ag_top.png"

            if astoria_class.get_worn("bottom") or astoria_class.get_worn("top") and astoria_class.get_cloth("top").id == astoria_cloth_topann.id: # # #
                ast_chibi_bottom = imagepath+animation+"ag_skirt"+status+".png" if animation else imagepath+"ag_skirt.png"

            if astoria_class.get_worn("robe") and not animation:
                ast_chibi_robe = imagepath+animation+"ag_robe"+status+".png" if animation else imagepath+"ag_robe.png"

            if astoria_class.get_worn("bottom") or astoria_class.get_worn("stockings"):
                if not status == "_move":
                    if ast_chibi_animation == "wand_imperio":
                        ast_chibi_shoes = "ch_ast imperio_shoes"
                    else:
                        ast_chibi_shoes = imagepath+animation+"ag_shoes.png"
                else:
                    if animation:
                        if ast_chibi_animation == "wand_imperio":
                            ast_chibi_shoes = "ch_ast imperio_shoes"
                        else:
                            ast_chibi_shoes = imagepath+animation+"ag_shoes.png"
            else:
                ast_chibi_shoes = "blank"
        return
    # END OF OLD CODE