label __init_variables:
    if not hasattr(renpy.store,'hg_pf_TalkToMe_OBJ'): #important!
        $ hg_pf_TalkToMe_OBJ = personal_favor(
            imagination_level = 0,
            menu_text = "Talk to me",
            start_label = "hg_pf_TalkToMe",
            costume_event = False
        )

    if not hasattr(renpy.store,'hg_pf_NicePanties_OBJ'): #important!
        $ hg_pf_NicePanties_OBJ = personal_favor(
            imagination_level = 0,
            menu_text = "Nice panties",
            start_label = "hg_pf_NicePanties",
            costume_event = False
        )

    if not hasattr(renpy.store,'hg_pf_BreastMolester_OBJ'): #important!
        $ hg_pf_BreastMolester_OBJ = personal_favor(
            imagination_level = 2,
            menu_text = "Breast molester",
            start_label = "hg_pf_BreastMolester",
            costume_event = False
        )

    if not hasattr(renpy.store,'hg_pf_ButtMolester_OBJ'): #important!
        $ hg_pf_ButtMolester_OBJ = personal_favor(
            imagination_level = 2,
            menu_text = "Butt molester",
            start_label = "hg_pf_ButtMolester",
            costume_event = False
        )

    if not hasattr(renpy.store,'hg_pf_ShowThemToMe_OBJ'): #important!
        $ hg_pf_ShowThemToMe_OBJ = personal_favor(
            imagination_level = 3,
            menu_text = "Show them to me!",
            start_label = "hg_pf_ShowThemToMe",
            costume_event = False
        )

    if not hasattr(renpy.store,'hg_pf_DanceForMe_OBJ'): #important!
        $ hg_pf_DanceForMe_OBJ = personal_favor(
            imagination_level = 3,
            menu_text = "Dance for me!",
            start_label = "hg_pf_DanceForMe",
            costume_event = False
        )

    if not hasattr(renpy.store,'hg_pf_ShowMeYourAss_OBJ'): #important!
        $ hg_pf_ShowMeYourAss_OBJ = personal_favor(
            imagination_level = 3,
            menu_text = "Show me that ass!",
            start_label = "hg_pf_ShowMeYourAss",
            costume_event = False
        )

    if not hasattr(renpy.store,'hg_pf_TouchYourself_OBJ'): #important!
        $ hg_pf_TouchYourself_OBJ = personal_favor(
            imagination_level = 4,
            menu_text = "Touch Yourself!",
            start_label = "hg_pf_TouchYourself",
            costume_event = False
        )

    if not hasattr(renpy.store,'hg_pf_TouchMe_OBJ'): #important!
        $ hg_pf_TouchMe_OBJ = personal_favor(
            imagination_level = 4,
            menu_text = "Touch me!",
            start_label = "hg_pf_TouchMe",
            costume_event = False
        )

    if not hasattr(renpy.store,'hg_pf_TitJob_OBJ'): #important!
        $ hg_pf_TitJob_OBJ = personal_favor(
            imagination_level = 4,
            menu_text = "Let me fuck them!",
            start_label = "hg_pf_TitJob",
            costume_event = False
        )

    if not hasattr(renpy.store,'hg_pf_SuckIt_OBJ'): #important!
        $ hg_pf_SuckIt_OBJ = personal_favor(
            imagination_level = 4,
            menu_text = "Suck it!",
            start_label = "hg_pf_SuckIt",
            costume_event = False
        )

    if not hasattr(renpy.store,'hg_pf_LetsHaveSex_OBJ'): #important!
        $ hg_pf_LetsHaveSex_OBJ = personal_favor(
            imagination_level = 5,
            menu_text = "Let's have sex!",
            start_label = "hg_pf_LetsHaveSex",
            costume_event = False
        )

    if not hasattr(renpy.store,'hg_pf_TimeForAnal_OBJ'): #important!
        $ hg_pf_TimeForAnal_OBJ = personal_favor(
            imagination_level = 5,
            menu_text = "Time for anal!",
            start_label = "hg_pf_TimeForAnal",
            costume_event = False
        )


    $ hg_pf_list = []
    $ hg_pf_list.append(hg_pf_TalkToMe_OBJ)
    $ hg_pf_list.append(hg_pf_NicePanties_OBJ)
    $ hg_pf_list.append(hg_pf_BreastMolester_OBJ)
    $ hg_pf_list.append(hg_pf_ButtMolester_OBJ)
    $ hg_pf_list.append(hg_pf_ShowThemToMe_OBJ)
    $ hg_pf_list.append(hg_pf_DanceForMe_OBJ)
    $ hg_pf_list.append(hg_pf_ShowMeYourAss_OBJ)
    $ hg_pf_list.append(hg_pf_TouchMe_OBJ)
    $ hg_pf_list.append(hg_pf_TitJob_OBJ)
    $ hg_pf_list.append(hg_pf_TouchYourself_OBJ)
    $ hg_pf_list.append(hg_pf_SuckIt_OBJ)
    $ hg_pf_list.append(hg_pf_LetsHaveSex_OBJ)
    $ hg_pf_list.append(hg_pf_TimeForAnal_OBJ)



    if not hasattr(renpy.store,'hg_pr_FlirtClassmate_OBJ'): #important!
        $ hg_pr_FlirtClassmate_OBJ = public_request()
    $ hg_pr_FlirtClassmate_OBJ.imagination_level = 0
    $ hg_pr_FlirtClassmate_OBJ.menu_text = "She's a flirt"
    $ hg_pr_FlirtClassmate_OBJ.start_label = "hg_pr_FlirtClassmate"
    $ hg_pr_FlirtClassmate_OBJ.complete_label = "hg_pr_FlirtClassmate_complete"

    if not hasattr(renpy.store,'hg_pr_FlirtTeacher_OBJ'): #important!
        $ hg_pr_FlirtTeacher_OBJ = public_request()
    $ hg_pr_FlirtTeacher_OBJ.imagination_level = 2
    $ hg_pr_FlirtTeacher_OBJ.menu_text = "She's bait"
    $ hg_pr_FlirtTeacher_OBJ.start_label = "hg_pr_FlirtTeacher"
    $ hg_pr_FlirtTeacher_OBJ.complete_label = "hg_pr_FlirtTeacher_complete"

    if not hasattr(renpy.store,'hg_pr_ClassmateTouchYou_OBJ'): #important!
        $ hg_pr_ClassmateTouchYou_OBJ = public_request()
    $ hg_pr_ClassmateTouchYou_OBJ.imagination_level = 3
    $ hg_pr_ClassmateTouchYou_OBJ.menu_text = "Let a classmate molest you"
    $ hg_pr_ClassmateTouchYou_OBJ.start_label = "hg_pr_ClassmateTouchYou"
    $ hg_pr_ClassmateTouchYou_OBJ.complete_label = "hg_pr_ClassmateTouchYou_complete"

    if not hasattr(renpy.store,'hg_pr_FlashClassmate_OBJ'): #important!
        $ hg_pr_FlashClassmate_OBJ = public_request()
    $ hg_pr_FlashClassmate_OBJ.imagination_level = 3
    $ hg_pr_FlashClassmate_OBJ.menu_text = "Flash your tits to a classmate"
    $ hg_pr_FlashClassmate_OBJ.start_label = "hg_pr_FlashClassmate"
    $ hg_pr_FlashClassmate_OBJ.complete_label = "hg_pr_FlashClassmate_complete"

    if not hasattr(renpy.store,'hg_pr_KissAGirl_OBJ'): #important!
        $ hg_pr_KissAGirl_OBJ = public_request()
    $ hg_pr_KissAGirl_OBJ.imagination_level = 4
    $ hg_pr_KissAGirl_OBJ.menu_text = "Kiss a girl."
    $ hg_pr_KissAGirl_OBJ.start_label = "hg_pr_KissAGirl"
    $ hg_pr_KissAGirl_OBJ.complete_label = "hg_pr_KissAGirl_complete"

    if not hasattr(renpy.store,'hg_pr_HandjobClassmate_OBJ'): #important!
        $ hg_pr_HandjobClassmate_OBJ = public_request()
    $ hg_pr_HandjobClassmate_OBJ.imagination_level = 4
    $ hg_pr_HandjobClassmate_OBJ.menu_text = "Give a handjob to a classmate"
    $ hg_pr_HandjobClassmate_OBJ.start_label = "hg_pr_HandjobClassmate"
    $ hg_pr_HandjobClassmate_OBJ.complete_label = "hg_pr_HandjobClassmate_complete"

    if not hasattr(renpy.store,'hg_pr_BlowjobClassmate_OBJ'): #important!
        $ hg_pr_BlowjobClassmate_OBJ = public_request()
    $ hg_pr_BlowjobClassmate_OBJ.imagination_level = 5
    $ hg_pr_BlowjobClassmate_OBJ.menu_text = "Give a blowjob to a classmate"
    $ hg_pr_BlowjobClassmate_OBJ.start_label = "hg_pr_BlowjobClassmate"
    $ hg_pr_BlowjobClassmate_OBJ.complete_label = "hg_pr_BlowjobClassmate_complete"

    if not hasattr(renpy.store,'hg_pr_SexWithClassmate_OBJ'): #important!
        $ hg_pr_SexWithClassmate_OBJ = public_request()
    $ hg_pr_SexWithClassmate_OBJ.imagination_level = 5
    $ hg_pr_SexWithClassmate_OBJ.menu_text = "Have sex with a classmate"
    $ hg_pr_SexWithClassmate_OBJ.start_label = "hg_pr_SexWithClassmate"
    $ hg_pr_SexWithClassmate_OBJ.complete_label = "hg_pr_SexWithClassmate_complete"


    $ hg_pr_list = []
    $ hg_pr_list.append(hg_pr_FlirtClassmate_OBJ)
    $ hg_pr_list.append(hg_pr_FlirtTeacher_OBJ)
    $ hg_pr_list.append(hg_pr_ClassmateTouchYou_OBJ)
    $ hg_pr_list.append(hg_pr_FlashClassmate_OBJ)
    $ hg_pr_list.append(hg_pr_KissAGirl_OBJ)
    $ hg_pr_list.append(hg_pr_HandjobClassmate_OBJ)
    $ hg_pr_list.append(hg_pr_BlowjobClassmate_OBJ)
    $ hg_pr_list.append(hg_pr_SexWithClassmate_OBJ)



    if not hasattr(renpy.store,'hg_ps_PantyThief_OBJ'): #important!
        $ hg_ps_PantyThief_OBJ = public_shaming()
    $ hg_ps_PantyThief_OBJ.menu_text = "Panty Thief"
    $ hg_ps_PantyThief_OBJ.start_label = "hg_ps_PantyThief"
    $ hg_ps_PantyThief_OBJ.complete_label = "hg_ps_PantyThief_complete"

    if not hasattr(renpy.store,'hg_ps_WalkOfShame_OBJ'): #important!
        $ hg_ps_WalkOfShame_OBJ = public_shaming()
    $ hg_ps_WalkOfShame_OBJ.menu_text = "Walk Of Shame"
    $ hg_ps_WalkOfShame_OBJ.start_label = "hg_ps_WalkOfShame"
    $ hg_ps_WalkOfShame_OBJ.complete_label = "hg_ps_WalkOfShame_complete"

    if not hasattr(renpy.store,'hg_ps_WearMyCum_OBJ'): #important!
        $ hg_ps_WearMyCum_OBJ = public_shaming()
    $ hg_ps_WearMyCum_OBJ.menu_text = "Wear My Cum"
    $ hg_ps_WearMyCum_OBJ.start_label = "hg_ps_WearMyCum"
    $ hg_ps_WearMyCum_OBJ.complete_label = "hg_ps_WearMyCum_complete"

    if not hasattr(renpy.store,'hg_ps_HiddenBlowjob_OBJ'): #important!
        $ hg_ps_HiddenBlowjob_OBJ = public_shaming()
    $ hg_ps_HiddenBlowjob_OBJ.menu_text = "Hidden Blowjob"
    $ hg_ps_HiddenBlowjob_OBJ.start_label = "hg_ps_HiddenBlowjob"
    $ hg_ps_HiddenBlowjob_OBJ.complete_label = "hg_ps_HiddenBlowjob_complete"

    if not hasattr(renpy.store,'hg_ps_LeashWalk_OBJ'): #important!
        $ hg_ps_LeashWalk_OBJ = public_shaming()
    $ hg_ps_LeashWalk_OBJ.menu_text = "Time for a walk (leash)"
    $ hg_ps_LeashWalk_OBJ.start_label = "hg_ps_LeashWalk"
    $ hg_ps_LeashWalk_OBJ.complete_label = "hg_ps_LeashWalk_complete"

    if not hasattr(renpy.store,'hg_ps_Buttplug_OBJ'): #important!
        $ hg_ps_Buttplug_OBJ = public_shaming()
    $ hg_ps_Buttplug_OBJ.menu_text = "Wear A Buttplug"
    $ hg_ps_Buttplug_OBJ.start_label = "hg_ps_Buttplug"
    $ hg_ps_Buttplug_OBJ.complete_label = "hg_ps_Buttplug_complete"


    $ hg_ps_list = []
    $ hg_ps_list.append(hg_ps_PantyThief_OBJ)
    #$ hg_ps_list.append(hg_ps_WalkOfShame_OBJ)
    $ hg_ps_list.append(hg_ps_Buttplug_OBJ)
    $ hg_ps_list.append(hg_ps_WearMyCum_OBJ)
    #$ hg_ps_list.append(hg_ps_HiddenBlowjob_OBJ)
    #$ hg_ps_list.append(hg_ps_LeashWalk_OBJ)

    return


