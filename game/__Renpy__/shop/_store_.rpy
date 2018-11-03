label __init_variables:
    if not hasattr(renpy.store,'gift_item_inv'): #important! Gift_Item.ID == Index in this array
        $ gift_item_inv = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if not hasattr(renpy.store,'shop_found'): #important!
        $ shop_found = False
    if not hasattr(renpy.store,'sscroll_'): #important!
        $ sscroll_ = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    if not hasattr(renpy.store,'fiction_books_intro'): #important!
        $ fiction_books_intro = False

    if not hasattr(renpy.store,'sacred_scrolls'):
        $ sacred_scrolls = [
            silver_scroll(id=1 , title="The room",           cost=10,    comments=["This is a first ever draft of the Dumbledore's office.","Not a very exciting thing to look at, sure. But holds great historical value."]),
            silver_scroll(id=2 , title="The calendar",       cost=30,    comments=["The calendar...","On the early stages of development I toyed with an idea of implementing an actual in-game calendar into the gameplay...","I soon realized how much more difficult it would be to create a game like that...","And since I personally believe that any time limits in any game always work against the fun factor I decided to abandon the idea...","Later on I used this drawing as a parchment paper for letters to be written on..."]),
            silver_scroll(id=3 , title="The girl",           cost=40,    comments=["A couple of very early drawings of Hermione..."]),
            silver_scroll(id=4 , title="Deeptroating",       cost=70,    comments=["The deepthroating scene...","My first attempt.","Been deemed unworthy and ended up here."]),
            silver_scroll(id=5 , title="Poster 01",          cost=80,    comments=["The game poster...","Hermione is Dahr's work. The rest is me..."]),
            silver_scroll(id=6 , title="Poster 02",          cost=80,    comments=["Alternative game poster.","This one has never been released."]),
            silver_scroll(id=7 , title="Chibi-dancing",      cost=90,    comments=["Some chibi closeups.","The one on the left never made it into the final game..."]),
            silver_scroll(id=8 , title="Game items",         cost=50,    comments=["A banch of items that I ended up not using...","I blame dahr and his awesome artwork."]),
            silver_scroll(id=9 , title="Panties no panties", cost=90,    comments=["The drawing of Hermione from the poster. (by Dahr)","I like one on the right with her panties still on."]),
            silver_scroll(id=10, title="A lot of pegs",      cost=50,    comments=["Another ithing that never made it into the final game...","The idea here was that the more you level up Hermione the more pegs she would let you to put on her...","And the nipple chain was supposed to be worn to class under the uniform."]),
            silver_scroll(id=11, title="House-elf brothel",  cost=110,   comments=["The house-elf brothel... Just another thing that never happened."]),
            silver_scroll(id=12, title="Me and Lola",        cost=110,   comments=["A drawing featuring yours truly as a Durmstrung mage and Lola as a student...","The drawing itself is by Dahr of course."]),
            silver_scroll(id=13, title="Hard training",      cost=100,   comments=["Another one of those side-quests that never happened...","This one was about--","No, I better not. Who knows, maybe we will get to adding those quests eventually."]),
            silver_scroll(id=14, title="Wizard's Chess",     cost=80,    comments=["Another sub-quest...","This one involving the school's wizard chess club."]),
            silver_scroll(id=15, title="Tutoring books",     cost=40,    comments=["There is more then one way for a pretty girl to carry her books around.","I thought it would be cool to change the way Hermione carries the books as she progresses with her training.","Since the whole tutoring arc got canceled I am showing it here..."]),
            silver_scroll(id=16, title="Extra gifts 01",     cost=30,    comments=["A couple of items that didn't make it into the final game...","The one on the left is an actual live house-elf to give as a present.","The one on the right is a portrait of a pervy but wise wizard. Supposed to be helping with studying..."]),
            silver_scroll(id=17, title="Extra gifts 02",     cost=30,    comments=["Few more items...","A newspaper, a bottle of perfume and a magical hat that says things you want to hear..."]),
            silver_scroll(id=18, title="Fiction books",      cost=90,    comments=["The fiction books...","The top row are my sketches, the bottom row are finalized drawings by dahr."]),
            silver_scroll(id=19, title="Singer whore",       cost=50,    comments=["A drawing of a famous singer.","Has no connection to this game and is here for no reason whatsoever."]),
            silver_scroll(id=20, title="Casting",            cost=70,    comments=["It took me a while to come up with a proper look for Hermione...","Version \"A\" was my first attempt. And I liked it up until the moment when I started to hate it...","Version \"B\" was my second attempt. And it's good. But her confident and semi-aggressive facial features didn't fit the character well...","Version \"C\" is the one that got the role. The Hermione that we all grew to care for by now, I'm sure."]),
            silver_scroll(id=21, title="Witch robe 01",      cost=90,    comments=["Sub-quests that never happened.","You are allowed to feel bad for rushing me.","If you did not rush me you are allowed to feel angry at people who did."]),
            silver_scroll(id=22, title="Witch robe 02",      cost=90,    comments=["Hermione presenting her body to Genie...","This would have been a quite memorable scene..."]),
            silver_scroll(id=23, title="Witch robe 03",      cost=150,   comments=["Didn't expect this one, did you?","In case you're wondering this is still Hermione."]),
            silver_scroll(id=24, title="Witch robe 04",      cost=150,   comments=[".................................","Sub-quests of course..."]),
            silver_scroll(id=25, title="The walk",           cost=100,   comments=["Another sub-quest...","We had a rather lengthy discussion with Dahr about this one...","I was sort of against it, but then Dahr sent me this picture and it made me shut up."]),
            silver_scroll(id=26, title="Durmstrang",         cost=80,    comments=["One the very early stages of development I had an idea of representing outcomes of your failed or successfully completed sub quests with a simplistic plates, or photographs...","At first many of the sub-quests involved deciding on how to spend the Hogwarts budget...","Spend your money to finance the school quiddich team, or to hire new teachers and such..."]),
            silver_scroll(id=27, title="Gag ball",           cost=200,   comments=["Isn't she adorable?"]),
            silver_scroll(id=28, title="New clothes 01",     cost=150,   comments=["Another (rather lengthy) sub-quest..."]),
            silver_scroll(id=29, title="New clothes 02",     cost=200,   comments=[".........."]),
            silver_scroll(id=30, title="The gang",           cost=70,    comments=["One of the very early sketches related to the quiddich sub-quests..."])
        ]

    return

