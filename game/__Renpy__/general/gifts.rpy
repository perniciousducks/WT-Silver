init python:
    
    class silver_item(object):
        cost = 0
        name = ""
        image = ""
        description = ""
    
    class gift_item(silver_item):
        id = 0
        whoringNeeded = 0
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def costOf(self, number_of_item):
            return self.cost * number_of_item
    
label __init_variables:
    
    
    # $ gift_list = []
    
    # gift_list.append(cost=20, name="Lollipop candy", users=["hermione"],
        # description="A lollipop candy. An adult candy for kids or kids candy for adults?")
    
    # gift_list.append(cost=40, name="Chocolate",
        # description="The recipe for this delicious milk chocolate is kept a secret. (Rumoured to contain dried faeries).")
    
    # gift_list.append(cost=35, name="Plush owl",
        # description="a Toy owl stuffed with feathers of an actual owl. It's so cuddly!")
    
    # gift_list.append(cost=50, name="Butterbeer", whoringNeeded=3,
        # description="Girls can't resist this beverage's buttery texture. Therefore it's always in high demand among the boys. \n{size=-4}Warning: no underage drinking is allowed without adults present.{/size}")
    
    # gift_list.append(cost=30, name="Educational magazines",
        # description="Educational magazines. \nthe Trusty companions of every social outcast.")
    
    # gift_list.append(cost=45, name="Girly magazines",
        # description="Girly magazines. \nAll cool girls are reading these.")
    
    # gift_list.append(cost=60, name="Adult magazines",
        # description="Your boyfriend is turning into a nice guy? \nYour husband won't abuse you anymore? \nAll you wanted to know about relationships, love and sex. Mostly about sex.")
    
    # gift_list.append(cost=80, name="Porn magazines", whoringNeeded=3,
        # description="Give these to your girlfriend to test her, to your wife to shame her and to your daughter to avoid \"the talk\".")
    
    # gift_list.append(cost=25, name="Viktor Krum Poster",
        # description="A skilled Quidditch Seeker, Viktor has been selected to play for the Bulgarian National Quidditch team despite still going to school, and is widely regarded as one of the best players in the world.")
    
    # gift_list.append(cost=75, name="Sexy lingerie",
        # description="Sexy lingerie \"Fairy Godmother\". Charm your wizard in bed or empress your sisters at a Sabbath.")
    
    # gift_list.append(cost=50, name="A pack of condoms", whoringNeeded=3,
        # description="\"Pink unicorn condoms\". \nUnleash the one-horned beast!\n{size=-4}May contain traces of actual unicorn saliva.{/size}")
    
    # gift_list.append(cost=55, name="Vibrator", whoringNeeded=3,
        # description="A magnificent, magically enhanced vibrator made of vine wood, with a dragon heartstring core.")
    
    # gift_list.append(cost=60, name="Jar of anal lubricant",
        # description="A Jar of anal lube, Buy this for your loved one - show that you care.")
    
    # gift_list.append(cost=70, name="Ball gag and cuffs",
        # description="Ball gag and cuffs, Turn your soulmate into your cellmate.")

    # gift_list.append(cost=85, name="Anal plugs", whoringNeeded=3,
        # description="Anal plugs decorated with actual tails. \nSizes vary to satisfy expert practitioners and beginner alike.")

    # gift_list.append(cost=200, name="Thestral Strap-on", whoringNeeded=3,
        # description="Thestral strap-on.\nWhen you see it, you'll shit bricks.")

    # gift_list.append(cost=500, name="Lady Speed Stick-2000",
        # description="The \"Lady Speed Stick-2000\", an elegant way of transportation for passionate witches. The trademarked saddle guarantees full satisfaction. Get one for your witch and she won't use her boring old broom ever again!")

    # gift_list.append(cost=350, name="Sex doll \"Joanne\"",
        # description="Sex doll \"Joanne\"... It's so realistic. Almost looks like a real human under the influence of a spell of some sort.")

    # gift_list.append(cost=65, name="Anal beads",image="images/store/gift_anal_beads.png",
        # description="Anal beads engraved with a strange inscription \"Property of L.C.\".")
    
    
    if not hasattr(renpy.store,'Lollipop'): #important!
        $ Lollipop = gift_item()
    $ Lollipop.id = 0
    $ Lollipop.cost = 20
    $ Lollipop.name = "lollipop candy"
    $ Lollipop.image = "images/store/gifts/1.png"
    $ Lollipop.description = "A lollipop candy. An adult candy for kids or kids candy for adults?"
    
    
    if not hasattr(renpy.store,'Chocolate'): #important!
        $ Chocolate = gift_item()
    $ Chocolate.id = 1
    $ Chocolate.cost = 40
    $ Chocolate.name = "Chocolate"
    $ Chocolate.image = "images/store/gifts/2.png"
    $ Chocolate.description = "The recipe for this delicious milk chocolate is kept a secret. (Rumoured to contain dried faeries)."
    
    if not hasattr(renpy.store,'PlushOwl'): #important!
        $ PlushOwl = gift_item()
    $ PlushOwl.id = 2
    $ PlushOwl.cost = 35
    $ PlushOwl.name = "Plush owl"
    $ PlushOwl.image = "images/store/gifts/3.png"
    $ PlushOwl.description = "a Toy owl stuffed with feathers of an actual owl. It's so cuddly!"
    
    if not hasattr(renpy.store,'Butterbeer'): #important!
        $ Butterbeer = gift_item()
    $ Butterbeer.id = 3
    $ Butterbeer.cost = 50
    $ Butterbeer.whoringNeeded = 3
    $ Butterbeer.name = "Butterbeer"
    $ Butterbeer.image = "images/store/gifts/4.png"
    $ Butterbeer.description = "Girls can't resist this beverage's buttery texture. Therefore it's always in high demand among the boys. \n{size=-4}Warning: no underage drinking is allowed without adults present.{/size}"
    
    if not hasattr(renpy.store,'EducationalMagazines'): #important!
        $ EducationalMagazines = gift_item()
    $ EducationalMagazines.id = 4
    $ EducationalMagazines.cost = 30
    $ EducationalMagazines.name = "Educational magazines"
    $ EducationalMagazines.image = "images/store/gifts/5.png"
    $ EducationalMagazines.description = "Educational magazines. \nthe Trusty companions of every social outcast."
    
    if not hasattr(renpy.store,'GirlyMagazines'): #important!
        $ GirlyMagazines = gift_item()
    $ GirlyMagazines.id = 5
    $ GirlyMagazines.cost = 45
    $ GirlyMagazines.name = "Girly magazines"
    $ GirlyMagazines.image = "images/store/gifts/6.png"
    $ GirlyMagazines.description = "Girly magazines. \nAll cool girls are reading these."
    
    if not hasattr(renpy.store,'AdultMagazines'): #important!
        $ AdultMagazines = gift_item()
    $ AdultMagazines.id = 6
    $ AdultMagazines.cost = 60
    $ AdultMagazines.name = "Adult magazines"
    $ AdultMagazines.image = "images/store/gifts/7.png"
    $ AdultMagazines.description = "Your boyfriend is turning into a nice guy? \nYour husband won't abuse you anymore? \nAll you wanted to know about relationships, love and sex. Mostly about sex."
    
    if not hasattr(renpy.store,'PornMagazines'): #important!
        $ PornMagazines = gift_item()
    $ PornMagazines.id = 7
    $ PornMagazines.cost = 80
    $ PornMagazines.whoringNeeded = 3
    $ PornMagazines.name = "Porn magazines"
    $ PornMagazines.image = "images/store/gifts/8.png"
    $ PornMagazines.description = "Give these to your girlfriend to test her, to your wife to shame her and to your daughter to avoid \"the talk\"."
    
    if not hasattr(renpy.store,'ViktorKrumPoster'): #important!
        $ ViktorKrumPoster = gift_item()
    $ ViktorKrumPoster.id = 8
    $ ViktorKrumPoster.cost = 25 #placeholder number
    $ ViktorKrumPoster.name = "Viktor Krum Poster"
    $ ViktorKrumPoster.image = "images/store/gifts/9.png"
    $ ViktorKrumPoster.description = "A skilled Quidditch Seeker, Viktor has been selected to play for the Bulgarian National Quidditch team despite still going to school, and is widely regarded as one of the best players in the world."
    
    if not hasattr(renpy.store,'SexyLingerie'): #important!
        $ SexyLingerie = gift_item()
    $ SexyLingerie.id = 9
    $ SexyLingerie.cost = 75 #placeholder number
    $ SexyLingerie.name = "Sexy lingerie"
    $ SexyLingerie.image = "images/store/gifts/10.png"
    $ SexyLingerie.description = "Sexy lingerie \"Fairy Godmother\". Charm your wizard in bed or empress your sisters at a Sabbath."
    
    if not hasattr(renpy.store,'PackOfCondoms'): #important!
        $ PackOfCondoms = gift_item()
    $ PackOfCondoms.id = 10
    $ PackOfCondoms.cost = 50
    $ PackOfCondoms.whoringNeeded = 3
    $ PackOfCondoms.name = "A pack of condoms"
    $ PackOfCondoms.image = "images/store/gifts/11.png"
    $ PackOfCondoms.description = "\"Pink unicorn condoms\". \nUnleash the one-horned beast!\n{size=-4}May contain traces of actual unicorn saliva.{/size}"
    
    if not hasattr(renpy.store,'Vibrator'): #important!
        $ Vibrator = gift_item()
    $ Vibrator.id = 11
    $ Vibrator.cost = 55
    $ Vibrator.whoringNeeded = 3
    $ Vibrator.name = "Vibrator"
    $ Vibrator.image = "images/store/gifts/12.png"
    $ Vibrator.description = "A magnificent, magically enhanced vibrator made of vine wood, with a dragon heartstring core."
    
    if not hasattr(renpy.store,'JarOfLube'): #important!
        $ JarOfLube = gift_item()
    $ JarOfLube.id = 12
    $ JarOfLube.cost = 60
    $ JarOfLube.name = "Jar of anal lubricant"
    $ JarOfLube.image = "images/store/gifts/13.png"
    $ JarOfLube.description = "A Jar of anal lube, Buy this for your loved one - show that you care."
    
    if not hasattr(renpy.store,'BallGagAndCuffs'): #important!
        $ BallGagAndCuffs = gift_item()
    $ BallGagAndCuffs.id = 13
    $ BallGagAndCuffs.cost = 70
    $ BallGagAndCuffs.name = "Ball gag and cuffs"
    $ BallGagAndCuffs.image = "images/store/gifts/14.png"
    $ BallGagAndCuffs.description = "Ball gag and cuffs, Turn your soulmate into your cellmate."
    
    if not hasattr(renpy.store,'AnalPlugs'): #important!
        $ AnalPlugs = gift_item()
    $ AnalPlugs.id = 14
    $ AnalPlugs.cost = 85
    $ AnalPlugs.whoringNeeded = 3
    $ AnalPlugs.name = "Anal plugs"
    $ AnalPlugs.image = "images/store/gifts/15.png"
    $ AnalPlugs.description = "Anal plugs decorated with actual tails. \nSizes vary to satisfy expert practitioners and beginner alike."
    
    if not hasattr(renpy.store,'ThestralStrapon'): #important!
        $ ThestralStrapon = gift_item()
    $ ThestralStrapon.id = 15
    $ ThestralStrapon.cost = 200
    $ ThestralStrapon.whoringNeeded = 3
    $ ThestralStrapon.name = "Thestral Strap-on"
    $ ThestralStrapon.image = "images/store/gifts/16.png"
    $ ThestralStrapon.description = "Thestral strap-on.\nWhen you see it, you'll shit bricks."
    
    if not hasattr(renpy.store,'SpeedStick2000'): #important!
        $ SpeedStick2000 = gift_item()
    $ SpeedStick2000.id = 16
    $ SpeedStick2000.cost = 500
    $ SpeedStick2000.name = "Lady Speed Stick-2000"
    $ SpeedStick2000.image = "images/store/gifts/17.png"
    $ SpeedStick2000.description = "The \"Lady Speed Stick-2000\", an elegant way of transportation for passionate witches. The trademarked saddle guarantees full satisfaction. Get one for your witch and she won't use her boring old broom ever again!"
    
    if not hasattr(renpy.store,'SexDollJoanne'): #important!
        $ SexDollJoanne = gift_item()
    $ SexDollJoanne.id = 17
    $ SexDollJoanne.cost = 350
    $ SexDollJoanne.name = "Sex doll \"Joanne\""
    $ SexDollJoanne.image = "images/store/gifts/18.png"
    $ SexDollJoanne.description = "Sex doll \"Joanne\"... It's so realistic. Almost looks like a real human under the influence of a spell of some sort."
    
    if not hasattr(renpy.store,'AnalBeads'): #important!
        $ AnalBeads = gift_item()
    $ AnalBeads.id = 18
    $ AnalBeads.cost = 65 #placeholder number
    $ AnalBeads.name = "Anal beads"
    $ AnalBeads.image = "images/store/gift_anal_beads.png"
    $ AnalBeads.description = "Anal beads engraved with a strange inscription \"Property of L.C.\"."
    
    
    $ gift_list = []
    $ gift_list.append(Lollipop)
    $ gift_list.append(Chocolate)
    $ gift_list.append(PlushOwl)
    $ gift_list.append(Butterbeer)
    $ gift_list.append(EducationalMagazines)
    $ gift_list.append(GirlyMagazines)
    $ gift_list.append(AdultMagazines)
    $ gift_list.append(PornMagazines)
    $ gift_list.append(ViktorKrumPoster)
    $ gift_list.append(SexyLingerie)
    $ gift_list.append(PackOfCondoms)
    $ gift_list.append(Vibrator)
    $ gift_list.append(JarOfLube)
    $ gift_list.append(BallGagAndCuffs)
    $ gift_list.append(AnalPlugs)
    $ gift_list.append(ThestralStrapon)
    $ gift_list.append(SpeedStick2000)
    #$ gift_list.append(SexDollJoanne)
    #$ gift_list.append(AnalBeads)
    
    return

