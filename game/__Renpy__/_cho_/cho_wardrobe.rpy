label cho_wardrobe_check(section, arg=None):
    if isinstance(arg, outfit_class):
        python:
            temp_count = [0, 0, 0]
            temp_score = 0
            for item in arg.group:
                if cho_whoring < item.whoring and temp_count[0] < item.whoring:
                    temp_count[0] = item.whoring
                if item.type in ("bra", "panties"):
                    temp_count[2] += 1
                    if char_active.get_cloth(item.type) != None:
                        if not char_active.get_cloth(item.type).id == item.id:
                            if cho_whoring < 5:
                                temp_count[1] += 1
                            
        # Outfit outrage score check
        if cho_whoring < temp_count[0]:
            call cho_main("Its too "+random.choice(("slutty", "revealing", "much", "breezy"))+"...",face="annoyed")
            $ temp_score += 1
        if temp_count[2] < 2 and cho_whoring < 10:
            if temp_score > 0:
                call cho_main("...not to mention missing underwear!",face="annoyed")
            else:
                call cho_main("Its missing underwear!",face="annoyed")
            $ temp_score += 1
        elif temp_count[1] > 0:
            call cho_main("I have told you before, I'm not letting you pick any underwear for me!",face="annoyed")
            $ temp_score += 1
            
        if temp_score > 0:
            call cho_main("I am NOT wearing it!",face="annoyed")
            #Hint
            $ wardrobe_fail_hint(max(temp_count[0], 5, 10))
            return
    else:
        if section == "tabswitch":
            if cho_whoring < 12:
                call cho_main("You want to make me wear body piercing and tattoos?",face="angry")
                call cho_main("I won't allow it!",face="annoyed")
                #Hint
                $ wardrobe_fail_hint(12)
                return False
            return True
        elif section == "touching":
            $ random_number = renpy.random.randint(1, 5)
            if arg == "boobs":
                if cho_whoring < 10:
                    $ slap_mouse_away()
                    
                    if random_number == 1:
                        call cho_main("No touching!",face="annoyed")
                    elif random_number == 2:
                        call cho_main("Bad [cho_genie_name]!",face="annoyed")
                    elif random_number == 3:
                        call cho_main("Hands to yourself.",face="annoyed")
                    elif random_number == 4:
                        call cho_main("Cut it out..",face="annoyed")
                    elif random_number == 5:
                        call cho_main("Hands off me.",face="annoyed")
                    return
            if arg == "pussy":
                if cho_whoring < 16:
                    $ slap_mouse_away()
                    
                    if random_number == 1:
                        call cho_main("Stop that!",face="annoyed")
                    elif random_number == 2:
                        call cho_main("[cho_genie_name]!",face="annoyed")
                    elif random_number == 3:
                        call cho_main("Unhand me..",face="annoyed")
                    elif random_number == 4:
                        call cho_main("Stop it please..",face="annoyed")
                    elif random_number == 5:
                        call cho_main("Hands off me.",face="annoyed")
                    return
            $ love_mouse_away()
            call cho_main("", face="horny")
            return
        elif section == "toggle":
            if arg in ("bra", "panties"):
                if cho_whoring < 9:
                    $ random_number = renpy.random.randint(1, 3)
                    if random_number == 1:
                        call cho_main("I'm not gonna flash you anything!",face="angry")
                        call cho_main("{size=-4}Pervert..{/size}",face="annoyed")
                    elif random_number == 2:
                        call cho_main("Take off my "+arg+"?! No way!",face="angry")
                        call cho_main("", face="annoyed")
                    else:
                        call cho_main("I am not taking off my "+arg+"!",face="angry")
                        call cho_main("", face="annoyed")
                    #Hint
                    $ wardrobe_fail_hint(10)
                    return
            elif arg in ("top", "bottom"):
                if cho_whoring < 3:
                    if arg == "top":
                        call cho_main("Take my top off for a quickie? Are you insane?",face="annoyed")
                    elif arg == "bottom":
                        call cho_main("Take my bottoms off so you can ogle my ass? No thank you.",face="annoyed")
                    #Hint
                    $ wardrobe_fail_hint(3)
                    return
            $ char_active.toggle_wear(arg)
            return
        elif section == "equip":
            if arg.type in ("bra", "panties"):
                if cho_whoring < 10:
                    if char_active.get_cloth("bra"):
                        if arg.id == char_active.get_cloth("bra").id:
                            call cho_main("No, I'm not taking off my bra!",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(10)
                            return
                    if char_active.get_cloth("panties"):
                        if arg.id == char_active.get_cloth("panties").id:
                            call cho_main("No, I'm not taking off my panties!",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(10)
                            return
                else:
                    if cho_whoring < arg.whoring:
                        call cho_wardrobe_too_much
                        return
            else:
                if cho_whoring < 3:
                    if arg.type in ("top", "bottom"):
                        if char_active.get_cloth("top"):
                            if arg.id == char_active.get_cloth("top").id:
                                call cho_main("I am not taking off my top, forget it!",face="annoyed")
                                #Hint
                                $ wardrobe_fail_hint(3)
                                return
                        if char_active.get_cloth("bottom"):
                            if arg.id == char_active.get_cloth("bottom").id:
                                call cho_main("I won't be walking bottomless on the school grounds..",face="annoyed")
                                #Hint
                                $ wardrobe_fail_hint(3)
                                return
                label cho_wardrobe_too_much:
                if cho_whoring < arg.whoring:
                    $ random_number = renpy.random.randint(1, 5)
                    if random_number == 1:
                        call cho_main("I'm not wearing that.",face="annoyed")
                    elif random_number == 2:
                        call cho_main("It's too slutty..",face="annoyed")
                    elif random_number == 3:
                        call cho_main("I would look like a tramp, I refuse.",face="annoyed")
                    elif random_number == 4:
                        call cho_main("I'm not Hermione,[cho_genie_name], ask her to humiliate herself for you amusement..",face="angry")
                    elif random_number == 5:
                        call cho_main("This is too much.",face="annoyed")
                    #Hint
                    $ wardrobe_fail_hint(arg.whoring)
                    return
                    
    $ renpy.play('sounds/equip.ogg')
    $ current_item = arg
    $ char_active.equip(current_item)
    return