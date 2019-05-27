

screen weasley_store_room():
    tag room_screen

    if daytime:
        add "images/rooms/weasley_store/store_day.png"
    else:
        add "images/rooms/weasley_store/store_night.png"

    use ui_top_bar

    zorder 0



label open_weasley_store:
    show screen blkfade
    with d3

    call room("weasley_store")
    call gen_chibi("hide")

    call play_music("weasley_store")

    if store_intro_done:
        call gen_chibi("stand","left","base")
        call hide_blkfade
    else:
        call gen_chibi("stand","0","base")
        call hide_blkfade

        call gen_walk(xpos="left", ypos="base", speed=1.4)

    pause.2

    $ renpy.block_rollback()

    call store_chit_chat

    $ store_category = 0 # Reset Button
    $ store_menu = True #Displays item's gold value.

    jump gift_shop_menu



label store_chit_chat:
    if not store_intro_done:
        $ store_intro_done = True
        fre "Professor Dumbledore? What are you doing here? I thought you didn't leave your office anymore."
        ger "You're not here to shut us down are you?"
        m "Shut you down? What for?"
        fre "NOTHING!"
        ger "We certainly aren't selling potions that we stole from Snape."
        fre "No sir! No prohibited goods being sold here."
        ger "None at all!"
        fre "But if we did sell them-"
        ger "Which we don't-"
        fre "They would be sold at the best prices in the school."
        ger "Unbeatable."
        m "Hmmmm. What sort of potions are you \'not\' selling?"
        fre "Well we aren't selling polyjuice potion."
        ger "Wouldn't dream of it."
        m "Well do you sell anything else?"
        ger "We have books, treats, and knick-knacks for sale."
        fre "Take a look."

    # After talking to Snape about Cho.
    # If you haven't yet beaten the Quiz.
    elif cho_intro_state not in ["event_1","event_2","talk_with_snape"] and quidditch_book_1_ITEM.unlocked == False and cho_quiz_complete == False:
        m "Boys..."
        twi "Hello again mr Dumbledore sir..."
        ger "What can we do for you?"
        m "Just having a look around at your fine merchandise..."
        fre "If you’re worried, don’t be... Everything is completely above board and procured from totally legitimate sources."
        ger "No stolen goods here..."
        m "I wasn’t looking out for stolen goods in particular, should I?"
        ger "Oh, well..."
        ger "Of course you weren’t..."
        m "Seems like I can’t find what I’m looking for anyway..."
        fre "Well, if you’re looking for something in particular then we could always look into procuring said item."
        ger "What type of object are you looking for?"
        m "Well... as you boys may know, the Quidditch season is starting soon..."
        fre "Yes?"
        m "Well, I realized that I haven't actually gone in depth with the sport yet."
        fre "I find that hard to believe... You’re telling me that \"the\" Dumbledore doesn’t know anything about Quidditch?"
        ger "Explains why you’d always just stare out in the distance and just clap politely..."
        m "I was always more fond of Basketball myself."
        fre "Sounds like the muggle sport our dad always goes on about...."
        fre "But in any case, since both George and I are on the Gryffindor team."
        m "You are?"
        ger "Yes... don’t you keep any kind of records on these things?"
        m "Of course, I’m just... forgetful when it comes to names, that’s all."
        ger "Understandable..."
        m "But, as I said, I’d like to get a runthrough of the basics of Quidditch this year."
        m "You don’t happen to have a Quidditch book to refresh my memories?"
        fre "Of course, you can have ours. We know it off by heart at this point!"

        $ quidditch_book_1_ITEM.unlocked = True
        $ quidditch_book_1_ITEM.unlockable = False # Makes it clickable in the menu.
        call give_gift(">You have unlocked a new book to read!", quidditch_book_1_ITEM)

        m "Great, thanks again boys..."
        twi "Don’t mention it..."
        twi "Make sure to take notes!"
        m "Are you assuming your headmaster doesn’t know how studying works?"
        fre "Of course not..."
        #ger "Anyway... if you need anything else we should have another book coming in at some point which is not just about the basics of Quidditch..."

    elif deck_unlocked and her_know_cards and not twins_know_cards:
        m "Hello boys."
        twi "Good day professor\nDumbledore, sir."
        m "I'm looking to acquire some Wizard cards."
        call play_sound("spit")
        fre "Wizard cards....*spit*"
        ger "Why would you want any of those?"
        m "What does one do with playing cards... play the game of course."
        fre "Well, we got some of our own to see if it was worth stocking them, but none for sale."
        ger "The profit margin was way to low... something about import tax."
        ger "We would have to sell a lot of them to make good profit."
        m "I see... so there's no way you'd stock them?"
        fre "Wizard cards hasn't been popular in ages..."
        ger "It does have potential though, not everyone at Hogwarts is going to be into dueling... or chess."
        fre "How about this... we did acquire a set of cards to try the game out."
        m "So..."
        ger "If you beat us we'll do a trial run and stock some cards for the students."
        twi "\"There's no way this\nold man would ever beat us.\""
        $ twins_know_cards = True
        jump twins_duel_menu

    elif twins_cards_stocked and not twins_second_win and not twins_cards_stocked_talk:
        m "Well, well. Looking good as always boys!"
        twi "..."
        m "In a professional sense that is, don't you worry... How are things going?"
        ger "Ah, yes... you were right sir, we've seemed to have struck gold with Wizard Cards."
        g9 "Glad to hear it."
        fre "In fact, we've sold out on our first batch."
        g4 "What, where am I supposed to get my cards then?"
        ger "Surely a professional like you would only need to win your cards?"
        m "Oh... yes of course, a professional like me..."
        fre "Anyway, we've gone ahead and put up a official unofficial tier system ladder."
        m "Unofficial... Official, you say?"
        ger "Yes, as we mentioned... there isn't really any official tournament rules."
        fre "We've sort of kept it that way in that we'll let the people playing set their own wagers and challenges to climb the ladder."
        fre "Any normal game will make you one token richer and once the agreed upon winning conditions for a challenge is reached you'll get 3 tokens."
        ger "And whatever other forfeit your opponent might have added."
        fre "3 challenges won will let you climb to the next tier."
        ger "Which lets you challenge even higher skilled players."
        m "And by skilled you mean players with better cards?"
        fre "Something like that."
        m "I see..."
        m "How do I know which players are currently in my tier?"
        fre "Ah yes, there's a notice board behind us. You should see some people that you know on it."
        ger "Snape was in here earlier to pick up some tokens."
        m "Snape was in here, he doesn't disapprove of your business?"
        fre "He was using a polyjuice potion to disguise himself as a student."
        ger "But that weird walk of his where he sort of slides across the floor gives him away a mile off."
        fre "Tell you what, lets set a wager right now. Usually we'd make it a bit more difficult but since you gave us the idea for this."
        ger "Beat us again and we'll give you 3 tokens."
        m "That's it? Sounds a bit out of character for you guys making it this easy."
        fre "Let's call it an insurance so that we can continue our business."
        ger "There's no way you'll beat us again anyway."
        $ twins_cards_stocked_talk = True
        jump twins_duel_menu

    else:
        if twins_interest:
            $ twins_interest = False
            twi "Greetings Dumbledore, sir!"
            m "Hello boys."
            m "I'm here to pick up my weekly cut of profits."
            twi "Of course!"

            $ her_help = 0
            if her_shop_help:
                ger "Miss Granger has helped us with promotions this week so that means more profits."
                $ her_help = 200
                $ her_shop_help = False

            $ shop_profit = renpy.random.randint(50+her_help, 300)
            ger "Here, your weekly cut."
            call give_reward("You've received "+str(int(shop_profit*twins_profit))+" gold.", "interface/icons/gold.png")

            $ gold += int(shop_profit*twins_profit)
            ger "..."
            twi "Did you need anything else?"

        else:
            twi "Hello Professor! Came here to buy?"

        if twins_know_cards:
            twi "Or duel?"
            label twins_menu:
            menu:
                "-Buy something-":
                    pass
                "-Let's duel- {image=interface/cards.png}":
                    label twins_duel_menu:
                    if geniecard_level < 2:
                        menu:
                            "-First Duel-":
                                jump twins_first_duel
                            "-Challenge-" if twins_first_win:
                                jump twins_second_duel
                            "{color=#858585}-You need to beat the first duel-{/color}" if not twins_first_win:
                                jump twins_duel_menu
                            "-Never mind-":
                                twi "Your loss professor."
                                pass
                    else:
                        jump twins_random_duel

    return