label happy(sub_mad = 0):
    hide screen hermione_main
    with d3
    $ mad -= sub_mad
    if mad <= 0:
        $ mad = 0
    if mad == 0:
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
    $ mad += add_mad
    ">Hermione's mood worsened...\n>Hermione is {size=+5}upset{/size} with you..."
    return
    
label her_gift_menu:
    python:
        choices = []
        for i in gift_list:
            if gift_item_inv[i.id] > 0:
                choices.append( ( ("-"+str(i.name)+"- ("+str(gift_item_inv[i.id])+")"), i) )
        
        choices.append(("-Never mind-", "nvm"))
        result = renpy.display_menu(choices)
        
    if result == "nvm":
        jump day_time_requests
    else:
        call give_her_gift(result) from _call_give_her_gift_1
    
label give_her_gift(gift_id):
    hide screen hermione_main
    with d5
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    
    if gift_id == 0:#candy
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A lollipop?","base","base") from _call_her_main_3640
            call give_gift(">You give the candy to Hermione...",gift_id) from _call_give_gift
            call her_main("Thank you, [genie_name].","base","base") from _call_her_main_3641
            call happy(5) from _call_happy
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Candy?","normal","base") from _call_her_main_3642
            call her_main("Candy is for kids, [genie_name].","open","base") from _call_her_main_3643
            call give_gift(">You give the candy to Hermione...",gift_id) from _call_give_gift_1
            call her_main("Thank you...","annoyed","worriedL") from _call_her_main_3644
            call happy(5) from _call_happy_1
            $ h_body = "body_06"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Candy?","normal","base") from _call_her_main_3645
            call give_gift(">You give the candy to Hermione...",gift_id) from _call_give_gift_2
            call her_main("Ehm... Sure, thanks...","open","suspicious") from _call_her_main_3646
            call happy(5) from _call_happy_2
            $ h_body = "body_06"
        if whoring >= 18: # Lv 7+  
            call her_main("A lollipop?","base","base") from _call_her_main_3647
            call her_main("Clever girls use candy like this as a \"weapon\".","smile","baseL") from _call_her_main_3648
            call give_gift(">You give the candy to Hermione...",gift_id) from _call_give_gift_3
            call her_main("Thank you, [genie_name].","base","happyCl") from _call_her_main_3649
            call happy(5) from _call_happy_3
            $ h_body = "body_128"
    if gift_id == 1:#chocolate
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A chocolate bar?","base","base") from _call_her_main_3650
            call give_gift(">You give the chocolate to Hermione...", gift_id) from _call_give_gift_4
            call her_main("Thank you, [genie_name].","base","base") from _call_her_main_3651
            call happy(10) from _call_happy_4
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("A chocolate bar?","normal","base") from _call_her_main_3652
            call her_main("Hm...","annoyed","frown") from _call_her_main_3653
            call her_main("That thing about fairies...") from _call_her_main_3654
            call her_main("That is a joke of some sort, right?","open","worried") from _call_her_main_3655
            call give_gift(">You give the chocolate to Hermione...", gift_id) from _call_give_gift_5
            call her_main("Thank you...","soft","base") from _call_her_main_3656
            call happy(10) from _call_happy_5
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A chocolate bar?","normal","base") from _call_her_main_3657
            call her_main("I just like the way it crunches, [genie_name]! N-not the taste...","grin","worriedCl",emote="05") from _call_her_main_3658
            call give_gift(">You give the chocolate to Hermione...", gift_id) from _call_give_gift_6
            call her_main("Ehm... Sure, thanks...","base","base") from _call_her_main_3659
            call happy(10) from _call_happy_6
        if whoring >= 18: # Lv 7+  
            call her_main("A chocolate bar?","base","base") from _call_her_main_3660
            call her_main("You spoil me, [genie_name].","smile","angry") from _call_her_main_3661
            call give_gift(">You give the chocolate to Hermione...", gift_id) from _call_give_gift_7
            call her_main("Thank you.","base","suspicious") from _call_her_main_3662
            call happy(10) from _call_happy_7
    if gift_id == 2:#plush owl
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A stuffed owl?","base","base") from _call_her_main_3663
            call her_main("It's cute...","base","base") from _call_her_main_3664
            call give_gift(">You give the owl to Hermione...",gift_id) from _call_give_gift_8
            call her_main("Thank you, [genie_name].","base","base") from _call_her_main_3665
            call happy(7) from _call_happy_8
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("A plush toy?","open","worried") from _call_her_main_3666
            call her_main("I like it!","base","base") from _call_her_main_3667
            call give_gift(">You give the owl to Hermione...",gift_id) from _call_give_gift_9
            call her_main("Thank you, [genie_name].","base","base") from _call_her_main_3668
            call happy(10) from _call_happy_9
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A toy?","base","base") from _call_her_main_3669
            call her_main("Toys are for kids, [genie_name].","open","base") from _call_her_main_3670
            call her_main("But I'll take it...","annoyed","worriedL") from _call_her_main_3671
            call give_gift(">You give the owl to Hermione...",gift_id) from _call_give_gift_10
            call her_main("Thank you, [genie_name].","base","base") from _call_her_main_3672
            call happy(15) from _call_happy_10
        if whoring >= 18: # Lv 7+  
            call her_main("This is one of those adult toys isn't it?","disgust","glance") from _call_her_main_3673
            call her_main("There's got to be a switch or a button somewhere...","open","down") from _call_her_main_3674
            call her_main("So... Does it vibrate or something?","base","down") from _call_her_main_3675
            call her_main("Oh...?","open","squint",cheeks="blush") from _call_her_main_3676
            call her_main("So it is really just a plush toy then?") from _call_her_main_3677
            call her_main("Shame...","angry","down_raised") from _call_her_main_3678
            call her_main("I mean, thank you, [genie_name].","angry","worriedCl",emote="05") from _call_her_main_3679
            call give_gift(">You give the owl to Hermione...",gift_id) from _call_give_gift_11
            $ h_body = "body_01"
            call happy(4) from _call_happy_11
    if gift_id == 3:#butterbeer
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Butterbeer?","base","base") from _call_her_main_3680
            call her_main("Are you sure about that, [genie_name]?","open","suspicious") from _call_her_main_3681
            call her_main("It does contain alcohol, you know...","base","base") from _call_her_main_3682
            call give_gift(">You give the bottle to Hermione...",gift_id) from _call_give_gift_12
            call her_main("Thank you.","base","base") from _call_her_main_3683
            call happy(3) from _call_happy_12
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Butterbeer, [genie_name]?","open","worried") from _call_her_main_3684
            call her_main("To let you in on a little secret, [genie_name]...","open","base") from _call_her_main_3685
            call her_main("I'm a big fan of this completely harmless beverage.","base","base") from _call_her_main_3686
            call give_gift(">You give the bottle to Hermione...",gift_id) from _call_give_gift_13
            call her_main("Thank you, [genie_name].","base","base") from _call_her_main_3687
            call happy(10) from _call_happy_13
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Butterbeer?","base","base") from _call_her_main_3688
            call her_main("Thank you, [genie_name].","grin","worriedCl",emote="05") from _call_her_main_3689
            call give_gift(">You give the bottle to Hermione...",gift_id) from _call_give_gift_14
            call her_main("I shall drink this with the girls later.","base","base") from _call_her_main_3690
            call happy(15) from _call_happy_14
        if whoring >= 18: # Lv 7+  
            call her_main("Butterbeer...?","base","base") from _call_her_main_3691
            call her_main("Thank you, [genie_name].","base","base") from _call_her_main_3692
            call give_gift(">You give the bottle to Hermione...",gift_id) from _call_give_gift_15
            call her_main("I shall drink this later with the boys.","base","base") from _call_her_main_3693
            call her_main("Err... I meant to say with the girls, of course.","open","baseL",cheeks="blush") from _call_her_main_3694
            call happy(20) from _call_happy_15
            $ h_body = "body_01"
    if gift_id == 4:#edu mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("\"Popular magic\" magazines?","base","base") from _call_her_main_3695
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_id) from _call_give_gift_16
            call her_main("Thank you, [genie_name]!","base","base") from _call_her_main_3696
            call her_main("I will use them for my research!") from _call_her_main_3697
            call happy(15) from _call_happy_16
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Sometimes I find information in magazines that I could never find in a book...","base","base") from _call_her_main_3698
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_id) from _call_give_gift_17
            call her_main("Thank you, [genie_name]!","base","base") from _call_her_main_3699
            call her_main("I will use them for my research!") from _call_her_main_3700
            call happy(10) from _call_happy_17
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Oh...","open","base") from _call_her_main_3701
            call her_main("Yes, I used to read magazines like that a lot...","base","base") from _call_her_main_3702
            call her_main("Lately not so much though...","open","worriedL") from _call_her_main_3703
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_id) from _call_give_gift_18
            call her_main("Thank you, [genie_name]!","base","base") from _call_her_main_3704
            call happy(3) from _call_happy_18
        if whoring >= 18: # Lv 7+  
            call her_main("Ehm...","open","worriedL") from _call_her_main_3705
            call her_main("To be honest, magazines like that lost their appeal to me completely lately...","open","suspicious") from _call_her_main_3706
            call her_main("But I don't mind taking them off you hands anyway, [genie_name].","open","worried") from _call_her_main_3707
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_id) from _call_give_gift_19
            call her_main("Thank you.","soft","baseL") from _call_her_main_3708
            call no_change from _call_no_change 
    if gift_id == 5:#girl mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Hm?","soft","base") from _call_her_main_3709
            call her_main("This is the sort of press some \"slytherin\" bimbo would appreciate.","annoyed","suspicious") from _call_her_main_3710
            call her_main("I am way above silly magazines like that, [genie_name].","open","closed") from _call_her_main_3711
            call no_change from _call_no_change_1
            $ h_body = "body_01"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("I don't read magazines of that nature, [genie_name]...","open","angryCl") from _call_her_main_3712
            call her_main("................","soft","baseL") from _call_her_main_3713
            call her_main("But I could give it a try just to humour you I suppose...","open","angryCl") from _call_her_main_3714
            call give_gift(">You give an assortment of rather girly magazines to Hermione...",gift_id) from _call_give_gift_20
            call her_main("Thank you, [genie_name]!","open","suspicious") from _call_her_main_3715
            call happy(5) from _call_happy_19
            $ h_body = "body_06"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("I ashamed to admit this, but...","open","worriedL") from _call_her_main_3716
            call her_main("I really enjoy reading magazines like that lately...","grin","worriedCl",emote="05") from _call_her_main_3717
            call give_gift(">You give an assortment of rather girly magazines to Hermione...",gift_id) from _call_give_gift_21
            call her_main("Thank you, [genie_name].","open","suspicious") from _call_her_main_3718
            call happy(15) from _call_happy_20
            $ h_body = "body_06"
        if whoring >= 18: # Lv 7+  
            call her_main("The Latest edition of \"Girlz\"?!","angry","wide") from _call_her_main_3719
            call her_main("I can't have enough of that brilliant magazine!","grin","worriedCl",emote="05") from _call_her_main_3720
            call give_gift(">You give an assortment of rather girly magazines to Hermione...",gift_id) from _call_give_gift_22
            call her_main("Thank you, [genie_name].","open","suspicious") from _call_her_main_3721
            call happy(15) from _call_happy_21
            $ h_body = "body_06"
    if gift_id == 6:#adult mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Are that...?","open","base") from _call_her_main_3722
            call her_main("Adult magazines, [genie_name]?","open","base") from _call_her_main_3723
            call her_main("Given to me by An esteemed wizard of your status?","annoyed","angryL") from _call_her_main_3724
            call her_main("[genie_name], surely you could find a more productive way to spend your free time.","disgust","glance") from _call_her_main_3725
            call her_main("And I most definitely would not have use for those...","angry","angry") from _call_her_main_3726
            call upset(7) from _call_upset
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Adult magazines?","angry","angry") from _call_her_main_3727
            call her_main("[genie_name], I have no interest in things like that.","annoyed","angryL") from _call_her_main_3728
            call her_main("And how is this an appropriate present for one of your students, [genie_name]?","angry","angry") from _call_her_main_3729
            call upset(3) from _call_upset_1
            $ h_body = "body_29"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Adult magazines?","open","base") from _call_her_main_3730
            call her_main("[genie_name], this is such an inappropriate present for a girl my age...","angry","worriedCl",emote="05") from _call_her_main_3731
            call give_gift(">You give an assortment of adult magazines to Hermione...",gift_id) from _call_give_gift_23
            call her_main("I shall throw these away myself...","annoyed","annoyed") from _call_her_main_3732
            call happy(8) from _call_happy_22
            $ h_body = "body_120"
        if whoring >= 18: # Lv 7+  
            call her_main("The New edition of \"L.o.v.e.\"!!!","smile","happyCl") from _call_her_main_3733
            call her_main("Err.. I mean, adult magazines?","angry","wink") from _call_her_main_3734
            call her_main("This is a little inappropriate...") from _call_her_main_3735
            call her_main("But I will take them...","base","happyCl") from _call_her_main_3736
            call give_gift(">You give an assortment of adult magazines to Hermione...",gift_id) from _call_give_gift_24
            call her_main("thank you, [genie_name].","base","happyCl") from _call_her_main_3737
            call happy(15) from _call_happy_23
    if gift_id == 7:#porn mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Hm... What is this?","base","base") from _call_her_main_3738
            call her_main("[genie_name], those are porn magazines!","scream","wide") from _call_her_main_3739
            call her_main("Shame on you, [genie_name]!","angry","angry",cheeks="blush") from _call_her_main_3740
            call upset(15) from _call_upset_2
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Porn magazines?","shock","wide") from _call_her_main_3741
            call her_main("[genie_name], what do you expect me to do with those?","open","down") from _call_her_main_3742
            call her_main("Research them?","annoyed","annoyed") from _call_her_main_3743
            call her_main("Despicable!","scream","angry",emote="01") from _call_her_main_3744
            call upset(8) from _call_upset_3
            $ h_body = "body_120"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("That's hardcore porn, [genie_name].","open","base") from _call_her_main_3745
            call her_main("Which is a completely inappropriate gift for a girl my age!","angry","worriedCl",emote="05") from _call_her_main_3746
            call her_main("..............","angry","down_raised") from _call_her_main_3747
            call her_main("But I will take them...","angry","base") from _call_her_main_3748
            call give_gift(">You give an assortment of porn magazines to Hermione...",gift_id) from _call_give_gift_25
            call her_main("And I shall throw them in the trash, where they and... girls who like these things belong...","annoyed","annoyed") from _call_her_main_3749
            call no_change from _call_no_change_2
            $ h_body = "body_120"
        if whoring >= 18: # Lv 7+  
            call her_main("Pornography?","shock","wide") from _call_her_main_3750
            call her_main("................","angry","down_raised") from _call_her_main_3751
            call her_main("How can women even agree to do things like that, [genie_name]?","angry","base") from _call_her_main_3752
            call her_main(".................","angry","down_raised") from _call_her_main_3753
            call her_main("Alright, I shall accept them...","upset","closed") from _call_her_main_3754
            call her_main("Solely for research purposes of course...","open","baseL",cheeks="blush") from _call_her_main_3755
            call give_gift(">You give an assortment of porn magazines to Hermione...",gift_id) from _call_give_gift_26
            call happy(15) from _call_happy_24
            $ h_body = "body_45"
    if gift_id == 8:#krum poster
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A Quidditch poster?","annoyed","down") from _call_her_main_3756
            call her_main("What am I supposed to do with it, [genie_name]?","annoyed","annoyed") from _call_her_main_3757
            call her_main("No, thank you.","annoyed","closed") from _call_her_main_3758
            call no_change from _call_no_change_3
            $ h_body = "body_71"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("A Quidditch poster?","annoyed","down") from _call_her_main_3759
            call her_main("Hm...","annoyed","annoyed") from _call_her_main_3760
            call her_main("I think I saw this player once or twice...","annoyed","down") from _call_her_main_3761
            call her_main("He is that Durmstrang student, right?","base","base") from _call_her_main_3762
            call give_gift(">You give the poster to Hermione...",gift_id) from _call_give_gift_27
            call happy(5) from _call_happy_25
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A Viktor Krum poster, [genie_name]?","annoyed","down") from _call_her_main_3763
            call her_main("Can't say that I care much for Quidditch, but...","open","suspicious") from _call_her_main_3764
            call her_main("I can see why the girls find the brutish physique of some players appealing...","open","down") from _call_her_main_3765
            call give_gift(">You give the poster to Hermione...",gift_id) from _call_give_gift_28
            call happy(15) from _call_happy_26
        if whoring >= 18: # Lv 7+  
            call her_main("A Viktor Krum poster?!","scream","wide_stare") from _call_her_main_3766
            call her_main("Thank you, [genie_name]!","grin","worriedCl",emote="05") from _call_her_main_3767
            call give_gift(">You give the poster to Hermione...",gift_id) from _call_give_gift_29
            call her_main("Can't wait to hang it over my bed!","smile","baseL") from _call_her_main_3768
            call her_main("The girls will go green with envy...","smile","glance") from _call_her_main_3769
            call happy(25) from _call_happy_27
    if gift_id == 9:#lingerie
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("lingerie?","angry","down_raised") from _call_her_main_3770
            call her_main("[genie_name], I cannot accept a gift like this from you...","upset","closed") from _call_her_main_3771
            call upset(10) from _call_upset_4
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("sexy lingerie?","angry","down_raised") from _call_her_main_3772
            call her_main("You know I cannot possibly accept a gift like that from you, [genie_name].","angry","base") from _call_her_main_3773
            call her_main("(It's pretty though).........","angry","down_raised") from _call_her_main_3774
            call no_change from _call_no_change_4
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("sexy lingerie?","base","down") from _call_her_main_3775
            call her_main("[genie_name] that is so inappropriate...","angry","wink") from _call_her_main_3776
            call give_gift(">You give the lingerie to Hermione...",gift_id) from _call_give_gift_30
            call her_main("Thank you, [genie_name].","base","baseL",cheeks="blush") from _call_her_main_3777
            call happy(7) from _call_happy_28
        if whoring >= 18: # Lv 7+  
            call her_main("sexy lingerie?","base","down") from _call_her_main_3778
            call her_main("Do You think it will make me look like one of the witches in those adult magazines, [genie_name]?","grin","dead") from _call_her_main_3779
            call her_main("Oh... I mean, thank you, [genie_name].","angry","wink") from _call_her_main_3780
            call give_gift(">You give the lingerie to Hermione...",gift_id) from _call_give_gift_31
            call happy(15) from _call_happy_29
    if gift_id == 10:#condoms
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Condoms?!","angry","wide") from _call_her_main_3781
            call her_main("[genie_name], I wouldn't even know what to do with them...","scream","angryCl") from _call_her_main_3782
            call upset(6) from _call_upset_5
            $ h_body = "body_03"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("...Condoms?","normal","frown") from _call_her_main_3783
            call her_main("Ehm... Is this a part of some new Hogwarts sex ed program or something?","open","angryCl") from _call_her_main_3784
            call her_main("No, [genie_name]... It feels wrong to accept a thing like this from you...","open","baseL",cheeks="blush") from _call_her_main_3785
            call no_change from _call_no_change_5
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A pack of condoms?","normal","base") from _call_her_main_3786
            call her_main("[genie_name], what possible use could I have for those?") from _call_her_main_3787
            call her_main("Well, I shall accept them simply because it is rude to refuse a gift...","open","angryCl") from _call_her_main_3788
            call give_gift(">You give a pack of condoms to Hermione...", gift_id) from _call_give_gift_32
            call happy(3) from _call_happy_30
            $ h_body = "body_29"
        if whoring >= 18: # Lv 7+
            call her_main("A pack of condoms?","open","suspicious") from _call_her_main_3789
            call her_main("I appreciate your concern, [genie_name]. Thank you.","base","glance") from _call_her_main_3790
            call give_gift(">You give a pack of condoms to Hermione...", gift_id) from _call_give_gift_33
            call happy(4) from _call_happy_31
            $ h_body = "body_45"
    if gift_id == 11:#vibrator
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A magic wand?","base","base") from _call_her_main_3791
            call her_main("No, it doesn't look like--","soft","base") from _call_her_main_3792
            call her_main(".........?") from _call_her_main_3793
            call her_main("!!!","angry","wide") from _call_her_main_3794
            call her_main("[genie_name]!","angry","angry",cheeks="blush") from _call_her_main_3795
            call her_main("This is just beyond inappropriate!","scream","angryCl") from _call_her_main_3796
            call upset(10) from _call_upset_6
            $ h_body = "body_120"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Is this what I think it is?","angry","down_raised") from _call_her_main_3797
            call her_main("[genie_name], let me remind you that I belong to the noble house of \"Gryffindor\".","open","annoyed",cheeks="blush") from _call_her_main_3798
            call her_main("A present like that would be appropriate for a girl from \"Slytherin\", [genie_name].","upset","closed") from _call_her_main_3799
            call upset(10) from _call_upset_7
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Is that a... vibrator?","angry","down_raised") from _call_her_main_3800
            call her_main("The design...") from _call_her_main_3801
            call her_main("it reminds me of my wand...") from _call_her_main_3802
            call her_main("Did you have this custom made for me [genie_name]?","angry","down_raised") from _call_her_main_3803
            call her_main("This is inappropriate...","scream","angryCl") from _call_her_main_3804
            call her_main("But I shall take it nonetheless...","annoyed","worriedL") from _call_her_main_3805
            call give_gift(">You give the vibrator to Hermione...",gift_id) from _call_give_gift_34
            call no_change from _call_no_change_6
        if whoring >= 18: # Lv 7+  
            call her_main("This vibrator...","open","worried") from _call_her_main_3806
            call her_main("It's... calling out for me...","open","worriedL") from _call_her_main_3807
            call her_main("But not in a dirty way, [genie_name].","disgust","glance") from _call_her_main_3808
            call give_gift(">You give the vibrator to Hermione...",gift_id) from _call_give_gift_35
            call her_main("Thank you, [genie_name].","base","down") from _call_her_main_3809
            call happy(10) from _call_happy_32
    if gift_id == 12:#anal lube
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("I don't know what this is...","open","base") from _call_her_main_3810
            call her_main("But I have the feeling that the jar is full of something vile and inappropriate...","angry","angry") from _call_her_main_3811
            call her_main("No, thank you, [genie_name].") from _call_her_main_3812
            call upset(6) from _call_upset_8
            $ h_body = "body_03"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Hm...","annoyed","down") from _call_her_main_3813
            call her_main("I think I know what this is...","disgust","glance") from _call_her_main_3814
            call her_main("But why would you give something like this to one of your pupils, [genie_name]?") from _call_her_main_3815
            call her_main("No, thank you.","annoyed","angryL") from _call_her_main_3816
            call upset(2) from _call_upset_9
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Anal lubricant?","angry","down_raised") from _call_her_main_3817
            call her_main("Ehm.. well... I know this girl...","open","baseL",cheeks="blush") from _call_her_main_3818
            call her_main("I mean I don't know her, she is a friend of a friend...") from _call_her_main_3819
            call her_main("Yes, I will take this for her...") from _call_her_main_3820
            call give_gift(">You give the jar to Hermione...", gift_id, 0) from _call_give_gift_36
            call her_main("Still, I think you should not give presents like this to your pupils, [genie_name].","open","annoyed",cheeks="blush") from _call_her_main_3821
            call no_change from _call_no_change_7
            $ h_body = "body_79"
        if whoring >= 18: # Lv 7+  
            call her_main("Anal lubricant, [genie_name]?","base","down") from _call_her_main_3822
            call her_main("I know a couple of girls who would do anything for a commodity like that.","open","annoyed",cheeks="blush") from _call_her_main_3823
            call her_main("Thank for looking out for us, [genie_name].","base","glance") from _call_her_main_3824
            call give_gift(">You give the jar to Hermione...", gift_id) from _call_give_gift_37
            call happy(5) from _call_happy_33
    if gift_id == 13:#gag and cuffs
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("What is this?","angry","down_raised") from _call_her_main_3825
            call her_main("Is this like one of those adult toys?","angry","suspicious",cheeks="blush") from _call_her_main_3826
            call her_main("What woman in her right mind would subject herself to a humiliation like that?","scream","angryCl") from _call_her_main_3827
            call her_main("And what possible use could I have for such objects?","open","annoyed",cheeks="blush") from _call_her_main_3828
            call her_main("This is just insulting, [genie_name]...","angry","angry",cheeks="blush") from _call_her_main_3829                                                                                                                                                                                                              
            call upset(10) from _call_upset_10
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("[genie_name], do you not realize how inappropriate it would be for me to accept a present like that?","open","annoyed",cheeks="blush") from _call_her_main_3830
            call her_main("And I would not even know what to do with them anyway...","open","baseL",cheeks="blush") from _call_her_main_3831
            call her_main("I mean these fluffy things are obviously handcuffs...","angry","down_raised") from _call_her_main_3832
            call her_main("But this ball... ehm...") from _call_her_main_3833
            call her_main("[genie_name], please...","upset","closed") from _call_her_main_3834
            call her_main("Just put them away.") from _call_her_main_3835
            call upset(5) from _call_upset_11
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A month ago I would've felt insulted to receive a gift like this...","upset","closed") from _call_her_main_3836
            call her_main("But by now I know that some girls really do find pleasure in toys like...","angry","down_raised") from _call_her_main_3837
            call her_main("But I assure you that I am not one of them, [genie_name].","upset","closed") from _call_her_main_3838
            call her_main("But I know a girl who knows a girl who is into things like...","open","baseL",cheeks="blush") from _call_her_main_3839
            call her_main("Yes, I shall take these to her...","base","baseL",cheeks="blush") from _call_her_main_3840
            call give_gift(">You give the ball gag and cuffs to Hermione...",gift_id) from _call_give_gift_38
            call happy(9) from _call_happy_34
        if whoring >= 18: # Lv 7+  
            call her_main("A ball gag and handcuffs?","open","squint",cheeks="blush") from _call_her_main_3841
            call her_main("This is completely inappropriate, [genie_name].","angry","wink") from _call_her_main_3842 # :)
            call her_main("But a gift is a gift, right?","base","suspicious") from _call_her_main_3843
            call give_gift(">You give the ball gag and cuffs to Hermione...",gift_id) from _call_give_gift_39
            call happy(15) from _call_happy_35
    if gift_id == 14:#anal plugs
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Hm...?","base","base") from _call_her_main_3844
            call her_main("Are those like key-chain toys?","soft","base") from _call_her_main_3845
            call give_gift(">You give the anal plugs to Hermione...",gift_id) from _call_give_gift_40
            call her_main("Thank you, [genie_name].","annoyed","annoyed") from _call_her_main_3846
            call happy(8) from _call_happy_36
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("[genie_name], are those adult toys of some sort?","open","annoyed",cheeks="blush") from _call_her_main_3847
            call her_main("those are some of those anal things, aren't they?","angry","angry",cheeks="blush") from _call_her_main_3848
            call her_main("[genie_name] this is nothing but a weapon meant to oppress women!") from _call_her_main_3849
            call her_main("Despicable!","upset","closed") from _call_her_main_3850
            call upset(15) from _call_upset_12
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Yes, I know that some girls have uhm...","upset","closed") from _call_her_main_3851
            call her_main("Have use for things such as these...","open","annoyed",cheeks="blush") from _call_her_main_3852
            call her_main("But not me, [genie_name].") from _call_her_main_3853
            call her_main("No, thank you.","upset","closed") from _call_her_main_3854
            call no_change from _call_no_change_8
        if whoring >= 18: # Lv 7+  
            call her_main("Anal plugs?","angry","down_raised") from _call_her_main_3855
            call her_main("I have no use for things like that, [genie_name]...","angry","base") from _call_her_main_3856
            call her_main("They are so pretty though...","angry","wink") from _call_her_main_3857
            call her_main(".....................","angry","down_raised") from _call_her_main_3858
            call her_main("Well, alright. I shall take them off your hands if I must, [genie_name].","soft","ahegao") from _call_her_main_3859
            call give_gift(">You give the anal plugs to Hermione...",gift_id) from _call_give_gift_41
            call her_main("But I shall never use them of course...","open","closed") from _call_her_main_3860
            call her_main("................","base","down") from _call_her_main_3861
            call happy(10) from _call_happy_37
    if gift_id == 15:#strap on
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("What is that?","angry","wide") from _call_her_main_3862
            call her_main("An artifact of some sort or a trophy?","open","base") from _call_her_main_3863
            call her_main("So well-crafted...","base","base") from _call_her_main_3864
            call her_main("Are you sure that it's alright for me to have it, [genie_name]?","base","base") from _call_her_main_3865
            call give_gift(">You give the strap-on to Hermione...",gift_id) from _call_give_gift_42
            call her_main("Thank you very much, [genie_name]. I promise to take good care of it.","open","closed") from _call_her_main_3866
            call happy(20) from _call_happy_38
            $ h_body = "body_15"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("!!!","angry","wide") from _call_her_main_3867
            call her_main("That is...","angry","down_raised") from _call_her_main_3868
            call her_main("But it doesn't even look... human...") from _call_her_main_3869
            call her_main("I mean...","annoyed","angryL") from _call_her_main_3870
            call her_main("[genie_name], do you have no shame?!","scream","angry",emote="01") from _call_her_main_3871
            call her_main("Presenting a thing like that to a pupil?!") from _call_her_main_3872
            call her_main("..................","open","down") from _call_her_main_3873
            call her_main("Please put it away, [genie_name].","angry","angry") from _call_her_main_3874
            call upset(15) from _call_upset_13
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("That thing...","angry","down_raised") from _call_her_main_3875
            call her_main("Is that the actual size of the... of the real \"thing\"?","angry","base") from _call_her_main_3876
            call her_main("I mean...","open","baseL",cheeks="blush") from _call_her_main_3877
            call her_main(".......................","angry","down_raised") from _call_her_main_3878
            call her_main("Is this like a party prank prop?","angry","base") from _call_her_main_3879
            call her_main("It's so well-crafted though...","angry","down_raised") from _call_her_main_3880
            call her_main("I will take it...","normal","worriedCl") from _call_her_main_3881
            call give_gift(">You give the strap-on to Hermione...",gift_id) from _call_give_gift_43
            call happy(10) from _call_happy_39
        if whoring >= 18: # Lv 7+  
            call her_main("It's... It's magnificent, [genie_name]...","shock","wide") from _call_her_main_3882
            call her_main("Is it really modeled after a thestral?","open","baseL",cheeks="blush") from _call_her_main_3883
            call her_main("But the creatures are invisible...","open","squint",cheeks="blush") from _call_her_main_3884
            call her_main("..................","angry","down_raised") from _call_her_main_3885
            call her_main("Breathtaking...","grin","dead") from _call_her_main_3886
            call her_main("Not in the way you think, [genie_name]...","upset","closed") from _call_her_main_3887
            call her_main("I am merely admiring the craftsmanship...","open","closed") from _call_her_main_3888
            call give_gift(">You give the strap-on to Hermione...",gift_id) from _call_give_gift_44
            call her_main("Thank you for the gift, [genie_name].","base","suspicious") from _call_her_main_3889
            call happy(30) from _call_happy_40
    if gift_id == 16:#speed stick
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A broom...?","base","base") from _call_her_main_3890
            call her_main("Hm...","normal","base") from _call_her_main_3891
            call her_main("What is that silly-looking thing attached to it?","normal","frown") from _call_her_main_3892
            call her_main("Is it like a saddle...?","open","suspicious") from _call_her_main_3893
            call give_gift(">You give the broom to Hermione...",gift_id) from _call_give_gift_45
            call her_main("Thank you for the gift, [genie_name].","open","worried") from _call_her_main_3894
            $ h_body = "body_06"
            call happy(20) from _call_happy_41
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("A broom...?","base","base") from _call_her_main_3895
            call her_main("Hm...","normal","frown") from _call_her_main_3896
            call her_main("It's a sex-toy of some sort, isn't it?","angry","angry") from _call_her_main_3897
            call her_main("But it is so well crafted...","open","down") from _call_her_main_3898
            call give_gift(">You give the broom to Hermione...",gift_id) from _call_give_gift_46
            call her_main("Thank you, [genie_name].","upset","closed") from _call_her_main_3899
            call happy(20) from _call_happy_42
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A broom...?","angry","down_raised") from _call_her_main_3900
            call her_main("Hm...") from _call_her_main_3901
            call her_main("What kind of saddle is that...?","disgust","glance") from _call_her_main_3902
            call her_main("Well, doesn't matter.","open","closed") from _call_her_main_3903
            call her_main("Refusing an expensive gift like that would be rude...") from _call_her_main_3904
            call give_gift(">You give the broom to Hermione...",gift_id) from _call_give_gift_47
            call her_main("Thank you, [genie_name].","upset","closed") from _call_her_main_3905
            call happy(30) from _call_happy_43
        if whoring >= 18: # Lv 7+  
            call her_main("A broom...","base","down") from _call_her_main_3906
            call her_main("Hm...") from _call_her_main_3907
            call her_main("That saddle, [genie_name]...","open","baseL",cheeks="blush") from _call_her_main_3908
            call her_main("It was designed especially for witches, was it not?","open","squint",cheeks="blush") from _call_her_main_3909
            call her_main("I am not sure whether this is inappropriate or clever...","annoyed","annoyed") from _call_her_main_3910
            call her_main("But this is a brilliant piece of engineering eitherway...","base","suspicious") from _call_her_main_3911
            call give_gift(">You give the broom to Hermione...",gift_id) from _call_give_gift_48
            call her_main("Thank you, [genie_name].","base","glance") from _call_her_main_3912
            call happy(30) from _call_happy_44
    if gift_id == 17:#sex doll
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Is this...","shock","wide") from _call_her_main_3913
            call her_main("A sex doll?!","angry","worriedCl",emote="05") from _call_her_main_3914
            call her_main("[genie_name]!!!","scream","worriedCl") from _call_her_main_3915
            call upset(20) from _call_upset_14
            $ h_body = "body_33"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("A sex doll?","shock","wide") from _call_her_main_3916
            call her_main("This is just so unbecoming for an esteemed wizard such as yourself, [genie_name]...","upset","closed") from _call_her_main_3917
            call upset(20) from _call_upset_15
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A sex doll...","angry","down_raised") from _call_her_main_3918
            call her_main("This is a little inappropriate...","upset","closed") from _call_her_main_3919
            call her_main("But maybe we could use it for a prank or something...","base","down") from _call_her_main_3920
            call give_gift(">You give the blow-up doll to Hermione...",gift_id) from _call_give_gift_49
            call her_main("Thank you, [genie_name].","base","down") from _call_her_main_3921
            call happy(10) from _call_happy_45
        if whoring >= 18: # Lv 7+  
            call her_main("the Joanne sex doll?","annoyed","down") from _call_her_main_3922
            call her_main("I Can't say that I approve of this...","open","baseL",cheeks="blush") from _call_her_main_3923
            call her_main("But I know Harry would love to have a go at it...","base","down") from _call_her_main_3924
            call give_gift(">You give the blow-up doll to Hermione...",gift_id) from _call_give_gift_50
            call her_main("Thank you, [genie_name].","base","baseL",cheeks="blush") from _call_her_main_3925
            call happy(30) from _call_happy_46
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    show screen hermione_main
    with d3
    return
    
