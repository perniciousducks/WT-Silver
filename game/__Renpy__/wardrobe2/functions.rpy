init python:
    def get_character_object(key):
        return character_list.get(key)
        
    def get_character_outfits_schedule(key):
        """Returns a list of outfits applicable for the current day and weather"""
        global daytime, weather_gen, raining, snowing, blizzard, storm
        
        schedule = []
        char = get_character_object(key)
        outfits = char.outfits_schedule[daytime]
        
        for i in outfits:
            if i.schedule[4] and (snowing or blizzard):
                schedule.append(i)
                continue
            if i.schedule[3] and raining:
                schedule.append(i)
                continue
            if i.schedule[2] and weather_gen >= 4 and not (raining or blizzard or snowing):
                schedule.append(i)
                continue
            if not (i.schedule[2] or i.schedule[3] or i.schedule[4]) and weather_gen < 4:
                schedule.append(i)
                continue
        return schedule
        
    def get_character_score(key):
        """Returns character outfit outrage score number"""
        score = 0
        char = get_character_object(key)
        for k, i in char.clothing.iteritems():
            if i[0] != None:
                if not i[0].type in ("tattoo0", "tattoo1", "piercing0", "piercing1", "buttplug"):
                    score += i[0].whoring
            else:
                if k == "top":
                    score += 30
                    if not char.get_worn("bra"):
                        score += 25
                        if char.get_worn("piercing1"):
                            score += 10
                        if char.get_worn("tattoo1"):
                            score += char.get_cloth("tattoo1").whoring
                elif k == "bra" and char.get_worn("top"):
                    score += 10
                elif k == "bottom":
                    score += 30
                    if char.get_worn("buttplug"):
                        score += 10
                    if not char.get_worn("panties"):
                        score += 25
                        if char.get_worn("buttplug"):
                            score += 25
                        if char.get_worn("piercing0"):
                            score += 10
                        if char.get_worn("tattoo0"):
                            score += char.get_cloth("tattoo0").whoring
                elif k == "panties" and char.get_worn("bottom"):
                    score += 15
        return score
        
    def slap_mouse_away():
        """Causes the mouse to be moved away from current position and displays a smoke effect"""
        renpy.play('sounds/slap.mp3')
        renpy.stop_predict_screen("gfx_effect")
        x, y = renpy.get_mouse_pos()
        xx = x+random.randint(-100, 100)
        yy = y+random.randint(-100, 100)
        renpy.show_screen("gfx_effect", start_x=x, start_y=y, target_x=xx, target_y=yy, img="smoke", xanchor=0.1, yanchor=0.7, zoom=0.2, duration=0.15)
        renpy.set_mouse_pos(xx, yy, duration=0.1)
        
    def love_mouse_away():
        """Causes the mouse to be moved away from current position and displays a heart effect"""
        renpy.play('sounds/kiss.mp3')
        renpy.stop_predict_screen("gfx_effect")
        x, y = renpy.get_mouse_pos()
        renpy.show_screen("gfx_effect", start_x=x, start_y=y, target_x=x, target_y=y, img="love_heart", xanchor=0.45, yanchor=0.65, zoom=0.2, timer=0.45)
        
    def wardrobe_fail_hint(value):
        """Causes the mouse to be moved away from current position and displays a smoke effect"""
        renpy.block_rollback()
        if cheats_active or game_difficulty <= 2:
            renpy.show_screen("blktone5")
            renpy.with_statement(d3)
            if active_girl == "tonks":
                renpy.say(None, "{size=+6}> Try again at friendship level {color=#7a0000}"+str(value)+"{/color}.{/size}")
            elif active_girl == "astoria":
                renpy.say(None, "{size=+6}> Try again at affection level {color=#7a0000}"+str(value)+"{/color}.{/size}")
            else:
                renpy.say(None, "{size=+6}> Try again at whoring level {color=#7a0000}"+str(value)+"{/color}.{/size}")
            renpy.hide_screen("blktone5")
            renpy.with_statement(d3)
        return