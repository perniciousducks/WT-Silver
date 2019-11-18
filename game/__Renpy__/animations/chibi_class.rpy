label chibi_test_scene:

    jump main_room

#TEMP skip say statements (for testing chibi code)
# python early:
#     def say_none(who, what, *args, **kwargs):
#         return
#     renpy.say = say_none

screen chibi(chibi_object):
    zorder chibi_object.zorder
    fixed:
        at chibi_object.transform
        fit_first True
        for d in chibi_object.displayables():
            add d
        frame: # Debug frame
            background "#00ff0055"

init -1 python:
    from collections import OrderedDict

    def update_chibi(name):
        get_chibi_object(name).update()

    def get_chibi_object(name):
        name = "{}_chibi".format(name)
        c = getattr(renpy.store, name, None)
        if c and isinstance(c, chibi):
            return c
        else:
            # Fail early, returning None is no good
            raise Exception("Chibi object not found. {}".format(name))

    class chibi(object):
        #TODO Document usage of chibi class
        #TODO Implement chibi_effect
        #TODO Fix chibi screen problems on rollback (eg. happens when astoria and tonks are both visible during imperio stuff)
        #TODO Fix: Coordinates vary for some chibis (maybe resolve positions outside of chibi class)
        #TODO Anchor chibi transforms to (0.5, 1.0) and realign positions

        """
            handling actions:
            * by action definition

            setting chibi layers:
            * layers can be accessed as `chibi_object[key]`
            * a layer can be set to either a filename or any kind of displayable (for the `add` statement)
            * when setting a filename, this class will take into account the current (special) action and resolve
                the actual image filename relative to `image_path`
            * adding `~` as a prefix to a filename will resolve it to the chibi's base image path instead of
                the special action directory (this is useful for images that are compatible with multiple actions)
            * the class will update layers whenever the action changes by calling `update_callback`,
                which is expected to set all the required chibi layers

            tag: name of the chibi (character name, use only letters)
            special: an action with its own set of layers (ie. images are loaded from a special directory)
            action: an action that uses the common set of layers (ie. images are loaded from the image path)
            places:
        """

        # action: (is_special, transform_name, move_action_name)
        actions = {
            None: (False, "chibi_base", "walk"),
            "walk": (False, "chibi_walk"),
            "fly": (True, "chibi_fly", "fly_move"),
            "fly_move": (True, "chibi_fly_move"),
            "wand": (True, "chibi_wand", "walk"),
        }

        # place: (x, y)
        places = {
            "base": (None, 250), # sna: 190 (240/245?) gen: 190
            "mid": (540, None), # cho:560 lun:580 sna:500 gen:500
            "desk": (440, None),
            "on_desk": (350, 180),
            "behind_desk": (230, 260), # gen:210, 190
            "door": (750, None),
        }

        def __init__(self, tag, layers, update_callback, zorder=3, speed=100, image_path=None, actions=None, places=None):
            self.tag = tag
            self.layers = OrderedDict([(k, None) for k in layers])
            self.update_callback = update_callback
            self.zorder = zorder
            self.speed = speed # pixels/sec

            if image_path:
                self.image_path = image_path
            else:
                self.image_path = "characters/{}/chibis".format(tag)
            
            if actions:
                # Override class variable for this instance
                self.actions = dict(chibi.actions)
                self.actions.update(actions)

            if places:
                # Override class variable for this instance
                self.places = dict(chibi.places)
                self.places.update(places)

            self.pos = (0,0)
            self.flip = False
            self.action = None
            self.action_info = self.resolve_action(None)
            self.special = None
            self.transform = None

            # Define a screen for the chibi
            self.screen_tag = "{}_chibi".format(tag)
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

        def move(self, x=None, y=None, speed=1.0, time_speed=None, redux=False):
            pos = self.resolve_position(x,y)
            dist = math.sqrt((self.pos[0] - pos[0])**2 + (self.pos[1] - pos[1])**2)
            time = dist / (float(self.speed) * speed)
            
            self.flip = self.pos[0] <= pos[0]

            #TODO Chibi action after moving should be configurable per action (default to stand/None)
            old_action = self.action
            if len(self.action_info) == 3:
                # Action info provides a move action
                move_action = self.action_info[2]
            else:
                # Current action is already a move action
                move_action = self.action
            
            # Apply the action with a transform
            trans_name = self.resolve_action(move_action)[1]
            trans = self.resolve_transform(trans_name, self.pos, pos, self.flip, time)
            self.do(move_action, trans)
            self.position(pos[0], pos[1])

            #TODO Add usage of redux parameter to chibi walk labels
            if redux:
                # Reduce the pause and don't do the old action
                if not isinstance(redux, bool):
                    time -= float(redux)
                if time > 0:
                    renpy.pause(time)
            else:
                # Pause while moving and then do the old action
                renpy.pause(time)
                if old_action != move_action:
                    self.do(old_action)

        def do(self, action=None, trans=None):
            self.action = action
            self.action_info = self.resolve_action(action)
            self.special = self.action_info[0]

            # Set the transform (static version by default)
            if trans == None:
                trans = self.resolve_transform(self.action_info[1], self.pos, self.flip)

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
            # Current position is not used until do/move is called
        
        def resolve_position(self, x=None, y=None):
            # Compute new position from place keywords (or just ints) for one or both of the coordinates
            if not isinstance(x, int):
                if x == None:
                    x = self.pos[0]
                elif x in self.places:
                    x = self.places[x][0] or self.pos[0]
                else:
                    x = int(x)
            if not isinstance(y, int):
                if y == None:
                    y = self.pos[1]
                elif y in self.places:
                    y = self.places[y][1] or self.pos[1]
                else:
                    y = int(y)
            return (x,y)

        def resolve_transform(self, name, *args):
            # Get transform from the store by name and apply arguments
            trans = getattr(renpy.store, name, None)
            if not isinstance(trans, renpy.display.transform.ATLTransform):
                if config.developer:
                    raise Exception("Expected an instance of ATLTransform: {}".format(name))
                else:
                    trans = chibi_base # Attempt to save the player from error
            return trans(*args)

        def resolve_action(self, name):
            # Get action info by name (falling back to "parent" action or default)
            while True:
                if name in self.actions:
                    return self.actions[name]
                elif '_' in name:
                    name = name.rsplit('_', 1)[0]
                else:
                    return self.actions[None]

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
                # Assume value is a filename and resolve it
                if value.startswith('~') or not self.special:
                    # Avoid special directory
                    value = self.image_path + "/" + value
                else:
                    value = self.image_path + "/" + self.action + "/" + value
            
            self.layers[key] = value
