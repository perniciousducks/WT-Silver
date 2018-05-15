
###DAY STARTS HERE###<<<<<<<<<<<<<<<<<<<-----------------------------------------------------------------------------------###
###========================================================================================================================###
label day_start:
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY THEME
#    $ renpy.set_style_preference("dialog", "Day")

### RESETING STUFF ###

call reset_hermione_main

call gen_chibi("hide")
call her_chibi("hide")
call sna_chibi("hide")

$ flip = False
$ chitchated_with_her = False #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
$ chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night and every day.

$ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
$ gifted    = False #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
$ searched  = False #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.
$ temp_name = "Day - "+str(day)+"\nWhoring - "+str(whoring)
$ save_name = temp_name

call luna_day_flags
$ only_upper    = False #When true, legs are not displayed in the hermione_main screen.
$ autograph     = False #Displays professor Lockhart's autograph on Hermione's leg.
$ no_blinking   = False #When True - blinking animation is not displayed.
$ sperm_on_tits = False #Sperm on tits when Hermione pulls her shirt up.
$ aftersperm    = False #Shows cum stains on Hermione's uniform.
$ uni_sperm     = False

$ phoenix_is_feed = False #At the beginning of every new day Phoenix is not fed.
$ day_random = renpy.random.randint(0, 10)

stop bg_sounds #Stops playing the fire SFX.
stop weather #Stops playing the rain SFX.

hide screen notes #A bunch of notes poping out with a "win" sound effect.
hide screen phoenix_food
hide screen done_reading
hide screen done_reading_02
hide screen candlefire_01 #CANDLE FIRE.
hide screen candlefire_02 #CANDLE FIRE.
hide screen lightening #Hide lighting so it won't get stuck during clear sky weather and such.
hide screen cloud_night_01 #NIGHT CLOUDS.
hide screen cloud_night_02 #NIGHT CLOUDS.
hide screen cloud_night_03 #NIGHT CLOUDS.

hide screen bld1
hide screen blktone
hide screen blkfade

if whoring >=  0 and whoring <  3:
    $ level = "01"
if whoring >=  3 and whoring <  6:
    $ level = "02"
if whoring >=  6 and whoring <  9:
    $ level = "03"
if whoring >=  9 and whoring < 12:
    $ level = "04"
if whoring >= 12 and whoring < 15:
    $ level = "05"

if whoring >= 15 and whoring < 18:
    $ level = "06"

if whoring >= 18 and whoring < 21:
    $ level = "07"

if whoring >= 21 and whoring < 24:
    $ level = "08"

if whoring >= 24 and whoring < 27:
    $ level = "09"

if whoring >= 27 and whoring < 30:
    $ level = "10"

if whoring >= 12 and not touched_by_boy and not force_unlock_pub_favors: #Turns true if sent Hermione to get touched by a boy at least once.
    $ lock_public_favors = True #Turns True if reached whoring level 05 while public event "Touched by boy" never attempted. Locks public events.
else:
    $ lock_public_favors = False

if imagination == 5 and whoring >= 24 and not lock_public_favors: #Unlocks blowjob/sex with teacher personal favours.
    $ imagination = 6

call update_hints

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



$ daytime = True #True when it is daytime. Turns False during nighttime.
$ interface_color = "gold"

$ hermione_sleeping = False
$ hermione_takes_classes = False
$ hermione_door_event_happened = False

$ snape_busy = False

$ fire_in_fireplace = False
hide screen fireplace_fire


### DAILY COUNTERS ###

$ days_without_an_event +=1

#Temporary Breasts and Ass expansion.
if hermione_expand_breasts_counter != 0:
    $ hermione_expand_breasts_counter -= 1
else:
    $ hermione_expand_breasts = False
    
if hermione_expand_ass_counter != 0:
    $ hermione_expand_ass_counter -= 1
else:
    $ hermione_expand_ass = False
    


### PAPERWORK (MONEY-MAKING) RELATED FLAGS ###
if day_of_week == 7: #Counts days of the week. Everyday +1. When day_of_week = 7 resets to zero.
    $ day_of_week = 0
    if finished_report >= 1:
        $ got_paycheck = True #When TRUE the paycheck is in the mail. Can't do paper work.
        $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
        #$ got_mail = True comented out because being replaced with $ letters += 1
$ day_of_week += 1

### HERMIONE ###
if game_difficulty <= 1: #Easy difficulty
    if mad >= 1:
        $ mad -= 3
        if mad <= 0:
            $ mad == 0
else: #Normal (2) $ hardcore (3) difficulty
    if mad >= 1:
        $ mad -= 2
        if mad < 0:
            $ mad == 0


if deliveryQ.got_mail():
    $ package_is_here = True




scene black

$ raining = False #No rain before the weather has been chosen at the beginning of every day.
hide screen new_window #Hiding clear sky bg.
hide screen cloud #THE CLOUD.


$ wather_generator = renpy.random.randint(1, 100)

#Sunny Weather
if wather_generator >=  1 and wather_generator < 41:
    show screen new_window #<<<------------------------------------------!!!!!!!!!!!
    #show image "images/main_room/weather/sunny.png"

#Floating Cloud
elif wather_generator >= 41 and wather_generator < 61:
    show screen new_window #<<<------------------------------------------!!!!!!!!!!!
    show screen cloud
    #show image "images/main_room/weather/sunny.png"
    #show cloud_01 at Position(xpos=280, ypos=215, xanchor="center", yanchor="center")

