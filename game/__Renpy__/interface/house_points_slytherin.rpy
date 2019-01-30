

### Slytherin Points ###

label slytherin_points: #points_changes: # SLYTHERIN POINTS AWARDING
    if generating_points == 1 and game_difficulty >= 1: # NO POINTS FOR SLYTHERIN ON THIS DAY.
            pass
    else: # POINTS WILL BE AWARDED


        if game_difficulty <= 1:  #Easy Difficulty
            if sna_support == 0: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 8
                $ slytherin_p_gain = "+8"

            if sna_support == 1: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 8
                $ slytherin_p_gain = "+8"

            if sna_support == 2: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 11
                $ slytherin_p_gain = "+11"

            if sna_support == 3: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 15
                $ slytherin_p_gain = "+15"

            if sna_support == 4: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 18
                $ slytherin_p_gain = "+18"

            if sna_support == 5: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 21
                $ slytherin_p_gain = "+21"

            if sna_support == 6: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 24
                $ slytherin_p_gain = "+24"

            if sna_support == 7: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 27
                $ slytherin_p_gain = "+27"

            if sna_support == 8: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 29
                $ slytherin_p_gain = "+29"

            if sna_support == 9: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 31
                $ slytherin_p_gain = "+31"

            if sna_support == 10: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 34
                $ slytherin_p_gain = "+34"

            if sna_support == 11: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 38
                $ slytherin_p_gain = "+38"

            if sna_support == 12: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 41
                $ slytherin_p_gain = "+41"

            if sna_support == 13: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 44
                $ slytherin_p_gain = "+44"

            if sna_support == 14: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 47
                $ slytherin_p_gain = "+47"

            if sna_support == 15: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 50
                $ slytherin_p_gain = "+50"

        else:   #normal difficulty

            if sna_support == 0: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 2
                $ slytherin_p_gain = "+2"

            if sna_support == 1: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 5
                $ slytherin_p_gain = "+5"

            if sna_support == 2: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 7
                $ slytherin_p_gain = "+7"

            if sna_support == 3: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 8
                $ slytherin_p_gain = "+8"

            if sna_support == 4: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 11
                $ slytherin_p_gain = "+11"

            if sna_support == 5: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 13
                $ slytherin_p_gain = "+13"

            if sna_support == 6: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 15
                $ slytherin_p_gain = "+15"

            if sna_support == 7: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 17
                $ slytherin_p_gain = "+17"

            if sna_support == 8: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 19
                $ slytherin_p_gain = "+19"

            if sna_support == 9: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 21
                $ slytherin_p_gain = "+21"

            if sna_support == 10: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 23
                $ slytherin_p_gain = "+23"

            if sna_support == 11: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 25
                $ slytherin_p_gain = "+25"

            if sna_support == 12: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 27
                $ slytherin_p_gain = "+27"

            if sna_support == 13: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 29
                $ slytherin_p_gain = "+29"

            if sna_support == 14: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 31
                $ slytherin_p_gain = "+31"

            if sna_support == 15: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin += 40
                $ slytherin_p_gain = "+40"
    return


#        if sna_support == 1: #Controls how much points is awarded to SLYTHERIN daily.
#            $ slytherin +=7
#            "Slytherin got +7 points."

#        if day >= 15 and day <= 21: #WEEK No.3 (Needs 30)
#            $ slytherin +=10
#            "Slytherin got +10 points."

#        if day >= 22 and day <= 28: #WEEK No.4 (Needs 50)
#            $ slytherin +=15
#            "Slytherin got +15 points."

#        if day >= 29 and day <= 35: #WEEK No.5 (Needs 60)
#            $ slytherin +=15
#            "Slytherin got +15 points."

#        if day >= 36 and day <= 42: #WEEK No.6 (Needs 70)
#            $ slytherin +=22
#            "Slytherin got +22 points."

#        if day >= 43 and day <= 49: #WEEK No.7 (Needs 90)
#            $ slytherin +=26
#            "Slytherin got +26 points."

#        if day >= 50 and day <= 56: #WEEK No.8 (Needs 100)
#            $ slytherin +=32
#            "Slytherin got +32 points."

#        if day >= 57 and day <= 63: #WEEK No.9 (Needs 110)
#            $ slytherin +=36
#            "Slytherin got +36 points."

#        if day >= 64 and day <= 70: #WEEK No.10 (Needs 130)
#            $ slytherin +=43
#            "Slytherin got +43 points."

#        if day >= 71 and day <= 77: #WEEK No.11 (Needs 140)
#            $ slytherin +=46
#            "Slytherin got +46 points."

#        if day >= 78 and day <= 84: #WEEK No.12 (Needs 150)
#            $ slytherin +=50
#            "Slytherin got +50 points."

#        if day >= 85 and day <= 91: #WEEK No.13 (Needs 170)
#            $ slytherin +=56
#            "Slytherin got +56 points."

#        if day >= 92 and day <= 98: #WEEK No.14 (Needs 185)
#            $ slytherin +=61
#            "Slytherin got +61 points."

#        if day >= 105: #WEEK No.15 (Needs 200)
#            $ slytherin +=66
#            "Slytherin got +66 points."