label give_gift(text = "", gift = 0):
    hide screen hermione_main
    with d3
    # note that gift is the index (starting with 0), while the image
    # files are starting with/off by 1!
    $ the_gift = "images/store/gifts/"+str(gift+1)+".png"
    show screen gift
    with d3
    "[text]"
    hide screen gift
    with d3
    $ gift_item_inv[gift] -= 1
    return
    
    
###GIVING CLOTHING RESPONSES
label giving_gryffindor_cheer:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    call her_main("A Cheerleading costume?","normal","base",xpos=140) from _call_her_main_3926
    hide screen hermione_main
    with d3
    $ the_gift = "images/store/07.png" # blue box
    show screen gift
    with d3
    ">You give the outfit to Hermione...\n>A Gryffindor Cheerleading outfit has been added to the wardrobe."
    hide screen gift
    call her_main("Thank you, [genie_name], although I don't know when I'd wear it.","open","angryCl") from _call_her_main_3927
    call happy from _call_happy_47
    
    call her_main("","normal","base",xpos=370) from _call_her_main_3928
    jump day_time_requests    

label giving_slytherin_cheer:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    call her_main("A Cheerleading costume? For Slytherin?","normal","base",xpos=140) from _call_her_main_3929
    hide screen hermione_main
    with d3
    $ the_gift = "images/store/07.png" # blue box
    show screen gift
    with d3
    ">You give the outfit to Hermione...\n>A Slytherin Cheerleading outfit has been added to the wardrobe."
    hide screen gift
    call her_main("Thank you, [genie_name], even though I'm not in Slytherin...","open","angryCl") from _call_her_main_3930
    call happy from _call_happy_48
    
    call her_main("","normal","base",xpos=370) from _call_her_main_3931
    jump day_time_requests    

