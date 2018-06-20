label __init_variables:
    if not hasattr(renpy.store,'hg_maid_OBJ'): #important!
        $ hg_maid_OBJ = hermione_outfit()
    $ hg_maid_OBJ.name = "Maid"
    $ hg_maid_OBJ.cost = 100
    $ hg_maid_OBJ.wait_time = 2
    $ hg_maid_OBJ.store_image = "maid.png"
    $ hg_maid_OBJ.outfit_layers = []
    $ hg_maid_OBJ.outfit_layers.extend(("maid_stockings.png","maid_skirt.png","maid_top.png","maid_gloves.png"))
    $ hg_maid_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_maid_OBJ.top_layers = []
    $ hg_maid_OBJ.top_layers.append("maid_hat.png")
    
    if not hasattr(renpy.store,'hg_gryffCheer_OBJ'):
        $ hg_gryffCheer_OBJ = hermione_outfit()
    $ hg_gryffCheer_OBJ.name = "Griffindor Cheerleader"
    $ hg_gryffCheer_OBJ.cost = 200
    $ hg_gryffCheer_OBJ.wait_time = 3
    $ hg_gryffCheer_OBJ.store_image = "cheer.png"
    $ hg_gryffCheer_OBJ.outfit_layers = []
    $ hg_gryffCheer_OBJ.outfit_layers.extend(("cheer_stockings.png","cheer_pants.png","cheer_top.png"))
    $ hg_gryffCheer_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_gryffCheer_OBJ.actions = []
    $ hg_gryffCheer_OBJ.action_images = []
    $ hg_gryffCheer_OBJ.actions.append("lift_top")
    $ hg_gryffCheer_OBJ.action_images.append("cherr_flash.png")
    
    if not hasattr(renpy.store,'hg_slythCheer_OBJ'):
        $ hg_slythCheer_OBJ = hermione_outfit()
    $ hg_slythCheer_OBJ.name = "Slythrin Cheerleader"
    $ hg_slythCheer_OBJ.cost = 200
    $ hg_slythCheer_OBJ.wait_time = 3
    $ hg_slythCheer_OBJ.store_image = "s_cheer.png"
    $ hg_slythCheer_OBJ.outfit_layers = []
    $ hg_slythCheer_OBJ.outfit_layers.extend(("s_cheer_stockings.png","s_cheer_pants.png","s_cheer_top.png"))
    $ hg_slythCheer_OBJ.breast_layer = "breasts_normal_pressed"
    $ hg_slythCheer_OBJ.actions = []
    $ hg_slythCheer_OBJ.action_images = []
    $ hg_slythCheer_OBJ.actions.append("lift_top")
    $ hg_slythCheer_OBJ.action_images.append("cherr_flash.png")
    
    if not hasattr(renpy.store,'hg_heartDancer_OBJ'):
        $ hg_heartDancer_OBJ = hermione_outfit()
    $ hg_heartDancer_OBJ.name = "Heart Dancer"
    $ hg_heartDancer_OBJ.cost = 300
    $ hg_heartDancer_OBJ.wait_time = 4
    $ hg_heartDancer_OBJ.store_image = "heart.png"
    $ hg_heartDancer_OBJ.outfit_layers = []
    $ hg_heartDancer_OBJ.outfit_layers.extend(("heart_legs.png","heart_top.png","heart_collar.png"))
    $ hg_heartDancer_OBJ.breast_layer = "breasts_normal"
    
    if not hasattr(renpy.store,'hg_silkNightgown_OBJ'):
        $ hg_silkNightgown_OBJ = hermione_outfit()
    $ hg_silkNightgown_OBJ.name = "Silk Nightgown"
    $ hg_silkNightgown_OBJ.cost = 140
    $ hg_silkNightgown_OBJ.wait_time = 2
    $ hg_silkNightgown_OBJ.store_image = "nightgown.png"
    $ hg_silkNightgown_OBJ.outfit_layers = []
    $ hg_silkNightgown_OBJ.outfit_layers.append("silk_nightgown.png")
    $ hg_silkNightgown_OBJ.breast_layer = "breasts_normal"
    
    if not hasattr(renpy.store,'hg_pirate_OBJ'):
        $ hg_pirate_OBJ = hermione_outfit()
    $ hg_pirate_OBJ.name = "Pirate"
    $ hg_pirate_OBJ.cost = 75
    $ hg_pirate_OBJ.wait_time = 2
    $ hg_pirate_OBJ.store_image = "pirate.png"
    $ hg_pirate_OBJ.outfit_layers = []
    $ hg_pirate_OBJ.outfit_layers.extend(("pirate_legs.png","pirate_pants.png","pirate_top.png"))
    $ hg_pirate_OBJ.breast_layer = "breasts_nipfix"
    
    if not hasattr(renpy.store,'hg_powerGirl_OBJ'):
        $ hg_powerGirl_OBJ = hermione_outfit()
    $ hg_powerGirl_OBJ.name = "Power Girl"
    $ hg_powerGirl_OBJ.cost = 350
    $ hg_powerGirl_OBJ.wait_time = 3
    $ hg_powerGirl_OBJ.store_image = "power.png"
    $ hg_powerGirl_OBJ.outfit_layers = []
    $ hg_powerGirl_OBJ.outfit_layers.extend(("power_cape.png","power_top.png","power_gloves.png","power_belt.png"))
    $ hg_powerGirl_OBJ.breast_layer = "breasts_normal"
    $ hg_powerGirl_OBJ.hair_layer = "power_hair"
    
    if not hasattr(renpy.store,'hg_msMarvel_OBJ'):
        $ hg_msMarvel_OBJ = hermione_outfit()
    $ hg_msMarvel_OBJ.name = "Mrs Marvel"
    $ hg_msMarvel_OBJ.cost = 250
    $ hg_msMarvel_OBJ.wait_time = 5
    $ hg_msMarvel_OBJ.store_image = "marvel.png"
    $ hg_msMarvel_OBJ.outfit_layers = []
    $ hg_msMarvel_OBJ.outfit_layers.extend(("marvel_pants.png","marvel_top.png","marvel_sash.png","marvel_gloves.png"))
    $ hg_msMarvel_OBJ.breast_layer = "breasts_normal"
    
    if not hasattr(renpy.store,'hg_harleyQuinn_OBJ'):
        $ hg_harleyQuinn_OBJ = hermione_outfit()
    $ hg_harleyQuinn_OBJ.name = "Harley Quinn"
    $ hg_harleyQuinn_OBJ.cost = 300
    $ hg_harleyQuinn_OBJ.wait_time = 4
    $ hg_harleyQuinn_OBJ.store_image = "harley.png"
    $ hg_harleyQuinn_OBJ.outfit_layers = []
    $ hg_harleyQuinn_OBJ.outfit_layers.extend(("harley_pants.png","harley_top.png","harley_gloves.png","harley_collar.png"))
    $ hg_harleyQuinn_OBJ.breast_layer = "breasts_normal"
    $ hg_harleyQuinn_OBJ.hair_layer = "harley_hair"
    
    if not hasattr(renpy.store,'hg_ballDress_OBJ'):
        $ hg_ballDress_OBJ = hermione_outfit()
    $ hg_ballDress_OBJ.name = "Ball Dress"
    $ hg_ballDress_OBJ.cost = 1500
    $ hg_ballDress_OBJ.wait_time = 7
    $ hg_ballDress_OBJ.store_image = "ball_dress.png"
    $ hg_ballDress_OBJ.outfit_layers = []
    $ hg_ballDress_OBJ.outfit_layers.extend(("ball_dress_skirt.png","ball_dress_top.png"))
    $ hg_ballDress_OBJ.breast_layer = "breasts_nipfix"
    
    if not hasattr(renpy.store,'hg_christmas_OBJ'):
        $ hg_christmas_OBJ = hermione_outfit()
    $ hg_christmas_OBJ.name = "Christmas Girl"
    $ hg_christmas_OBJ.cost = 50
    $ hg_christmas_OBJ.wait_time = 2
    $ hg_christmas_OBJ.store_image = "christmas.png"
    $ hg_christmas_OBJ.outfit_layers = []
    $ hg_christmas_OBJ.outfit_layers.extend(("christmas_pants.png","christmas_top.png","christmas_gloves.png","christmas_collar.png"))
    $ hg_christmas_OBJ.top_layers = []
    $ hg_christmas_OBJ.top_layers.append("christmas_antlers.png")
    $ hg_christmas_OBJ.breast_layer = "breasts_normal_pressed"
    
    if not hasattr(renpy.store,'hg_laraCroft_OBJ'):
        $ hg_laraCroft_OBJ = hermione_outfit()
    $ hg_laraCroft_OBJ.name = "Lara Croft"
    $ hg_laraCroft_OBJ.cost = 270
    $ hg_laraCroft_OBJ.wait_time = 2
    $ hg_laraCroft_OBJ.store_image = "lara.png"
    $ hg_laraCroft_OBJ.outfit_layers = []
    $ hg_laraCroft_OBJ.outfit_layers.extend(("lara_pants.png","lara_top.png","lara_gloves.png"))
    $ hg_laraCroft_OBJ.breast_layer = "breasts_normal"

    if not hasattr(renpy.store,'hg_tifa_OBJ'):
        $ hg_tifa_OBJ = hermione_outfit()
    $ hg_tifa_OBJ.name = "Tifa"
    $ hg_tifa_OBJ.cost = 220
    $ hg_tifa_OBJ.wait_time = 2
    $ hg_tifa_OBJ.store_image = "tifa.png"
    $ hg_tifa_OBJ.outfit_layers = []
    $ hg_tifa_OBJ.outfit_layers.extend(("tifa_pants.png","tifa_top.png","tifa_gloves.png","tifa_ear.png"))
    $ hg_tifa_OBJ.breast_layer = "breasts_normal"
    $ hg_tifa_OBJ.hair_layer = "tifa_hair"

    if not hasattr(renpy.store,'hg_rocker_OBJ'):
        $ hg_rocker_OBJ = hermione_outfit()
    $ hg_rocker_OBJ.name = "Rocker"
    $ hg_rocker_OBJ.cost = 85
    $ hg_rocker_OBJ.wait_time = 1
    $ hg_rocker_OBJ.store_image = "rocker.png"
    $ hg_rocker_OBJ.outfit_layers = []
    $ hg_rocker_OBJ.outfit_layers.extend(("rocker_skirt.png","rocker_top.png","rocker_band.png"))
    $ hg_rocker_OBJ.breast_layer = "breasts_normal"

    if not hasattr(renpy.store,'hg_present_OBJ'):
        $ hg_present_OBJ = hermione_outfit()
    $ hg_present_OBJ.name = "Present"
    $ hg_present_OBJ.cost = 35
    $ hg_present_OBJ.wait_time = 1
    $ hg_present_OBJ.store_image = "present.png"
    $ hg_present_OBJ.outfit_layers = []
    $ hg_present_OBJ.outfit_layers.extend(("present_pant.png","present_top.png"))
    $ hg_present_OBJ.breast_layer = "breasts_nipfix"

    if not hasattr(renpy.store,'hg_japan_OBJ'):
        $ hg_japan_OBJ = hermione_outfit()
    $ hg_japan_OBJ.name = "Japanese Schoolgirl"
    $ hg_japan_OBJ.cost = 125
    $ hg_japan_OBJ.wait_time = 2
    $ hg_japan_OBJ.store_image = "japan.png"
    $ hg_japan_OBJ.outfit_layers = []
    $ hg_japan_OBJ.outfit_layers.extend(("japan_pant.png","japan_top.png"))
    $ hg_japan_OBJ.breast_layer = "breasts_normal_pressed"

    if not hasattr(renpy.store,'hg_witch_OBJ'):
        $ hg_witch_OBJ = hermione_outfit()
    $ hg_witch_OBJ.name = "Witch outfit"
    $ hg_witch_OBJ.cost = 175
    $ hg_witch_OBJ.wait_time = 2
    $ hg_witch_OBJ.store_image = "witch.png"
    $ hg_witch_OBJ.outfit_layers = []
    $ hg_witch_OBJ.outfit_layers.extend(("witch_stockings.png","witch_top.png","witch_cloak.png","witch_hat.png"))
    $ hg_witch_OBJ.breast_layer = "breasts_normal_pressed"

    if not hasattr(renpy.store,'hg_bio_OBJ'):
        $ hg_bio_OBJ = hermione_outfit()
    $ hg_bio_OBJ.name = "Bioshock outfit"
    $ hg_bio_OBJ.cost = 200
    $ hg_bio_OBJ.wait_time = 2
    $ hg_bio_OBJ.store_image = "bio.png"
    $ hg_bio_OBJ.outfit_layers = []
    $ hg_bio_OBJ.outfit_layers.extend(("bio_skirt.png","bio_chocker.png","bio_jacket.png","bio_corset.png"))
    $ hg_bio_OBJ.breast_layer = "breasts_normal_pressed"

    if not hasattr(renpy.store,'hg_yenn_OBJ'):
        $ hg_yenn_OBJ = hermione_outfit()
    $ hg_yenn_OBJ.name = "Yennefer's costume"
    $ hg_yenn_OBJ.cost = 275
    $ hg_yenn_OBJ.wait_time = 4
    $ hg_yenn_OBJ.store_image = "yenn.png"
    $ hg_yenn_OBJ.outfit_layers = []
    $ hg_yenn_OBJ.outfit_layers.extend(("yenn_stockings.png","yenn_pant.png","yenn_skirt.png","yenn_top.png","yenn_gloves.png","yenn_chocker.png","yenn_scarf.png","yenn_belt.png"))
    $ hg_yenn_OBJ.breast_layer = "breasts_normal"


    $ hermione_outfits_list = []
    $ hermione_outfits_list.append(hg_maid_OBJ)
    $ hermione_outfits_list.append(hg_gryffCheer_OBJ)
    $ hermione_outfits_list.append(hg_slythCheer_OBJ)
    $ hermione_outfits_list.append(hg_heartDancer_OBJ)
    $ hermione_outfits_list.append(hg_silkNightgown_OBJ)
    $ hermione_outfits_list.append(hg_pirate_OBJ)
    $ hermione_outfits_list.append(hg_powerGirl_OBJ)
    $ hermione_outfits_list.append(hg_msMarvel_OBJ)
    $ hermione_outfits_list.append(hg_harleyQuinn_OBJ)
    $ hermione_outfits_list.append(hg_ballDress_OBJ)
    $ hermione_outfits_list.append(hg_christmas_OBJ)
    $ hermione_outfits_list.append(hg_laraCroft_OBJ)
    $ hermione_outfits_list.append(hg_tifa_OBJ)
    $ hermione_outfits_list.append(hg_rocker_OBJ)
    $ hermione_outfits_list.append(hg_present_OBJ)
    $ hermione_outfits_list.append(hg_japan_OBJ)
    $ hermione_outfits_list.append(hg_witch_OBJ)
    $ hermione_outfits_list.append(hg_bio_OBJ)
    $ hermione_outfits_list.append(hg_yenn_OBJ)
    
    return
   



