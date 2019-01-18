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
    
    if not check_winner() == "winner":
        jump twins_duel_lost
    
    hide screen blkfade
    stop music fadeout 1
    
    if not twins_first_win:
        twi "No way!"
        ger "You must've been cheating."
        m "It's all in the cards boys."
        ger "I can see that... perhaps it's worth stocking some after all."
        fre "Indeed, if the cards you have play such a big role..."
        ger "You'd have to buy more and more for any chance to win."
        fre "And we..."
        twi "We'll be rich!"
        m "So you'll stock some?"
        ger "Absolutely! We'll send you an owl when it's ready and if they sell well we'll play you again."
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
    if twins_cards_stocked == False:
        m "(I need to wait for an owl from them before we can duel again)"
        jump twins_duel_menu
                                
    fre "Good luck."
    ger "You'll need it."

    call setup_deck(twins_second_deck)
    $ response_card = ""
    
    play music "music/vs_twins.ogg" fadein 1.0
    play sound "sounds/Genie_VS_Twins.mp3"
    show screen genie_vs_twins
    pause 1
    show screen move_twins
    pause 4
    hide screen move_twins
    hide screen genie_vs_twins
    
    if renpy.random.randint(0,1) == 0:
        call enemy_turn

    while response_card != "EndGame":
        call cardgame
        if response_card == "Close":
            jump twins_duel_cancel
        #Should be a better way but renpy dont have break for while loops-_-
        if response_card == "AfterEnemy":
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            # Prevents volume to change again when using rollback
            $ renpy.block_rollback()
            $ rnd_text = twins_speech_card[renpy.random.randint(0,len(twins_speech_card)-1)]
            #$ rnd_twin = renpy.random.choice = [fre, goe]
            
            if renpy.random.randint(0, 1) == 0:
                fre "[rnd_text!t]"
            else:
                ger "[rnd_text!t]"
            $ _preferences.volumes['music'] = volume
    
    if not check_winner() == "winner":
        jump twins_duel_lost
    
    hide screen blkfade
    stop music fadeout 1
    if not twins_second_win:
        fre "I feel like we should have foreseen this."
        ger "I blame Trelawney on this, she said that luck would be on our side today..."
        fre "Well, a promise is a promise. Here's your reward..."
        $ card_rand_twins = renpy.random.choice(['fred', 'george'])
        $ unlocked_cards += [eval(card_rand_twins)]
        call give_reward("You have received a special card!", "images/cardgame/t1/special/%s_v1.png" % str(card_rand_twins))
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
    "You " + check_winner()
    stop music fadeout 1
    #jump return_office
    hide screen blkfade
    with dissolve
    menu:
        "-Rematch-":
            jump twins_duel_menu
        "-Be a loser-":
            pass
    ger "Cards not in your favour professor? Maybe next time..."
    "You return to your office."
    
    jump main_room
    
label twins_duel_cancel:
    show screen blkfade 
    with dissolve
    stop music fadeout 1
    #jump return_office
    hide screen blkfade
    with dissolve
    ger "Cards not in your favour professor? Maybe next time..."
    "You return to your office."
    
    jump main_room
    
screen genie_vs_twins:
    zorder 8
    add "images/cardgame/VS/background_twins.png" xalign 0.5 yalign 0.5
    add "images/cardgame/VS/genie_01.png" at move_in(-300, 3)
screen move_twins:
    zorder 8
    add "images/cardgame/VS/snape_01.png" at move_in(300, 1)
