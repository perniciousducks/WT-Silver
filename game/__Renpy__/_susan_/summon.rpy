


label summon_susan:

    call load_susan_clothing_saves from _call_load_susan_clothing_saves_1

    call play_sound("door") from _call_play_sound_186 #Sound of a door opening.

    ### RANDOM CLOTHING EVENTS ###
    #call susan_door_event

    call update_sus_uniform from _call_update_sus_uniform_20

    #call sus_chibi("stand","mid","base")

    if one_of_ten < 4:
        if daytime:
            call sus_main("Good day, [genie_name].","base","base","base","mid",xpos="base",ypos="base") from _call_sus_main_136
        else:
            call sus_main("Good evening, [genie_name].","base","base","base","mid",xpos="base",ypos="base") from _call_sus_main_137
    elif one_of_ten < 7:  
        call sus_main("How can I help you, [genie_name]?","base","base","worried","R",xpos="base",ypos="base") from _call_sus_main_138
    else:
        call sus_main("You wanted to see me, [genie_name]?","base","base","worried","down",xpos="base",ypos="base") from _call_sus_main_139

    label susan_requests:

    $ menu_y = 0.5 #Menu is moved to the middle. #Don't add xpos!

    $ wardrobe_active = False

    menu:
        "-Talk-":
            if not chitchated_with_susan: 
                call susan_chit_chat from _call_susan_chit_chat 
                jump susan_talk
            else:
                jump susan_talk 
                
        "-Inventory-" if susan_wardrobe_unlocked and susan_imperio_influence:
            $ active_girl = "susan"

            call load_susan_clothing_saves from _call_load_susan_clothing_saves_2

            call reset_wardrobe_vars from _call_reset_wardrobe_vars_2
            call update_wr_color_list from _call_update_wr_color_list_3

            $ wardrobe_active = 1 #True
            call sus_main(xpos="wardrobe",ypos="base") from _call_sus_main_140
            call screen wardrobe
        "{color=#858585}-Inventory-{/color}" if susan_wardrobe_unlocked and not susan_imperio_influence:
            call nar(">Susan isn't willing to let you change her Wardrobe!") from _call_nar_566
            jump susan_requests
        "{color=#858585}-Hidden-{/color}" if not susan_wardrobe_unlocked:
            call nar(">You haven't unlocked this feature yet.") from _call_nar_567
            jump susan_requests
            
        "-Dismiss her-":
            if daytime:
                call sus_main("I will go back to classes then, [sus_genie_name].","base","base","base","down") from _call_sus_main_141
            else:
                call sus_main("Uhm... good night then, [sus_genie_name].","base","base","base","down") from _call_sus_main_142

            hide screen susan_main
            #hide screen susan_blink #Susan chibi.

            $ menu_x = 0.5 #Menu position is back to default. (Center).
            $ menu_y = 0.5 #Menu position is back to default. (Center).
                    
            $ susan_busy = True  
            
            if daytime:
                jump day_main_menu
            else:
                jump night_main_menu
                    
                    
