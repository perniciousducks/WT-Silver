label cho_wardrobe_check(section, arg=None):
    if isinstance(arg, DollOutfit):
        python:
            temp_count = [0, 0, 0]
            temp_score = 0
            for item in arg.group:
                if cho_whoring < item.level and temp_count[0] < item.level:
                    temp_count[0] = item.level
                if item.type in ("bra", "panties"):
                    temp_count[2] += 1
                    if char_active.get_equipped(item.type) != None:
                        if not char_active.get_equipped(item.type).id == item.id:
                            if cho_whoring < 5:
                                temp_count[1] += 1

        # Outfit outrage score check
        if cho_whoring < temp_count[0]:
            call cho_main("Its too "+random.choice(("slutty", "revealing", "much", "breezy", "Granger like"))+"...",face="annoyed")
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
                if wardrobe_chitchats:
                    call cho_main("You want me to have piercing and tattoos?",face="angry")
                    call cho_main("My body is already perfect without things like that...",face="annoyed")
                #Hint
                $ wardrobe_fail_hint(12)
                return False
            return True
        elif section == "category":
            return arg #IMPORTANT
        elif section == "touching":
            $ random_number = renpy.random.randint(1, 5)
            if arg == "boobs":
                if cho_whoring < 10:
                    $ slap_mouse_away()
                    if wardrobe_chitchats:
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
                    if wardrobe_chitchats:
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
                    if wardrobe_chitchats:
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
                    if wardrobe_chitchats:
                        if arg == "top":
                            call cho_main("Take my top off? Are you crazy?",face="annoyed")
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
                    if char_active.is_worn("bra"):
                        if arg.id == char_active.get_equipped("bra").id:
                            if wardrobe_chitchats:
                                call cho_main("No, I'm not taking off my bra!",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(10)
                            return
                    if char_active.is_worn("panties"):
                        if arg.id == char_active.get_equipped("panties").id:
                            if wardrobe_chitchats:
                                call cho_main("No, I'm not taking off my panties!",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(10)
                            return
                else:
                    if cho_whoring < arg.level:
                        call .too_much
                        return
            else:
                if cho_whoring < 3:
                    if arg.type in ("top", "bottom"):
                        if char_active.is_worn("top"):
                            if arg.id == char_active.get_equipped("top").id:
                                if wardrobe_chitchats:
                                    call cho_main("I am not taking off my top, forget it!",face="annoyed")
                                #Hint
                                $ wardrobe_fail_hint(3)
                                return
                        if char_active.is_worn("bottom"):
                            if arg.id == char_active.get_equipped("bottom").id:
                                if wardrobe_chitchats:
                                    call cho_main("I won't be walking bottomless on the school grounds..",face="annoyed")
                                #Hint
                                $ wardrobe_fail_hint(3)
                                return
                label .too_much:
                if cho_whoring < arg.level:
                    if wardrobe_chitchats:
                        $ random_number = renpy.random.randint(1, 5)
                        if random_number == 1:
                            call cho_main("I'm not wearing that.",face="annoyed")
                        elif random_number == 2:
                            call cho_main("It's too slutty..",face="annoyed")
                        elif random_number == 3:
                            call cho_main("I would look like a tramp, I refuse.",face="annoyed")
                        elif random_number == 4:
                            call cho_main("I'm not Granger,[cho_genie_name], ask her to humiliate herself for your amusement..",face="angry")
                        elif random_number == 5:
                            call cho_main("This is too much.",face="annoyed")
                    #Hint
                    $ wardrobe_fail_hint(arg.level)
                    return

    $ renpy.play('sounds/equip.ogg')
    $ current_item = arg
    if isinstance(current_item, DollCloth) and current_item.type != "hair" and char_active.is_equipped(current_item.type) and char_active.clothes[current_item.type][0].id == current_item.id:
        $ char_active.unequip(current_item.type)
    else:
        $ char_active.equip(current_item)
    return