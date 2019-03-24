

label summon_characters:
    call update_display_characters_summon_list

    $ hide_transitions = True # Hides transitions.
    $ bg_transp = 1.0
    $ bg_color = None
    $ color_background = False

    call screen summon_characters



label summon_a_character:
    if character_choice == "hermione":
        $ summoned_character_list.append("hermione")
        call her_main()
    if character_choice == "luna":
        $ summoned_character_list.append("luna")
        call lun_main()
    if character_choice == "astoria":
        $ summoned_character_list.append("astoria")
        call ast_main()
    if character_choice == "susan":
        $ summoned_character_list.append("susan")
        call sus_main()
    if character_choice == "cho":
        $ summoned_character_list.append("cho")
        call cho_main()

    if character_choice == "genie":
        $ summoned_character_list.append("genie")
        call gen_main()
    if character_choice == "snape":
        $ summoned_character_list.append("snape")
        call sna_main()
    if character_choice == "tonks":
        $ summoned_character_list.append("tonks")
        call ton_main()

    if character_choice == "bg":
        $ summoned_character_list.append("bg")
        show screen custom_background
        with d3

    hide screen bld1

    call screen summon_characters



label close_summon_characters:
    show screen blkfade
    with d3

    call reset_menu_position

    $ hide_transitions = False

    call hide_characters
    hide screen custom_background

    $ display_background = False

    hide screen blktone
    hide screen blkfade
    with fade
    pause.5

    jump day_main_menu

label hide_summon_characters:
    hide screen summon_characters
    with d3

    pause

    call screen summon_characters



label remove_character:
    if character_choice == "hermione":
        $ summoned_character_list.remove("hermione")
        hide screen hermione_main
    if character_choice == "luna":
        $ summoned_character_list.remove("luna")
        hide screen luna_main
    if character_choice == "astoria":
        $ summoned_character_list.remove("astoria")
        hide screen astoria_main
    if character_choice == "susan":
        $ summoned_character_list.remove("susan")
        hide screen susan_main
    if character_choice == "cho":
        $ summoned_character_list.remove("cho")
        hide screen cho_chang
    if character_choice == "genie":
        $ summoned_character_list.remove("genie")
        hide screen genie_main
    if character_choice == "snape":
        $ summoned_character_list.remove("snape")
        hide screen snape_main
    if character_choice == "tonks":
        $ summoned_character_list.remove("tonks")
        hide screen tonks_main
    if character_choice == "bg":
        $ summoned_character_list.remove("bg")
        hide screen custom_background

    call screen summon_characters



