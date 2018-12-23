label twins_first_duel:
    call setup_deck(twins_first_deck)

    call play_music("grape_soda")
    $ response_card = ""
    
    if renpy.random.randint(0,1) == 0:
        call enemy_turn

    while response_card != "EndGame":
        call cardgame
        if response_card == "Close":
            jump twins_duel_cancel
        #Should be a better way but renpy dont have break for while loops-_-
    
    if not check_winner():
        jump twins_duel_lost
    
    hide screen blkfade
    stop music fadeout 1
    if not twins_first_win:
        twi "No way!"
        ger "You must've been cheating."
        m "It's all in the cards boys."
        ger "We can see that... perhaps it's worth stocking some after all."
        fre "Indeed, if what cards you have play such a big role..."
        ger "People would have to buy more and more for any chance to win..."
        fre "And we..."
        twi "We'll be rich!"
        m "So you'll stock some?"
        ger "Absolutely! We'll send you and owl when it's ready and if they sell well we'll play you again."
        twi "And we'll win next time!"
        m "We'll see about that, I can't have students going around showing up to their headmaster can I..."
        $ twins_first_win = True
        $ twins_cards_delay = twins_cards_delay+day
        pass
    else:
        twi "Not again.."
        m "Tough luck boys."
        pass
    
    "You return to your office."    
    jump main_room
    
label twins_second_duel:
    call setup_deck(twins_first_deck)

    call play_music("grape_soda")
    $ response_card = ""
    
    if renpy.random.randint(0,1) == 0:
        call enemy_turn

    while response_card != "EndGame":
        call cardgame
        if response_card == "Close":
            jump twins_duel_cancel
        #Should be a better way but renpy dont have break for while loops-_-
    
    if not check_winner():
        jump twins_duel_lost
    
    hide screen blkfade
    stop music fadeout 1
    if not twins_second_win:
        twi "No way!"
        ger "You must've been cheating."
        $ twins_second_win = True
        pass
    else:
        twi "Not again.."
        m "Tough luck boys."
        pass
    
    "You return to your office."    
    jump main_room
    
label twins_duel_lost:
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
    twi "Cards not in your favour professor? Maybe next time..."
    "You return to your office."
    
    jump main_room
    
label twins_duel_cancel:
    show screen blkfade 
    with dissolve
    stop music fadeout 1
    #jump return_office
    hide screen blkfade
    with dissolve
    twi "Cards not in your favour professor? Maybe next time..."
    "You return to your office."
    
    jump main_room