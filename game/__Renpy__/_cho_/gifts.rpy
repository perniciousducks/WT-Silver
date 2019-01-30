

#Tonks Gift Responses

label give_cho_gift(gift_item):
    hide screen cho_chang
    with d5

    #$ gave_cho_gift = True

    if gift_item == lollipop_ITEM:
        call cho_main("Sweets?",pupils="down",face="horny",xpos="mid",ypos="base",trans="d5")
        call cho_main("My team captain hasn't let buy any to keep my blood sugar balanced, whatever that means.",mouth="soft",face="annoyed")
        call give_gift(">You give the sweets to Cho...",gift_item)
        call cho_main("But thanks, [cho_genie_name].",face="neutral")

    if gift_item == chocolate_ITEM:
        call cho_main("Chocolate?",pupils="down",face="horny",xpos="mid",ypos="base",trans="d5")
        call cho_main("I probably shouldn't... although.",pupils="R",face="horny")
        call give_gift(">You give the chocolate to Cho...",gift_item)
        call cho_main("I'll take it, [cho_genie_name]!",face="happy")

    if gift_item == plush_owl_ITEM:
        call cho_main("A toy?",face="annoyed",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the stuffed owl to Cho...",gift_item)
        call cho_main("My team would probably laugh if they saw me with this...",mouth="open",face="annoyed")
        call cho_main("I guess it's cute...",face="annoyed")

    if gift_item == butterbeer_ITEM:
        call cho_main("Butterbeer?",face="disgusted",xpos="mid",ypos="base",trans="d5")
        call cho_main("Isn't this supposed to be very alcoholic?",face="annoyed")
        call give_gift(">You give the Butterbeer to Cho...",gift_item)
        call cho_main("Wait, it says low alcohol content on it... those boys lied to me.",face="angry")
        call cho_main("Thank you, [cho_genie_name].",face="happy")

    if gift_item == science_mag_ITEM:
        call cho_main("Oh, I heard that they put out a new formula for broom polish in this issue.",mouth="open",pupils="R",face="neutral",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give an assortment of educational magazines to Cho...",gift_item)
        call cho_main("Thank you, [cho_genie_name].",face="neutral")

    if gift_item == girls_mag_ITEM:
        call cho_main("Girls magazines?",pupils="down",face="annoyed",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give an assortment of rather girly magazines to Cho...",gift_item)
        call cho_main("I don't usually read these types of magazines, the boys used to make fun of me for it.",face="annoyed")
        call cho_main("But they can't get into the girls dorm.",face="neutral")

    if gift_item == adult_mag_ITEM:
        call cho_main("Adult magazines?",face="disgusted",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give an assortment of adult magazines to Cho...",gift_item)
        call cho_main("These people do have nice, posture...",face="horny")
        call cho_main("I... I guess they could be useful.",face="horny")
        call cho_main("Thank you, [cho_genie_name].",face="neutral")

    if gift_item == porn_mag_ITEM:
        call cho_main("What's this?",face="annoyed",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give an assortment of porn magazines to Cho...",gift_item)
        call cho_main("What's with these positions? Is that a broom handle up her...",mouth="open",eye="wide",brows="raised",pupils="down")
        call cho_main("Oh my-...",mouth="soft",pupils="R",face="disgusted")

    if gift_item == krum_poster_ITEM:
        call cho_main("A Viktor Krum poster?",mouth="scream",eye="wide",brows="raised",pupils="mid",xpos="mid",ypos="base",trans="hpunch")
        call give_gift(">You give the poster to Cho...",gift_item)
        call cho_main("I'll take that if you don't mind.",pupils="downR",face="horny")
        call cho_main("(...)",mouth="soft",pupils="up",face="horny")
        call cho_main("I love it, [cho_genie_name].",pupils="mid",face="horny")

    if gift_item == sexy_lingerie_ITEM:
        call cho_main("Lingerie?",face="annoyed",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the lingerie to Cho...",gift_item)
        call cho_main("Seems pretty flexible. I might be able use these when stretching.",mouth="pout",pupils="down",face="annoyed")

    if gift_item == pink_condoms_ITEM:
        call cho_main("Condoms?",face="annoyed",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give a pack of condoms to Cho...", gift_item)
        call cho_main("I do surround myself with mostly boys, so having these at hand could be useful...",pupils="downR",face="horny")
        call cho_main("Thank you for your concerns, [cho_genie_name]...",mouth="soft",pupils="mid",face="neutral")

    if gift_item == vibrator_ITEM:
        call cho_main("A Vibrator?",face="horny",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the vibrator to Cho...", gift_item)
        call cho_main("Ahh, It does promote a healthy lifestyle...",face="horny")
        call cho_main("Thank you, [cho_genie_name].",face="happy")

    if gift_item == anal_lube_ITEM:
        call cho_main("Anal lube?",face="annoyed",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the jar of anal lube to Cho...", gift_item)
        call cho_main("You should've given me this yesterday, [cho_genie_name].",mouth="soft",face="annoyed")
        call cho_main("I haven't been able to sit on a broom all day after yesterday's game...",mouth="pout",pupils="down",face="annoyed")

    if gift_item == ballgag_and_cuffs_ITEM:
        call cho_main("Ball gag and cuffs?",pupils="down",face="annoyed",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the ball gag and cuffs to Cho...", gift_item)
        call cho_main("How progressive... do they require a safe-word to open?",face="horny")
        call cho_main("Wait, how would a safe-word work when you have a ball in your mouth...",mouth="quiver",eye="wide",brows="raised",pupils="down")

    if gift_item == anal_plugs_ITEM:
        call cho_main("Anal plugs?",face="annoyed",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give a set of anal plugs to Cho...", gift_item)
        call cho_main("But these would stick out under my robes...",face="annoyed")
        call cho_main("Maybe people would just think it's a tail or something...",face="horny")
        call cho_main("Thank you, [cho_genie_name].",face="neutral")

    if gift_item == testral_strapon_ITEM:
        call cho_main("A strap-on?",mouth="open",eye="wide",brows="sad",pupils="down",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the thestral strap-on to Cho...", gift_item)
        call cho_main("How would that even fit in anyone?",mouth="quiver",eye="wide",brows="raised",pupils="down")
        #call cho_main("I do like to keep my girls flexible...",face="neutral")

    if gift_item == broom_2000_ITEM:
        call cho_main("Is that a skittle diddler 2000, with a built-in vibrator and pulse function?",mouth="scream",eye="wide",brows="raised",pupils="down",xpos="mid",ypos="base",trans="hpunch")
        call give_gift(">You give the broom to Cho...", gift_item)
        call cho_main("I mean, it's a nice broom alright...",pupils="downR",face="horny")
        call cho_main("But, to be honest, [cho_genie_name]...",mouth="soft",pupils="down",face="horny")
        call cho_main("I can't wait to try it out!",pupils="mid",face="happy")

    if gift_item == sexdoll_ITEM:
        call cho_main("A sex doll?",face="annoyed",xpos="mid",ypos="base",trans="d5")
        call give_gift(">You give the sex doll to Cho...", gift_item)
        call cho_main("It says Joanne on it...",face="disgusted")
        call cho_main("I leave it in the boys changing room, should be a good reward after a practice.",face="annoyed")


    hide screen cho_chang
    with d5
    call cho_main(xpos="base",ypos="base",trans="d5")

    return
