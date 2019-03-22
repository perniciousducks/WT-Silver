

#Day Start.

label day_start:
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY THEME
    show screen blkfade

#    $ renpy.set_style_preference("dialog", "Day")

$ daytime = True #True when it is daytime. Turns False during nighttime.
# Dont change UI if using nightmode
if not persistent.nightmode:
    $ interface_color = "gold"

$ temp_name = "Day - "+str(day)+"\nWhoring - "+str(her_whoring)
$ save_name = temp_name



### RESETING STUFF ###
call room(hide_screens=True)

call reset_day_flags
call reset_day_and_night_flags

$ chitchated_with_her = False
$ chitchated_with_astoria = False
$ chitchated_with_susan = False
$ chitchated_with_snape = False
$ chitchated_with_tonks = False




#Hermione Daily Flags.
call reset_hermione
$ gifted    = False #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
$ hermione_door_event_happened = False
$ flip = False
$ no_blinking   = False #When True - blinking animation is not displayed.
$ hermione_busy = False

if hermione_expand_breasts_counter != 0:
    $ hermione_expand_breasts_counter -= 1
else:
    $ hermione_expand_breasts = False

if hermione_expand_ass_counter != 0:
    $ hermione_expand_ass_counter -= 1
else:
    $ hermione_expand_ass = False

#Luna Daily Flags.
call reset_luna
$ days_to_luna-= 1
$ luna_busy = False

#Astoria Daily Flags.
call update_astoria
$ astoria_busy = False

#Susan Daily Flags.
call update_susan
$ susan_busy = False
if susan_imperio_counter > 0:
    $ susan_imperio_counter -= 1            #Removes 1 at each new day.
    $ susan_imperio_influence = True
    if susan_imperio_counter <= 0:
        $ susan_imperio_influence = False
        call reset_susan_clothing

#Cho Daily Flags.
call update_cho
$ cho_busy = False

#Tonks Daily Flags.
call update_tonks
$ tonks_busy = False

#Snape Daily Flags.
call update_snape
$ snape_busy = False

#Genie Reset.
call update_genie







if her_whoring >= 12 and not touched_by_boy and not force_unlock_pub_favors: #Turns true if sent Hermione to get touched by a boy at least once.
    $ lock_public_favors = True #Turns True if reached her_whoring level 05 while public event "Touched by boy" never attempted. Locks public events.
else:
    $ lock_public_favors = False

$ generating_snape_bonus = renpy.random.randint(1, 2) #Determines whether ot not Snape bonus will be added to the Slytherin house.
$ generating_points = renpy.random.randint(1, 2) #Determines whether or not point will be awarded to Slytherin on this day. # MAKE NO CHANGES HERE. BEING USED AS "ONE_OUT_OF_TWO".
$ generating_points_gryffindor = renpy.random.randint(1, 10) #Addying point to Gryffindor (07_points_gry.rpy)
$ generating_points_hufflepuff = renpy.random.randint(1, 10) #Addying point to Hufflepuff (07_points_gry.rpy)
$ generating_points_ravenclaw = renpy.random.randint(1, 10) #Addying point to Ravenclaw (07_points_gry.rpy)

$ one_out_of_three = renpy.random.randint(1, 3) #Generating one number out of three for various porpoises.
$ i_of_iv = renpy.random.randint(1, 4) #Generating one number out of three for various porpoises.
$ one_of_five = renpy.random.randint(1, 5) #Generating one number out of three for various porpoises.
$ i_of_vii = renpy.random.randint(1, 7)
$ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.
$ one_of_tw = renpy.random.randint(1, 20) #Generating one number out of three for various porpoises.

$ day_random = renpy.random.randint(0, 10)

if day_random in [0,1,2]:
    call set_ast_susan_name
if day_random in [3,4,5]:
    call set_ast_tonks_name
if day_random in [6,7,8]:
    call set_ton_astoria_name
if day_random in [9,10]:
    pass

### CUPBOARD MONEY GENERATOR ###

