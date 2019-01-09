

#Tonks Gift Responses

label give_lun_gift(gift_item):
    hide screen luna_main
    with d5
    call lun_main(xpos="mid",ypos="base",trans="d5")

    if gift_item == lollipop_ITEM:
        lun "A lollipop?"
        call give_gift(">You give the lollipop to Luna...", gift_item)
        lun "My father always believed that you should always have something sugary around in case any baby unicorns come to visit."
        lun "Thank you, [lun_genie_name]."

    if gift_item == chocolate_ITEM:
        lun "Chocolate?"
        call give_gift(">You give the chocolate to Luna...", gift_item)
        lan "Aaah, I heard these helps with dementia... Or was it Dementors?"

    if gift_item == plush_owl_ITEM:
        lun "A plush owl?"
        call give_gift(">You give the owl plushie to Luna...", gift_item)
        lun "I love owls... Always had a few around me growing up, delivering the newspaper my father publishes."

    if gift_item == butterbeer_ITEM:
        lun "Butterbeer?"
        call give_gift(">You give the bottle to Luna...", gift_item)
        lun "How did you know? I didn't wear my cork necklace today."
        lun "Thank you, [lun_genie_name]."

    if gift_item == science_mag_ITEM:
        lun "Magical creatures weekly?"
        call give_gift(">You give an assortment of educational magazines to Luna...", gift_item)
        lun "Thestrals and their link with death..."
        lun "Interesting..."

    if gift_item == girls_mag_ITEM:
        call give_gift(">You give the girls magazine to Luna...",gift_item)
        #Add text

    if gift_item == adult_mag_ITEM:
        call give_gift(">You give the adult magazine to Luna...",gift_item)
        #Add text

    if gift_item == porn_mag_ITEM:
        call give_gift(">You give the porn magazine to Luna...",gift_item)
        #Add text

    if gift_item == krum_poster_ITEM:
        call give_gift(">You give the poster to Luna...",gift_item)
        #Add text

    if gift_item == sexy_lingerie_ITEM:
        call give_gift(">You give the lingerie to Luna...",gift_item)
        #Add text

    if gift_item == pink_condoms_ITEM:
        call give_gift(">You give the condoms to Luna...",gift_item)
        #Add text

    if gift_item == vibrator_ITEM:
        call give_gift(">You give the vibrator to Luna...",gift_item)
        #Add text

    if gift_item == anal_lube_ITEM:
        call give_gift(">You give the anal lube to Luna...",gift_item)
        #Add text

    if gift_item == ballgag_and_cuffs_ITEM:
        call give_gift(">You give the handcuffs to Luna...",gift_item)
        #Add text

    if gift_item == anal_plugs_ITEM:
        call give_gift(">You give the anal plugs to Luna...",gift_item)
        #Add text

    if gift_item == testral_strapon_ITEM:
        call give_gift(">You give the strap-on to Luna...",gift_item)
        #Add text

    if gift_item == broom_2000_ITEM:
        call give_gift(">You give the broom to Luna...",gift_item)
        #Add text

    if gift_item == sexdoll_ITEM:
        call give_gift(">You give the doll to Luna...",gift_item)
        #Add text


    hide screen luna_main
    with d5
    call lun_main(xpos="base",ypos="base",trans="d5")

    return
