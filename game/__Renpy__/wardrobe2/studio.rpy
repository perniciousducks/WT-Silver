default studio_room_bg = 0
default studio_room_bg_hue = 0
default studio_room_bg_saturation = 2.0
default studio_room_bg_brightness = 1.0
default studio_room_bg_blur = 0.0
default studio_room_bg_flipx = 1
default studio_room_bg_flipy = 1
default studio_room_bg_xoffset = 1080
default studio_room_bg_yoffset = 600

default studio_room_overlay = 0
default studio_room_overlay_alpha = 1.0
default studio_room_overlay_hue = 0
default studio_room_overlay_saturation = 2.0
default studio_room_overlay_brightness = 1.0
default studio_room_overlay_blur = 0.0
default studio_room_overlay_flipx = 1
default studio_room_overlay_flipy = 1
default studio_room_overlay_xoffset = 1080
default studio_room_overlay_yoffset = 600

default studio_room_overlay2 = 0
default studio_room_overlay2_alpha = 1.0
default studio_room_overlay2_hue = 0
default studio_room_overlay2_saturation = 2.0
default studio_room_overlay2_brightness = 1.0
default studio_room_overlay2_blur = 0.0
default studio_room_overlay2_flipx = 1
default studio_room_overlay2_flipy = 1
default studio_room_overlay2_xoffset = 1080
default studio_room_overlay2_yoffset = 600

default studio_text = False
default studio_text_input = "Witch Trainer: Silver"
default studio_text_alpha = 1.0
default studio_text_size = 24
default studio_text_color = "#FFFFFF"
default studio_text_outline = 4
default studio_text_outline_color = "#000000"

default studio_image_eyebrows = 0
default studio_image_eyes = 0
default studio_image_pupils = 0
default studio_image_mouth = 0
default studio_image_zoom = 0.5
default studio_image_flip = 1
default studio_image_alpha = 1.0
default studio_image_rotation = 0.0
default studio_image_body = True

default studio_image_xx = 1010
default studio_image_yy = 1200

init python:
    def character_dropped(drags, drops):
        drags[0].snap(540, 300)
        return