if game_difficulty <= 1: #Easy difficulty
    $ gold1 = renpy.random.randint(8, 20) # Money you find in the cupboard when Whoring Level: 1-2.
    $ gold2 = renpy.random.randint(20, 80) # Money you find in the cupboard when Whoring Level: 3-4.
    $ gold3 = renpy.random.randint(40, 100) # Money you find in the cupboard when Whoring Level: 5-6.
    $ gold4 = renpy.random.randint(60, 180) # Money you find in the cupboard when Whoring Level: 7+.
else: #Normal (2) & hardcore (3) difficulty
    $ gold1 = renpy.random.randint(5, 15)
    $ gold2 = renpy.random.randint(15, 60)
    $ gold3 = renpy.random.randint(30, 75)
    $ gold4 = renpy.random.randint(45, 135)


scene black




### DAILY COUNTERS ###
$ days_without_an_event +=1

if day_of_week == 7: #Counts days of the week. Everyday +1. When day_of_week = 7 resets to zero.
    $ day_of_week = 0
    if finished_report >= 1:
        $ letter_paperwork_report_OBJ.mailLetter()

$ day_of_week += 1

$ day +=1

### MOOD ###
if game_difficulty <= 1:   # Easy difficulty
    if her_mood >= 1:
        $ her_mood -= 3
    if cho_mood >= 1:
        $ cho_mood -= 3
elif game_difficulty == 2: # Normal difficulty
    if her_mood >= 1:
        $ her_mood -= 2
    if cho_mood >= 1:
        $ cho_mood -= 2
else:                      # Hardcore # Gifting items is required!
    pass

if her_mood < 0:
    $ her_mood = 0
if cho_mood < 0:
    $ cho_mood = 0



### WEATHER
stop bg_sounds #Stops playing the fire SFX.
stop weather #Stops playing the rain SFX.
if day != 1:
    $ weather_gen = renpy.random.randint(1, 6)

# Quidditch Matches
if start_match == 1:
    $ weather_gen = 1
$ show_weather()



# Mail
if deliveryQ.got_mail():
    $ package_is_here = True

if clothing_mail_item != None:
    $ clothing_mail_timer -= 1

    if clothing_mail_timer <= 1:
        $ package_is_here = True

if day >= 2 and not letter_from_hermione_B_OBJ.read:
    $ letter_from_hermione_B_OBJ.mailLetter()

if day >= 12 and not letter_paperwork_unlock_OBJ.read:
    $ letter_paperwork_unlock_OBJ.mailLetter()

if day >= 25 and her_whoring >= 9 and not letter_curse_complaint_OBJ.read:
    $ letter_curse_complaint_OBJ.mailLetter()

if day >= 26 and not deck_unlocked:
    $ letter_deck.mailLetter()

if day >= twins_cards_delay and deck_unlocked and twins_first_win and not twins_cards_stocked:
    $ letter_cards_store.mailLetter()

if geniecard_level < 2 and snape_third_win and her_third_win and twins_second_win:
    $ letter_cardgame_t2.mailLetter()

if package_is_here or letter_queue_list != []:
    play sound "sounds/owl.mp3"


call room("main_room", hide_screens=False) #Screens already get hidden above.

hide screen blkfade
with fade

call points_changes #Makes house points changes.
call house_points




#EVENTS

label day_resume:

# Cho Events.
if day >= 18 and her_whoring >= 2 and days_without_an_event >= 1 and not cho_intro_1_complete:
    $ days_without_an_event = 0
    $ cho_intro_1_complete = True
    jump cho_intro_1

if huffl_matches_won == 1 and quidditch_commentator == "None":
    $ lock_cho_practice = True
    $ quidditch_commentator = "Ask Hermione"
    jump quidditch_commentator_event_1

# Quidditch Matches.
if start_match == 1 and days_without_an_event >= 1:
    $ start_match = 0 # Reset
    jump hufflepuff_match


if day == 7:
    call event_08 #Hermione shows up for the first time.
if (day >= 8 or day >= 12) and hermione_is_waiting_01 and not event09:
    call event_09 #Second visit from Hermione. Says she sent a letter to the Minestry.
                  #Takes place after first special event with Snape, where he just complains about Hermione.
if event13_happened and not event14_happened:
    call event_14 #Returns