label silver_requests:
    if slytherin >= gryffindor:
        show screen hermione_main

        label silver_requests_root:
        menu:
            "-Personal favours-":
                label not_now_pf:
                python:
                    pf_menu = []
                    for i in hg_pf_list:
                        if i.imagination_level > imagination:
                            pf_menu.append(("{color=#858585}-A vague idea-{/color}","vague"))
                        else:
                            pf_menu.append((i.getMenuText(),i.start_label))
                    pf_menu.append(("-Never mind-", "nvm"))
                    result = renpy.display_menu(pf_menu)
                if result == "nvm":
                    jump silver_requests_root
                elif result == "vague":
                    call vague_idea
                    jump not_now_pf
                else:
                    $ renpy.jump(result)

            "{color=#858585}-Public requests-{/color}" if not daytime:
                show screen blktone
                with d3
                ">Public requests are available during the daytime only."
                hide screen blktone
                with d3
                jump silver_requests_root
            "-Public requests-" if daytime:
                if lock_public_favors:
                    her "Em... [genie_name]..."
                    her "I do not mind to keep selling you the favours..."
                    her "But only as long as we keep them private..."
                    jump silver_requests_root
                else:
                    label not_now_pr:
                    python:
                        pr_menu = []
                        for i in hg_pr_list:
                            if i.imagination_level > imagination:
                                pr_menu.append(("{color=#858585}-A vague idea-{/color}","vague"))
                            else:
                                pr_menu.append((i.getMenuText(),i.start_label))
                        pr_menu.append(("-Never mind-", "nvm"))
                        result = renpy.display_menu(pr_menu)
                    if result == "nvm":
                        jump silver_requests_root
                    elif result == "vague":
                        call vague_idea
                        jump not_now_pr
                    else:
                        $ renpy.jump(result)

            "{color=#858585}-Public Shaming-{/color}" if not daytime:
                show screen blktone
                with d3
                ">Public Shaming events are available during the daytime only."
                hide screen blktone
                with d3
                jump silver_requests_root
            "-Public Shaming-"if daytime:
                label not_now_ps:
                python:
                    ps_menu = []
                    for i in hg_ps_list:
                        ps_menu.append((i.getMenuText(),i.start_label))
                    ps_menu.append(("-Never mind-", "nvm"))
                    result = renpy.display_menu(ps_menu)
                if result == "nvm":
                    jump silver_requests_root
                else:
                    $ renpy.jump(result)

            "-Never mind-":
                jump hermione_requests


    else:
        show screen hermione_main
        with d3
        her "The Gryffindors are in the lead. I don't need to do this."
        jump hermione_requests