label character_face_change:

    $ menu_x = 0.5
    $ menu_y = 0.75

    if character_choice == "hermione":
        call her_main("")
        label summon_hermione_face_change:
        show screen hermione_main
        menu:
            "Change Hermione's face expression?"
            "-Mouth-":
                call set_her_face(change="mouth")
                jump summon_hermione_face_change
            "-Eyes-":
                call set_her_face(change="eyes")
                jump summon_hermione_face_change
            "-Cheeks-":
                call set_her_face(change="cheeks")
                jump summon_hermione_face_change
            "-Tears-":
                call set_her_face(change="tears")
                jump summon_hermione_face_change
            "-Keep it-":
                pass

    if character_choice == "luna":
        call lun_main("")
        label summon_luna_face_change:
        show screen luna_main
        menu:
            "Change Luna's face expression?"
            "-Mouth-":
                call set_lun_face(change="mouth")
                jump summon_luna_face_change
            "-Eyes-":
                call set_lun_face(change="eyes")
                jump summon_luna_face_change
            "-Eyebrows-":
                call set_lun_face(change="brows")
                jump summon_luna_face_change
            "-Pupils-":
                call set_lun_face(change="pupils")
                jump summon_luna_face_change
            "-Keep it-":
                pass

    if character_choice == "astoria":
        call ast_main("")
        label summon_astoria_face_change:
        show screen astoria_main
        menu:
            "Change Astoria's face expression?"
            "-Mouth-":
                call set_ast_face(change="mouth")
                jump summon_astoria_face_change
            "-Eyes-":
                call set_ast_face(change="eyes")
                jump summon_astoria_face_change
            "-Eyebrows-":
                call set_ast_face(change="brows")
                jump summon_astoria_face_change
            "-Pupils-":
                call set_ast_face(change="pupils")
                jump summon_astoria_face_change
            "-Keep it-":
                pass

    if character_choice == "susan":
        call sus_main("")
        label summon_susan_face_change:
        show screen susan_main
        menu:
            "Change Susan's face expression?"
            "-Mouth-":
                call set_sus_face(change="mouth")
                jump summon_susan_face_change
            "-Eyes-":
                call set_sus_face(change="eyes")
                jump summon_susan_face_change
            "-Eyebrows-":
                call set_sus_face(change="brows")
                jump summon_susan_face_change
            "-Pupils-":
                call set_sus_face(change="pupils")
                jump summon_susan_face_change
            "-Keep it-":
                pass

    if character_choice == "cho":
        call cho_main("")
        label summon_cho_face_change:
        show screen cho_chang
        menu:
            "Change Cho's face expression?"
            "-Mouth-":
                call set_cho_face(change="mouth")
                jump summon_cho_face_change
            "-Eyes-":
                call set_cho_face(change="eyes")
                jump summon_cho_face_change
            "-Eyebrows-":
                call set_cho_face(change="brows")
                jump summon_cho_face_change
            "-Pupils-":
                call set_cho_face(change="pupils")
                jump summon_cho_face_change
            "-Keep it-":
                pass

    if character_choice == "genie":
        pass

    if character_choice == "snape":
        pass

    if character_choice == "tonks":
        call ton_main("")
        label summon_tonks_face_change:
        show screen tonks_main
        menu:
            "Change Tonks's face expression?"
            "-Mouth-":
                call set_ton_face(change="mouth")
                jump summon_tonks_face_change
            "-Eyes-":
                call set_ton_face(change="eyes")
                jump summon_tonks_face_change
            "-Eyebrows-":
                call set_ton_face(change="brows")
                jump summon_tonks_face_change
            "-Pupils-":
                call set_ton_face(change="pupils")
                jump summon_tonks_face_change
            "-Keep it-":
                pass

    if character_choice == "bg":
        call pick_custom_background

    hide screen bld1

    call screen summon_characters



label move_character:

    if character_choice == "bg":
        call screen summon_characters

    call reset_menu_position

    hide screen custom_background
    $ bg_transp = 0.3
    show screen custom_background
    with d5

    $ temp_name = renpy.input("(Please enter the X position for the sprite. This should be a number between 0 and 600)")
    $ temp_name = temp_name.strip()
    $ temp_xpos = int(temp_name)

    $ temp_name = renpy.input("(Please enter the Y position for the sprite. This is normally 0)")
    $ temp_name = temp_name.strip()
    $ temp_ypos = int(temp_name)

    menu:
        "Flip character?"
        "-Yes-":
            $ temp_flip = -1
        "-No-":
            $ temp_flip = 1

    if character_choice == "hermione":
        $ hermione_flip = temp_flip
        call her_main(xpos=temp_xpos,ypos=temp_ypos)

    if character_choice == "luna":
        $ luna_flip = temp_flip
        call lun_main(xpos=temp_xpos,ypos=temp_ypos)

    if character_choice == "astoria":
        $ astoria_flip = temp_flip
        call ast_main(xpos=temp_xpos,ypos=temp_ypos)

    if character_choice == "susan":
        $ susan_flip = temp_flip
        call sus_main(xpos=temp_xpos,ypos=temp_ypos)

    if character_choice == "cho":
        $ cho_flip = temp_flip
        call cho_main(xpos=temp_xpos,ypos=temp_ypos)

    if character_choice == "genie":
        $ genie_flip = temp_flip
        call gen_main(xpos=temp_xpos,ypos=temp_ypos)

    if character_choice == "snape":
        $ snape_flip = temp_flip
        call sna_main(xpos=temp_xpos,ypos=temp_ypos)

    if character_choice == "tonks":
        $ tonks_flip = temp_flip
        call ton_main(xpos=temp_xpos,ypos=temp_ypos)

    hide screen bld1
    if bg_transp != 1.0:
        hide screen custom_background
        $ bg_transp = 1.0
        show screen custom_background
        with d5

    call screen summon_characters



