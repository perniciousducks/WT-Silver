

# Tonks Gift Menu
label tonks_gift_menu:

    python:

        category_list = [] #Max 5 items! #Use the item's name inside the 'interface/icons' folder.
        category_list.append("ui_gifts")
        #category_list.append("ui_quest_items")

        if current_category == None:
            current_category = category_list[0]
            category_choice = category_list[0]

        item_list = []
        if current_category == "ui_gifts":
            menu_title = "Gift Items"
            item_list.extend(candy_gift_list)
            item_list.extend(mag_gift_list)
            item_list.extend(drink_gift_list)
            item_list.extend(toy_gift_list)
        if current_category == "ui_quest_items":
            menu_title = "Quest Items"
            item_list.extend(toy_gift_list)

        #item_list = list(filter(lambda x: x.unlocked==False, item_list))
    show screen bottom_menu(item_list, category_list, menu_title, xpos=0, ypos=475)

    $ _return = ui.interact()

    hide screen bottom_menu
    if category_choice != current_category:
        $ current_category = _return

    elif isinstance(_return, item_class):
        if _return.number > 0:
            call give_ton_gift(_return)
            jump tonks_requests
        else:
            ">You don't own this item."
            jump tonks_gift_menu

    elif _return == "Close":
        $ current_page = 0
        $ category_choice = None
        hide screen bottom_menu
        with d3

        jump tonks_requests

    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    jump tonks_gift_menu



# Tonks Gift Responses

