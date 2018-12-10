

label __init_variables:
    #Guide
    if not hasattr(renpy.store,'guide_active'): #important!
        $ guide_active = False
    if not hasattr(renpy.store,'guide_page'): #important!
        $ guide_page = 0
    if not hasattr(renpy.store,'guide_show_hint'): #important!
        $ guide_show_hint = False
    if not hasattr(renpy.store,'guide_show_next_step'): #important!
        $ guide_show_next_step = False
    if not hasattr(renpy.store,'guide_add_tip'): #important!
        $ guide_add_tip = False


    if not hasattr(renpy.store,'current_side_quests'): #important!
        $ current_side_quests = []

    #Tips and Facts
    if not hasattr(renpy.store,'daily_rndm_tip_or_fact'): #important!
        $ daily_rndm_tip_or_fact = 0
    if not hasattr(renpy.store,'guide_tip_text'): #important!
        $ guide_tip_text = ""

    return








#Start: There is a star icon at the top left corner of the screen. This is will open the player guide.
#It will help you progress through the game, give you helpful tips, or even tell you what to do next entirely.

#28.gifts.rpy
#candy:          lvl 1-7= +5
#chocolate:      lvl 1-7= +10
#plush owl:      lvl 1-2= +7,  3-4= +10, 5-6= +15, 7+= +4
#butterbeer:     lvl 1-2= +3,  3-4= +10, 5-6= +15, 7+= 20
#edu-mags:       lvl 1-2= +15, 3-4= +10, 5-6= +3,  7+= +0
#girl-mags:      lvl 1-2= +0,  3-4= +5,  5-6= +15, 7+= +15
#adult-mags:     lvl 1-2= -7,  3-4= -3,  5-6= +8,  7+= +15
#porn-mags:      lvl 1-2= -15, 3-4= -8,  5-6= +0,  7+= +15
#krum poster:    lvl 1-2= +0,  3-4= +4,  5-6= +15, 7+= +25
#lingerie:       lvl 1-2= -10, 3-4= +0,  5-6= +7,  7+= +15
#condoms:        lvl 1-2= -6,  3-4= +0,  5-6= +3,  7+= +4
#vibrator:       lvl 1-2= -10, 3-4= -10, 5-6= +0,  7+= +10
#anal lube:      lvl 1-2= -6,  3-4= -2,  5-6= +0,  7+= +5
#gag and cuffs:  lvl 1-2= -10, 3-4= -5,  5-6= +9,  7+= +15
#anal plugs:     lvl 1-2= +8,  3-4= -15, 5-6= +0,  7+= +10
#strap on:       lvl 1-2= +20, 3-4= -15, 5-6= +10, 7+= +30
#speed stick:    lvl 1-2= +20, 3-4= +20, 5-6= +30, 7+= +30
#sex doll:       lvl 1-2= -20, 3-4= -20, 5-6= +10, 7+= +30
#ADD:            lvl 1-2= ,  3-4= ,  5-6= ,  7+=

### Run label every time before guide gets opened. ###
### Tip of the day ###

