label open_stat_menu(charName="hermione"):
    $stat_screen = ""
    $stat_char = ""
    if charName == "hermione":
        $ hermione_xpos=540
        call updateHermioneWords 
        call update_her_uniform 
        $stat_char = "hermione_main"
        $stat_screen = "hermione_stat_menu"
    
    elif charName == "luna":
        $ luna_xpos=540
        $stat_char = "luna_main"
        $stat_screen = "luna_stat_menu"
    else:
        $stat_screen = "not_implemented"

    if stat_char != "":
        $ renpy.show_screen(stat_char)
    if stat_screen != "":
        $ renpy.show_screen(stat_screen)

    show screen select_character
    $ _return = ui.interact()
    
    if _return == "Close":
        $renpy.hide_screen(stat_screen)
        $renpy.hide_screen(stat_char)
        hide screen select_character
        jump day_main_menu
    elif _return == "color":
        call open_stat_menu(charName) 
    else:
        $renpy.hide_screen(stat_screen)
        $renpy.hide_screen(stat_char)
        call open_stat_menu(_return)
     
screen select_character:
    zorder 4
    #Wardrobe Color
    $ wr_background_color = []

    $ wr_background_color.append("base")
    $ wr_background_color.append("red")
    $ wr_background_color.append("green")
    $ wr_background_color.append("blue")
    
    $ indexSize = 0 # just update this after each button and copy the code bellow and the button will automaticlig find the correct position in the index. The icon image need to be 200*210 pixel
    add "interface/stat_select/"+str(interface_color)+"/ground_stat_screen_"+str(wardrobe_color)+".png"
    text "-Character Select-" xpos 40 ypos 100 size 14 
    
    use close_button
    
    imagebutton:
        xpos 40 + ( 85 * (indexSize%2))
        ypos 140 + ( 90 * ((indexSize/2) - ((indexSize / 2)% 1)))
        idle Transform("interface/stat_select/CharacterIcon/HermioneIcon.png", zoom=.40) 
        hover Transform("interface/stat_select/CharacterIcon/HermioneIcon_Hover.png", zoom=.40) 
        action Return("hermione")
    $ indexSize += 1 
    
    if luna_unlocked == True:
        imagebutton:
            xpos 40 + ( 85 * (indexSize%2))
            ypos 140 + ( 90 * ((indexSize/2) - ((indexSize / 2)% 1)))
            idle Transform("interface/stat_select/CharacterIcon/LunaIcon.png", zoom=.40) 
            hover Transform("interface/stat_select/CharacterIcon/LunaIcon_Hover.png", zoom=.40) 
            action Return("luna")
        $ indexSize += 1 
        
    #Wardrobe background color
    for i in range(0,len(wr_background_color)):
        imagebutton:
            xpos 667+(20*i)
            ypos 559
            idle "interface/wardrobe/icons/colors/"+wr_background_color[i]+".png"
            action [SetVariable("wardrobe_color",wr_background_color[i]), Return("color")]
  
screen not_implemented:
    side "c r":
        area (247, 137, 385, 400)

        viewport id "vp":
            draggable True
            mousewheel True
            
            frame:
                background #00000000
                text "This Character is not implemented" xalign 0.5 yalign 0.5 size 16 bold 0.2

        vbar value YScrollValue("vp")
    
    zorder 8        
        
#steps is how many bars should be fill where 10 is max
screen stat_bar(steps, top_text, buttom_text, top_padding = 20):
    $stateFullImage = "interface/stat_select/"+str(interface_color)+"/StatBar_Full.png"
    $stateEmptyImage = "interface/stat_select/"+str(interface_color)+"/StatBar_Empty.png"
    
    #Just some padding
    frame:
        background #00000000
        ysize top_padding
        
    text top_text xalign 0.5 size 30 bold 0.2
    frame:
        background #00000000
        xalign 0.5
        ysize 30
        xsize 360
        add LiveCrop((0, 0, steps*36, 600), stateFullImage)
        add stateEmptyImage
    text "-"+buttom_text+"-" xalign 0.5 size 20 
    
screen text_stat(startText, endText, amount, top_padding = 20):
    #Just some padding
    frame:
        background #00000000
        ysize top_padding
    
    text (startText + str(amount) + endText) size 20 
    
screen charecter_name(name):
    frame:
        background #00000000
        xpos 700
        ypos 60
        ysize 30
        xsize 230
        
        text name xalign 0.5 yalign 0.5 size 20  
        
