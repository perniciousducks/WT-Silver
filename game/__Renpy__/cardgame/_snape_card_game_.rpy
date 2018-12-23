label snape_first_duel:
    call setup_deck(snape_first_deck)
    sna "A bit dusty but this should do!"
    m "You, or the deck?"
    sna "I... the deck, obviously."
    sna "Let's do this."

    call play_music("grape_soda")
    $ response_card = ""
    
    if renpy.random.randint(0,1) == 0:
        call enemy_turn

    while response_card != "EndGame":
        call cardgame
        if response_card == "Close":
            jump snape_duel_cancel
        #Should be a better way but renpy dont have break for while loops-_-
    
    if not check_winner():
        jump snape_duel_lost
    
    hide screen blkfade
    stop music fadeout 1
    call sna_main( "I feel like I should have gone over the rules a bit more before trying this game again.","snape_05")
    call sna_main(  "Well played though.","snape_05")
    $ snape_first_win = True
    call play_sound("door")
    call sna_chibi("hide")
    $ snape_busy = True
        
    jump main_room
            
label snape_second_duel:
    call setup_deck(snape_second_deck)
    sna "That first one was just a warm up, there's no way you'll beat me this time!"
    m "Time to get our decks out."
    sna "...."
    sna "Let's just play."

    call play_music("grape_soda")
    $ response_card = ""
    if renpy.random.randint(0,1) == 0:
        call enemy_turn

    while response_card != "EndGame":
        call cardgame
        if response_card == "Close":
            jump snape_duel_cancel
        #Should be a better way but renpy dont have break for while loops-_-
    
    if not check_winner():
        jump snape_duel_lost
    
    hide screen blkfade
    stop music fadeout 1
    call sna_main( "Not again... I swear these cards used to be good when I bought them.","snape_05")
    call sna_main( "They must've made them obsolete to get you to buy more.","snape_05")
    call sna_main( "So deliciously mischievous.","snape_05")
    call sna_main(remove=True)
    $ snape_second_win = True
    call play_sound("door")
    call sna_chibi("hide")
    $ snape_busy = True
    
    if not her_know_cards:
        m "This is awesome, I wonder if Hermione would want to play against me."
 
    jump main_room
    
label snape_third_duel:
    if her_know_cards == False:
        m "(I should probably see if Hermione is interested and practice some more before challenging Snape.)"
        jump snape_duel_menu
        
    call setup_deck(snape_third_deck)
    sna "you're not beating me again genie, I've practiced with one of the greatest Wizard cards player there is!"
    m "Me?"
    sna "I... no, of course not."
    sna "Let's do this."
    
    $ response_card = ""
    
    call play_music("boss_card_theme")
    call play_sound("Genie_VS_Snape")
    show screen snape_vs_genie_screen
    pause 1
    show screen move_snape
    pause 4
    hide screen move_snape
    hide screen snape_vs_genie_screen
    show screen snape_vs_genie_smile
    pause
    hide screen snape_vs_genie_smile
    
    if renpy.random.randint(0,1) == 0:
        call enemy_turn

    while response_card != "EndGame":
        call cardgame
        if response_card == "Close":
            jump snape_duel_cancel
        #Should be a better way but renpy dont have break for while loops-_-
        if response_card == "AfterEnemy":
            $ volume = _preferences.volumes['music']
            $ _preferences.volumes['music'] *= .5
            # Prevents volume to change again when using rollback
            $ renpy.block_rollback()
            call sna_main( (snape_speach_card[renpy.random.randint(0,len(snape_speach_card)-1)]),"snape_05")
            call sna_main(remove=True)
            $ _preferences.volumes['music'] = volume
    
    if not check_winner():
        jump snape_duel_lost
    
    #Won third match
    stop music fadeout 1
    hide screen blkfade
    call sna_main( "Impossible! I was sure I'd have you this time...","snape_05")
    call sna_main( "Well, a deal is a deal...","snape_05")
    $ snape_third_win = True
    #[You've unlocked x Item]
    #
    #
    #
    #
    #
    call play_sound("door")
    call sna_chibi("hide")
    $ snape_busy = True
    
    jump main_room
    
label snape_duel_lost:
    show screen blkfade 
    with dissolve
    "You lost"
    stop music fadeout 1
    #jump return_office
    hide screen blkfade
    with dissolve
    menu:
        "-Rematch-":
            jump snape_duel_menu
        "-Be a loser-":
            pass
    sna "Cards not in your favour today? Maybe next time..."
    call play_sound("door")
    call sna_chibi("hide")
    $ snape_busy = True
    
    jump main_room
    
label snape_duel_cancel:
    show screen blkfade 
    with dissolve
    stop music fadeout 1
    #jump return_office
    hide screen blkfade
    with dissolve
    sna "Cards not in your favour today? Maybe next time..."
    call play_sound("door")
    call sna_chibi("hide")
    $ snape_busy = True
    
    jump main_room
    
screen snape_vs_genie_screen:
    zorder 8
    add "images/cardgame/VS/background_snape.png" xalign 0.5 yalign 0.5
    add "images/cardgame/VS/genie_name_plate.png" at move_in(-300, 1)
screen move_snape:
    zorder 9
    add "images/cardgame/VS/snape_name_plate.png" at move_in(300, 1)
    
screen snape_vs_genie_smile:
    zorder 10
    add "images/cardgame/VS/background_snape.png" xalign 0.5 yalign 0.5
    add "images/cardgame/VS/genie_vs_snape_smile.png"