label hermione_wardrobe_check(section, arg=None):
    if isinstance(arg, DollOutfit):
        python:
            temp_count = [0, 0, 0]
            temp_score = 0
            for item in arg.group:
                if her_whoring < item.level and temp_count[0] < item.level:
                    temp_count[0] = item.level
                if item.type in ("bra", "panties"):
                    temp_count[2] += 1
                    if char_active.get_equipped(item.type) != None:
                        if not char_active.get_equipped(item.type).id == item.id:
                            if her_whoring < 5:
                                temp_count[1] += 1

        # Outfit outrage score check
        if her_whoring < temp_count[0]:
            call her_main("It's too "+random.choice(("slutty", "revealing", "much", "breezy"))+"...",face="annoyed")
            $ temp_score += 1
        if temp_count[2] < 2 and her_whoring < 10:
            if temp_score > 0:
                call her_main("...not to mention missing underwear!",face="annoyed")
            else:
                call her_main("It's missing underwear!",face="annoyed")
            $ temp_score += 1
        elif temp_count[1] > 0:
            call her_main("I have told you before, I'm not letting you pick any underwear for me!",face="angry")
            $ temp_score += 1

        if temp_score > 0:
            call her_main("I am NOT wearing it!",face="annoyed")
            #Hint
            $ wardrobe_fail_hint(max(temp_count[0], 5, 10))
            return
    else:
        if section == "tabswitch":
            if her_whoring < 12:
                if wardrobe_chitchats:
                    call her_main("You want me to have piercing and tattoos?", "open", "narrow", "angry", "L")
                    call her_main("My body is already perfect without things like that...", "annoyed", "happyCl", "angry", "L", cheeks="blush")
                #Hint
                $ wardrobe_fail_hint(12)
                return False
            return True
        elif section == "category":
            return arg #IMPORTANT
        elif section == "touching":
            $ random_number = renpy.random.randint(1, 5)
            if arg == "boobs":
                if her_whoring < 10:
                    $ slap_mouse_away()
                    if wardrobe_chitchats:
                        if random_number == 1:
                            call her_main("No touching!", "open", "narrow", "angry", "L")
                        elif random_number == 2:
                            call her_main("Bad [genie_name]!", "annoyed", "happyCl", "angry", "L", cheeks="blush")
                        elif random_number == 3:
                            call her_main("Hands to yourself.", "clench", "base", "angry", "R")
                        elif random_number == 4:
                            call her_main("Cut it out..", "open", "narrow", "angry", "mid")
                        elif random_number == 5:
                            call her_main("Hands off me.", "mad", "wide", "angry", "mid")
                    return
            if arg == "pussy":
                if her_whoring < 16:
                    $ slap_mouse_away()
                    if wardrobe_chitchats:
                        if random_number == 1:
                            call her_main("Stop that!", "angry", "wide", "angry", "mid")
                        elif random_number == 2:
                            call her_main("[genie_name]!", "open", "narrow", "angry", "L")
                        elif random_number == 3:
                            call her_main("Unhand me..", "mad", "wide", "angry", "mid")
                        elif random_number == 4:
                            call her_main("Stop it please..", "open", "happyCl", "angry", "mid", cheeks="blush")
                        elif random_number == 5:
                            call her_main("Hands off me.", "clench", "narrow", "angry", "mid")
                    return
            $ love_mouse_away()
            call her_main("", face="horny")
            return
        elif section == "toggle":
            if arg in ("bra", "panties"):
                if her_whoring < 9:
                    if wardrobe_chitchats:
                        $ random_number = renpy.random.randint(1, 3)
                        if random_number == 1:
                            call her_main("I'm not gonna flash you anything!", "clench", "narrow", "angry", "mid")
                            call her_main("{size=-4}Pervert..{/size}", "annoyed", "narrow", "angry", "R")
                        elif random_number == 2:
                            call her_main("Take off my [arg]?! No way!", "clench", "narrow", "angry", "mid")
                            call her_main("", "annoyed", "narrow", "angry", "down")
                        else:
                            call her_main("I am not taking off my [arg]!", "clench", "narrow", "angry", "mid")
                            call her_main("", "annoyed", "narrow", "angry", "mid")
                    #Hint
                    $ wardrobe_fail_hint(10)
                    return
            elif arg in ("top", "bottom"):
                if her_whoring < 3:
                    if wardrobe_chitchats:
                        if arg == "top":
                            call her_main("Take my top off? Are you crazy?", "annoyed", "narrow", "angry", "L")
                        elif arg == "bottom":
                            call her_main("Take my bottoms off so you can ogle my ass? No thank you.", "open", "narrow", "angry", "mid")
                    #Hint
                    $ wardrobe_fail_hint(3)
                    return
            $ char_active.toggle_wear(arg)
            return
        elif section == "equip":
            if arg.type in ("bra", "panties"):
                if her_whoring < 10:
                    if char_active.get_equipped("bra"):
                        if arg.id == char_active.get_equipped("bra").id:
                            if wardrobe_chitchats:
                                call her_main("No, I'm not taking off my bra!", "clench", "wide", "angry", "mid")
                            #Hint
                            $ wardrobe_fail_hint(10)
                            return
                    if char_active.get_equipped("panties"):
                        if arg.id == char_active.get_equipped("panties").id:
                            if wardrobe_chitchats:
                                call her_main("No, I'm not taking off my panties!", "mad", "narrow", "angry", "mid")
                            #Hint
                            $ wardrobe_fail_hint(10)
                            return
                else:
                    if her_whoring < arg.level:
                        call .too_much
                        return
            else:
                if her_whoring < 3:
                    if arg.type in ("top", "bottom"):
                        if char_active.get_equipped("top"):
                            if arg.id == char_active.get_equipped("top").id:
                                if wardrobe_chitchats:
                                    call her_main("I am not taking off my top, forget it!", "annoyed", "narrow", "angry", "L", cheeks="blush")
                                #Hint
                                $ wardrobe_fail_hint(3)
                                return
                        if char_active.get_equipped("bottom"):
                            if arg.id == char_active.get_equipped("bottom").id:
                                if wardrobe_chitchats:
                                    call her_main("I won't be walking bottomless on the school grounds..", "upset", "happyCl", "angry", "mid", cheeks="blush")
                                #Hint
                                $ wardrobe_fail_hint(3)
                                return
                label .too_much:
                if her_whoring < arg.level:
                    if wardrobe_chitchats:
                        $ random_number = renpy.random.randint(1, 5)
                        if random_number == 1:
                            call her_main("I'm not wearing that.", "annoyed", "base", "angry", "down")
                        elif random_number == 2:
                            call her_main("It's too slutty..", "annoyed", "happyCl", "angry", "R")
                        elif random_number == 3:
                            call her_main("I would look like a tramp, I refuse.", "annoyed", "wide", "angry", "mid")
                        elif random_number == 4:
                            call her_main("I'm not some Slytherin skank,[genie_name], ask them to humiliate themselves for your amusement..", "open", "narrow", "angry", "L")
                        elif random_number == 5:
                            call her_main("This is too much.", "annoyed", "narrow", "angry", "R")
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