label giving_maid_outfit:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    $ nets = 7 # Means already gifted.
    call her_main("A maid outfit?","normal","base",xpos=140) from _call_her_main_3932
    hide screen hermione_main
    with d3
    $ the_gift = "images/store/07.png" # blue box
    show screen gift
    with d3
    ">You give the outfit to Hermione...\n>A maid outfit has been added to the wardrobe."
    hide screen gift
    call her_main("Thank you, [genie_name].","open","angryCl") from _call_her_main_3933
    call happy from _call_happy_49
    
    call her_main("","normal","base",xpos=370) from _call_her_main_3934
    jump day_time_requests    

label giving_silk_nightgown:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    call her_main("A nightgown?","normal","base",xpos=140) from _call_her_main_3935
    hide screen hermione_main
    with d3
    $ the_gift = "images/store/07.png"# blue box
    show screen gift
    with d3
    ">You give the nightgown to Hermione...\n>A silk nightgown has been added to the wardrobe."
    hide screen gift
    call her_main("Thank you, [genie_name].","open","angryCl") from _call_her_main_3936
    call happy from _call_happy_50
    
    call her_main("","normal","base",xpos=370) from _call_her_main_3937
    jump day_time_requests    
    
    
label giving_skirt:
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ have_miniskirt = False # Turns TRUE when you have the skirt in your possession.
    $ gave_miniskirt = True #Turns True when Hermione has the miniskirt.
    $ days_without_an_event = 0
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5
    
    
    $ mad = 0
    m "Here... This is for you..."
    $ the_gift = "images/store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">You give the school miniskirt to Hermione..."
    hide screen gift
    with d3
    hide screen hermione_main
    with d3
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    
    call her_main("Hm...? What is this?","base","base") from _call_her_main_3938
    call her_main("A skirt?","open","worried") from _call_her_main_3939
    call her_main("Thank you [genie_name].","base","base") from _call_her_main_3940
    #her "Thank you professor."
    m "Don't mention it."
    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3  
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "body_01"
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    jump day_time_requests
    
