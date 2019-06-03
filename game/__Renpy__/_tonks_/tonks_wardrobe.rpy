label tonks_wardrobe_check(section, arg=None):
    if isinstance(arg, outfit_class):
        python:
            temp_count = [0, 0, 0]
            temp_score = 0
            for item in arg.group:
                if int(ton_friendship/2) < item.whoring:
                    temp_count[0] = item.whoring
                if item.type in ("bra", "panties"):
                    temp_count[2] += 1
                    if char_active.get_cloth(item.type) != None:
                        if not char_active.get_cloth(item.type).id == item.id:
                            if int(ton_friendship/2) < 5:
                                temp_count[1] += 1
                            
        # Outfit outrage score check
        if temp_count[0] > int(ton_friendship/2):
            call ton_main("Its too "+random.choice("slutty", "revealing", "much", "breezy")+" even for myself...",face="annoyed")
            $ temp_score += 1
        if temp_count[2] < 2 and int(ton_friendship/2) < 10:
            if temp_score > 0:
                call ton_main("...not to mention missing underwear!",face="annoyed")
            else:
                call ton_main("Its missing underwear!",face="annoyed")
            $ temp_score += 1
        elif temp_count[1] > 0:
            call ton_main("I have told you before, I'm not letting you pick any underwear for me!",face="annoyed")
            $ temp_score += 1
            
        if temp_score > 0:
            call ton_main("I am NOT wearing it!",face="annoyed")
            $ wardrobe_fail_hint(max(temp_count[0], 5, 10))
            return
    else:
        if section == "touching":
            if int(ton_friendship/2) < 12:
                $ slap_mouse_away()
                
                $ random_number = renpy.random.randint(1, 5)
                if random_number == 1:
                    call ton_main("No touching!",face="annoyed")
                elif random_number == 2:
                    call ton_main("Bad [ton_genie_name]!",face="annoyed")
                elif random_number == 3:
                    call ton_main("Hands to yourself.",face="annoyed")
                elif random_number == 4:
                    call ton_main("Cut it out..",face="annoyed")
                elif random_number == 5:
                    call ton_main("Hands off me.",face="annoyed")
                return
            call ton_main("", face="horny")
        elif section == "toggle":
            if arg in ("bra", "panties"):
                if int(ton_friendship/2) < 9:
                    $ random_number = renpy.random.randint(1, 3)
                    if random_number == 1:
                        call ton_main("I'm not gonna flash you anything!",face="angry")
                        call ton_main("{size=-4}Pervert..{/size}",face="annoyed")
                    elif random_number == 2:
                        call ton_main("Take off my "+arg+"?! No way!",face="angry")
                        call ton_main("", face="annoyed")
                    else:
                        call ton_main("I am not taking off my "+arg+"!",face="angry")
                        call ton_main("", face="annoyed")
                    #Hint
                    $ wardrobe_fail_hint(10)
                    return
            $ char_active.toggle_wear(arg)
            return
        elif section == "equip":
            if arg.type in ("bra", "panties"):
                if arg.id in (char_active.get_cloth("bra").id, char_active.get_cloth("panties").id):
                    if int(ton_friendship/2) < 10:
                        call ton_main("No, I'm not taking off my underwear!",face="angry")
                        #Hint
                        $ wardrobe_fail_hint(10)
                        return
                else:
                    if int(ton_friendship/2) < 5:
                        call ton_main("I am not letting you pick underwear for me.",face="angry")
                        call ton_main("{size=-8}Yet...{/size}",face="horny")
                        #Hint
                        $ wardrobe_fail_hint(5)
                        return
                    else:
                        if int(ton_friendship/2) < arg.whoring:
                            call tonks_wardrobe_too_much
                            return
            else:
                label tonks_wardrobe_too_much:
                if int(ton_friendship/2) < arg.whoring:
                    $ random_number = renpy.random.randint(1, 5)
                    if random_number == 1:
                        call ton_main("I'm not wearing that.",face="annoyed")
                    elif random_number == 2:
                        call ton_main("It's too slutty..",face="annoyed")
                    elif random_number == 3:
                        call ton_main("I would look like a tramp, I refuse.",face="annoyed")
                    elif random_number == 4:
                        call ton_main("I'm not Hermione,[ton_genie_name], ask her to humiliate herself for you amusement..",face="angry")
                    elif random_number == 5:
                        call ton_main("This is too much.",face="annoyed")
                    #Hint
                    $ wardrobe_fail_hint(arg.whoring)
                    return
    $ renpy.play('sounds/equip.ogg')
    $ current_item = arg
    $ char_active.equip(current_item)
    return