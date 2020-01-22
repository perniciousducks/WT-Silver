
# Screen used by chibi class (each chibi object derives its own uniquely tagged screen from this one)
screen chibi(chibi_object):
    zorder chibi_object.zorder
    sensitive False
    fixed:
        at chibi_object.transform
        fit_first True
        for d in chibi_object.displayables():
            add d
        # frame: # Debug frame
        #     background "#00ff0055"

screen chibi_emote(emote, chibi_object):
    zorder chibi_object.zorder
    sensitive False
    add "emo_{}".format(emote):
        at emote_effect
        anchor (0.5, 1.0)
        pos chibi_object.pos
        offset ((75, -200) if chibi_object.tag in ("genie", "snape") else (50, 0))

label chibi_emote(emote, name):
    python:
        if emote == "hide":
            emote = None
        get_chibi_object(name).emote(emote)

init -1 python:
    def update_chibi(name):
        # Update the chibi object for a given character
        get_chibi_object(name).update()

    def get_chibi_object(name):
        # Get a chibi object by its character's name
        name = "{}_chibi".format(name)
        c = getattr(renpy.store, name, None)
        if c and isinstance(c, Chibi):
            return c
        else:
            # Fail early, returning None is no good
            raise Exception("Chibi object not found. {}".format(name))

    class Chibi(object):
        """ Manages a character's chibi.

            Actions:
            * Represent what a chibi is doing.
            * Determine which transform is applied.
            * Allow layers to be changed to the relevant images (via update callback).
            
            There are two types of actions, one is used in place and the other while moving.

            Actions are defined in the `actions` dict as a tuple: (special, transform, move_action).
            * `special` (bool) specifies whether layer images should come from a folder with the same name as the action.
              This can be useful to prevent repetitive code in update callbacks.
            * `transform` (string) is the name of the transform that is used for this action.
              It will be combined with a base transform.
            * `move_action` (string) if set, it's the action that will be used when the chibi starts moving after the current action.
              It should not be set for move actions.
            
            Layers:
            A chibi is made up of one or more named layers. These are cleared on update and should be set by a callback function.
            * Layers can be accessed as `chibi_object[key]`.
            * A layer can be set to either a filename or any kind of displayable.
            * When setting an image filename, this class will look for it in `image_path` (or `image_path/action` if the action is special).
            * Adding `~` as a prefix to a filename will ignore the special action folder.
              This can be useful for images that are compatible with multiple actions.
            * Layers are updated whenever the action changes by calling `update_callback`, which is expected to set the layers again.
        """

        actions = {
            None: (False, None, "walk"),
            "walk": (False, "chibi_walk"),
            "fly": (True, "chibi_fly", "fly_move"),
            "fly_move": (True, "chibi_fly_move"),
            "wand": (True, "chibi_wand", "walk"),
        }

        def __init__(self, tag, layers, update_callback, zorder=3, speed=100, image_path=None, actions=None, places=None):
            self.tag = tag
            
            # Use a tuple/list to specify the order of layers in a dict
            self.layers_order = layers
            self.layers = dict([(k, None) for k in layers])

            self.update_callback = update_callback

            if image_path:
                self.image_path = image_path
            else:
                self.image_path = "characters/{}/chibis".format(tag)
            
            if actions:
                # Override class variable for this instance
                self.actions = dict(Chibi.actions)
                self.actions.update(actions)

            self.zorder = zorder
            self.speed = speed # pixels/sec

            self.pos = (0,0)
            self.flip = False
            self.action = None
            self.action_info = self.resolve_action(None)
            self.special = None
            self.transform = None

            # Define a screen for the chibi
            self.screen_tag = "{}_chibi".format(tag)
            renpy.define_screen(self.screen_tag, Chibi._screen, tag=self.screen_tag, zorder="chibi_object.zorder")

            # Define a screen for the chibi emote
            self.emote_tag = "{}_chibi_emote".format(tag)
            renpy.define_screen(self.emote_tag, Chibi._emote_screen, tag=self.emote_tag, zorder="chibi_object.zorder")

        @staticmethod
        def _screen(chibi_object, **kwargs):
            # Emulate a Ren'py `use` statement to derive a chibi screen from the generic one
            renpy.use_screen("chibi", chibi_object, _name=kwargs["_name"], _scope=kwargs["_scope"])

        @staticmethod
        def _emote_screen(emote, chibi_object, **kwargs):
            # Emulate a Ren'py `use` statement to derive a chibi_emote screen from the generic one
            renpy.use_screen("chibi_emote", emote, chibi_object, _name=kwargs["_name"], _scope=kwargs["_scope"])

        def show(self):
            renpy.show_screen(self.screen_tag, chibi_object=self)

        def hide(self):
            renpy.hide_screen(self.screen_tag)
            renpy.hide_screen(self.emote_tag)

        def emote(self, emote=None):
            if renpy.get_screen(self.emote_tag):
                renpy.hide_screen(self.emote_tag)
                renpy.pause(0.2) # Pause for duration of emote_effect
            if emote:
                renpy.show_screen(self.emote_tag, emote=emote, chibi_object=self)
        
        def update(self):
            self.clear()
            if self.update_callback:
                self.update_callback(self)

        def move(self, x=None, y=None, speed=1.0, reduce=False):
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
            trans = self.resolve_transform(trans_name, self.pos, pos, time)
            self.do(move_action, trans)
            self.position(pos[0], pos[1])

            if reduce:
                # Reduce the pause and don't do the old action
                if not isinstance(reduce, bool):
                    time -= float(reduce)
                if time > 0:
                    renpy.pause(time)
            else:
                # Pause while moving and then do the old action
                renpy.pause(time)
                if old_action != move_action:
                    self.do(old_action)
        
        def path_move(self, path, speed=1.0):
            for i in xrange(len(path)):
                x,y = path[i]
                reduce = i < len(path)-1 # Reduce all except last node
                self.move(x, y, speed, reduce)

        def do(self, action=None, trans=None):
            self.action = action
            self.action_info = self.resolve_action(action)
            self.special = self.action_info[0]

            # Set the transform (static version by default)
            if trans == None:
                trans = self.resolve_transform(self.action_info[1])

            # Hide the screen so transform is reset properly
            self.hide()
            self.transform = trans
            self.update()
            self.show()

        def position(self, x=None, y=None, flip=None):
            """Set the position to be used on next update."""
            (x,y) = self.resolve_position(x,y)
            if flip != None:
                self.flip = flip
            self.pos = (x,y)
        
        def resolve_position(self, x=None, y=None):
            """Compute new position from place keywords (or just ints) for one or both of the coordinates."""
            return ChibiRoom.place((x,y), self.pos)

        def resolve_transform(self, name, *args):
            """Get transform from the store by name and apply arguments."""
            if name:
                trans = getattr(renpy.store, name, None)
                if isinstance(trans, renpy.display.transform.ATLTransform):
                    # Combine with base transform
                    return combine_transforms(self.base_transform(), trans(*args))
                elif config.developer:
                    raise Exception("Expected a transform: {}".format(name))
            # No transform was given or found
            return self.base_transform()

        def base_transform(self):
            scale = ChibiRoom.get().scale
            return chibi_base(self.pos, self.flip, scale)

        def resolve_action(self, name):
            """Get action info by name (falling back to "parent" action or default)."""
            while True:
                if name in self.actions:
                    return self.actions[name]
                elif '_' in name:
                    name = name.rsplit('_', 1)[0]
                else:
                    return self.actions[None]

        def displayables(self):
            """Yields non-empty layers in an iterable manner."""
            for k in self.layers_order:
                d = self.layers.get(k, None)
                if d != None:
                    yield d

        def clear(self):
            for k in self.layers.iterkeys():
                self.layers[k] = None

        def __getitem__(self, key):
            return self.layers[key]
        
        def __setitem__(self, key, value):
            if key not in self.layers:
                # Layer must be defined at init
                raise KeyError(key)
            
            if isinstance(value, basestring) and '.' in value:
                # Assume value is a filename and resolve it
                if value.startswith('~') or not self.special:
                    # Avoid special directory
                    value = self.image_path + "/" + value.lstrip("~/")
                else:
                    value = self.image_path + "/" + self.action + "/" + value
            
            self.layers[key] = value
    
    class ChibiRoom(object):
        """Defines chibi scale factor and named positions (places) for a room."""

        # Rooms by name
        rooms = dict()

        def __init__(self, name, scale, places):
            self.name = name
            self.scale = scale
            self.places = places

            ChibiRoom.rooms[self.name] = self

        def resolve(self, p, d, x_or_y):
            """Resolve p as coordinate, if None return d, else return p as integer."""
            if not isinstance(p, int):
                if p == None:
                    return d
                elif p in self.places:
                    return self.places[p][int(x_or_y)] or d
                else:
                    return int(p)
            return p

        @staticmethod
        def get(room=None):
            room = room or renpy.store.current_room
            chibi_room = ChibiRoom.rooms.get(room, None)
            if not chibi_room:
                raise Exception("Chibi room is not defined for {}".format(room))
            return chibi_room
        
        @staticmethod
        def place(place, position, room=None):
            """Resolve place coordinates in the current room, or a given room (by name)."""
            chibi_room = ChibiRoom.get(room)
            x = chibi_room.resolve(place[0], position[0], False)
            y = chibi_room.resolve(place[1], position[1], True)
            return (x,y)
