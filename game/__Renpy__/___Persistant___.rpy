

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

    ### Gallery ###
    if not hasattr(renpy.store,'gallery_active'):
        $ gallery_active = False
        $ ball_ending_2  = False

    ### Difficulty ###
    if not hasattr(renpy.store,'game_difficulty'):
        $ game_difficulty = 2                      # 2 = normal

    ### Gameplay ###
    if not hasattr(renpy.store,'always_read_letter'):

        $ ss_event_pause  = 0
        $ ss_summon_pause = 0
        $ nt_event_pause  = 0
        $ nt_summon_pause = 0
        $ hg_event_pause  = 0
        $ hg_summon_pause = 0
        $ cc_event_pause  = 0
        $ cc_summon_pause = 0
        $ ll_event_pause  = 0
        $ ll_summon_pause = 0
        $ ag_event_pause  = 0
        $ ag_summon_pause = 0
        $ sb_event_pause  = 0
        $ sb_summon_pause = 0

        $ always_read_letter = False
        $ owl_away = False
        $ owl_away_counter = 0

    ### Misc ###
    if not hasattr(renpy.store,'desk_zorder'):
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
        $ desk_zorder = 2

    if not hasattr(renpy.store,'unlocked_xmas_deco'):
        $ unlocked_7th = False
        $ charName = "genie"
        $ unlocked_xmas_deco = False

    # Phoenix
    if not hasattr(renpy.store,'phoenix_is_fed'):
        $ phoenix_is_fed = False
        $ phoenix_is_petted = False
        $ phoenix_fed_counter = 0
        $ phoenix_petted_counter = 0

    # Other
    if not hasattr(renpy.store,'stat_fireplace_counter'):
        $ stat_fireplace_counter = 0
        $ stat_reports_counter = 0

    # Room Deco
    if not hasattr(renpy.store,'current_room'):
        $ current_room = "main_room"
        $ room_deco = ""
        $ cupboard_deco = ""

    # HD RESCALE RATION
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

    # CGs
    if not hasattr(renpy.store,'cg_image'):
        $ ccg_folder = "luna_bj"
        $ ccg1 = "herm"
        $ ccg2 = 1
        $ ccg3 = "gene"
        $ loopimage = None
        $ cg_image = "e2"
        $ cg_path  = "images/CG/"+cg_image+".png"

    if not hasattr(renpy.store,'sc_cg_base'):
        $ sc_cg_base = "images/CG/sc34/1/base_1.png"
        $ sc_cg_image_1 = "images/CG/sc34/1/A_1.png"
        $ sc_cg_image_2 = "images/CG/sc34/2/B_1.png"
        $ sc_cg_image_3 = "images/CG/sc34/2/C_1.png"
        $ sccgxpos = 200
        $ sccgypos = 50

    # Using images instead of chibis.
    if not hasattr(renpy.store,'face_on_cg'):
        $ face_on_cg = False #"call her_main(,ypos="head")" will use screen "her_face". Face gets positioned automatically.
        $ use_cgs = False



    # Reset Persistants
    if not hasattr(renpy.store,'reset_persistants'): #Turns true when creating a new game only.
        $ reset_persistants            = False

    if not hasattr(renpy.store,'reset_cho_content'):
        $ reset_luna_content = False
        $ reset_cho_content = False

    # Rooms
    call room_objects_init

    # Genie Init
    call genie_init

    # Snape Init
    call snape_init
    call snape_progress_init

    # Hermione Init
    call her_init #Defines newly added variables. Resets variables after creating a new game.
    call her_clothing_lists_init #Lists update every time!
    call her_progress_init #Defines newly added variables. Resets variables after creating a new game.

    # Luna Init
    call luna_init
    call luna_progress_init

    # Cho Init
    call cho_init
    call cho_progress_init
    call cho_wardrobe_init

    # Susan Init
    call susan_init
    call susan_progress_init

    # Astoria Init
    call astoria_init
    call astoria_progress_init
    call astoria_wardrobe_init

    # Tonks Init
    call tonks_init
    call tonks_progress_init
    call tonks_wardrobe_init

    # Quests
    call quest_init

    # Map
    call map_init

    # Wardrobe
    call wardrobe_init

    # Items
    call store_init
    call store_items_init
    call quest_items_init

    # Minigames & Mirror Stories
    call dark_room_init

    # Cheats
    call cheats_init

    # Save compatibility
    if not hasattr(renpy.store,'updated_early_game'):
        $ updated_early_game = False
    if hermione_favors == True and updated_early_game == False:
        call update_early_game_vars


    # Hidden Blowjob
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


label update_early_game_vars: # Save compatibility
    $ updated_early_game = True # Prevents this from being called again.
    
    $ bird_examined = True
    $ desk_examined = True
    $ cupboard_examined = True
    $ door_examined = True
    $ fireplace_examined = True

    $ achievement.unlock("start", True)

    $ genie_intro.E1_complete = True
    $ genie_intro.E2_complete = True
    $ genie_intro.E3_complete = True

    $ snape_intro.E1_complete   = True
    $ snape_intro.E2_complete   = True
    $ snape_intro.E3_complete   = True
    $ snape_intro.duel_complete = True
    $ snape_intro.E4_complete   = True
    $ snape_intro.E5_complete   = True

    $ hang_with_snape.E1_complete = True
    $ hang_with_snape.E2_complete = True
    $ hang_with_snape.E3_complete = True
    $ hang_with_snape.E4_complete = True
    $ hang_with_snape.E5_complete = True

    $ tonks_intro.E1_complete = True
    $ tonks_intro.E2_complete = True
    $ tonks_intro.E3_complete = True

    $ hang_with_tonks.E1_complete = True

    $ hermione_intro.E1_complete = True
    $ hermione_intro.E2_complete = True
    $ hermione_intro.E3_complete = True
    $ hermione_intro.E4_complete = True
    $ hermione_intro.E5_complete = True
    $ hermione_intro.E6_complete = True

    $ letter_from_hermione_A_OBJ.mailRead()
    $ letter_from_hermione_B_OBJ.mailRead()
    $ letter_paperwork_unlock_OBJ.mailRead()
    $ letter_paperwork_report_OBJ.mailRead()
    $ letter_favor_complaint_OBJ.mailRead()

    $ snape_unlocked = True
    $ achievement.unlock("unlocksna", True)

    $ tonks_unlocked = True
    $ achievement.unlock("unlockton", True)

    $ hermione_unlocked = True
    $ achievement.unlock("unlockher", True)
    $ tutoring_hermione_unlocked = True
    $ hermione_favors = True

    return
