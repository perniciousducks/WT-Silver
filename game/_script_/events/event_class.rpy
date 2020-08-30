init python:
    class quest_class(object):
        def __init__(self, **kwargs):
            self.title = ""
            self.hint = ""

            self.__dict__.update(kwargs)

        def status(self):
            return list(self.__dict__)


    class counter_class(object):
        def __init__(self, **kwargs):
            self.title       = ""
            self.bool        = False # Can me switched to 'True' and 'False' for events
            self.trigger     = False # Can only be switched to 'True'
            self.counter     = 0

            self.hg_counter  = 0 # Hermione
            self.gw_counter  = 0 # Ginny
            self.cc_counter  = 0 # Cho
            self.ll_counter  = 0 # Luna
            self.sb_counter  = 0 # Susan
            self.ag_counter  = 0 # Astoria
            self.dg_counter  = 0 # Daphne
            self.pp_counter  = 0 # Pansy
            self.ss_counter  = 0 # Snape
            self.nt_counter  = 0 # Tonks

            self.__dict__.update(kwargs)

        def status(self):
            return list(self.__dict__)

        def triggered(self):
            self.trigger = True
            self.counter += 1
            return


    class event_class(object):
        """
        Handles and tracks event progression.

        Event labels ending with "_intro" are treated as one-time events. Otherwise the event can be repeated.

        `tier` (int): The current tier number, which determines the set of events to run.
        `counter` (int): The number of successfully completed events.
        `points` (int): The number of successfully completed events in the current tier.
        """

        def __init__(self, **kwargs):
            self.title     = ""
            self.hint      = ""
            self.counter   = 0

            self.start_label = ""
            self.start_tier = 0
            self.inProgress = False

            self.events = []

            self.icons = []
            self.iconset = []

            # Private attributes
            self._tier     = 0
            self._points    = 0

            self.__dict__.update(kwargs)

            if self.events == []:
                raise Exception('Events: "events" list was not defined in event_class.')

            # Insert empty list for 'empty' tiers to avoid wrong lookup later on
            for i in xrange(self.start_tier-1):
                self.events.insert(0, [])

            self._max_tiers = len(self.events)

            if self.iconset == []:
                raise Exception('Events: "iconset" list was not defined in event_class. You need to add at least one set of icons.')
            elif len(self.iconset) < self._max_tiers:
                for i in xrange(self._max_tiers-len(self.iconset)):
                    self.iconset.append([self.iconset[0][0], self.iconset[0][1]])

            for i in xrange(self._max_tiers):
                for j in xrange(len(self.events[i])):
                    self.events[i][j] += [False]

        def start(self):
            self.counter += 1
            self.points += 1
            for i in xrange(len(self.events[self._tier])):
                if self.events[self._tier][i][1] == False:
                    self.events[self._tier][i][1] = True
                    return renpy.jump(self.events[self._tier][i][0])
            events_filtered = filter(lambda x: '_intro' not in x[0], self.events[self._tier])
            random_event = events_filtered[random.randint(0, len(events_filtered)-1)][0]
            return renpy.jump(random_event)

        def change_icon(self, a="heart_half", b="heart_red"):
            for icon in self.iconset:
                if icon[1] == a:
                    icon[1] = b

        def start_advance(self):
            self.counter += 1
            self.points += 1
            for i in xrange(self._max_tiers):
                for j in xrange(len(self.events[i])):
                    if self.events[i][j][1] == False:
                        self.events[i][j][1] = True
                        self._tier = i
                        return renpy.jump(self.events[i][j][0])
            events_filtered = filter(lambda x: '_intro' not in x[0], self.events[self._tier])
            random_event = events_filtered[random.randint(0, len(events_filtered)-1)][0]
            return renpy.jump(random_event)

        def get_menu_item(self, disabled=False, return_value=None):
            menu_text = ""

            if self.hint:
                menu_text += "{image=interface/check_True.webp}"

            if self.title:
                menu_text += "\"{}\"".format(self.title)

            if disabled:
                menu_text = "{color=[menu_disabled]}" + menu_text + "{/color}"

            imagepath = "interface/icons/small/"

            icon = None
            if len(self.icons) > 0 and self.icons[self._tier]:
                icon = imagepath + self.icons[self._tier] + ".webp"

            progress = []
            for e in self.events[self._tier]:
                if e[1]:
                    progress.append(imagepath + self.iconset[self._tier][1] + ".webp")
                else:
                    progress.append(imagepath + self.iconset[self._tier][0] + ".webp")

            if return_value is None:
                return_value = "block" if disabled else self.start_label

            action = renpy.ui.ChoiceReturn(None, return_value, kwargs={ "icon": icon, "progress": progress })

            return (menu_text, action)

        def fail(self):
            self.counter = max(0, self.counter-1)
            self.points -= 1
            self.events[self._tier][self._points][1] = False
            return

        # Reset the event completely
        def reset(self):
            for i in xrange(self._max_tiers):
                for j in xrange(len(self.events[i])):
                    self.events[i][j][1] = False
            self._tier = 0
            self._points = 0
            self.counter = 0
            self.inProgress = False

        def status(self, value):
            status_list = []
            for item in self.events[value-1]:
                status_list += [item[1]]
            return status_list

        def is_complete(self, ignore_in_progress=False):
            return self.tier == len(self.events) and self.is_tier_complete(ignore_in_progress=ignore_in_progress)

        def is_tier_complete(self, ignore_in_progress=False):
            return self.points == len(self.events[self._tier]) and (not self.inProgress or ignore_in_progress)

        def is_event_complete(self, tier, event):
            return bool(self.events[tier-1][event-1][1])

        @property
        def points(self):
            return self._points

        @points.setter
        def points(self, value):
            self._points = max(0, min(value, len(self.events[self._tier])))

        @property
        def tier(self):
            return self._tier+1

        @tier.setter
        def tier(self, value):
            if value > self._tier+1:
                self._points = 0
            self._tier = max(0, min(value-1, self._max_tiers-1))

        @property
        def max_tiers(self):
            return self._max_tiers

        @max_tiers.setter
        def max_tiers(self, value):
            pass

    class stats_class(dict):

        def __delitem__(self, key):
            """Override delitem method to delete inner dictionary key."""
            del self[key]

        def __missing__(self, key):
            """Return zero if key does not exist in the inner dictionary."""
            return 0

        def __setattr__(self, name, value):
            """Override setattr method to add attributes as keys and values in the inner dictionary."""
            self[name] = value

        def __getattr__(self, name):
            """Override getattr method to return a value of the key from the inner dictionary."""
            # Skip protected attributes and/or injected Ren'py methods
            if not name.startswith("_"):
                return self[name]
            raise AttributeError("'"+self.__class__.__name__+"' has no attribute '"+name+"'")

        def status(self):
            """Print currently defined keys and values in the console."""
            for key, value in self.iteritems():
                print key + " == " + str(value)
            return

        def reset(self):
            """Reset all key values back to default values depending on the value type."""
            for key in self.iterkeys():
                if isinstance(self[key], (float, int)):
                    self[key] = 0
                elif isinstance(self[key], bool):
                    self[key] = False
                else:
                    pass
            return
