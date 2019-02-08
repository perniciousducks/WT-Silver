label snape_first_duel:
    call sna_main( "A bit dusty but this should do!","snape_03")
    m "You, or the deck?"
    call sna_main( "I... the deck, obviously.","snape_14")
    call sna_main( "Let's do this.","snape_17")

    call play_music("grape_soda")

    $ duel_response = start_duel(snape_first_deck)
          
    if duel_response == "Close":
        jump snape_duel_cancel
        
    elif not duel_response == "win":
        jump snape_duel_lost


    hide screen blkfade
    stop music fadeout 1
    call sna_main( "Maybe I should've gone over the rules a bit more before trying this game again....","snape_05")
    call sna_main(  "Well played though.","snape_04")
    $ snape_first_win = True
    call play_sound("door")
    call sna_chibi("hide")
    $ snape_busy = True

    $ geniecard_tokens += 1

    jump main_room

label snape_second_duel:
    call sna_main( "That first one was just a warm up, there's no way you'll beat me this time!","snape_16")
    g9 "Time to get our decks out."
    call sna_main( "....","snape_25")
    call sna_main( "Let's just play.","snape_04")

    call play_music("grape_soda")
    
    $ duel_response = start_duel(snape_second_deck)
          
    if duel_response == "Close":
        jump snape_duel_cancel
        
    elif not duel_response == "win":
        jump snape_duel_lost

    hide screen blkfade
    stop music fadeout 1
    call sna_main( "Not again... I swear these cards used to be good when I bought them.","snape_07")
    call sna_main( "They must've made them obsolete to get you to buy more.","snape_04")
    call sna_main( "So deliciously mischievous.","snape_02")
    call sna_main(remove=True)
    $ snape_second_win = True
    call play_sound("door")
    call sna_chibi("hide")
    $ snape_busy = True

    if not her_know_cards:
        g9 "This is awesome, I wonder if Hermione would want to play against me..."

    $ geniecard_tokens += 1

    jump main_room

label snape_third_duel:
    if her_know_cards == False:
        m "(I should probably see if Hermione is interested and practice some more before challenging Snape.)"
        jump snape_duel_menu

    if twins_cards_stocked_talk == False:
        m "(I should wait for an owl from Fred and George and train with Hermione first.)"
        jump snape_duel_menu

    call setup_deck(snape_third_deck)
    m "So, how about that prize?"
    call sna_main( "Again with the prize...","snape_01")
    m "I'm bored okay... and I like prizes..."
    call sna_main( "Fine, I challenge you!!","snape_10")
    m "..."
    call sna_main( "You don't say it like that anymore?","snape_05")
    m "No, that's lame."
    call sna_main( "You're not going to beat me again genie, I've practiced with the greatest Wizard cards player there is!","snape_02")
    m "Me?"
    call sna_main( "I... no, of course not.","snape_14")
    call sna_main( "Let's do this.","snape_17")
    call sna_main( "Show me what you got genie... beat me and I'll give you a card from my collection and 3 tokens.","snape_18")
    m "Bring it."
    
    call play_music("boss_card_theme")
    play sound "sounds/Genie_VS_Snape.mp3"
    show screen genie_vs_snape
    show screen move_genie
    pause 1
    show screen versus
    pause 1
    show screen move_snape
    pause 2.5
    hide screen move_genie
    hide screen move_snape
    show screen genie_vs_snape_smile
    pause
    hide screen versus
    hide screen genie_vs_snape
    hide screen genie_vs_snape_smile
    
    $ duel_response = start_duel(snape_third_deck, "snape_after")
          
    if duel_response == "Close":
        jump snape_duel_cancel
        
    elif not duel_response == "win":
        jump snape_duel_lost

    #Won third match
    stop music fadeout 1
    hide screen blkfade

    if snape_third_win == False:
        call sna_main( "Impossible, what's wrong with these cards...","snape_05")
        m "They're old, that's what."
        m "Now to the prize..."
        call sna_main( "Fine, here's your tokens and one of my precious cards....","snape_05")
        call sna_main( "\"You were a good card my boy. But it's time to grow up.\"","snape_05")
        $ snape_third_win = True
        $ unlocked_cards += [snape]
        call give_reward("You have received a special card!", "images/cardgame/t1/special/snape_v1.png")
        $ geniecard_tokens += 3
    else:
        $ geniecard_tokens += 1

    call play_sound("door")
    call sna_chibi("hide")
    $ snape_busy = True

    jump main_room
    