### DRESS CODE ###
label mini_on:
    
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("You cannot be serious, [genie_name]!","open","angryCl") from _call_her_main_3941
        her "A skirt this short?!"
        call her_main("...It barely covers anything, [genie_name].","annoyed","annoyed") from _call_her_main_3942
        menu:
            m "..."
            "\"Fine. Forget it.\"":
                call her_main("Gladly...","disgust","glance") from _call_her_main_3943
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                call her_main("well, alright...","disgust","glance") from _call_her_main_3944
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 10
                call upset from _call_upset_16
        
        

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Hm...?","soft","base") from _call_her_main_3945
        call her_main("But it's so short...","annoyed","suspicious") from _call_her_main_3946
        menu:
            m "..."
            "\"Just put it on!\"":
                call her_main("[genie_name] this is hardly the appropriate attire for a Hogwarts student.","normal","frown") from _call_her_main_3947
                call her_main("I refuse!","annoyed","frown") from _call_her_main_3948
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                call upset from _call_upset_17                                                                                                                                                                                                                #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                call her_main("Hm...","normal","frown") from _call_her_main_3949
                call her_main("Well, in that case...","open","suspicious") from _call_her_main_3950
                call her_main("As long as it benefits my house...","annoyed","worriedL") from _call_her_main_3951
            "\"Fine. Forget it\"":
                call her_main("Alright...","base","base") from _call_her_main_3952
                jump day_time_requests

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Hm...?","soft","base") from _call_her_main_3953
        call her_main("But it's so short...","annoyed","suspicious") from _call_her_main_3954
        menu:
            m "..."
            "\"Just put it on!\"":
                call her_main("Alright, alright...","annoyed","angryL") from _call_her_main_3955
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                call her_main("Hm...","normal","frown") from _call_her_main_3956
                call her_main("Alright. I don't mind then.","grin","baseL") from _call_her_main_3957
            "\"Fine. Forget it\"":
                call her_main("Oh...","soft","baseL") from _call_her_main_3958
                jump day_time_requests
        


    
    if whoring >= 18: # Lv 7+
        call her_main("Of course, [genie_name]...","angry","down_raised") from _call_her_main_3959
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_78"
                                                                                                                                                                                                                          #HERMIONE
    
    
    $ legs_02 = True
    $ legs_03 = False
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_109 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_110 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    
label mini_off:
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("I'm glad that you came to your senses, [genie_name].","open","angryCl") from _call_her_main_3960
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_03"
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Gladly, [genie_name].","base","base") from _call_her_main_3961

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Alright...","soft","baseL") from _call_her_main_3962
    
    if whoring >= 18: # Lv 7+
        call her_main("That boring thing again?","angry","worried") from _call_her_main_3963
    
    
    $ legs_02 = False
    $ legs_03 = False
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_111 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_112 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
   
