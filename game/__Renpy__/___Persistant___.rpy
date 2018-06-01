

### PERSISTANTS ###

label __init_variables:
    
    #place save variables here 
    if not hasattr(renpy.store,'addicted'): #important!
        $ addicted = False

    if not hasattr(renpy.store,'pitch_open'): #important!
        $ pitch_open = True
    if not hasattr(renpy.store,'maid_working_unlocked'): #important!
        $ maid_working_unlocked = True
    if not hasattr(renpy.store,'inn_first'): #important!
        $ inn_first = True
    if not hasattr(renpy.store,'attic_open'): #important!
        $ attic_open = False
    if not hasattr(renpy.store,'custom_outfit_old'): #important!
        $ custom_outfit_old = 0
    if not hasattr(renpy.store,'show_attic'): #important!
        $ show_attic = True
    if not hasattr(renpy.store,'show_clothes_store'): #important!
        $ show_clothes_store = True
    if not hasattr(renpy.store,'show_forest'): #important!
        $ show_forest = True
    if not hasattr(renpy.store,'show_inn'): #important!
        $ show_inn = True
    if not hasattr(renpy.store,'show_pitch'): #important!
        $ show_pitch = True
    if not hasattr(renpy.store,'tentacle_cosmetic'): #important!
        $ tentacle_cosmetic = False
    if not hasattr(renpy.store,'maid'): #important!
        $ maid = True
    if not hasattr(renpy.store,'cheerleader'): #important!
        $ cheerleader = True
    if not hasattr(renpy.store,'custom_skirt'): #important!
        $ custom_skirt = 0
    if not hasattr(renpy.store,'custom_shirt'): #important!
        $ custom_shirt = 0

    if not hasattr(renpy.store,'tent_scroll'): #important!
        $ tent_scroll = False
        
        
    if not hasattr(renpy.store,'shaming'): #important!
        $ shaming = 0
    if not hasattr(renpy.store,'shaming_busy'): #important!
        $ shaming_busy = False
    if not hasattr(renpy.store,'shaming_01'): #important!
        $ shaming_01 = False
    if not hasattr(renpy.store,'shaming_02'): #important!
        $ shaming_02 = False
    if not hasattr(renpy.store,'shaming_03'): #important!
        $ shaming_03 = False
        
        
    if not hasattr(renpy.store,'heretic'): #important!
        $ heretic = 0
    if not hasattr(renpy.store,'heretic_01'): #important!
        $ heretic_01 = False
    if not hasattr(renpy.store,'heretic_02'): #important!
        $ heretic_02 = False
    if not hasattr(renpy.store,'heretic_03'): #important!
        $ heretic_03 = False
    if not hasattr(renpy.store,'heretic_busy'): #important!
        $ heretic_busy = False
        
        
    if not hasattr(renpy.store,'legs_03'): #important!
        $ legs_03 = False
    if not hasattr(renpy.store,'scene_number'): #important!
        $ scene_number = 1
    if not hasattr(renpy.store,'cust_char_1_enabled'): #important!
        $ cust_char_1_enabled = False
    if not hasattr(renpy.store,'cust_char_2_enabled'): #important!
        $ cust_char_2_enabled = False
    if not hasattr(renpy.store,'cust_char_3_enabled'): #important!
        $ cust_char_3_enabled = False
    if not hasattr(renpy.store,'fawkes_intro_done'): #important!
        $ fawkes_intro_done = True
    if not hasattr(renpy.store,'temp_outfit'): #important! 
        $ temp_outfit = custom_outfit_old

    ### Interface ###
    if not hasattr(renpy.store,'interface_color'): #important!
        $ interface_color = "gold"

    ### Difficulty ###
    if not hasattr(renpy.store,'game_difficulty'): #important!
        $ game_difficulty = 2                      # 2 = normal
        $ hardcore_difficulty_active = False       # for hardcore play-through rewards

    ### Cheats ###
    if not hasattr(renpy.store,'cheats_active'): #important!
        $ cheats_active = False
    if not hasattr(renpy.store,'force_unlock_pub_favors'): #important!
        $ force_unlock_pub_favors = False
    if not hasattr(renpy.store,'skip_duel'): #important!
        $ skip_duel = False
    if not hasattr(renpy.store,'next_day'): #important!
        $ next_day = False
    
    
    if not hasattr(renpy.store,'new_request_01_heart'): #important!
        $ new_request_01_heart = 0
    if not hasattr(renpy.store,'new_request_02_heart'): #important!
        $ new_request_02_heart = 0
    if not hasattr(renpy.store,'new_request_03_heart'): #important!
        $ new_request_03_heart = 0
    if not hasattr(renpy.store,'new_request_04_heart'): #important!
        $ new_request_04_heart = 0
    if not hasattr(renpy.store,'new_request_05_heart'): #important!
        $ new_request_05_heart = 0
    if not hasattr(renpy.store,'new_request_08_heart'): #important!
        $ new_request_08_heart = 0
    if not hasattr(renpy.store,'new_request_11_heart'): #important!
        $ new_request_11_heart = 0
    if not hasattr(renpy.store,'new_request_12_heart'): #important!
        $ new_request_12_heart = 0
    if not hasattr(renpy.store,'new_request_16_heart'): #important!
        $ new_request_16_heart = 0
    if not hasattr(renpy.store,'new_request_22_heart'): #important!
        $ new_request_22_heart = 0
    if not hasattr(renpy.store,'new_request_29_heart'): #important!
        $ new_request_29_heart = 0
    if not hasattr(renpy.store,'new_request_31_heart'): #important!
        $ new_request_31_heart = 0
    
    if not hasattr(renpy.store,'pub_q_sex_teach'): #important!
        $ pub_q_sex_teach = False
    if not hasattr(renpy.store,'hg_pf_TheGamble_Flag'): #important!
        $ hg_pf_TheGamble_Flag = False
    if not hasattr(renpy.store,'hg_pf_TheGamble_FlagA'): #important!
        $ hg_pf_TheGamble_FlagA = False
    if not hasattr(renpy.store,'hg_pf_TheGamble_FlagB'): #important!
        $ hg_pf_TheGamble_FlagB = False
    if not hasattr(renpy.store,'hg_pf_TheGamble_FlagC'): #important!
        $ hg_pf_TheGamble_FlagC = False
    

    if not hasattr(renpy.store,'gift_order'): #important!
        $ gift_order = None
    if not hasattr(renpy.store,'order_quantity'): #important!
        $ order_quantity = 0
    if not hasattr(renpy.store,'tentacle_owned'): #important!
        $ tentacle_owned = False
    if not hasattr(renpy.store,'tent_scroll'): #important!
        $ tent_scroll = False

    if not hasattr(renpy.store,'hermione_ass_cum'): #important!
        $ hermione_ass_cum = False

    ###Tutoring fix
    if not hasattr(renpy.store,'table_position_x'): #important!
        $ table_position_x = 20

    ###MISC
    if not hasattr(renpy.store,'hermione_action_under'): #important!
        $ hermione_action_under = False

    if not hasattr(renpy.store,'hermione_squirt'): #important!
        $ hermione_squirt = False

    if not hasattr(renpy.store,'hermione_futa'): #important!
        $ hermione_futa = False

    if not hasattr(renpy.store,'milk_level'): #important!
        $ milk_level = 0
    if not hasattr(renpy.store,'milking'): #important!
        $ milking = 0

    if not hasattr(renpy.store,'potion_scene_11_progress'): #important!
        $ potion_scene_11_progress = 0

        
    ###CGs
    if not hasattr(renpy.store,'cgg_folder'): #important!
        $ ccg_folder = "luna_bj"
        $ ccg1 = "herm"
        $ ccg2 = 1
        $ ccg3 = "gene"
        
    #SC34 update 2 stuff, thanks akabur.
    if not hasattr(renpy.store,'sc_cg_base'): #important!
        $ sc_cg_base = "images/28_cg/sc34/1/base_1.png"
        $ sc_cg_image_1 = "images/28_cg/sc34/1/A_1.png"
        $ sc_cg_image_2 = "images/28_cg/sc34/2/B_1.png"
        $ sc_cg_image_3 = "images/28_cg/sc34/2/C_1.png"
        $ sccgxpos = 200
        $ sccgypos = 50

    #Using images instead of chibis.
    if not hasattr(renpy.store,'face_on_cg'): #important!
        $ face_on_cg = False #"call her_head" will use screen "her_face". Face gets positioned automatically.
        $ use_cgs = False

        
    #Favor ID's
    $ hg_pf_TalkToMe_ID = 0        #00 Genie touches himself.
    $ hg_pf_NicePanties_ID = 1     #01 "Lift your skirt".
    $ hg_pf_BreastMolester_ID = 2  #02 "Molest tits."
    $ hg_pf_ButtMolester_ID = 3    #03 "Molest butt."
    $ hg_pf_ShowThemToMe_ID = 4    #04 "Show me your tits."
    $ hg_pf_DanceForMe_ID = 5      #05 "Get naked."
    $ hg_pf_LetMeTouchThem_ID = 6  #06 "Let me play with your tits."
    $ hg_pf_TouchMe_ID = 7         #07 (Handjob).
    $ hg_pf_SuckIt_ID = 8          #08 (Blowjob).
    $ hg_pf_LetsHaveSex_ID = 9     #09 (Sex).
    $ hg_pf_TimeForAnal_ID = 10    #10 (Anal sex)
    $ hg_pf_TheGamble_ID = 11      #11 (Gamble with hg)
    
    $ hg_pr_FlirtClassmate_ID = 0 #00 "Flirt with 3 classmates".
    $ hg_pr_FlirtTeacher_ID = 1 #01 "Flirt with a teacher".
    $ hg_pr_ClassmateTouchYou_ID = 2 #02 "Let a classmate molest you."
    $ hg_pr_FlashClassmate_ID = 3 #03 "Flash a classmate."
    $ hg_pr_KissAGirl_ID = 4 #04 "Kiss female classmate."
    $ hg_pr_HandjobClassmate_ID = 5 #05 (Give handjob to a classmate)
    $ hg_pr_BlowjobClassmate_ID = 6 #06 (Blow a classamate).
    $ hg_pr_BlowjobTeacher_ID = 7 #07 (Blow a teacher)
    $ hg_pr_SexWithClassmate_ID = 8 #08 (sex with classamate).
    
    
    
    #Character Paths
    $ gen_path = "characters/genie/"
    $ sna_path = "characters/snape/"
    $ her_path = "characters/hermione/"
    $ lun_path = "characters/luna/"
    $ cho_path = "characters/cho/"
    $ sus_path = "characters/susan/"
    $ ast_path = "characters/astoria/"
    

    #Reset Persistants
    if not hasattr(renpy.store,'reset_persistants'): #Turns true when creating a new game only.
        $ reset_persistants            = False

    #Genie Init
    if not hasattr(renpy.store,'genie_sprite_base'): #important!
        call init_genie_layering

    #Snape Init
    call snape_init
    call snape_progress_init

    #Hermione Init
    call her_init                #Defines newly added variables. Resets variables after creating a new game.
    call her_clothing_init       #Defines newly added variables. Resets variables after creating a new game.
    call her_chibi_init          #Defines newly added variables. Resets variables after creating a new game.
    call her_clothing_lists_init #Lists update every time!
    call her_progress_init       #Defines newly added variables. Resets variables after creating a new game.
    
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

    call wardrobe_init

    
    #Ginny unlock. #After 3 turn true, Genie wants to find out more about Ginny. #Not implemented.
    if not hasattr(renpy.store,'mentioned_ginnys_hair'):
        $ mentioned_ginnys_hair         = False #Wardrobe Hair #Always available.
        $ snapes_plan_for_ginny         = False #Pf DanceForMe #Always available.
        $ hanging_out_with_ginny        = False #Pf TitJob     #Always available.
        $ handjob_practice_with_ginny   = False #Pf Handjob
        $ kissed_ginny                  = False #Pr KissAGirl
        $ flashing_tits_with_ginny      = False #Pr FlasAClassmate
    
    
    #Update max tutoring if there is add more events 
    $ max_tutoring = 14 
    
    #Sorter Values
    $ zorder_character = 7
   
    
    $ row_index_selected = 0
    $ column_index_selected = 0
    
    return
