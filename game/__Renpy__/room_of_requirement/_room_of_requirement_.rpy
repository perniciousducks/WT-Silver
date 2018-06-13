

screen room_of_requirement:
    add "images/room_of_requirement/empty_room.png"
    add "images/main_room/door.png" at Position(xpos=898, ypos=315, xanchor="center", yanchor="center")
    add "images/room_of_requirement/mirror.png" xpos 100 ypos 180
    add "images/main_room/candle.png" at Position(xpos=350, ypos=200, xanchor="center", yanchor="center")
    add "images/main_room/candle.png" at Position(xpos=700, ypos=200, xanchor="center", yanchor="center")
    zorder -1
    
screen room_of_requirement_menu:
    tag room_screen
    
    imagebutton: # DOOR
        xpos 758+140
        ypos 315
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/main_room/door.png"
        hover "images/main_room/door_hover.png"
        action [Hide("room_of_rquirement_menu"), Jump("door")]
        
    imagebutton: # Cadle Fire left
        xpos 350
        ypos 200
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/main_room/candle.png"
        hover "images/main_room/candle.png"
        action [Hide("room_of_rquirement_menu"), Jump("door")]
        
    imagebutton: # Cadle Fire Right
        xpos 700
        ypos 200
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/main_room/candle.png"
        hover "images/main_room/candle.png"
        action [Hide("room_of_rquirement_menu"), Jump("door")]
    zorder -1
    
label enter_room_of_req:
    show screen room_of_requirement
    if first_visit_req == False:
        call sna_chibi(xpos = "200", ypos = "250")
        call gen_chibi(action = "", xpos = "780", ypos = "200", flip=True)
        m "It's just and empty room....with a mirror?"
        s "A mirror you say?"
        m "Snape!... cough I mean, Severus I'm glad to be back...I went to this horrible world filled with sand."
        
    call screen room_of_requirement_menu