## Outfit Blocks
label set_hermione_outfit(outfit):
    show screen blkfade
    hide screen hermione_main
    with d3
    call h_outfit_OBJ(outfit) 
    pause .5
    hide screen blkfade
    with d5
    return
    
label h_outfit_OBJ(outfit):
    if outfit == None:
        $ hermione_costume = False
        call update_her_uniform 
        call h_update_hair 
    else:
        $ hermione_costume = True
        
        $ h_request_wear_top = True
        $ hermione_wear_top = True
        
        $ hermoine_outfit_GLBL = outfit

        if hermione_use_action and hermione_action in hermoine_outfit_GLBL.actions:
            pass
        else:
            call h_action("None") 

        call update_her_uniform 
        call h_update_hair 
        
        if transparency < 1 or not hermione_wear_top:
            if not hermione_perm_expand:
                $ hermione_breasts = "characters/hermione/body/breasts/breasts_normal.png" 
            else:
                $ hermione_breasts = "characters/hermione/body/breasts/breasts_expanded_large.png"
        else:
            $ hermione_breasts = "characters/hermione/body/breasts/"+outfit.breast_layer+".png"
        

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
        purchased = False
        cost = 0
        wait_time = 0 #the ammount of time to wait until compleded from clothes store
        top_layers = []
        outfit_layers = []
        actions = []
        action_images = []
        hair_layer = ""
        breast_layer = "breasts_nipfix"
        store_image = ""
        
        
        def getMenuText(self):
            return "-"+self.name+"-"
        def getFullPath(self, passed_list):
            list = []
            for i in passed_list:
                list.append("characters/hermione/clothes/custom/"+i)
            return list
        def getOutfitLayers(self):
            return self.getFullPath(self.outfit_layers)
        def getTopLayers(self):
            return self.getFullPath(self.top_layers)
        def getActionImage(self, action):
            return self.action_images[self.actions.index(action)]
        def getStoreImage(self):
           return "images/store/cs_gui/"+self.store_image
    
