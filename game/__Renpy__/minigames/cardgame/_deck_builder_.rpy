label deck_builder:
    hide screen main_room_menu
    show screen deck_builder_screen
    $ _return = ui.interact()

    if _return in unlocked_cards:
        $ selectcard = unlocked_cards.index(_return)
        jump deck_builder
    
    elif _return == "Close":
        $ selectcard = -1
        hide screen deck_builder_screen
        jump day_main_menu
    elif _return == "inc":
        $ currentpage += 1
        $ selectcard = -1
        jump deck_builder
    elif _return == "dec":
        $ currentpage -= 1
        $ selectcard = -1
        jump deck_builder
    elif _return == "unselect":
        $ selectcard = -1
        jump deck_builder
    else:
        if not selectcard == -1:
            python:
                if unlocked_cards[selectcard].copies > -1:
                    unlocked_cards[selectcard].copies -= 1
                    add_card_to_deck(playerdeck[int(_return)].title)
                    playerdeck[int(_return)] = unlocked_cards[selectcard]
                    selectcard = -1
                    pass
            jump deck_builder
            
        else:
            jump deck_builder

screen deck_builder_screen:
    zorder 8
    $ card_shown=5
    imagebutton idle "images/cardgame/deck_builder.png" action Return("unselect")

    for i in range(0, clamp(card_shown, 0, (len(unlocked_cards))-(card_shown*currentpage))):
            use cardrender(unlocked_cards[clamp(i+(currentpage*card_shown), 0, len(unlocked_cards))], 18,17+80*i, True, color=False)
            
    if not selectcard == -1:
        use cardrender(unlocked_cards[selectcard], 885,316)
        #add im.Scale(unlocked_cards[selectcard].imagepath, card_width*0.5, card_height*0.5) xpos 885 ypos 316
        
        vbox:
            xpos 560
            ypos 320
            xsize 340
            ysize 33
            text unlocked_cards[selectcard].get_title() xalign 0 yalign 0.5 size 22
            
        vbox:
            xpos 760
            ypos 520
            xsize 112
            ysize 33
            text unlocked_cards[selectcard].get_amount() xalign 1 yalign 0.5
            
        vbox:
            xpos 560
            ypos 520
            xsize 112
            ysize 33
            text "{color=#ffffff}Value:{/color}"+unlocked_cards[selectcard].get_totalvalue() xalign 0 yalign 0.5
            
        vbox:
            xpos 560
            ypos 350
            xsize 300
            ysize 500
            text unlocked_cards[selectcard].get_description()
    
    for i in range(0,5):
        # Need to get the amount this way since renpy dont save the pointer so after you load a game the card in the playerdeck is not the same as in unlocked_cards anymore
        if not selectcard == -1 and unlocked_cards[selectcard].copies > 0:
            use cardrender(playerdeck[i], 223+165*i,17, True, return_value=i) 
        else:
            use cardrender(playerdeck[i], 223+165*i,17, True, return_value=i) 
        
        #$ lefttext = "{color=#ffffff}"
        #$ righttext = "{/color}"
    
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
    
    #Exit button
    imagebutton:
        xpos 274
        ypos 502
        idle "images/cardgame/button.png"
        hover "images/cardgame/button_hover.png"
        action Return("Close")
    
    #Easter egg    
    hbox:
        xpos 1020
        ypos 296
        xsize 40
        ysize 40
        button action Jump("color_change") background "#ffffff00"
        #add Solid(get_hex_string(playercolor_r, playercolor_g, playercolor_b))
  
    use close_button

label color_change:
    menu:
        "-Change player color-":
            "Enter the color in RGB format (0 to 255)"
            $ playercolor_r = float(renpy.input("Red", "", "0123456789", length=3))/255
            $ playercolor_g = float(renpy.input("Green", "", "0123456789", length=3))/255
            $ playercolor_b = float(renpy.input("Blue", "", "0123456789", length=3))/255
            $ playerborder = playerTint("images/cardgame/border.png")
            pass
        "-Change enemy color-":
            "Enter the color in RGB format (0 to 255)"
            $ enemycolor_r = float(renpy.input("Red", "", "0123456789", length=3))/255
            $ enemycolor_g = float(renpy.input("Green", "", "0123456789", length=3))/255
            $ enemycolor_b = float(renpy.input("Blue", "", "0123456789", length=3))/255
            $ enemyborder = enemyTint("images/cardgame/border.png")
            pass
        "-Reset-":
            $ playercolor_r = 51.0/255.0
            $ playercolor_g = 92.0/255.0
            $ playercolor_b = 147.0/255.0
            $ enemycolor_r = 116.0/255.0
            $ enemycolor_g = 0
            $ enemycolor_b = 0
            $ playerborder = playerTint("images/cardgame/border.png")
            $ enemyborder = enemyTint("images/cardgame/border.png")
            pass
        "-Exit-":
            pass
    jump deck_builder