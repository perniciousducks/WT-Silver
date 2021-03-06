
# Maps title + toggle names to menu state (current page and toggles)
default menu_states = {}

init python:
    def store_menu_states(menu_id, scope):
        menu_states[menu_id] = scope

#List Menu #Customizable
screen list_menu(menu_id, title, toggle_names=tuple(), menu_groups=[]):
    zorder 5

    use close_button

    # Store screen variables while hidden
    default old_scope = menu_states.get(menu_id, None)
    on ("hide","replaced") action Function(store_menu_states, menu_id, _scope)

    default current_page = 0 if old_scope is None else old_scope["current_page"]
    default toggles = set([i for i in xrange(0,max(len(toggle_names), len(menu_groups)))]) if old_scope is None else old_scope["toggles"]

    # Menu items from enabled groups
    default menu_items = []
    $ menu_items = list(itertools.chain.from_iterable([menu_groups[i] for i in sorted(toggles) if i < len(menu_groups)]))

    default items_shown = 4
    default max_page = 0
    $ max_page = max(0, (len(menu_items)-1)/items_shown)
    $ current_page = min(current_page, max_page)

    # Page up
    imagebutton:
        xpos 825
        ypos 240
        idle "interface/general/"+interface_color+"/button_arrow_up.png"
        hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
        sensitive current_page > 0
        action SetScreenVariable("current_page", max(0, current_page-1))

    # Page down
    imagebutton:
        xpos 825
        ypos 292
        idle "interface/general/"+interface_color+"/button_arrow_down.png"
        hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
        sensitive current_page <= max_page
        action SetScreenVariable("current_page", min(max_page, current_page+1))

    # Main window
    imagemap:
        xsize 638
        ysize 544
        xalign 0.5
        yalign 0.5

        ground "interface/panels/"+interface_color+"/items_panel.png"
        hover "interface/panels/"+interface_color+"/items_panel_hover.png"

        # Header
        hbox:
            pos (11,30)
            xysize (265,45)
            text title align (0.5,0.5) size 16 bold 0.2

        # Toggles
        grid 2 2:
            pos (319,31)
            for i in xrange(0,4):
                if i < len(toggle_names):
                    $ toggle_names[i]
                    if i in toggles:
                        $ toggle_image = "interface/general/"+interface_color+"/check_true.png"
                    else:
                        $ toggle_image = "interface/general/"+interface_color+"/check_false.png"
                    button:
                        style "empty"
                        xysize (110,22)
                        left_margin 5
                        clicked [ToggleSetMembership(toggles, i),SetScreenVariable("current_page", 0),Return(("toggle"+str(i), i in toggles))]
                        add toggle_image zoom 0.8
                        text "{size=10}" + toggle_names[i] + "{/size}" xpos 22 yalign 0.5
                else:
                    null

        # Items
        $ page_offset = current_page*items_shown
        for i in xrange(page_offset, page_offset+items_shown):
            if i < len(menu_items):
                $ item_ypos = 85+90*(i-page_offset)
                if not menu_items[i].unlockable: # Unlockables are shown but aren't clickable
                    hotspot (16, item_ypos, 528, 87) clicked Return(menu_items[i])
                use list_menu_item(menu_items[i], item_ypos)

screen list_menu_item(menu_item, ypos=0):
    frame:
        style "empty"
        xpos 16
        ypos ypos
        xsize 528
        ysize 87

        $ item_image = menu_item.get_image()
        if isinstance(item_image, im.ImageBase):
            $ item_image, image_zoom = crop_image_zoom(item_image, 83, 83)
        else:
            $ image_zoom = get_zoom(item_image, 83, 83)

        fixed:
            pos (6,2)
            xysize (83, 83)
            add item_image align (0.5, 0.5) zoom image_zoom

        fixed:
            pos (100, 0)
            xysize (420, 24)
            text menu_item.get_name() size 16 yalign 1.0

            if store_menu: # Displays item's gold value
                text menu_item.get_cost() size 16 text_align 1.0 align (1.0,1.0)

        fixed:
            pos (100, 32)
            xysize (420, 50)
            text menu_item.get_description() size 12

        text menu_item.get_annotation() align (1.0,1.0) offset (-2,-2)

