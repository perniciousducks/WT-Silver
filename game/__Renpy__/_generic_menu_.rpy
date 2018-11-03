screen generic_scroll_menu(menu_items, title, toogle1="", toogle2=""):
    $ item_shown=4
    zorder 5
    
    use close_button
    
    if not currentpage <= 0:
        imagebutton:
            xpos 825
            ypos 240
            idle "interface/general/"+interface_color+"/button_arrow_up.png"
            hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
            action Return("dec")
            
    if currentpage < math.ceil((len(menu_items)-1)/item_shown):
        imagebutton:
            xpos 825
            ypos 292
            idle "interface/general/"+interface_color+"/button_arrow_down.png"
            hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
            action Return("inc")
          
    imagemap:
        xsize 638
        ysize 544
        xalign 0.5
        yalign 0.5
        
        ground "interface/store/"+interface_color+"/items_panel.png"
        hover "interface/store/"+interface_color+"/items_panel_hover.png"
        
        if not toogle1 == "":
            $ toogle1_image = "interface/general/"+interface_color+"/check_true.png" if toogle1_bool else "interface/general/"+interface_color+"/check_false.png"
            hotspot (325, 30, 150, 24) clicked Return("toogle1")
            add toogle1_image xpos 325 ypos 30 zoom 0.8
            text "{size=10}" + toogle1 + "{/size}" xpos 350 ypos 35
        
        if not toogle2 == "":
            $ toogle1_image = "interface/general/"+interface_color+"/check_true.png" if toogle2_bool else "interface/general/"+interface_color+"/check_false.png"
            hotspot (325, 50, 150, 24) clicked Return("toogle2")
            add toogle1_image xpos 325 ypos 50 zoom 0.8
            text "{size=10}" + toogle2 + "{/size}" xpos 350 ypos 55
 
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
                use generic_scroll_item(menu_items[i], 77+90*(i-(currentpage*item_shown)))

            
screen generic_scroll_item(mirror_story, ypos=0):
    frame:
        background #00000000
        xpos 12
        ypos ypos
        xsize 535
        ysize 100
        
        $ image_zoom = get_zoom(mirror_story.get_image(), 82, 81)
        
        vbox:
            xpos 0
            ypos 1
            xsize 82
            ysize 81
            add mirror_story.get_image() xalign 0.5 yalign 0.5 zoom image_zoom
        
        vbox:
            xpos 94
            ypos 3
            xsize 440
            ysize 22
            text mirror_story.get_title() yalign 0.5
            
        vbox:
            xpos 94
            ypos 30
            xsize 430
            ysize 55
            text mirror_story.get_description()

        text mirror_story.get_buttom_right() xalign 1.0 yalign 1.0
        
init python:
    toogle1_bool = True
    toogle2_bool = True

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