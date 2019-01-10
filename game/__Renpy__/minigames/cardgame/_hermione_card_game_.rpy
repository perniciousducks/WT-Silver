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
        her "Well, that's interesting. I was sure that my deck would've been balanced enough..."
        m "It's just a practice round, I'm sure you'll do better next time."
        her "Your smile says otherwise."
        m "..."
        $ her_first_win = True
        pass
    else:
        her "This game is stupid!"
        pass
        
    jump main_room
    
label hermione_second_duel:
    call setup_deck(her_second_deck)

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
    if not her_second_win:
        her "I got 5 boosters, how isn't that enough to build a better deck than yours?"
        m "It's more important where you place those cards..."
        her "I know what I'm doing...."
        m "So, do you want to take a break?"
        her "No, I'm ready..."
        m "You sure?"
        her "I said I'm ready."
        $ her_second_win = True
        pass
    else:
        her "This game is stupid!"
        pass
        
    jump main_room
    
label hermione_third_duel:
    her "I'll make my house proud, you'll see."
    her "Wait, I should probably have asked for point for this."
    m "To late, here we go."
    
    call setup_deck(her_third_deck)
    
    $ response_card = ""
    
    call play_music("boss_card_theme")
    play sound "sounds/Genie_VS_Hermione4.mp3"
    show screen genie_vs_hermione
    show screen move_genie
    pause 1
    show screen versus
    pause 1
    show screen move_hermione
    pause 3
    hide screen move_genie
    hide screen move_hermione
    show screen genie_vs_hermione_smile
    with hpunch
    stop music fadeout 0
    pause
    hide screen versus
    hide screen genie_vs_hermione
    hide screen genie_vs_hermione_smile
    play music "music/vs_hermione.mp3"
    if renpy.random.randint(0,1) == 0:
        call enemy_turn

    while response_card != "EndGame":
        call cardgame
        if response_card == "Close":
            jump her_duel_cancel
        #Should be a better way but renpy dont have break for while loops-_-
        if response_card == "AfterEnemy":
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            # Prevents volume to change again when using rollback
            $ renpy.block_rollback()
            #
            #
            #
            # BUGGED
            $ her_speech = her_speech_card[renpy.random.randint(0,len(her_speech_card)-1)]
            call her_main ("[her_speech!t]", "base", "base")
            hide screen hermione_main
            $ _preferences.volumes['music'] = volume
    
    if not check_winner():
        jump her_duel_lost
    
    #Won third match
    stop music fadeout 1
    hide screen blkfade
    
    if her_third_win == False:
        her "Nooo, how's this even possible?" 
        her "I'm supposed to be the smartest girl in my year..."
        m "Looks like Wisdom beats intelligence..."
        her "You don't have to patronize me, I'll get you next time. You'll see."
        m "You seem to have forgotten something..."
        her "Fine..."
        her "Here..."
        $ her_third_win = True
        
    call play_sound("door")
    $ hermione_busy = True
    
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
            jump hermione_duel_menu
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
    her "Cards not in your favour [genie_name]? Maybe next time..."
    
    jump main_room
    
screen genie_vs_hermione:
    zorder 8
    add "images/cardgame/VS/background_twins.png" xalign 0.5 yalign 0.5
screen move_genie:
    zorder 8
    add "images/cardgame/VS/genie_01.png" at move_in(-300, 0.5)
screen versus:
    zorder 8
    add "images/cardgame/VS/vs.png"
screen move_hermione:
    zorder 8
    add "images/cardgame/VS/hermione_01.png" at move_in(300, 0.5)
    
screen genie_vs_hermione_smile:
    zorder 8
    add "images/cardgame/VS/genie_03.png"
    add "images/cardgame/VS/hermione_02.png"
    text "Click to continue" xalign 0.5 yalign 1.0