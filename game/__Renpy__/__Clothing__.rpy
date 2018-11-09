

label clothing_init:

    ### OUTFITS ###

    #Hermione Outfits.
    if not hasattr(renpy.store,'hg_outfit_maid_OBJ'): #important!
        $ hg_outfit_maid_OBJ = outfit_class()
    $ hg_outfit_maid_OBJ.id = "hg_outfit_maid"
    $ hg_outfit_maid_OBJ.image = "hg_maid.png"
    $ hg_outfit_maid_OBJ.outfit_layers = ["maid_stockings.png","maid_skirt.png","maid_top.png","maid_gloves.png"]
    $ hg_outfit_maid_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_outfit_maid_OBJ.hair_layer = "B"
    $ hg_outfit_maid_OBJ.top_layers = "maid_hat"

    if not hasattr(renpy.store,'hg_outfit_pirate_OBJ'):
        $ hg_outfit_pirate_OBJ = outfit_class()
    $ hg_outfit_pirate_OBJ.id = "hg_outfit_pirate"
    $ hg_outfit_pirate_OBJ.image = "hg_pirate.png"
    $ hg_outfit_pirate_OBJ.outfit_layers = ["pirate_legs.png","pirate_pants.png","pirate_top.png"]
    $ hg_outfit_pirate_OBJ.breast_layer = "breasts_nipfix"

    if not hasattr(renpy.store,'hg_outfit_christmas_OBJ'):
        $ hg_outfit_christmas_OBJ = outfit_class()
    $ hg_outfit_christmas_OBJ.id = "hg_outfit_christmas"
    $ hg_outfit_christmas_OBJ.image = "hg_christmas.png"
    $ hg_outfit_christmas_OBJ.outfit_layers = ["christmas_pants.png","christmas_top.png","christmas_gloves.png","christmas_collar.png"]
    $ hg_outfit_christmas_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_outfit_christmas_OBJ.top_layers = "antlers"

    if not hasattr(renpy.store,'hg_outfit_present_OBJ'):
        $ hg_outfit_present_OBJ = outfit_class()
    $ hg_outfit_present_OBJ.id = "hg_outfit_present"
    $ hg_outfit_present_OBJ.image = "hg_present.png"
    $ hg_outfit_present_OBJ.outfit_layers = ["present_pant.png","present_top.png"]
    $ hg_outfit_present_OBJ.breast_layer = "breasts_nipfix"

    if not hasattr(renpy.store,'hg_outfit_japan_OBJ'):
        $ hg_outfit_japan_OBJ = outfit_class()
    $ hg_outfit_japan_OBJ.id = "hg_outfit_japan"
    $ hg_outfit_japan_OBJ.image = "hg_japan.png"
    $ hg_outfit_japan_OBJ.outfit_layers = ["japan_pant.png","japan_top.png"]
    $ hg_outfit_japan_OBJ.breast_layer = "breasts_normal_pressed"

    if not hasattr(renpy.store,'hg_outfit_witch_OBJ'):
        $ hg_outfit_witch_OBJ = outfit_class()
    $ hg_outfit_witch_OBJ.id = "hg_outfit_witch"
    $ hg_outfit_witch_OBJ.image = "hg_witch.png"
    $ hg_outfit_witch_OBJ.outfit_layers = ["witch_stockings.png","witch_top.png","witch_cloak.png"]
    $ hg_outfit_witch_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_outfit_witch_OBJ.top_layers = "witch_hat"

    if not hasattr(renpy.store,'hg_outfit_egypt_OBJ'):
        $ hg_outfit_egypt_OBJ = outfit_class()
    $ hg_outfit_egypt_OBJ.id = "hg_outfit_egypt"
    $ hg_outfit_egypt_OBJ.image = "hg_egypt.png"
    $ hg_outfit_egypt_OBJ.outfit_layers = ["egyptian_top.png","egyptian_bottom.png","egyptian_shackles.png"]
    $ hg_outfit_egypt_OBJ.breast_layer = "breasts_normal"


    #Hermione Costumes.
    if not hasattr(renpy.store,'hg_costume_power_girl_OBJ'):
        $ hg_costume_power_girl_OBJ = outfit_class()
    $ hg_costume_power_girl_OBJ.id = "hg_costume_power_girl"
    $ hg_costume_power_girl_OBJ.image = "hg_power.png"
    $ hg_costume_power_girl_OBJ.outfit_layers = ["power_cape.png","power_top.png","power_cape_top.png","power_gloves.png","power_belt.png"]
    $ hg_costume_power_girl_OBJ.breast_layer = "breasts_normal"
    $ hg_costume_power_girl_OBJ.hair_layer = "P"

    if not hasattr(renpy.store,'hg_costume_ms_marvel_OBJ'):
        $ hg_costume_ms_marvel_OBJ = outfit_class()
    $ hg_costume_ms_marvel_OBJ.id = "hg_costume_ms_marvel"
    $ hg_costume_ms_marvel_OBJ.image = "hg_marvel.png"
    $ hg_costume_ms_marvel_OBJ.outfit_layers = ["marvel_pants.png","marvel_top.png","marvel_sash.png","marvel_gloves.png"]
    $ hg_costume_ms_marvel_OBJ.breast_layer = "breasts_normal"

    if not hasattr(renpy.store,'hg_costume_harley_quinn_OBJ'):
        $ hg_costume_harley_quinn_OBJ = outfit_class()
    $ hg_costume_harley_quinn_OBJ.id = "hg_costume_harley_quinn"
    $ hg_costume_harley_quinn_OBJ.image = "hg_harley.png"
    $ hg_costume_harley_quinn_OBJ.outfit_layers = ["harley_pants.png","harley_top.png","harley_gloves.png","harley_collar.png"]
    $ hg_costume_harley_quinn_OBJ.breast_layer = "breasts_normal"
    $ hg_costume_harley_quinn_OBJ.hair_layer = "H"

    if not hasattr(renpy.store,'hg_costume_lara_croft_OBJ'):
        $ hg_costume_lara_croft_OBJ = outfit_class()
    $ hg_costume_lara_croft_OBJ.id = "hg_costume_lara_croft"
    $ hg_costume_lara_croft_OBJ.image = "hg_lara.png"
    $ hg_costume_lara_croft_OBJ.outfit_layers = ["lara_pants.png","lara_top.png","lara_gloves.png"]
    $ hg_costume_lara_croft_OBJ.breast_layer = "breasts_normal"

    if not hasattr(renpy.store,'hg_costume_tifa_OBJ'):
        $ hg_costume_tifa_OBJ = outfit_class()
    $ hg_costume_tifa_OBJ.id = "hg_costume_tifa"
    $ hg_costume_tifa_OBJ.image = "hg_tifa.png"
    $ hg_costume_tifa_OBJ.outfit_layers = ["tifa_pants.png","tifa_top.png","tifa_gloves.png","tifa_ear.png"]
    $ hg_costume_tifa_OBJ.breast_layer = "breasts_normal"
    $ hg_costume_tifa_OBJ.hair_layer = "T"

    if not hasattr(renpy.store,'hg_costume_elizabeth_OBJ'):
        $ hg_costume_elizabeth_OBJ = outfit_class()
    $ hg_costume_elizabeth_OBJ.id = "hg_costume_elizabeth"
    $ hg_costume_elizabeth_OBJ.image = "hg_bio.png"
    $ hg_costume_elizabeth_OBJ.outfit_layers = ["bio_skirt.png","bio_chocker.png","bio_corset.png","bio_jacket.png"]
    $ hg_costume_elizabeth_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_costume_elizabeth_OBJ.hair_layer = "E"

    if not hasattr(renpy.store,'hg_costume_yennefer_OBJ'):
        $ hg_costume_yennefer_OBJ = outfit_class()
    $ hg_costume_yennefer_OBJ.id = "hg_costume_yennefer"
    $ hg_costume_yennefer_OBJ.image = "hg_yenn.png"
    $ hg_costume_yennefer_OBJ.outfit_layers = ["yenn_stockings.png","yenn_pant.png","yenn_skirt.png","yenn_top.png","yenn_gloves.png","yenn_chocker.png","yenn_scarf.png","yenn_belt.png"]
    $ hg_costume_yennefer_OBJ.breast_layer = "breasts_normal"


    #Hermione Dresses.
    if not hasattr(renpy.store,'hg_dress_yule_ball_OBJ'):
        $ hg_dress_yule_ball_OBJ = outfit_class()
    $ hg_dress_yule_ball_OBJ.id = "hg_dress_yule_ball"
    $ hg_dress_yule_ball_OBJ.image = "hg_ball_dress.png"
    $ hg_dress_yule_ball_OBJ.outfit_layers = ["ball_dress_skirt.png","ball_dress_top.png"]
    $ hg_dress_yule_ball_OBJ.breast_layer = "breasts_nipfix"
    $ hg_dress_yule_ball_OBJ.hair_layer = "B"
    $ hg_dress_yule_ball_OBJ.top_layers = "tiara"

    if not hasattr(renpy.store,'hg_dress_dancer_OBJ'):
        $ hg_dress_dancer_OBJ = outfit_class()
    $ hg_dress_dancer_OBJ.id = "hg_dress_dancer"
    $ hg_dress_dancer_OBJ.image = "hg_heart.png"
    $ hg_dress_dancer_OBJ.outfit_layers = ["heart_legs.png","heart_top.png","heart_collar.png"]
    $ hg_dress_dancer_OBJ.breast_layer = "breasts_normal"

    #Event Costumes.
    #Does not have a store item!
    if not hasattr(renpy.store,'hg_standart_school_OBJ'): #important!
        $ hg_standart_school_OBJ = outfit_class()
    $ hg_standart_school_OBJ.id = "hg_standart_school"
    $ hg_standart_school_OBJ.outfit_layers = ["../uniform/skirt_2.png", "../uniform/top_1.png"]
    $ hg_standart_school_OBJ.breast_layer = "breasts_nipfix"

    if not hasattr(renpy.store,'hg_standart_school_noshirt_OBJ'): #important!
        $ hg_standart_school_noshirt_OBJ = outfit_class()
    $ hg_standart_school_noshirt_OBJ.id = "hg_standart_school_noshirt"
    $ hg_standart_school_noshirt_OBJ.outfit_layers = ["../uniform/skirt_2.png", "../underwear/base/bra_base.png"]
    $ hg_standart_school_noshirt_OBJ.breast_layer = "breasts_nipfix"



    # Luna Outfits

    #ADD


    # Astoria
    if not hasattr(renpy.store,'ag_costume_lazy_town_OBJ'):
        $ ag_costume_lazy_town_OBJ = outfit_class()
    $ ag_costume_lazy_town_OBJ.id = "ag_costume_lazy_town"
    $ ag_costume_lazy_town_OBJ.image = "ag_lazy.png"
    $ ag_costume_lazy_town_OBJ.outfit_layers = ["lazy_tights.png","lazy_dress.png","lazy_bracelet.png"]
    $ ag_costume_lazy_town_OBJ.hair_layer = "L"

    if not hasattr(renpy.store,'ag_costume_lazy_town_short_OBJ'): #Not a store OBJ!
        $ ag_costume_lazy_town_short_OBJ = outfit_class()
    $ ag_costume_lazy_town_short_OBJ.id = "ag_costume_lazy_town_short"
    $ ag_costume_lazy_town_short_OBJ.image = "ag_lazy_short.png"
    $ ag_costume_lazy_town_short_OBJ.outfit_layers = ["lazy_tights.png","lazy_dress_short.png","lazy_bracelet.png"]
    $ ag_costume_lazy_town_short_OBJ.hair_layer = "L"

    if not hasattr(renpy.store,'ag_dress_yule_ball_OBJ'):
        $ ag_dress_yule_ball_OBJ = outfit_class()
    $ ag_dress_yule_ball_OBJ.id = "ag_dress_yule_ball"
    $ ag_dress_yule_ball_OBJ.image = "ag_ball_dress.png"
    $ ag_dress_yule_ball_OBJ.outfit_layers = ["ball_dress.png"]


    # Susan Outfits

    #ADD


    # Cho Outfits
    if not hasattr(renpy.store,'cc_outfit_quidditch_OBJ'):
        $ cc_outfit_quidditch_OBJ = outfit_class()
    $ cc_outfit_quidditch_OBJ.id = "cc_outfit_quidditch"
    $ cc_outfit_quidditch_OBJ.image = "cc_quidditch.png"
    $ cc_outfit_quidditch_OBJ.outfit_layers = []
    call update_cho_quidditch_outfit #Adds outfit layers.

    if not hasattr(renpy.store,'cc_dress_traditional_OBJ'):
        $ cc_dress_traditional_OBJ = outfit_class()
    $ cc_dress_traditional_OBJ.id = "cc_dress_traditional"
    $ cc_dress_traditional_OBJ.image = "cc_traditional_dress.png"
    $ cc_dress_traditional_OBJ.outfit_layers = ["traditional_dress.png"]

    return



init python:

    class outfit_class(object):
        id = ""
        top_layers = []
        outfit_layers = []
        actions = []
        action_images = []
        hair_layer = ""
        breast_layer = "breasts_nipfix"
        image = ""

        def getOutfitLayers(self):
            return self.outfit_layers
        def getHairLayers(self):
            return self.hair_layer
        def getTopLayers(self):
            return self.top_layers
        def getActionImage(self, action):
            return self.action_images[self.actions.index(action)]

        def getImage(self):
            return self.image
        def getStoreImage(self):
            return "interface/icons/outfit/"+self.image