label close_weasley_store:
    hide screen weasley_store_menu
    hide screen gift
    show screen blkfade
    with d5

    $ store_menu = False #Displays item's gold value.

    jump main_room



screen weasley_store_menu():
    tag store_menu
    $ UI_xpos_offset = 100

    zorder 4

    # Close Button
    use top_bar_close_button

    # Gifts Button
    imagebutton:
        xpos 725 +UI_xpos_offset
        ypos 105
        idle "interface/general/"+interface_color+"/button_select.png"
        if store_category != 0: # Gifts
            hover "interface/general/"+interface_color+"/button_select_hover.png"
            action [SetVariable("store_category",0), Jump("gift_shop_menu")]
    if store_category == 0: # Gifts
        text "Gifts" xalign 0.5 yalign 0.5 xpos 767 +UI_xpos_offset ypos 121 size 16
    else:
        text "Gifts" xalign 0.5 yalign 0.5 xpos 767 +UI_xpos_offset ypos 121 size 14

    # Books Button & Scrolls + Tentacle Scroll
    imagebutton:
        xpos 725 +UI_xpos_offset
        ypos 105+44
        idle "interface/general/"+interface_color+"/button_select.png"
        if store_category != 1: # Books
            hover "interface/general/"+interface_color+"/button_select_hover.png"
            action [SetVariable("store_category",1), Jump("book_shop_menu")]
    if store_category == 1: # Books
        text "Books" xalign 0.5 yalign 0.5 xpos 767 +UI_xpos_offset ypos 121+44 size 16
    else:
        text "Books" xalign 0.5 yalign 0.5 xpos 767 +UI_xpos_offset ypos 121+44 size 14

    # Potions
    imagebutton:
        xpos 725 +UI_xpos_offset
        ypos 105+88
        idle "interface/general/"+interface_color+"/button_select.png"
        if store_category != 2:
            hover "interface/general/"+interface_color+"/button_select_hover.png"
            action [SetVariable("store_category",2), Jump("shop_potion_menu")]
    if store_category == 2:
        text "Potions" xalign 0.5 yalign 0.5 xpos 767 +UI_xpos_offset ypos 121+88 size 16
    else:
        text "Potions" xalign 0.5 yalign 0.5 xpos 767 +UI_xpos_offset ypos 121+88 size 14

    # Token Shop
    if twins_cards_stocked:
        imagebutton:
                xpos 725+95 +UI_xpos_offset
                ypos 105
                idle "interface/general/"+interface_color+"/button_select.png"
                if store_category != 3:
                    hover "interface/general/"+interface_color+"/button_select_hover.png"
                    action [SetVariable("store_category",3), Jump("token_shop_menu")]
        if store_category == 3:
            text "Tokens" xalign 0.5 yalign 0.5 xpos 767+95 +UI_xpos_offset ypos 121 size 16
        else:
            text "Tokens" xalign 0.5 yalign 0.5 xpos 767+95 +UI_xpos_offset ypos 121 size 14



