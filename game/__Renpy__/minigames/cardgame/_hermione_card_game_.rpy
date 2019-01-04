label hermione_first_duel:
    call setup_deck(her_first_deck)

    call play_music("grape_soda")
    $ response_card = ""
    
    if renpy.random.randint(0,1) == 0:
        call enemy_turn

    while response_card != "EndGame":
        call cardgame
        if response_card == "Close":
            jump her_duel_cancel
        #Should be a better way but renpy dont have break for while loops-_-
    
    if not check_winner():
        jump her_duel_lost
    
    hide screen blkfade
    stop music fadeout 1
    if not her_first_win:
        her "Genie wins text"
        $ her_first_win = True
        pass
    else:
        her "Hermione lost again text"
        pass
        
    jump main_room
    
label her_duel_lost:
    show screen blkfade 
    with dissolve
    "You lost"
    stop music fadeout 1
    #jump return_office
    hide screen blkfade
    with dissolve
    menu:
        "-Rematch-":
            jump twins_duel_menu
        "-Be a loser-":
            pass
    her "Cards not in your favour [genie_name]? Maybe next time..."
    
    jump main_room
    
label her_duel_cancel:
    show screen blkfade 
    with dissolve
    stop music fadeout 1
    #jump return_office
    hide screen blkfade
    with dissolve
    twi "Cards not in your favour [genie_name]? Maybe next time..."
    
    jump main_room