label setup_deck(opppent_deck): 
    python:
        player_deck = []
        for card in playerdeck:
            player_deck.append(card.clone())
        enemy_deck = []
        for card in opppent_deck:
            card.playercard = False
            enemy_deck.append(card.clone())
        reset_table_cards()
    return
    
label cardgame:
    hide screen main_room_menu
    show screen card_battle(player_deck,enemy_deck)
    $ renpy.music.stop("weather") #Stop playing weather SFX
    $ renpy.block_rollback() #Disallow rollback cheating
    $ _return = ui.interact()

    if _return in player_deck:
        $ selectcard = player_deck.index(_return)
        $ response_card = "NewTurn"
        return "NewTurn"
    elif _return in enemy_deck:
        $ selectenemycard = enemy_deck.index(_return)
        $ response_card = "NewTurn"
        return "NewTurn"
    
    elif _return == "Close":
        $ selectcard = -1
        $ selectenemycard = -1
        hide screen card_battle
        $ response_card = "Close"
        return "Close"
        
    elif _return == "unselect":
        $ selectcard = -1
        $ selectenemycard = -1
        $ response_card = "NewTurn"
        return "NewTurn"
        
    else:
        if not selectcard == -1:
            play sound "sounds/card.mp3"
            $ y = int(math.floor(int(_return)/3))
            $ x = int(_return)-(y*3)
            
            $ table_cards[x][y] = player_deck[selectcard]
            $ table_cards[x][y].playercard = True
            $ del player_deck[selectcard]
            $ selectcard = -1
            $ update_table(x,y)
            
            pause 0.7 # Autoplay enemy card
            if (len(player_deck) == 0 or len(enemy_deck) == 0):
                $ response_card = "EndGame"
                if check_winner() == "win":
                    show screen card_end_message("You win!")
                    play sound "sounds/card_win.ogg" #Fanfare
                elif check_winner() == "draw":
                    show screen card_end_message("Draw")
                else:
                    show screen card_end_message("You lost...")
                pause 3 # Pause before end
                hide screen card_end_message
                hide screen card_battle 
                with dissolve
                # Replay weather SFX
                if raining:
                    $ renpy.music.play("sounds/rain.mp3", "weather", fadeout=1.0, fadein=1.0)
                if blizzard:
                    $ renpy.music.play("sounds/blizzard.ogg", "weather", fadeout=1.0, fadein=1.0)
                return "EndGame"
                
            call enemy_turn
            play sound "sounds/card.mp3"
            $ response_card = "AfterEnemy"
            if (len(player_deck) == 0 or len(enemy_deck) == 0):
                $ response_card = "EndGame"
                if check_winner() == "win":
                    show screen card_end_message("You win!")
                    play sound "sounds/card_win.ogg" #Fanfare
                elif check_winner() == "draw":
                    show screen card_end_message("Draw")
                else:
                    show screen card_end_message("You lost...")
                pause 3 # Pause before end
                hide screen card_end_message
                hide screen card_battle 
                with dissolve
                # Replay weather SFX
                if raining:
                    $ renpy.music.play("sounds/rain.mp3", "weather", fadeout=1.0, fadein=1.0)
                if blizzard:
                    $ renpy.music.play("sounds/blizzard.ogg", "weather", fadeout=1.0, fadein=1.0)
                return "EndGame"
            return "NewTurn"
        else:
            $ response_card = "NewTurn"
            return "NewTurn"
        
label enemy_turn:
    python:
        high_score = 0
        high_score_card = None
        high_score_pos = 0
        
        for card in enemy_deck:
            tuple_my = card.getAIScore(table_cards)
            if tuple_my[0] > high_score:
                high_score = tuple_my[0]
                high_score_pos = tuple_my[1]
                high_score_card = card
                
        y = int(math.floor(int(high_score_pos)/3))
        x = int(high_score_pos)-(y*3)
        del enemy_deck[enemy_deck.index(high_score_card)]
        table_cards[x][y] = high_score_card        
        table_cards[x][y].playercard = False
        update_table(x,y)
    return
       
        
