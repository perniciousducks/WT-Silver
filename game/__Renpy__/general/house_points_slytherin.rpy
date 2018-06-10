

### Slytherin Points ###

label points_changes: # SLYTHERIN POINTS AWARDING
    if generating_points == 1 and game_difficulty >= 1: # NO POINTS FOR SLYTHERIN ON THIS DAY.
            pass
    else: # POINTS WILL BE AWARDED
        

        if game_difficulty <= 1:  #Easy Difficulty
            if snapes_support == 0: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+5")
        
            if snapes_support == 1: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+8")

            if snapes_support == 2: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+11")
        
            if snapes_support == 3: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+15")

            if snapes_support == 4: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+18")
        
            if snapes_support == 5: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+21")
        
            if snapes_support == 6: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+24")
            
            if snapes_support == 7: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+27")
        
            if snapes_support == 8: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+29")
        
            if snapes_support == 9: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+31")
            
            if snapes_support == 10: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+34")

            if snapes_support == 11: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+38")

            if snapes_support == 12: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+41")
        
            if snapes_support == 13: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+44")
            
            if snapes_support == 14: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+47")

            if snapes_support == 15: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+50")

        else:   #normal difficulty

            if snapes_support == 0: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+2")
       
            if snapes_support == 1: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+5")

            if snapes_support == 2: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+7")
        
            if snapes_support == 3: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+8")

            if snapes_support == 4: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+11")
        
            if snapes_support == 5: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+13")
        
            if snapes_support == 6: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+15")
            
            if snapes_support == 7: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+17")
        
            if snapes_support == 8: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+19")
        
            if snapes_support == 9: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+21")
            
            if snapes_support == 10: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+23")

            if snapes_support == 11: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+25")

            if snapes_support == 12: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+27")
        
            if snapes_support == 13: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+29")
            
            if snapes_support == 14: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+31")

            if snapes_support == 15: #Controls how much points is awarded to SLYTHERIN daily.
                call add_house_points("s","+40")
    return

      
#        if snapes_support == 1: #Controls how much points is awarded to SLYTHERIN daily.
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




        
    
    