label end_hg_pf: #Hides screens. Hermione walks out. Resets Hermione.
    hide screen hermione_main

    hide screen bld1
    hide screen blktone

    if hermione_chibi_xpos_name in ["desk"]:
        call her_chibi("stand","desk","base")
    elif hermione_chibi_xpos_name in ["mid"]:
        call her_chibi("stand","mid","base")
    else:
        call her_chibi("hide")

    call gen_chibi("sit_behind_desk")

    with d3

    #Walk
    if hermione_chibi_xpos_name in ["desk"]:
        call her_walk("desk","leave",2.7)
    if hermione_chibi_xpos_name in ["mid"]:
        call her_walk("mid","leave",2)

    call reset_hermione

    $ hermione_busy = True

    jump main_room



label hg_pr_transition_block:

    hide screen bld1
    hide screen hermione_main
    hide screen blktone
    with d3

    if hermione_chibi_xpos_name == "desk":
        call her_walk("desk","leave",2.7)
    elif hermione_chibi_xpos_name == "mid":
        call her_walk("mid","leave",2)
    else:
        call her_chibi("leave")

    $ hermione_busy = True

    jump main_room



label could_not_flirt: #Sent here when choose "Favour failed! No points for you!" (Hermione is leaving without getting any points).

    show screen blkfade #Should be active anyways.

    hide screen hermione_main
    hide screen hermione_main_ass

    hide screen chair_left
    hide screen desk
    hide screen groping_naked_tits
    hide screen genie_and_tits_01
    hide screen jerking_off_01 #Hermione topless. Genie jerking off.
    if hermione_chibi_xpos_name == "desk":
        call her_chibi("stand","desk","base")
    else:
        call her_chibi("stand","mid","base")
    show screen genie

    hide screen bld1
    hide screen blktone
    hide screen blkfade
    with fade

    if hermione_chibi_xpos_name == "desk":
        call her_walk("desk","leave",2.7)
    else:
        call her_walk("mid","leave",2)

    $ hermione_busy = True

    jump main_room



