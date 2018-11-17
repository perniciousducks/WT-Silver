

label map_init:

    if not hasattr(renpy.store,'her_map_location') or reset_persistants:
        label reset_map_init:

        $ map_unlocked = False

        $ her_map_location = "library"
        $ lun_map_location = "room_r"
        $ ast_map_location = "room_s"
        $ sus_map_location = "room_h"
        $ cho_map_location = "training_grounds"

        $ sna_map_location = "potions"
        $ ton_map_location = "defense"

        $ first_time_7th = True
        $ pitch_open = True
        $ inn_intro = False
        $ attic_open = False

    return



label leave_main_room:
    hide screen main_room_menu
    hide screen main_room
    hide screen chair_right
    hide screen fireplace
    hide screen candlefire
    hide screen desk
    hide screen phoenix_food
    hide screen owl
    hide screen genie
    return



### Map Screen ###

screen map_screen:
    zorder 4

    $ UI_xpos_offset = 140

    add "interface/map/map.png" xpos UI_xpos_offset ypos 0

    #Office
    imagebutton:
        xpos 0 +UI_xpos_offset
        ypos 0
        focus_mask True
        idle "interface/map/room_office_idle.png"
        hover "interface/map/room_office_hover.png"
        action Return("main_room")

    #Weasley Store
    imagebutton:
        xpos 0+UI_xpos_offset
        ypos 0
        focus_mask True
        idle "interface/map/room_weasley_store_idle.png"
        hover "interface/map/room_weasley_store_hover.png"
        action Return("open_weasley_store")

    #Clothing Store
    imagebutton:
        xpos 0+UI_xpos_offset
        ypos 0
        focus_mask True
        idle "interface/map/room_clothing_store_idle.png"
        hover "interface/map/room_clothing_store_hover.png"
        action Return("clothes_store")

    #Potions
    imagebutton:
        xpos 0+UI_xpos_offset
        ypos 0
        focus_mask True
        idle "interface/map/room_potions_idle.png"
        #hover "interface/map/room_potions_hover.png"
        #action Return("potions_room")

    #Room of Requirement
    imagebutton:
        xpos 0+UI_xpos_offset
        ypos 0
        focus_mask True
        if unlocked_7th:
            idle "interface/map/room_ror_idle.png"
            hover "interface/map/room_ror_hover.png"
        else:
            idle "interface/map/room_ror_empty_idle.png"
            hover "interface/map/room_ror_empty_hover.png"
        action Return("floor_7th")

    #Lake
    imagebutton:
        xpos 0+UI_xpos_offset
        ypos 0
        focus_mask True
        idle "interface/map/room_boat_house_idle.png"
        hover "interface/map/room_boat_house_hover.png"
        action Return("map_lake")

    #Forest (Temporary until we have a map for the nothern section!)
    imagebutton:
        xpos 0+UI_xpos_offset
        ypos 0
        focus_mask True
        idle "interface/map/room_north_courtyard_idle.png"
        hover "interface/map/room_north_courtyard_hover.png"
        action Return("map_forest")

    # (X upper-left corner, Y upper-left corner, width, height).
    #hotspot (189, 218, 38, 20) clicked Return("map_attic") #attic
    #hotspot (275, 449, 75, 15) clicked Return("map_dorms") #dorms

    #Map Events
    #if her_whoring >= 21 and one_of_five in [1,2,3] and weather_gen < 5 and not daytime and not hermione_busy: #Increased change for event. Won't happen during the rain.
    #    hotspot (227, 442, 55, 55) clicked Return("hermione_map_BJ")