label tiny_on:
    
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("You cannot be serious, [genie_name]!","open","angryCl") from _call_her_main_3964
        her "A skirt THIS short?!"
        call her_main("...It doesn't cover anything, [genie_name].","annoyed","annoyed") from _call_her_main_3965
        menu:
            m "..."
            "\"Fine. Forget it.\"":
                call her_main("Gladly...","disgust","glance") from _call_her_main_3966
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 35 points.\"":
                $ gryffindor +=35
                her "........................"
                her "..............................."
                call her_main("well, alright...","disgust","glance") from _call_her_main_3967
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 10
                call upset from _call_upset_18
        
        

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Hm...?","soft","base") from _call_her_main_3968
        call her_main("But it's soooo short...","annoyed","suspicious") from _call_her_main_3969
        menu:
            m "..."
            "\"Just put it on!\"":
                call her_main("[genie_name] this is hardly the appropriate attire for a Hogwarts student.","normal","frown") from _call_her_main_3970
                call her_main("I refuse!","annoyed","frown") from _call_her_main_3971
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                call upset from _call_upset_19                                                                                                                                                                                                                #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 35 points.\"":
                $ gryffindor +=35
                call her_main("Hm...","normal","frown") from _call_her_main_3972
                call her_main("Well, in that case...","open","suspicious") from _call_her_main_3973
                call her_main("As long as it benefits my house...","annoyed","worriedL") from _call_her_main_3974
            "\"Fine. Forget it\"":
                call her_main("Alright...","base","base") from _call_her_main_3975
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Hm...?","soft","base") from _call_her_main_3976
        call her_main("But it's soooo short...","annoyed","suspicious") from _call_her_main_3977
        menu:
            m "..."
            "\"Just put it on!\"":
                call her_main("Alright, alright...","annoyed","angryL") from _call_her_main_3978
            "\"I will give you 10 points.\"":
                $ gryffindor +=10
                call her_main("Hm...","normal","frown") from _call_her_main_3979
                call her_main("Alright. I don't mind then.","grin","baseL") from _call_her_main_3980
            "\"Fine. Forget it\"":
                call her_main("Oh...","soft","baseL") from _call_her_main_3981
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
        


    
    if whoring >= 18: # Lv 7+
        call her_main("Of course, [genie_name]...","angry","down_raised") from _call_her_main_3982
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_78"
                                                                                                                                                                                                                          #HERMIONE
    
    
    $ legs_03 = True
    $ legs_02 = False
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_113 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_114 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    
label give_glasses:
    call her_main("But I don't need glasses...","base","base") from _call_her_main_3983
    
    $ glasses_worn = True
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_115 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_116 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label take_glasses:
    call her_main("I was just getting used to them though.","base","base") from _call_her_main_3984
    
    $ glasses_worn = False
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_117 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_118 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label badge_put:
    call her_main("Of course, [genie_name]...","base","base") from _call_her_main_3985
    
    $ hermione_badges = True
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_119 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_120 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label shirt_off:
    call her_main("That boring old thing? ok then","open","suspicious") from _call_her_main_3986
    
    $ wear_shirts = False
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_121 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_122 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label shirt_on:
    call her_main("Finally, it was soooo boring dressing like this","base","base") from _call_her_main_3987
    
    $ wear_shirts = True
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_123 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_124 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label bra_on:
    call her_main("What, I can't do that, everyone would call me a slut","angry","angry") from _call_her_main_3988
    m "just do it"
    $ h_body = "body_30"
    her "[genie_name], I have to draw a line somewhere, I'm not walking around with no shirt on!"
    m "i'll give you 100 points"
    her "200"
    m "sure, why not"
    her ".............fine"
    
    $ wear_shirts = False
    $ gryffindor +=200
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_125 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_126 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label bra_off:
    call her_main("oh thank you, you have no idea what it was like...","base","base") from _call_her_main_3989
    
    $ wear_shirts = True
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_127 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_128 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
    
