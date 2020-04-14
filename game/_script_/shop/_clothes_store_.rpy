init python:
    def unlock_clothing_compat(item):
        """Unlock a clothing item. Compatible with new outfit system."""
        if isinstance(item, Item):
            item.unlocked = True
        elif isinstance(item, DollOutfit):
            item.unlock()
        elif isinstance(item, DollCloth):
            item.unlocked = True

        #TODO Find a better solution than outfit linking (probably just convert all clothes to new wardrobe system)
        if isinstance(item, Item) and item.id in outfit_linking:
            var_name = outfit_linking[item.id]
            outfit = globals()[var_name]
            outfit.unlock()

init python:
    # Used for prediction
    def all_clothes_images():
        lists = [
            hermione_outfits_list, hermione_costumes_list, hermione_dresses_list, hermione_clothing_sets_list,
            luna_outfits_list, luna_costumes_list, luna_dresses_list, luna_clothing_sets_list,
            astoria_outfits_list, astoria_costumes_list, astoria_dresses_list, astoria_clothing_sets_list,
            susan_outfits_list, susan_costumes_list, susan_dresses_list, susan_clothing_sets_list,
            cho_outfits_list, cho_costumes_list, cho_dresses_list, cho_clothing_sets_list
        ]
        for i in lists:
            for j in i:
                yield j.get_image()

### CLOTHING STORE ###

screen clothing_store_room():
    tag room_screen

    if daytime:
        add "images/rooms/_bg_/corridor.png" #Need day image.
    else:
        add "images/rooms/_bg_/corridor.png"

    use ui_top_bar

    zorder 0

label open_clothing_store:
    show screen blkfade
    with d3

    call room("clothing_store")

    call play_music("clothing_store")

    hide screen blkfade
    with d3
    pause.2

    $ renpy.block_rollback()

    $ renpy.start_predict(*all_clothes_images())

    call clothing_store_chitchat

    #Reset
    $ store_category = 0
    $ item_choice = None
    $ current_page = 0
    $ character_choice = 1 #Hermione
    $ character_choice_list = [1,2,3,4,5]
    $ store_menu = True #Displays item's gold value.

    show screen clothing_store_menu

    jump clothing_shop_menu

label clothing_store_chitchat:
    if not clothing_store_intro_done:
        $ clothing_store_intro_done = True
        ">You enter to see an old woman busy sewing together two pieces of long dark fabric."
        ">The woman is dressed almost entirely in pink and has a warm, approachable air to her."
        m "Hello."
        maf "Hello, Professor Dumbledore."
        maf "What can I do for you? Would you like a new cloak, or do you require some alterations to an existing item?"
        m "Neither thank you, I'm just here to make a few inquiries."
        maf "Of course sir, what could I help you with?"
        m "Firstly, what type of items do you sell?"
        maf "Well, I'm a tailor. I make uniforms for the staff and students."
        maf "I also perform alterations to existing items. This is mainly when a student goes through a growth spurt or gets a hole in their cloak."
        m "I see. Do you ever make custom orders?"
        maf "Not really, although it is my passion. Most of what I'm asked to make are standard black robes."
        m "So you're interested in making unique outfits?"
        maf "Absolutely, although I would have to order the fabrics in. I don't really have a range of colours at the moment."
        maf "What did you have in mind?"
        m "A few things. I haven't decided on anything specific yet."
        maf "Well, while you're making up your mind, feel free to browse the store."
    else:
        maf "Well, what can I get for you today?"

    return

label close_clothing_store:
    $ renpy.play('sounds/door2.mp3')
    hide screen clothing_store_menu
    hide screen list_menu
    hide screen clothing_menu
    with d3

    $ renpy.stop_predict(*all_clothes_images())

    m "That's all for today, thank you."
    maf "You're welcome, sir. Come back any time."

    $ store_menu = False #Displays item's gold value.

    jump return_office

screen clothing_store_menu():
    tag store_menu
    if store_category == 0:
        $ UI_xpos_offset = 0
    else:
        $ UI_xpos_offset = 100

    zorder 4

    # Close Button
    use close_button

