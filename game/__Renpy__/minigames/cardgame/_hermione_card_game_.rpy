

# Hermione Duel Menu

label hermione_cardgame_menu:
    if her_know_cards == False:
        m "[hermione_name]..."
        call her_main( "Yes, [genie_name]?","base","base")
        m "Are you familiar with Wizard Cards?"
        call her_main( "I've heard of it... it used to be a popular card game a decade or so ago.","annoyed","squint")
        g9 "So, would you like to play it?"
        call her_main( "Do they even make the cards still? I don't think there's anyone in Hogsmeade stocking them.","normal","suspicious")
        call her_main( "So I wouldn't be able to play against you...","base","base")
        call her_main( "Unless Fred and Geo...","clench","wide")
        m "Unless... who now?"
        call her_main( "\"Hermione... learn to keep your mouth shut.\"","mad","wideL")
        m "[hermione_name]..."
        call her_main( "I'm sorry sir, I should have told you...","open","worried")
        call her_main( "Fred and George have a secret shop set up in the school.","normal","worriedL")
        m "I see..."
        call her_main( "Please don't tell them I told you.","open","worriedCl")
        m "So you say they might have some cards?"
        call her_main( "Wha... yes, maybe.","base","soft")
        call her_main( "You're not going to shut them down?","angry","suspicious")
        m "Why should I? It's a free market is it not?"
        g9 "A little bit of competition with Hoemead is good for consumers."
        call her_main( "But... I mean, yes of course.","annoyed","worried")
        m "So you'll play if they stock some cards?"
        call her_main( "I mean...","soft","down_raised")
        m "If they don't get shut down I mean."
        call her_main( "Oh, yes of course I'll play.","shock","wide")
        call her_main( "...","soft","surprised")
        call her_main( "Anything else you needed or am I free to go?","base","worried")
        $ her_know_cards = True
        jump hermione_requests

    elif her_know_cards and twins_know_cards == False:
        m "(I should talk to Fred and George about wizard cards first.)"
        jump hermione_requests

    elif her_know_cards and twins_know_cards and not twins_cards_stocked:
        m "(I have to convince Fred and George to start stocking up cards in their shop first.)"
        jump hermione_requests

    elif twins_cards_stocked_talk and not her_cards_stocked_talk:
        m "Hello again [hermione_name]."
        call her_main( "Hello [genie_name].","base","base")
        m "I wanted to thank you for mentioning the Weasley shop."
        call her_main( "You're not shutting them down are you?","soft","down")
        m "Of course not, where else am I supposed to get my supplies from?"
        call her_main( "Oh, yes... where.","normal","down_raised")
        g9 "In fact, I noticed that you were on the list."
        call her_main( "What list? Have I done something wrong?","soft","worried")
        m "The tier list for the card-game of course."
        call her_main( "Ah, yes...","normal","soft")
        call her_main( "I went there to see if you had shut them down and ended up with a deck of cards.","mad","angryCl")
        g9 "\"Sounds like even I could learn some bartering tricks from those two.\""
        m "So, how about a little some practice rounds then?"
        call her_main( " I've only recently started playing so I'm not that good yet.","base","glance")
        m "Don't worry, after a few practice rounds you'll get up to speed, when you're ready we'll play the real challenge..."
        $ her_cards_stocked_talk = True
        jump hermione_duel_menu

    else:
        if geniecard_level < 2:
            label hermione_duel_menu:
            menu:
                "-First Duel-":
                    jump hermione_first_duel
                "-Second Duel-" if her_first_win:
                    jump hermione_second_duel
                "{color=#858585}-You need to beat the first duel-{/color}" if not her_first_win:
                    jump hermione_duel_menu
                "-Challenge-" if her_second_win:
                    jump hermione_third_duel
                "{color=#858585}-You need to beat the second duel-{/color}" if not her_second_win:
                    jump hermione_duel_menu
                "-Never mind-":
                    jump hermione_requests
        else:
            jump hermione_random_duel