screen bottom_menu(menu_id, group_names, menu_groups, func_btn=None):
    zorder 30

    use close_button

    # Store screen variables while hidden
    default old_scope = menu_states.get(menu_id, None)
    on ("hide","replaced") action Function(store_menu_states, menu_id, _scope)

    default current_page = 0 if old_scope is None else old_scope["current_page"]
    default current_group = 0 if old_scope is None else old_scope["current_group"]

    # Menu items from enabled groups
    default menu_items = []
    $ menu_items = menu_groups[current_group]

    default items_shown = 9
    default max_page = 0
    $ max_page = max(0, (len(menu_items)-1)/items_shown)
    $ current_page = min(current_page, max_page)

    # Main window
    imagemap:
        xpos 0
        ypos 475
        xsize 1080
        ysize 548

        ground "interface/panels/"+interface_color+"/bottom_panel.png"
        hover "interface/panels/"+interface_color+"/bottom_panel_hover.png"

        # Menu name
        $ title = group_names[current_group][0]
        add "interface/general/"+interface_color+"/button_wide.png" xpos 130 ypos 0
        text title xalign 0.5 yalign 0.5 xpos 130+70 ypos 0+18 size 12

        # Categories
        for i in xrange(0,len(menu_groups)):
            $ group_icon = group_names[i][1]
            imagebutton:
                xpos 300+(33*i)
                ypos 0
                idle "interface/topbar/buttons/"+interface_color+"/"+group_icon+".png"
                hover image_hover("interface/topbar/buttons/" +interface_color+ "/" +group_icon+".png")
                sensitive current_group != i
                action [SetScreenVariable("current_group", i), SetScreenVariable("current_page", 0)]

        if func_btn:
            imagebutton:
                xpos 300+(33*(len(menu_groups)+1))
                ypos 0
                idle "interface/topbar/buttons/"+interface_color+"/"+func_btn+".png"
                hover image_hover("interface/topbar/buttons/"+interface_color+"/"+func_btn+".png")
                action Return("func")

        # Items
        $ page_offset = current_page*items_shown
        for i in xrange(page_offset, page_offset+items_shown):
            if i < len(menu_items):
                $ col = i % 5
                $ row = i % 1
                hotspot ( 140+(90*(i-page_offset)), 34, 90, 90) clicked Return((current_group, menu_items[i]))
                use icon_menu_item(menu_items[i], 140+(90*(i-page_offset)), 34 )

    # Page left
    imagebutton:
        xpos 80
        ypos 475+50
        idle "interface/general/"+interface_color+"/button_arrow_left.png"
        hover "interface/general/"+interface_color+"/button_arrow_left_hover.png"
        sensitive current_page > 0
        action SetScreenVariable("current_page", max(0, current_page-1))

    # Page right
    imagebutton:
        xpos 880+80
        ypos 475+50
        idle "interface/general/"+interface_color+"/button_arrow_right.png"
        hover "interface/general/"+interface_color+"/button_arrow_right_hover.png"
        sensitive current_page <= max_page
        action SetScreenVariable("current_page", min(max_page, current_page+1))

screen icon_menu_item(menu_item, xpos=0, ypos=0):
    frame:
        background None
        xpos xpos
        ypos ypos
        xsize 90
        ysize 90

        $ item_image = menu_item.get_image()
        if isinstance(item_image, im.ImageBase):
            $ item_image, image_zoom = crop_image_zoom(item_image, 80, 80)
        else:
            $ image_zoom = get_zoom(item_image, 80, 80)

        fixed:
            xsize 80
            ysize 80
            if menu_item.number > 0 or menu_item.unlocked == True:
                add item_image xalign 0.5 yalign 0.5 zoom image_zoom
            else:
                add gray_tint(item_image) xalign 0.5 yalign 0.5 zoom image_zoom

            if menu_item.number > 0:
                text "{color=#ffffff}" +str(menu_item.number)+ "{/color}"

            if menu_item.active:
                add "interface/topbar/icon_check.png" align (1.0,1.0)

