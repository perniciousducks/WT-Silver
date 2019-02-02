label test_card_game:
    $ testing = ""
    call play_music("grape_soda")
    
    $duel_response = start_duel(her_second_deck)
          
    if duel_response == "Close":
        jump her_duel_cancel
        
    elif not duel_response == "win":
        jump her_duel_lost
        

    jump main_room