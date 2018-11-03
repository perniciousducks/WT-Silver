
###DAY STARTS HERE###<<<<<<<<<<<<<<<<<<<-----------------------------------------------------------------------------------###
###========================================================================================================================###
label day_start:
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY THEME
#    $ renpy.set_style_preference("dialog", "Day")

### RESETING STUFF ###


call gen_chibi("hide")
call her_chibi("hide")
call sna_chibi("hide")

$ chitchated_with_her = False
$ chitchated_with_astoria = False
$ chitchated_with_susan = False
$ chitchated_with_snape = False
$ chitchated_with_tonks = False

$ gifted    = False #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
$ searched  = False #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.
$ temp_name = "Day - "+str(day)+"\nWhoring - "+str(whoring)
$ save_name = temp_name



#Hermione Daily Flags.
$ hermione_busy = False
$ hermione_door_event_happened = False
call reset_hermione_main
$ flip = False
$ no_blinking   = False #When True - blinking animation is not displayed.
$ sperm_on_tits = False #Sperm on tits when Hermione pulls her shirt up.
$ uni_sperm     = False
$ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.

if hermione_expand_breasts_counter != 0:
    $ hermione_expand_breasts_counter -= 1
else:
    $ hermione_expand_breasts = False

if hermione_expand_ass_counter != 0:
    $ hermione_expand_ass_counter -= 1
else:
    $ hermione_expand_ass = False


#Luna Daily Flags.
$ luna_busy = False
$ days_to_luna-= 1

#Astoria Daily Flags.
$ astoria_busy = False

#Susan Daily Flags.
$ susan_busy = False
if susan_imperio_counter > 0:
    $ susan_imperio_counter -= 1            #Removes 1 at each new day.
    $ susan_imperio_influence = True
    if susan_imperio_counter <= 0:
        $ susan_imperio_influence = False
        $ reset_susans_wardrobe = True
        call susan_init
        $ reset_susans_wardrobe = False

#Cho Daily Flags.
$ cho_busy = False
if cho_known:
    $ days_since_cho += 1
if cho_quidd:
    $ days_since_quidd += 1

#Tonks Daily Flags.
$ tonks_busy = False

#Snape Daily Flags.
$ snape_busy = False



$ phoenix_is_feed = False #At the beginning of every new day Phoenix is not fed.

stop bg_sounds #Stops playing the fire SFX.
stop weather #Stops playing the rain SFX.

hide screen notes #A bunch of notes poping out with a "win" sound effect.
hide screen phoenix_food
hide screen done_reading
hide screen done_reading_near_fire
hide screen fireplace_glow
hide screen bld1
hide screen blktone
hide screen blkfade


if whoring >= 12 and not touched_by_boy and not force_unlock_pub_favors: #Turns true if sent Hermione to get touched by a boy at least once.
    $ lock_public_favors = True #Turns True if reached whoring level 05 while public event "Touched by boy" never attempted. Locks public events.
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
hide screen main_room
hide screen weather

$ daytime = True #True when it is daytime. Turns False during nighttime.
$ interface_color = "gold"


$ fire_in_fireplace = False
hide screen fireplace_fire


### DAILY COUNTERS ###
$ days_without_an_event +=1

if day_of_week == 7: #Counts days of the week. Everyday +1. When day_of_week = 7 resets to zero.
    $ day_of_week = 0
    if finished_report >= 1:
        $ got_paycheck = True #When TRUE the paycheck is in the mail. Can't do paper work.
        $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
        #$ got_mail = True comented out because being replaced with $ letters += 1

$ day_of_week += 1

### MOOD ###
if game_difficulty <= 1:   # Easy difficulty
    if mad >= 1:
        $ mad -= 3
    if cho_mad >= 1:
        $ cho_mad -= 3
elif game_difficulty == 2: # Normal difficulty
    if mad >= 1:
        $ mad -= 2
    if cho_mad >= 1:
        $ cho_mad -= 2
else:                      # Hardcore # Gifting items is required!
    pass

if mad < 0:
    $ mad == 0
if cho_mad < 0:
    $ cho_mad == 0



if deliveryQ.got_mail():
    $ package_is_here = True



$ raining = False #No rain before the weather has been chosen at the beginning of every day.
hide screen new_window #Hiding clear sky bg.

### WEATHER
$ weather_gen = renpy.random.randint(1, 6)
$ show_weather()
show screen weather

hide screen candlefire

