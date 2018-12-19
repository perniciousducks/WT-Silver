init python:
    class gift_item(item_class):
        id = 0
        whoringNeeded = 0
        cost = 0

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def costOf(self, number_of_item):
            return self.cost * number_of_item

        def get_description(self):
            out_des = ""
            if len(self.description) > 90:
                out_des = self.description[0:90] + "..."
            else:
                out_des = self.description
            return out_des

        def get_buttom_right(self):
            return "Cost: " + str(self.cost)

label __init_variables:

    if not hasattr(renpy.store,'Lollipop'): #important!
        $ Lollipop = gift_item()
    $ Lollipop.id = 0
    $ Lollipop.cost = 20
    $ Lollipop.title = "lollipop candy"
    $ Lollipop.unlocked = True
    $ Lollipop.imagepath = "images/store/gifts/1.png"
    $ Lollipop.description = "A lollipop candy. An adult candy for kids or kids candy for adults?"


    if not hasattr(renpy.store,'Chocolate'): #important!
        $ Chocolate = gift_item()
    $ Chocolate.id = 1
    $ Chocolate.cost = 40
    $ Chocolate.title = "Chocolate"
    $ Chocolate.unlocked = True
    $ Chocolate.imagepath = "images/store/gifts/2.png"
    $ Chocolate.description = "The recipe for this delicious milk chocolate is kept a secret. (Rumoured to contain dried faeries)."

    if not hasattr(renpy.store,'PlushOwl'): #important!
        $ PlushOwl = gift_item()
    $ PlushOwl.id = 2
    $ PlushOwl.cost = 35
    $ PlushOwl.title = "Plush owl"
    $ PlushOwl.unlocked = True
    $ PlushOwl.imagepath = "images/store/gifts/3.png"
    $ PlushOwl.description = "a Toy owl stuffed with feathers of an actual owl. It's so cuddly!"

    if not hasattr(renpy.store,'Butterbeer'): #important!
        $ Butterbeer = gift_item()
    $ Butterbeer.id = 3
    $ Butterbeer.cost = 50
    $ Butterbeer.whoringNeeded = 3
    $ Butterbeer.title = "Butterbeer"
    $ Butterbeer.unlocked = True
    $ Butterbeer.imagepath = "images/store/gifts/4.png"
    $ Butterbeer.description = "Girls can't resist this beverage's buttery texture. Therefore it's always in high demand among the boys. \n{size=-4}Warning: no underage drinking is allowed without adults present.{/size}"

    if not hasattr(renpy.store,'EducationalMagazines'): #important!
        $ EducationalMagazines = gift_item()
    $ EducationalMagazines.id = 4
    $ EducationalMagazines.cost = 30
    $ EducationalMagazines.unlocked = True
    $ EducationalMagazines.title = "Educational magazines"
    $ EducationalMagazines.imagepath= "images/store/gifts/5.png"
    $ EducationalMagazines.description = "Educational magazines. \nthe Trusty companions of every social outcast."

    if not hasattr(renpy.store,'GirlyMagazines'): #important!
        $ GirlyMagazines = gift_item()
    $ GirlyMagazines.id = 5
    $ GirlyMagazines.cost = 45
    $ GirlyMagazines.title = "Girly magazines"
    $ GirlyMagazines.unlocked = True
    $ GirlyMagazines.imagepath= "images/store/gifts/6.png"
    $ GirlyMagazines.description = "Girly magazines. \nAll cool girls are reading these."

    if not hasattr(renpy.store,'AdultMagazines'): #important!
        $ AdultMagazines = gift_item()
    $ AdultMagazines.id = 6
    $ AdultMagazines.cost = 60
    $ AdultMagazines.title = "Adult magazines"
    $ AdultMagazines.unlocked = True
    $ AdultMagazines.imagepath= "images/store/gifts/7.png"
    $ AdultMagazines.description = "Your boyfriend is turning into a nice guy? \nYour husband won't abuse you anymore? \nAll you wanted to know about relationships, love and sex. Mostly about sex."

    if not hasattr(renpy.store,'PornMagazines'): #important!
        $ PornMagazines = gift_item()
    $ PornMagazines.id = 7
    $ PornMagazines.cost = 80
    $ PornMagazines.whoringNeeded = 3
    $ PornMagazines.title = "Porn magazines"
    $ PornMagazines.unlocked = True
    $ PornMagazines.imagepath= "images/store/gifts/8.png"
    $ PornMagazines.description = "Give these to your girlfriend to test her, to your wife to shame her and to your daughter to avoid \"the talk\"."

    if not hasattr(renpy.store,'ViktorKrumPoster'): #important!
        $ ViktorKrumPoster = gift_item()
    $ ViktorKrumPoster.id = 8
    $ ViktorKrumPoster.cost = 25 #placeholder number
    $ ViktorKrumPoster.title = "Viktor Krum Poster"
    $ ViktorKrumPoster.unlocked = True
    $ ViktorKrumPoster.imagepath= "images/store/gifts/9.png"
    $ ViktorKrumPoster.description = "A skilled Quidditch Seeker, Viktor has been selected to play for the Bulgarian National Quidditch team despite still going to school, and is widely regarded as one of the best players in the world."

    if not hasattr(renpy.store,'SexyLingerie'): #important!
        $ SexyLingerie = gift_item()
    $ SexyLingerie.id = 9
    $ SexyLingerie.cost = 75 #placeholder number
    $ SexyLingerie.title = "Sexy lingerie"
    $ SexyLingerie.unlocked = True
    $ SexyLingerie.imagepath= "images/store/gifts/10.png"
    $ SexyLingerie.description = "Sexy lingerie \"Fairy Godmother\". Charm your wizard in bed or empress your sisters at a Sabbath."

    if not hasattr(renpy.store,'PackOfCondoms'): #important!
        $ PackOfCondoms = gift_item()
    $ PackOfCondoms.id = 10
    $ PackOfCondoms.cost = 50
    $ PackOfCondoms.whoringNeeded = 3
    $ PackOfCondoms.title = "A pack of condoms"
    $ PackOfCondoms.unlocked = True
    $ PackOfCondoms.imagepath= "images/store/gifts/11.png"
    $ PackOfCondoms.description = "\"Pink unicorn condoms\". \nUnleash the one-horned beast!\n{size=-4}May contain traces of actual unicorn saliva.{/size}"

    if not hasattr(renpy.store,'Vibrator'): #important!
        $ Vibrator = gift_item()
    $ Vibrator.id = 11
    $ Vibrator.cost = 55
    $ Vibrator.whoringNeeded = 3
    $ Vibrator.title = "Vibrator"
    $ Vibrator.unlocked = True
    $ Vibrator.imagepath= "images/store/gifts/12.png"
    $ Vibrator.description = "A magnificent, magically enhanced vibrator made of vine wood, with a dragon heartstring core."

    if not hasattr(renpy.store,'JarOfLube'): #important!
        $ JarOfLube = gift_item()
    $ JarOfLube.id = 12
    $ JarOfLube.cost = 60
    $ JarOfLube.title = "Jar of anal lubricant"
    $ JarOfLube.unlocked = True
    $ JarOfLube.imagepath= "images/store/gifts/13.png"
    $ JarOfLube.description = "A Jar of anal lube, Buy this for your loved one - show that you care."

    if not hasattr(renpy.store,'BallGagAndCuffs'): #important!
        $ BallGagAndCuffs = gift_item()
    $ BallGagAndCuffs.id = 13
    $ BallGagAndCuffs.cost = 70
    $ BallGagAndCuffs.title = "Ball gag and cuffs"
    $ BallGagAndCuffs.unlocked = True
    $ BallGagAndCuffs.imagepath= "images/store/gifts/14.png"
    $ BallGagAndCuffs.description = "Ball gag and cuffs, Turn your soulmate into your cellmate."

    if not hasattr(renpy.store,'AnalPlugs'): #important!
        $ AnalPlugs = gift_item()
    $ AnalPlugs.id = 14
    $ AnalPlugs.cost = 85
    $ AnalPlugs.whoringNeeded = 3
    $ AnalPlugs.title = "Anal plugs"
    $ AnalPlugs.unlocked = True
    $ AnalPlugs.imagepath= "images/store/gifts/15.png"
    $ AnalPlugs.description = "Anal plugs decorated with actual tails. Sizes vary to satisfy expert practitioners and beginner alike."

    if not hasattr(renpy.store,'ThestralStrapon'): #important!
        $ ThestralStrapon = gift_item()
    $ ThestralStrapon.id = 15
    $ ThestralStrapon.cost = 200
    $ ThestralStrapon.whoringNeeded = 3
    $ ThestralStrapon.title = "Thestral Strap-on"
    $ ThestralStrapon.unlocked = True
    $ ThestralStrapon.imagepath= "images/store/gifts/16.png"
    $ ThestralStrapon.description = "Thestral strap-on.\nWhen you see it, you'll shit bricks."

    if not hasattr(renpy.store,'SpeedStick2000'): #important!
        $ SpeedStick2000 = gift_item()
    $ SpeedStick2000.id = 16
    $ SpeedStick2000.cost = 500
    $ SpeedStick2000.title = "Lady Speed Stick-2000"
    $ SpeedStick2000.unlocked = True
    $ SpeedStick2000.imagepath= "images/store/gifts/17.png"
    $ SpeedStick2000.description = "The \"Lady Speed Stick-2000\", an elegant way of transportation for passionate witches. The trademarked saddle guarantees full satisfaction. Get one for your witch and she won't use her boring old broom ever again!"

    if not hasattr(renpy.store,'SexDollJoanne'): #important!
        $ SexDollJoanne = gift_item()
    $ SexDollJoanne.id = 17
    $ SexDollJoanne.cost = 350
    $ SexDollJoanne.title = "Sex doll \"Joanne\""
    $ SexDollJoanne.unlocked = True
    $ SexDollJoanne.imagepath= "images/store/gifts/18.png"
    $ SexDollJoanne.description = "Sex doll \"Joanne\"... It's so realistic. Almost looks like a real human under the influence of a spell of some sort."

    if not hasattr(renpy.store,'AnalBeads'): #important!
        $ AnalBeads = gift_item()
    $ AnalBeads.id = 18
    $ AnalBeads.cost = 65 #placeholder number
    $ AnalBeads.title = "Anal beads"
    $ AnalBeads.unlocked = True
    $ AnalBeads.imagepath= "images/store/gift_anal_beads.png"
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