label snape_random_duel:
    call play_music("grape_soda")
    $ response_card = ""

    if renpy.random.randint(0,1) == 0:
        call enemy_turn

    while response_card != "EndGame":
        call cardgame
        if response_card == "Close":
            $ wine -= 1
            jump snape_duel_cancel
        #Should be a better way but renpy dont have break for while loops-_-

    if not check_winner() == "win":
        $ wine -= 1
        jump snape_duel_lost

    hide screen blkfade
    stop music fadeout 1
    call sna_main( "Maybe I should've gone over the rules a bit more before trying this game again....","snape_05")
    call sna_main(  "Well played though.","snape_04")
    call play_sound("door")
    call sna_chibi("hide")
    $ snape_busy = True
    #
    #
    # Random ingredient or a potion
    #
    #
    $ geniecard_tokens += 1

    jump main_room

label snape_after:
    $ volume = _preferences.volumes['music']
    $ _preferences.volumes['music'] *= .5
    $ s_punch = renpy.random.randint(1, 4)
    play sound "sounds/card_punch%s.mp3" % s_punch
    # Prevents volume to change again when using rollback
    $ renpy.block_rollback()
    call sna_main( (snape_speech_card[renpy.random.randint(0,len(snape_speech_card)-1)]),"snape_05")
    call sna_main(remove=True)
    $ _preferences.volumes['music'] = volume
    return
    
label snape_duel_lost:
    hide screen blkfade
    stop music fadeout 1

    menu:
        "-Rematch-":
            if geniecard_level == 1:
                jump snape_duel_menu
            else:
                m "I demand a rematch!"
                if wine < 1:
                    sna "Seems like you lost all of your bottles, maybe next time."
                    g4 "...You evil creature..."
                    pass
                else:
                    sna "Fine."
                    sna "More wine for me!"
                    jump snape_random_duel
        "-Be a loser-":
            pass
            
    if geniecard_level == 1:
        sna "Cards not in your favour today? Maybe next time..."
    else: # Rub it in
        $ rndm_one_of_three = renpy.random.randint(1, 3)
        if rndm_one_of_three == 1:
            sna "Thanks for the bottle... Genie"
            g4 "...."
        elif rndm_one_of_three == 2:
            m "..."
            m "Good game..."
            sna "Forgetting something?"
            m "Fine, here's your bottle..."
        else:
            sna "HA!"
            sna "I mean... good game."
            m "You're allowed to show enthusiasm you know..."
            sna "I know, but it's bad for my image..."
            m "..."
            m "Whatever, here's your bottle."
            
    call play_sound("door")
    call sna_chibi("hide")
    $ snape_busy = True

    jump main_room

label snape_duel_cancel:
    show screen blkfade
    with dissolve
    stop music fadeout 1
    hide screen blkfade
    with dissolve
    
    if geniecard_level == 1:
        sna "Cards not in your favour today? Maybe next time..."
    else:
        sna "In that case, it's a forfeit."
        sna "I'll take that wine now."
        m "Wait a minute..."
        sna "I don't make the rules, I just play by them."
        m "Fine..."
            
    call play_sound("door")
    call sna_chibi("hide")
    $ snape_busy = True

    jump main_room

screen genie_vs_snape:
    zorder 8
    add "images/cardgame/VS/background_snape.png" xalign 0.5 yalign 0.5
screen move_genie:
    zorder 8
    add "images/cardgame/VS/genie_01.png" at move_in(-300, 0.5)
screen versus:
    zorder 8
    add "images/cardgame/VS/vs.png"
screen move_snape:
    zorder 8
    add "images/cardgame/VS/snape_01.png" at move_in(300, 0.5)

screen genie_vs_snape_smile:
    zorder 8
    add "images/cardgame/VS/genie_02.png"
    add "images/cardgame/VS/snape_02.png"
    text "Click to continue" xalign 0.5 yalign 1.0