label studio(studio_return, studio_char):
    call hide_characters
    
    python:
        studio_eyebrows_list = os.listdir(config.basedir+"\\game\\characters\\"+active_girl+"\\face\\eyebrows\\")
        studio_eyes_list = os.listdir(config.basedir+"\\game/characters\\"+active_girl+"\\face\\eyes\\")
        studio_eyes_list.remove("_white_.png")
        studio_mouth_list = os.listdir(config.basedir+"\\game\\characters\\"+active_girl+"\\face\\mouth\\")
        studio_pupils_list = os.listdir(config.basedir+"\\game\\characters\\"+active_girl+"\\face\\pupils\\")
    
    $ studio_bg_list = ["wall_day", "castle", "forest", "highlight", "versus", "main_room_day", "main_room_night", "corridor", "custom"]
    $ studio_bg_overlay_list = [None, "curtains", "card", "g_bottom", "g_left", "g_circular"]
    
    $ studio_outfit_saves = {"cho": cho_outfit_last, "tonks": tonks_outfit_last, "astoria": astoria_outfit_last}
    
    if studio_image_eyebrows > len(studio_eyebrows_list):
        $ studio_image_eyebrows = 0
    if studio_image_eyes > len(studio_eyes_list):
        $ studio_image_eyes = 0
    if studio_image_pupils > len(studio_pupils_list):
        $ studio_image_pupils = 0
    if studio_image_mouth > len(studio_mouth_list):
        $ studio_image_mouth = 0
    
    $ char_active.expression(eyebrows=studio_eyebrows_list[studio_image_eyebrows][:-4], eyes=studio_eyes_list[studio_image_eyes][:-4], pupils=studio_pupils_list[studio_image_pupils][:-4], mouth=studio_mouth_list[studio_image_mouth][:-4])
    
    $ studio_hide = False
    
    $ image_arrow = "interface/frames/"+interface_color+"/arrow2.png"
    
    label studio_after_init:
    
    show screen studio
    
    $ _return = ui.interact()
    
    hide screen studio
    if _return == "confirm":
        show screen studio
        $ txt_filename = "exported"
        $ txt_filename = renpy.input("Filename", txt_filename, "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#& ", length=64)
        $ studio_hide = True
        $ renpy.pause(0.1, hard=True)
        $ item_to_export.outfit_export(True, txt_filename)
        $ studio_hide = False
        $ char_active.equip(studio_outfit_saves.get(active_girl))
        hide screen studio
        call expression studio_char pass (xpos="wardrobe", ypos="base", face="neutral")
        call expression 't_wardrobe' pass (return_label=studio_return, char_label=studio_char)
    elif _return == "cancel":
        $ char_active.equip(studio_outfit_saves.get(active_girl))
        call expression studio_char pass (xpos="wardrobe", ypos="base", face="neutral")
        call expression 't_wardrobe' pass (return_label=studio_return, char_label=studio_char)
    elif _return[0] == "body":
        $ studio_outfit_saves.get(active_girl).save()
        $ char_active.equip(studio_outfit_saves.get(active_girl))
        $ studio_image_body = _return[1]
    elif _return[0] == "eyebrows":
        if _return[1] == "inc":
            $ studio_image_eyebrows += 1
        else:
            $ studio_image_eyebrows -= 1
        $ studio_image_eyebrows = clamp(studio_image_eyebrows, 0, len(studio_eyebrows_list)-1)
        $ char_active.expression(eyebrows=studio_eyebrows_list[studio_image_eyebrows][:-4])
    elif _return[0] == "eyes":
        if _return[1] == "inc":
            $ studio_image_eyes += 1
        else:
            $ studio_image_eyes -= 1
        $ studio_image_eyes = clamp(studio_image_eyes, 0, len(studio_eyes_list)-1)
        $ char_active.expression(eyes=studio_eyes_list[studio_image_eyes][:-4])
    elif _return[0] == "pupils":
        if _return[1] == "inc":
            $ studio_image_pupils += 1
        else:
            $ studio_image_pupils -= 1
        $ studio_image_pupils = clamp(studio_image_pupils, 0, len(studio_pupils_list)-1)
        $ char_active.expression(pupils=studio_pupils_list[studio_image_pupils][:-4])
    elif _return[0] == "mouth":
        if _return[1] == "inc":
            $ studio_image_mouth += 1
        else:
            $ studio_image_mouth -= 1
        $ studio_image_mouth = clamp(studio_image_mouth, 0, len(studio_mouth_list)-1)
        $ char_active.expression(mouth=studio_mouth_list[studio_image_mouth][:-4])
    elif _return[0] == "bg":
        if _return[1] == "inc":
            $ studio_room_bg += 1
        else:
            $ studio_room_bg -= 1
        $ studio_room_bg = clamp(studio_room_bg, 0, len(studio_bg_list)-1)
    elif _return[0] == "overlay":
        if _return[1] == "inc":
            if _return[2] == 1:
                $ studio_room_overlay += 1
            else:
                $ studio_room_overlay2 += 1
        else:
            if _return[2] == 1:
                $ studio_room_overlay -= 1
            else:
                $ studio_room_overlay2 -= 1
        $ studio_room_overlay = clamp(studio_room_overlay, 0, len(studio_bg_overlay_list)-1)
        $ studio_room_overlay2 = clamp(studio_room_overlay2, 0, len(studio_bg_overlay_list)-1)
    elif _return[0] == "reset":
        if _return[1] == "character":
            $ studio_image_zoom = 0.5
            $ studio_image_flip = 1
            $ studio_image_alpha = 1.0
            $ studio_image_rotation = 0.0
            $ studio_image_body = True
        elif _return[1] == "background":
            $ studio_room_bg_hue = 0
            $ studio_room_bg_saturation = 2.0
            $ studio_room_bg_brightness = 1.0
            $ studio_room_bg_blur = 0.0
            $ studio_room_bg_flipx = 1
            $ studio_room_bg_flipy = 1
            $ studio_room_bg_xoffset = 1080
            $ studio_room_bg_yoffset = 600
        elif _return[1] == "overlay":
            if _return[2] == 1:
                $ studio_room_overlay_alpha = 1.0
                $ studio_room_overlay_hue = 0
                $ studio_room_overlay_saturation = 2.0
                $ studio_room_overlay_brightness = 1.0
                $ studio_room_overlay_blur = 0.0
                $ studio_room_overlay_flipx = 1
                $ studio_room_overlay_flipy = 1
                $ studio_room_overlay_xoffset = 1080
                $ studio_room_overlay_yoffset = 600
            else:
                $ studio_room_overlay2_alpha = 1.0
                $ studio_room_overlay2_hue = 0
                $ studio_room_overlay2_saturation = 2.0
                $ studio_room_overlay2_brightness = 1.0
                $ studio_room_overlay2_blur = 0.0
                $ studio_room_overlay2_flipx = 1
                $ studio_room_overlay2_flipy = 1
                $ studio_room_overlay2_xoffset = 1080
                $ studio_room_overlay2_yoffset = 600
        elif _return[1] == "text":
            $ studio_text_size = 24
            $ studio_text_color = "#FFFFFF"
            $ studio_text_outline = 4
            $ studio_text_outline_color = "#000000"
    elif _return[0] == "input":
        show screen studio
        if _return[1] == "text":
            $ studio_text_backup = studio_text_input
            $ studio_text_input = renpy.input("Text", studio_text_input, "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#@,.&:;!?-\/* ", length=128)
            if studio_text_input == "Close":
                $ studio_text_input = studio_text_backup
        elif _return[1] == "color":
            $ studio_text_color = color_picker(get_rgb_list(studio_text_color), False, "Text Color", pos_xy=[200, 130])
            $ studio_text_color = get_hex_string(studio_text_color[0]/255.0, studio_text_color[1]/255.0, studio_text_color[2]/255.0, studio_text_color[3]/255.0)
        else:
            $ studio_text_outline_color = color_picker(get_rgb_list(studio_text_outline_color), False, "Outline Color", pos_xy=[200, 130])
            $ studio_text_outline_color = get_hex_string(studio_text_outline_color[0]/255.0, studio_text_outline_color[1]/255.0, studio_text_outline_color[2]/255.0, studio_text_outline_color[3]/255.0)
    else:
        call expression studio_char pass (xpos="wardrobe", ypos="base", face="neutral")
        call expression 't_wardrobe' pass (return_label=studio_return, char_label=studio_char)
        
    jump studio_after_init

