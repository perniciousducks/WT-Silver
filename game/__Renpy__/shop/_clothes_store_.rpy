init python:
    def unlock_clothing_compat(item):
        """Unlock a clothing item. Compatible with new outfit system."""
        if isinstance(item, item_class):
            item.unlocked = True
        elif isinstance(item, outfit_class) or isinstance(item, cloth_class):
            item.unlock(True)

        if item.id in outfit_linking:
            outfit_linking[item.id].unlock(True)

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
        maf "Absolutely, although I would have to order the fabrics in. I don't really have a range of colors at the moment."
        maf "What did you have in mind?"
        m "A few things. I haven't decided on anything specific yet."
        maf "Well, while your making up your mind, feel free to browse the store."
    else:
        maf "Well, what can I get for you today?"

    return



label close_clothing_store:
    $ renpy.play('sounds/door2.mp3')
    hide screen clothing_store_menu
    hide screen list_menu
    hide screen clothing_menu
    with d3

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
    use top_bar_close_button

    # Outfits Button
    imagebutton:
        xpos 725 +UI_xpos_offset
        ypos 105
        idle "interface/general/"+interface_color+"/button_select.png"
        if store_category != 0:
            hover "interface/general/"+interface_color+"/button_select_hover.png"
            action [SetVariable("store_category",0), Jump("clothing_shop_menu")]
    if store_category == 0:
        text "Outfits" xalign 0.5 yalign 0.5 xpos 767 +UI_xpos_offset ypos 121 size 16
    else:
        text "Outfits" xalign 0.5 yalign 0.5 xpos 767 +UI_xpos_offset ypos 121 size 14

    # Clothing Items Button
    imagebutton:
        xpos 725 +UI_xpos_offset
        ypos 149
        idle "interface/general/"+interface_color+"/button_select.png"
        if store_category != 1:
            hover "interface/general/"+interface_color+"/button_select_hover.png"
            action [SetVariable("store_category",1), Jump("clothing_items_shop_menu")]
    if store_category == 1:
        text "Items" xalign 0.5 yalign 0.5 xpos 767 +UI_xpos_offset ypos 121+44 size 16
    else:
        text "Items" xalign 0.5 yalign 0.5 xpos 767 +UI_xpos_offset ypos 121+44 size 14




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

    $ _return = ui.interact()

    hide screen clothing_menu

    if isinstance(_return, item_class):
        $ item_choice = _return

    elif _return == "buy":
        call purchase_outfit(item_choice)
        $ item_choice = None
        $ current_page = 0
        jump clothing_shop_menu

    elif _return == "Close":
        $ current_page = 0
        jump close_clothing_store

    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    elif _return == "left":
        $ current_page = 0
        $ character_choice += -1
    elif _return == "right":
        $ current_page = 0
        $ character_choice += 1

    jump clothing_shop_menu



#Clothing Items
label clothing_items_shop_menu:
    hide screen clothing_menu
    show screen clothing_store_menu

    python:
        item_list = []
        if toggle1_bool:
            pass
            #item_list.extend()
        if toggle2_bool:
            item_list.extend(accs_list)
        if toggle3_bool:
            item_list.extend(misc_list)
        if toggle4_bool:
            item_list.extend(dye_list)

        item_list = list(filter(lambda x: (x.unlocked==False and x.unlockable==False), item_list))

    show screen list_menu(item_list, "Clothing Items", toggle1="Clothing", toggle2="Accs.", toggle3="Misc.", toggle4="Dyes" )

    $ _return = ui.interact()

    hide screen list_menu

    if isinstance(_return, item_class):
        call purchase_clothing_item(_return)

    elif _return == "Close":
        $ current_page = 0
        jump close_clothing_store

    elif _return == "toggle1":
        $ toggle1_bool = not toggle1_bool
    elif _return == "toggle2":
        $ toggle2_bool = not toggle2_bool
    elif _return == "toggle3":
        $ toggle3_bool = not toggle3_bool
    elif _return == "toggle4":
        $ toggle4_bool = not toggle4_bool

    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    jump clothing_items_shop_menu



label purchase_clothing_item(item):
    hide screen clothing_store_menu
    hide screen list_menu
    hide screen clothing_menu
    with d3

    if gold >= item.cost:
        $ item.unlocked = True #Unlocks item.
        $ gold -= item.cost

        $ the_gift = item.get_image()
        show screen gift
        with d3

        "Item purchased!"

        hide screen gift
        with d3

    else:
        m "I don't have enough gold."

    return



