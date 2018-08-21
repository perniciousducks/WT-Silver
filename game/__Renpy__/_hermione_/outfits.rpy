label __init_variables:

    # Outfits
    if not hasattr(renpy.store,'hg_maid_OBJ'): #important!
        $ hg_maid_OBJ = hermione_outfit()
    $ hg_maid_OBJ.name = "Maid"
    $ hg_maid_OBJ.cost = 250
    $ hg_maid_OBJ.type = "outfit"
    $ hg_maid_OBJ.items = ["outfit","hair","hat","gloves","garter","stockings"]
    $ hg_maid_OBJ.wait_time = 2
    $ hg_maid_OBJ.image = "hg_maid.png"
    $ hg_maid_OBJ.outfit_layers = ["maid_stockings.png","maid_skirt.png","maid_top.png","maid_gloves.png"]
    $ hg_maid_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_maid_OBJ.hair_layer = "B"
    $ hg_maid_OBJ.top_layers = "maid_hat"
    $ hg_maid_OBJ.description = "> A classic Maids Outfit for a classy Witch."

    if not hasattr(renpy.store,'hg_heartDancer_OBJ'):
        $ hg_heartDancer_OBJ = hermione_outfit()
    $ hg_heartDancer_OBJ.name = "Heart Dancer"
    $ hg_heartDancer_OBJ.cost = 80
    $ hg_heartDancer_OBJ.type = "dress"
    $ hg_heartDancer_OBJ.items = ["outfit"]
    $ hg_heartDancer_OBJ.wait_time = 1
    $ hg_heartDancer_OBJ.image = "hg_heart.png"
    $ hg_heartDancer_OBJ.outfit_layers = ["heart_legs.png","heart_top.png","heart_collar.png"]
    $ hg_heartDancer_OBJ.breast_layer = "breasts_normal"
    $ hg_heartDancer_OBJ.description = "> A sexy dancers outfit with heart shaped nipple tassels."

    if not hasattr(renpy.store,'hg_pirate_OBJ'):
        $ hg_pirate_OBJ = hermione_outfit()
    $ hg_pirate_OBJ.name = "Pirate"
    $ hg_pirate_OBJ.cost = 75
    $ hg_pirate_OBJ.type = "outfit"
    $ hg_pirate_OBJ.items = ["outfit"]
    $ hg_pirate_OBJ.wait_time = 1
    $ hg_pirate_OBJ.image = "hg_pirate.png"
    $ hg_pirate_OBJ.outfit_layers = ["pirate_legs.png","pirate_pants.png","pirate_top.png"]
    $ hg_pirate_OBJ.breast_layer = "breasts_nipfix"
    $ hg_pirate_OBJ.description = "> A lightweight Pirates outfit with only room for the\n  necessities Comes with two canon ball storage compartments."

    if not hasattr(renpy.store,'hg_powerGirl_OBJ'):
        $ hg_powerGirl_OBJ = hermione_outfit()
    $ hg_powerGirl_OBJ.name = "Power Girl"
    $ hg_powerGirl_OBJ.cost = 350
    $ hg_powerGirl_OBJ.type = "costume"
    $ hg_powerGirl_OBJ.items = ["outfit"]
    $ hg_powerGirl_OBJ.wait_time = 3
    $ hg_powerGirl_OBJ.image = "hg_power.png"
    $ hg_powerGirl_OBJ.outfit_layers = ["power_cape.png","power_top.png","power_cape_top.png","power_gloves.png","power_belt.png"]
    $ hg_powerGirl_OBJ.breast_layer = "breasts_normal"
    $ hg_powerGirl_OBJ.hair_layer = "P"
    $ hg_powerGirl_OBJ.description = "> An outfit for when you feel extra heroic\n  \"Sometimes it takes balls to be a woman\"."

    if not hasattr(renpy.store,'hg_msMarvel_OBJ'):
        $ hg_msMarvel_OBJ = hermione_outfit()
    $ hg_msMarvel_OBJ.name = "Mrs Marvel"
    $ hg_msMarvel_OBJ.cost = 250
    $ hg_msMarvel_OBJ.type = "costume"
    $ hg_msMarvel_OBJ.items = ["outfit"]
    $ hg_msMarvel_OBJ.wait_time = 2
    $ hg_msMarvel_OBJ.image = "hg_marvel.png"
    $ hg_msMarvel_OBJ.outfit_layers = ["marvel_pants.png","marvel_top.png","marvel_sash.png","marvel_gloves.png"]
    $ hg_msMarvel_OBJ.breast_layer = "breasts_normal"
    $ hg_msMarvel_OBJ.description = "> For the girl that likes the lightningbolt\n  better on the chest than the forehead."

    if not hasattr(renpy.store,'hg_harleyQuinn_OBJ'):
        $ hg_harleyQuinn_OBJ = hermione_outfit()
    $ hg_harleyQuinn_OBJ.name = "Harley Quinn"
    $ hg_harleyQuinn_OBJ.cost = 300
    $ hg_harleyQuinn_OBJ.type = "costume"
    $ hg_harleyQuinn_OBJ.items = ["outfit"]
    $ hg_harleyQuinn_OBJ.wait_time = 3
    $ hg_harleyQuinn_OBJ.image = "hg_harley.png"
    $ hg_harleyQuinn_OBJ.outfit_layers = ["harley_pants.png","harley_top.png","harley_gloves.png","harley_collar.png"]
    $ hg_harleyQuinn_OBJ.breast_layer = "breasts_normal"
    $ hg_harleyQuinn_OBJ.hair_layer = "H"
    $ hg_harleyQuinn_OBJ.description = "> A outfit for when you're actually nuts\n  rather than just crazy for them."

    if not hasattr(renpy.store,'hg_ballDress_OBJ'):
        $ hg_ballDress_OBJ = hermione_outfit()
    $ hg_ballDress_OBJ.name = "Ball Dress"
    $ hg_ballDress_OBJ.cost = 1500
    $ hg_ballDress_OBJ.type = "dress"
    $ hg_ballDress_OBJ.items = ["outfit","hair","neckless","tiara"]
    $ hg_ballDress_OBJ.wait_time = 7
    $ hg_ballDress_OBJ.image = "hg_ball_dress.png"
    $ hg_ballDress_OBJ.outfit_layers = ["ball_dress_skirt.png","ball_dress_top.png"]
    $ hg_ballDress_OBJ.breast_layer = "breasts_nipfix"
    $ hg_ballDress_OBJ.hair_layer = "B"
    $ hg_ballDress_OBJ.top_layers = "tiara"
    $ hg_ballDress_OBJ.description = "> A traditional ball dress complete with a imitation\n  ball-queen tiara."

    if not hasattr(renpy.store,'hg_christmas_OBJ'):
        $ hg_christmas_OBJ = hermione_outfit()
    $ hg_christmas_OBJ.name = "Christmas Girl"
    $ hg_christmas_OBJ.cost = 50
    $ hg_christmas_OBJ.type = "outfit"
    $ hg_christmas_OBJ.items = ["outfit"]
    $ hg_christmas_OBJ.wait_time = 2
    $ hg_christmas_OBJ.image = "hg_christmas.png"
    $ hg_christmas_OBJ.outfit_layers = ["christmas_pants.png","christmas_top.png","christmas_gloves.png","christmas_collar.png"]
    $ hg_christmas_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_christmas_OBJ.top_layers = "antlers"
    $ hg_christmas_OBJ.description = "> A christmas themed outfit complete with tightly wrapped\n  snowglobes."

    if not hasattr(renpy.store,'hg_laraCroft_OBJ'):
        $ hg_laraCroft_OBJ = hermione_outfit()
    $ hg_laraCroft_OBJ.name = "Lara Croft"
    $ hg_laraCroft_OBJ.cost = 270
    $ hg_laraCroft_OBJ.type = "costume"
    $ hg_laraCroft_OBJ.items = ["outfit","gloves"]
    $ hg_laraCroft_OBJ.wait_time = 2
    $ hg_laraCroft_OBJ.image = "hg_lara.png"
    $ hg_laraCroft_OBJ.outfit_layers = ["lara_pants.png","lara_top.png","lara_gloves.png"]
    $ hg_laraCroft_OBJ.breast_layer = "breasts_normal"
    $ hg_laraCroft_OBJ.description = "> An outfit perfectly suited for exploring deep, dark\n  and moist caverns."

    if not hasattr(renpy.store,'hg_tifa_OBJ'):
        $ hg_tifa_OBJ = hermione_outfit()
    $ hg_tifa_OBJ.name = "Tifa"
    $ hg_tifa_OBJ.cost = 220
    $ hg_tifa_OBJ.type = "costume"
    $ hg_tifa_OBJ.items = ["outfit"]
    $ hg_tifa_OBJ.wait_time = 2
    $ hg_tifa_OBJ.image = "hg_tifa.png"
    $ hg_tifa_OBJ.outfit_layers = ["tifa_pants.png","tifa_top.png","tifa_gloves.png","tifa_ear.png"]
    $ hg_tifa_OBJ.breast_layer = "breasts_normal"
    $ hg_tifa_OBJ.hair_layer = "T"
    $ hg_tifa_OBJ.description = "> An outfit for when when your sexual fantasies\n  are just getting started."

    if not hasattr(renpy.store,'hg_present_OBJ'):
        $ hg_present_OBJ = hermione_outfit()
    $ hg_present_OBJ.name = "Present"
    $ hg_present_OBJ.cost = 35
    $ hg_present_OBJ.type = "outfit"
    $ hg_present_OBJ.items = ["outfit"]
    $ hg_present_OBJ.wait_time = 1
    $ hg_present_OBJ.image = "hg_present.png"
    $ hg_present_OBJ.outfit_layers = ["present_pant.png","present_top.png"]
    $ hg_present_OBJ.breast_layer = "breasts_nipfix"
    $ hg_present_OBJ.description = "> A tightly wrapped gift, scissors not included."

    if not hasattr(renpy.store,'hg_japan_OBJ'):
        $ hg_japan_OBJ = hermione_outfit()
    $ hg_japan_OBJ.name = "Japanese Schoolgirl"
    $ hg_japan_OBJ.cost = 125
    $ hg_japan_OBJ.type = "outfit"
    $ hg_japan_OBJ.items = ["outfit"]
    $ hg_japan_OBJ.wait_time = 2
    $ hg_japan_OBJ.image = "hg_japan.png"
    $ hg_japan_OBJ.outfit_layers = ["japan_pant.png","japan_top.png"]
    $ hg_japan_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_japan_OBJ.description = "> A schoolgirl outfit traditionally worn in Japan."

    if not hasattr(renpy.store,'hg_witch_OBJ'):
        $ hg_witch_OBJ = hermione_outfit()
    $ hg_witch_OBJ.name = "Witch outfit"
    $ hg_witch_OBJ.cost = 250
    $ hg_witch_OBJ.type = "outfit"
    $ hg_witch_OBJ.items = ["outfit","hat"]
    $ hg_witch_OBJ.wait_time = 3
    $ hg_witch_OBJ.image = "hg_witch.png"
    $ hg_witch_OBJ.outfit_layers = ["witch_stockings.png","witch_top.png","witch_cloak.png"]
    $ hg_witch_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_witch_OBJ.top_layers = "witch_hat"
    $ hg_witch_OBJ.description = "> Release your inner witch with this halloween\n  inspired outfit."

    if not hasattr(renpy.store,'hg_bio_OBJ'):
        $ hg_bio_OBJ = hermione_outfit()
    $ hg_bio_OBJ.name = "Bioshock outfit"
    $ hg_bio_OBJ.cost = 400
    $ hg_bio_OBJ.type = "outfit"
    $ hg_bio_OBJ.items = ["outfit","hair","choker"]
    $ hg_bio_OBJ.wait_time = 3
    $ hg_bio_OBJ.image = "hg_bio.png"
    $ hg_bio_OBJ.outfit_layers = ["bio_skirt.png","bio_chocker.png","bio_corset.png","bio_jacket.png"]
    $ hg_bio_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_bio_OBJ.hair_layer = "E"
    $ hg_bio_OBJ.description = "> Flick some coins for this Bioshock inspired outfit."

    if not hasattr(renpy.store,'hg_yenn_OBJ'):
        $ hg_yenn_OBJ = hermione_outfit()
    $ hg_yenn_OBJ.name = "Yennefer's costume"
    $ hg_yenn_OBJ.cost = 500
    $ hg_yenn_OBJ.type = "outfit"
    $ hg_yenn_OBJ.items = ["outfit","scarf","choker","stockings"]
    $ hg_yenn_OBJ.wait_time = 3
    $ hg_yenn_OBJ.image = "hg_yenn.png"
    $ hg_yenn_OBJ.outfit_layers = ["yenn_stockings.png","yenn_pant.png","yenn_skirt.png","yenn_top.png","yenn_gloves.png","yenn_chocker.png","yenn_scarf.png","yenn_belt.png"]
    $ hg_yenn_OBJ.breast_layer = "breasts_normal"
    $ hg_yenn_OBJ.description = "> A Witcher inspired outfit to fit even the most\n  perverted witch"

    $ hermione_outfits_list = []
    $ hermione_outfits_list.append(hg_maid_OBJ)
    $ hermione_outfits_list.append(hg_heartDancer_OBJ)
    $ hermione_outfits_list.append(hg_ballDress_OBJ)
    $ hermione_outfits_list.append(hg_pirate_OBJ)
    $ hermione_outfits_list.append(hg_powerGirl_OBJ)
    $ hermione_outfits_list.append(hg_msMarvel_OBJ)
    $ hermione_outfits_list.append(hg_harleyQuinn_OBJ)
    $ hermione_outfits_list.append(hg_christmas_OBJ)
    $ hermione_outfits_list.append(hg_laraCroft_OBJ)
    $ hermione_outfits_list.append(hg_tifa_OBJ)
    $ hermione_outfits_list.append(hg_present_OBJ)
    $ hermione_outfits_list.append(hg_japan_OBJ)
    $ hermione_outfits_list.append(hg_witch_OBJ)
    $ hermione_outfits_list.append(hg_bio_OBJ)
    $ hermione_outfits_list.append(hg_yenn_OBJ)



    # Astoria
    if not hasattr(renpy.store,'ag_ball_dress_OBJ'):
        $ ag_ball_dress_OBJ = hermione_outfit()
    $ ag_ball_dress_OBJ.name = "Ball Dress"
    $ ag_ball_dress_OBJ.cost = 300
    $ ag_ball_dress_OBJ.type = "dress"
    $ ag_ball_dress_OBJ.items = ["outfit"]
    $ ag_ball_dress_OBJ.wait_time = 4
    $ ag_ball_dress_OBJ.image = "ag_ball_dress.png"
    $ ag_ball_dress_OBJ.outfit_layers = ["ball_dress.png"]
    $ ag_ball_dress_OBJ.description = "> A cute dress for your favourite princess!"

    if not hasattr(renpy.store,'ag_lazy_OBJ'):
        $ ag_lazy_OBJ = hermione_outfit()
    $ ag_lazy_OBJ.name = "Lazy Town Outfit"
    $ ag_lazy_OBJ.cost = 120
    $ ag_lazy_OBJ.type = "costume"
    $ ag_lazy_OBJ.items = ["outfit","hair","bracelet"]
    $ ag_lazy_OBJ.wait_time = 1
    $ ag_lazy_OBJ.image = "ag_lazy.png"
    $ ag_lazy_OBJ.outfit_layers = ["lazy_tights.png","lazy_dress.png","lazy_bracelet.png"]
    $ ag_lazy_OBJ.hair_layer = "L"
    $ ag_lazy_OBJ.description = "> Nobody is lazy at Hogwarts!"

    if not hasattr(renpy.store,'ag_lazy_short_OBJ'): #Not a store item!
        $ ag_lazy_short_OBJ = hermione_outfit()
    $ ag_lazy_short_OBJ.name = "Short Lazy Town Outfit"
    $ ag_lazy_short_OBJ.unlockable = True
    #$ ag_lazy_short_OBJ.cost = 120
    $ ag_lazy_short_OBJ.type = "costume"
    $ ag_lazy_short_OBJ.items = ["outfit","hair","bracelet"]
    $ ag_lazy_short_OBJ.wait_time = 1
    $ ag_lazy_short_OBJ.image = "ag_lazy_short.png"
    $ ag_lazy_short_OBJ.outfit_layers = ["lazy_tights.png","lazy_dress_short.png","lazy_bracelet.png"]
    $ ag_lazy_short_OBJ.hair_layer = "L"
    $ ag_lazy_short_OBJ.description = "> Nobody is lazy at Hogwarts!"

    $ astoria_outfits_list = []
    $ astoria_outfits_list.append(ag_ball_dress_OBJ)
    $ astoria_outfits_list.append(ag_lazy_OBJ)
    $ astoria_outfits_list.append(ag_lazy_short_OBJ)


    if not hasattr(renpy.store,'astoria_outfit_GLBL'):
        $ hermoine_outfit_GLBL = None
        $ astoria_outfit_GLBL = None
        $ susan_outfit_GLBL = None
        $ cho_outfit_GLBL = None
        $ luna_outfit_GLBL = None


    return






