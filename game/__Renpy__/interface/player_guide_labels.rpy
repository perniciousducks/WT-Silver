

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
        hide screen bld1
        call hide_blktone
        call screen main_room_menu