#Gifts
label gift_shop_menu:
    show screen weasley_store_menu

    python:
        item_list = []
        if toggle1_bool:
            item_list.extend(candy_gift_list)
        if toggle2_bool:
            item_list.extend(drink_gift_list)
        if toggle3_bool:
            item_list.extend(mag_gift_list)
        if toggle4_bool:
            item_list.extend(toy_gift_list)

        #item_list = list(filter(lambda x: x.unlocked==False, item_list))

    show screen list_menu(item_list, "Gifts", toggle1="Candy", toggle2="Beverages", toggle3="Mags", toggle4="Toys" )

    $ _return = ui.interact()

    hide screen list_menu
    if isinstance(_return, item_class):
        call object_gift_block(_return)

    elif _return == "Close":
        $ current_page = 0
        jump close_weasley_store

    elif _return == "toggle1":
        $ toggle1_bool = not toggle1_bool
        $ current_page = 0
    elif _return == "toggle2":
        $ toggle2_bool = not toggle2_bool
        $ current_page = 0
    elif _return == "toggle3":
        $ toggle3_bool = not toggle3_bool
        $ current_page = 0
    elif _return == "toggle4":
        $ toggle4_bool = not toggle4_bool
        $ current_page = 0

    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    jump gift_shop_menu

label object_gift_block(item):
    $ the_gift = item.get_image()
    show screen gift
    with d3

    "[item.description]"
    $ cost2 = item.cost * 2
    $ cost3 = item.cost * 4
    $ cost4 = item.cost * 8

    menu:
        "-Buy 1 for ([item.cost] galleons)-":
            call object_purchase_item(item, 1)
        "-Buy 2 for ([cost2] galleons)-":
            call object_purchase_item(item, 2)
        "-Buy 4 for ([cost3] galleons)-":
            call object_purchase_item(item, 4)
        "-Buy 8 for ([cost4] galleons)-":
            call object_purchase_item(item, 8)
        "-Never mind-":
            pass

    hide screen gift
    with d3

    return