label set_her_map_location(location = ""):
    #her_random_number (1-5), gets defined once during the day and once during the nigh.
    if location != "":
        if location == "library":
            $ her_map_location = "library"
        elif location in ["gryffindor_room","gryff_room","room_g"]:
            $ her_map_location = "room_g"
        elif location in ["slytherin_room","slyth_room","room_s"]:
            $ her_map_location = "room_s"
        elif location == "great_hall":
            $ her_map_location = "great_hall"
        elif location == "courtyard":
            $ her_map_location = "courtyard"

    else: #Random
        if her_whoring < 11:
            if her_random_number in [1,2]: #Library
                $ her_map_location = "library"
            elif her_random_number in [3]: #Great Hall
                $ her_map_location = "great_hall"
            else: #Gryff Room
                $ her_map_location = "room_g"
        else:
            if lock_public_favors:
                if her_random_number == 1: #Great Hall
                    $ her_map_location = "great_hall"
                elif her_random_number == 2: #Courtyard
                    $ her_map_location = "courtyard"
                else: #Gryff Room
                    $ her_map_location = "room_g"
            else:
                if her_random_number == 1: #Slytherin Room
                    $ her_map_location = "room_s"
                elif her_random_number == 2: #Courtyard
                    $ her_map_location = "courtyard"
                else: #Gryff Room
                    $ her_map_location = "room_g"

    call update_character_map_locations

    return

label set_cho_map_location(location = ""):
    #cho_random_number (1-5), gets defined once during the day and once during the nigh.
    if location != "":
        if location == "training_grounds":
            $ cho_map_location = "library"
        elif location in ["ravenclaw_room","raven_room","room_r"]:
            $ cho_map_location = "room_r"

    else: #Random
        if her_random_number in [1,2]: #Library
            $ cho_map_location = "training_grounds"
        else: #Ravenclaw Room
            $ cho_map_location = "room_r"

    call update_character_map_locations

    return

label update_character_map_locations:
    if her_map_location == "library":
        $ her_map_xpos = 622
        $ her_map_ypos = 118
    if her_map_location == "room_g":
        $ her_map_xpos = 156
        $ her_map_ypos = 269
    if her_map_location == "room_s":
        $ her_map_xpos = 255
        $ her_map_ypos = 156
    if her_map_location == "great_hall":
        $ her_map_xpos = 27
        $ her_map_ypos = 370
    if her_map_location == "courtyard":
        $ her_map_xpos = 539
        $ her_map_ypos = 263

    #Cho
    if cho_map_location == "room_r":
        $ cho_map_xpos = 406
        $ cho_map_ypos = 339
    if cho_map_location == "training_grounds":
        $ cho_map_xpos = 691
        $ cho_map_ypos = 65

    #Tonks
    $ ton_map_xpos = 427
    $ ton_map_ypos = 222

    #Snape
    $ sna_map_xpos = 488
    $ sna_map_ypos = 480

    return


screen map_screen_characters:
    zorder 5

    $ UI_xpos_offset = 140

    #Hermione
    if hermione_unlocked:
        imagebutton:
            xpos her_map_xpos +UI_xpos_offset
            ypos her_map_ypos
            focus_mask True
            idle "interface/map/name_hermione.png"
            hover "interface/map/name_hermione_hover.png"
            action Return("hermione")

    #Cho
    if cho_unlocked:
        imagebutton:
            xpos cho_map_xpos +UI_xpos_offset
            ypos cho_map_ypos
            focus_mask True
            idle "interface/map/name_cho.png"
            hover "interface/map/name_cho_hover.png"
            action Return("cho")

    #Snape
    if snape_unlocked:
        imagebutton:
            xpos sna_map_xpos +UI_xpos_offset
            ypos sna_map_ypos
            focus_mask True
            idle "interface/map/name_snape.png"
            hover "interface/map/name_snape_hover.png"
            action Return("snape")

    #Tonks
    if tonks_unlocked:
        imagebutton:
            xpos ton_map_xpos +UI_xpos_offset
            ypos ton_map_ypos
            focus_mask True
            idle "interface/map/name_tonks.png"
            hover "interface/map/name_tonks_hover.png"
            action Return("tonks")


