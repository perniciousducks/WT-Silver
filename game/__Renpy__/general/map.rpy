

### Map Screen ###

screen map_screen:
    zorder hermione_main_zorder-1
    
    imagemap:
        ground "interface/map/map_ground.png"
        idle "interface/map/map_idle.png"
        hover "interface/map/map_hover.png"
        # (X upper-left corner, Y upper-left corner, width, height).
        hotspot (192+140, 229, 38, 20) clicked Jump("map_attic") #attic
        hotspot (272+140, 373, 63, 41) clicked Jump("clothes_store") #clothes
        hotspot (25+140, 374, 102, 66) clicked Jump("map_forest") #forest
        hotspot (302+140, 523, 112, 49) clicked Jump("map_lake") #lake
        hotspot (273+140, 459, 75, 8) clicked Jump("map_dorms") #dorms
        #hotspot (656+140, 232, 106, 33) clicked Jump("inn_menu") #inn
        #hotspot (376+140, 84, 111, 57) clicked Jump("map_pitch") #pitch
        hotspot (307+140, 240, 59, 37) clicked Jump("shop_intro") #shop
        hotspot (33+140, 535, 39, 39) clicked Jump("day_main_menu") #return
        

label map_attic: #Label controlling what happens when you access the attic
    if not attic_open:
        ">You venture up to the attic but find that the door is locked."
        m "Damn, it's locked."
        m "Guess I'll have to ask Snape about a key."
        jump return_office
    if attic_open and tentacle_owned:
        ">You venture up to the attic and find an angry tentacle plant."
        m "Better get out of here before the plant remembers that I'm the one that cut it."
        ">You quickly return to your office."
        jump return_office
    else: #Scene where genie has to take a sample of the devil's snare plant
        ">You find your way through the winding staircases to the attic door."
        m "Hmmmmm, it seems to be open."
        ">You walk through the dusty room, light softly cascading though the windows."
        m "Well where's this magical plant?"
        ">A slender piece of vine is visible, skirting the room, as if to avoid the light."
        m "This must be it."
        ">You cut a piece and leave."
        ">As you shut the door you hear the room erupt in a series of loud crashes."
        $ tentacle_owned = True
        jump return_office


label map_forest: #Label controlling what happens when you go to the forest
    if daytime:
        m "I really shouldn't be leaving the castle during the day. It's too risky..."
        jump day_main_menu
    else:
        pass
        
    call outskirts_of_hogwarts 
    
    m "Lets see what I can find out here..."
        
    menu:
        "-Search the area-":
            $ ran = renpy.random.random()
            if ran < 0.3:
                ">You search around the forest and manage to find an odd looking herb."
                m "This must be wormwood."
                menu: 
                    "-Take the wormwood-":
                        ">You gain 1 wormwood."
                        $ potion_inv.add("ing_wormwood")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            elif ran < 0.6:
                ">You search around the forest and manage to find an odd looking herb."
                m "This must be Knotgrass."
                menu: 
                    "-Take the Knotgrass-":
                        ">You gain 1 Knotgrass."
                        $ potion_inv.add("ing_knotgrass")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            else:
                ">You search around the forest but find nothing of interest."
                jump return_office
   
label map_lake: #Label controlling what happens when you go to the lake
    if daytime:
        m "I really shouldn't be leaving the castle during the day. It's too risky..."
        jump day_main_menu
    else:
        pass
    call outskirts_of_hogwarts 
    
    m "Lets see what I can find out here..." 
    
    menu:
        "-Search the area-":
            $ ran = renpy.random.random()
            if ran < 0.3:
                ">You search around the lake and manage to find an slender, green vine."
                m "This must be Niffler's fancy."
                menu: 
                    "-Take the Niffler's fancy-":
                        ">You gain 1 Niffler's fancy."
                        $ potion_inv.add("ing_niffler_fancy")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            elif ran < 0.6:
                ">You search around the lake and manage to find an exposed root that looks similar to ginger."
                m "This must be Root of Aconite."
                menu: 
                    "-Take the Root of Aconite-":
                        ">You gain 1 Root of Aconite."
                        $ potion_inv.add("ing_aconite_root")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            else:
                ">You search around the lake but find nothing of interest."
                jump return_office  

