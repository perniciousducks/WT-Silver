label fireplace:
    if fireplace_examined:
        if not day == 1:
            $ fire_in_fireplace = not fire_in_fireplace 
        
        if not daytime and (1 < weather_gen < 4) and (puzzle_random == 0) and (found_puzzle_1 == False):
            menu:
                "Search fireplace":
                    m "(Hmm, there's something glimmering in the fireplace.)"
                    "Click Click Click Click Click!!!"
                    m "(A loose brick...If only I could..*Hhng*...There we go.)"
                    call give_reward("You have unlocked a puzzle in the cupboard", "images/store/unlock_puzzle_1.png")
                    m "Seems straight forward enough"
                    hide screen glow_effect
                    $ found_puzzle_1 = True
                    
                "Turn fire off/on":
                    if fire_in_fireplace:
                        show screen fireplace_fire
                    else:
                        hide screen fireplace_fire
                        stop bg_sounds #Stops playing the fire SFX.
        else:        
            if fire_in_fireplace:
                show screen fireplace_fire
            else:
                hide screen fireplace_fire
                stop bg_sounds #Stops playing the fire SFX.
        
        jump day_main_menu
    else:
        menu:
            "-Examine the fireplace-" if not fireplace_examined:
                $ fireplace_examined = True
                hide screen genie
                call gen_chibi("stand","mid","base") 
                show screen chair_left #Empty chair near the desk.
                show screen desk
                with Dissolve(0.5)
                m "Hm... Looks like an ordinary fireplace..."
                show screen genie
                hide screen genie_stands
                hide screen chair_left #Empty chair near the desk.
                hide screen desk
                with Dissolve(0.5)
                jump day_main_menu

            "-Never mind-":
                jump day_main_menu