label hermione_first_duel:
    call play_music("grape_soda")

    $ duel_response = start_duel(her_first_deck)

    if duel_response == "Close":
        jump her_duel_cancel

    elif not duel_response == "win":
        jump her_duel_lost

    hide screen blkfade
    stop music fadeout 1
    if not her_first_win:
        call her_main( "Well, that's interesting. I was sure that my deck would've been balanced enough...","angry","angryCl")
        g9 "It's just a practice round, I'm sure you'll do better next time."
        call her_main( "Your smile says otherwise.","mad","angryL")
        m "..."
        $ her_first_win = True
        pass
    else:
        call her_main( "This game is stupid!","angry","angryCl")
        pass

    $ geniecard_tokens += 1

    jump main_room

label hermione_second_duel:
    call play_music("grape_soda")

    $ duel_response = start_duel(her_second_deck)

    if duel_response == "Close":
        jump her_duel_cancel

    elif not duel_response == "win":
        jump her_duel_lost

    hide screen blkfade
    stop music fadeout 1
    if not her_second_win:
        call her_main( "I got 5 boosters, how isn't that enough to build a better deck than yours?","mad","annoyed")
        m "It's more important where you place those cards..."
        call her_main( "I know what I'm doing....","open","angryCl")
        g9 "So, do you want to take a break?"
        call her_main( "No, I'm ready...","soft","concerned")
        m "You sure?"
        call her_main( "I said I'm ready.","clench","angry")
        $ her_second_win = True
        jump hermione_duel_menu
        pass
    else:
        call her_main( "This game is stupid!","angry","angryCl")
        pass

    $ geniecard_tokens += 1

    jump main_room

label hermione_third_duel:
    call her_main( "I'll make my house proud, you'll see.","grin","happy")
    call her_main( "Wait, I should have asked for point for this.","shock","shocked")
    g9 "To late, here we go."

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

    $ duel_response = start_duel(her_third_deck, her_after)

    if duel_response == "Close":
        jump her_duel_cancel

    elif not duel_response == "win":
        jump her_duel_lost

    #Won third match
    stop music fadeout 1
    hide screen blkfade

    if her_third_win == False:
        call her_main( "Nooo, how's this even possible?","clench","shocked")
        call her_main( "I'm supposed to be the smartest girl in my year...","mad","surprised")
        g9 "Looks like Wisdom beats intelligence..."
        call her_main( "You don't have to patronize me, I'll get you next time. You'll see.","upset","suspicious")
        g9 "You seem to have forgotten something..."
        call her_main( "Fine...","angry","glance")
        call her_main( "Here...","mad","glanceL")
        $ unlocked_cards += [card_her_librarian]
        call give_reward("You have received a card!", "images/cardgame/t1/hermione/her_librarian_v1.png")
        $ her_third_win = True
        $ geniecard_tokens += 3
    else:
        $ geniecard_tokens += 1

    call play_sound("door")
    $ hermione_busy = True

    jump main_room