label floor_7th:
    if unlocked_7th == False:
        m"\"I don't have any reason to go there...\""
        jump door
    else:
        call blkfade
        call leave_main_room
        show screen floor_7th_screen


        if unlocked_7th and first_time_7th:
            call gen_chibi(xpos="door", ypos="base", flip=True)
            call hide_blkfade
            $ first_time_7th=False
            m"So... he was walking around here."
            call gen_chibi(action="hide")
            call gen_walk(pos1="door", pos2="200")
            m"I can definitely sense a strong magical energy in this place..."
            call gen_walk(pos1="200", pos2="door")
            m"Maybe if I...or I could..."
            call gen_walk(pos1="door", pos2="100")
            g11"I could be in my office jacking off right now!!"
            show screen room_of_req_door
            pause 1
            call gen_chibi(xpos="100", ypos="base")
            g9"Well... will you look at that"
            hide screen room_of_req_door
            show screen floor_7th_door
            call screen floor_7th_menu
        else:
            call gen_chibi(xpos="100", ypos="base")
            show screen floor_7th_door
            call hide_blkfade
            call screen floor_7th_menu

label map_attic: #Label controlling what happens when you access the attic
    if not attic_open:
        ">You venture up to the attic but find that the door is locked."
        m "Damn, it's locked."
        m "Guess I'll have to ask Snape about a key."
        jump return_office
    if attic_open and tentacle_owned:
        ">You venture up to the attic and find an angry tentacle plant."
        m "Better get out of here before the plant remembers that I'm the one that cut it."
        ">You quickly return to your office."
        jump return_office
    else: #Scene where genie has to take a sample of the devil's snare plant
        ">You find your way through the winding staircases to the attic door."
        m "Hmmmmm, it seems to be open."
        ">You walk through the dusty room, light softly cascading though the windows."
        m "Well where's this magical plant?"
        ">A slender piece of vine is visible, skirting the room, as if to avoid the light."
        m "This must be it."
        ">You cut a piece and leave."
        ">As you shut the door you hear the room erupt in a series of loud crashes."
        $ tentacle_owned = True
        jump return_office


label map_forest: #Label controlling what happens when you go to the forest
    if daytime:
        m "I shouldn't be leaving the castle during the day. It's too risky..."
        jump door
    else:
        pass

    call outskirts_of_hogwarts

    m "Lets see what I can find out here..."

    menu:
        "-Search the area-":
            $ ran = renpy.random.random()
            if ran < 0.3:
                ">You search around the forest and manage to find an odd looking herb."
                m "This must be wormwood."
                menu:
                    "-Take the wormwood-":
                        ">You gain 1 wormwood."
                        $ potion_inv.add("ing_wormwood")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            elif ran < 0.6:
                ">You search around the forest and manage to find an odd looking herb."
                m "This must be Knotgrass."
                menu:
                    "-Take the Knotgrass-":
                        ">You gain 1 Knotgrass."
                        $ potion_inv.add("ing_knotgrass")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            else:
                ">You search around the forest but find nothing of interest."
                jump return_office

label map_lake: #Label controlling what happens when you go to the lake
    if daytime:
        m "I shouldn't be leaving the castle during the day. It's too risky..."
        jump door
    else:
        pass
    call outskirts_of_hogwarts

    m "Lets see what I can find out here..."

    menu:
        "-Search the area-":
            $ ran = renpy.random.random()
            if ran < 0.3:
                ">You search around the lake and manage to find an slender, green vine."
                m "This must be Niffler's fancy."
                menu:
                    "-Take the Niffler's fancy-":
                        ">You gain 1 Niffler's fancy."
                        $ potion_inv.add("ing_niffler_fancy")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            elif ran < 0.6:
                ">You search around the lake and manage to find an exposed root that looks similar to ginger."
                m "This must be Root of Aconite."
                menu:
                    "-Take the Root of Aconite-":
                        ">You gain 1 Root of Aconite."
                        $ potion_inv.add("ing_aconite_root")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            else:
                ">You search around the lake but find nothing of interest."
                jump return_office