screen card_battle(l_playerdeck, l_enemydeck):
    zorder 5
    imagebutton idle "images/cardgame/card_table.png" action Return("unselect")
    
    #fix card error when you select the last card
    if not selectenemycard < len(l_enemydeck):
        $ selectenemycard = -1
        
    imagemap:
        ground "images/cardgame/card_table.png"

        for y in range(0,3):
            for x in range(0,3):
                if table_cards[x][y] == None:
                    hotspot (353+124*x, 25+184*y, 125, 182) clicked Return(str(x+y*3))
                else:
                    use cardrender(table_cards[x][y], 353+124*x, 25+184*y, cardzoom=0.375)
   
    for i in range(0, len(l_playerdeck)):
        if not selectcard == i:
            use cardrender(l_playerdeck[i], 18,17+80*i, True)
    
    if not selectcard == -1:
        use cardrender(l_playerdeck[selectcard], 54,17+80*selectcard)
        
    for i in range(0, len(l_enemydeck)):
        if not selectenemycard == i:
            use cardrender(l_enemydeck[i], 898,17+80*i, True)
            
    if not selectenemycard == -1:
        use cardrender(l_enemydeck[selectenemycard], 860,17+80*selectenemycard)
        
    use close_button
        
screen cardrender(card, xpos_card, ypos_card, interact=False, return_value=None, cardzoom=0.5, color=True):
    if return_value == None:
        $ return_value = card
    frame:
        xpos xpos_card -4
        ypos ypos_card -4
        xsize card_width*cardzoom
        ysize card_height*cardzoom
        background #00000000

        if interact:
            imagebutton:
                if not color and card.copies <= -1:
                    idle grayTint(card.get_card_image(zoom=cardzoom))
                    hover grayTint(card.get_card_hover(zoom=cardzoom))
                else:
                    idle card.get_card_image(zoom=cardzoom)
                    hover card.get_card_hover(zoom=cardzoom)
                action Return(return_value)
        else:
            if not color:
                add grayTint(card.get_card_image(zoom=cardzoom))
            else:
                add card.get_card_image(zoom=cardzoom)
        
        if card.playercard:
            add playerborder zoom cardzoom
        else:
            add enemyborder zoom cardzoom
        
        $ lefttext = "{color=#ffffff}"
        $ righttext = "{/color}"
        
        if cardzoom >= 0.5:
            $ sizetext = 14
        else:
            $ sizetext = 10
        
        hbox:
            xsize card_width*cardzoom
            ysize card_height*cardzoom
            text lefttext+str(card.topvalue)+righttext xalign 0.5 yalign 0.03 size 18
        
        hbox:
            xsize card_width*cardzoom
            ysize card_height*cardzoom
            text lefttext+str(card.bottomvalue)+righttext xalign 0.5 yalign 0.985 size 18
        
        hbox:
            xsize card_width*cardzoom
            ysize card_height*cardzoom
            text lefttext+str(card.rightvalue)+righttext xalign 0.95 yalign 0.5 size 18
        
        hbox:
            xsize card_width*cardzoom
            ysize card_height*cardzoom
            text lefttext+str(card.leftvalue)+righttext xalign 0.05 yalign 0.5 size 18
        
        #Total Value
        hbox:
            xsize card_width*cardzoom
            ysize card_height*cardzoom
            # Set horizontal offset for single digit value
            # I have no idea why it has to be >= 25 but its the only value that works.
            if len(str(card.get_totalvalue())) >= 25:
                text lefttext+str(card.get_totalvalue())+righttext xalign 0.15 yalign 0.1 size sizetext
            else:
                text lefttext+str(card.get_totalvalue())+righttext xalign 0.15 yalign 0.1 size sizetext xoffset 5
            
screen start_deck:
    zorder 9

    for i in range(0, len(unlocked_cards)):
        use cardrender(unlocked_cards[i],40+125*i,200, interact=False, cardzoom=0.375)
        
screen card_end_message(message):
    zorder 9

    text "{color=#FFF}{size=+40}[message]{/size}{/color}" xpos 540 ypos 300 xalign 0.5 yalign 0.5 outlines [ (5, "#000", 0, 0) ]