label pick_custom_background:

    call reset_menu_position

    menu:
        ">Change background image."
        "-Corridor-":
            call custom_bg("corridor")
        "-Wall-":
            call custom_bg("wall_day")
        "-Forest-":
            call custom_bg("forest")
        "-Castle-":
            call custom_bg("castle")
        "-White-":
            call custom_bg("white")
        "-Change BG Color-":
            $ custom_bg_color = color_picker([255.0, 255.0, 255.0, 255], False, "background color")
            $ color_background = True
        "-Add BG Color-" if bg_color != None:
            $ color_background = True
        "-Remove BG Color-" if color_background:
            $ color_background = False

        "-Custom-":
            $ temp_name = renpy.input("(Please enter the image name of your image located in \"images/rooms/_bg_/*****.png\"\nThe image resolution should be 1080 x 600.\nDo not add a .png at the end!)")
            $ temp_name = temp_name.strip()
            call custom_bg(temp_name)

    return

label custom_bg(bg=""):
    hide screen custom_background

    if bg != "":
        $ custom_bg_image = "images/rooms/_bg_/"+str(bg)+".png"

    show screen custom_background
    with d3

    return

screen custom_background():
    tag custom_background

    if color_background:
        add im.MatrixColor( "images/rooms/_bg_/white.png", im.matrix.tint(custom_bg_color[0]/255.0, custom_bg_color[1]/255.0, custom_bg_color[2]/255.0)) alpha bg_transp
    else:
        add custom_bg_image alpha bg_transp

    zorder 3






screen summon_characters():

    tag summon_characters_menu
    zorder 5

    # Close Button
    imagebutton:
        xpos 1028
        ypos 11
        idle "interface/general/"+interface_color+"/button_close.png"
        hover "interface/general/"+interface_color+"/button_close_hover.png"
        action Jump("close_summon_characters")

    # Hide screen Button
    imagebutton:
        xpos 980
        ypos 11
        idle "interface/general/"+interface_color+"/clothes.png"
        hover "interface/general/"+interface_color+"/clothes_hover.png"
        action Jump("hide_summon_characters")

    # Character Buttons
    for i in range(0,len(character_summon_list)):

        imagebutton:
            xpos 10
            ypos 45+(44*i)
            idle "interface/general/"+interface_color+"/button_select.png"
            hover "interface/general/"+interface_color+"/button_select_hover.png"
            if character_summon_list[i] not in summoned_character_list:
                action [SetVariable("character_choice",character_summon_list[i]), Jump("summon_a_character")]
            else:
                action [SetVariable("character_choice",character_summon_list[i]), Jump("remove_character")]
        text character_summon_list[i] xalign 0.5 yalign 0.5 xpos 10+42 ypos 45+16+(44*i) size 12

        if character_summon_list[i] in summoned_character_list:
            imagebutton:
                xpos 100
                ypos 52+(44*i)
                idle "interface/general/"+interface_color+"/clothes.png"
                hover "interface/general/"+interface_color+"/clothes_hover.png"
                action [SetVariable("character_choice",character_summon_list[i]), Jump("character_face_change")]

            imagebutton:
                xpos 137
                ypos 47+(44*i)
                idle "interface/general/"+interface_color+"/check_true.png"
                hover "interface/general/"+interface_color+"/check_false.png"
                action [SetVariable("character_choice",character_summon_list[i]), Jump("move_character")]
