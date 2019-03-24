

#Night Start.

label night_start:
    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    show screen blkfade

#    $ renpy.set_style_preference("dialog", "Night")
# $ textColor = "#1e1008"

$ daytime = False
$ interface_color = "gray"

$ temp_name = "Day - "+str(day)+"\nWhoring - "+str(her_whoring)
$ save_name = temp_name

###RESET STUFF
call room(hide_screens=True)

call reset_day_and_night_flags

# Hermione
call reset_hermione
$ no_blinking = False #When True - blinking animation is not displayed.
$ gifted = False #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
$ hermione_busy = False

#Luna
call reset_luna
$ luna_busy = False

#Astoria
call update_astoria
$ astoria_busy = False

#Susan
call update_susan
$ susan_busy = False

#Cho
$ cho_busy = False

#Tonks
call update_tonks
$ tonks_busy = False

#Snape
call update_snape
$ snape_busy = False

#Genie
call update_genie


$ chitchated_with_her = False
$ chitchated_with_astoria = False
$ chitchated_with_susan = False
$ chitchated_with_snape = False
$ chitchated_with_tonks = False

scene black



### WEATHER ###
stop bg_sounds #Stops playing the fire SFX.
stop weather #Stops playing the rain SFX.
$ show_weather()



#Mail
if day >= 1 and not letter_from_hermione_A_OBJ.read:
    $ letter_from_hermione_A_OBJ.mailLetter()



call room("main_room", hide_screens=False) #Screens already get hidden above.

hide screen blkfade
with fade







call points_changes #Makes house points changes.




#EVENTS

label night_resume:

### NIGHT EVENTS ###
if day == 1:
    call owl_intro #Returns
if day == 2:
    jump event_03 #No return. Jumps next day.
if day == 4:
    jump event_05 #Before Duel #No return.
if day == 5:
    jump event_07 #No return.
if days_without_an_event >= 1 and hermione_is_waiting_02 and not event11_happened:
    call event_11 #Returns
if days_without_an_event >= 1 and event11_happened and not event12_happened:
    jump event_12 #No return.
if days_without_an_event >= 1 and event12_happened and not event13_happened:
    jump event_13 #No return.
if day >= 15 and event13_happened and not event15_happened:
    call event_15 #Returns

# Tonks intro.
if astoria_unlocked and not tonks_intro_happened and days_without_an_event >= 1:
    $ tonks_intro_happened = True
    $ days_without_an_event = 0
    jump tonks_intro_event

# Snape prevents the ministry from detecting curses.
if tonks_intro_happened and not spells_unlocked and days_without_an_event >= 1:
    $ spells_unlocked = True #Astoria can now use spells.
    $ days_without_an_event = 0
    jump snape_spell_intro

# Tonks becomes a teacher.
if third_curse_got_cast and not tonks_unlocked and days_without_an_event >= 1:
    $ tonks_unlocked = True
    $ astoria_intro_completed = True
    $ days_without_an_event = 0
    jump astoria_tonks_intro

# Luna events.
if luna_known and not luna_unlocked:
    call hat_intro_3 #Returns

if luna_reverted and lun_corruption == -1:
    $ days_without_an_event = 0
    jump luna_reverted_greeting_2 #Sets lun_corruption to 0

# Hermione working return.
if current_job == 1:
    jump maid_responses
if current_job == 2:
    jump barmaid_responses
if current_job == 3:
    jump gryffindor_cheer_responses
if current_job == 4:
    jump slytherin_cheer_responses
if current_job == 5:
    jump hermione_helping_selling_cards
#Hermione Potions return.
if cat_ears_potion_return:
    jump potion_scene_1_1_2
if transparent_quest:
    $ transparent_quest = False
    jump potion_scene_4_2
if addicted == True:
    jump potion_scene_3_1_2

if hg_pf_TheGamble_Flag and hg_pf_TheGamble_FlagC or hg_pf_TheGamble_FlagA:
    jump hg_pf_TheGamble_complete


# Cho Events.
if cho_intro_1_complete and not cho_intro_2_complete: # Happens right after intro.
    $ cho_intro_2_complete = True
    jump cho_intro_2
if quidditch_match_in_progress:
    $ quidditch_match_in_progress = False
    jump quidditch_match_return
if main_match_1_stage == "return":
    $ main_match_1_stage = "end"
    jump hufflepuff_match_return

# Hermione Personal Requests, Public Shaming return.
python:
    for i in hg_pr_list: #Call any public request event if it's in progress
        if i.inProgress:
            renpy.jump(i.complete_label)
    for i in hg_ps_list: #Call any public shaming event if it's in progress
        if i.inProgress:
            renpy.jump(i.complete_label)

if gave_the_dress and days_without_an_event >= 2: #$ gave_the_dress = True #Turns True when Hermione has the dress.
    jump good_bye_snape

if milking == -1:
    call potion_scene_11_1_2 #Returns
if milking == -3:
    call potion_scene_11_3_2


if her_whoring == 11 and not touched_by_boy and not ignore_warning:
    call nar("!!! Attention !!!","start")
    ">Increasing Hermione's Whoring level any further without doing more public requests will lock your game to a specific ending."
    ">This message will repeat until you increase her Whoring level, or do a certain number of public requests!"
    call nar(">You should also save your game here.","end")
    menu:
        "-Understood-":
            pass
        "-Don't tell me what to do!-":
            call nar(">This message will stop appearing. You're on your own!")
            $ ignore_warning = True


#Atoria / Tonks event return.
if astoria_tonks_event_in_progress:
    jump astoria_tonks_event #These do not return to 'night_resume'!




### Guide ###
call update_hints





label night_main_menu:

### MENU PLACEMENT ###
call reset_menu_position

hide screen bld1
hide screen blktone
call hide_characters
with d1

call screen main_room_menu
