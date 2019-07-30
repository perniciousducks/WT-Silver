init python:
    def stats_sortfilter(item, sortby=False):
        return item

####################################
############# Menu #################
####################################

default door_show_busy = True

label door_menu(xx=723, yy=90):

    $ hide_transitions = True
    $ renpy.suspend_rollback(True)
    # Styling
    if daytime:
        $ btn_hover = "#edc48240"
    else:
        $ btn_hover = "#7d75aa40"
        
    call update_stats
    
    $ map_transcript_loc = {"library": "Library", "room_g": "Gryffindor Dormitory", "room_s": "Slytherin Dormitory", "room_r": "Ravenclaw Dormitory", "room_h": "Hufflepuff Dormitory", "great_hall": "Great Hall", "courtyard": "Courtyard", "forest": "Forest", "greenhouse": "Greenhouse", "defense": "D.A.D.A Classroom", "training_grounds": "Training Grounds", "Lake": "Lake", "randomstudent": renpy.random.choice(["Classroom", "Bathroom", "Hagrid's Hut", "Weasley's Store", "Mafkin's Store", "Broom Cupboard", "Attic"]), "randomsnape": renpy.random.choice(["Classroom", "Boathouse", "Bathroom", "Snape's Office", "Hall", "Slytherin Dormitory", "Library", "Attic", "Forest", "Lake", "Dungeons", "Quidditch Cave", "Staircase", "Behind your door", "Room of Doom"]), "randomtonks": renpy.random.choice(["Classroom", "Bathroom", "Hall", "Gryffindor Dormitory", "Slytherin Dormitory", "Hufflepuff Dormitory", "Ravenclaw Dormitory", "Training Grounds", "Tonks' Room", "Quidditch Pitch", "Infirmary", "Sex Dungeon", "Hospital Wing", "Forest", "Lake", "Greenhouse", "Mafkin's Store"])}
        
    # Door dictionary
    $ door_dict = {
                    "Snape": {"ico": "head_snape_1", "flag": snape_unlocked, "busy": snape_busy, "loc": "randomsnape"},
                    "Tonks": {"ico": "head_tonks_1", "flag": tonks_unlocked, "busy": tonks_busy, "loc": "randomtonks"},
                    "Hermione": {"ico": "head_hermione_2", "flag": hermione_unlocked, "busy": hermione_busy, "loc": her_map_location},
                    "Cho": {"ico": "head_cho_2", "flag": cho_unlocked, "busy": cho_busy, "loc": cho_map_location},
                    "Luna": {"ico": "head_luna_2", "flag": luna_unlocked, "busy": luna_busy, "loc": lun_map_location},
                    "Astoria": {"ico": "head_astoria_2", "flag": astoria_unlocked, "busy": astoria_busy, "loc": ast_map_location},
                    "Susan": {"ico": "head_susan_2", "flag": susan_unlocked, "busy": susan_busy, "loc": sus_map_location}
                    }

    $ door_categories_sorted = ["Snape", "Tonks", "Hermione", "Cho", "Luna", "Astoria", "Susan"] #"Ginny", "Daphne", "Padma", "Patil", "Myrtle", "Mafkin"
    $ door_categories_sorted_length = len(door_categories_sorted)

    $ current_sorting = door_show_busy

    label door_menu_after_init:
    $ renpy.block_rollback()

    show screen bld1
    show screen door_menu(xx, yy)

    $ _return = ui.interact()

    hide screen bld1
    hide screen door_menu

    if _return[0] == "summon":
        if not _return[2]:
            hide screen bld1
            hide screen door_menu
            $ renpy.jump("summon_"+_return[1].lower())
        else:
            show screen bld1
            show screen door_menu(xx, yy)
            if daytime or _return[1] in ["Tonks", "Snape"]:
                call nar(">"+_return[1]+" is currently busy. Try again later.")
            else:
                call nar(">"+_return[1]+" is currently asleep. Try again tomorrow.")
    else:
        $ hide_transitions = False
        $ renpy.suspend_rollback(False)
        jump day_main_menu

    jump door_menu_after_init

screen door_menu(xx, yy):
    tag door_menu
    zorder 4

    use top_bar_close_button
    frame:
        style "empty"
        pos (xx, yy)
        xsize 207
        ysize 454

        add "interface/achievements/"+interface_color+"/panel_left.png"
        
        vbox:
            pos (6, 384)
            button action NullAction() style "empty" xsize 195 ysize 32
            frame:
                style "empty"
                textbutton "Show Busy:" style "empty" xsize 195 ysize 32 text_align (0.4, 0.5) text_size 12 hover_background btn_hover action ToggleVariable("door_show_busy", True, False)
                add "interface/general/"+str(interface_color)+"/check_"+str(door_show_busy).lower()+".png" xalign 0.8 yoffset 2
        vbox:
            pos (6, 6)
            $ tmp_x = 0
            for char in door_categories_sorted:
                if not door_dict[char]["flag"]:
                    pass
                else:
                    if not door_show_busy and door_dict[char]["busy"]:
                        pass
                    else:
                        $ tmp_x += 1
                        frame:
                            style "empty"
                            xsize 195
                            ysize 50
                            vbox:
                                vbox:
                                    if not door_dict[char]["busy"]:
                                        textbutton char xsize 195 ysize 48 style "empty" hover_background "interface/achievements/"+interface_color+"/highlight_left_b.png" text_xalign 0.6 text_yalign 0.5 text_xanchor 0.5 text_size 20 action Return(["summon", char, False])
                                    else:
                                        textbutton char xsize 195 ysize 48 style "empty" hover_background "interface/achievements/"+interface_color+"/highlight_left_b.png" text_xalign 0.6 text_yalign 0.5 text_xanchor 0.5 text_size 20 text_color "#8C8C70" action Return(["summon", char, True])

                                add "interface/achievements/"+interface_color+"/spacer_left.png"
                            add "interface/achievements/"+interface_color+"/iconbox.png" yoffset 1
                            if not door_dict[char]["busy"]:
                                $ image_zoom = crop_image_zoom("interface/icons/head/"+door_dict.get(char).get("ico")+".png", 42, 42)
                            else:
                                $ image_zoom = crop_image_zoom("interface/icons/head/"+door_dict.get(char).get("ico")+".png", 42, 42, True)
                            frame:
                                style "empty"
                                xsize 42
                                ysize 42
                                add image_zoom[0] zoom image_zoom[1] align (0.5, 1.0) offset (3, 4)
                            add "interface/achievements/glass_iconbox.png" pos (3, 3)
                            text map_transcript_loc[door_dict[char]["loc"]] size 10 xalign 0.625 yalign 0.9 xanchor 0.5
        if not snape_unlocked:
            text "You don't know anyone" size 12 at truecenter
        else:
            if tmp_x <= 0:
                text "All characters are busy" size 12 at truecenter
            