label snape_first_duel:
    call setup_deck(snape_first_deck)
    sna "you're not beating me again genie, I've practiced with the greatest Wizard cards player there is!"
    m "Me?"
    sna "I... no, of course not."
    sna "Let's do this."
    python:
        while ((len(player_deck) != 0) and (len(enemy_deck) != 0)):
            response_card = renpy.call("cardgame")
            if response_card == "Cancel":
                renpy.jump("snape_duel_cancel")

        if not check_winner():
            renpy.jump("snape_duel_lost")
            
    sna "I feel like I should have gone over the rules a bit more before trying this game again."
    sna "Well played though."
            
label snape_second_duel:
    call setup_deck(snape_second_deck)
    sna "you're not beating me again genie, I've practiced with the greatest Wizard cards player there is!"
    m "Me?"
    sna "I... no, of course not."
    sna "Let's do this."
    python:
        while ((len(player_deck) != 0) and (len(enemy_deck) != 0)):
            response_card = renpy.call("cardgame")
            if response_card == "Cancel":
                renpy.jump("snape_duel_cancel")

        if not check_winner():
            renpy.jump("snape_duel_lost")
            
    sna "Not again... I swear these cards used to be good when I bought them."
    sna "They must've made them obsolete to get you to buy more."
    sna "So deliciously mischievous."
    
label snape_third_duel:
    call setup_deck(snape_third_deck)
    sna "you're not beating me again genie, I've practiced with the greatest Wizard cards player there is!"
    m "Me?"
    sna "I... no, of course not."
    sna "Let's do this."
    
    python:
        while ((len(player_deck) != 0) and (len(enemy_deck) != 0)):
            response_card = renpy.call("cardgame")
            if response_card == "Cancel":
                renpy.jump("snape_duel_cancel")

        if not check_winner():
            renpy.jump("snape_duel_lost")
            
    sna "Impossible! I was sure I'd have you this time..."
    sna "Well, a deal is a deal..."
    #[You've unlocked x Item]
    
    
label snape_duel_lost:
    "You lost"
    jump snape
    
label snape_duel_cancel:
    sna "Cards not in your favour today? Maybe next time..."   