label object_purchase_item(item, quantity):
    $ transit_time = renpy.random.randint(1, 5)
    $ order_cost = item.cost*quantity
    if gold >= (order_cost):
        menu:
            "-add next day delivery (15 galleons)-" if gold >= order_cost + 15:
                $ gold -= 15
                $ transit_time = 1
            "{color=#858585}-add next day delivery (15 galleons)-{/color}" if gold < order_cost + 15:
                pass
            "-no thanks-":
                pass
        $ gold -= order_cost
        $ deliveryQ.send(item, transit_time, quantity,'Gift')
        if transit_time ==  1:
            "Thank your for shopping at \"Dahr's oddities\". Your order shall be delivered tomorrow."
        else:
            "Thank your for shopping at \"Dahr's oddities\". Your order shall be delivered in 1 to [transit_time] days."

    else:
        m "I don't have enough gold."

    hide screen gift
    with d3

    return



#Books & Scrolls
label book_shop_menu:
    show screen weasley_store_menu

    if not book_store_intro_done:
        hide screen weasley_store_menu
        hide screen list_menu
        with d3

        fre "These books are mostly light erotica..."
        ger "Some of the girls insisted that I order them in."
        $ book_store_intro_done = True
        pause.5

        jump book_shop_menu

    python:
        item_list = []
        if toggle1_bool:
            item_list.extend(book_list.fiction_books)
        if toggle2_bool:
            item_list.extend(book_list.read_books)
            item_list.extend(book_list.write_books)
        if toggle3_bool:
            item_list.extend(forbidden_scroll_list)
            item_list.extend(scroll_list_A)
            item_list.extend(scroll_list_B)
            item_list.extend(scroll_list_C)

        item_list = list(filter(lambda x: x.unlocked==False and x.unlockable==False, item_list))

    show screen list_menu(item_list, "Books & Scrolls", toggle1="Fictional", toggle2="Educational", toggle3="Scrolls" )

    $ _return = ui.interact()

    hide screen list_menu

    if isinstance(_return, item_class):
        if _return.type == "book":
            call purchase_book(_return)
        else:
            if _return in forbidden_scroll_list:
                call purchase_forbidden_scroll(_return)
            else:
                call purchase_scroll(_return)

    elif _return == "Close":
        $ current_page = 0
        jump close_weasley_store

    elif _return == "toggle1":
        $ toggle1_bool = not toggle1_bool
        $ current_page = 0
    elif _return == "toggle2":
        $ toggle2_bool = not toggle2_bool
        $ current_page = 0
    elif _return == "toggle3":
        $ toggle3_bool = not toggle3_bool
        $ current_page = 0

    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    jump book_shop_menu

