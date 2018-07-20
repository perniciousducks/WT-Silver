

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
        xpos 100
        ypos 180
        idle "images/room_of_requirement/mirror.png"
        hover "images/room_of_requirement/mirror.png"
        action [Hide("room_of_requirement_menu"), Jump("mirror_menu")]
    
    imagebutton: # DOOR
        xpos 758+140
        ypos 315
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/main_room/door.png"
        hover "images/main_room/door_hover.png"
        action [Hide("room_of_requirement_menu"), Jump("leave_room_req")]
        
    imagebutton: # Cadle Fire left
        xpos 350
        ypos 200
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/main_room/candle.png"
        hover "images/main_room/candle.png"
        action [Hide("room_of_requirement_menu"), Jump("turn_on_cadle_2")]
        
    imagebutton: # Cadle Fire Right
        xpos 700
        ypos 200
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "images/main_room/candle.png"
        hover "images/main_room/candle.png"
        action [Hide("room_of_requirement_menu"), Jump("turn_on_cadle_1")]
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
    
label mirror_menu:
    $ currentpage = 0
    show screen event_menu
    $ _return = ui.interact()
    
    hide screen event_menu
    
    if _return == "Cancel":
        call screen room_of_requirement_menu
        
    elif _return == "Info":
        call screen info_screen
    
    else:
        $renpy.jump(_return)

screen info_screen:
    imagebutton: # X
        xpos 1013
        ypos 13
        idle "interface/map/close_ground.png"
        hover "interface/map/close_hover.png"
        action [Hide("info_screen"), Jump("mirror_menu")]
        
    add "interface/frames/"+interface_color+"/PinkBox.png" xalign 0.5 yalign 0.5 zoom 3
    vbox:
        xalign 0.5
        yalign 0.5
        xsize 300
        ysize 300
        
        text "The mirror of Erised contains a collection of side stories. Ones that would either not fit in the main game or over the top parodies dreamt up by the genie. \n\nThe stories can be unlocked by completing the task listed in the description of each entry. Make sure to look at the story theme to see what you want to go for first." xalign 0.5 yalign 0.5
        
screen event_menu:
    imagebutton: # X
        xpos 1013
        ypos 13
        idle "interface/map/close_ground.png"
        hover "interface/map/close_hover.png"
        action Return("Cancel")
        
    imagebutton:
        xpos 960
        ypos 530
        idle "interface/info.png"
        hover "interface/info_hover.png"
        action Return("Info")
    
           
    frame:
        background #00000000
        xsize 638
        ysize 544
        xalign 0.5
        yalign 0.5
        
        add "interface/room_of_req/mirror_event_menu.png"
        
        hbox:
            xpos 11
            ypos 30
            xsize 419
            ysize 41
            text "The PornMaker" xalign 0.5 yalign 0.5 size 16 bold 0.2
        
        
        vbox:
            xpos 12
            ypos 86
            xsize 598
            ysize 448
        
            for i in range(0, 5):
                if (currentpage*5)+i > len(mr_evs_list):
                    add "interface/room_of_req/mirror_event_item.png"
                else:
                    use mirror_item(mr_evs_list[currentpage*5])
            
screen mirror_item(mirror_story):
    frame:
        background #00000000
        xpos -6
        ypos -7
        xsize 601
        ysize 90
        
        if mirror_story.unlocked:
            imagebutton:
                idle "interface/room_of_req/mirror_event_item.png"
                hover "interface/room_of_req/mirror_event_item.png"
                action Return(mirror_story.start_label)
        else:
            add "interface/room_of_req/mirror_event_item.png"
        
        vbox:
            xpos 0
            ypos 1
            xsize 82
            ysize 81
            
            add "interface/room_of_req/locked.png" xalign 0.5 yalign 0.5 zoom 0.8
        
        vbox:
            xpos 94
            ypos 3
            xsize 500
            ysize 22
            
            text mirror_story.getMenuText() yalign 0.5
            
        vbox:
            xpos 94
            ypos 30
            xsize 500
            ysize 55
            
            text mirror_story.getDescription()   
            
screen candle_light_1:
    add "candle_fire_01" xpos 590 ypos 85
    
screen candle_light_2:
    add "candle_fire_02" xpos 240 ypos 85
    
screen room_of_req_door:
    add "images/room_of_requirement/front_door.png" at fade_in(200, 160, 1)
    zorder -1

screen floor_7th_screen:
    add "images/room_of_requirement/corridor.png"
    #add "images/room_of_requirement/picture_frame.png" xpos 800 ypos 140 zoom 0.60
    #add "flower_animation" xpos 830 ypos 160 zoom 0.60
    add "images/main_room/candle.png" xpos 0 ypos 95
    add "candle_fire_02" xpos 0 ypos 95
    add "images/main_room/candle.png" xpos 300 ypos 95
    add "candle_fire_01" xpos 300 ypos 95
    add "images/main_room/candle.png" xpos 600 ypos 95
    add "candle_fire_02" xpos 600 ypos 95
    add "images/main_room/candle.png" xpos 900 ypos 95
    add "candle_fire_01" xpos 900 ypos 95
    
    #TODO: Add some light
    zorder -1
    