label shop_intro:
    show screen shop_screen
    if shop_found:
        twi "Hello Professor! What would you like to buy?"
        jump shop_menu
    else:
        $ show_clothes_store = True
        $ shop_found = True
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
        jump shop_menu

label shop_menu:
    show screen shop_screen
    call screen shop_screen_menu

screen shop_screen_menu:
    tag room_screen

    zorder hermione_main_zorder-1

    if daytime:
        add "interface/map/room_bg1.png" at Position(xpos=140)
    else:
        add "interface/map/room_bg2.png" at Position(xpos=140)

    imagemap:
        ground "interface/map/shop_ground.png"
        hover "interface/map/shop_hover.png"
        # (X upper-left corner, Y upper-left corner, width, height).
        hotspot (0, 0, 266, 110) clicked Jump("sscrolls") #Scrolls 1
        hotspot (0, 215, 233, 80) clicked Jump("shop_books") #Books
        hotspot (70, 340, 85, 75) clicked Jump("gifts_menu") #Gift Box
        hotspot (0, 455, 230, 128) clicked Jump("tentacle_shop_scene") #Tentacle Scroll
        hotspot (606+280, 0, 197, 538) clicked Jump("shop_potion_menu") #Potions
        hotspot (750+280, 550, 40, 40) clicked [Show("main_room_menu"),Jump("day_main_menu")] #Return Button

screen shop_screen:
    tag room_screen

    zorder hermione_main_zorder-1

    if daytime:
        add "interface/map/room_bg1.png" at Position(xpos=140)
    else:
        add "interface/map/room_bg2.png" at Position(xpos=140)
    
    add "interface/map/shop_ground.png"        
        