#Clothing Store, Outfits & Sets.
label clothing_shop_menu:
    hide screen list_menu
    show screen clothing_store_menu

    python:
        item_list = []
        if character_choice == 1:
            item_list.extend(hermione_outfits_list)
            item_list.extend(hermione_costumes_list)
            item_list.extend(hermione_dresses_list)
            item_list.extend(hermione_clothing_sets_list)
        if character_choice == 2:
            item_list.extend(luna_outfits_list)
            item_list.extend(luna_costumes_list)
            item_list.extend(luna_dresses_list)
            item_list.extend(luna_clothing_sets_list)
        if character_choice == 3:
            item_list.extend(astoria_outfits_list)
            item_list.extend(astoria_costumes_list)
            item_list.extend(astoria_dresses_list)
            item_list.extend(astoria_clothing_sets_list)
        if character_choice == 4:
            item_list.extend(susan_outfits_list)
            item_list.extend(susan_costumes_list)
            item_list.extend(susan_dresses_list)
            item_list.extend(susan_clothing_sets_list)
        if character_choice == 5:
            item_list.extend(cho_outfits_list)
            item_list.extend(cho_costumes_list)
            item_list.extend(cho_dresses_list)
            item_list.extend(cho_clothing_sets_list)

        item_list = list(filter(lambda x: (x.unlocked==False and x.unlockable==False), item_list))

    show screen clothing_menu(item_list, character_choice, item_choice)
    with d3

    $ _return = ui.interact()

    hide screen clothing_menu

    if isinstance(_return, Item):
        $ item_choice = _return

    elif _return == "buy":
        call purchase_outfit(item_choice)
        $ item_choice = None
        $ current_page = 0
        if clothing_mail_item != None:
            jump close_clothing_store
        else:
            jump clothing_shop_menu

    elif _return == "Close":
        $ current_page = 0
        $ item_choice = None
        jump close_clothing_store

    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    elif _return == "left":
        $ current_page = 0
        $ character_choice += -1
        $ item_choice = None
    elif _return == "right":
        $ current_page = 0
        $ character_choice += 1
        $ item_choice = None

    jump clothing_shop_menu

