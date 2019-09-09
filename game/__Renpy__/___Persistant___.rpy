#TODO Move default variable definitions to appropriate files

default addicted          = False
default tentacle_cosmetic = False

default interface_color = "gold"

default gallery_active = False
default ball_ending_2  = False

default game_difficulty = 2

# Used to pause events/summons for a number of days
default ss_event_pause  = 0
default ss_summon_pause = 0
default nt_event_pause  = 0
default nt_summon_pause = 0
default hg_event_pause  = 0
default hg_summon_pause = 0
default cc_event_pause  = 0
default cc_summon_pause = 0
default ll_event_pause  = 0
default ll_summon_pause = 0
default ag_event_pause  = 0
default ag_summon_pause = 0
default sb_event_pause  = 0
default sb_summon_pause = 0

default always_read_letter = False
default owl_away           = False
default owl_away_counter   = 0

# Sprite positioning
default nxpos        = 0
default nypos        = 0
default nscale       = 0.5
default walk_xpos    = 750
default walk_ypos    = 250
default chibi_xpos   = 0
default chibi_ypos   = 0
default chibi_zorder = 1
default desk_zorder  = 2

default unlocked_7th       = False
default charName           = "genie"
default unlocked_xmas_deco = False

# Phoenix
default phoenix_is_fed         = False
default phoenix_is_petted      = False
default phoenix_fed_counter    = 0
default phoenix_petted_counter = 0

default stat_fireplace_counter = 0
default stat_reports_counter   = 0

# Room decoration
default current_room  = "main_room"
default room_deco     = ""
default cupboard_deco = ""

# Scale factors (because most images are 2x larger)
# Scale-ratio of each character can be changed to be used in custom "CG" scenes. Made larger, more zoomed in,...
default scaleratio          = 2
default genie_scaleratio    = 2
default snape_scaleratio    = 2
default tonks_scaleratio    = 2
default hermione_scaleratio = 2
default luna_scaleratio     = 2
default astoria_scaleratio  = 2
default susan_scaleratio    = 2
default cho_scaleratio      = 2

# CGs
default ccg_folder = "luna_bj"
default ccg1       = "herm"
default ccg2       = 1
default ccg3       = "gene"
default loopimage  = None
default cg_image   = "e2"
default cg_path    = "images/CG/"+cg_image+".png"

default sc_cg_base    = "images/CG/sc34/1/base_1.png"
default sc_cg_image_1 = "images/CG/sc34/1/A_1.png"
default sc_cg_image_2 = "images/CG/sc34/2/B_1.png"
default sc_cg_image_3 = "images/CG/sc34/2/C_1.png"

default sccgxpos = 200
default sccgypos = 50

# CG or chibis
default face_on_cg = False # `call her_main(,ypos="head")` will use screen "her_face". Face gets positioned automatically.
default use_cgs = False

#TODO hg_hidden_blowjob_characters is never used
default hg_hidden_blowjob_characters = set(["snape"])
# if luna_unlocked and luna_reverted:
#     $ hg_hidden_blowjob_characters.add("luna")
# if astoria_unlocked:
#     $ hg_hidden_blowjob_characters.add("astoria")
# if susan_unlocked:
#     $ hg_hidden_blowjob_characters.add("susan")
# if cho_unlocked:
#     $ hg_hidden_blowjob_characters.add("cho")
# if tonks_unlocked:
#     $ hg_hidden_blowjob_characters.add("tonks")

# Skip to Hermione
label update_early_game_vars:
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

    $ letter_hg_1.mailRead()
    $ letter_hg_2.mailRead()
    $ letter_min_work.mailRead()
    $ letter_min_report.mailRead()
    $ letter_min_favors.mailRead()

    $ snape_unlocked = True
    $ achievement.unlock("unlocksna", True)

    $ tonks_unlocked = True
    $ achievement.unlock("unlockton", True)

    $ hermione_unlocked = True
    $ achievement.unlock("unlockher", True)
    $ tutoring_hermione_unlocked = True
    $ hermione_favors = True

    return
