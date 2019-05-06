label t_wardrobe_quidditch():
    $ char_active = get_character_object(active_girl)
    $ hide_transitions = True
    
    $ image_arrow = "interface/frames/"+interface_color+"/arrow2.png"
    
    python:
        quidditch_items = { "robe": [choq_cloth_robequidditch1, None],
                            "bottom": [choq_cloth_pantslong2, choq_cloth_pantsshort4, choq_cloth_schoolskirt3]}
        current_item = [0, 0]
    
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
    elif _return == "apply":
        # Add reactions here, example:
        
        if cho_class.get_cloth("robe") == None:
            call remove_quidditch_coat
            
        # If taking off coat failed
        if _return == "fail":
            jump t_wardrobe_quidditch_after_init
            
        if cho_class.get_cloth("bottom").id == choq_cloth_schoolskirt3.id:
            call use_quidditch_skirt_1
        elif cho_class.get_cloth("bottom").id == choq_cloth_pantslong2.id:
            call use_quidditch_pants_1
        elif cho_class.get_cloth("bottom").id == choq_cloth_pantsshort4.id:
            call use_quidditch_pants_2
            
        $ cho_outfit_quidditch.save() #<- use this to save quidditch outfit if all checks are passed
        $ hide_transitions = False
        return
    else:
        m "Nevermind, your current outfit is sufficient enough."
        cho "Okay."
        $ hide_transitions = False
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
    textbutton "Apply" action Return("apply") pos (400, 450)