label sscrolls:
    jump store_scrolls
label sscrolls2:
    jump store_scrolls

label store_scrolls:
    python:
        scrolls_menu = list(filter(lambda x: x.purchased==False, sacred_scrolls))
        
    show screen shop_screen
    show screen generic_scroll_menu(scrolls_menu, "Scroll Stock" )
    $ _return = ui.interact()
    
    hide screen generic_scroll_menu

    if isinstance(_return, generic_menu_item):
        $ the_gift = _return.imagepath # SACRED SCROLL.
        show screen gift
        with d3
        dahr "A scroll containing sacred knowledge.\n(May also contain spoilers)."
        menu:
            "-Buy the scroll ([_return.cost] gold)-":
                if gold >= _return.cost:
                    $ gold -= _return.cost
                    $ _return.purchased = True
                    $ sscroll_[_return.id] = True # Turns TRUE if the scroll had been bought.
                    $ renpy.play('sounds/win_04.mp3')   #Not loud.
                    ">A New scroll has been added to your sacred scrolls collection."
                    hide screen gift
                    with d3
                    call thx_4_shoping2 #Massage that says "Thank you for shopping here!".                    
                else:
                    call no_gold #Massage: m "I don't have enough gold".
                    hide screen gift
 
            "-Never mind-":
                hide screen gift
        
        
    elif _return == "Close":
        $ currentpage = 0
        jump shop_menu
       
    elif _return == "inc":
        $ currentpage += 1
    elif _return == "dec":
        $ currentpage += -1
           
    jump store_scrolls
        


label shop_books:
    show screen shop_screen
    if not fiction_books_intro:
        twi "These books are mostly light erotica..." 
        ger "Some of the girls insisted that I order them in."
        $ fiction_books_intro = True
    else:
        twi "What type of book would you like?"
        
    label shop_book_menu:
    python:
        books_menu_list = []
        if toogle1_bool:
            books_menu_list.extend(Books_OBJ.read_books)
            books_menu_list.extend(Books_OBJ.write_books)
        if toogle2_bool:
            books_menu_list.extend(Books_OBJ.fiction_books)
        
        books_menu_list = list(filter(lambda x: x.purchased==False, books_menu_list))
       
    show screen shop_screen
    show screen generic_scroll_menu(books_menu_list, "Book Stock", toogle1="Educational Books", toogle2="Fiction Books" )
    
    $ _return = ui.interact()
    
    hide screen generic_scroll_menu

    if isinstance(_return, generic_menu_item):
        call purchase_book(_return)
        
    elif _return == "Close":
        $ currentpage = 0
        jump shop_menu
        
    elif _return == "toogle1":
        $ toogle1_bool = not toogle1_bool
    elif _return == "toogle2":
        $ toogle2_bool = not toogle2_bool
        
    elif _return == "inc":
        $ currentpage += 1
    elif _return == "dec":
        $ currentpage += -1
        
    jump shop_book_menu
    
label purchase_book(BookOBJ):
    $ the_gift = BookOBJ.imagepath
    show screen gift
    with d3
    "[BookOBJ.description]"
    menu:
        "-Buy the book for [BookOBJ.cost] gold -":
            if gold >= BookOBJ.cost:
                $ gold -= BookOBJ.cost
                $ BookOBJ.purchased = True
                "Book [BookOBJ.title] has been added to your collection."
                hide screen gift
                with d3
            else:
                call no_gold #Massage: m "I don't have enough gold".
        "-Never mind-":
            hide screen gift
    return


