label tonks_wardrobe_check(section, arg=None):
    if isinstance(arg, outfit_class):
        python:
            temp_count = [0, 0, 0]
            temp_score = 0
            for item in arg.group:
                if ton_friendship < item.whoring*2 and temp_count[0]*2 < item.whoring*2:
                    temp_count[0] = item.whoring
                if item.type in ("bra", "panties"):
                    temp_count[2] += 1
                    if char_active.get_cloth(item.type) != None:
                        if not char_active.get_cloth(item.type).id == item.id:
                            if ton_friendship < 15:
                                temp_count[1] += 1
                            
        # Outfit outrage score check
        if ton_friendship < temp_count[0]*2:
            call ton_main("It looks lovely, but I doubt our studends would understand...",face="annoyed")
            $ temp_score += 1
        if temp_count[2] < 2 and ton_friendship < 20:
            if temp_score > 0:
                call ton_main("...especially because of missing underwear",face="annoyed")
            else:
                call ton_main("No panties? I like that, but no thanks, I'm at work.",face="annoyed")
            $ temp_score += 1
        elif temp_count[1] > 0:
            call ton_main("I feel alright wearing my current set of underwear.",face="annoyed")
            $ temp_score += 1
            
        if temp_score > 0:
            call ton_main("Sorry, [ton_genie_name] but I can't wear it.",face="annoyed")
            #Hint
            $ wardrobe_fail_hint(max(temp_count[0]*2, 15, 20))
            return
    else:
        if section == "tabswitch":
            if ton_friendship < 24:
                call ton_main("As much as I'd like to get a new piercing or a tattoo I can't simply let you modify my body like that.",face="angry")
                #Hint
                $ wardrobe_fail_hint(24)
                return False
            return True
        elif section == "touching":
            $ random_number = renpy.random.randint(1, 10)
            if arg == "boobs":
                if ton_friendship < 20:
                    $ slap_mouse_away()
                    
                    if random_number == 1:
                        call ton_main("That's not how a headmaster should treat their subordinates.",face="annoyed")
                    elif random_number == 2:
                        call ton_main("Its inappropriate, lets keep it civil alright?",face="annoyed")
                    return
            if arg == "pussy":
                if ton_friendship < 30:
                    $ slap_mouse_away()
                    
                    if random_number == 1:
                        call ton_main("You've gotta earn it first.",face="annoyed")
                    elif random_number == 2:
                        call ton_main("If you'd like to keep these hands intact I suggest you stop it right now, [ton_genie_name].",face="annoyed")
                    return
            $ love_mouse_away()
            call ton_main("", face="horny")
            return
        elif section == "toggle":
            if arg in ("bra", "panties"):
                if ton_friendship < 15:
                    $ random_number = renpy.random.randint(1, 2)
                    if random_number == 1:
                        call ton_main("Maybe another time..",face="angry")
                    elif random_number == 2:
                        call ton_main("I like my underwear in its proper place.",face="angry")
                    #Hint
                    $ wardrobe_fail_hint(15)
                    return
            elif arg in ("top", "bottom"):
                if ton_friendship < 10:
                    if arg == "top":
                        call ton_main("Take my top off for a quickie? Are you insane?!",face="annoyed")
                        call ton_main("Just kidding, sure have a quick look, [ton_genie_name].",face="annoyed")
                        $ char_active.toggle_wear(arg)
                        call ton_main("",face="happy")
                        pause 1.0
                        call ton_main("",face="happy")
                        pause 1.0
                        call ton_main("",face="happy")
                        $ char_active.toggle_wear(arg)
                        g4 "What gives?!"
                        call ton_main("Your time's up.",face="annoyed")
                        m "......"
                    elif arg == "bottom":
                        call ton_main("Maybe later.",face="annoyed")
                    #Hint
                    $ wardrobe_fail_hint(10)
                    return
            $ char_active.toggle_wear(arg)
            return
        elif section == "equip":
            if arg.type in ("bra", "panties"):
                if ton_friendship < 20:
                    if char_active.get_cloth("bra"):
                        if arg.id == char_active.get_cloth("bra").id:
                            call ton_main("If you behave maybe I'll let you take a peek later, [ton_genie_name].",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(20)
                            return
                    if char_active.get_cloth("panties"):
                        if arg.id == char_active.get_cloth("panties").id:
                            call ton_main("",face="happy")
                            nar "> Suddenly Tonks starts laughing."
                            call ton_main("You're bold I'll give you that much.",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(20)
                            return
                else:
                    if ton_friendship < arg.whoring:
                        call tonks_wardrobe_too_much
                        return
            else:
                if ton_friendship < 30:
                    if arg.type in ("top", "bottom"):
                        if char_active.get_cloth("top"):
                            if arg.id == char_active.get_cloth("top").id:
                                call ton_main("Mmm.. I like where your head is at, but I have to refuse.",face="annoyed")
                                #Hint
                                $ wardrobe_fail_hint(30)
                                return
                        if char_active.get_cloth("bottom"):
                            if arg.id == char_active.get_cloth("bottom").id:
                                call ton_main("As much as I'd like to I can't walk bottomless around school grounds.",face="annoyed")
                                #Hint
                                $ wardrobe_fail_hint(30)
                                return
                label tonks_wardrobe_too_much:
                if ton_friendship < arg.whoring*2:
                    $ random_number = renpy.random.randint(1, 3)
                    if random_number == 1:
                        call ton_main("I can't wear that in public, even if I wanted to.",face="annoyed")
                    elif random_number == 2:
                        call ton_main("It does look nice but I cannot show myself in such attire around hogwarts.",face="annoyed")
                    else:
                        call ton_main("It would make me look like a whore, thanks but no thanks.",face="annoyed")
                    
                    #Hint
                    $ wardrobe_fail_hint(arg.whoring*2)
                    return
                    
    $ renpy.play('sounds/equip.ogg')
    $ current_item = arg
    $ char_active.equip(current_item)
    return