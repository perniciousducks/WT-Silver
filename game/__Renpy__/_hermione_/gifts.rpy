

# Hermione Gift Menu

label hermione_gift_menu:
    call update_quest_items

    python:

        category_list = []
        category_list.append("ui_gifts")
        category_list.append("ui_quest_items")

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
            item_list.extend(her_quest_items_list)

        #item_list = list(filter(lambda x: x.unlocked==False, item_list))
    show screen bottom_menu(item_list, category_list, menu_title, xpos=0, ypos=475)

    $ _return = ui.interact()

    hide screen bottom_menu
    if category_choice != current_category:
        $ current_category = _return

    elif isinstance(_return, item_class):
        if _return in her_quest_items_list:
            menu:
                "Would you like to use this quest item?"
                "\"(Yes, let's do it!)\"":
                    $ quest_item = _return
                    jump give_her_quest_item
                "\"(Not right now.)\"":
                    jump hermione_gift_menu
        elif _return.number > 0:
            call give_her_gift(_return)
        else:
            ">You don't own this item."
            jump hermione_gift_menu

        if her_mood != 0:
            jump hermione_gift_menu
        else:
            jump hermione_requests

    elif _return == "Close":
        $ current_page = 0
        $ category_choice = None
        hide screen bottom_menu
        with d3

        jump hermione_requests

    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    jump hermione_gift_menu



# Hermione Gift Responses

label give_her_quest_item: #(quest_item)

    $ gave_hermione_gift = True

    if quest_item == sealed_scroll_ITEM:
        jump tentacle_scene_intro

    if quest_item == collar_quest_ITEM:
        ">This Quest is now active!\nIt will start the next morning."
        $ collar = 5
        call update_quest_items
        jump hermione_gift_menu