label map_dorms: #Label controlling what happens when you go to the dorms
    menu:
        "-Search the area-":#Luna's Hair
            $ ran = renpy.random.random()
            if ran < 0.3:
                ">You search around the dorms and manage to find a clump for bright orange fur."
                m "This must belong to some sort of animal."
                menu:
                    "-Take the Fur-":
                        ">You gain 1 Cat Fur."
                        $ potion_inv.add("ing_cat_hair")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            elif ran < 0.6:
                ">You search around the dorms and manage to find an comb with some hair in it."
                m "This must be someones hair."
                menu:
                    "-Take the hair-":
                        ">You gain 1 Luna's Hair."
                        $ potion_inv.add("ing_luna_hair")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            else:
                ">You search around the dorms but find nothing of interest."
                jump return_office

label map_pitch: #Label controlling what happens when you go to the quidditch pitch
    if pitch_open:
        hoo "Hello Professor Dumbledore, nice to see you out of your office today."
        hoo "What brings you down to the Quidditch pitch today?"
        m "Quidditch, what sort of name is that?" #put in low talking tone
        hoo "What was that?"
        m "Nothing, just commenting about the weather." #Maybe change this
        hoo "Well I'm glad that you're here. I wanted to have words with you about a problem that I'm having at the moment."
        m "What's wrong?"
        hoo "Attendance at quidditch matches has slowly been declining over the last couple of months."
        hoo "Students just don't seem to want to turn up to watch their teams play. It's affecting team morale."
        m "And how would you like to fix this?"
        hoo "Perhaps we could make attendance to the match mandatory."
        m "I don't think that that would work. If I did that you would just end up with a lot of disgruntled students booing your own team."
        m "If poor attendance is affecting morale I would hate to think what that would do to the players."
        hoo "Well then what do you suggest?"
        m "You need a way to attract and excite the crowd. To get the students here and to get them cheering."
        m "What you need is a cheerleading team."
        hoo "A what?"
        m "A team of girls to dance and cheer for their team. To get their fellow students brimming with enthusiasm."
        hoo "I'm not sure Sir, Hogwarts has always been a traditional school."
        hoo "Something like this goes in the face of that legacy."
        m "Well if you feel that way then I think you might just have to accept the declining number of students watching the game."
        hoo "Fine, but I'm not comfortable with a team of these \"\Cheerleaders\"\. At most I'd be comfortable with one girl dancing." #Maybe adjust this so that there is a team
        m "Well I think I have the perfect candidate. I'll send her over next practice session to try out."
        hoo "Okay, just make sure she's wearing something appropriate."
        $ pitch_first = False
        jump return_office
    else:
        ">You look around the open field but can't see any students or teachers"
        m "Mustn't be a practice day."
        jump return_office

label outskirts_of_hogwarts:
    call blkfade
    hide screen genie
    show screen chair_left
    show screen desk
    call gen_chibi("stand","desk","base")
    call hide_blkfade

    call gen_walk("desk","leave",3)
    call blkfade

    stop music fadeout 1.0

    centered "{size=+7}{color=#cbcbcb}Outskirts of hogwarts{/color}{/size}"

    play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.

    show screen blkback # Hide room

    $ end_u_1_pic =  "images/yule_ball/171.png"
    show screen end_u_1
    pause.3
    call hide_blkfade
    pause.8
    $ renpy.play('sounds/steps_grass.mp3') # SOUNDS OF STEPS IN THE GRASS.
    $ end_u_3_pic =  "images/yule_ball/172.png"
    show screen end_u_3
    with d7

    return


label return_office:
    call hide_characters
    show screen blkfade
    with d3
    #">You return to your office."

    hide screen ccg
    hide screen end_u_1
    hide screen end_u_3
    hide screen chair_left
    hide screen desk
    call her_chibi("hide")
    call sna_chibi("hide")
    call gen_chibi("hide")
    show screen main_room
    show screen genie
    hide screen blkback

    pause.5
    hide screen blkfade
    with d5


    $ menu_x = 0.5
    $ menu_y = 0.5

    if daytime:
        call play_music("day_theme")
    else:
        call play_music("night_theme")

    pause.5

    if daytime:
        jump day_resume
    else:
        jump night_resume