label g_stockings_on:
    call her_main("Ok then","base","base") from _call_her_main_3990
    
    $ stockings = 2
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_129 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_130 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label g_stockings_off:
    call her_main("Ok.","base","base") from _call_her_main_3991
    
    $ stockings = 0
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_131 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_132 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label lace_on:
    call her_main("A bra?","base","base") from _call_her_main_3992
    m "I thought that you could use a new one."
    her "Thank you [genie_name]."
    
    $ custom_bra = 1
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_133 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_134 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label lace_off:
    call her_main("Ok","base","base") from _call_her_main_3993
    
    $ custom_bra = 0
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_135 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_136 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label cupless_on:
    call her_main("You want me to wear this?","base","base") from _call_her_main_3994
    m "No one will see it."
    her "...Fine"
    
    $ custom_bra = 2
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_137 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_138 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label cupless_off:
    call her_main("Finally. This thing isn't very comfortable.","base","base") from _call_her_main_3995
    
    $ custom_bra = 0
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_139 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_140 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label silk_on:
    call her_main("You want me to change bra?","base","base") from _call_her_main_3996
    her "Ok then"
    
    $ custom_bra = 3
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_141 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_142 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label silk_off:
    call her_main("Ok","base","base") from _call_her_main_3997
    
    $ custom_bra = 0
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_143 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_144 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_06_on:
    call her_main("What is this?","base","base") from _call_her_main_3998
    m "I literally have no idea"
    her "Ok then"
    
    $ custom_06_worn = True
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_145 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_146 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_06_off:
    call her_main("Ok","base","base") from _call_her_main_3999
    
    $ custom_06_worn = False
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_147 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_148 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_07_on:
    call her_main("What is this?","base","base") from _call_her_main_4000
    m "I literally have no idea"
    her "Ok then"
    
    $ custom_07_worn = True
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_149 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_150 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_07_off:
    call her_main("Ok","base","base") from _call_her_main_4001
    
    $ custom_07_worn = False
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_151 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_152 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_08_on:
    call her_main("What is this?","base","base") from _call_her_main_4002
    m "I literally have no idea"
    her "Ok then"
    
    $ custom_08_worn = True
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_153 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_154 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_08_off:
    call her_main("Ok","base","base") from _call_her_main_4003
    
    $ custom_08_worn = False
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_155 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_156 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_09_on:
    call her_main("What is this?","base","base") from _call_her_main_4004
    m "I literally have no idea"
    her "Ok then"
    
    $ custom_09_worn = True
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_157 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_158 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_09_off:
    call her_main("Ok","base","base") from _call_her_main_4005
    
    $ custom_09_worn = False
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_159 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_160 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_10_on:
    call her_main("What is this?","base","base") from _call_her_main_4006
    m "I literally have no idea"
    her "Ok then"
    
    $ custom_10_worn = True
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_161 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_162 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_10_off:
    call her_main("Ok","base","base") from _call_her_main_4007
    
    $ custom_10_worn = False
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_163 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_164 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label h_top_on:
    hide screen hermione_main
    with d5  
    $ hermione_wear_top = True
    call update_her_uniform from _call_update_her_uniform_84
    show screen hermione_main
    with d5 
    return
    
