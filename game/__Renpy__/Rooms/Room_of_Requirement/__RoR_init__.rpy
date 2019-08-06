label __init_variables:
    #Check if you have visit room of req before

    if not hasattr(renpy.store,'temp_outfit_GLBL'): #important!
        $ temp_outfit_GLBL = None

    if not hasattr(renpy.store,'first_visit_req'): #important!
        $ first_visit_req = False

    if not hasattr(renpy.store,'mr_ev_WPIIA'):
        $ mr_ev_WPIIA = mirror_stories(
                name = "Whose points is it anyway?",
                unlockable = True,
                story_description = "Parody of the game show of \"whose points is it anyway?\"",
                start_label = "whose_points",
                authors = ["TeamSilver"],
                categories= ["Parody","Lewd", "Gameshow"],
                ach_desc = "Unlock the characters",
                content_characters = ["luna", "astoria", "hermione"]
            )

    if not hasattr(renpy.store,'mr_ev_GHE'):
        $ mr_ev_GHE = mirror_stories(
                name = "The genie, the desk and the door",
                story_description = "The genie tries to figure out how people know when he calls for them.",
                start_label = "genie_house_elf",
                authors = ["TeamSilver"],
                categories= ["Parody"],
                ach_desc = "Unlock the mirror of noisrevrep/Erised",
                content_characters = []
            )

    if not hasattr(renpy.store,'mr_ev_AOC'):
        $ mr_ev_AOC = mirror_stories(
                name = "An odd circumstance",
                unlockable = True,
                story_description = "You find yourself being confronted by a mysterious girl that seemingly seems to know you.",
                start_label = "an_odd_circumstance",
                authors = ["TeamSilver"],
                categories= ["Parody", "lewd"],
                ach_desc = "Completed Hermiones Suck It personal favours",
                content_characters = ["hermione"]
            )

    if not hasattr(renpy.store,'mr_ev_ABTTD'):
        $ mr_ev_ABTTD = mirror_stories(
                name = "A bad time to disrobe",
                unlockable = True,
                story_description = "The genie gets a hold of a invisibility cloak and puts it to good use.",
                start_label = "a_bad_time_to_disrobe",
                authors = ["TeamSilver"],
                categories= [],
                ach_desc = "Finish private favour, \"Show them to me!\" at least once.",
                content_characters = ["hermione"]
            )

    if not hasattr(renpy.store,'mr_ev_ASOC'):
        $ mr_ev_ASOC = mirror_stories(
                name = "A spaced out conversation",
                unlockable = True,
                story_description = "The genie and Snape gets real for a little bit.",
                start_label = "a_spaced_out_conversation",
                authors = ["Ignatz"],
                categories= [],
                ach_desc = "Unlocks after spending some evenings drinking by the fire with Snape.",
                content_characters = []
            )

    if not hasattr(renpy.store,'mr_ev_ABAS'):
        $ mr_ev_ABAS = mirror_stories(
                name = "A Booty at sea",
                unlockable = True,
                story_description = "The genie imagine himself to be a great pirate and roleplays his most intimate times with Hermione.",
                start_label = "anal_parit_event",
                authors = ["TeamSilver"],
                categories= [],
                ach_desc = "Finish the \"Time for Anal\" Private favours.",
                content_characters = ["hermione"]
            )

    if not hasattr(renpy.store,'mr_ev_ADR'):
        $ mr_ev_ADR = mirror_stories(
                name = "A Dark Room (Incomplete)",
                story_description = "A minigame inspired by the textbased game \"A Dark Room\".\n>WIP! It is currently incomplete but in a playable state.",
                start_label = "start_dark_room_game",
                authors = ["TeamSilver"],
                categories= ["minigame"],
                ach_desc = "",
                content_characters = []
            )

    if not hasattr(renpy.store,'mr_ev_AXmasTale'):
        $ mr_ev_AXmasTale = mirror_stories(
                name = "A Christmas Tale",
                story_description = "A surprise visit.",
                start_label = "a_christmas_tale",
                authors = ["TeamSilver"],
                categories= [],
                ach_desc = "",
                content_characters = []
            )

    if not hasattr(renpy.store,'mr_ev_PaH'):
        #Story Unlock requirements: Finish the first 3 Wizard Cards challenges.
        $ mr_ev_PaH = mirror_stories(
                name = "Previously at Hogwarts",
                story_description = "Snape tries to find a solution to stifle his anger and finds himself yet again in the Headmasters office.",
                start_label = "prev_at_hogwarts",
                authors = ["TeamSilver"],
                categories= [],
                ach_desc = "",
                content_characters = []
            )
    if not hasattr(renpy.store,'mr_ev_PR'):
        $ mr_ev_PR = mirror_stories(
                name = "Panty Raid",
                story_description = "Genie asks Hermione to go out and collect other girls panties.",
                start_label = "panty_raid_event",
                authors = ["WaxerRed"],
                categories= ["Panties fetish", "Lesbian", "Corruption"],
                ach_desc = "",
                content_characters = ["hermione"]
            )

    # WIP
    #if not hasattr(renpy.store,'mr_ev_CM'):
    #    $ mr_ev_CM = mirror_stories(
    #            name = "Class Masturbation",
    #            story_description = "Genie asks Hermione to go out and masturbate in her classes",
    #            start_label = "class_masturbation_event",
    #            authors = ["WaxerRed"],
    #            categories= [],
    #            ach_desc = "",
    #            content_characters = ["hermione"]
    #        )

    $ mr_evs_list = []
    $ mr_evs_list.append(mr_ev_PaH)
    $ mr_evs_list.append(mr_ev_AXmasTale)
    $ mr_evs_list.append(mr_ev_WPIIA)
    $ mr_evs_list.append(mr_ev_GHE)
    $ mr_evs_list.append(mr_ev_ABTTD)
    $ mr_evs_list.append(mr_ev_ASOC)
    $ mr_evs_list.append(mr_ev_ABAS)
    $ mr_evs_list.append(mr_ev_ADR)
    $ mr_evs_list.append(mr_ev_PR)
    $ mr_evs_list.append(mr_ev_AOC)

    #$ mr_evs_list.append(mr_ev_CM)

    $current_page = 0

    return

