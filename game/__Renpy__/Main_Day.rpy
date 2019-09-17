label day_start:
    $ daytime = True
    
    call common_start

    # Start Quests
    jump quests

    label day_resume:

    # Favors
    if hg_pr_sex_skip: # Hermione does not show up. This sends to label where she shows up next morning.
        $ hg_pr_sex.start() # hg_pr_sex_T1_intro_E2

    label day_main_menu:

    ### MENU PLACEMENT ###
    call reset_menu_position

    call hide_characters
    call gen_chibi("sit_behind_desk")
    with d3

    if bird_examined and desk_examined and cupboard_examined and door_examined and fireplace_examined and not genie_intro.E2_complete:
        jump genie_intro_E2

    call screen main_room_menu
