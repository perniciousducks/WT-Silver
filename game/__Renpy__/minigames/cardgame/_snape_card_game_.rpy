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

    $ random_player_deck = create_random_deck(0,150,unlocked_cards)
    
    $ random_enemy_deck = create_random_deck(get_deck_score(unlocked_cards)-2, get_deck_score(unlocked_cards)+8, cards_all)
    
    $ duel_response = start_duel(random_enemy_deck, "snape_after", [renpy.random.randint(0,3), False, True, False], random_player_deck)

    if duel_response == "Close":
        $ wine -= 1
        jump snape_duel_cancel
        
    elif not duel_response == "win":
        $ wine -= 1
        jump snape_duel_lost
    hide screen blkfade
    stop music fadeout 1
    
    if random_snape_win:
        m "Yes!"
        g9 "No wine for you.."
        call sna_main("...","snape_04")
        g9 "Now, how about that prize we discussed."
        call sna_main("Ah, yes... something from my collection.","snape_05")
        "You've got a random potion ingredient from Snape \[item\]"
        g4 "What the fuck is this..."
        call sna_main("As I said...","snape_01")
        call sna_main("Something from my collection...","snape_02")
        m "..."
        call sna_main("I'm the potions master, what did you think it was going to be?","snape_03")
        m "I don't know... Like a whip or something?"
        call sna_main("Hey, just because I reside in the dungeon...","snape_07")
        g9 "I bet you do have a whip..."
        call sna_main("Well...","snape_12")
        m "Whatever, I'll take it."
        call sna_main("What, the whi...","snape_18")
        call sna_main("Oh, the potion ingredient...","snape_14")
        call sna_main("There's plenty more where that came from if you want another game...","snape_24")
        m "..."
        m "I'll think about it."
    else:
        $ random_choice = renpy.random.randint(0, 3)
        if random_choice == 0:
            g9 "Another victory in the bag..."
            call sna_main("I don't get it...","snape_03")
            call sna_main("...You must've been cheating.","snape_04")
            m "Skill... it's called skill."
        elif random_choice == 1:
            call sna_main("Not again... did you look at my cards before the game?","snape_10")
            m "How would I have done that?"
            call sna_main("I don't know...","snape_08")
            call sna_main("Some kind of Genie hocus pocus?","snape_07")
            m "..."
            call sna_main("Did I just...","snape_25")
            m "Yeah, a little bit..."
            call sna_main("I'm just going to leave this here...","snape_14")
        elif random_choice == 2:
            g9 "Sweet, another win for me."
            call sna_main("... I let you win that one.","snape_03")
            m "Sure you did."
        elif random_choice == 3:
            call sna_main("Damnit!","snape_17")
            g4 "Hey, chill out... it's just a game."
            call sna_main("Just a game?!","snape_18")
            call sna_main("Do you know what students came from the slytherin house are known for Genie?","snape_07")
            g9 "Well, from what you've told me... being massive sluts?"
            call sna_main("YES...","snape_08")
            call sna_main("Wait, no...","snape_16")
            call sna_main("We're known for being cunning...","snape_17")
            m "..."
            call sna_main("Cunning... Genie.","snape_18")
            m "Yeah, I got you."
            m "Hey, I could just give you another bottle..."
            call sna_main("...","snape_12")
            call sna_main("No... I'll beat you next time.","snape_16")
            g9 "That's the spirit."
        elif random_choice == 4:
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
        $ rndm_one_of_three = renpy.random.randint(1, 7)
        if rndm_one_of_three == 1:
            sna "Thanks for the bottle... Genie"
            g4 "...."
        elif rndm_one_of_three == 2:
            m "..."
            m "Good game..."
            sna "Forgetting something?"
            m "Fine, here's your bottle..."
        elif rndm_one_of_three == 3:
            call sna_main("Another win for me...","snape_02")
            m "And your last..."
            call sna_main("Sorry, can't hear you over the sound of my victory.","snape_01")
            m "..."
        elif rndm_one_of_three == 4:
            call sna_main("Child's play...","snape_02")
            m "I'm hundreds of years old you know..."
            call sna_main("And I beat you...","snape_02")
            m "just show how luck based the game is honestly..."
        elif rndm_one_of_three == 5:
            call sna_main("...","snape_02")
            m "Just take your prize and go."
        elif rndm_one_of_three == 6:
            call sna_main("Nice one...","snape_02")
            m "Hey, don't be a bad winner"
            call sna_main("Hey, I was just...","snape_03")
            call sna_main("I see what you're doing...","snape_04")
            call sna_main("I'll take that wine now...","snape_02")
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