label map_dorms: #Label controlling what happens when you go to the dorms
    menu:
        "-Search the area-":#Luna's Hair
            $ ran = renpy.random.random()
            if ran < 0.3:
                ">You search around the dorms and manage to find a clump for bright orange fur."
                m "This must belong to some sort of animal."
                menu: 
                    "-Take the Fur-":
                        ">You gain 1 Cat Fur."
                        $ potion_inv.add("ing_cat_hair")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            elif ran < 0.6:
                ">You search around the dorms and manage to find an comb with some hair in it."
                m "This must be someones hair."
                menu: 
                    "-Take the hair-":
                        ">You gain 1 Luna's Hair."
                        $ potion_inv.add("ing_luna_hair")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            else:
                ">You search around the dorms but find nothing of interest."
                jump return_office         
            
label map_pitch: #Label controlling what happens when you go to the quidditch pitch
    if pitch_open:
        hoo "Hello Professor Dumbledore, nice to see you out of your office today."
        hoo "What brings you down to the Quidditch pitch today?"
        m "Quidditch, what sort of name is that?" #put in low talking tone
        hoo "What was that?"
        m "Nothing, just commenting about the weather." #Maybe change this
        hoo "Well I'm glad that you're here. I wanted to have words with you about a problem that I'm having at the moment."
        m "What's wrong?"
        hoo "Attendance at quidditch matches has slowly been declining over the last couple of months."
        hoo "Students just don't seem to want to turn up to watch their teams play. It's affecting team morale."
        m "And how would you like to fix this?"
        hoo "Perhaps we could make attendance to the match mandatory."
        m "I don't think that that would work. If I did that you would just end up with a lot of disgruntled students booing your own team."
        m "If poor attendance is affecting morale I would hate to think what that would do to the players."
        hoo "Well then what do you suggest?"
        m "You need a way to attract and excite the crowd. To get the students here and to get them cheering."
        m "What you need is a cheerleading team."
        hoo "A what?"
        m "A team of girls to dance and cheer for their team. To get their fellow students brimming with enthusiasm."
        hoo "I'm not sure Sir, Hogwarts has always been a traditional school."
        hoo "Something like this goes in the face of that legacy."
        m "Well if you feel that way then I think you might just have to accept the declining number of students watching the game."
        hoo "Fine, but I'm not comfortable with a team of these \"\Cheerleaders\"\. At most I'd be comfortable with one girl dancing." #Maybe adjust this so that there is a team
        m "Well I think I have the perfect candidate. I'll send her over next practice session to try out."
        hoo "Okay, just make sure she's wearing something appropriate."
        $ pitch_first = False
        jump return_office
    else:
        ">You look around the open field but can't see any students or teachers"
        m "Mustn't be a practice day."
        jump return_office
            
label outskirts_of_hogwarts:
    call blkfade 
    hide screen genie
    show screen chair_left
    show screen desk
    call gen_chibi("stand","desk","base") 
    call hide_blkfade 
        
    call gen_walk("desk","leave",3) 
    call blkfade 
        
    stop music fadeout 1.0
    
    centered "{size=+7}{color=#cbcbcb}Outskirts of hogwarts{/color}{/size}"

    play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.
    
    show screen blkback # Hide room

    $ end_u_1_pic =  "images/yule_ball/171.png"
    show screen end_u_1
    pause.3
    call hide_blkfade 
    pause.8
    $ renpy.play('sounds/steps_grass.mp3') # SOUNDS OF STEPS IN THE GRASS.
    $ end_u_3_pic =  "images/yule_ball/172.png"
    show screen end_u_3
    with d7 
    
    return
    
label return_office:
    call blkfade 
    #">You return to your office."
    
    hide screen end_u_1
    hide screen end_u_3
    hide screen chair_left
    hide screen desk
    call gen_chibi("hide") 
    show screen genie
    hide screen blkback
    pause.5
    call hide_blkfade 
    
    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu
