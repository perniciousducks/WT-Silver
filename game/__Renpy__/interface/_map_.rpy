init python:
    def image_scale(image, zoom=0.5, alpha=1.0):
        #return im.Scale(image, math.ceil(get_width(image)*zoom), math.ceil(get_height(image)*zoom))
        return im.Alpha(im.FactorScale(image, zoom, bilinear=True), alpha)

transform animate:
    alpha 0 # set the value to zero in the start
    time map_ani_time #1.5
    linear 1 alpha 1 # go from zero to 1 in one second

label map_init:
    $ map_scale = 0.7/scaleratio
    $ UI_xpos_offset = 230
    $ UI_ypos_offset = 150

    if not hasattr(renpy.store,'map_ani_time') or reset_persistants:
        label reset_map_init:

        $ map_unlocked = False

        $ her_map_location = "library"
        $ lun_map_location = "room_r"
        $ ast_map_location = "room_s"
        $ sus_map_location = "room_h"
        $ cho_map_location = "training_grounds"

        $ sna_map_location = "room_potions"
        $ ton_map_location = "room_defense"

        $ first_time_7th = True
        $ pitch_open = True
        $ inn_intro = False
        $ attic_open = False

        $ map_ani_time = 1.5

    return

### Map Screen ###
screen map_screen():
    tag map
    zorder 4

    if map_ani_time != 0:
        add "map_unfold" xpos UI_xpos_offset ypos UI_ypos_offset zoom map_scale#Scaled to 588x420
    else:
        add "interface/map/map.png" xpos UI_xpos_offset ypos UI_ypos_offset zoom map_scale#Scaled to 588x420
    use map_buttons
    #use mouse_positions #Shows XY position of the mouse on the screen, updated per click

screen mouse_positions():
    zorder 1
    text str(renpy.get_mouse_pos())

    button:
        xpos 0
        ypos 0
        style "empty"
        action renpy.restart_interaction

image map_unfold:
    "interface/map/anim/map_03.png"
    pause.5
    "interface/map/anim/map_02.png" with Dissolve(0.5)
    pause.5
    "interface/map/anim/map_01.png" with Dissolve(0.5)
    pause.5
    "interface/map/map.png" with Dissolve(0.5)

screen map_buttons():
    tag map
    zorder 4
    #Office
    imagebutton at animate:
        xpos UI_xpos_offset +112
        ypos UI_ypos_offset +234
        idle "interface/map/room_office_idle.png"
        hover "interface/map/room_office_hover.png"
        hovered SetVariable("ball_hint", "office")
        unhovered SetVariable("ball_hint", None)
        action Return("main_room")

    #Gryffindor
    imagebutton at animate:
        xpos UI_xpos_offset +148
        ypos UI_ypos_offset +214
        idle "interface/map/room_gryffindor_idle.png"
        hover "interface/map/room_gryffindor_hover.png"
        hovered SetVariable("ball_hint", "dorm_gryffindor")
        unhovered SetVariable("ball_hint", None)
        action Return("gryffindor_dormitories")

    #Ravenclaw
    imagebutton at animate:
        xpos UI_xpos_offset +286
        ypos UI_ypos_offset +256
        idle "interface/map/room_ravenclaw_idle.png"
        hover "interface/map/room_ravenclaw_hover.png"
        hovered SetVariable("ball_hint", "dorm_ravenclaw")
        unhovered SetVariable("ball_hint", None)
        action Return("ravenclaw_dormitories")

    #Hufflepuff
    imagebutton at animate:
        xpos UI_xpos_offset +76
        ypos UI_ypos_offset +295
        idle "interface/map/room_hufflepuff_idle.png"
        #hovered SetVariable("ball_hint", "dorm_hufflepuff")
        #unhovered SetVariable("ball_hint", None)
        #hover "interface/map/room_hufflepuff_hover.png"
        #action Return("hufflepuff_dormitories")

    #Slytherin
    imagebutton at animate:
        xpos UI_xpos_offset +214
        ypos UI_ypos_offset +136
        idle "interface/map/room_slytherin_idle.png"
        #hovered SetVariable("ball_hint", "dorm_slytherin")
        #unhovered SetVariable("ball_hint", None)
        #hover "interface/map/room_slytherin_hover.png"
        #action Return("slytherin_dormitories")

    #Weasley Store
    imagebutton at animate:
        xpos UI_xpos_offset +246
        ypos UI_ypos_offset +231
        idle "interface/map/room_weasley_store_idle.png"
        hover "interface/map/room_weasley_store_hover.png"
        hovered SetVariable("ball_hint", "weasley_store")
        unhovered SetVariable("ball_hint", None)
        action Return("open_weasley_store")

    #Clothing Store
    imagebutton at animate:
        xpos UI_xpos_offset +462
        ypos UI_ypos_offset +231
        idle "interface/map/room_clothing_store_idle.png"
        hover "interface/map/room_clothing_store_hover.png"
        hovered SetVariable("ball_hint", "clothing_store")
        unhovered SetVariable("ball_hint", None)
        action Return("open_clothing_store")

    #Potions
    imagebutton at animate:
        xpos UI_xpos_offset +314
        ypos UI_ypos_offset +331
        idle "interface/map/room_potions_idle.png"
        unhovered SetVariable("ball_hint", None)
        if store_intro_done:
            hover "interface/map/room_potions_hover.png"
            hovered SetVariable("ball_hint", "potions")
            action Return("potions_room")

    #Room of Requirement
    if unlocked_7th:
        imagebutton at animate:
            xpos UI_xpos_offset +116
            ypos UI_ypos_offset +160
            unhovered SetVariable("ball_hint", None)
            if first_time_7th == True:
                idle "interface/map/room_ror_empty_idle.png"
                hover "interface/map/room_ror_empty_hover.png"
                hovered SetVariable("ball_hint", "room_of_req")
                action Return("floor_7th")
            else:
                idle "interface/map/room_ror_idle.png"
                hover "interface/map/room_ror_hover.png"
                hovered SetVariable("ball_hint", "room_of_req")
                action Return("floor_7th")

    #Lake
    imagebutton at animate:
        xpos UI_xpos_offset +131
        ypos UI_ypos_offset +367
        idle "interface/map/room_boat_house_idle.png"
        hover "interface/map/room_boat_house_hover.png"
        hovered SetVariable("ball_hint", "lake")
        unhovered SetVariable("ball_hint", None)
        action Return("map_lake")

    #Forest
    imagebutton at animate:
        xpos UI_xpos_offset +103
        ypos UI_ypos_offset +12
        idle "interface/map/room_north_courtyard_idle.png"
        hover "interface/map/room_north_courtyard_hover.png"
        hovered SetVariable("ball_hint", "forest")
        unhovered SetVariable("ball_hint", None)
        action Return("map_forest")

    #Attic
    if sealed_scroll_ITEM.unlocked and not tentacle_owned: #Open, not visited yet
        imagebutton at animate:
            xpos UI_xpos_offset +340
            ypos UI_ypos_offset +226
            idle "interface/map/room_attic_closed_idle.png"
            hover "interface/map/room_attic_closed_hover.png"
            hovered SetVariable("ball_hint", "attic")
            unhovered SetVariable("ball_hint", None)
            action Return("map_attic")

    if sealed_scroll_ITEM.unlocked and tentacle_owned: #Open
        imagebutton at animate:
            xpos UI_xpos_offset +340
            ypos UI_ypos_offset +226
            idle "interface/map/room_attic_open_idle.png"
            hover "interface/map/room_attic_open_hover.png"
            hovered SetVariable("ball_hint", "attic")
            unhovered SetVariable("ball_hint", None)
            action Return("map_attic")

    # Map animation toggle
    text "Animation" xpos 630+21 ypos 530+10 size 10 at animate
    imagebutton at animate:
        xpos 630
        ypos 530
        if map_ani_time != 0:
            idle "interface/general/"+str(interface_color)+"/check_true_hidden.png"
            hover "interface/general/"+str(interface_color)+"/check_false.png"
            hovered SetVariable("ball_hint", None)
            unhovered SetVariable("ball_hint", None)
            action SetVariable("map_ani_time", 0)
        else:
            idle "interface/general/"+str(interface_color)+"/check_false_hidden.png"
            hover "interface/general/"+str(interface_color)+"/check_true.png"
            hovered SetVariable("ball_hint", None)
            unhovered SetVariable("ball_hint", None)
            action SetVariable("map_ani_time", 1.5)


    add "interface/map/map_lines_vert.png" xpos UI_xpos_offset ypos UI_ypos_offset zoom map_scale at animate#Add vertical lines overlay

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
            if her_reputation < 12:
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

            if hg_T5_blowjob_trigger == True and one_of_five in [1,2,3] and weather_gen < 5 and not daytime and not hermione_busy:
                $ her_map_location = "forest"

    call update_character_map_locations

    return

label set_lun_map_location(location = ""):
    #lun_random_number (1-5), gets defined once during the day and once during the nigh.
    if location != "":
        if location == "greenhouse":
            $ lun_map_location = "greenhouse"
        elif location == "forest":
            $ lun_map_location = "forest"
        elif location in ["ravenclaw_room","raven_room","room_r"]:
            $ lun_map_location = "room_r"

    else: #Random
        if lun_random_number in [1]:
            $ lun_map_location = "greenhouse"
        elif lun_random_number in [2,3]:
            $ lun_map_location = "forest"
        else: #Ravenclaw Room
            $ lun_map_location = "room_r"

    call update_character_map_locations

    return

label set_ast_map_location(location = ""):
    #ast_random_number (1-5), gets defined once during the day and once during the nigh.
    if location != "":
        if location == "courtyard":
            $ ast_map_location = "courtyard"
        elif location in ["slytherin_room","slyth_room","room_s"]:
            $ ast_map_location = "room_s"
        elif location in ["defense_classroom"]:
            $ ast_map_location = "defense"

    else: #Random
        if ast_random_number in [1,2]:
            $ ast_map_location = "courtyard"
        else: #Slytherin Room
            $ ast_map_location = "room_s"

    call update_character_map_locations

    return

label set_sus_map_location(location = ""):
    #sus_random_number (1-5), gets defined once during the day and once during the nigh.
    if location != "":
        if location == "great_hall":
            $ sus_map_location = "great_hall"
        elif location in ["hufflepuff_room","huffl_room","room_h"]:
            $ sus_map_location = "room_r"

    else: #Random
        if sus_random_number in [1,2]:
            $ sus_map_location = "great_hall"
        else: #Hufflepuff Room
            $ sus_map_location = "room_h"

    call update_character_map_locations

    return

label set_cho_map_location(location = ""):
    #cho_random_number (1-5), gets defined once during the day and once during the nigh.
    if location != "":
        if location == "training_grounds":
            $ cho_map_location = "training_grounds"
        elif location in ["ravenclaw_room","raven_room","room_r"]:
            $ cho_map_location = "room_r"

    else: #Random
        if cho_random_number in [1,2]:
            $ cho_map_location = "training_grounds"
        else: #Ravenclaw Room
            $ cho_map_location = "room_r"

    call update_character_map_locations

    return