#animation of flower for painting maybe?    
image flower_animation:
    "images/animation/Bouquet4.png"
    pause 30
    "images/animation/BouquetPaf.png"
    pause .2
    "images/animation/Flower1.png"
    pause .2
    "images/animation/Flower2.png"
    pause .2
    "images/animation/Flower3.png"
    pause .2
    "images/animation/Flower4.png"
    pause 30
    "images/animation/FlowerPaf.png"
    pause .2
    "images/animation/Bouquet1.png"
    pause .2
    "images/animation/Bouquet1.png"
    pause .2
    "images/animation/Bouquet2.png"
    pause .2
    "images/animation/Bouquet3.png"
    pause .2
    "images/animation/Bouquet4.png"
    repeat
    

screen floor_7th_door:
    add "images/room_of_requirement/front_door.png" xpos 200 ypos 160
    zorder -1
    
screen floor_7th_menu:
    imagebutton:
        xpos 200
        ypos 160
        idle "images/room_of_requirement/front_door.png"
        hover "images/room_of_requirement/front_door.png"
        action [Jump("enter_room_of_req")]
    zorder -1
    
label enter_room_of_req:
    call blkfade 
    show screen room_of_requirement
    hide screen floor_7th_door
    hide screen room_of_req_door
    hide screen floor_7th_screen
    hide screen floor_7th_menu
    
    
    if first_visit_req == False:
        call gen_chibi(action = "", xpos = "door", ypos = "base", flip=True)
        call hide_blkfade
        $ first_visit_req = True
        m"It's just an empty room....with a mirror?"
        call gen_walk(pos1="door", pos2="200")
        m"...."
        vQ"So you've found the mirror of Erised"
        m"cough I mean...yes Severus, it is I... \"Dumbledore\""
        call sna_chibi(xpos="door")
        call gen_chibi(action = "", xpos = "200", ypos = "base")
        m "I'm so glad to be back..."
        call sna_main(".....","snape_05") 
        m "Worth a shot..."
        call sna_main("I'm quite certain I told you to stay in your office... For how long have you been roaming the school grounds?", "snape_06")
        m "This is the first time... hence why I was so lost."
        call sna_main(".....","snape_05")
        m "Only for the past week or so..."
        call sna_main(".....","snape_07")
        m "Yeah pretty much since the moment I got here."
        call sna_main("*Sigh* Well, you've not been caught so I suppose it's okay as long as you don't make any weird requests or comments to other staff members.","snape_06")
        m "...."
        call sna_main(".....","snape_03") 
        m "I might have ordered a few oddities from Madam Mafkin..."
        call sna_main("Hahahah...That old hag?","snape_28")
        call sna_main("She's nuts, she can sow that's for damn sure but she'd never know nor care...do whatever you want with her. ", "snape_01")
        m "\"I'd rather not...\""
        call sna_main("Now, continuing where I left off. This mirror that you've found...", "snape_09")
        call sna_main("I thought Albus would've moved it out of the school after the last incident...", "snape_22")
        call gen_chibi(action = "", xpos = "200", ypos = "base", flip=True)
        m "What kind of incident? It's just some dusty old mirror... why would Dumbledore care about it? And what's going on with this room?"
        call sna_main("I don't know about the room, I'm more concerned by this mirror. Why don't you have a look in it and tell me what you see?", "snape_06")
        m "*Squints* Just seems like an old mirror to me, a bit dusty and cloudy thou...hold on a minute."
        call sna_main(".....", "snape_23")
        m "... I see myself...I've won the house cup."
        call sna_main("Really?", "snape_05")
        m "No, I can see myself in Agrabah. I'm surrounded by a harem of women all dedicated to pleasing me."
        call sna_main("You really are nothing more than a sexual deviant are you?", "snape_02")
        m "Pretty much."
        call sna_main("The mirror is known as the mirror of Erised, or Desire backwards...", "snape_09")
        g9 "Very clever..."
        call sna_main("Quite...in short, it's designed to show you your deepest desire... but by your comment I'm sure you already got that.", "snape_05")
        m "Your magic might be foreign to me but this seems like nothing more than a party trick, I already know what I desire. "
        call sna_main("Well, it would be quite dull... if you didn't include the changes I made that had it locked up in the first place.", "snape_20")
        m "I could probably make a good guess already but please, do tell..."
        call sna_main("Well... the original intentions are quite boring so I expanded the enchantment and it turned out to be incredibly difficult but clever that I am...", "snape_23")
        m "Getting bored!"
        call sna_main("It's a porn creator..", "snape_03")
        g5 "A what, sorry?"
        call sna_main("A porn creator. Well, technically it's used to let you live out your fantasies, be they impure or not. So not necessarily porn.", "snape_01")
        g5 "And you didn't tell me a thing like this existed?"
        call sna_main("Well, it didn't exist until I made it...and I thought it was moved or destroyed.", "snape_26")
        g4 "Get out."
        call sna_main("What?", "snape_05")
        g9 "I said get out, I found it so I get to keep it."
        call sna_main("But, I thought maybe I could move...", "snape_06")
        g4 "It's staying right where it is, I've been getting incredibly bored lately and might consider roaming the school a bit more...actually, I feel the urge to take a trip to the girls dormitory right now."
        call sna_main("Fine, it stays. Please don't... just remember that it will take time for it to reshape and create imagery so check back every now and then.", "snape_06")
        m "Noted... Out. Now."
        
        hide screen snape_main
        hide screen snape_head
        hide screen bld1
        call give_reward("You've unlocked the room of requirement", "images/store/06.png") 
        call sna_chibi(action="hide")
        call gen_chibi(action = "", xpos = "200", ypos = "base", flip=True)
        
    call gen_chibi(action = "", xpos = "200", ypos = "base", flip=True)
    call hide_blkfade    
    call screen room_of_requirement_menu
    