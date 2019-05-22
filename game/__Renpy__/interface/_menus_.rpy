

### Universal Menus ###

#Close Button
screen close_button(offsetx = 0, offsety = 0, close_var=lambda : "Close"):
    imagebutton:
            xpos 1028-offsetx
            ypos 11-offsety
            idle "interface/general/"+interface_color+"/button_close.png"
            hover "interface/general/"+interface_color+"/button_close_hover.png"
            action Return(close_var())
            keysym "game_menu"


#List Menu #Customizable
screen list_menu(menu_items, title, toggle1="", toggle2="", toggle3="", toggle4=""):
    $ items_shown=4
    zorder 5

    #Close Button
    use top_bar_close_button

    #Up Button
    imagebutton:
        xpos 825
        ypos 240
        idle "interface/general/"+interface_color+"/button_arrow_up.png"
        if not current_page <= 0:
            hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
            action Return("dec")

    #Down Button
    imagebutton:
        xpos 825
        ypos 292
        idle "interface/general/"+interface_color+"/button_arrow_down.png"
        if current_page < math.ceil((len(menu_items)-1)/items_shown):
            hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
            action Return("inc")

    #Main Window
    imagemap:
        xsize 638
        ysize 544
        xalign 0.5
        yalign 0.5

        ground "interface/panels/"+interface_color+"/items_panel.png"
        hover "interface/panels/"+interface_color+"/items_panel_hover.png"

        #Header
        hbox:
            xpos 11
            ypos 30
            xsize 265
            ysize 45
            text title xalign 0.5 yalign 0.5 size 16 bold 0.2

        #Toggles
        if toggle1 != "": #Top left
            $ toggle1_image = "interface/general/"+interface_color+"/check_true.png" if toggle1_bool else "interface/general/"+interface_color+"/check_false.png"
            hotspot (319, 31, 115, 22) clicked Return("toggle1")
            add toggle1_image xpos 322 ypos 30 zoom 0.8
            text "{size=10}" + toggle1 + "{/size}" xpos 342 ypos 35

        if toggle2 != "": #Borrom left
            $ toggle1_image = "interface/general/"+interface_color+"/check_true.png" if toggle2_bool else "interface/general/"+interface_color+"/check_false.png"
            hotspot (319, 31+20, 115, 22) clicked Return("toggle2")
            add toggle1_image xpos 322 ypos 30+22 zoom 0.8
            text "{size=10}" + toggle2 + "{/size}" xpos 342 ypos 35+20

        if toggle3 != "": #Top right
            $ toggle1_image = "interface/general/"+interface_color+"/check_true.png" if toggle3_bool else "interface/general/"+interface_color+"/check_false.png"
            hotspot (319+114, 31, 115, 22) clicked Return("toggle3")
            add toggle1_image xpos 322+115 ypos 30 zoom 0.8
            text "{size=10}" + toggle3 + "{/size}" xpos 342+115 ypos 35

        if toggle4 != "": #Borrom right
            $ toggle1_image = "interface/general/"+interface_color+"/check_true.png" if toggle4_bool else "interface/general/"+interface_color+"/check_false.png"
            hotspot (319+114, 31+20, 115, 22) clicked Return("toggle4")
            add toggle1_image xpos 322+115 ypos 30+22 zoom 0.8
            text "{size=10}" + toggle4 + "{/size}" xpos 342+115 ypos 35+20

        #Items
        for i in range(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < len(menu_items):
                if menu_items[i].unlockable == False: #Unlockables are shown but aren't buyable/clickable
                    hotspot (12, 86+90*(i-(current_page*items_shown)), 540, 90) clicked Return(menu_items[i])
                use list_menu_item(menu_items[i], 77+90*(i-(current_page*items_shown)))


screen list_menu_item(menu_item, ypos=0):
    frame:
        background #00000000
        xpos 12
        ypos ypos
        xsize 530
        ysize 100

        $ image_zoom = get_zoom(menu_item.get_image(), 82, 81)

        vbox:
            xpos 0
            ypos 1
            xsize 82
            ysize 81
            add menu_item.get_image() xalign 0.5 yalign 0.5 zoom image_zoom

        vbox:
            xpos 100
            ypos 5
            xsize 440
            ysize 22
            text menu_item.get_name() size 16 yalign 0.5

        if store_menu: #Displays item's gold value.
            vbox:
                xpos 270
                ypos 5
                xsize 250
                ysize 22
                text menu_item.get_cost() size 16 xalign 1.0 yalign 0.5

        vbox:
            xpos 100
            ypos 35
            xsize 430
            ysize 55
            text menu_item.get_description() size 12

        text menu_item.get_buttom_right() xalign 1.0 yalign 1.0



#Icon Menu #Customizable
screen icon_menu(menu_items, categories, character, title, xpos, ypos):
    $ items_shown = 20
    $ ui_xpos = xpos
    $ ui_ypos = ypos
    zorder 5

    #Close Button
    use top_bar_close_button

    #Up Button
    imagebutton:
        xpos ui_xpos +480
        ypos ui_ypos +175
        idle "interface/general/"+interface_color+"/button_arrow_up.png"
        if not current_page <= 0:
            hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
            action Return("dec")

    #Down Button
    imagebutton:
        xpos ui_xpos +480
        ypos ui_ypos +175 +52
        idle "interface/general/"+interface_color+"/button_arrow_down.png"
        if current_page < math.ceil((len(menu_items)-1)/items_shown):
            hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
            action Return("inc")

    #Main Window
    imagemap:
        xpos ui_xpos
        ypos ui_ypos
        xsize 467 #width of ground/hover image.
        ysize 548 #height of ground/hover image.

        ground "interface/panels/"+interface_color+"/icon_panel.png"
        hover "interface/panels/"+interface_color+"/icon_panel_hover.png"

        #Header
        hbox:
            xpos 11
            ypos 30
            xsize 265
            ysize 45
            text title xalign 0.5 yalign 0.5 size 16 bold 0.2

        #Categories
        for i in range(0,len(categories)): #Max 5 items!
            hotspot (12+(90*i), 87, 83, 85) clicked SetVariable("category_choice",categories[i]), Return(categories[i])
            add "interface/icons/" +str(categories[i])+ ".png" xpos 0+(90*i) ypos 70 zoom 0.35

        #Items
        for i in range(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < len(menu_items):
                $ row = i // 5
                $ col = i % 5
                if menu_items[i].number > 0 or menu_items[i].unlocked == True:
                    hotspot ( (12+(90*col)), (87+92+(92*row)-(current_page*items_shown)), 83, 85) clicked Return(menu_items[i])
                text str(menu_items[i].number) xpos 75+(90*col) ypos 150+92+(92*row)
                use icon_menu_item(menu_items[i], 5+90*(col-(current_page*items_shown)), 175+90*(row-(current_page*items_shown)))


screen icon_menu_item(menu_item, xpos=0, ypos=0):
    frame:
        background #00000000
        xpos xpos
        ypos ypos
        xsize 90
        ysize 92

        $ image_zoom = get_zoom(menu_item.get_image(), 82, 81)

        vbox:
            xpos 0
            ypos 1
            xsize 82
            ysize 81
            if menu_item.number > 0 or menu_item.unlocked == True:
                add menu_item.get_image() xalign 0.5 yalign 0.5 zoom image_zoom
            else:
                add grayTint(menu_item.get_image() ) xalign 0.5 yalign 0.5 zoom image_zoom

            if menu_item.number > 0:
                text "{color=#ffffff}" +str(menu_item.number)+ "{/color}" xalign 0.5 xpos 15 ypos -80

            if menu_item.active:
                #text "{color=#ffffff}Active{/color}" xalign 0.5 ypos -20
                add "interface/topbar/icon_check.png" xalign 0.95 ypos -40




# Bottom Menu #Customizable
screen bottom_menu(menu_items, categories, title, xpos, ypos, func_btn=False, func_btn_ico="ui_empty"):
    $ items_shown= 9
    $ UI_xpos_offset = xpos
    $ UI_ypos_offset = ypos
    zorder 5

    #Close Button
    use top_bar_close_button

    #Main Window
    imagemap:
        xpos UI_xpos_offset
        ypos UI_ypos_offset
        xsize 1080 #width of ground/hover image.
        ysize 548 #height of ground/hover image.

        ground "interface/panels/" +interface_color+ "/bottom_panel.png"
        hover "interface/panels/"  +interface_color+ "/bottom_panel_hover.png"


        #Menu Name
        add "interface/general/" +interface_color+ "/button_wide.png" xpos 130 ypos 0
        text title xalign 0.5 yalign 0.5 xpos 130+70 ypos 0+18 size 12

        #Categories
        for i in range(0,len(categories)):
            #hotspot (300+(33*i), 0, 33, 34) clicked SetVariable("category_choice",categories[i]), Return(categories[i])
            #add "interface/topbar/buttons/" +interface_color+ "/" +str(categories[i])+ ".png" xpos 300+(33*i) ypos 0

            # Use imagebutton instead of hotspot to make use of imagehover() tint function
            imagebutton:
                xpos 300+(33*i)
                ypos 0
                idle "interface/topbar/buttons/" +interface_color+ "/" +str(categories[i])+ ".png"
                hover image_hover("interface/topbar/buttons/" +interface_color+ "/" +str(categories[i])+ ".png")
                action [SetVariable("category_choice",categories[i]), Return(categories[i])]

        if func_btn:
            imagebutton:
                xpos 300+(33*(len(categories)+1))
                ypos 0
                idle "interface/topbar/buttons/"+interface_color+"/"+func_btn_ico+".png"
                hover image_hover("interface/topbar/buttons/"+interface_color+"/"+func_btn_ico+".png")
                action Return("func")

        #Items
        for i in range(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < len(menu_items):
                $ col = i % 5
                $ row = i % 1
                hotspot ( 140+(90*(i-(current_page*items_shown))), 34, 83, 85) clicked Return(menu_items[i])
                use icon_menu_item(menu_items[i], 135+(90*(i-(current_page*items_shown))), 34 )

    #Left Button
    imagebutton:
        xpos UI_xpos_offset +80
        ypos UI_ypos_offset +50
        idle "interface/general/"+interface_color+"/button_arrow_left.png"
        if not current_page <= 0:
            hover "interface/general/"+interface_color+"/button_arrow_left_hover.png"
            action Return("dec")

    #Right Button
    imagebutton:
        xpos UI_xpos_offset +80 +880
        ypos UI_ypos_offset +50
        idle "interface/general/"+interface_color+"/button_arrow_right.png"
        if current_page < math.ceil((len(menu_items)-1)/items_shown):
            hover "interface/general/"+interface_color+"/button_arrow_right_hover.png"
            action Return("inc")



# Clothing Menu #Customizable
screen clothing_menu(menu_items, character, preview):
    $ items_shown=3
    zorder 5

    #Close Button.
    use top_bar_close_button

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
                idle  grayTint("interface/general/gold_bag.png")
                hover grayTint("interface/general/gold_bag.png")
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

            for i in range(0,len(preview.get_items() )):
                $ row = i % 3
                $ col = i % 2
                text "+"+preview.get_items()[i] xpos 511+(80*col) ypos (490+(12*row)) size 12

            text preview.get_wait_time() xpos 83 ypos 557 size 16
            text "Gold: "+preview.get_cost() xpos 509 ypos 557 size 16

        #Mannequin Display Panels.
        for i in range(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < len(menu_items):
                hotspot( 70+(227*(i-(current_page*items_shown))) , (107) , 175 , 284 ) clicked Return(menu_items[i])

                add menu_items[i].get_image() xpos (-7+(227*(i-(current_page*items_shown)) )) ypos 30 zoom 0.6/scaleratio

        #Large Mannequin Preview.
        if preview != None:
            add preview.get_image() xpos 600 ypos 0 zoom 1.0/scaleratio
        else:
            add "interface/icons/outfits/mannequin_"+str(character)+".png" xpos 600 ypos 0 zoom 1.0/scaleratio



#Character Select Menu #Customizable
screen character_select_menu(character_list=[], menu_text="menu name", xposition=24, yposition=52):

    imagemap:
        xpos xposition
        ypos yposition
        xsize 198
        ysize 548

        ground "interface/stat_select/"+str(interface_color)+"/ground_character_screen_"+str(wardrobe_color)+".png"
        hover "interface/stat_select/"+str(interface_color)+"/hover_character_screen_"+str(wardrobe_color)+".png"
        
        button style "empty" action NullAction()

        vbox:
            xpos 11
            ypos 31
            xsize 173
            ysize 41
            text menu_text xalign 0.5 yalign 0.5  size 14

        for i in range(0,len(character_list)):
            $ row = i // 2
            $ col = i % 2

            $ button_image = im.FactorScale(get_head_icon(character_list[i][0]), 0.4) if character_list[i][1] == 1 else grayTint(im.FactorScale(get_head_icon(character_list[i][0]), 0.4))



            hotspot(13+(90*col), 87+(92*row), 83, 85) clicked Return(character_list[i][0])

            add button_image xpos (90*col) ypos 92+(92*row)





### Menu Init ###

init -2 python:

    def whiteTint(image):
        return im.MatrixColor( image, im.matrix.tint(1.1, 1.1, 1.1))

    def grayTint(image):
        return im.MatrixColor( image, im.matrix.desaturate() * im.matrix.tint(1.1, 1.1, 1.1))

    def yellowTint(image):
        return im.MatrixColor( image,  im.matrix.tint(1.2, 1.1, 0.7))

    toggle1_bool = True
    toggle2_bool = True
    toggle3_bool = True
    toggle4_bool = True

    def get_head_icon(name):
        return "interface/icons/head/head_"+str(name)+"_1.png"

    def get_zoom(image, xsize, ysize):
        if isinstance(image, basestring):
            image = im.Image(image)

        myRender = renpy.render(image, 800, 800, 0, 0)
        sizes = myRender.get_size()
        x = sizes[0]
        y = sizes[1]

        if xsize / x < ysize / y:
            return min(1.0, xsize / x)
        return min(1.0, ysize / y)