hide screen chair_left
hide screen chair_right
hide screen fireplace
hide screen genie
hide screen owl
hide screen owl_02
hide screen with_snape #Genie hangs out with Snape in front of the fireplace.
hide screen with_snape_animated #Genie hangs out with Snape in front of the fireplace.
if package_is_here:
    hide screen package

show screen main_room
show screen chair_right
show screen fireplace

show screen genie


### DAY MAIL ###
if day == 2:
    $ letter_from_hermione_02 = True #Turns true when you get second letter from Hermione.
    $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.

if day == 12: # LETTER THAT UNLOCKS PAPERWORK BUTTON.
    $ work_unlock = True # Send a letter that will unlock an ability to write reports.
    $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.

#Astoria intro.
if day >= 25 and whoring >= 9 and not ministry_letter_received:
    $ ministry_letter = True
    $ letters += 1 #Displays Owl

if day >= 26 and not deck_unlocked:    
    $ deck_mail_send = True
    $ letters += 1 #Displays Owl
    
if outfit_order_placed and not outfit_ready:
    call outfit_purchase_check

if package_is_here:
    play sound "sounds/owl.mp3"  #Quiet...
    show screen package

if got_mail or mail_from_her or letters >= 1:
    play sound "sounds/owl.mp3"  #Quiet...
    show screen owl

hide screen points
show screen points

with fade

$ day +=1

call points_changes #Makes house points changes.




#EVENTS

label day_resume:

#Cho Events. They happen first because Cho wakes up at 5 in the morning apparently.
if days_since_cho == 1 and days_without_an_event >= 1:
    $ days_without_an_event = 0
    jump hermione_cho
if days_since_cho == 2 and days_without_an_event >= 1 and not cho_unlocked:
    $ days_without_an_event = 0
    jump cho_intro_2

if days_since_cho >= 8 and not cho_quidd:
    $ cho_quidd = True
    jump cho_quidd_intro



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


if whoring >= 15 and not event_chairman_happened: #Turns True after an event where Hermione comes and says that she wants to be in the Autumn Ball committee.
    call want_to_rule #Returns

if whoring >= 15 and event_chairman_happened and days_without_an_event >= 2 and not snape_against_chairman_hap: # Turns TRUE after Snape comes and complains that appointing Hermione in the Autumn Ball committee was a mistake.
    jump against_the_rule #No return.

if whoring >= 18 and days_without_an_event >= 5 and snape_against_chairman_hap and not have_no_dress_hap: #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    call crying_about_dress #Returns

if whoring >= 18 and have_no_dress_hap and not sorry_for_hesterics and days_without_an_event >= 1: # Turns TRUE after Hermione comes and apologizes for the day (event) before.
    call sorry_about_hesterics #Returns



#Luna events.
if whoring >= 21 and not hat_known:
    call hat_intro #Returns

if luna_reverted and luna_corruption == -2 and days_to_luna <= 0:
    $ days_without_an_event = 0
    jump luna_reverted_greeting_1 #Sets luna_corruption to -1, returns next night.

if luna_reverted and luna_corruption >= 0 and days_to_luna <= 0:
    if luna_reverted and luna_corruption == 0:
        $ days_without_an_event = 0
        jump luna_reverted_event_1
    elif luna_reverted and luna_corruption == 1:
        $ days_without_an_event = 0
        jump luna_reverted_event_2
    elif luna_reverted and luna_corruption == 2:
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



if whoring == 11 and not touched_by_boy and not ignore_warning:
    call nar("!!! Attention !!!","start")
    ">Increasing Hermione's whoring level any further without doing more public requests will lock your game to a specific ending."
    ">This message will repeat until you increase her whoring level, or do a certain number of public requests!"
    call nar(">You should also save your game here.","end")
    menu:
        "-Understood-":
            pass
        "-Don't tell me what to do!-":
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

        $ work_unlock = True # Send a letter that will unlock the ability to write reports.
        $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
        play sound "sounds/owl.mp3"  #Quiet...
        show screen owl

### EVENTS ### (COMMENTED OUT FOR THE TESTING PORPOISES) ===============================================================================================================================
if day == 1 and not bird_examined and not desk_examined and not cupboard_examined and not door_examined and not fireplace_examined:
    call event_01 #Returns

### Guide ###
call update_hints





label day_main_menu:

### MENU PLACEMENT ###
$ menu_x = 0.5
$ menu_y = 0.5

if phoenix_is_feed:
    show screen phoenix_food

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

show screen animation_feather
call screen main_room_menu