label purchase_book(item):
    $ the_gift = item.get_image()
    show screen gift
    with d3
    "[item.description]"
    menu:
        "-Buy the book for [item.cost] gold -":
            if gold >= item.cost:
                $ gold -= item.cost
                $ item.unlocked = True
                "Book [item.name] has been added to your collection."
            else:
                m "I don't have enough gold."
        "-Never mind-":
            pass

    hide screen gift
    with d3

    return

label purchase_forbidden_scroll(item):
    hide screen weasley_store_menu
    with d3

    if her_whoring <= 15:
        m "What's in this scroll?"
        ger "Don't worry about it."
        m "Why?"
        ger "You're not ready for what's in this scroll."
        m "Well that just makes me want it more."
        ger "Too bad."
        return

    m "What's this scroll?"
    fre "This is the recipe for a powerful and forbidden potion."
    ger "Acquired completely legitimately I might add!"
    m "What does it do?"
    fre "It transforms you into any magical creature you desire."
    m "Like what?"
    fre "Anything you can secure a sample of."
    ger "A powerful phoenix, a terrifying gorgon, a deadly basilisk or an awe inspiring dragon."
    m "Not sure I'd really want to transform into any of those..."
    ger "Well then perhaps there is a creature that would suit you and your \"Hobbies\"."
    m "Such as?"
    fre "There are rumors of a \"plant\" hidden somewhere on the school grounds"
    m "A plant? Why would I want to be a plant?"
    ger "This is no ordinary plant, it has fast and powerful limbs that are incredibly sensitive"
    m "So it's a tentacle monster?"
    ger "Pretty much. We're not sure where it lives however."
    fre "No idea!"
    ger "Certainly not in the attic!"
    m "Ok, well how much is the scroll?"
    ger "300 gold coins."
    m "300! Why on earth is it so expensive?"
    fre "Forbidden magic is quite a risky and expensive endeavor Professor, We'll sell it for no less than 300."

    menu:
        "-Buy the scroll ([item.cost] gold)":
            if gold >= item.cost:
                m "Fine, here's the money"
                ger "Thank you very much"
                $ the_gift = item.get_image() # SACRED SCROLL.
                show screen gift
                with d3

                $ gold -= item.cost
                $ item.unlocked = True
                ">A New scroll has been added to your sacred scrolls collection."
            else:
                m "I don't have enough gold."
        "-No thanks-":
            m "No thanks, not right now"
            fre "Perhaps later then"

    hide screen gift
    with d3

    return

label purchase_scroll(item):
    $ the_gift = item.get_image() # SACRED SCROLL.
    show screen gift
    with d3
    ">A scroll containing sacred knowledge.\n(May also contain spoilers)."
    menu:
        "-Buy the scroll ([item.cost] gold)-":
            if gold >= item.cost:
                $ gold -= item.cost
                $ item.unlocked = True
                ">A New scroll has been added to your sacred scrolls collection."
            else:
                m "I don't have enough gold."
        "-Never mind-":
            pass

    hide screen gift
    with d3

    return



