label snape_first_duel:
    call setup_deck(snape_first_deck)
    sna "you're not beating me again genie, I've practiced with the greatest Wizard cards player there is!"
    m "Me?"
    sna "I... no, of course not."
    sna "Let's do this."
    hide screen genie
    hide screen candlefire
    call sna_main(remove=True)
    
    call play_music("grape_soda")
    $ response_card = ""
    if renpy.random.randint(0,1) == 0:
        call enemy_turn

    while response_card != "EndGame":
        call cardgame
        if response_card == "Close":
            jump snape_duel_cancel
        #Should be a better way but renpy dont have break for while loops-_-
        if response_card == "AfterEnemy":
            call sna_main( (snape_speach_card[renpy.random.randint(0,len(snape_speach_card)-1)]),"snape_05")
            call sna_main(remove=True)
    
    show screen blkfade
    if not check_winner():
        jump snape_duel_lost
        
    show screen genie
    call sna_main( "I feel like I should have gone over the rules a bit more before trying this game again.","snape_05")
    call sna_main(  "Well played though.","snape_05")
    call sna_main(remove=True)
    $ beat_snape_ones = True
    jump return_office
            
label snape_second_duel:
    call setup_deck(snape_second_deck)
    sna "you're not beating me again genie, I've practiced with the greatest Wizard cards player there is!"
    m "Me?"
    sna "I... no, of course not."
    sna "Let's do this."
    hide screen genie
    hide screen candlefire
    call sna_main(remove=True)

    call play_music("grape_soda")
    $ response_card = ""
    if renpy.random.randint(0,1) == 0:
        call enemy_turn

    while response_card != "EndGame":
        call cardgame
        if response_card == "Close":
            jump snape_duel_cancel
        #Should be a better way but renpy dont have break for while loops-_-
        if response_card == "AfterEnemy":
            call sna_main( (snape_speach_card[renpy.random.randint(0,len(snape_speach_card)-1)]),"snape_05")
            call sna_main(remove=True)
    
    show screen blkfade
    if not check_winner():
        jump snape_duel_lost
            
    call sna_main( "Not again... I swear these cards used to be good when I bought them.","snape_05")
    call sna_main( "They must've made them obsolete to get you to buy more.","snape_05")
    call sna_main( "So deliciously mischievous.","snape_05")
    call sna_main(remove=True)
    $ beat_snape_twice = True
    jump return_office
    
label snape_third_duel:
    call setup_deck(snape_third_deck)
    sna "you're not beating me again genie, I've practiced with the greatest Wizard cards player there is!"
    m "Me?"
    sna "I... no, of course not."
    sna "Let's do this."
    hide screen genie
    hide screen candlefire
    call sna_main(remove=True)

    $ response_card = ""
    if renpy.random.randint(0,1) == 0:
        call enemy_turn

    while response_card != "EndGame":
        call cardgame
        if response_card == "Close":
            jump snape_duel_cancel
        #Should be a better way but renpy dont have break for while loops-_-
        if response_card == "AfterEnemy":
            call sna_main( (snape_speach_card[renpy.random.randint(0,len(snape_speach_card)-1)]),"snape_05")
            call sna_main(remove=True)
    
    show screen blkfade
    if not check_winner():
        jump snape_duel_lost
            
    call sna_main( "Impossible! I was sure I'd have you this time...","snape_05")
    call sna_main( "Well, a deal is a deal...","snape_05")
    #[You've unlocked x Item]
    jump return_office
    
label snape_duel_lost:
    "You lost"
    jump return_office
    
label snape_duel_cancel:
    sna "Cards not in your favour today? Maybe next time..."   
    jump return_office