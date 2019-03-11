init python:
    def character_dropped(drags, drops):
        drags[0].snap(540, 300)
        return

label studio:
    hide screen cho_chang
    show screen studio
    
    $ studio_image_zoom = 0.7
    $ studio_image_flip = 1
    $ studio_image_alpha = 1.0
    $ studio_image_rotation = 0.0
    
    $ studio_image_xx = 1010
    $ studio_image_yy = 1200
    
    $ studio_hide = False
    
    #label studio_after_init:
    
    $ image_arrow = "interface/frames/"+interface_color+"/arrow.png"
    
    $ _return = ui.interact()
    
    hide screen studio
    
    if _return == "Close":
        call expression 't_wardrobe' pass (return_label="cho_requests", char_label="cho_main")
        
    jump studio

screen studio:
    tag studio
    zorder 4
    
    key hkey_hide action ToggleVariable("studio_hide", True, False)
    key hkey_mhide action ToggleVariable("studio_hide", True, False)
    
    use character_studio
    
screen character_studio:
    tag character_studio
    zorder 5
    
    if not studio_hide:
        use top_bar_close_button
        
        frame:
            style "empty"
            vbox:
                hbox:
                    spacing 32
                    imagebutton idle image_arrow
                    imagebutton idle im.Flip(image_arrow, horizontal=True)
                hbox:
                    spacing 32
                    imagebutton idle image_arrow
                    imagebutton idle im.Flip(image_arrow, horizontal=True)
                hbox:
                    spacing 32
                    imagebutton idle image_arrow
                    imagebutton idle im.Flip(image_arrow, horizontal=True)
                hbox:
                    spacing 32
                    imagebutton idle image_arrow
                    imagebutton idle im.Flip(image_arrow, horizontal=True)
                hbox:
                    spacing 32
                    imagebutton idle image_arrow
                    imagebutton idle im.Flip(image_arrow, horizontal=True)
                    
                frame:
                    style "empty"
                    xpos 116
                    xanchor 0.5
                    xsize 100
                    bar value VariableValue("studio_image_zoom", 1.0, max_is_zero=False, style=u'bar', offset=0, step=0.01)
                
                frame:
                    style "empty"
                    xpos 116
                    xanchor 0.5
                    xsize 100
                    bar value VariableValue("studio_image_alpha", 1.0, max_is_zero=False, style=u'bar', offset=0, step=0.01)
                    
                frame:
                    style "empty"
                    xpos 116
                    xanchor 0.5
                    xsize 100
                    bar value VariableValue("studio_image_rotation", 359.0, max_is_zero=False, style=u'bar', offset=0, step=1.0)
                    
                textbutton "{size=11}{color=#FFF}Flip{/color}{/size}" action ToggleVariable("studio_image_flip", -1, 1) xsize 94 xpos 116 xanchor 0.5
                    
            vbox:
                ypos 18
                spacing 88
                text "{color=#FFF}{size=-5}eyes{/size}{/color}" xpos 116 xanchor 0.5
                text "{color=#FFF}{size=-5}tears{/size}{/color}" xpos 116 xanchor 0.5
                text "{color=#FFF}{size=-5}mouth{/size}{/color}" xpos 116 xanchor 0.5
                text "{color=#FFF}{size=-5}blush{/size}{/color}" xpos 116 xanchor 0.5
                text "{color=#FFF}{size=-5}background{/size}{/color}" xpos 116 xanchor 0.5
                
            vbox:
                ypos 513
                spacing 14
                text "{color=#FFF}{size=-5}Zoom{/size}{/color}" xpos 116 xanchor 0.5
                text "{color=#FFF}{size=-5}Opacity{/size}{/color}" xpos 116 xanchor 0.5
                text "{color=#FFF}{size=-5}Rotation{/size}{/color}" xpos 116 xanchor 0.5
    
    drag:
        drag_name "character_studio"
        #dragged character_dropped
        draggable True
        drag_offscreen True
        xpos 160 ypos -76
        add char_active.get_image() zoom get_zoom(cho_class.get_image(), int((studio_image_xx-300)*studio_image_zoom), int((studio_image_yy-100)*studio_image_zoom)) xzoom studio_image_flip alpha studio_image_alpha rotate studio_image_rotation