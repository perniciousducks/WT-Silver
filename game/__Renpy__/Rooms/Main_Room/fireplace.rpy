label fireplace:
    if day == 1:
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
                hide screen genie_stand
                hide screen chair_left #Empty chair near the desk.
                hide screen desk
                with Dissolve(0.5)
        jump day_main_menu

    if not daytime and (1 < weather_gen < 4) and (puzzle_random == 0) and (found_puzzle_1 == False):
        menu:
            "Search fireplace":
                m "(Hmm, there's something glimmering in the fireplace.)"
                "Click Click Click Click Click!!!"
                m "(A loose brick...If only I could..*Hhng*...There we go.)"
                call give_reward("You have unlocked a puzzle in the cupboard", "interface/icons/icon_puzzle.png")
                m "Seems straight forward enough"
                hide screen fireplace_glow
                $ found_puzzle_1 = True

            "Turn fire off/on":
                if fire_in_fireplace:
                    $ fire_in_fireplace = False
                    hide screen fireplace_fire
                    stop bg_sounds #Stops playing the fire SFX.
                else:
                    $ fire_in_fireplace = True
                    show screen fireplace_fire
    else:
        if fire_in_fireplace:
            $ fire_in_fireplace = False
            hide screen fireplace_fire
            stop bg_sounds #Stops playing the fire SFX.
        else:
            $ fire_in_fireplace = True
            show screen fireplace_fire

    jump day_main_menu