label h_top_off:
    hide screen hermione_main
    with d5    
    $ hermione_wear_top = False
    call update_her_uniform from _call_update_her_uniform_85
    show screen hermione_main
    with d5 
    return
    
label h_skirt_on:
    hide screen hermione_main
    with d5  
    $ hermione_wear_skirt = True
    call update_her_uniform from _call_update_her_uniform_86
    show screen hermione_main
    with d5 
    return
    
label h_skirt_off:
    hide screen hermione_main
    with d5  
    $ hermione_wear_skirt = False
    call update_her_uniform from _call_update_her_uniform_87
    show screen hermione_main
    with d5 
    return
    
###WEAR PANTIES
label h_panties_on:
    m "I want you to start wearing panties again"
    her "those boring old things"
    m "yep"
    her "do i get anything for this"
    menu:
        "hows 5 points sound":
            $ gryffindor += 5
            pass
        "nope just do it":
            pass
    her "fine I'll do it"
    $ h_request_wear_panties = True
    return
    
label h_panties_off:
    m "stop wearing those panties"
    her "freedom at last"
    $ h_request_wear_panties = False
    return
    
label h_badge_on(badge = "SPEW_badge"):
    hide screen hermione_main
    with d5
    $ hermione_badges = True
    $ h_badge = badge
    call update_her_uniform from _call_update_her_uniform_88
    show screen hermione_main
    with d5
    return
    
label h_badge_off(badge = "SPEW_badge"):
    hide screen hermione_main
    with d5
    $ hermione_badges = False
    $ h_badge = ""
    call update_her_uniform from _call_update_her_uniform_89
    show screen hermione_main
    with d5
    return
    

    


    
label set_h_costume(costume_id = 0):
    hide screen hermione_main
    with d5
    call h_outfit_OBJ(costume_id) from _call_h_outfit_OBJ_8
    show screen hermione_main
    with d5
    return
    

#call play_sound("door") #Sound of a door opening.
    
label badge_take:
    call her_main("As you wish, [genie_name]...","base","base") from _call_her_main_4008
    $ badges = True
    $ ba_01 = False
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_165 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_166 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
### FISHNETS ###
label nets_put:
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("fishnet stockings...?","open","worried") from _call_her_main_4009
        call her_main("You cannot be serious, [genie_name]!","open","base") from _call_her_main_4010
        menu:
            m "..."
            "\"Fine. Forget it.\"":
                call her_main("Gladly...","annoyed","angryL") from _call_her_main_4011
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                call her_main("well, alright...","disgust","glance") from _call_her_main_4012
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 5
                call upset from _call_upset_20
    
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Hm...?","soft","base") from _call_her_main_4013
        call her_main("I am not that kind of girl [genie_name]...","annoyed","suspicious") from _call_her_main_4014
        her "You may have better luck with someone from \"Slytherin\"..."
        menu:
            m "..."
            "\"Just put it on!\"":
                call her_main("[genie_name] this is hardly the appropriate attire for a Hogwarts student.","normal","frown") from _call_her_main_4015
                call her_main("I refuse!","annoyed","frown") from _call_her_main_4016
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                call upset from _call_upset_21                                                                                                                                                                                                                #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                call her_main("Hm...","normal","frown") from _call_her_main_4017
                call her_main("Well, in that case...","open","suspicious") from _call_her_main_4018
                call her_main("As long as it benefits my house...","annoyed","worriedL") from _call_her_main_4019
            "\"Fine. Forget it\"":
                call her_main("Alright...","base","base") from _call_her_main_4020
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
    
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Hm...?","soft","base") from _call_her_main_4021
        call her_main("Fishnet stockings?","annoyed","suspicious") from _call_her_main_4022
        call her_main("I don't know about that [genie_name]...","annoyed","worriedL") from _call_her_main_4023
        m "..."
        menu:
            "\"Just put them on!\"":
                call her_main("Alright, alright...","annoyed","angryL") from _call_her_main_4024
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                call her_main("Hm...","normal","frown") from _call_her_main_4025
                call her_main("Alright. I don't mind then.","grin","baseL") from _call_her_main_4026
            "\"Fine. Forget it\"":
                call her_main("Oh...","soft","baseL") from _call_her_main_4027
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3            
        jump day_time_requests
    
    if whoring >= 18: # Lv 7+
        call her_main("If you insist, [genie_name]...","angry","down_raised") from _call_her_main_4028
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_78"
    
    $ ne = True # Shows fishnets layer.
    $ ne_01 = True # Shows the fishnets.
    
    #$ legs_02 = True
    #$ legs_03 = False
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_167 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_168 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    pause.1
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    
label nets_take:
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("I'm glad that you came to your senses, [genie_name].","open","angryCl") from _call_her_main_4029
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_03"
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Gladly, [genie_name].","base","base") from _call_her_main_4030

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("As you wish, [genie_name].","annoyed","angryL") from _call_her_main_4031
    
    if whoring >= 18: # Lv 7+
        call her_main("Really? Aw...","angry","worried") from _call_her_main_4032
    
    
    $ ne = False # Shows fishnets layer.
    $ ne_01 = False # Shows the fishnets.
    #$ legs_02 = False
    #$ legs_03 = False
    
    show screen blkfade
    with d3
    call play_sound("door") from _call_play_sound_169 #Sound of a door opening.
    pause 2
    call play_sound("door") from _call_play_sound_170 #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    show screen hermione_main
    with d3
    jump day_time_requests

#

    


    