screen hermione_stat_menu: 
    
    use charecter_name("Hermione")
        
    side "c r":
        area (220, 107, 425, 480)

        viewport id "vp":
            draggable True
            mousewheel True
            
            vbox:
                use stat_bar(int(whoring/2.4), "-Whoring-", "-"+whoringWord+"-")
                
                use stat_bar(madValue, "-Mood-", "-"+moodWord+"-")
               
                use stat_bar(int(whoring/2.4), "-Reputation-", "-"+reputationWord+"-")
               
                use stat_bar(int((v_tutoring/max_tutoring)*10), "-Tutoring-" ,"-"+tutoringWord+"-")
                
                use text_stat("Hermione has given ", " Handjobs", hg_pf_TouchMe_OBJ.points)
                
                use text_stat("Hermione has given ", " Blowjobs", hg_pf_SuckIt_OBJ.points)
                
                use text_stat("Hermione has given ", " Tit jobs", hg_pf_TitJob_OBJ.points)
                
                use text_stat("Hermione and you have had sex ", " times", hg_pf_LetsHaveSex_OBJ.points)
                
                use text_stat("Hermione and you have had anal sex ", " times", hg_pf_TimeForAnal_OBJ.points)
              
        vbar value YScrollValue("vp")
    
    zorder 8

screen luna_stat_menu:
    $stateFullImage = "interface/stat_select/"+str(interface_color)+"/StatBar_Full.png"
    $stateEmptyImage = "interface/stat_select/"+str(interface_color)+"/StatBar_Empty.png"
    
    use charecter_name("Luna")
        
    text "-Corruption-" xalign 0.375 ypos 50+ 68 size 30 bold 0.2
    text "-Dom points-" xalign 0.375 ypos 225+ 68 size 30 bold 0.2
    text "-Sub points-" xalign 0.375 ypos 400+ 68 size 30 bold 0.2

    text "-"+str(luna_corruption)+"-" xalign 0.39 ypos 50+130 size 20 
    text "-"+str(luna_dom)+"-" xalign 0.39 ypos 225+130 size 20
    text "-"+str(luna_sub)+"-" xalign 0.39 ypos 400+130 size 20 
        
    #When the max amount of the diffrent stats add the full bare with crop
    add stateEmptyImage xpos 250 ypos 150
    add stateEmptyImage xpos 250 ypos 325
    add stateEmptyImage xpos 250 ypos 500    
    zorder 8
    
screen close_button(offsetx = 0, offsety = 0, close_var=lambda : "Close"):
    imagebutton:
            xpos 1028-offsetx
            ypos 11-offsety
            idle "interface/general/"+interface_color+"/button_close.png"
            hover "interface/general/"+interface_color+"/button_close_hover.png"
            action Return(close_var())

label updateHermioneWords:
    $ whoringWords = ["Pure", "Naive", "Curious", "Naughty", "Perverse", "Immoral", "Slutty", "Shameless", "Cumslut", "Total Cumslut", "Shameless Cumslut"] 
    $ madWords = ["Happy", "Slightly upset", "annoyed", "upset", "very upset", "mad", "angry", "hateful", "despises you", "Furious", "Absolutely Furious"] 
    $ whoreWords = ["Teacher's pet", "School star", "good girl", "minx", "slutty schoolgirl", "easy lay", "whore", "slut for sex", "gryffindor whore", "school cumdump", "mudblood cumdump"] 
    $ slutWords = ["Teacher's pet", "School star", "good girl", "principal's pet", "slutty schoolgirl", "slut", "principal's slut", "daddy's girl", "gryffindor slut", "Dumbledore's whore", "Dumbledore's cumdump"]
    $ tutoringWords = ["pure ", "naive", "tempted", "curious", "tainted", "eager", "sinful", "perverted", "corrupted", "depraved", "shattered"]
    $ tutoringWord = tutoringWords[(v_tutoring/max_tutoring)*10]
    $ whoringWord = whoringWords[int(whoring/2.4)]

    if mad > 9:
        $ moodWord = "Blind rage"
        $ madValue = 10
    elif mad < 0:
        $ madValue = 0
        $ moodWord = madWords[madValue]
    else:
        $ moodWord = madWords[mad]
        $ madValue = mad

    if lock_public_favors:
        $ reputationWord = slutWords[int(whoring/2.4)]
    else:
        $ reputationWord = whoreWords[int(whoring/2.4)]

    return