label hermione_random_duel:
    m "Ready for another game of cards?"

    if her_whoring < 8:
        call her_main("You've already challenged me though...","open","squintL")
        call her_main("and I lost.","annoyed","down")
        g9 "What if we made it a wager..."
        call her_main("Like gambling? No thank you!","clench","annoyed")
        m "It's not gambling, just a friendly house point wager..."
        call her_main("Sounds like gambling to me...","normal","suspicious")
        m "So, how about it?"
        call her_main("I'll pass, [genie_name]...","open","worriedL")

        m "\"Seem like she's a bit to pure minded to accept any kind of wager right now...\""
        jump hermione_requests
    else:
        call her_main("You've already challenged me though...","open","squintL")
        call her_main("and I lost.","annoyed","down")
        g9 "What if we made it a wager..."
        call her_main("Gambling you mean?","open","worried")
        m "Not for money obviously."
        call her_main("What are you suggesting then?","base","happy", cheeks="blush")
        m "Well, I was thinking house points."
        call her_main("House points...","normal","squintL")
        call her_main("How would this work then?","open","squint")
        m "Well, if you win I'll give you 10 points to Gryffindor."
        call her_main("Only 10?","annoyed","Glance")
        m "20 then..."
        call her_main("And if I lose?","open","SquintL")
        m "I'll take the same amount away."
        m "\"As if she's going to let that happen...\""
        call her_main("...","normal","WorriedCl", cheeks="blush")
        call her_main("Okay... In that case to make it fair, let's add these extra rules...","open","happy")

    label hermione_random_duel_rematch:

    call play_music("boss_card_theme")

    $ random_player_deck = create_random_deck(0,150,unlocked_cards)

    $ random_enemy_deck = create_random_deck(get_deck_score(random_player_deck)-2, get_deck_score(random_player_deck)+8, cards_all)

    $ duel_response = start_duel(random_enemy_deck, her_after, [5, False, False, True], random_player_deck)

    if duel_response == "Close":
        jump her_duel_cancel
    elif duel_response == "draw":
        jump her_duel_draw
    elif not duel_response == "win":
        jump her_duel_lost

    #Won third match
    stop music fadeout 1
    hide screen blkfade

    if not her_random_win:
        $ her_random_win = True
        $ geniecard_tokens += 3
    else:
        $ geniecard_tokens += 1

    m "Seems like I've won this one [hermione_name]."
    call her_main ("I noticed...","normal","worriedL")
    m "You do know what this means, don't you?"
    call her_main("...","normal","worried")
    g9 "This means I'm going to have to deduct 20 points from Gryffindor house."
    call her_main("Please, don't. I don't want the others to wake up tomorrow wondering why there's 20 house points missing...","open","worriedCl")
    m "Well, in that case..."

    menu:
        "-Send Hermione to work, promoting the card game.-" if not cardgame_work:
            $ cardgame_work = True
            g9 "In that case, I think I have a good idea for a job..."
            call her_main("A job?","open","squint")
            m "Yes, I'd like you to start helping the twins promote the card game..."
            call her_main("I can do that...","base","worried", cheeks="blush")
            call her_main("But not today if that's okay with you.","open","down")
            g9 "That's fine, wouldn't want you to go there looking as defeated as you are at the moment."
            call her_main("...","normal","squintL", cheeks="blush")
            call her_main("Did you need anything else?","open","soft", cheeks="blush")
            call give_reward("Hermione can now work by helping the twins promote the card game.", "interface/icons/icon_gambler_hat.png")
            jump hermione_requests
        "-Ask for a blowjob instead-":
            jump hg_wager_bj
        "-Deduct the points-":
            pass

    m "No, sorry miss Granger... Minus 20 points to Gryffindor..."
    call her_main("...","disgust","down")
    call her_main("Fine, that's fair...","open","down_raised")
    call her_main("But I'm done playing for today...","normal","worriedCl", cheeks="blush")
    $ gryffindor -= 20

    call play_sound("door")
    $ hermione_busy = True

    jump main_room

label her_duel_draw:
    stop music fadeout 1

    menu:
        "-Rematch-":
            if geniecard_level == 1:
                jump hermione_duel_menu
            else:
                jump hermione_random_duel_rematch
        "-Stop playing-":
            pass

    her "Okay, another time then..."
    jump main_room

label her_duel_lost:
    stop music fadeout 1

    if geniecard_level > 1:
        her "Hah, told you I'd do it!"
        her "I'll take those points now."
        m "Fine, 20 to gryffindor."
        $ gryffindor += 20

    menu:
        "-Rematch-":
            if geniecard_level == 1:
                jump hermione_duel_menu
            else:
                jump hermione_random_duel
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

screen genie_vs_hermione():
    zorder 8
    add "images/cardgame/VS/background_twins.png" xalign 0.5 yalign 0.5
screen move_hermione():
    zorder 8
    add "images/cardgame/VS/hermione_01.png" at move_in(300, 0.5)

screen genie_vs_hermione_smile():
    zorder 8
    add "images/cardgame/VS/genie_03.png"
    add "images/cardgame/VS/hermione_02.png"
    text "Click to continue" xalign 0.5 yalign 1.0

init python:
    def her_after():
        volume = _preferences.volumes['music']
        _preferences.volumes['music'] *= .5
        s_punch = renpy.random.randint(1, 4)
        renpy.sound.play("sounds/card_punch%s.mp3" % s_punch)
        # Prevents volume to change again when using rollback
        renpy.block_rollback()
        her_speech = her_speech_card[renpy.random.randint(0,len(her_speech_card)-1)]
        renpy.say(her, her_speech)
        renpy.hide_screen("hermione_main")
        _preferences.volumes['music'] = volume
        return
