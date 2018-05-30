

### Gryffindor, Hufflepuff, Ravenclaw Points ###

label points_changes_gryffindor:

    ### GRYFFINDOR POINTS ###
    if generating_points_gryffindor == 1 or generating_points_gryffindor == 2: # 0 POINT.
        pass
    elif generating_points_gryffindor == 3 or generating_points_gryffindor == 4: # 1 POINTS.
        $ gryffindor +=1
        hide screen g_p_u
        $ g_p_u_pic = "what_01_points"
        show screen g_p_u

    elif generating_points_gryffindor == 5 or generating_points_gryffindor == 6: # 2 POINTS.
        $ gryffindor +=2
        hide screen g_p_u
        $ g_p_u_pic = "what_02_points"
        show screen g_p_u
    
    elif generating_points_gryffindor == 7 or generating_points_gryffindor == 8: # 3 POINTS
        $ gryffindor +=3
        hide screen g_p_u
        $ g_p_u_pic = "what_03_points"
        show screen g_p_u

    elif generating_points_gryffindor == 9: # 5 POINTS.
        $ gryffindor +=5
        hide screen g_p_u
        $ g_p_u_pic = "what_05_points"
        show screen g_p_u

        
    elif generating_points_gryffindor == 10: 
        $ gryffindor +=11
        hide screen g_p_u
        $ g_p_u_pic = "what_11_points"
        show screen g_p_u



    
###  Hufflepuff ###


    if generating_points_hufflepuff == 1 or generating_points_hufflepuff == 2: # 0 POINT.
        pass
        
    elif generating_points_hufflepuff == 3 or generating_points_hufflepuff == 4: # 1 POINTS.
        $ hufflepuff +=1
        hide screen h_p_u
        $ h_p_u_pic = "what_01_points"
        show screen h_p_u
    
    elif generating_points_hufflepuff == 5 or generating_points_hufflepuff == 6: # 2 POINTS.
        $ hufflepuff +=2
        hide screen h_p_u
        $ h_p_u_pic = "what_02_points"
        show screen h_p_u
    
    elif generating_points_hufflepuff == 7 or generating_points_hufflepuff == 8: # 3 POINTS
        $ hufflepuff +=4
        hide screen h_p_u
        $ h_p_u_pic = "what_04_points"
        show screen h_p_u
        
    elif generating_points_hufflepuff == 9: # 5 POINTS.
        $ hufflepuff +=7
        hide screen h_p_u
        $ h_p_u_pic = "what_07_points"
        show screen h_p_u
        
    elif generating_points_hufflepuff == 10: #15 POINTS.
        $ hufflepuff +=14
        hide screen h_p_u
        $ h_p_u_pic = "what_14_points"
        show screen h_p_u


### Ravenclaw ###


    if generating_points_ravenclaw == 1 or generating_points_ravenclaw == 2: # 0 POINT.
        pass
    elif generating_points_ravenclaw == 3 or generating_points_ravenclaw == 4: # 1 POINTS.
        $ ravenclaw +=1
        hide screen r_p_u
        $ r_p_u_pic = "what_01_points"
        show screen r_p_u
    
    elif generating_points_ravenclaw == 5 or generating_points_ravenclaw == 6: # 2 POINTS.
        $ ravenclaw +=2
        hide screen r_p_u
        $ r_p_u_pic = "what_02_points"
        show screen r_p_u
    
    elif generating_points_ravenclaw == 7 or generating_points_ravenclaw == 8: # 3 POINTS
        $ ravenclaw +=6
        hide screen r_p_u
        $ r_p_u_pic = "what_06_points"
        show screen r_p_u
        
    elif generating_points_ravenclaw == 9: # 5 POINTS.
        $ ravenclaw +=8
        hide screen r_p_u
        $ r_p_u_pic = "what_08_points"
        show screen r_p_u
        
    elif generating_points_ravenclaw == 10: #15 POINTS.
        $ ravenclaw +=13
        hide screen r_p_u
        $ r_p_u_pic = "what_13_points"
        show screen r_p_u





return 


