label t_wardrobe_quidditch():
    $ char_active = get_character_object(active_girl)
    $ hide_transitions = True
    
    $ image_arrow = "interface/frames/"+interface_color+"/arrow2.png"
    
    python:
        quidditch_items = { "robe": [cho_cloth_robequidditch1, None],
                            "top": [cho_cloth_topsweater1, cho_cloth_topsweater2, cho_cloth_topschool1, cho_cloth_topschool2, cho_cloth_topschool3, cho_cloth_topschool4, cho_cloth_topschool5, cho_cloth_topschool6, cho_cloth_topsailor1, None],
                            "bottom": [cho_cloth_pantslong2, cho_cloth_pantsshort4, cho_cloth_schoolskirt1, cho_cloth_schoolskirt2, cho_cloth_schoolskirt3, cho_cloth_schoolskirt4, cho_cloth_skirtshort1, None]}
        current_item = [0, 0, 0]
    
    label t_wardrobe_quidditch_after_init:
    
    show screen t_wardrobe_quidditch_menuitem(550, 50)
    
    $ _return = ui.interact()
    
    hide screen t_wardrobe_quidditch_menuitem
    
    if _return[0] == "equip":
        $ renpy.play('sounds/equip.ogg')
        if _return[1] == "dec":
            $ current_item[_return[2]] = clamp(current_item[_return[2]]-1, 0, len(quidditch_items.items()[_return[2]][1])-1)
        else:
            $ current_item[_return[2]] = clamp(current_item[_return[2]]+1, 0, len(quidditch_items.items()[_return[2]][1])-1)
            
        if not char_active.get_cloth(quidditch_items.keys()[_return[2]]) == quidditch_items.items()[_return[2]][1][current_item[_return[2]]]:
            if not quidditch_items.items()[_return[2]][1][current_item[_return[2]]] == None:
                $ char_active.equip(quidditch_items.items()[_return[2]][1][current_item[_return[2]]])
            else:
                $ char_active.unequip(quidditch_items.keys()[_return[2]])
    else:
        $ hide_transitions = False
        $ char_active.wear("all")
        return
    jump t_wardrobe_quidditch_after_init
        
screen t_wardrobe_quidditch_menuitem(xx, yy):
    tag wardrobe_menuitem
    zorder 4
    
    use top_bar_close_button
    
    # left
    for i in xrange(len(quidditch_items.keys())):
        hbox:
            pos (460, 250+(100*i))
            spacing 210
            imagebutton idle image_arrow hover image_hover(image_arrow) action Return(["equip", "dec", i])
            imagebutton idle im.Flip(image_arrow, horizontal=True) hover image_hover(im.Flip(image_arrow, horizontal=True)) action Return(["equip", "inc", i])