label give_ton_gift(gift_item):
    hide screen tonks_main
    with d5

    $ gave_tonks_gift = True

    if gift_item == lollipop_ITEM:
        call ton_main("A lollipop?",face="neutral",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the lollipop to Tonks...", gift_item)
        call ton_main("I know the perfect student to give this to.",face="happy")
        call ton_friendship(plus=1)

    if gift_item == chocolate_ITEM:
        call ton_main("Mhmm, Chocolate!",pupils="down",face="happy",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the chocolate to Tonks...", gift_item)
        call ton_main("It's said that chocolate is a very effective mood enhancer after a Dementor attack.",mouth="open",face="happy")
        call ton_main("That's because chocolate is considered to be a great aphrodisiac...",face="horny")
        call ton_main("I'll keep this for one of my private lessions.",face="happy")
        call ton_friendship(plus=1)

    if gift_item == plush_owl_ITEM:
        call ton_main("An Owl?",face="neutral",xpos="mid",ypos="base",trans="d5")
        call ton_main("Oh, it's a toy... Haven't seen one of these in a while.",face="disgusted")
        call give_gift(">You give the stuffed owl to Tonks...",gift_item)
        call ton_main("Okay, for nostalgias sake then...",face="neutral")
        call ton_friendship(plus=0)

    if gift_item == butterbeer_ITEM:
        call ton_main("Butterbeer?",face="disgusted",xpos="mid",ypos="base",trans="d5")
        call ton_main("Don't you have anything stronger?",mouth="open",face="annoyed")
        call give_gift(">You give the the bottle to Tonks...", gift_item)
        call ton_main("Just joking, I'll save it for when I've got company.",face="happy")
        call ton_friendship(plus=1)

    if gift_item == science_mag_ITEM:
        call ton_main("Jinxes and sphinxes? These could help for some of my lessons.",mouth="open",face="neutral",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give an assortment of educational magazines to Tonks...", gift_item)
        call ton_main("Thank you, [ton_genie_name].",face="neutral")
        call ton_friendship(plus=0)

    if gift_item == girls_mag_ITEM:
        call ton_main("Some girl magazines? I could definitely put these in my classroom.",mouth="open",face="neutral",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give an assortment of rather girly magazines to Tonks...", gift_item)
        call ton_main("The girls do love staying after hours to socialize.",face="happy")
        call ton_friendship(plus=0)

    if gift_item == adult_mag_ITEM:
        call ton_main("Adult magazines?",face="disgusted",xpos="mid",ypos="base",trans="d5")
        call ton_main("Wont be the first time I've slipped one in the stack of magazines in my classroom",face="horny")
        call give_gift(">You give an assortment of adult magazines to Tonks...", gift_item)
        call ton_main("Thank you, [ton_genie_name].",face="happy")
        call ton_friendship(plus=1)

    if gift_item == porn_mag_ITEM:
        call ton_main("Porn magazines?",face="disgusted",xpos="mid",ypos="base",trans="d5")
        call ton_main("I already know most positions in this book already of course...",face="happy")
        call give_gift(">You give an assortment of pornographic magazines to Tonks...", gift_item)
        call ton_main("Although...",face="horny")
        call ton_main("I'll keep them. Thank you, [ton_genie_name].",face="happy")
        call ton_friendship(plus=1)

    if gift_item == krum_poster_ITEM:
        call ton_main("That's that Krum boy is it?",face="horny",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the poster to Tonks...", gift_item)
        call ton_main("Nice figure, could set a good mood in the classroom... Or my office.",pupils="down",face="happy")
        call ton_main("Thank you, [ton_genie_name].",face="happy")
        call ton_friendship(plus=1)

    if gift_item == sexy_lingerie_ITEM:
        call ton_main("Oh, I see you're a man of a sense of style.",mouth="open",pupils="down",face="happy",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the sexy lingerie to Tonks...", gift_item)
        call ton_main("If it were up to me these would be part of the school uniform...",face="happy")
        call ton_friendship(plus=1)

    if gift_item == pink_condoms_ITEM:
        call ton_main("Some condoms?",face="neutral",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give some condoms to Tonks...", gift_item)
        call ton_main("Safe sex is important...",face="neutral")
        call ton_main("I don't remember taking sex ed when I was in school,... maybe I was too busy experimenting it myself that day....",face="horny")
        call ton_friendship(plus=1)

    if gift_item == vibrator_ITEM:
        call ton_main("A vibra... back massager?",face="disgusted",xpos="mid",ypos="base",trans="d5")
        call ton_main("Mm, Mine seemingly went missing from my desk. This should do if it doesn't turn up again.",face="annoyed")
        call give_gift(">You give the vibrator to Tonks...", gift_item)
        call ton_main("Thank you, [ton_genie_name].",face="neutral")
        call ton_friendship(plus=1)

    if gift_item == anal_lube_ITEM:
        call ton_main("That's one big jar of Anal lube you have there.",face="disgusted",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the jar of lube to Tonks...", gift_item)
        call ton_main("What's the difference between this and regular lube?",mouth="open",face="disgusted")
        call ton_main("Seems like it might be enough to cover the whole body...",mouth="open",face="happy")
        call ton_main("Thank you, [ton_genie_name].",face="neutral")
        call ton_friendship(plus=1)

    if gift_item == ballgag_and_cuffs_ITEM:
        call ton_main("Ball gag and cuffs?",pupils="down",face="happy",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the ball gag and cuffs to Tonks...", gift_item)
        call ton_main("These are pretty cute. Should come in handy during my.... private lessons.",face="horny")
        call ton_friendship(plus=1)

    if gift_item == anal_plugs_ITEM:
        call ton_main("Some anal plugs?",face="disgusted",xpos="mid",ypos="base",trans="d5")
        call ton_main("Wow, this is what they use these days? Very colorful...",face="happy")
        call give_gift(">You give an assortment of anal plugs to Tonks...", gift_item)
        call ton_main("I think I might leave some in one of the desks...",face="horny")
        call ton_friendship(plus=1)

    if gift_item == testral_strapon_ITEM:
        call ton_main("Is that a strap-on?",mouth="open",eye="wide",brows="wide",pupils="wide",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the thestral strap-on to Tonks...", gift_item)
        call ton_main("This will be a perfect addition to my collection...",face="angry")
        call ton_main("Thank you, [ton_genie_name].",face="happy")
        call ton_friendship(plus=2)

    if gift_item == broom_2000_ITEM:
        call ton_main("I don't remember the brooms looking like this when I took flying lessons...",face="angry",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the broom to Tonks...", gift_item)
        call ton_main("Seems like a good way to stay put on the broom though... unless you lose focus.",mouth="open",face="happy")
        call ton_main("Which you probably will with this...",face="horny")
        call ton_friendship(plus=3)

    if gift_item == sexdoll_ITEM:
        call ton_main("a sex doll?",face="horny",xpos="mid",ypos="base",trans="d5")
        call ton_main("Not too useful for me, but I might put it in one of our secret gift exchanges.",mouth="open",face="horny")
        call give_gift(">You give the sex doll to Tonks...", gift_item)
        call ton_main("They'll gossip for weeks wondering who it's from.",face="horny")
        call ton_friendship(plus=1)

    hide screen tonks_main
    with d5
    call ton_main(xpos="base",ypos="base",trans="d5")

    return


label ton_friendship(plus=None, minus=None):
    show screen blktone5
    with d3

    if plus == 0 or minus == 0:
        "Tonks' friendship towards you hasn't changed much."

    elif plus != None:
        $ ton_friendship += plus
        if plus == 1:
            "Tonks likes you a bit more now."
        else:
            "Tonks likes you a lot more now."

    elif minus != None:
        $ ton_friendship += -minus
        if minus == 1:
            "Tonks didn't seem to like that."
        else:
            "Tonks likes you a bit less now."

    if ton_friendship < 0:
        $ ton_friendship = 0
    if ton_friendship > 100:
        $ ton_friendship = 100

    hide screen blktone5
    #Add transition after return.

    return