### MUSIC BLOCK ###
label music_block:
    if daytime:
        call play_music("day_theme")
    else:
        call play_music("night_theme")
    return

### YOU LUCK IMAGINATION ###
label vague_idea:

    call nar(">You lack imagination for an idea of this caliber.")

    return





label her_walk_desk_blkfade:

    hide screen bld1
    hide screen blktone
    hide screen hermione_main
    with d3
    pause.2

    call her_walk("mid","desk",2,loiter=False, redux_pause = 2)
    call blkfade

    return

#############This massage shows when you make a request, and Hermione refuses because she is not slutty enough yet.
label too_much:
    stop music fadeout 2.0
    call her_main("[genie_name]??!","shock","wide",xpos="mid",trans="fade")
    her "How could you ask for such a thing!?"
    call her_main("I think I better leave.","angry","worriedCl",emote="05")

    $ mad += 7

    jump end_hg_pf

label very_no:
    stop music fadeout 2.0
    call her_main("Absolutely not!","annoyed","angryL",xpos="mid",trans="fade")
    her "I'll show you that my integrity and honour as a Gryffindor cannot be bought!"
    call her_main("I'm leaving this instant.","scream","angryCl")

    $ mad += 7

    jump end_hg_pf


init python:
    class silver_request(object):
        menu_text = ""
        start_label = ""
        complete_label = ""
        points = 0


    class personal_favor(silver_request):
        hearts_level = 0
        imagination_level = 0
        costume_event = False
        progress_hint = False

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def getMenuText(self):
            menu_image = "interface/heart_0"+str(self.hearts_level)+".png"
            ret_str = "Favor: \""+self.menu_text+"\" {image="+menu_image+"}"
            if self.progress_hint:
               ret_str += "  {image=interface/check_True.png}"
            if self.costume_event:
               ret_str += "  {image=interface/clothes.png}"
            return ret_str

    class public_request(silver_request):
        imagination_level = 0
        complete = False
        inProgress = False

        def getMenuText(self):
            menu_image = "interface/check_"+str(self.complete)+".png"
            return "Favour: \""+self.menu_text+"\" {image="+menu_image+"}"

    class public_shaming(silver_request):
        complete = False
        inProgress = False

        def getMenuText(self):
            menu_image = "interface/check_"+str(self.complete)+".png"
            return "Event: "+self.menu_text+" {image="+menu_image+"}"