label susan_talk: 
    menu: 
        #"--":
        "-Address me only as-":
            menu:
                "-Sir-":
                    $ sus_genie_name = "Sir"
                    call sus_main("Very well, [sus_genie_name].","base","base","base","mid") from _call_sus_main_143
                    jump susan_talk
                "-Dumbledore-":
                    $ sus_genie_name = "Dumbledore"
                    call sus_main("Ok, [sus_genie_name].","base","base","worried","down") from _call_sus_main_144
                    jump susan_talk
                "-Professor-":
                    $ sus_genie_name = "Professor"
                    call sus_main("Of course, [sus_genie_name].","base","base","base","R") from _call_sus_main_145
                    jump susan_talk
                "-Old man-":
                    $ sus_genie_name = "Old man"
                    call sus_main("That wouldn't be very polite, Professor.","open","closed","base","mid") from _call_sus_main_146
                    m "Don't worry, [susan_name]. I always tell my students to call me silly names."
                    g9 "It helps bonding with them!"
                    call sus_main("If you say so,... Uhm-- [sus_genie_name].","base","base","base","mid") from _call_sus_main_147
                    g4 "And soon I'm going to bond with your tits!"
                    jump susan_talk
                "-Genie-":
                    $ sus_genie_name = "Genie"
                    call sus_main("I uhm--","upset","base","base","L") from _call_sus_main_148
                    call sus_main("Do all the people call you that?","upset","narrow","worried","mid") from _call_sus_main_149
                    m "Yes-yes--, everybody!"
                    m "It's perfectly normal!"
                    call sus_main("(...)","upset","base","worried","down") from _call_sus_main_150
                    call sus_main("O-ok then,... [sus_genie_name].","base","base","worried","R") from _call_sus_main_151
                    jump susan_talk
                "-Lord Voldemort-":
                    $ sus_genie_name = "Lord Voldemort"
                    call sus_main("Why would you want me to call you that?","open","closed","worried","mid") from _call_sus_main_152
                    call sus_main("We aren't supposed to mention his name!","open","narrow","worried","down") from _call_sus_main_153
                    m "It's only a name girl..."
                    call sus_main("It's the name of, you-know-who!","upset","closed","worried","mid") from _call_sus_main_154
                    call sus_main("That name really creeps me out, Professor!","open","closed","worried","mid") from _call_sus_main_155
                    m "I don't want my students to be scared of a name, Susan! It's practice."
                    m "Come on... say it."
                    call sus_main("Ok...","open","narrow","worried","down") from _call_sus_main_156
                    call sus_main("V-Voldemort--...","upset","closed","worried","mid") from _call_sus_main_157
                    jump susan_talk
                "-Daddy-":
                    $ sus_genie_name = "Daddy"
                    call sus_main("Sir, no!","scream","closed","worried","mid") from _call_sus_main_158
                    call sus_main("I can't possibly call you that!","scream","wide","angry","wide") from _call_sus_main_159
                    m "But I want you to."
                    g9 "There's no harm in calling me Daddy."
                    call sus_main("But that's!--","open","narrow","angry","mid") from _call_sus_main_160
                    call sus_main("(This is wrong, Susan!)","upset","narrow","worried","down") from _call_sus_main_161
                    call sus_main("Alright,... Professor-- Eeeeh--... D-Daddy.","base","closed","worried","mid") from _call_sus_main_162
                    jump susan_talk
                "-Master-":
                    $ sus_genie_name = "Master"
                    call sus_main("M-Master?","upset","narrow","base","mid") from _call_sus_main_163
                    call sus_main("I don't think I should call my teachers that.","open","closed","worried","mid") from _call_sus_main_164
                    m "No-no--, that's what you call your teachers nowadays!"
                    m "But only call me that!"
                    call sus_main("Uhm--... very well, [sus_genie_name].","upset","narrow","worried","R") from _call_sus_main_165
                    jump susan_talk
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ sus_genie_name = "Sir"
                        call sus_main("I will just call you [sus_genie_name] again.","base","base","base","mid") from _call_sus_main_166
                    else:
                        $ sus_genie_name = temp_name
                        call sus_main("Uhm... ok. I will call you [sus_genie_name].","upset","narrow","base","L") from _call_sus_main_167
                    jump susan_talk
                "-Never mind-":
                    jump susan_requests
                
             
        "-From now on I will refer to you as-":
            menu:
                "-Miss Bones-":
                    $ susan_name = "Miss Bones"
                    call sus_main("Of course, [sus_genie_name].","base","base","base","mid") from _call_sus_main_168
                    jump susan_talk
                "-Girl-":
                    $ susan_name = "Girl"
                    call sus_main("I'm ok with that, [sus_genie_name].","base","base","worried","R") from _call_sus_main_169
                    jump susan_talk
                "-Cow-":
                    $ susan_name = "Cow"
                    call sus_main("Why would you want to call me that, [sus_genie_name]?","upset","narrow","worried","down") from _call_sus_main_170
                    call sus_main("The other girls already call me that and I hate it...","open","base","worried","down") from _call_sus_main_171
                    m "You poor poor thing!"
                    m "You see, if someone like me would call you that, maybe it wouldn't affect you as much."
                    call sus_main("I--... You might be right.","upset","narrow","base","down") from _call_sus_main_172
                    call sus_main("You can call me a Cow, [sus_genie_name].","base","base","base","mid") from _call_sus_main_173
                    jump susan_talk
                "-Slut-":
                    $ susan_name = "Slut"
                    call sus_main("[sus_genie_name]!","scream","closed","angry","R") from _call_sus_main_174
                    call sus_main("You can't be serious!","scream","wide","base","wide") from _call_sus_main_175
                    m "Why not. Nobody has to know..."
                    call sus_main("How could you even think of me like that!","open","base","worried","down") from _call_sus_main_176
                    call sus_main("I'm not a... slut.","upset","narrow","worried","R") from _call_sus_main_177
                    m "Of course not. This is just to strengthen your self-esteem."
                    m "Trust me, I know what I'm doing."
                    m "Being called a slut always boosts a girls confidence!"
                    call sus_main("R-really?","open","base","base","mid") from _call_sus_main_178
                    m "Yes. Now... shall we try it?"
                    call sus_main("... alright, [sus_genie_name]...","upset","narrow","worried","R") from _call_sus_main_179
                    jump susan_talk
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ susan_name = "Miss Bones"
                    else:
                        $ susan_name = temp_name
                        call sus_main("I don't like it, but--","open","closed","worried","mid") from _call_sus_main_180
                        call sus_main("Promise you'll only call me that when we are alone.","upset","base","worried","mid") from _call_sus_main_181
                        g9 "Promised!"
                    jump susan_talk
                "-Never mind-":
                    jump susan_talk

                    
        "-Never mind":
            jump susan_requests