#Astoria Intro.
if hermione_finds_astoria and days_without_an_event >= 2 and not astoria_unlocked:
    $ astoria_unlocked = True
    $ days_without_an_event = 0
    jump astoria_captured_intro


if her_whoring >= 15 and not event_chairman_happened: #Turns True after an event where Hermione comes and says that she wants to be in the Autumn Ball committee.
    call want_to_rule #Returns

if her_whoring >= 15 and event_chairman_happened and days_without_an_event >= 2 and not snape_against_chairman_hap: # Turns TRUE after Snape comes and complains that appointing Hermione in the Autumn Ball committee was a mistake.
    jump against_the_rule #No return.

if her_whoring >= 18 and days_without_an_event >= 5 and snape_against_chairman_hap and not have_no_dress_hap: #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    call crying_about_dress #Returns

if her_whoring >= 18 and have_no_dress_hap and not sorry_for_hesterics and days_without_an_event >= 1: # Turns TRUE after Hermione comes and apologizes for the day (event) before.
    call sorry_about_hesterics #Returns



#Luna events.
if her_whoring >= 21 and not hat_known:
    call hat_intro #Returns

if luna_reverted and lun_corruption == -2 and days_to_luna <= 0:
    $ days_without_an_event = 0
    jump luna_reverted_greeting_1 #Sets lun_corruption to -1, returns next night.

if luna_reverted and lun_corruption >= 0 and days_to_luna <= 0:
    if luna_reverted and lun_corruption == 0:
        $ days_without_an_event = 0
        jump luna_reverted_event_1
    elif luna_reverted and lun_corruption == 1:
        $ days_without_an_event = 0
        jump luna_reverted_event_2
    elif luna_reverted and lun_corruption == 2:
        $ days_without_an_event = 0
        jump luna_reverted_event_3
    else:
        pass

### NOT IN USE
#if day == 10:
#    call event_08_02 #Hermione shows up for the second time. (Shorter skirts notion).
#if day == 11:
#    call event_08_03 #Hermione shows up for the third time. (Rules for teachers noton).

### NOT IN USE
#if day >= 13 and not event10 and hermione_is_waiting_02:
#    call event_10 #Hermione shows up for the third time. Says that she started "MRM" and sent letter to the ministry.

if collar == 5:
    $ days_without_an_event = 0
    jump collar_scene

if hg_pr_SexWithClassmate_AltFlag:#Hermione does not show up. This sends to label where she shows up next morning.
    call hg_pr_SexWithClassmate_Alt



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



### CHEATS / SKIPPING ###
if skip_duel or skip_to_hermione:
    $ bird_examined = True
    $ desk_examined = True
    $ cupboard_examined = True
    $ door_examined = True
    $ fireplace_examined = True
    if skip_duel:
        $ skip_duel = False
        $ rum_times = 3 #7 unlocks map!
        $ day = 5

    if skip_to_hermione:
        $ skip_to_hermione = False
        #Add vars
        $ snape_unlocked = True
        $ event08_happened = True
        $ event09 = True #You let Hermione in. This event will stop looping now.
        $ hermione_is_waiting_01 = False #Makes sure this event is not repeated.
        $ event11_happened = True #Allows next event to start.
        $ event12_happened = True #Allows next event to start.
        $ event13_happened = True #Allows next event to start.
        $ rum_times = 6 #7 unlocks map!

        if day < 14:
            $ day = 14
        call event_14 #returns

### EVENTS ### (COMMENTED OUT FOR THE TESTING PORPOISES) ===============================================================================================================================
if day == 1 and not bird_examined and not desk_examined and not cupboard_examined and not door_examined and not fireplace_examined:
    call event_01 #Returns

### Guide ###
call update_hints





label day_main_menu:

### MENU PLACEMENT ###
$ menu_x = 0.5
$ menu_y = 0.5

if day == 1 and daytime and bird_examined and desk_examined and cupboard_examined and door_examined and fireplace_examined:
    show screen bld1
    with d3
    m "It's getting darker already..."
    m "Did I just spend an entire day examining this room?"
    hide screen bld1
    with d3
    jump night_start

hide screen bld1
hide screen blktone
call hide_characters
with d1

call screen main_room_menu