screen studio():
    tag studio
    zorder 4
    
    key hkey_hide action ToggleVariable("studio_hide", True, False)
    key hkey_mhide action ToggleVariable("studio_hide", True, False)
    
    frame background "#000"
    
    if studio_room_bg_blur > 0.0:
        add im.Blur(im.MatrixColor("images/rooms/_bg_/"+studio_bg_list[studio_room_bg]+".png", (im.matrix.hue(studio_room_bg_hue)*im.matrix.saturation(clamp(studio_room_bg_saturation-1.0, 0.0, 2.0)))*im.matrix.brightness(studio_room_bg_brightness-1.0)), studio_room_bg_blur) ypos studio_room_bg_yoffset-300 xpos studio_room_bg_xoffset-540 xzoom studio_room_bg_flipx yzoom studio_room_bg_flipy xanchor 0.5 yanchor 0.5
    else:
        add im.MatrixColor("images/rooms/_bg_/"+studio_bg_list[studio_room_bg]+".png", (im.matrix.hue(studio_room_bg_hue)*im.matrix.saturation(clamp(studio_room_bg_saturation-1.0, 0.0, 2.0)))*im.matrix.brightness(studio_room_bg_brightness-1.0)) ypos studio_room_bg_yoffset-300 xpos studio_room_bg_xoffset-540 xzoom studio_room_bg_flipx yzoom studio_room_bg_flipy xanchor 0.5 yanchor 0.5
        
    if not studio_bg_overlay_list[studio_room_overlay] == None:
        if studio_room_overlay_blur > 0.0:
            add im.Blur(im.MatrixColor("images/rooms/overlays/"+studio_bg_overlay_list[studio_room_overlay]+".png", (im.matrix.hue(studio_room_overlay_hue)*im.matrix.saturation(clamp(studio_room_overlay_saturation-1.0, 0.0, 2.0)))*im.matrix.brightness(studio_room_overlay_brightness-1.0)), studio_room_overlay_blur) ypos studio_room_overlay_yoffset-300 xpos studio_room_overlay_xoffset-540 xzoom studio_room_overlay_flipx yzoom studio_room_overlay_flipy alpha studio_room_overlay_alpha xanchor 0.5 yanchor 0.5
        else:
            add im.MatrixColor("images/rooms/overlays/"+studio_bg_overlay_list[studio_room_overlay]+".png", (im.matrix.hue(studio_room_overlay_hue)*im.matrix.saturation(clamp(studio_room_overlay_saturation-1.0, 0.0, 2.0)))*im.matrix.brightness(studio_room_overlay_brightness-1.0)) ypos studio_room_overlay_yoffset-300 xpos studio_room_overlay_xoffset-540 xzoom studio_room_overlay_flipx yzoom studio_room_overlay_flipy alpha studio_room_overlay_alpha xanchor 0.5 yanchor 0.5
    
    drag:
        drag_name "character"
        #dragged character_dropped
        draggable not studio_hide
        drag_offscreen True
        xpos 160 ypos -75
        if studio_image_body:
            add char_active.get_image() zoom get_zoom(char_active.get_image(), int(studio_image_xx*studio_image_zoom), int(studio_image_yy*studio_image_zoom)) xzoom studio_image_flip alpha studio_image_alpha rotate studio_image_rotation
        else:
            add studio_outfit_saves.get(active_girl).get_image() zoom get_zoom(char_active.get_image(), int(studio_image_xx*studio_image_zoom), int(studio_image_yy*studio_image_zoom)) xzoom studio_image_flip alpha studio_image_alpha rotate studio_image_rotation
        
    if not studio_bg_overlay_list[studio_room_overlay2] == None:
        if studio_room_overlay2_blur > 0.0:
            add im.Blur(im.MatrixColor("images/rooms/overlays/"+studio_bg_overlay_list[studio_room_overlay2]+".png", (im.matrix.hue(studio_room_overlay2_hue)*im.matrix.saturation(clamp(studio_room_overlay2_saturation-1.0, 0.0, 2.0)))*im.matrix.brightness(studio_room_overlay2_brightness-1.0)), studio_room_overlay2_blur) ypos studio_room_overlay2_yoffset-300 xpos studio_room_overlay2_xoffset-540 xzoom studio_room_overlay2_flipx yzoom studio_room_overlay2_flipy alpha studio_room_overlay2_alpha xanchor 0.5 yanchor 0.5
        else:
            add im.MatrixColor("images/rooms/overlays/"+studio_bg_overlay_list[studio_room_overlay2]+".png", (im.matrix.hue(studio_room_overlay2_hue)*im.matrix.saturation(clamp(studio_room_overlay2_saturation-1.0, 0.0, 2.0)))*im.matrix.brightness(studio_room_overlay2_brightness-1.0)) ypos studio_room_overlay2_yoffset-300 xpos studio_room_overlay2_xoffset-540 xzoom studio_room_overlay2_flipx yzoom studio_room_overlay2_flipy alpha studio_room_overlay2_alpha xanchor 0.5 yanchor 0.5
    
    if studio_text:
        drag:
            drag_name "studio_text"
            draggable not studio_hide
            drag_offscreen False
            xpos 540 ypos 300
            xanchor 0.5 yanchor 0.5
            frame:
                style "empty"
                if studio_text_outline > 0:
                    text "[studio_text_input]" size studio_text_size color studio_text_color outlines [ (studio_text_outline, studio_text_outline_color, 0, 0)]:
                        at transform:
                            alpha studio_text_alpha
                else:
                    text "[studio_text_input]" size studio_text_size color studio_text_color:
                        at transform:
                            alpha studio_text_alpha
                            
    if export_in_progress:
        add "images/rooms/overlays/card_sp.png"
        hbox:
            xalign 1.0 
            yalign 1.0
            textbutton "confirm" action Return("confirm") xalign 1.0 yalign 1.0
            textbutton "cancel" action Return("cancel") xalign 1.0 yalign 1.0
        frame:
            style "empty"
            pos (688, 512)
            $ ver = config.version[:4]+"."+config.version[4:6] if len(config.version) >=5 else config.version
            text "WT:S [ver]" size 12 color "#FFFFFF" outlines [(1, "#000000", 0, 0)] xanchor 1.0
    
    if not studio_hide:
        use character_studio
    