# Clothing Menu #Customizable
screen clothing_menu(menu_items, character, preview):
    $ items_shown=3
    zorder 5

    #Close Button.
    use close_button

    #Up Button.
    imagebutton:
        xpos 725
        ypos 240
        idle "interface/general/"+interface_color+"/button_arrow_up.png"
        if not current_page <= 0:
            hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
            action Return("dec")

    #Down Button.
    imagebutton:
        xpos 725
        ypos 292
        idle "interface/general/"+interface_color+"/button_arrow_down.png"
        if current_page < math.ceil((len(menu_items)-1)/items_shown):
            hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
            action Return("inc")

    #Left Button (Bottom right of screen).
    imagebutton:
        xpos 977
        ypos 544
        idle "interface/general/"+interface_color+"/button_arrow_left.png"
        if character >= character_choice_list[1]:
            hover "interface/general/"+interface_color+"/button_arrow_left_hover.png"
            action Return("left")

    #Right Button (Bottom right of screen).
    imagebutton:
        xpos 1029
        ypos 544
        idle "interface/general/"+interface_color+"/button_arrow_right.png"
        if character < character_choice_list[-1]:
            hover "interface/general/"+interface_color+"/button_arrow_right_hover.png"
            action Return("right")

    #Bag of Gold Icon
    if preview != None:
        imagebutton:
            xpos 705
            ypos 490
            if gold >= preview.cost:
                idle  "interface/general/gold_bag.png"
                hover "interface/general/gold_bag_hover.png"
            else:
                idle  gray_tint("interface/general/gold_bag.png")
                hover gray_tint("interface/general/gold_bag.png")
            action Return("buy") #Buys whatever is currently previewed (item_choice)


    #Main Store Window.
    imagemap:
        xpos 0
        ypos 0

        if preview == None:
            ground "interface/panels/"+str(interface_color)+"/clothing_panel_main.png"
            hover "interface/panels/"+str(interface_color)+"/clothing_panel_main_hover.png"
        else:
            ground "interface/panels/"+str(interface_color)+"/clothing_panel_full.png"
            hover "interface/panels/"+str(interface_color)+"/clothing_panel_full_hover.png"

            #Item Information Display Panel.
            text preview.get_name() xpos 83 ypos 458 size 16
            text preview.get_description() xpos 85 ypos 490 size 12
            text preview.get_type() xpos 509 ypos 458 size 16
            text ", ".join(preview.get_items()) pos (511, 490) xmaximum 180 size 12
            text preview.get_wait_time() xpos 83 ypos 557 size 16
            text "Price: "+preview.get_cost() xpos 509 ypos 557 size 16

        #Mannequin Display Panels.
        $ page_offset = current_page*items_shown
        for i in xrange(page_offset, page_offset+items_shown):
            if i < len(menu_items):
                hotspot( 70+(227*(i-page_offset)) , (107) , 175 , 284 ) clicked Return(menu_items[i])

                add menu_items[i].get_image() xpos (-7+(227*(i-page_offset))) ypos 30 zoom 0.6/scaleratio

        #Large Mannequin Preview.
        if preview != None:
            add preview.get_image() xpos 600 ypos 0 zoom 1.0/scaleratio
        else:
            if character == 1:
                add hermione.body.get_mannequin() xpos 600 ypos 0 zoom 1.0/scaleratio
            elif character == 3:
                add astoria.body.get_mannequin() xpos 600 ypos 0 zoom 1.0/scaleratio
            elif character == 5:
                add cho.body.get_mannequin() xpos 600 ypos 0 zoom 1.0/scaleratio
            else:
                add "interface/icons/outfits/mannequin_"+str(character)+".png" xpos 600 ypos 0 zoom 1.0/scaleratio