#Cloudy Weather
elif wather_generator >= 61 and wather_generator < 81:
    show image "images/main_room/weather/cloudy.png" at Position(xpos=290+140, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    $ lighting_generator = renpy.random.randint(1, 2)
    if lighting_generator == 1:
        show lightening at Position(xpos=290+140, ypos=218, xanchor="center", yanchor="center") #Rain animation

#Raining
elif wather_generator >= 81 and wather_generator < 91:
    #play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    $ raining = True
    show image "images/main_room/weather/cloudy.png" at Position(xpos=290+140, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    show rain at Position(xpos=290+140, ypos=218, xanchor="center", yanchor="center") #Rain animation

#Thunder and Lightning!
elif wather_generator >= 91 and wather_generator < 101:
    #play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    $ raining = True
    show image "images/main_room/weather/cloudy.png" at Position(xpos=290+140, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    show lightening at Position(xpos=290+140, ypos=218, xanchor="center", yanchor="center") #Rain animation
    show rain at Position(xpos=290+140, ypos=218, xanchor="center", yanchor="center") #Rain animation


hide screen room_night
show screen room

hide screen door
hide screen cupboard
hide screen chair
hide screen fireplace
hide screen phoenix
hide screen candle_01
hide screen candle_02
hide screen genie
hide screen owl
hide screen owl_02
hide screen with_snape #Genie hangs out with Snape in front of the fireplace.
hide screen with_snape_animated #Genie hangs out with Snape in front of the fireplace.
if package_is_here:
    hide screen package


show screen door
show screen cupboard
show screen chair
show screen fireplace
show screen phoenix
show screen candle_01
show screen candle_02



### DAY MAIL ###
if day == 2:
    $ letter_from_hermione_02 = True #Turns true when you get second letter from Hermione.
    $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.

if day == 12: # LETTER THAT UNLOCKS PAPERWORK BUTTON.
    $ work_unlock = True # Send a letter that will unlock an ability to write reports.
    $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.

if outfit_order_placed and not outfit_ready:
    call outfit_purchase_check

if package_is_here:
    play sound "sounds/owl.mp3"  #Quiet...
    show screen package

show screen genie

if got_mail or mail_from_her or letters >= 1:
    play sound "sounds/owl.mp3"  #Quiet...
    show screen owl

hide screen points
show screen points

with fade

$ day +=1


###4 Houses
call FH_day
if days_since_cho == 2:
    jump hermione_cho
if days_since_cho == 4 and not cho_met:
    jump cho_intro_2
    


#EVENTS

if day == 7:
    call event_08 #Returns #Hermione shows up for the first time.
if (day >= 8 or day >= 12) and hermione_is_waiting_01 and not event09:
    call event_09 #Returns #Second visit from Hermione. Says she sent a letter to the Minestry.
                  #Takes place after first special event with Snape, where he just complains about Hermione.
if event13_happened and not event14_happened:
    call event_14 #Returns

if whoring >= 15 and not event_chairman_happened: #Turns True after an event where Hermione comes and says that she wants to be in the Autumn Ball committee.
    call want_to_rule #Returns

if whoring >= 15 and event_chairman_happened and days_without_an_event >= 2 and not snape_against_chairman_hap: # Turns TRUE after Snape comes and complains that appointing Hermione in the Autumn Ball committee was a mistake.
    jump against_the_rule #No return.

if whoring >= 18 and days_without_an_event >= 5 and snape_against_chairman_hap and not have_no_dress_hap: #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    call crying_about_dress #Returns

if whoring >= 18 and have_no_dress_hap and not sorry_for_hesterics and days_without_an_event >= 1: # Turns TRUE after Hermione comes and apologizes for the day (event) before.
    call sorry_about_hesterics #Returns

#HAT EVENT
if whoring >= 21 and not hat_known:
    call hat_intro #Returns

#Luna event's
if luna_corruption == 10 and luna_reverted:
    jump luna_reverted_greeting_1 #No return.

### NOT IN USE
#if day == 10:
#    call event_08_02 #Hermione shows up for the second time. (Shorter skirts notion).
#if day == 11:
#    call event_08_03 #Hermione shows up for the third time. (Rules for teachers noton).

### NOT IN USE
#if day >= 13 and not event10 and hermione_is_waiting_02:
#    call event_10 #Hermione shows up for the third time. Says that she started "MRM" and sent letter to the ministry.

if skip_duel == True:
    $ day = 5
    $ bird_examined = True 
    $ desk_examined = True
    $ cupboard_examined = True 
    $ door_examined = True
    $ fireplace_examined = True
    $ skip_duel = False
    
### EVENTS ### (COMMENTED OUT FOR THE TESTING PORPOISES) ===============================================================================================================================
if day == 1 and not bird_examined and not desk_examined and not cupboard_examined and not door_examined and not fireplace_examined:
    call event_01 #Returns

if collar == 5:
    jump collar_scene

### Guide ###
#Random Number for Tip/Fact of the Day
$ daily_rndm_tip_or_fact = renpy.random.randint(0, 18)
call update_quests


call Day_Request_Block





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
with d1

show screen animation_feather
call screen main_room_menu