label set_defined_menu_vars:
    python:
        tmp_list_a = []
        tmp_list_b = []
        for i in range(0,hermione_defined_outfit_list_size):
            if hermione_outfit_names[i] not in ["null",""]:
                tmp_list_a.append(hermione_outfit_names[i])
                tmp_list_b.append(i)

        h_menu_list = [[0 for i in xrange(2)] for i in xrange(len(tmp_list_a)+1)]
        for i in range(0,len(tmp_list_a)):
            h_menu_list[i][0] = tmp_list_a[i]
            h_menu_list[i][1] = tmp_list_b[i]
        h_menu_list[len(h_menu_list)-1][0] = "-nevermind-"
        h_menu_list[len(h_menu_list)-1][1] = -1
    return




init python:
    class outfit_list(list):
        list = []

    class hermione_outfit(object):
        name = ""
        unlockable = False
        unlocked = False
        cost = 0
        type = "outfit"
        items = ["outfit"]
        wait_time = 0 #the ammount of time to wait until compleded from clothes store
        top_layers = []
        outfit_layers = []
        actions = []
        action_images = []
        hair_layer = ""
        breast_layer = "breasts_nipfix"
        image = ""
        description = ""


        def getMenuText(self):
            return "-"+self.name+"-"
        def getOutfitLayers(self):
            return self.outfit_layers
        def getHairLayers(self):
            return self.hair_layer
        def getTopLayers(self):
            return self.top_layers
        def getActionImage(self, action):
            return self.action_images[self.actions.index(action)]

        def getStoreName(self):
            return self.name
        def getImage(self):
            return self.image
        def getStoreImage(self):
            return "interface/icons/outfit/"+self.image
        def getStoreCost(self):
            return "Cost: "+str(self.cost)+" gold"
        def getStoreWaitTime(self):
            return "Wait Time: "+str(self.wait_time)+" days."
        def getStoreDescription(self):
            return self.description

        def getType(self):
            return self.type
        def getStoreItems(self):
            return self.items
