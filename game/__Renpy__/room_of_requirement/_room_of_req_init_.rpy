label __init_variables:
    #Check if you have visit room of req before
    if not hasattr(renpy.store,'first_visit_req'): #important!
        $ first_visit_req = False
        
    if not hasattr(renpy.store,'mr_ev_WPIIA'):
        $mr_ev_WPIIA = mirror_stories(
                title = "Whose points is it anyway?",
                start_label = "whose_points",
                authors = ["Johnny",""],
                categories= ["Parody","Lewd", "Gameshow",""],
                ach_desc = "Unlock the mirror of noisrevrep/Erised"
            )
    
    $ mr_evs_list = []
    $ mr_evs_list.append(mr_ev_WPIIA)
    
        
init python:
    class mirror_stories:
        title = ""
        unlocked = False
        start_label = ""
        authors = []
        categories = []
        ach_desc = ""
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def getMenuText(self):
            ret_str = self.title
            if self.unlocked:
               ret_str += "  {image=images/room_of_requirement/unlocked_icon.png}"
            else:
               ret_str += "  {image=images/room_of_requirement/lock_icon.png}"
            return ret_str