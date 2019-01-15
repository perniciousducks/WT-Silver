label house_points:
    # Hover temp variable
    $ toggle_points = False
    #Sum all house points
    $ total_points = slytherin+gryffindor+ravenclaw+hufflepuff
    # Outline settings
    $ points_outline = [ (1, "#000", 0, 0) ]
    if daytime:
        $ daygold_colour = "{color=#000}"
        $ daygold_outline = [ (1, "#e4ba70", 0, 0) ]
    else:
        $ daygold_colour = "{color=#FFF}"
        $ daygold_outline = [ (1, "#000", 0, 0) ]
    
    # Set value to our displayable variable
    $ slytherin_points = slytherin
    $ gryffindor_points = gryffindor
    $ ravenclaw_points = ravenclaw
    $ hufflepuff_points = hufflepuff
    
    #If points variable value exceedes one thousand make it a decimal number instead and round to x.x
    #Remember, "slytherin_points" is a string! If you need points integer use i.e. "slytherin" variable instead.
    if slytherin >= 1000:
        $ slytherin_points = str(round(slytherin/1000.0, 1))+"{size=-2}k{/size}"
    
    if gryffindor >= 1000:
        $ gryffindor_points = str(round(gryffindor/1000.0, 1))+"{size=-2}k{/size}"
        
    if ravenclaw >= 1000:
        $ ravenclaw_points = str(round(ravenclaw/1000.0, 1))+"{size=-2}k{/size}"
        
    if hufflepuff >= 1000:
        $ hufflepuff_points = str(round(hufflepuff/1000.0, 1))+"{size=-2}k{/size}"
        
    #Check who's in the lead
    $ housepoints = [slytherin, gryffindor, ravenclaw, hufflepuff]
    $ housepoints_sorted = sorted(housepoints, reverse=True)
    
    $ slytherin_place = housepoints_sorted.index(housepoints[0])+1
    $ gryffindor_place = housepoints_sorted.index(housepoints[1])+1
    $ ravenclaw_place = housepoints_sorted.index(housepoints[2])+1
    $ hufflepuff_place = housepoints_sorted.index(housepoints[3])+1
    
    # Set banners yanchor depending on the placement (ascending)
    $ housepoints_y = [None, 0.0, 0.25, 0.5, 0.75]
    
    return

screen ui_top_bar:
    tag ui
    zorder 2
    add "interface/topbar/"+str(interface_color)+"/bar.png"
    use ui_points
    use ui_stats
    
    #Debug
    if config.debug:
        hbox:
            xpos 10 ypos 40
            text "{size=-5}{color=#FFF}[total_points] [housepoints]\n[housepoints_y]\n[persistent.toggle_points]\n\nSly:[slytherin_place]\nGry:[gryffindor_place]\nRav:[ravenclaw_place]\nHuf:[hufflepuff_place]{/color}{/size}"
    
screen ui_points:
    #Slytherin
    imagebutton:
        xanchor 0.5
        xpos 540
        ypos 0
        if not persistent.toggle_points and not toggle_points: 
            yanchor housepoints_y[slytherin_place]
            idle "interface/topbar/slytherin.png"
        else: 
            yanchor 0
            idle "interface/topbar/slytherin_empty.png"
        action NullAction()
        
    #Gryffindor    
    imagebutton:
        xanchor 0.5
        xpos 540
        ypos 0
        if not persistent.toggle_points and not toggle_points: 
            yanchor housepoints_y[gryffindor_place]
            idle "interface/topbar/gryffindor.png"
        else: 
            yanchor 0
            idle "interface/topbar/gryffindor_empty.png"
        action NullAction()
        
    #Ravenclaw    
    imagebutton:
        xanchor 0.5
        xpos 540
        ypos 0
        if not persistent.toggle_points and not toggle_points: 
            yanchor housepoints_y[ravenclaw_place]
            idle "interface/topbar/ravenclaw.png"
        else: 
            yanchor 0
            idle "interface/topbar/ravenclaw_empty.png"
        action NullAction()
        
    #Hufflepuff    
    imagebutton:
        xanchor 0.5
        xpos 540
        ypos 0
        if not persistent.toggle_points and not toggle_points: 
            yanchor housepoints_y[hufflepuff_place]
            idle "interface/topbar/hufflepuff.png"
        else: 
            yanchor 0
            idle "interface/topbar/hufflepuff_empty.png"
        action NullAction()
    
    #If hovered or toggled variable
    if persistent.toggle_points or toggle_points:
        #Show raw points
        hbox:
            xanchor 0.5
            xpos 480
            ypos 30
            text "{size=-7}{color=#FFF}[slytherin_points]{/color}{/size}" outlines points_outline xalign 0.5 xanchor 0.5
        hbox:
            xanchor 0.5
            xpos 520
            ypos 30
            text "{size=-7}{color=#FFF}[gryffindor_points]{/color}{/size}" outlines points_outline xalign 0.5 xanchor 0.5
        hbox:
            xanchor 0.5
            xpos 560
            ypos 30
            text "{size=-7}{color=#FFF}[ravenclaw_points]{/color}{/size}" outlines points_outline xalign 0.5 xanchor 0.5
        hbox:
            xanchor 0.5
            xpos 601
            ypos 30
            text "{size=-7}{color=#FFF}[hufflepuff_points]{/color}{/size}" outlines points_outline xalign 0.5 xanchor 0.5
        
        #Show placement number
        hbox:
            xanchor 0.5
            xpos 480
            ypos 10
            text "{size=-2}{color=#FFF}[slytherin_place]{/color}{/size}" outlines points_outline
        hbox:
            xanchor 0.5
            xpos 520
            ypos 10
            text "{size=-2}{color=#FFF}[gryffindor_place]{/color}{/size}" outlines points_outline
        hbox:
            xanchor 0.5
            xpos 560
            ypos 10
            text "{size=-2}{color=#FFF}[ravenclaw_place]{/color}{/size}" outlines points_outline
        hbox:
            xanchor 0.5
            xpos 600
            ypos 10
            text "{size=-2}{color=#FFF}[hufflepuff_place]{/color}{/size}" outlines points_outline
            
    #Clickable area    
    imagebutton:
        xanchor 0.5
        yanchor 0
        xpos 540
        ypos 0
        idle "interface/topbar/hover_zone.png"
        hovered SetVariable("toggle_points", True)
        unhovered SetVariable("toggle_points", False)
        action ToggleVariable("persistent.toggle_points", True, False)
        
screen ui_stats:
    drag:
        drag_name "ui_stats"
        drag_handle (0, 0, 1.0, 1.0)
        draggable True

        window:
            style "empty"
            add "interface/topbar/"+str(interface_color)+"/stats.png" xpos 660 ypos 8
            
            hbox: ### DAYS COUNTER ###
                spacing 5 xpos 690 ypos 11
                text "{size=-6}[daygold_colour][day]{/color}{/size}" outlines daygold_outline
            hbox: ### GOLD COUNTER ###
                spacing 5 xpos 790 ypos 11
                text "{size=-6}[daygold_colour][gold]{/color}{/size}" outlines daygold_outline