label give_her_gift(gift_item):
    hide screen hermione_main
    with d5
    call her_main(xpos="mid",ypos="base",trans="d5")

    $ gave_hermione_gift = True

    if gift_item == lollipop_ITEM:#candy
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("A lollipop?","base","base")
            call give_gift(">You give the candy to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","base","base")
            call happy(5)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("Candy?","normal","base")
            call her_main("Candy is for kids, [genie_name].","open","base")
            call give_gift(">You give the candy to Hermione...",gift_item)
            call her_main("Thank you...","annoyed","worriedL")
            call happy(5)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("Candy?","normal","base")
            call give_gift(">You give the candy to Hermione...",gift_item)
            call her_main("Ehm... Sure, thanks...","open","suspicious")
            call happy(5)
        if her_whoring >= 18: # Lv 7+
            call her_main("A lollipop?","base","base")
            call her_main("Clever girls use candy like this as a \"weapon\".","smile","baseL")
            call give_gift(">You give the candy to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","base","happyCl")
            call happy(5)
    if gift_item == chocolate_ITEM:#chocolate
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("A chocolate bar?","base","base")
            call give_gift(">You give the chocolate to Hermione...", gift_item)
            call her_main("Thank you, [genie_name].","base","base")
            call happy(10)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("A chocolate bar?","normal","base")
            call her_main("Hm...","annoyed","frown")
            call her_main("That thing about fairies...")
            call her_main("That is a joke of some sort, right?","open","worried")
            call give_gift(">You give the chocolate to Hermione...", gift_item)
            call her_main("Thank you...","soft","base")
            call happy(10)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("A chocolate bar?","normal","base")
            call her_main("I just like the way it crunches, [genie_name]! N-not the taste...","grin","worriedCl",emote="05")
            call give_gift(">You give the chocolate to Hermione...", gift_item)
            call her_main("Ehm... Sure, thanks...","base","base")
            call happy(10)
        if her_whoring >= 18: # Lv 7+
            call her_main("A chocolate bar?","base","base")
            call her_main("You spoil me, [genie_name].","smile","angry")
            call give_gift(">You give the chocolate to Hermione...", gift_item)
            call her_main("Thank you.","base","suspicious")
            call happy(10)
    if gift_item == plush_owl_ITEM:#plush owl
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("A stuffed owl?","base","base")
            call her_main("It's cute...","base","base")
            call give_gift(">You give the owl to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","base","base")
            call happy(7)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("A plush toy?","open","worried")
            call her_main("I like it!","base","base")
            call give_gift(">You give the owl to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","base","base")
            call happy(10)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("A toy?","base","base")
            call her_main("Toys are for kids, [genie_name].","open","base")
            call her_main("But I'll take it...","annoyed","worriedL")
            call give_gift(">You give the owl to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","base","base")
            call happy(15)
        if her_whoring >= 18: # Lv 7+
            call her_main("This is one of those adult toys isn't it?","disgust","glance")
            call her_main("There's got to be a switch or a button somewhere...","open","down")
            call her_main("So... Does it vibrate or something?","base","down")
            call her_main("Oh...?","open","squint",cheeks="blush")
            call her_main("So it is really just a plush toy then?")
            call her_main("Shame...","angry","down_raised")
            call her_main("I mean, thank you, [genie_name].","angry","worriedCl",emote="05")
            call give_gift(">You give the owl to Hermione...",gift_item)
            call happy(4)
    if gift_item == butterbeer_ITEM:#butterbeer
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("Butterbeer?","base","base")
            call her_main("Are you sure about that, [genie_name]?","open","suspicious")
            call her_main("It does contain alcohol, you know...","base","base")
            call give_gift(">You give the bottle to Hermione...",gift_item)
            call her_main("Thank you.","base","base")
            call happy(3)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("Butterbeer, [genie_name]?","open","worried")
            call her_main("To let you in on a little secret, [genie_name]...","open","base")
            call her_main("I'm a big fan of this completely harmless beverage.","base","base")
            call give_gift(">You give the bottle to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","base","base")
            call happy(10)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("Butterbeer?","base","base")
            call her_main("Thank you, [genie_name].","grin","worriedCl",emote="05")
            call give_gift(">You give the bottle to Hermione...",gift_item)
            call her_main("I shall drink this with the girls later.","base","base")
            call happy(15)
        if her_whoring >= 18: # Lv 7+
            call her_main("Butterbeer...?","base","base")
            call her_main("Thank you, [genie_name].","base","base")
            call give_gift(">You give the bottle to Hermione...",gift_item)
            call her_main("I shall drink this later with the boys.","base","base")
            call her_main("Err... I meant to say with the girls, of course.","open","baseL",cheeks="blush")
            call happy(20)
    if gift_item == science_mag_ITEM:#edu mags
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("\"Popular magic\" magazines?","base","base")
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_item)
            call her_main("Thank you, [genie_name]!","base","base")
            call her_main("I will use them for my research!")
            call happy(15)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("Sometimes I find information in magazines that I could never find in a book...","base","base")
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_item)
            call her_main("Thank you, [genie_name]!","base","base")
            call her_main("I will use them for my research!")
            call happy(10)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("Oh...","open","base")
            call her_main("Yes, I used to read magazines like that a lot...","base","base")
            call her_main("Lately not so much though...","open","worriedL")
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_item)
            call her_main("Thank you, [genie_name]!","base","base")
            call happy(3)
        if her_whoring >= 18: # Lv 7+
            call her_main("Ehm...","open","worriedL")
            call her_main("To be honest, magazines like that lost their appeal to me completely lately...","open","suspicious")
            call her_main("But I don't mind taking them off you hands anyway, [genie_name].","open","worried")
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_item)
            call her_main("Thank you.","soft","baseL")
            call no_change
    if gift_item == girls_mag_ITEM:#girl mags
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("Hm?","soft","base")
            call her_main("This is the sort of press some \"slytherin\" bimbo would appreciate.","annoyed","suspicious")
            call her_main("I am way above silly magazines like that, [genie_name].","open","closed")
            call no_change
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("I don't read magazines of that nature, [genie_name]...","open","angryCl")
            call her_main("................","soft","baseL")
            call her_main("But I could give it a try just to humour you I suppose...","open","angryCl")
            call give_gift(">You give an assortment of rather girly magazines to Hermione...",gift_item)
            call her_main("Thank you, [genie_name]!","open","suspicious")
            call happy(5)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("I ashamed to admit this, but...","open","worriedL")
            call her_main("I really enjoy reading magazines like that lately...","grin","worriedCl",emote="05")
            call give_gift(">You give an assortment of rather girly magazines to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","open","suspicious")
            call happy(15)
        if her_whoring >= 18: # Lv 7+
            call her_main("The Latest edition of \"Girlz\"?!","angry","wide")
            call her_main("I can't have enough of that brilliant magazine!","grin","worriedCl",emote="05")
            call give_gift(">You give an assortment of rather girly magazines to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","open","suspicious")
            call happy(15)
    if gift_item == adult_mag_ITEM:#adult mags
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("Are that...?","open","base")
            call her_main("Adult magazines, [genie_name]?","open","base")
            call her_main("Given to me by An esteemed wizard of your status?","annoyed","angryL")
            call her_main("[genie_name], surely you could find a more productive way to spend your free time.","disgust","glance")
            call her_main("And I most definitely would not have use for those...","angry","angry")
            call upset(7)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("Adult magazines?","angry","angry")
            call her_main("[genie_name], I have no interest in things like that.","annoyed","angryL")
            call her_main("And how is this an appropriate present for one of your students, [genie_name]?","angry","angry")
            call upset(3)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("Adult magazines?","open","base")
            call her_main("[genie_name], this is such an inappropriate present for a girl my age...","angry","worriedCl",emote="05")
            call give_gift(">You give an assortment of adult magazines to Hermione...",gift_item)
            call her_main("I shall throw these away myself...","annoyed","annoyed")
            call happy(8)
        if her_whoring >= 18: # Lv 7+
            call her_main("The New edition of \"L.o.v.e.\"!!!","smile","happyCl")
            call her_main("Err.. I mean, adult magazines?","angry","wink")
            call her_main("This is a little inappropriate...")
            call her_main("But I will take them...","base","happyCl")
            call give_gift(">You give an assortment of adult magazines to Hermione...",gift_item)
            call her_main("thank you, [genie_name].","base","happyCl")
            call happy(15)
    if gift_item == porn_mag_ITEM:#porn mags
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("Hm... What is this?","base","base")
            call her_main("[genie_name], those are porn magazines!","scream","wide")
            call her_main("Shame on you, [genie_name]!","angry","angry",cheeks="blush")
            call upset(15)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("Porn magazines?","shock","wide")
            call her_main("[genie_name], what do you expect me to do with those?","open","down")
            call her_main("Research them?","annoyed","annoyed")
            call her_main("Despicable!","scream","angry",emote="01")
            call upset(8)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("That's hardcore porn, [genie_name].","open","base")
            call her_main("Which is a completely inappropriate gift for a girl my age!","angry","worriedCl",emote="05")
            call her_main("..............","angry","down_raised")
            call her_main("But I will take them...","angry","base")
            call give_gift(">You give an assortment of porn magazines to Hermione...",gift_item)
            call her_main("And I shall throw them in the trash, where they and... girls who like these things belong...","annoyed","annoyed")
            call no_change
        if her_whoring >= 18: # Lv 7+
            call her_main("Pornography?","shock","wide")
            call her_main("................","angry","down_raised")
            call her_main("How can women even agree to do things like that, [genie_name]?","angry","base")
            call her_main(".................","angry","down_raised")
            call her_main("Alright, I shall accept them...","upset","closed")
            call her_main("Solely for research purposes of course...","open","baseL",cheeks="blush")
            call give_gift(">You give an assortment of porn magazines to Hermione...",gift_item)
            call happy(15)
    if gift_item == krum_poster_ITEM:#krum poster
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("A Quidditch poster?","annoyed","down")
            call her_main("What am I supposed to do with it, [genie_name]?","annoyed","annoyed")
            call her_main("No, thank you.","annoyed","closed")
            call no_change
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("A Quidditch poster?","annoyed","down")
            call her_main("Hm...","annoyed","annoyed")
            call her_main("I think I saw this player once or twice...","annoyed","down")
            call her_main("He is that Durmstrang student, right?","base","base")
            call give_gift(">You give the poster to Hermione...",gift_item)
            call happy(5)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("A Viktor Krum poster, [genie_name]?","annoyed","down")
            call her_main("Can't say that I care much for Quidditch, but...","open","suspicious")
            call her_main("I can see why the girls find the brutish physique of some players appealing...","open","down")
            call give_gift(">You give the poster to Hermione...",gift_item)
            call happy(15)
        if her_whoring >= 18: # Lv 7+
            call her_main("A Viktor Krum poster?!","scream","wide_stare")
            call her_main("Thank you, [genie_name]!","grin","worriedCl",emote="05")
            call give_gift(">You give the poster to Hermione...",gift_item)
            call her_main("Can't wait to hang it over my bed!","smile","baseL")
            call her_main("The girls will go green with envy...","smile","glance")
            call happy(25)
    if gift_item == sexy_lingerie_ITEM:#lingerie
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("lingerie?","angry","down_raised")
            call her_main("[genie_name], I cannot accept a gift like this from you...","upset","closed")
            call upset(10)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("sexy lingerie?","angry","down_raised")
            call her_main("You know I cannot possibly accept a gift like that from you, [genie_name].","angry","base")
            call her_main("(It's pretty though).........","angry","down_raised")
            call no_change
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("sexy lingerie?","base","down")
            call her_main("[genie_name] that is so inappropriate...","angry","wink")
            call give_gift(">You give the lingerie to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","base","baseL",cheeks="blush")
            call happy(7)
        if her_whoring >= 18: # Lv 7+
            call her_main("sexy lingerie?","base","down")
            call her_main("Do You think it will make me look like one of the witches in those adult magazines, [genie_name]?","grin","dead")
            call her_main("Oh... I mean, thank you, [genie_name].","angry","wink")
            call give_gift(">You give the lingerie to Hermione...",gift_item)
            call happy(15)
    if gift_item == pink_condoms_ITEM:#condoms
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("Condoms?!","angry","wide")
            call her_main("[genie_name], I wouldn't even know what to do with them...","scream","angryCl")
            call upset(6)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("...Condoms?","normal","frown")
            call her_main("Ehm... Is this a part of some new Hogwarts sex ed program or something?","open","angryCl")
            call her_main("No, [genie_name]... It feels wrong to accept a thing like this from you...","open","baseL",cheeks="blush")
            call no_change
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("A pack of condoms?","normal","base")
            call her_main("[genie_name], what possible use could I have for those?")
            call her_main("Well, I shall accept them simply because it is rude to refuse a gift...","open","angryCl")
            call give_gift(">You give a pack of condoms to Hermione...", gift_item)
            call happy(3)
        if her_whoring >= 18: # Lv 7+
            call her_main("A pack of condoms?","open","suspicious")
            call her_main("I appreciate your concern, [genie_name]. Thank you.","base","glance")
            call give_gift(">You give a pack of condoms to Hermione...", gift_item)
            call happy(4)
    if gift_item == vibrator_ITEM:#vibrator
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("A magic wand?","base","base")
            call her_main("No, it doesn't look like--","soft","base")
            call her_main(".........?")
            call her_main("!!!","angry","wide")
            call her_main("[genie_name]!","angry","angry",cheeks="blush")
            call her_main("This is just beyond inappropriate!","scream","angryCl")
            call upset(10)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("Is this what I think it is?","angry","down_raised")
            call her_main("[genie_name], let me remind you that I belong to the noble house of \"Gryffindor\".","open","annoyed",cheeks="blush")
            call her_main("A present like that would be appropriate for a girl from \"Slytherin\", [genie_name].","upset","closed")
            call upset(10)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("Is that a... vibrator?","angry","down_raised")
            call her_main("The design...")
            call her_main("it reminds me of my wand...")
            call her_main("Did you have this custom made for me [genie_name]?","angry","down_raised")
            call her_main("This is inappropriate...","scream","angryCl")
            call her_main("But I shall take it nonetheless...","annoyed","worriedL")
            call give_gift(">You give the vibrator to Hermione...",gift_item)
            call no_change
        if her_whoring >= 18: # Lv 7+
            call her_main("This vibrator...","open","worried")
            call her_main("It's... calling out for me...","open","worriedL")
            call her_main("But not in a dirty way, [genie_name].","disgust","glance")
            call give_gift(">You give the vibrator to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","base","down")
            call happy(10)
    if gift_item == anal_lube_ITEM:#anal lube
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("I don't know what this is...","open","base")
            call her_main("But I have the feeling that the jar is full of something vile and inappropriate...","angry","angry")
            call her_main("No, thank you, [genie_name].")
            call upset(6)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("Hm...","annoyed","down")
            call her_main("I think I know what this is...","disgust","glance")
            call her_main("But why would you give something like this to one of your pupils, [genie_name]?")
            call her_main("No, thank you.","annoyed","angryL")
            call upset(2)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("Anal lubricant?","angry","down_raised")
            call her_main("Ehm.. well... I know this girl...","open","baseL",cheeks="blush")
            call her_main("I mean I don't know her, she is a friend of a friend...")
            call her_main("Yes, I will take this for her...")
            call give_gift(">You give the jar to Hermione...",gift_item)
            call her_main("Still, I think you should not give presents like this to your pupils, [genie_name].","open","annoyed",cheeks="blush")
            call no_change
        if her_whoring >= 18: # Lv 7+
            call her_main("Anal lubricant, [genie_name]?","base","down")
            call her_main("I know a couple of girls who would do anything for a commodity like that.","open","annoyed",cheeks="blush")
            call her_main("Thank for looking out for us, [genie_name].","base","glance")
            call give_gift(">You give the jar to Hermione...",gift_item)
            call happy(5)
    if gift_item == ballgag_and_cuffs_ITEM:#gag and cuffs
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("What is this?","angry","down_raised")
            call her_main("Is this like one of those adult toys?","angry","suspicious",cheeks="blush")
            call her_main("What woman in her right mind would subject herself to a humiliation like that?","scream","angryCl")
            call her_main("And what possible use could I have for such objects?","open","annoyed",cheeks="blush")
            call her_main("This is just insulting, [genie_name]...","angry","angry",cheeks="blush")
            call upset(10)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("[genie_name], do you not realise how inappropriate it would be for me to accept a present like that?","open","annoyed",cheeks="blush")
            call her_main("And I would not even know what to do with them anyway...","open","baseL",cheeks="blush")
            call her_main("I mean these fluffy things are obviously handcuffs...","angry","down_raised")
            call her_main("But this ball... ehm...")
            call her_main("[genie_name], please...","upset","closed")
            call her_main("Just put them away.")
            call upset(5)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("A month ago I would've felt insulted to receive a gift like this...","upset","closed")
            call her_main("But by now I know that some girls really do find pleasure in toys like...","angry","down_raised")
            call her_main("But I assure you that I am not one of them, [genie_name].","upset","closed")
            call her_main("But I know a girl who knows a girl who is into things like...","open","baseL",cheeks="blush")
            call her_main("Yes, I shall take these to her...","base","baseL",cheeks="blush")
            call give_gift(">You give the ball gag and cuffs to Hermione...",gift_item)
            call happy(9)
        if her_whoring >= 18: # Lv 7+
            call her_main("A ball gag and handcuffs?","open","squint",cheeks="blush")
            call her_main("This is completely inappropriate, [genie_name].","angry","wink") # :)
            call her_main("But a gift is a gift, right?","base","suspicious")
            call give_gift(">You give the ball gag and cuffs to Hermione...",gift_item)
            call happy(15)
    if gift_item == anal_plugs_ITEM:#anal plugs
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("Hm...?","base","base")
            call her_main("Are those like key-chain toys?","soft","base")
            call give_gift(">You give the anal plugs to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","annoyed","annoyed")
            call happy(8)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("[genie_name], are those adult toys of some sort?","open","annoyed",cheeks="blush")
            call her_main("those are some of those anal things, aren't they?","angry","angry",cheeks="blush")
            call her_main("[genie_name] this is nothing but a weapon meant to oppress women!")
            call her_main("Despicable!","upset","closed")
            call upset(15)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("Yes, I know that some girls have uhm...","upset","closed")
            call her_main("Have use for things such as these...","open","annoyed",cheeks="blush")
            call her_main("But not me, [genie_name].")
            call her_main("No, thank you.","upset","closed")
            call no_change
        if her_whoring >= 18: # Lv 7+
            call her_main("Anal plugs?","angry","down_raised")
            call her_main("I have no use for things like that, [genie_name]...","angry","base")
            call her_main("They are so pretty though...","angry","wink")
            call her_main(".....................","angry","down_raised")
            call her_main("Well, alright. I shall take them off your hands if I must, [genie_name].","soft","ahegao")
            call give_gift(">You give the anal plugs to Hermione...",gift_item)
            call her_main("But I shall never use them of course...","open","closed")
            call her_main("................","base","down")
            call happy(10)
    if gift_item == testral_strapon_ITEM:#strap on
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("What is that?","angry","wide")
            call her_main("An artifact of some sort or a trophy?","open","base")
            call her_main("So well-crafted...","base","base")
            call her_main("Are you sure that it's alright for me to have it, [genie_name]?","base","base")
            call give_gift(">You give the strap-on to Hermione...",gift_item)
            call her_main("Thank you very much, [genie_name]. I promise to take good care of it.","open","closed")
            call happy(20)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("!!!","angry","wide")
            call her_main("That is...","angry","down_raised")
            call her_main("But it doesn't even look... human...")
            call her_main("I mean...","annoyed","angryL")
            call her_main("[genie_name], do you have no shame?!","scream","angry",emote="01")
            call her_main("Presenting a thing like that to a pupil?!")
            call her_main("..................","open","down")
            call her_main("Please put it away, [genie_name].","angry","angry")
            call upset(15)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("That thing...","angry","down_raised")
            call her_main("Is that the actual size of the... of the real \"thing\"?","angry","base")
            call her_main("I mean...","open","baseL",cheeks="blush")
            call her_main(".......................","angry","down_raised")
            call her_main("Is this like a party prank prop?","angry","base")
            call her_main("It's so well-crafted though...","angry","down_raised")
            call her_main("I will take it...","normal","worriedCl")
            call give_gift(">You give the strap-on to Hermione...",gift_item)
            call happy(10)
        if her_whoring >= 18: # Lv 7+
            call her_main("It's... It's magnificent, [genie_name]...","shock","wide")
            call her_main("Is it really modeled after a thestral?","open","baseL",cheeks="blush")
            call her_main("But the creatures are invisible...","open","squint",cheeks="blush")
            call her_main("..................","angry","down_raised")
            call her_main("Breathtaking...","grin","dead")
            call her_main("Not in the way you think, [genie_name]...","upset","closed")
            call her_main("I am merely admiring the craftsmanship...","open","closed")
            call give_gift(">You give the strap-on to Hermione...",gift_item)
            call her_main("Thank you for the gift, [genie_name].","base","suspicious")
            call happy(30)
    if gift_item == broom_2000_ITEM:#speed stick
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("A broom...?","base","base")
            call her_main("Hm...","normal","base")
            call her_main("What is that silly-looking thing attached to it?","normal","frown")
            call her_main("Is it like a saddle...?","open","suspicious")
            call give_gift(">You give the broom to Hermione...",gift_item)
            call her_main("Thank you for the gift, [genie_name].","open","worried")
            call happy(20)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("A broom...?","base","base")
            call her_main("Hm...","normal","frown")
            call her_main("It's a sex-toy of some sort, isn't it?","angry","angry")
            call her_main("But it is so well crafted...","open","down")
            call give_gift(">You give the broom to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","upset","closed")
            call happy(20)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("A broom...?","angry","down_raised")
            call her_main("Hm...")
            call her_main("What kind of saddle is that...?","disgust","glance")
            call her_main("Well, doesn't matter.","open","closed")
            call her_main("Refusing an expensive gift like that would be rude...")
            call give_gift(">You give the broom to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","upset","closed")
            call happy(30)
        if her_whoring >= 18: # Lv 7+
            call her_main("A broom...","base","down")
            call her_main("Hm...")
            call her_main("That saddle, [genie_name]...","open","baseL",cheeks="blush")
            call her_main("It was designed especially for witches, was it not?","open","squint",cheeks="blush")
            call her_main("I am not sure whether this is inappropriate or clever...","annoyed","annoyed")
            call her_main("But this is a brilliant piece of engineering eitherway...","base","suspicious")
            call give_gift(">You give the broom to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","base","glance")
            call happy(30)
    if gift_item == sexdoll_ITEM:#sex doll
        if her_whoring >= 0 and her_whoring <= 5: # Lv 1-2.
            call her_main("Is this...","shock","wide")
            call her_main("A sex doll?!","angry","worriedCl",emote="05")
            call her_main("[genie_name]!!!","scream","worriedCl")
            call upset(20)
        if her_whoring >= 6 and her_whoring <= 11: # Lv 3-4.
            call her_main("A sex doll?","shock","wide")
            call her_main("This is just so unbecoming for an esteemed wizard such as yourself, [genie_name]...","upset","closed")
            call upset(20)
        if her_whoring >= 12 and her_whoring <= 17: # Lv 5-6.
            call her_main("A sex doll...","angry","down_raised")
            call her_main("This is a little inappropriate...","upset","closed")
            call her_main("But maybe we could use it for a prank or something...","base","down")
            call give_gift(">You give the blow-up doll to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","base","down")
            call happy(10)
        if her_whoring >= 18: # Lv 7+
            call her_main("the Joanne sex doll?","annoyed","down")
            call her_main("I Can't say that I approve of this...","open","baseL",cheeks="blush")
            call her_main("But I know Harry would love to have a go at it...","base","down")
            call give_gift(">You give the blow-up doll to Hermione...",gift_item)
            call her_main("Thank you, [genie_name].","base","baseL",cheeks="blush")
            call happy(30)

    hide screen hermione_main
    with d5
    call her_main(xpos="base",ypos="base",trans="d5")

    return



label give_gift(text = "", gift = ""):
    hide screen hermione_main
    with d3
    $ the_gift = "interface/icons/"+str(gift.image)+".png"
    show screen gift
    with d3
    "[text]"
    hide screen gift
    with d3
    $ gift.number -= 1

    return



label happy(sub_mad = 0):
    hide screen hermione_main
    with d3
    $ her_mood -= sub_mad
    if her_mood < 0:
        $ her_mood = 0
    if her_mood == 0:
        ">Hermione's mood has improved...\n>Hermione is {size=+5}not upset{/size} with you..."
    else:
        ">Hermione's mood has improved...\n>Hermione is {size=+5}still upset{/size} with you..."
    return

label no_change:
    hide screen hermione_main
    with d3
    ">Hermione's mood didn't change much..."
    return

label upset(add_mad):
    hide screen hermione_main
    with d3
    $ her_mood += add_mad
    ">Hermione's mood worsened...\n>Hermione is {size=+5}upset{/size} with you..."
    return
