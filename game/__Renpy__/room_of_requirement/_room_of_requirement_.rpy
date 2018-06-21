

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
        action [Hide("room_of_rquirement_menu"), Jump("leave_room_req")]
        
    imagebutton: # Cadle Fire left
        xpos 350
        ypos 200
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/main_room/candle.png"
        hover "images/main_room/candle.png"
        action [Hide("room_of_rquirement_menu"), Jump("turn_on_cadle_2")]
        
    imagebutton: # Cadle Fire Right
        xpos 700
        ypos 200
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/main_room/candle.png"
        hover "images/main_room/candle.png"
        action [Hide("room_of_rquirement_menu"), Jump("turn_on_cadle_1")]
    zorder -1

label turn_on_cadle_1:  
    if renpy.get_screen("candle_light_1") == None:
        show screen candle_light_1
    else:
        hide screen candle_light_1
    call screen room_of_requirement_menu
        
label turn_on_cadle_2:   
    if renpy.get_screen("candle_light_2") == None:
        show screen candle_light_2
    else:
        hide screen candle_light_2
    call screen room_of_requirement_menu
    
label leave_room_req: 
    hide screen room_of_requirement
    hide screen candle_light_1
    hide screen candle_light_2
    jump return_office
    
screen candle_light_1:
    add "candle_fire_01" xpos 590 ypos 85
    
screen candle_light_2:
    add "candle_fire_01" xpos 240 ypos 85
    
screen room_of_req_door:
    add "images/room_of_requirement/front_door.png" at fade_in(450, 150, 1)

screen floor_7th_screen:
    add "images/room_of_requirement/corridor.png"
    if unlocked_7th and not first_time_7th:
        add "images/room_of_requirement/front_door.png" at fade_in(450, 150, 1)
    #TODO: Add some light
    zorder -1

screen floor_7th_menu:
    imagebutton:
        xpos 450
        ypos 150
        idle "images/room_of_requirement/front_door.png"
        hover "images/room_of_requirement/front_door.png"
        action [Jump("enter_room_of_req")]
    
label enter_room_of_req:
    call blkfade 
    show screen room_of_requirement
    hide screen floor_7th_screen
    hide screen floor_7th_menu
    
    
    if first_visit_req == False:
        call gen_chibi(action = "", xpos = "door", ypos = "base", flip=True)
        call hide_blkfade
        $ first_visit_req = True
        m"It's just an empty room....with a mirror?"
        call gen_walk(pos1="door", pos2="200")
        m"...."
        "So you've found the mirror of Erised"
        call sna_chibi(xpos="door")
        call gen_chibi(action = "", xpos = "200", ypos = "base")
        m "Snape!... cough I mean, Severus I'm glad to be back...I went to this horrible world filled with sand."
        sna "....."
        m "Worth a shot..."
        sna "I'm quite certain I told you to stay in your office...
For how long have you been roaming the school grounds?"
        m "This is the first time... hence why I was so lost."
        sna "...."
        m "Only for the past week or so..."
        sna "...."
        m "Yeah pretty much since the moment I got here."
        sna "*Sigh* Well, you've not been caught so I suppose it's okay as long as you don't make any weird requests or comments to other staff members."
        m "...."
        sna "...."
        m "I might have ordered a few oddities from Madam Mafkin..."
        #TODO: snape laugh face
        sna "Hahahah...That old hag?"
        # TODO: now serius
        sna "She's nuts, she can sow that's for damn sure but she'd never know nor care...do whatever you want with her. "
        m "\"I'd rather not...\""
        sna "Now, continuing where I left off. This mirror that you've found..."
        #TODO: snape smirkface
        sna "I thought Albus would've moved it out of the school after the last incident... "
        m "What kind of incident? It's just some dusty old mirror... why would Dumbledore care about it? And what's going on with this room?"
        sna "I don't know about the room, I'm more concerned by this mirror. Why don't you have a look in it and tell me what you see?"
        m "*Squints* Just seems like an old mirror to me, a bit dusty and cloudy thou...hold on a minute."
        #TODO: snape smirks
        sna "...."
        m "... I see myself...I've won the house cup."
        sna "Really?"
        m "No, I can see myself in Agrabah. I'm surrounded by a harem of women all dedicated to pleasing me."
        sna "You really are nothing more than a sexual deviant are you? "
        m "Pretty much."
        sna "The mirror is known as the mirror of Erised, or Desire backwards..."
        g9 "Very clever..."
        sna "Quite...in short, it's designed to show you your deepest desire... but by your comment I'm sure you already got that."
        m "Your magic might be foreign to me but this seems like nothing more than party trick, I already know what I desire. "
        sna "Well, it would be quite dull... if you didn't include the changes I made that had it locked up in the first place."
        m "I could probably make a good guess already but please, do tell..."
        sna "Well... the original intentions are quite boring so I expanded the enchantment and it turned out to be incredibly difficult but clever that I am..."
        m "Getting bored!"
        sna "It's a porn creator.."
        m "A what, sorry?"
        sna "A porn creator. Well, technically it's used to let you live out your fantasies, be they impure or not. So not necessarily porn."
        g5 "And you didn't tell me a thing like this existed?"
        sna "Well, it didn't exist until I made it...and I thought it was moved or destroyed."
        m "Get out."
        sna "What?"
        m "I said get out, I found it so I get to keep it."
        sna "But, I thought maybe I could move..."
        m "It's staying right where it is, I've been getting incredibly bored lately and might consider roaming the school a bit more...actually, I feel the urge to take a trip to the girls dormitory right now."
        sna "Fine, it stays. Please don't... just remember that it will take time for it to reshape and create imagery so check back every now and then."
        m "Noted... Out. Now."
        call give_reward("You've unlocked the room of requirements", "images/store/06.png") 
        call sna_chibi(action="hide")
        call gen_chibi(action = "", xpos = "200", ypos = "base", flip=True)
        
    call gen_chibi(action = "", xpos = "200", ypos = "base", flip=True)
    call hide_blkfade    
    call screen room_of_requirement_menu
    