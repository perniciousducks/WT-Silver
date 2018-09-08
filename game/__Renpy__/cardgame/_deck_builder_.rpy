label deck_builder:
    show screen deck_builder_screen()
    $ _return = ui.interact()

    if _return in unlocked_cards:
        $ selectcard = unlocked_cards.index(_return)
        jump deck_builder
    
    elif _return == "Close":
        $ selectcard = -1
        hide screen deck_builder_screen
        jump return_office
    elif _return == "inc":
        $ currentpage += currentpage+1
        jump deck_builder
    elif _return == "dec":
        $ currentpage += -1
        jump deck_builder
    else:
        if not selectcard == -1:
            python:
                unlocked_cards[selectcard].copies += -1
                add_card_to_deck(playerdeck[int(_return)].title)
                playerdeck[int(_return)] = unlocked_cards[selectcard]
                selectcard = -1
            jump deck_builder
            
        else:
            jump deck_builder

screen deck_builder_screen:
    $ card_shown=5
    add "images/cardgame/deck_builder.png"
 
    for i in range(0, card_shown):
        if not selectcard == (currentpage*card_shown)+i:
            use cardrender(unlocked_cards[i], 20,60+70*i, True)
    
    if not selectcard == -1:
        use cardrender(unlocked_cards[selectcard], 60,60+70*selectcard-(currentpage*card_shown))
        add im.Scale(unlocked_cards[selectcard].imagepath, card_width*0.25, card_height*0.25) xpos 805 ypos 63
    
    for i in range(0,5):
        # Need to get the amount this way since renpy dont save the pointer so after you load a game the card in the playerdeck is not the same as in unlocked_cards anymore
        if not selectcard == -1 and unlocked_cards[selectcard].copies > 0:
            use cardrender(playerdeck[i], 193+115*i,60, True, return_value=i) 
        else:
            use cardrender(playerdeck[i], 193+115*i,60, False, return_value=i) 
            
        vbox:
            xpos 258
            ypos 252
            xsize 170
            ysize 33
            text unlocked_cards[selectcard].get_title() xalign 0.5 yalign 0.5
            
        vbox:
            xpos 645
            ypos 252
            xsize 112
            ysize 33
            text unlocked_cards[selectcard].get_amount() xalign 0.5 yalign 0.5
            
        vbox:
            xpos 262
            ypos 310
            xsize 490
            ysize 160
            text unlocked_cards[selectcard].get_description()
    
    if not currentpage <= 0:
        imagebutton:
            xpos 190
            ypos 240
            idle "interface/general/"+interface_color+"/button_arrow_up.png"
            hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
            action Return("dec")
            
    if currentpage < math.ceil((len(unlocked_cards)-1)/card_shown):
        imagebutton:
            xpos 190
            ypos 292
            idle "interface/general/"+interface_color+"/button_arrow_down.png"
            hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
            action Return("inc")
            
    hbox:
        xpos 805
        ypos 380
        xsize 260
        ysize 40
        add Solid(get_hex_string(playercolor_r, playercolor_g, playercolor_b), xsize = 40) 
        textbutton "{color=#8f939b}"+"Player border color"+"{/color}" action Jump("playercolor_change") background "#ffffff00"
        
    hbox:
        xpos 805
        ypos 430
        xsize 260
        ysize 40
        add Solid(get_hex_string(enemycolor_r, enemycolor_g, enemycolor_b), xsize = 40) 
        textbutton "{color=#8f939b}"+"Enemy border color"+"{/color}" action Jump("enemycolor_change") background "#ffffff00"
  
    use close_button

label playercolor_change:
    "The color is rgb and is from 0 to 255"
    $ playercolor_r = float(renpy.input("Red"))/255
    $ playercolor_g = float(renpy.input("Green"))/255
    $ playercolor_b = float(renpy.input("Blue"))/255
    $ playerboarder = playerTint("images/cardgame/sides.png")
    jump deck_builder
    
label enemycolor_change:
    "The color is rgb and is from 0 to 255"
    $ enemycolor_r = float(renpy.input("Red"))/255
    $ enemycolor_g = float(renpy.input("Green"))/255
    $ enemycolor_b = float(renpy.input("Blue"))/255
    $ enemyboarder = enemyTint("images/cardgame/sides.png")
    jump deck_builder