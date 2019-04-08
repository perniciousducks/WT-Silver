init python:
    class event_class(object):
        name = ""
        events = []
        max_tiers = 0
        tier = 0
        
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
            
            if self.events == []:
                raise Exception('Events: "events" list was not defined in event_class.')

            self.max_tiers = len(self.events)

            for i in xrange(0, self.max_tiers):
                for j in xrange(0, len(self.events[i])):
                    self.events[i][j] += [False]
                    
        def start(self):
            for i in xrange(0, len(self.events[self.tier])):
                if self.events[self.tier][i][1] == False:
                    self.events[self.tier][i][1] = True
                    return renpy.jump(self.events[self.tier][i][0])
            events_filtered = filter(lambda x: '_intro' not in x[0], self.events[self.tier])
            random_event = events_filtered[random.randint(0, len(events_filtered)-1)][0]
            return renpy.jump(random_event)
            
        def start_advance(self):
            for i in xrange(0, self.max_tiers):
                for j in xrange(0, len(self.events[i])):
                    if self.events[i][j][1] == False:
                        self.events[i][j][1] = True
                        self.tier = i
                        return renpy.jump(self.events[i][j][0])
            events_filtered = filter(lambda x: '_intro' not in x[0], self.events[self.tier])
            random_event = events_filtered[random.randint(0, len(events_filtered))][0]
            return renpy.jump(random_event)