screen character_studio():
    tag character_studio
    zorder 5
    
    if not export_in_progress:
        use top_bar_close_button
    
    if config.developer:
        vbox:
            xpos 50 yalign 0.9
            text "Eyebrows: {size=-4}{color=#93c763}"+studio_eyebrows_list[studio_image_eyebrows][:-4]+"{/color}{/size}" color "#fff" outlines [(1, "#000000", 0, 0)]
            text "Eyes: {size=-4}{color=#93c763}"+studio_eyes_list[studio_image_eyes][:-4]+"{/color}{/size}" color "#fff" outlines [(1, "#000000", 0, 0)]
            text "Pupils: {size=-4}{color=#93c763}"+studio_pupils_list[studio_image_pupils][:-4]+"{/color}{/size}" color "#fff" outlines [(1, "#000000", 0, 0)]
            text "Mouth: {size=-4}{color=#93c763}"+studio_mouth_list[studio_image_mouth][:-4]+"{/color}{/size}" color "#fff" outlines [(1, "#000000", 0, 0)]
    
    frame:
        ypos 50
        xpos 50
        style "empty"
        hbox:
            spacing 50
            vbox:
                hbox:
                    spacing 32
                    imagebutton idle image_arrow hover image_hover(image_arrow) action Return(["eyebrows", "dec"])
                    imagebutton idle im.Flip(image_arrow, horizontal=True) hover image_hover(im.Flip(image_arrow, horizontal=True)) action Return(["eyebrows", "inc"])
                hbox:
                    spacing 32
                    imagebutton idle image_arrow hover image_hover(image_arrow) action Return(["eyes", "dec"])
                    imagebutton idle im.Flip(image_arrow, horizontal=True) hover image_hover(im.Flip(image_arrow, horizontal=True)) action Return(["eyes", "inc"])
                hbox:
                    spacing 32
                    imagebutton idle image_arrow hover image_hover(image_arrow) action Return(["pupils", "dec"])
                    imagebutton idle im.Flip(image_arrow, horizontal=True) hover image_hover(im.Flip(image_arrow, horizontal=True)) action Return(["pupils", "inc"])
                hbox:
                    spacing 32
                    imagebutton idle image_arrow hover image_hover(image_arrow) action Return(["mouth", "dec"])
                    imagebutton idle im.Flip(image_arrow, horizontal=True) hover image_hover(im.Flip(image_arrow, horizontal=True)) action Return(["mouth", "inc"])
                if config.developer:
                    hbox:
                        spacing 32
                        imagebutton idle image_arrow hover image_hover(image_arrow) action Return(["body", True])
                        imagebutton idle im.Flip(image_arrow, horizontal=True) hover image_hover(im.Flip(image_arrow, horizontal=True)) action Return(["body", False])
                    hbox:
                        spacing 32
                        imagebutton idle image_arrow
                        imagebutton idle im.Flip(image_arrow, horizontal=True)
                    
                frame:
                    style "empty"
                    xpos 50
                    xanchor 0.5
                    xsize 96
                    vbox:
                        bar value VariableValue("studio_image_zoom", 1.0, max_is_zero=False, style=u'bar', offset=0, step=0.01)
                        bar value VariableValue("studio_image_alpha", 1.0, max_is_zero=False, style=u'bar', offset=0, step=0.01)
                        bar value VariableValue("studio_image_rotation", 359.0, max_is_zero=False, style=u'bar', offset=0, step=1.0)
                    
                textbutton "{size=11}{color=#FFF}Flip{/color}{/size}" action ToggleVariable("studio_image_flip", -1, 1) xsize 94 xpos 50 xanchor 0.5
                textbutton "{size=11}{color=#FFF}Reset{/color}{/size}" action Return(["reset", "character"]) xsize 94 xpos 50 xanchor 0.5
            vbox:
                hbox:
                    spacing 32
                    imagebutton idle image_arrow hover image_hover(image_arrow) action Return(["bg", "dec"])
                    imagebutton idle im.Flip(image_arrow, horizontal=True) hover image_hover(im.Flip(image_arrow, horizontal=True)) action Return(["bg", "inc"])
                    
                frame:
                    style "empty"
                    xpos 50
                    xanchor 0.5
                    xsize 96
                    vbox:
                        bar value VariableValue("studio_room_bg_hue", 360, max_is_zero=False, style=u'bar', offset=0, step=1)
                        bar value VariableValue("studio_room_bg_saturation", 4.0, max_is_zero=False, style=u'bar', offset=0, step=0.1)
                        bar value VariableValue("studio_room_bg_brightness", 2.0, max_is_zero=False, style=u'bar', offset=0, step=0.1)
                        bar value VariableValue("studio_room_bg_blur", 5.0, max_is_zero=False, style=u'bar', offset=0, step=0.1)
                        bar value VariableValue("studio_room_bg_xoffset", 2160, max_is_zero=False, style=u'bar', offset=0, step=1)
                        bar value VariableValue("studio_room_bg_yoffset", 1200, max_is_zero=False, style=u'bar', offset=0, step=1)
                    
                textbutton "{size=11}{color=#FFF}Flip X{/color}{/size}" action ToggleVariable("studio_room_bg_flipx", -1, 1) xsize 94 xpos 50 xanchor 0.5
                textbutton "{size=11}{color=#FFF}Flip Y{/color}{/size}" action ToggleVariable("studio_room_bg_flipy", -1, 1) xsize 94 xpos 50 xanchor 0.5
                textbutton "{size=11}{color=#FFF}Reset{/color}{/size}" action Return(["reset", "background"]) xsize 94 xpos 50 xanchor 0.5
            
            vbox:
                hbox:
                    spacing 32
                    imagebutton idle image_arrow hover image_hover(image_arrow) action Return(["overlay", "dec", 1])
                    imagebutton idle im.Flip(image_arrow, horizontal=True) hover image_hover(im.Flip(image_arrow, horizontal=True)) action Return(["overlay", "inc", 1])
                    
                if not studio_bg_overlay_list[studio_room_overlay] == None:    
                    frame:
                        style "empty"
                        xpos 50
                        xanchor 0.5
                        xsize 96
                        vbox:
                            bar value VariableValue("studio_room_overlay_alpha", 1.0, max_is_zero=False, style=u'bar', offset=0, step=0.01)
                            bar value VariableValue("studio_room_overlay_hue", 360, max_is_zero=False, style=u'bar', offset=0, step=1)
                            bar value VariableValue("studio_room_overlay_saturation", 4.0, max_is_zero=False, style=u'bar', offset=0, step=0.1)
                            bar value VariableValue("studio_room_overlay_brightness", 2.0, max_is_zero=False, style=u'bar', offset=0, step=0.1)
                            bar value VariableValue("studio_room_overlay_blur", 5.0, max_is_zero=False, style=u'bar', offset=0, step=0.1)
                            bar value VariableValue("studio_room_overlay_xoffset", 2160, max_is_zero=False, style=u'bar', offset=0, step=1)
                            bar value VariableValue("studio_room_overlay_yoffset", 1200, max_is_zero=False, style=u'bar', offset=0, step=1)
                        
                    textbutton "{size=11}{color=#FFF}Flip X{/color}{/size}" action ToggleVariable("studio_room_overlay_flipx", -1, 1) xsize 94 xpos 50 xanchor 0.5
                    textbutton "{size=11}{color=#FFF}Flip Y{/color}{/size}" action ToggleVariable("studio_room_overlay_flipy", -1, 1) xsize 94 xpos 50 xanchor 0.5
                    textbutton "{size=11}{color=#FFF}Reset{/color}{/size}" action Return(["reset", "overlay", 1]) xsize 94 xpos 50 xanchor 0.5
                    
            vbox:
                hbox:
                    spacing 32
                    imagebutton idle image_arrow hover image_hover(image_arrow) action Return(["overlay", "dec", 2])
                    imagebutton idle im.Flip(image_arrow, horizontal=True) hover image_hover(im.Flip(image_arrow, horizontal=True)) action Return(["overlay", "inc", 2])
                    
                if not studio_bg_overlay_list[studio_room_overlay2] == None:    
                    frame:
                        style "empty"
                        xpos 50
                        xanchor 0.5
                        xsize 96
                        vbox:
                            bar value VariableValue("studio_room_overlay2_alpha", 1.0, max_is_zero=False, style=u'bar', offset=0, step=0.01)
                            bar value VariableValue("studio_room_overlay2_hue", 360, max_is_zero=False, style=u'bar', offset=0, step=1)
                            bar value VariableValue("studio_room_overlay2_saturation", 4.0, max_is_zero=False, style=u'bar', offset=0, step=0.1)
                            bar value VariableValue("studio_room_overlay2_brightness", 2.0, max_is_zero=False, style=u'bar', offset=0, step=0.1)
                            bar value VariableValue("studio_room_overlay2_blur", 5.0, max_is_zero=False, style=u'bar', offset=0, step=0.1)
                            bar value VariableValue("studio_room_overlay2_xoffset", 2160, max_is_zero=False, style=u'bar', offset=0, step=1)
                            bar value VariableValue("studio_room_overlay2_yoffset", 1200, max_is_zero=False, style=u'bar', offset=0, step=1)
                        
                    textbutton "{size=11}{color=#FFF}Flip X{/color}{/size}" action ToggleVariable("studio_room_overlay2_flipx", -1, 1) xsize 94 xpos 50 xanchor 0.5
                    textbutton "{size=11}{color=#FFF}Flip Y{/color}{/size}" action ToggleVariable("studio_room_overlay2_flipy", -1, 1) xsize 94 xpos 50 xanchor 0.5
                    textbutton "{size=11}{color=#FFF}Reset{/color}{/size}" action Return(["reset", "overlay", 2]) xsize 94 xpos 50 xanchor 0.5
            vbox:
                hbox:
                    spacing 32
                    imagebutton idle image_arrow hover image_hover(image_arrow) action ToggleVariable("studio_text", True, False)
                    imagebutton idle im.Flip(image_arrow, horizontal=True) hover image_hover(im.Flip(image_arrow, horizontal=True)) action ToggleVariable("studio_text", True, False)
                    
                if studio_text:
                    textbutton "{size=11}{color=#FFF}Input{/color}{/size}" action Return(["input", "text"]) xsize 94 xpos 50 xanchor 0.5
                    frame:
                        style "empty"
                        xpos 50
                        xanchor 0.5
                        xsize 96
                        vbox:
                            bar value VariableValue("studio_text_alpha", 1.0, max_is_zero=False, style=u'bar', offset=0, step=0.01)
                            bar value VariableValue("studio_text_size", 100, max_is_zero=False, style=u'bar', offset=0, step=1)
                            bar value VariableValue("studio_text_outline", 20, max_is_zero=False, style=u'bar', offset=0, step=1)
                    textbutton "{size=11}{color=#FFF}Color{/color}{/size}" action Return(["input", "color"]) xsize 94 xpos 50 xanchor 0.5
                    if studio_text_outline > 0:
                        textbutton "{size=11}{color=#FFF}Outline color{/color}{/size}" action Return(["input", "outline_color"]) xsize 94 xpos 50 xanchor 0.5
                    textbutton "{size=11}{color=#FFF}Reset{/color}{/size}" action Return(["reset", "text"]) xsize 94 xpos 50 xanchor 0.5
    frame:
        ypos 24
        xpos 100
        style "empty"
        hbox:
            spacing 50
            vbox:
                text "Character" xanchor 0.5 color "#FFF" outlines [ (2, "#000", 0, 0) ] text_align 0.5
                vbox:
                    xpos -2
                    ypos 19
                    spacing 28
                    text "[studio_image_eyebrows]" xanchor 0.5 color "#FFF" outlines [ (2, "#000", 0, 0) ] text_align 0.5
                    text "[studio_image_eyes]" xanchor 0.5 color "#FFF" outlines [ (2, "#000", 0, 0) ] text_align 0.5
                    text "[studio_image_pupils]" xanchor 0.5 color "#FFF" outlines [ (2, "#000", 0, 0) ] text_align 0.5
                    text "[studio_image_mouth]" xanchor 0.5 color "#FFF" outlines [ (2, "#000", 0, 0) ] text_align 0.5
                    if config.developer:
                        text "Body" xanchor 0.5 color "#FFF" outlines [ (2, "#000", 0, 0) ] text_align 0.5
                        text "3" xanchor 0.5 color "#FFF" outlines [ (2, "#000", 0, 0) ] text_align 0.5
            vbox:
                text "Background" xanchor 0.5 color "#FFF" outlines [ (2, "#000", 0, 0) ] text_align 0.5 xpos -10
                text "[studio_room_bg]" xanchor 0.5 color "#FFF" outlines [ (2, "#000", 0, 0) ] text_align 0.5 xpos -10 ypos 19
                vbox:
                    xpos -10
                    ypos 46
                    spacing 13
                    text "Hue" xanchor 0.5 size 11 color "#FFF"
                    text "Saturation" xanchor 0.5 size 11 color "#FFF"
                    text "Brightness" xanchor 0.5 size 11 color "#FFF"
                    text "Blur" xanchor 0.5 size 11 color "#FFF"
                    text "xoffset" xanchor 0.5 size 11 color "#FFF"
                    text "yoffset" xanchor 0.5 size 11 color "#FFF"
            vbox:
                text "Underlay" xanchor 0.5 color "#FFF" outlines [ (2, "#000", 0, 0) ] text_align 0.5 xpos -36
                text "[studio_room_overlay]" xanchor 0.5 color "#FFF" outlines [ (2, "#000", 0, 0) ] text_align 0.5 xpos -36 ypos 19
                if not studio_bg_overlay_list[studio_room_overlay] == None:
                    vbox:
                        xpos -36
                        ypos 46
                        spacing 13
                        text "Alpha" xanchor 0.5 size 11 color "#FFF"
                        text "Hue" xanchor 0.5 size 11 color "#FFF"
                        text "Saturation" xanchor 0.5 size 11 color "#FFF"
                        text "Brightness" xanchor 0.5 size 11 color "#FFF"
                        text "Blur" xanchor 0.5 size 11 color "#FFF"
                        text "xoffset" xanchor 0.5 size 11 color "#FFF"
                        text "yoffset" xanchor 0.5 size 11 color "#FFF"
            vbox:
                text "Overlay" xanchor 0.5 color "#FFF" outlines [ (2, "#000", 0, 0) ] text_align 0.5 xpos -32
                text "[studio_room_overlay2]" xanchor 0.5 color "#FFF" outlines [ (2, "#000", 0, 0) ] text_align 0.5 xpos -30 ypos 19
                if not studio_bg_overlay_list[studio_room_overlay2] == None:
                    vbox:
                        xpos -36
                        ypos 46
                        spacing 13
                        text "Alpha" xanchor 0.5 size 11 color "#FFF"
                        text "Hue" xanchor 0.5 size 11 color "#FFF"
                        text "Saturation" xanchor 0.5 size 11 color "#FFF"
                        text "Brightness" xanchor 0.5 size 11 color "#FFF"
                        text "Blur" xanchor 0.5 size 11 color "#FFF"
                        text "xoffset" xanchor 0.5 size 11 color "#FFF"
                        text "yoffset" xanchor 0.5 size 11 color "#FFF"
            vbox:
                text "Text" xanchor 0.5 color "#FFF" outlines [ (2, "#000", 0, 0) ] text_align 0.5 xpos -16
                text "[studio_text]" xanchor 0.5 color "#FFF" size 12 outlines [ (1, "#000", 0, 0) ] text_align 0.5 xpos -16 ypos 19