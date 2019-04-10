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

    if day >= 25 and not daytime and (1 < weather_gen < 4) and (puzzle_box_ITEM.unlocked == False and unlocked_7th == False):
        menu:
            "Search fireplace":
                m "(Hmm, there's something glimmering in the fireplace.)"
                "Click Click Click Click Click!!!"
                m "(A loose brick...If only I could..*Hhng*...There we go.)"
                call give_reward("A puzzle box has been added to your inventory!", "interface/icons/icon_puzzle.png")
                m "Seems straight forward enough."
                $ puzzle_box_ITEM.unlocked = True

    else:
        if fire_in_fireplace:
            $ fire_in_fireplace = False
            hide screen fireplace_fire
            stop bg_sounds #Stops playing the fire SFX.
        else:
            $ fire_in_fireplace = True
            $ stat_fireplace_counter += 1
            show screen fireplace_fire

    jump day_main_menu