label update_character_map_locations:
    if her_map_location == "library":
        $ her_map_xpos = 685
        $ her_map_ypos = 94
    if her_map_location == "room_g":
        $ her_map_xpos = 340
        $ her_map_ypos = 212
    if her_map_location == "room_s":
        $ her_map_xpos = 440
        $ her_map_ypos = 184
    if her_map_location == "great_hall":
        $ her_map_xpos = 300
        $ her_map_ypos = 240
    if her_map_location == "courtyard":
        $ her_map_xpos = 674
        $ her_map_ypos = 216
    if her_map_location == "forest":
        $ her_map_xpos = 290
        $ her_map_ypos = 40

    #Luna
    if lun_map_location == "room_r":
        $ lun_map_xpos = 536
        $ lun_map_ypos = 242
    if lun_map_location == "forest":
        $ lun_map_xpos = 430
        $ lun_map_ypos = 50
    if lun_map_location == "greenhouse":
        $ lun_map_xpos = 680
        $ lun_map_ypos = 320

    #Astoria
    if ast_map_location == "room_s":
        $ ast_map_xpos = 476
        $ ast_map_ypos = 118
    if ast_map_location == "courtyard":
        $ ast_map_xpos = 634
        $ ast_map_ypos = 254
    if ast_map_location == "defense": #Event
        $ ast_map_xpos = 530
        $ ast_map_ypos = 190

    #Susan
    if sus_map_location == "room_h":
        $ sus_map_xpos = 360
        $ sus_map_ypos = 320
    if sus_map_location == "great_hall":
        $ sus_map_xpos = 300
        $ sus_map_ypos = 280

    #Cho
    if cho_map_location == "room_r":
        $ cho_map_xpos = 494
        $ cho_map_ypos = 276
    if cho_map_location == "training_grounds":
        $ cho_map_xpos = 750
        $ cho_map_ypos = 50

    #Tonks
    $ ton_map_xpos = 548
    $ ton_map_ypos = 156

    #Snape
    $ sna_map_xpos = 598
    $ sna_map_ypos = 348

    return


screen map_screen_characters():
    tag map
    zorder 5

    $ UI_xpos_offset = 0

    #Hermione
    if hermione_unlocked:
        imagebutton at animate:
            xpos +UI_xpos_offset +her_map_xpos
            ypos +UI_ypos_offset +her_map_ypos
            xalign 0.5
            yalign 0.5
            idle "interface/map/name_hermione.png"
            hover "interface/map/name_hermione_hover.png"
            hovered SetVariable("ball_hint", "summon_hermione")
            unhovered SetVariable("ball_hint", None)
            action Return("hermione")

    #Luna
    if luna_unlocked:
        imagebutton at animate:
            xpos UI_xpos_offset+ lun_map_xpos
            ypos UI_ypos_offset+ lun_map_ypos
            xalign 0.5
            yalign 0.5
            idle "interface/map/name_luna.png"
            hover "interface/map/name_luna_hover.png"
            hovered SetVariable("ball_hint", "summon_luna")
            unhovered SetVariable("ball_hint", None)
            action Return("luna")

    #Astoria
    if astoria_unlocked:
        imagebutton at animate:
            xpos UI_xpos_offset +ast_map_xpos
            ypos UI_ypos_offset +ast_map_ypos
            xalign 0.5
            yalign 0.5
            idle "interface/map/name_astoria.png"
            hover "interface/map/name_astoria_hover.png"
            hovered SetVariable("ball_hint", "summon_astoria")
            unhovered SetVariable("ball_hint", None)
            action Return("astoria")

    #Susan
    if susan_unlocked:
        imagebutton at animate:
            xpos UI_xpos_offset +sus_map_xpos
            ypos UI_ypos_offset +sus_map_ypos
            xalign 0.5
            yalign 0.5
            idle "interface/map/name_susan.png"
            hover "interface/map/name_susan_hover.png"
            hovered SetVariable("ball_hint", "summon_susan")
            unhovered SetVariable("ball_hint", None)
            action Return("susan")

    #Cho
    if cho_unlocked:
        imagebutton at animate:
            xpos UI_xpos_offset +cho_map_xpos
            ypos UI_ypos_offset +cho_map_ypos
            xalign 0.5
            yalign 0.5
            idle "interface/map/name_cho.png"
            hover "interface/map/name_cho_hover.png"
            hovered SetVariable("ball_hint", "summon_cho")
            unhovered SetVariable("ball_hint", None)
            action Return("cho")

    #Snape
    if snape_unlocked:
        imagebutton at animate:
            xpos UI_xpos_offset +sna_map_xpos
            ypos UI_ypos_offset +sna_map_ypos
            xalign 0.5
            yalign 0.5
            idle "interface/map/name_snape.png"
            hover "interface/map/name_snape_hover.png"
            hovered SetVariable("ball_hint", "summon_snape")
            unhovered SetVariable("ball_hint", None)
            action Return("snape")

    #Tonks
    if tonks_unlocked:
        imagebutton at animate:
            xpos UI_xpos_offset +ton_map_xpos
            ypos UI_ypos_offset +ton_map_ypos
            xalign 0.5
            yalign 0.5
            idle "interface/map/name_tonks.png"
            hover "interface/map/name_tonks_hover.png"
            hovered SetVariable("ball_hint", "summon_tonks")
            unhovered SetVariable("ball_hint", None)
            action Return("tonks")