label shop_potion_menu:
    hide screen weasley_store_menu
    hide screen list_menu
    with d3

    python:
        potion_menu = []
        potion_menu.append(("-Questions acquiring items-", "questions"))
        for potion in potion_lib.getBuyable():
            if her_whoring < potion.whoring_rec:
                potion_menu.append(("{color=#858585}-"+potion.name+"-{/color}","her_whoring"))
            else:
                potion_menu.append(("-"+potion.name+"-",potion))
        potion_menu.append(("-Never mind-", "nvm"))
        PotionOBJ = custom_menu(potion_menu)
    if isinstance(PotionOBJ, silver_potion):
        python:
            potion_menu = []
            potion_menu.append(("-Buy the potion for "+str(PotionOBJ.cost)+" Gold-", PotionOBJ))
            potion_menu.append(("-Never mind-", "nvm"))
            choice = custom_menu(potion_menu)
        if isinstance(choice, silver_potion):
            if gold >= PotionOBJ.cost:
                $ gold -= PotionOBJ.cost
                $ potion_inv.add(PotionOBJ.id)
                $ renpy.say(m, PotionOBJ.name+" aquired, although it's missing a key ingredient...")
            else:
                $ renpy.say(m, "I don't have enough gold.")
        jump shop_potion_menu
    if PotionOBJ == "questions":
        menu:
            "-Knotgrass-":
                m "Do you know where I can find \"Knotgrass\"?"
                fre "You can sometimes find Knotgrass by the forbidden forest."
            "-Root of Aconite-":
                m "Do you know where I can find \"Root of Aconite\"?"
                ger "Root of Aconite can be found down by the lake."
            "-Wormwood-":
                m "Do you know where I can find \"Wormwood\"?"
                ger "Wormwood is sometimes found in the forbidden forest."
            "-Niffler's Fancy-":
                m "Do you know where I can find \"Niffler's Fancy\"?"
                fre "Hmm... I think I heard that it's found by the lake."
        jump shop_potion_menu
    if PotionOBJ == "her_whoring":
        "Hermione must be \"Trained\" more before you can purchase this."
    if PotionOBJ == "nvm":
        pass
    $ store_category = 0
    jump gift_shop_menu




# Token Shop
label token_shop_menu:
    show screen weasley_store_menu

    call update_deco_items

    python:
        item_list = []

        if toggle1_bool:
            item_list.extend([hg_gamble_slut_ITEM])
        if toggle2_bool:
            item_list.extend(fireplace_deco_list)
            item_list.extend(cupboard_deco_list)
            item_list.extend(wall_deco_list)
            item_list.extend(misc_deco_list)
            item_list.extend(misc_hat_list)

        item_list = list(filter(lambda x: x.unlocked==False, item_list))

    show screen list_menu(item_list, "Token Shop", toggle1="Outfits", toggle2="Decorations")

    $ _return = ui.interact()

    hide screen list_menu

    if isinstance(_return, item_class):
        call purchase_deco(_return)

    elif _return == "Close":
        $ current_page = 0
        jump close_weasley_store

    elif _return == "toggle1":
        $ toggle1_bool = not toggle1_bool
        $ current_page = 0
    elif _return == "toggle2":
        $ toggle2_bool = not toggle2_bool
        $ current_page = 0
    elif _return == "toggle3":
        $ toggle3_bool = not toggle3_bool
        $ current_page = 0
    elif _return == "toggle4":
        $ toggle4_bool = not toggle4_bool
        $ current_page = 0

    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    jump token_shop_menu

label purchase_deco(item):
    $ the_gift = item.get_image()
    show screen gift
    with d3
    "[item.description]"

    if item.type == "outfit_token":
        $ item_token_str = "A new \"%s\" outfit has been added to Hermiones' wardrobe." % item.name
        $ item_token_type = " outfit"
    else:
        $ item_token_str = "%s has been added to your decoration menu." % item.type
        $ item_token_type = ""
    menu:
        "-Buy [item.name][item_token_type] for [item.cost] tokens -":
            if geniecard_tokens >= item.cost:
                $ geniecard_tokens -= item.cost
                $ item.unlocked = True
                "[item_token_str]"

                if len(filter(lambda x: x.unlocked==False, wall_deco_list)) <= 0:
                    $ achievement.unlock("postman")
                if len(filter(lambda x: x.unlocked==False, misc_hat_list)) <= 0:
                    $ achievement.unlock("hats")
            else:
                m "I don't have enough tokens."
        "-Never mind-":
            pass

    hide screen gift
    with d3

    return
