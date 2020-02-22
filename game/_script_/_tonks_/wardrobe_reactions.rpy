label tonks_wardrobe_check(section, arg=None):
    if isinstance(arg, DollOutfit):
        python:
            temp_count = [0, 0, 0] # [0: required level, 1: underwear changed, 2: underwear equipped]
            temp_score = 0
            for item in arg.group:
                if ton_friendship < item.level and temp_count[0] < item.level:
                    temp_count[0] = item.level
                if item.type in ("bra", "panties"):
                    temp_count[2] += 1
                    if char_active.is_worn(item.type) != None:
                        if not char_active.get_equipped(item.type).id == item.id:
                            if ton_friendship < 15:
                                temp_count[1] += 1

        # Outfit outrage score check
        if ton_friendship < temp_count[0]:
            call ton_main("It looks lovely, but you'd have to prove yourself a bit more before I put that on...",face="annoyed",eyebrows="angry",mouth="smile")
            $ temp_score += 1
        if temp_count[2] < 2 and ton_friendship < 0: # Disabled underwear check
            if temp_score > 0:
                call ton_main("...especially something without underwear",face="annoyed",eyebrows="angry",mouth="horny")
            else:
                call ton_main("No panties? I like that, but no thanks, I'm at work.",face="annoyed",eyebrows="angry",mouth="base")
            $ temp_score += 1
        elif temp_count[1] > 0:
            call ton_main("I feel perfectly fine wearing my current set of underwear for the time being.",face="annoyed")
            $ temp_score += 1

        if temp_score > 0:
            call ton_main("Sorry, [ton_genie_name] but I can't wear that.",face="annoyed")
            #Hint
            $ wardrobe_fail_hint(max(temp_count[0], 15, 20))
            return
    else:
        if section == "tabswitch":
            # Need more art
            $ TBA_message()
            return False

            # if ton_friendship < 24:
                # call ton_main("As much as I'd like to get a new piercing or a tattoo I can't simply let you modify my body like that.",face="angry")
                # #Hint
                # $ wardrobe_fail_hint(24)
                # return False
            # return True
        elif section == "category":
            #haircolour fix
            if arg[1] == "head":
                $ tonks.get_equipped("hair").color = tonks_haircolor
            return arg #IMPORTANT
        elif section == "touching":
            $ random_number = renpy.random.randint(1, 10)
            if arg == "boobs":
                if ton_friendship < 20:
                    $ slap_mouse_away()
                    if wardrobe_chitchats:
                        if random_number == 1:
                            call ton_main("That's not how a headmaster should treat their subordinates.",face="annoyed")
                        elif random_number == 2:
                            call ton_main("It's inappropriate, lets keep it civil okay?",face="annoyed")
                        elif random_number == 3:
                            call ton_main("Someone fancy themselves a bit of a bad boy?",face="annoyed",mouth="base")
                        elif random_number == 4:
                            call ton_main("Hey, those are my funbags... Don't be naughty.",face="annoyed",mouth="horny")
                        elif random_number == 5:
                            call ton_main("Hey now, someone's getting a bit ahead of themselves.",face="annoyed")
                        elif random_number == 6:
                            call ton_main("Those aren't for you to play with...",face="annoyed")
                    return
            if arg == "pussy":
                if ton_friendship < 30:
                    $ slap_mouse_away()
                    if wardrobe_chitchats:
                        if random_number == 1:
                            call ton_main("You have to to earn it first.",face="annoyed")
                        elif random_number == 2:
                            call ton_main("If you'd like to keep these hands intact I suggest you stop it right now, [ton_genie_name].",face="annoyed")
                        elif random_number == 3:
                            call ton_main("Hey, who said you had permission to approach the chamber of secrets?",face="annoyed",eyebrows="angry",mouth="smile")
                        elif random_number == 4:
                            call ton_main("That place is reserved for good boys and girls...",face="annoyed",eyebrows="angry",mouth="smile")
                        elif random_number == 5:
                            call ton_main("That forest is forbidden entry for first years... let's get to know each other a bit better first...",face="annoyed",eyebrows="angry",mouth="smile")
                    return
            $ love_mouse_away()
            call ton_main("", face="horny")
            return
        elif section == "toggle":
            if arg in ("bra", "panties"):
                if ton_friendship < 0: # Disabled underwear check
                    if wardrobe_chitchats:
                        $ random_number = renpy.random.randint(1, 2)
                        if random_number == 1:
                            call ton_main("Maybe another time...",face="annoyed",eyebrows="raised")
                        elif random_number == 2:
                            call ton_main("I like my underwear in its proper place.",face="annoyed",eyebrows="base",mouth="angry")
                    #Hint
                    $ wardrobe_fail_hint(15)
                    return
            elif arg in ("top", "bottom"):
                if ton_friendship < 10:
                    if arg == "top":
                        if wardrobe_chitchats:
                            call ton_main("Someone's being naughty... I might have to give you a spanking for that.",face="annoyed",eyebrows="angry",mouth="smile")
                            call ton_main("Just kidding! Sure, have a quick look, [ton_genie_name].",face="annoyed",eyebrows="raised",mouth="horny")
                            $ char_active.toggle_wear(arg)
                            $ char_active.strip("robe")
                            call ton_main("",face="happy")
                            pause 1.0
                            call ton_main("",face="happy")
                            pause 1.0
                            call ton_main("",face="happy")
                            $ char_active.toggle_wear(arg)
                            $ char_active.wear("robe")
                            g4 "What gives?!"
                            call ton_main("Time's up.",face="annoyed",eyebrows="angry",mouth="smile")
                            m "......"
                    elif arg == "bottom":
                        if wardrobe_chitchats:
                            call ton_main("Maybe later.",face="annoyed",eyebrows="raised")
                    #Hint
                    $ wardrobe_fail_hint(10)
                    return
            $ char_active.toggle_wear(arg)
            return
        elif section == "equip":
            if arg.type in ("bra", "panties"):
                if ton_friendship < 0: # Disabled underwear check
                    if char_active.get_equipped("bra"):
                        if arg.id == char_active.get_equipped("bra").id:
                            if wardrobe_chitchats:
                                call ton_main("If you behave maybe I'll let you take a peek later, [ton_genie_name].",face="annoyed",eyebrows="angry",mouth="smile")
                            #Hint
                            $ wardrobe_fail_hint(20)
                            return
                    if char_active.get_equipped("panties"):
                        if arg.id == char_active.get_equipped("panties").id:
                            if wardrobe_chitchats:
                                call ton_main("",face="happy")
                                nar "> Tonks clicks her tongue, staring at you in a disapproving manner."
                                call ton_main("Getting ahead of ourselves are we? You're bold, I'll give you that much.",face="annoyed",eyebrows="angry",mouth="smile")
                            #Hint
                            $ wardrobe_fail_hint(20)
                            return
                else:
                    if ton_friendship < arg.level:
                        call .too_much
                        return
            else:
                if ton_friendship < 30:
                    if arg.type in ("top", "bottom"):
                        if char_active.get_equipped("top"):
                            if arg.id == char_active.get_equipped("top").id:
                                if wardrobe_chitchats:
                                    call ton_main("Mmm... I like where your head is at, but I have to refuse.",face="annoyed",eyebrows="angry",mouth="smile")
                                #Hint
                                $ wardrobe_fail_hint(30)
                                return
                        if char_active.get_equipped("bottom"):
                            if arg.id == char_active.get_equipped("bottom").id:
                                if wardrobe_chitchats:
                                    call ton_main("Really... doing that would be quite uncouth don't you think?",face="annoyed",eyebrows="angry",mouth="horny")
                                #Hint
                                $ wardrobe_fail_hint(30)
                                return
                label .too_much:
                if ton_friendship < arg.level:
                    if wardrobe_chitchats:
                        $ random_number = renpy.random.randint(1, 3)
                        if random_number == 1:
                            call ton_main("Not yet big boy, perhaps once this scheme of ours comes more into fruition...",face="annoyed",eyebrows="angry",mouth="smile")
                        elif random_number == 2:
                            call ton_main("It does look nice but you need to deserve it...",face="annoyed",eyebrows="angry",mouth="smile")
                        else:
                            call ton_main("Hmm, what would you think of me if I wore this...? Later perhaps.",face="annoyed",eyebrows="raised",mouth="horny")

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