label floor_7th:
    if unlocked_7th == False:
        m"\"I don't have any reason to go there...\""
        jump desk
    else:
        call blkfade
        call room(hide_screens=True)
        show screen floor_7th_screen

        if unlocked_7th and first_time_7th:
            call gen_chibi(xpos="door", ypos="base", flip=True)
            call hide_blkfade

            $ first_time_7th=False
            m "So... he was walking around here."

            call gen_walk(xpos="200", ypos="base", speed=2.7)

            call bld
            m "I can definitely sense a strong magical energy in this place..."

            call gen_walk(xpos="door", ypos="base", speed=2.7)

            call bld
            m "Maybe if I...or I could..."

            call gen_walk(xpos="120", ypos="base", speed=2.7)

            call bld
            g4 "I could be in my office jacking off right now!!"
            show screen room_of_req_door
            pause 1

            call gen_chibi(xpos="120",ypos="base")
            pause.8

            call bld
            g9 "Well... will you look at that"
            hide screen room_of_req_door
            show screen floor_7th_door
            call screen floor_7th_menu
        else:
            call gen_chibi(xpos="120", ypos="base")
            show screen floor_7th_door
            call hide_blkfade
            call screen floor_7th_menu


label map_attic: #Label controlling what happens when you access the attic
    if not sealed_scroll_ITEM.unlocked:
        ">You venture up to the attic but find that the door is locked."
        m "Damn, it's locked."
        m "Guess I'll have to ask Snape about a key."
        jump desk
    if sealed_scroll_ITEM.unlocked and tentacle_owned:
        ">You venture up to the attic and find an angry tentacle plant."
        m "Better get out of here before the plant remembers that I'm the one that cut it."
        ">You quickly return to your office."
        jump desk
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
        jump desk


label map_forest: #Label controlling what happens when you go to the forest
    if daytime:
        m "I shouldn't be leaving the castle during the day. It's too risky..."
        jump desk

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
        jump desk

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



label gryffindor_dormitories:
    show screen blkfade
    with d3
    pause.8

    show screen blktone
    hide screen blkfade
    with d5

    menu:
        "-Search the area-":#Cat Hair
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
            else:
                ">You search around the dorms but find nothing of interest."
                jump return_office


label ravenclaw_dormitories:
    show screen blkfade
    with d3
    pause.8

    show screen blktone
    hide screen blkfade
    with d5

    menu:
        "-Search the area-":#Luna's Hair
            $ ran = renpy.random.random()
            if ran < 0.3:
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

    call gen_walk(action="leave", speed=2.8)
    call blkfade

    stop music fadeout 1.0

    centered "{size=+7}{color=#cbcbcb}Outskirts of hogwarts{/color}{/size}"

    call room(hide_screens=True)

    play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.

    $ ccg_folder = "ball"
    $ ccg(layer1="171", layer2="blank", layer3="blank")
    pause.3
    call hide_blkfade
    pause.8
    call play_music("walking_on_grass")
    $ ccg(layer2="172")

    return


label return_office:
    call hide_characters
    show screen blkfade
    with d3

    pause.8

    jump main_room
