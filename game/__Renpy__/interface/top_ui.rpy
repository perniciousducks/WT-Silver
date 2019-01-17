init python:
    def ui_dropped(drags, drops):
        drags[0].snap(drags[0].target_x, 0)
        return
        
    def text_points(points):
        if points < 1000:
            return str(points)
        else:
            return  str(round(points/1000.0, 1))+"{size=-2}k{/size}"

label house_points:
    # Debug
    if config.debug:
        $ total_points = slytherin+gryffindor+ravenclaw+hufflepuff
    
    # Hover temp variable and UI lock
    $ toggle_ui_lock = True
    $ toggle_points = False
    
    # Outline settings
    $ points_outline = [ (1, "#000", 0, 0) ]
    if daytime:
        $ daygold_colour = "{color=#000}"
        $ daygold_outline = [ (1, "#e4ba70", 0, 0) ]
    else:
        $ daygold_colour = "{color=#FFF}"
        $ daygold_outline = [ (1, "#000", 0, 0) ]
    
    #If points variable value exceedes one thousand make it a decimal number instead and round to x.x
    #Remember, "slytherin_points" is a string! If you need points integer use i.e. "slytherin" variable instead.
    $ slytherin_points = text_points(slytherin)
    $ gryffindor_points = text_points(gryffindor)
    $ ravenclaw_points = text_points(ravenclaw)
    $ hufflepuff_points = text_points(hufflepuff)
        
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

screen ui_top_bar():
    tag ui
    zorder 2
    add "interface/topbar/"+str(interface_color)+"/bar.png"
    use ui_stats
    use ui_points
    
    #Debug
    if config.debug:
        hbox:
            xpos 10 ypos 40
            text "{size=-5}{color=#FFF}[total_points] [housepoints]\n[housepoints_y]\nToggle display:[persistent.toggle_points]\n\nSly:[slytherin_place]\nGry:[gryffindor_place]\nRav:[ravenclaw_place]\nHuf:[hufflepuff_place]\nUI lock:[toggle_ui_lock]{/color}{/size}"
    
screen ui_points():
    drag:
        drag_name "ui_points"
        draggable not toggle_ui_lock
        dragged ui_dropped
        drag_handle(0, 0, 1.0, 1.0)
        xpos 540 ypos 0
        xanchor 0.5
        frame:
            style "empty"
            xsize 162
            ysize 64
            xanchor 0.5
            
            if not persistent.toggle_points and not toggle_points:
                add "interface/topbar/slytherin.png" yanchor housepoints_y[slytherin_place]
                add "interface/topbar/gryffindor.png" yanchor housepoints_y[gryffindor_place]
                add "interface/topbar/ravenclaw.png" yanchor housepoints_y[ravenclaw_place]
                add "interface/topbar/hufflepuff.png" yanchor housepoints_y[hufflepuff_place]
            else:
                # Add empty banners
                add "interface/topbar/slytherin_empty.png" yanchor 0
                add "interface/topbar/gryffindor_empty.png" yanchor 0
                add "interface/topbar/ravenclaw_empty.png" yanchor 0
                add "interface/topbar/hufflepuff_empty.png" yanchor 0
                # Show points
                text "{size=-7}{color=#FFF}[slytherin_points]{/color}{/size}" outlines points_outline xpos 17 ypos 30 xanchor 0.5
                text "{size=-7}{color=#FFF}[gryffindor_points]{/color}{/size}" outlines points_outline xpos 58 ypos 30 xanchor 0.5
                text "{size=-7}{color=#FFF}[ravenclaw_points]{/color}{/size}" outlines points_outline xpos 98 ypos 30 xanchor 0.5
                text "{size=-7}{color=#FFF}[hufflepuff_points]{/color}{/size}" outlines points_outline xpos 139 ypos 30 xanchor 0.5
                # Show placement number
                text "{size=-2}{color=#FFF}[slytherin_place]{/color}{/size}" outlines points_outline xpos 17 ypos 10 xanchor 0.5
                text "{size=-2}{color=#FFF}[gryffindor_place]{/color}{/size}" outlines points_outline xpos 58 ypos 10 xanchor 0.5
                text "{size=-2}{color=#FFF}[ravenclaw_place]{/color}{/size}" outlines points_outline xpos 98 ypos 10 xanchor 0.5
                text "{size=-2}{color=#FFF}[hufflepuff_place]{/color}{/size}" outlines points_outline xpos 139 ypos 10 xanchor 0.5
            
            if toggle_ui_lock:  
                imagebutton:
                    idle "interface/topbar/hover_zone.png"
                    hovered SetVariable("toggle_points", True)
                    unhovered SetVariable("toggle_points", False)
                    action ToggleVariable("persistent.toggle_points", True, False)
                    activate_sound "sounds/click3.mp3"

    # Toggle UI lock button
    imagebutton:
        xpos 1047
        idle "interface/topbar/buttons/"+str(interface_color)+"/ui_%s.png" % toggle_ui_lock
        action ToggleVariable("toggle_ui_lock", False, True)
        activate_sound "sounds/click3.mp3"

screen ui_stats:
    drag:
        drag_name "ui_stats"
        draggable not toggle_ui_lock
        dragged ui_dropped
        frame:
            style "empty"
            xsize 217
            ysize 26
            add "interface/topbar/"+str(interface_color)+"/stats.png" xalign 0.5 yalign 1.0

            hbox:
                xpos 40 ypos 11
                text "{size=-6}[daygold_colour][day]{/color}{/size}" outlines daygold_outline
            hbox:
                xpos 140 ypos 11
                text "{size=-6}[daygold_colour][gold]{/color}{/size}" outlines daygold_outline