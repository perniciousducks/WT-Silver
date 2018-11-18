

### Universal Menus ###

#List Menu #Customizable
screen list_menu(menu_items, title, toggle1="", toggle2="", toggle3="", toggle4=""):
    $ item_shown=4
    zorder 5

    use close_button


    imagebutton:
        xpos 825
        ypos 240
        idle "interface/general/"+interface_color+"/button_arrow_up.png"
        if not currentpage <= 0:
            hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
            action Return("dec")


    imagebutton:
        xpos 825
        ypos 292
        idle "interface/general/"+interface_color+"/button_arrow_down.png"
        if currentpage < math.ceil((len(menu_items)-1)/item_shown):
            hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
            action Return("inc")

    imagemap:
        xsize 638
        ysize 544
        xalign 0.5
        yalign 0.5

        ground "interface/store/"+interface_color+"/items_panel.png"
        hover "interface/store/"+interface_color+"/items_panel_hover.png"

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

        hbox:
            xpos 5
            ypos 30
            xsize 300
            ysize 41
            text title xalign 0.5 yalign 0.5 size 16 bold 0.2

        for i in range(currentpage*item_shown, (currentpage*item_shown)+item_shown):
            if i < len(menu_items):
                if menu_items[i].unlocked:
                    hotspot (12, 86+90*(i-(currentpage*item_shown)), 540, 90) clicked Return(menu_items[i])
                use list_menu_item(menu_items[i], 77+90*(i-(currentpage*item_shown)))


screen list_menu_item(menu_item, ypos=0):
    frame:
        background #00000000
        xpos 12
        ypos ypos
        xsize 535
        ysize 100

        $ image_zoom = get_zoom(menu_item.get_image(), 82, 81)

        vbox:
            xpos 0
            ypos 1
            xsize 82
            ysize 81
            add menu_item.get_image() xalign 0.5 yalign 0.5 zoom image_zoom

        vbox:
            xpos 94
            ypos 3
            xsize 440
            ysize 22
            text menu_item.get_title() yalign 0.5

        vbox:
            xpos 94
            ypos 30
            xsize 430
            ysize 55
            text menu_item.get_description()

        text menu_item.get_buttom_right() xalign 1.0 yalign 1.0


#Character Select Menu #Customizable
screen character_select_menu(character_list=[], menu_text="menu name", xposition=24, yposition=52):

    imagemap:
        xpos xposition
        ypos yposition
        xsize 198
        ysize 548

        ground "interface/stat_select/"+str(interface_color)+"/ground_character_screen_"+str(wardrobe_color)+".png"
        hover "interface/stat_select/"+str(interface_color)+"/hover_character_screen_"+str(wardrobe_color)+".png"

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



init -2 python:

    def grayTint(image):
        return im.MatrixColor( image, im.matrix.desaturate() * im.matrix.tint(1.1, 1.1, 1.1))

    def yellowTint(image):
        return im.MatrixColor( image,  im.matrix.tint(1.2, 1.1, 0.7))

    class list_menu_item_class(object):
        imagepath = "images/store/potions/potion_3.png"
        title = "This is the title"
        description = ""
        unlocked = False

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def get_image(self):
            return self.imagepath

        def get_title(self):
            return self.title

        def get_description(self):
            return self.description

        def get_buttom_right(self):
            return ""


    toggle1_bool = True
    toggle2_bool = True
    toggle3_bool = True
    toggle4_bool = True

    def get_head_icon(name):
        return "interface/icons/head/head_"+str(name)+"_1.png"

    def get_zoom(image, xsize, ysize):
        myDisplayable = im.Image(image)
        myRender = renpy.render(myDisplayable, 800, 600, 0, 0)
        sizes = myRender.get_size()
        x = sizes[0]
        y = sizes[1]

        if x > y:
            return xsize / x
        else:
            return ysize / y
