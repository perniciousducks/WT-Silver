label astoria_wardrobe_check(section, arg=None):
    if isinstance(arg, outfit_class):
        python:
            temp_count = [0, 0, 0]
            temp_score = 0
            for item in arg.group:
                if ast_affection < item.whoring and temp_count[0]*2 < item.whoring*2:
                    temp_count[0] = item.whoring
                if item.type in ("bra", "panties"):
                    temp_count[2] += 1
                    if char_active.get_cloth(item.type) != None:
                        if not char_active.get_cloth(item.type).id == item.id:
                            if ast_affection < 15:
                                temp_count[1] += 1

        # Outfit outrage score check
        if ast_affection < temp_count[0]*2:
            call ast_main("You're joking right? Why'd you think I would ever put this on...",face="annoyed")
            $ temp_score += 1
        if temp_count[2] < 2 and ast_affection < 20:
            if temp_score > 0:
                call ast_main("...There's no underwear on that... What kind of pervert created this?",face="annoyed")
            else:
                call ast_main("No panties? I'd rather keep mine on thank you very much...",face="annoyed")
            $ temp_score += 1
        elif temp_count[1] > 0:
            call ast_main("I prefer wearing the underwear I have on already...",face="annoyed")
            $ temp_score += 1

        if temp_score > 0:
            call ast_main("Sorry, [ast_genie_name] but I can't wear that.",face="annoyed")
            #Hint
            $ wardrobe_fail_hint(max(temp_count[0], 15, 20))
            return
    else:
        if section == "tabswitch":
            # Need more art
            $ TBA_message()
            return False

            # if ast_affection < 24:
                # call ast_main("As much as I'd like to get a new piercing or a tattoo I can't simply let you modify my body like that.",face="angry")
                # #Hint
                # $ wardrobe_fail_hint(24)
                # return False
            # return True
        elif section == "category":
            return arg #IMPORTANT
        elif section == "touching":
            if arg == "boobs":
                if ast_affection < 20:
                    $ slap_mouse_away()
                    
                    $ random_number = renpy.random.randint(1, 7)

                    if random_number == 1:
                        call ast_main("Hey, cut that out!",face="annoyed")
                    elif random_number == 2:
                        call ast_main("Ouch, that hurts...",face="annoyed")
                    elif random_number == 3:
                        call ast_main("Hey, no nipple twisters...",face="annoyed")
                    elif random_number == 4:
                        call ast_main("Bad Touch!",face="annoyed")
                    elif random_number == 5:
                        call ast_main("*EEEH* Don't you have better things to do?",face="annoyed")
                    elif random_number == 6:
                        call ast_main("{size=+5}What are you doing?{/size}",face="annoyed")
                    elif random_number == 7:
                        call ast_main("Stop that!",face="annoyed")
                    return
            if arg == "pussy":
                if ast_affection < 30:
                    $ slap_mouse_away()
                    
                    $ random_number = renpy.random.randint(1, 6)

                    if random_number == 1:
                        call ast_main("Hey, that's private property.",face="annoyed")
                    elif random_number == 2:
                        call ast_main("Get your filthy hands off me, [ast_genie_name].",face="annoyed")
                    elif random_number == 3:
                        call ast_main("Stop it, you creep.",face="annoyed")
                    elif random_number == 4:
                        call ast_main("Why would you do that... nasty old man...",face="annoyed")
                    elif random_number == 5:
                        call ast_main("Don't touch me...",face="annoyed")
                    elif random_number == 6:
                        call ast_main("Don't be gross, [ast_genie_name].",face="annoyed")

                    return
            $ love_mouse_away()
            call ast_main("", face="horny")
            return
        elif section == "toggle":
            if arg in ("bra", "panties"):
                if ast_affection < 15:
                    $ random_number = renpy.random.randint(1, 2)
                    if random_number == 1:
                        call ast_main("*Eeeh* No?",face="angry")
                    elif random_number == 2:
                        call ast_main("I'd rather keep my underwear on...",face="angry")
                    #Hint
                    $ wardrobe_fail_hint(15)
                    return
            elif arg in ("top", "bottom"):
                if ast_affection < 10:
                    if arg == "top":
                        call ast_main("You want me to take my clothes of... Oh sure, I'll just go ahead and bare my chest and all as well then shall I?",face="annoyed")
                        call ast_main("Just kidding, sure have a quick look, [ast_genie_name].",face="annoyed")
                        g4 "Really?!"
                        call ast_main("{size=+5}NO!{/size}",face="annoyed")
                        m "......"
                    elif arg == "bottom":
                        call ast_main("{size=+5}No, get away from me!{/size}",face="annoyed")
                    #Hint
                    $ wardrobe_fail_hint(10)
                    return
            $ char_active.toggle_wear(arg)
            return
        elif section == "equip":
            if arg.type in ("bra", "panties"):
                if ast_affection < 20:
                    if char_active.get_cloth("bra"):
                        if arg.id == char_active.get_cloth("bra").id:
                            call ast_main("I'd rather not do that right now, [ast_genie_name].",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(20)
                            return
                    if char_active.get_cloth("panties"):
                        if arg.id == char_active.get_cloth("panties").id:
                            call ast_main("",face="happy")
                            nar "> Astoria starts giggling."
                            call ast_main("Yeah right...",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(20)
                            return
                else:
                    if ast_affection < arg.whoring:
                        call astoria_wardrobe_too_much
                        return
            else:
                if ast_affection < 30:
                    if arg.type in ("top", "bottom"):
                        if char_active.get_cloth("top"):
                            if arg.id == char_active.get_cloth("top").id:
                                call ast_main("I guess I could... but I'm not going to.",face="annoyed")
                                #Hint
                                $ wardrobe_fail_hint(30)
                                return
                        if char_active.get_cloth("bottom"):
                            if arg.id == char_active.get_cloth("bottom").id:
                                call ast_main("Hey, that's a great idea... but not in this universe.",face="annoyed")
                                #Hint
                                $ wardrobe_fail_hint(30)
                                return
                label astoria_wardrobe_too_much:
                if ast_affection < arg.whoring:
                    $ random_number = renpy.random.randint(1, 3)
                    if random_number == 1:
                        call ast_main("Nuh uh, I'm not putting that on.",face="annoyed")
                    elif random_number == 2:
                        call ast_main("*Pfff* You want me to wear that? In your dreams old man...",face="annoyed")
                    else:
                        call ast_main("Don't be such a creep, thanks but no thanks.",face="annoyed")

                    #Hint
                    $ wardrobe_fail_hint(arg.whoring)
                    return

    $ renpy.play('sounds/equip.ogg')
    $ current_item = arg
    $ char_active.equip(current_item)
    return
