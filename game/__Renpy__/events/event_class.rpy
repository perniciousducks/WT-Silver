init python:
    class event_class(object):
        title     = ""
        _tier     = 0
        _max_tiers = 0
        level     = 0
        max_level = 3
        points    = 0
        counter   = 0

        start_label = ""
        inProgress = False
        hint = False

        events = []

        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

            if self.events == []:
                raise Exception('Events: "events" list was not defined in event_class.')

            self._max_tiers = len(self.events)

            for i in xrange(self._max_tiers):
                for j in xrange(len(self.events[i])):
                    self.events[i][j] += [False]

        def start(self):
            for i in xrange(len(self.events[self._tier])):
                if self.events[self._tier][i][1] == False:
                    self.events[self._tier][i][1] = True
                    return renpy.jump(self.events[self._tier][i][0])
            events_filtered = filter(lambda x: '_intro' not in x[0], self.events[self._tier])
            random_event = events_filtered[random.randint(0, len(events_filtered)-1)][0]
            return renpy.jump(random_event)

        def start_advance(self):
            for i in xrange(self._max_tiers):
                for j in xrange(len(self.events[i])):
                    if self.events[i][j][1] == False:
                        self.events[i][j][1] = True
                        self._tier = i
                        return renpy.jump(self.events[i][j][0])
            events_filtered = filter(lambda x: '_intro' not in x[0], self.events[self._tier])
            random_event = events_filtered[random.randint(0, len(events_filtered)-1)][0]
            return renpy.jump(random_event)

        def getMenuText(self):
            heart_list = []
            menu_text = None
            for i in xrange(self._max_tiers):
                if i < self._tier:
                    heart_list.append("interface/icons/small/star_yellow.png")
                else:
                    heart_list.append("interface/icons/small/star_empty.png")
            # Before Text
            if self.hint:
                menu_text = "{image=interface/check_True.png} "
            # Main Text
            if menu_text != None:
                menu_text += "\""+self.title+"\" "
            else:
                menu_text = "\""+self.title+"\" "
            # After Text
            for heart in heart_list:
                menu_text += "{image="+heart+"}"

            return menu_text
            
        @property
        def tier(self):
            return self._tier+1
            
        @tier.setter
        def tier(self, value):
            self._tier = max(0, min(value-1, self._max_tiers))