label purchase_outfit(item):
    hide screen clothing_store_menu
    hide screen list_menu
    hide screen clothing_menu
    with d3

    if clothing_mail_timer != 0:
        maf "I'm sorry luv, but I'm still quite busy working on your item."
        maf "Come back once you got my package."
        return

    if gold < item.cost:
        m "I don't have enough gold."
        return

    if item == hg_cheer_g_ITEM:
        m "I'd like to order a cheerleader outfit."
        maf "A cheerleader outfit? Those horribly crass things popular in America?"
        maf "Why on earth would you want to buy that?"
        m "Well I was speaking to Madam Hooch and she was practically begging me to start a Cheer squad for each house."
        maf "Madam Hooch said that?"
        m "Yes, of course I said no but I did agree to a one student trial for Gryffindor."
        maf "Well, that seems fair enough. Did you have any preference as to the design?"
        m "Not really, just make it sporty I suppose."
        maf "Ok, well come and see me in a few days and I will have it for you."
        m "Thank you."

    if item == hg_cheer_s_ITEM:
        m "I'd like to order another cheerleader outfit."
        maf "Another cheerleader outfit? I thought you said that it was only a one person trial?"
        m "It was at first but due to the success of the Gryffindor cheerleader Slytherin demanded one as well."
        maf "Those Slytherins never could stand being second."
        maf "So do you just want the same basic design modified to suit?"
        m "Maybe make this one a little more sporty if you know what I mean."
        maf "Well you can come pick it up in a few days."
        m "Thank you."

    #if item == hg_cheer_r_ITEM:
    #    jump place_outfit_order

    #if item == hg_cheer_h_ITEM:
    #    jump place_outfit_order

    if item == hg_outfit_maid_ITEM:
        m "I'd like to order a maid outfit."
        maf "A maid costume, what on earth for? Surely the cleaning elves keep your office tidy."
        m "It's going to be a present."
        maf "For whom?"
        m "I'm afraid I can't say."
        maf "Well as long as it's not for a student..."
        maf "Did you have any style in mind?"
        m "Prefrerebly a french maid."
        maf "..."
        maf "Well I should have it available for pickup in a few days after I get the materials in."
        m "Thank you."

    if item == hg_nighty_silk_ITEM:
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

    if item == hg_dress_yule_ball_ITEM:
        if not sorry_for_hesterics:
            m "Do you sell Dresses?"
            maf "A dress? Are we talking ball-dresses, or more burlesque?"
            m "Hmm... Balls actually."
            maf "How surprising."
            m "I was thinking that I could have a custom one made. For a very good girl of mine."
        if sorry_for_hesterics:
            m "Do you sell Ball Dresses?"
            maf "Hmmm, we do although they're nothing special. Why?"
            m "A 'girl' approached me with a problem. Apparently she's unable to aquire a dress for this years autumn ball."
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

    if item == hg_costume_ms_marvel_ITEM:
        m "Tell me Madam Mafkin, have you ever heard of super-heroes?"
        maf "Yes yes, those people in the comic books. My grandson is quite fond of them."
        m "Fantastic, I was wondering if it would be possible for you to make me a costume."
        maf "Certainly, who did you have in mind?"
        m "Do you know Ms Marvel?"
        maf "I'm afraid not..."
        maf "But I'm sure that my grandson has a comic of hers. I'm set to visit him this weekend so I can take a look."
        m "Thank you very much."
        maf "No need to thank me sir. Payment will suffice."

    if item == hg_dress_dancer_ITEM:
        m "Have you ever seen a burlesque show Madam?"
        maf "I've done more than that, I've designed a few of the outfits for them!"
        m "Splendid, I was wondering if I could commision one."
        maf "Most Certainly, any particular color in mind?"
        m "Ideally red."
        maf "As you wish."
        m "Thank you very much."
        maf "You're quite welcome sir."

    if item == hg_costume_power_girl_ITEM:
        m "I was wondering if it would be possible for you to make me a super hero costume."
        maf "Certainly, who did you have in mind?"
        m "Do you know Power Girl?"
        maf "I'm afraid not..."
        maf "But I'm sure that my grandson has a comic of hers. I'm set to visit him this weekend so I can take a look."
        m "Thank you very much."
        maf "No need to thank me sir. Payment will suffice."

    if item == hg_costume_harley_quinn_ITEM:
        m "I was wondering if it would be possible for you to make me a super villain costume."
        maf "Certainly, who did you have in mind?"
        m "Do you know Harley Quinn?"
        maf "I'm afraid not..."
        maf "But I'm sure that my grandson has a comic of hers. I'll just have to wrestle it out of his grubby little hands."
        m "Thank you very much."
        maf "You're quite welcome."

    if item == hg_costume_lara_croft_ITEM:
        m "I was wondering if it would be possible for you to make me another costume."
        maf "Certainly, what are you after?"
        m "I don't suppose that you know Lara croft?"
        maf "I'm afraid not..."
        m "She's a video game character..."
        maf "Well my little muggle grandson loves video games. I'm sure he can show me what she looks like."
        m "Thank you very much."
        maf "You're welcome. I'm seeing him tonight so I should be able to complete this one slightly faster than usual."
        m "Fantastic."

    if item == hg_outfit_christmas_ITEM:
        m "I was wondering if it would be possible for you to make me a festive costume."
        maf "Certainly, what what holiday are you looking to \"celebrate\"?"
        m "Christmas."
        maf "At this time of year?"
        m "It's never to early to start the festivities..."
        maf "Evidently not. I'll have it done as soon as I can. "
        m "Thank you very much."
        maf "You're welcome. I'll even give you a special price. Consider it my Christmas gift to you.."
        m "Thank you."

    if item == hg_outfit_pirate_ITEM:
        m "I want a pirate outfit"
        maf "ok"

    if item == hg_costume_elizabeth_ITEM:
        m "Have you ever heard of bioshock infinite?"
        maf "Biology what now?"
        m "..."
        m "It might be something to ask your grandson about..."
        maf "I assume you want the costume from whatever that is?"
        m "If it's not too much..."
        maf "Consider it done!"
        m "Thank you very much."
        maf "You're welcome."

    if item == hg_costume_yennefer_ITEM:
        m "Have you ever heard of the sorceress yennefer?"
        maf "Of course! The mother of a universe hopper isn't quickly forgotten..."
        m "Think you could make a copy of her outfit?"
        maf "Certainly."
        m "Thank you very much."
        maf "You can thank me with coin!"


    # Purchase Outfit
    $ clothing_mail_item = item
    $ clothing_mail_timer = item.wait_time

    $ item.unlockable = True #Hides it from the store menu.
    $ gold -= item.cost

    m "Here is your gold."
    maf "Thank you.\nI'll start working on it right away, Professor!"
    if item.wait_time == 1:
        maf "You can expect a package with the outfit by tomorrow."
    else:
        maf "You can expect a package with the outfit in about [item.wait_time] days."

    return
