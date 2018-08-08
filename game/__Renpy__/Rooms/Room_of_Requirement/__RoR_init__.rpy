label __init_variables:
    #Check if you have visit room of req before
    
    if not hasattr(renpy.store,'first_visit_req'): #important!
        $ first_visit_req = False
        
    if not hasattr(renpy.store,'mr_ev_WPIIA'):
        $mr_ev_WPIIA = mirror_stories(
                title = "Whose points is it anyway?",
                story_description = "Parody of the game show of \"whose points is it anyway?\"",
                start_label = "whose_points",
                authors = ["Johnny"],
                categories= ["Parody","Lewd", "Gameshow"],
                ach_desc = "Unlock the characters",
                content_characters = ["luna", "astoria", "hermione"]
            )
    
    if not hasattr(renpy.store,'mr_ev_GHE'):
        $mr_ev_GHE = mirror_stories(
                title = "The genie, the desk and the door",
                story_description = "The genie tries to figure out how people know when he calls for them.",
                start_label = "genie_house_elf",
                authors = ["Johnny"],
                categories= ["Parody"],
                ach_desc = "Unlock the mirror of noisrevrep/Erised",
                content_characters = []
            )
    if not hasattr(renpy.store,'mr_ev_ABTTD'):
        $mr_ev_ABTTD = mirror_stories(
                title = "A bad time to disrobe.",
                story_description = "The genie gets a hold of a invisibility cloak and puts it to good use.",
                start_label = "a_bad_time_to_disrobe",
                authors = ["Johnny"],
                categories= [],
                ach_desc = "Finish private favour, \"Show them to me!\" at least once.",
                content_characters = ["hermione"]
            )
    
    
    
    $ mr_evs_list = []
    $ mr_evs_list.append(mr_ev_WPIIA)
    $ mr_evs_list.append(mr_ev_GHE)
    $ mr_evs_list.append(mr_ev_ABTTD)
    
    $currentpage = 0
        
init python:
    class mirror_stories:
        title = ""
        unlocked = False
        start_label = ""
        authors = []
        categories = []
        story_description = ""
        ach_desc = ""
        content_characters = []
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def getMenuText(self):
            ret_str = "{size=12}\""+self.title+"\" by "
            for s in self.authors:
                ret_str += s +", "

            return ret_str[0:len(ret_str)-2]+"{/size}"
       
        def getDescription(self):
            returnV = "{size=10}"
            if self.unlocked:
                returnV += "story description: " + self.story_description
            else:
                returnV += self.ach_desc
                    
            return returnV+"{/size}" 
        
        def getCharcters(self):
            ret_str = ""
            for c in self.content_characters:
                if c == "luna":
                    ret_str += "{image=interface/room_of_req/luna_icon.png}"
                elif c == "hermione":
                    ret_str += "{image=interface/room_of_req/hermione_icon.png}"
                elif c == "astoria":
                    ret_str += "{image=interface/room_of_req/astoria_icon.png}"
                elif c == "susan":
                    ret_str += "{image=interface/room_of_req/susan_icon.png}"
                elif c == "cho":
                    ret_str += "{image=interface/room_of_req/cho_icon.png}"
                elif c == "tonks":
                    ret_str += "{image=interface/room_of_req/tonks_icon.png}"
                else:
                    ret_str += "{image=heart_00}"
            
            return ret_str
        
        def checkLock(self):
            unlocked = True
            for c in self.content_characters:
                if c == "luna":
                    unlocked = unlocked and luna_unlocked
                elif c == "hermione":
                    unlocked = unlocked and summoning_hermione_unlocked
                elif c == "astoria":
                    unlocked = unlocked and astoria_unlocked
                elif c == "susan":
                    unlocked = unlocked and susan_unlocked
                elif c == "cho":
                    unlocked = unlocked and cho_met
                elif c == "tonks":
                    unlocked = unlocked and tonks_unlocked
                else:
                    unlocked = False
            self.unlocked = unlocked and self.unlock_check()
            return self.unlocked
            
        #Make a elif with the title and the cretevia to unlock
        #And if you dont make any then it will all ways be true
        def unlock_check(self):
            if self.title == "A bad time to disrobe.":
                return hg_pf_ShowThemToMe_OBJ.points > 0
            else:
                return True
            