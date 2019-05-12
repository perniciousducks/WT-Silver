

### PERSISTANTS ###

label __init_variables:

    #place save variables here
    if not hasattr(renpy.store,'addicted'):
        $ addicted = False
    if not hasattr(renpy.store,'tentacle_cosmetic'):
        $ tentacle_cosmetic = False

    ### Interface ###
    if not hasattr(renpy.store,'interface_color'):
        $ interface_color = "gold"

    ### Difficulty ###
    if not hasattr(renpy.store,'game_difficulty'):
        $ game_difficulty = 2                      # 2 = normal

    ### Gameplay ###
    if not hasattr(renpy.store,'ignore_warning'):
        $ ignore_warning = False #Warning message that tells you which ending you will get.

    ### Misc ###
    if not hasattr(renpy.store,'walk_xpos'):
        #For UI help,temporary add them to your UI element and use the console to quickly get it into place.
        #Then replace the variables with the number you ended up with.
        $ nxpos = 0
        $ nypos = 0
        $ nscale = 0.5
        $ walk_xpos = 750
        $ walk_ypos = 250
        $ chibi_xpos = 0
        $ chibi_ypos = 0
        $ chibi_zorder = 0

    if not hasattr(renpy.store,'unlocked_xmas_deco'):
        $ unlocked_7th = False
        $ charName = "genie"
        $ unlocked_xmas_deco = False

    #Phoenix
    if not hasattr(renpy.store,'phoenix_is_fed'):
        $ fawkes_intro_done = False
        $ phoenix_is_fed = False
        $ phoenix_is_petted = False
        $ phoenix_fed_counter = 0
        $ phoenix_petted_counter = 0

    #Other
    if not hasattr(renpy.store,'stat_fireplace_counter'):
        $ stat_fireplace_counter = 0
        $ stat_reports_counter = 0

    #Room Deco
    if not hasattr(renpy.store,'room_deco'):
        $ room_deco = ""
        $ cupboard_deco = ""

    #HD RESCALE RATION
    if not hasattr(renpy.store,'genie_scaleratio'):
        $ scaleratio = 2 #BECAUSE THE IMAGES ARE 2X LARGER

        $ genie_scaleratio = 2 #Scaleratio of each character can be changed to be used in custom "CG" scenes. Made larger, more zoomed in,...
        $ snape_scaleratio = 2
        $ tonks_scaleratio = 2

        $ hermione_scaleratio = 2
        $ luna_scaleratio = 2
        $ astoria_scaleratio = 2
        $ susan_scaleratio = 2
        $ cho_scaleratio = 2

    #CGs
    if not hasattr(renpy.store,'ccg_folder'):
        $ ccg_folder = "luna_bj"
        $ ccg1 = "herm"
        $ ccg2 = 1
        $ ccg3 = "gene"

    if not hasattr(renpy.store,'sc_cg_base'):
        $ sc_cg_base = "images/CG/sc34/1/base_1.png"
        $ sc_cg_image_1 = "images/CG/sc34/1/A_1.png"
        $ sc_cg_image_2 = "images/CG/sc34/2/B_1.png"
        $ sc_cg_image_3 = "images/CG/sc34/2/C_1.png"
        $ sccgxpos = 200
        $ sccgypos = 50

    #Using images instead of chibis.
    if not hasattr(renpy.store,'face_on_cg'):
        $ face_on_cg = False #"call her_main(,ypos="head")" will use screen "her_face". Face gets positioned automatically.
        $ use_cgs = False



    #Reset Persistants
    if not hasattr(renpy.store,'reset_persistants'): #Turns true when creating a new game only.
        $ reset_persistants            = False

    if not hasattr(renpy.store,'reset_cho_content'):
        $ reset_luna_content = False
        $ reset_cho_content = False

    if not hasattr(renpy.store,'loopimage'):
        $ loopimage = None

    #Rooms
    call room_objects_init

    #Genie Init
    call genie_init

    #Snape Init
    call snape_init
    call snape_progress_init

    #Hermione Init
    call her_init #Defines newly added variables. Resets variables after creating a new game.
    call her_clothing_lists_init #Lists update every time!
    call her_progress_init #Defines newly added variables. Resets variables after creating a new game.

    #Luna Init
    call luna_init
    call luna_progress_init

    #Cho Init
    call cho_init
    call cho_progress_init

    #Susan Init
    call susan_init
    call susan_progress_init

    #Astoria Init
    call astoria_init
    call astoria_progress_init

    #Tonks Init
    call tonks_init
    call tonks_progress_init

    #Map
    call map_init

    #Wardrobe
    call wardrobe_init

    #Items
    call store_init
    call store_items_init
    call quest_items_init

    #Minigames & Mirror Stories
    call dark_room_init

    #Cheats
    call cheats_init


    #Hidden Blowjob
    $ hg_hidden_blowjob_character_list = ["snape"]
    if luna_unlocked and luna_reverted:
        $ hg_hidden_blowjob_character_list.append("luna")
    #if astoria_unlocked:
    #    $ hg_hidden_blowjob_character_list.append("astoria")
    #if susan_unlocked:
    #    $ hg_hidden_blowjob_character_list.append("susan")
    #if cho_unlocked:
    #    $ hg_hidden_blowjob_character_list.append("cho")
    if tonks_unlocked:
        $ hg_hidden_blowjob_character_list.append("tonks")

    return
