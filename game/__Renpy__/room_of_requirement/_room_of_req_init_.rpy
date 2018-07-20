label __init_variables:
    #Check if you have visit room of req before
    if not hasattr(renpy.store,'first_visit_req'): #important!
        $ first_visit_req = False
        
    if not hasattr(renpy.store,'mr_ev_WPIIA'):
        $mr_ev_WPIIA = mirror_stories(
                title = "Whose points is it anyway?",
                start_label = "whose_points",
                authors = ["Johnny"],
                categories= ["Parody","Lewd", "Gameshow",""],
                ach_desc = "Unlock the mirror of noisrevrep/Erised"
            )
            
    
    $ mr_evs_list = []
    $ mr_evs_list.append(mr_ev_WPIIA)
    $ mr_evs_list.append(mr_ev_WPIIA)
    $ mr_evs_list.append(mr_ev_WPIIA)
    $ mr_evs_list.append(mr_ev_WPIIA)
    $ mr_evs_list.append(mr_ev_WPIIA)
    $ mr_evs_list.append(mr_ev_WPIIA)
    $ mr_evs_list.append(mr_ev_WPIIA)
    $ mr_evs_list.append(mr_ev_WPIIA)
    
        
init python:
    class mirror_stories:
        title = ""
        unlocked = False
        start_label = ""
        authors = []
        categories = []
        story_description = ""
        ach_desc = ""
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def getMenuText(self):
            ret_str = "\""+self.title+"\" by "
            for s in self.authors:
                ret_str += s +", "

            return ret_str[0:len(ret_str)-2]
       
        def getDescription(self):
            returnV = "{size=12}"
            if self.unlocked:
                returnV += "story description: " + self.story_description
            else:
                returnV += self.ach_desc
                    
            return returnV+"{/size}"  