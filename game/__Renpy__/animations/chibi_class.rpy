label chibi_test_scene:
    # $ susan_chibi.position(x="mid",y="base")
    # $ susan_chibi.do()
    # $ susan_chibi.show()
    # pause 2
    # $ susan_chibi.move(x="door")
    # pause 2
    # $ susan_chibi.hide()

    # $ tonks_chibi.position(x="mid",y="base")
    # $ tonks_chibi.do()
    # $ tonks_chibi.show()
    # pause 2
    # $ tonks_chibi.move(x="door")
    # pause 2
    # $ tonks_chibi.hide()

    # $ cho_class.equip(cho_outfit_quidditch)
    # $ cho_chibi.position(x="door",y="base")
    # $ cho_chibi.do("fly")
    # $ cho_chibi.show()
    # pause 4
    # $ cho_chibi.move(x="desk")
    # pause 4
    # $ cho_chibi.move(x="door")
    # pause 4
    # $ cho_chibi.do("fly", flip=False)
    # pause 4
    # $ cho_chibi.hide()
    $ renpy.checkpoint()
    "Begin"
    $ astoria_chibi.position(x="mid", y="base")
    $ astoria_chibi.do()
    $ astoria_chibi.show()
    "Check 1"
    $ astoria_chibi.do("wand")
    $ astoria_chibi.zorder = 2
    "Check 2"
    $ astoria_chibi.hide()
    "Done"

    jump main_room

screen chibi(chibi_object):
    zorder chibi_object.zorder
    fixed:
        at chibi_object.transform
        fit_first True
        for d in chibi_object.displayables():
            add d
        transclude # Allow additional content when used by another screen
        frame: # Debug frame
            background "#00ff0055"

#TODO Fix: Coordinates vary for some chibis
#TODO Anchor chibi transforms to (0.5, 1.0) and realign positions
define chibi_places = {
    "mid": (540, None), # cho:560 lun:580 sna:500 gen:500
    "desk": (440, None),
    "on_desk": (350, 180),
    "behind_desk": (230, 260),
    "door": (750, None),
    "base": (None, 250), # sna: 190 gen: 190
}

#TODO Define a reasonable base speed
define chibi_base_speed = 100 # pixels/sec

init -1 python:
    from collections import OrderedDict
    from fnmatch import fnmatch
    import os.path

    def update_chibi(name):
        name = "{}_chibi".format(name)
        c = getattr(renpy.store, name, None)
        if c and isinstance(c, chibi):
            c.update()
        elif config.developer:
            raise Exception("Chibi object not found. {}".format(name))

    class chibi(object):
        #TODO Document usage of chibi class
        #TODO Implement chibi_effect
        #TODO Fix chibi screen problems on rollback (eg. happens when astoria and tonks are both visible during imperio stuff)
        """
            handling (special) actions:
            * transform is selected automatically (transform chibi_{action_name}, default to chibi_base)
            * (TODO) action is switched to moving version ({action}_move) during movement

            setting chibi layers:
            * layers can be accessed as `chibi_object[key]`
            * a layer can be set to either a filename or any kind of displayable (for the `add` statement)
            * when setting a filename, this class will take into account the current (special) action and resolve
                the actual image filename relative to `image_path`
            * adding `~` as a prefix to a filename will resolve it to the chibi's base image path instead of
                the special action directory (this is useful for images that are compatible with multiple actions)
            * note that layers must be updated whenever the action changes. When this happens, the class calls
                `update_callback`, which is expected to set all the required chibi layers

            tag: name of the chibi (character name, use only letters)
            special: an action with its own set of layers (ie. images are loaded from a special directory)
            action: an action that uses the common set of layers (ie. images are loaded from the image path)
        """

        actions = (
            
        )

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
            if self.update_callback:
                self.update_callback(self)

        def move(self, x=None, y=None, speed=1.0, time_speed=None):
            pos = self.resolve_position(x,y)
            dist = math.sqrt((self.pos[0] - pos[0])**2 + (self.pos[1] - pos[1])**2)
            time = dist / (float(chibi_base_speed) * speed)

            # Temporary aid for time to speed conversion
            if time_speed and config.developer:
                print "calc-time: {}, req-time: {}, conv-speed: {}".format(time, time_speed, time/time_speed)
            
            self.flip = self.pos[0] <= pos[0]
            flip = -1 if self.flip else 1

            #TODO Implement automatic action handling for actions that have a moving version (eg. fly -> fly_move)
            if self.special in ("fly", "fly_move"):
                trans = self.resolve_transform("fly_move", self.pos, pos, self.flip, time)
                self.do("fly_move", trans)
            else:
                trans = self.resolve_transform("walk", self.pos, pos, self.flip, time)
                self.do("walk", trans)
            self.position(pos[0], pos[1])

            renpy.pause(time)
            #TODO Implement "redux_pause" so move returns before animation is finished (following lines should still execute somehow)
            if self.special in ("fly", "fly_move"):
                self.do("fly")
            else:
                self.do()

        def do(self, action=None, trans=None, flip=None):
            # Set the (special) action
            self.action = self.special = None
            if action != "walk":
                self.special = action
            else:
                self.action = action
            
            if flip != None:
                self.flip = flip
            # Set the transform (static version by default)
            if trans == None:
                trans = self.resolve_transform(action, self.pos, self.flip)
            # Hide the screen so transform is reset properly
            self.hide()
            self.transform = trans
            self.update()
            self.show()

        def position(self, x=None, y=None, flip=None):
            (x,y) = self.resolve_position(x,y)
            if flip != None:
                self.flip = flip
            self.pos = (x,y)
            # Transform position is not used/updated until do/move is called
        
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

        def resolve_transform(self, action, *args):
            # Find a transform called `chibi_{action}` for the action or its "parent" (ie. segment up to last `_`)
            # For example: `wand_casting` matches `chibi_wand_casting`, or `chibi_wand` if the former is not defined
            trans = None
            while action and trans == None:
                name = "chibi_{}".format(action)
                trans = getattr(renpy.store, name, None)
                if trans == None and '_' in action:
                    action = action.rsplit('_', 1)[0]
            if trans == None:
                name = "chibi_base"
                trans = chibi_base # Default static transform
            if not isinstance(trans, renpy.display.transform.ATLTransform):
                if config.developer:
                    raise Exception("Expected an instance of ATLTransform: {}".format(name))
                else:
                    trans = chibi_base
            return trans(*args)

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