label purchase_outfit(item):
    hide screen clothing_store_menu
    hide screen list_menu
    hide screen clothing_menu
    with d3

    if clothing_mail_item != None:
        maf "I'm sorry luv, but I'm still quite busy working on your previous order."
        maf "Come back once you received my package."
        return

    if item == hg_maid:
        m "I'd like to order a maid outfit."
        maf "A maid costume, what on earth for? Surely the cleaning elves keep your office tidy."
        m "It's going to be a present."
        maf "For whom?"
        m "I'm afraid I can't say."
        maf "Well as long as it's not for a student..."
        maf "Did you have any style in mind?"
        m "Preferably a french maid."
        maf "..."
        maf "Well I should have it available for pick-up in a few days after I get the materials in."
        m "Thank you."

    elif item == hg_nightie:
        m "I'd like to order another custom outfit today."
        maf "Certainly Sir. These outfits have started to become the highlight of my job. Everything else seems quite conservative by comparison."
        m "Well I can assure you that this outfit is not conservative."
        maf "Hmmm?"
        m "I'd like to order a girls Nightgown."
        maf "Well that doesn't seem overl-"
        m "Made of silk."
        maf "Ahh. I assume that you also want it transparent?"
        m "If it's possible."
        maf "Of course it is possible, who do you take me for?"
        maf "I just have to order in the materials, although silks not cheap."
        m "Don't worry about the cost."
        maf "As you wish Sir, it should be ready in a couple of days."
        m "Thank you."

    elif item == hg_ball:
        if not ball_quest.E4_complete:
            m "Do you sell Dresses?"
            maf "A dress? Are we talking ball dresses, or more burlesque?"
            m "Hmm... Balls actually."
            maf "How surprising."
            m "I was thinking that I could have a custom one made. For a very good girl of mine."
        else:
            m "Do you sell Ball dresses?"
            maf "Hmmm, we do although they're nothing special. Why?"
            m "A 'girl' approached me with a problem. Apparently she's unable to acquire a dress for this years autumn ball."
            maf "How tragic, well I'm sure that one of these cheap ones will suffice."
            m "I was thinking that I could have a custom one made. She is a very good girl."
        maf "I see. Would I be correct in assuming that this girls measurements are the same as the other outfits you've had me make?"
        m "Yes you would."
        maf "Well then I'll make her the best dress this school's ever seen. From what I've heard she's earned it..."
        maf "It should be ready in about a week."
        m "A week? Why so long?"
        maf "A ball dress isn't something that's thrown together. It requires love and attention. It doesn't come cheap either."
        m "Well, thank you."
        maf "You're welcome."

    elif item == hg_msmarv:
        m "Tell me Madam Mafkin, have you ever heard of superheroes?"
        maf "Yes yes, those people in the comic books. My grandson is quite fond of them."
        m "Fantastic, I was wondering if it would be possible for you to make me a costume."
        maf "Certainly, who did you have in mind?"
        m "Do you know Ms Marvel?"
        maf "I'm afraid not..."
        maf "But I'm sure that my grandson has a comic of hers. I'm set to visit him this weekend so I can take a look."
        m "Thank you very much."
        maf "No need to thank me sir. Payment will suffice."

    elif item == hg_hslut:
        m "Have you ever seen a burlesque show Madam?"
        maf "I've done more than that, I've designed a few of the outfits for them!"
        m "Splendid, I was wondering if I could commission one."
        maf "Most Certainly, any particular colour in mind?"
        m "Ideally red."
        maf "As you wish."
        m "Thank you very much."
        maf "You're quite welcome sir."

    # elif item == hg_costume_power_girl_ITEM:
        # m "I was wondering if it would be possible for you to make me a super hero costume."
        # maf "Certainly, who did you have in mind?"
        # m "Do you know Power Girl?"
        # maf "I'm afraid not..."
        # maf "But I'm sure that my grandson has a comic of hers. I'm set to visit him this weekend so I can take a look."
        # m "Thank you very much."
        # maf "No need to thank me sir. Payment will suffice."

    # elif item == hg_costume_harley_quinn_ITEM:
        # m "I was wondering if it would be possible for you to make me a super villain costume."
        # maf "Certainly, who did you have in mind?"
        # m "Do you know Harley Quinn?"
        # maf "I'm afraid not..."
        # maf "But I'm sure that my grandson has a comic of hers. I'll just have to wrestle it out of his grubby little hands."
        # m "Thank you very much."
        # maf "You're quite welcome."

    elif item == hg_croft:
        m "I was wondering if it would be possible for you to make me another costume."
        maf "Certainly, what are you after?"
        m "I don't suppose that you know Lara croft?"
        maf "I'm afraid not..."
        m "She's a video game character..."
        maf "Well my little muggle grandson loves video games. I'm sure he can show me what she looks like."
        m "Thank you very much."
        maf "You're welcome. I'm seeing him tonight so I should be able to complete this one slightly faster than usual."
        m "Fantastic."

    # elif item == hg_outfit_christmas_ITEM:
        # m "I was wondering if it would be possible for you to make me a festive costume."
        # maf "Certainly, what what holiday are you looking to \"celebrate\"?"
        # m "Christmas."
        # maf "At this time of year?"
        # m "It's never to early to start the festivities..."
        # maf "Evidently not. I'll have it done as soon as I can. "
        # m "Thank you very much."
        # maf "You're welcome. I'll even give you a special price. Consider it my Christmas gift to you.."
        # m "Thank you."

    # elif item == hg_outfit_pirate_ITEM:
        # m "I want a pirate outfit"
        # maf "ok"

    elif item == hg_bioshock:
        m "Have you ever heard of bioshock infinite?"
        maf "Biology what now?"
        m "..."
        m "It might be something to ask your grandson about..."
        maf "I assume you want the costume from whatever that is?"
        m "If it's not too much..."
        maf "Consider it done!"
        m "Thank you very much."
        maf "You're welcome."

    elif item == hg_yennefer:
        m "Have you ever heard of the sorceress Yennefer?"
        maf "Of course! The mother of a universe hopper isn't quickly forgotten..."
        m "Think you could make a copy of her outfit?"
        maf "Certainly."
        m "Thank you very much."
        maf "Toss a coin to your tailor."

    # Purchase Outfit

    if gold >= item.cost:

        $ clothing_mail_item = item
        $ clothing_mail_timer = item.wait_time
        $ order_cost = item.cost
        $ order_tip = int(item.cost * 0.20) # int() removes decimental

        menu:
            "-add next day delivery (+[order_tip] gold)-" if gold >= order_cost + order_tip:
                $ order_cost = order_cost + order_tip
                $ clothing_mail_timer = 1
                g9 "I'll tip you handsomely if you can get it done by tomorrow."
                maf "Oh, Professor. I {b}do{/b} love a challenge."
                maf "I should have all the materials laying around somewhere..."
            "{color=[menu_disabled]}-add next day delivery (+[order_tip] gold)-{/color}" if gold < order_cost + order_tip:
                m "(I don't have enough money for that.)"
                pass
            "-no thanks-":
                pass

    else:
        m "I don't have enough gold."
        return

    $ item.unlockable = True #Hides it from the store menu.
    $ gold -= order_cost

    m "Here is your gold."
    maf "Thank you.\nI'll start working on it right away, Professor!"
    if clothing_mail_timer == 1:
        maf "You can expect a package with the outfit by tomorrow."
    else:
        $ _tmp = "You can expect a package with the outfit in about "+num_to_word(clothing_mail_timer)+" days."
        maf "[_tmp]"

    return