label shop_potion_menu:
    show screen shop_screen
    python:
        potion_menu = []
        potion_menu.append(("-Questions acquiring items-", "questions"))
        for potion in potion_lib.getBuyable():
            if whoring < potion.whoring_rec:
                potion_menu.append(("{color=#858585}-"+potion.name+"-{/color}","whoring"))
            else:
                potion_menu.append(("-"+potion.name+"-",potion))
        potion_menu.append(("-Never mind-", "nvm"))
        PotionOBJ = renpy.display_menu(potion_menu)
    if isinstance(PotionOBJ, silver_potion):
        python:
            potion_menu = []
            potion_menu.append(("-Buy the potion for "+str(PotionOBJ.cost)+" Gold-", PotionOBJ))
            potion_menu.append(("-Never mind-", "nvm"))
            choice = renpy.display_menu(potion_menu)
        if isinstance(choice, silver_potion):
            if gold > PotionOBJ.cost:
                $ gold -= PotionOBJ.cost
                $ potion_inv.add(PotionOBJ.id)
                $ renpy.say(m, PotionOBJ.name+" aquired, although it's missing a key ingredient...")
            else:
                $ renpy.say(m, "I don't have enough gold.")
        call screen shop_screen_menu
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
    if PotionOBJ == "whoring":
        call cust_excuse("Hermione mus be \"Trained\" more before you can purchase this.")
    if PotionOBJ == "nvm":
        pass
    call screen shop_screen_menu


label gifts_menu:
    show screen shop_screen

    show screen generic_scroll_menu(gift_list, "Gift Stock")
    
    $ _return = ui.interact()
    
    hide screen generic_scroll_menu
    if isinstance(_return, generic_menu_item):
        call object_gift_block(_return) 
        
    elif _return == "Close":
        $ currentpage = 0
        jump shop_menu

    elif _return == "inc":
        $ currentpage += 1
    elif _return == "dec":
        $ currentpage += -1
        
    jump gifts_menu
    
label object_gift_block(item):
    $ the_gift = item.imagepath
    show screen gift
    with d3
    #$ tmp = item.description
    dahr "[item.description]"
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
            hide screen gift
            pass

    return

label object_purchase_item(item, quantity):
    $ transit_time = renpy.random.randint(1, 5)
    $ order_cost = item.cost*quantity
    if gold >= (order_cost):
        menu:
            "-add next day delivery (15 galleons)-" if gold >= order_cost + 15:
                $ gold -= 15
                $ transit_time = 1
                # $ next_day = True
            "{color=#858585}-add next day delivery (15 galleons)-{/color}" if gold < order_cost + 15:
                pass
            "-no thanks-":
                pass
        $ gold -= order_cost
        $ deliveryQ.send(item,transit_time,quantity,'Gift')
        # $ gift_order = item
        # $ order_placed = True
        if transit_time ==  1:
            dahr "Thank your for shopping at \"Dahr's oddities\". Your order shall be delivered tomorrow."
        else:
            dahr "Thank your for shopping at \"Dahr's oddities\". Your order shall be delivered in 1 to [transit_time] days."
        hide screen gift
        with d3

    else:
        call no_gold #Massage: m "I don't have enough gold".

    return





### ALREADY HAVE THIS BOOK
label do_have_book:
    show screen bld1
    m "I already own this one."
    hide screen bld1
    hide screen gift
    with d3
    return

### THANK YOU FOR shopping here.
label thx_4_shoping:
    # $ days_in_delivery2 = one_of_five  #Generating one number out of three for various porpoises.

    if one_of_five ==  1:
        dahr "Thank your for shopping at \"Dahr's oddities\". Your order shall be delivered tomorrow."
        hide screen gift
        with d3
        return
    else:
        dahr "Thank your for shopping at \"Dahr's oddities\". Your order shall be delivered in 1 to [one_of_five] days."
        hide screen gift
        with d3
        return

### THANK YOU FOR shopping here. IMMEDIATE DELIVERY.
label thx_4_shoping2:
    dahr "Thank your for shopping at \"Dahr's oddities\"."
    hide screen gift
    with d3
    return

### NOT ENOUGH GOLD ###
label no_gold:
    m "I don't have enough gold... This is depressing..."
    hide screen gift
    with d3
    return

### ITEM IS OUT OF STOCK ###
label out:
    show screen bld1
    with d3
    dahr "This item is currently out of stock."
    hide screen bld1
    with d3
    jump gifts_menu
