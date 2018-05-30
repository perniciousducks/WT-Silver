

label open_guide:
    $ renpy.play('sounds/scroll.mp3')
    $ guide_page = 0
    $ guide_show_hint = False
    $ guide_show_next_step = False
    #call update_tip_of_the_day
    $ sQuest_get_map.counter = 1 #Testing Purpose only
    $ sQuest_buy_at_shop.counter = 1 #Testing Purpose only
    call update_quests
    call update_tip_of_the_day
    call blktone
    call screen guide
    label guide_return_point:
        $ renpy.play('sounds/scroll.mp3')
        call hide_blktone
        call screen main_room_menu
    

label give_reward(text="",gift=""):
    show screen blktone5
    with d3
    
    $ renpy.play('sounds/win2.mp3') 
    show screen notes
    with d9
    hide screen notes
    with d3

    if gift!="":
        $ the_gift = gift
    else:
        $ the_gift = "images/store/01.png"

    $ menu_x = 0.5
    $ menu_y = 0.75 #makes the menu lower so it isn't writing over the image.

    if text != "":
        $ quest_reward_text = text

    show screen gift
    with d3

    menu:
        "[quest_reward_text]"
        "-Done Reading-":
            pass

    hide screen gift
    with d1
    
    hide screen blktone5
    with d3
    
    $ menu_y = 0.5 #return to default menu align

    return

#Adds star next to personal favours if you can gain whoring points.
label update_hints:

    #Favour 1
    if whoring < 3:
        $ hg_pf_TalkToMe_OBJ.progress_hint = True
    else:
        $ hg_pf_TalkToMe_OBJ.progress_hint = False

    #Favour 2
    if whoring < 3:
        $ hg_pf_NicePanties_OBJ.progress_hint = True
    else:
        $ hg_pf_NicePanties_OBJ.progress_hint = False

    #Favour 3
    if whoring >= 3 and whoring < 6:
        $ hg_pf_BreastMolester_OBJ.progress_hint = True
    else:
        $ hg_pf_BreastMolester_OBJ.progress_hint = False

    #Favour 4
    if whoring >= 3 and whoring < 6:
        $ hg_pf_ButtMolester_OBJ.progress_hint = True
    elif whoring >= 9 and not cho_known:
        $ hg_pf_ButtMolester_OBJ.progress_hint = True
    else:
        $ hg_pf_ButtMolester_OBJ.progress_hint = False

    #Favour 5
    if whoring >= 6 and whoring < 9:
        $ hg_pf_ShowThemToMe_OBJ.progress_hint = True
    else:
        $ hg_pf_ShowThemToMe_OBJ.progress_hint = False

    #Favour 6
    if whoring >= 9 and whoring < 12:
        $ hg_pf_DanceForMe_OBJ.progress_hint = True
    else:
        $ hg_pf_DanceForMe_OBJ.progress_hint = False

    #Favour 7
    if whoring >= 9 and whoring < 12:
        $ hg_pf_ShowMeYourAss_OBJ.progress_hint = True
    else:
        $ hg_pf_ShowMeYourAss_OBJ.progress_hint = False

    #Favour 8
    if whoring >= 9 and whoring < 12:
        $ hg_pf_LetMeTouchThem_OBJ.progress_hint = True
    else:
        $ hg_pf_LetMeTouchThem_OBJ.progress_hint = False

    #Favour 9
    if whoring >= 12 and whoring < 15:
        $ hg_pf_TouchMe_OBJ.progress_hint = True
    else:
        $ hg_pf_TouchMe_OBJ.progress_hint = False

    #Favour 10
    if whoring >= 15 and whoring < 18:
        $ hg_pf_TitJob_OBJ.progress_hint = True
    else:
        $ hg_pf_TitJob_OBJ.progress_hint = False

    #Favour 11
    if whoring >= 15 and whoring < 18:
        $ hg_pf_SuckIt_OBJ.progress_hint = True
    else:
        $ hg_pf_SuckIt_OBJ.progress_hint = False

    #Favour 12
    if whoring >= 18 and whoring < 21:
        $ hg_pf_LetsHaveSex_OBJ.progress_hint = True
    else:
        $ hg_pf_LetsHaveSex_OBJ.progress_hint = False

    #Favour 13
    if whoring >= 21 and whoring < 24:
        $ hg_pf_TimeForAnal_OBJ.progress_hint = True
    else:
        $ hg_pf_TimeForAnal_OBJ.progress_hint = False

    return