label update_tip_of_the_day:

    #Reset Text
    $ guide_tip_text = ""

    #Gift Items Tip
    if her_mood > 0: #Picks this first when she is mad.

        #Always relevant
        $ rndm_one_of_ten = renpy.random.randint(1, 10)

        if rndm_one_of_ten ==  1: #Broom
            $ guide_add_tip = True
            $ guide_tip_text = "A new broom is always a great gift!\nBuy one at the shop for the cheap price of\nonly 500g!\nGet it now! Get it! GET IT!"
        if rndm_one_of_ten ==  2: #Condoms, Anal Lube
            $ guide_add_tip = False #False=Fact                             #Max Characters
            $ guide_tip_text = "Condoms might not be the best gift for a\nyoung girl...\nNeither is anal lube!"
        if rndm_one_of_ten ==  3: #Butterbeer
            $ guide_add_tip = True                                          #Max Characters
            $ guide_tip_text = "Seems like Hermione is mad at you!\nGift her some butterbeer!\nEverybody loves butterbeer!"
        if rndm_one_of_ten ==  4: #Candy
            $ guide_add_tip = True                                          #Max Characters
            $ guide_tip_text = "Seems like Hermione is mad at you!\nGive her a lollipop to better her mood!\nYou can also watch her lick it!"
        if rndm_one_of_ten ==  5: #Chocolate
            $ guide_add_tip = True                                          #Max Characters
            $ guide_tip_text = "Seems like Hermione is mad at you!\nWhy not give her some chocolate to better\nbetter her mood!"

        #her_whoring specific gifts
        if rndm_one_of_ten >= 6 and rndm_one_of_ten <= 10:
            if her_whoring >= 0 and her_whoring <= 5:  #lvl 1-2
                $ rndm_one_of_three = renpy.random.randint(1, 3)
                if rndm_one_of_three == 1:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "Why not buy her a strap-on?\nWhat could possibly go wrong!"
                elif rndm_one_of_three == 2:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "Hermione seems to be quite fond of\neducational magazines!\nNo not sexual-education...\nYes the boring looking ones!"
                elif rndm_one_of_three == 3:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "Seems like Hermione is mad at you!\nMaybe she'd like a gift?\nJust... don't buy her a sex-doll!"

            if her_whoring >= 6 and her_whoring <= 11: #lvl 3-4
                $ rndm_one_of_three = renpy.random.randint(1, 3)
                if rndm_one_of_three == 1:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "A girl like Hermione might be into plush animals!"
                elif rndm_one_of_three == 2:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "Have you heard of Viktor Krum?\nAll the witches love him!\nMaybe Hermione would like a poster of him!"
                elif rndm_one_of_three == 3:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "She still prefers her educational magazines, but maybe you can get her interested in the ones specific for girls!"

            if her_whoring >= 12 and her_whoring <= 17: #lvl 5-6
                $ rndm_one_of_three = renpy.random.randint(1, 3)
                if rndm_one_of_three == 1:
                    $ guide_add_tip = True
                    $ guide_tip_text = "Apparently they released a new set of new and exclusive plush owls!\nGotta catch 'em all!"
                elif rndm_one_of_three == 2:
                    $ guide_add_tip = True
                    $ guide_tip_text = "She really seems to like this Krum guy!\nMaybe you should buy her a poster of him!"
                elif rndm_one_of_three == 3:
                    $ guide_add_tip = True
                    $ guide_tip_text = "One might think Hermione has grown interested in sex-toys by now..."

            if her_whoring >= 18 and her_whoring <= 23: #7
                $ rndm_one_of_three = renpy.random.randint(1, 3)
                if rndm_one_of_three == 1:
                    $ guide_add_tip = False #False=Fact
                    $ guide_tip_text = "Educational Magazines? Fuck that shit!\nWho needs those!"
                elif rndm_one_of_three == 2:
                    $ guide_add_tip = True
                    $ guide_tip_text = "I have heard there is a new Krum poster in the store!\nHermione will kiss your feet if you buy it for her!"
                elif rndm_one_of_three == 3:
                    $ guide_add_tip = True
                    $ guide_tip_text = "She is really into sex stuff now.\nYou really did your job well!\nStill you kind of fucked up and she's mad at you!\nMaybe buy her something!"



    else:



        ## Funny Tips ##
        if daily_rndm_tip_or_fact ==  0:                                     #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Never tickle a sleeping dragon."

        if daily_rndm_tip_or_fact ==  1:                                     #Max Characters
            $ guide_add_tip = False #False=Fact
            $ guide_tip_text = "Book 3 will always be the best one!"

        if daily_rndm_tip_or_fact ==  2:                                     #Max Characters
            $ guide_add_tip = False #False=Fact
            $ guide_tip_text = "Don't worry headmaster, Snape is not going to kill you.\nDifferent timeline!"

        if daily_rndm_tip_or_fact ==  3:                                     #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Don't walk into the forbidden forest alone!\nThere are creatures that live there, of the likes you have never seen before.\nThey call them cars!"

        if daily_rndm_tip_or_fact ==  4:                                     #Max Characters
            $ guide_add_tip = False #False=Fact
            $ guide_tip_text = "Flying-carpets were the preferred way for a wizard to travel. Now it's brooms.\nWhat real wizard wants to sit on a broom?\nAt least carpets don't hurt you crotch!"

        if daily_rndm_tip_or_fact ==  5:                                     #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "The small star icon on the top left of your screen opens the player guide!...\nOh you already knew that?\nWell never mind then!"

        if daily_rndm_tip_or_fact ==  6:                                     #Max Characters
            $ guide_add_tip = False
            $ guide_tip_text = "It's not a good idea to use an unforgivable curse!\nWhile the Imperius Curse might have had some usefulness to you, you will sadly have to corrupt Hermione the old way!"

        if daily_rndm_tip_or_fact ==  7:                                     #Max Characters
            $ guide_add_tip = False
            $ guide_tip_text = "We have noticed you are running an Ad-Blocker!\nPlease disable your Ad-Blocker to support this Quest-Guide! Thank You."

        if daily_rndm_tip_or_fact ==  8:                                     #Max Characters
            $ guide_add_tip = False
            $ guide_tip_text = "Dumbledore is gay apparently.\nNot that I mind that, I'm just running out of useful facts to tell."

        if daily_rndm_tip_or_fact ==  9:                                     #Max Characters
            $ guide_add_tip = False
            $ guide_tip_text = "Support us on Patreon!"

        if daily_rndm_tip_or_fact ==  10:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Do. Or do not.\nThere is no try!"


        ## Helpful Tips ##
        if daily_rndm_tip_or_fact ==  11:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Rainy or cloudy day?\nRead a book!\nThe moody weather will help you focus, and be more productive!"
        if daily_rndm_tip_or_fact ==  12:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Rainy or cloudy day?\nBest weather to write some reports!\nThe moody weather will help you focus, and be more productive!"
        if daily_rndm_tip_or_fact ==  13:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Turn on the fireplace during the rain!\nThe warming comfort of a fire-lit room makes reading faster and writing more enjoyable!"
        if daily_rndm_tip_or_fact ==  14:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Drinking wine with Snape not only lengthens your strong friendship with him, he'll also be more willing to reward Slytherin with a higher number of house-points!"
        if daily_rndm_tip_or_fact ==  15:                                    #Max Characters
            $ guide_tip_text = "Keep rummaging through your cupboard.\nYou'll never know what useful things you can find until you try!"
        if daily_rndm_tip_or_fact ==  16:                                    #Max Characters
            $ guide_add_tip = False #False=Fact
            $ guide_tip_text = "Dumbledore had quite a selection of wine.\nHe might have some wine left in his cupboard!"

        if daily_rndm_tip_or_fact ==  17:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "If Hermione is mad at you it might take -days- for her to like you again!\nBest to just buy her a gift!"

        if daily_rndm_tip_or_fact ==  18:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "If Hermione is mad you, you can give her gifts to better her mood!\nDependant on her Whoring level she will prefer some gifts over others!"



    return