init python:

    class mirror_stories(item_class):
        start_label = ""
        authors = []
        categories = []
        story_description = ""
        ach_desc = ""
        content_characters = []

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def get_name(self):
            ret_str = "{size=12}\""+self.name+"\" by "
            for s in self.authors:
                ret_str += s +", "

            return ret_str[0:len(ret_str)-2]+"{/size}"

        def get_description(self):
            returnV = "{size=10}"
            if self.unlocked:
                returnV += "story description: " + self.story_description
            else:
                returnV += self.ach_desc

            return returnV+"{/size}"

        def get_buttom_right(self):
            return self.getCharcters()

        def get_image(self):
            if self.unlocked == False:
                return "interface/icons/icon_lock.png"
            else:
                return "interface/icons/icon_lock_open.png"

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
                    unlocked = unlocked and hermione_unlocked
                elif c == "astoria":
                    unlocked = unlocked and astoria_unlocked
                elif c == "susan":
                    unlocked = unlocked and susan_unlocked
                elif c == "cho":
                    unlocked = unlocked and cho_unlocked
                elif c == "tonks":
                    unlocked = unlocked and tonks_unlocked
                else:
                    unlocked = False
            self.unlocked = unlocked and self.unlock_check()
            if self.unlocked:
                self.unlockable = False #Makes you able to click on the item.
            return self.unlocked

        #Make a elif with the name and the criteria to unlock
        #And if you dont make any then it will all ways be true
        def unlock_check(self):
            if self.name == "A bad time to disrobe":
                return hg_pf_admire_breasts.points > 0
            elif self.name == "A spaced out conversation":
                return sna_friendship > 60
            elif self.name == "A Booty at sea":
                return hg_pf_anal_sex.points > 2
            elif self.name == "An odd circumstance":
                return hg_pf_blowjob.points > 2
            else:
                return True
