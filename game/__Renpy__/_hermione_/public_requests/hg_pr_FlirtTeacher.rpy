

### Flirt With Teacher ###

##(Level 02) (15 pt.) (Flirt with teachers). (Available during daytime only).
label hg_pr_FlirtTeacher:
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.
    
    if hg_pr_FlirtTeacher_OBJ.points < 1:
        m "{size=-4}(Tell her to be flirtatious with her teachers today?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests

    call bld
    
    m "[hermione_name], I want you to be especially flirtatious with your teachers today."

    if whoring < 3 or hg_pr_FlirtClassmate_OBJ.points < 2:
        jump too_much
   
    #Intro
    if hg_pr_FlirtTeacher_OBJ.points == 0 and whoring < 9:
        call her_main("I will do my best, [genie_name]!","base","base",xpos="right",ypos="base")
        call her_main("I am glad you finally decided to act, [genie_name]!","open","base")
        m "Huh?"
        call her_main("You are finally ready to investigate the teachers who made a habit out of buying favours from the students, aren't you?","normal","frown") 
        call her_main("I am honoured to pose as bait in this noble endeavor.","open","closed")
        m "Ehm... Yeah, that's exactly what I'm doing."
        call her_main("Splendid! You can count on me, [genie_name]!","normal","frown")

    #Second time event.
    else:
        call her_main("I shall provide you with a detailed report later tonight, [genie_name].","normal","frown",xpos="right",ypos="base")
        m "I will be waiting..."
    
    her "Well, I'd better go now. Classes are about to start..."
    
    $ hg_pr_FlirtTeacher_OBJ.inProgress = True
    
    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.

    
label hg_pr_FlirtTeacher_complete:

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    call bld
    

    #First level.
    call her_main("Good evening, [genie_name].","base","base",xpos="right",ypos="base")
    m "[hermione_name]..."
    m "Did you complete your task?"
    her "I did as you asked [genie_name]..."

    menu:
        "\"Great. Here are your points.\"":
            pass
        "\"Give me the details.\"":
            hide screen hermione_main
            with d3
            m "Tell me how many teachers did you flirt with, [hermione_name]?"
            m "Give me the details."
            show screen blktone
            with d3
    
            #First level.
            if  whoring >= 3 and whoring < 6:

                #Event A
                if one_out_of_three == 1: ### Flitwick
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Well, I tried flirting with Professor Flitwick...","open","worriedL",xpos="right",ypos="base")
                    call her_main("But it didn't really work...","annoyed","frown")
                    call her_main("..............................","annoyed","angryL")
                    m "How exciting..."
                    m "Is this all you have for me today, [hermione_name]?"
                    call her_main("Y-yes...","open","worried")
                    her "But [genie_name], I know for a fact that professor Flitwick is \"dirty\"!"
                    her "Everyone knows that because of his height..."
                    call her_main("He sometimes... ehm...","soft","baseL")
                    call her_main("He likes to look up girl's skirts, [genie_name]!","annoyed","worriedL")
                    m "Don't we all?"
                    call her_main("What?","open","base")
                    m "I said, don't we all hate it and must be outraged by the a man like Professor Flick-flick."
                    call her_main("Er... It's \"Professor Flitwick\", [genie_name].","normal","frown")
                    m "Right. Putting him on my \"Naughty boys list\" as we speak."
                    call her_main("......................","annoyed","suspicious")
                    m "Well, I hate to admit it but you did a lousy job of today's favour, [hermione_name]."
                    call her_main("................................","annoyed","angryL")

                    menu:
                        "\"Here are your point's though.\"":
                            call her_main("Really?","angry","worried")
                            call her_main("Thank you so much [genie_name]!","smile","happyCl")
                        "\"No points for you!\"":

                            call her_main("But [genie_name], I did my best!","angry","worried")
                            call her_main("You are going back on your promise [genie_name]!","mad","worried",tears="soft")
                            m "......................."
                            stop music fadeout 1.0
                            call her_main("How unbecoming of a school headmaster!","scream","worriedCl")
                            m "You are dismissed, [hermione_name]."
                            call her_main("Tsk!","angry","angry",emote="01")
                            $ mad += 18
                            call music_block
                            
                            $ hg_pr_FlirtTeacher_OBJ.inProgress = False
                            jump could_not_flirt
                          
                #Event B 
                elif one_out_of_three == 2: ### Snape
                    call her_main("..................","soft","baseL",xpos="right",ypos="base")
                    her "............................"
                    m "[hermione_name]?"
                    call her_main("Yes, [genie_name]... I'm sorry... I just...","open","worried")
                    call her_main("............","soft","baseL")
                    m "Did you do what I asked you to do?"
                    call her_main("I tried, [genie_name]. I really did...","open","base")
                    m "Who did you try to flirt with?"
                    call her_main(".........","soft","baseL")
                    call her_main("Professor Snape, [genie_name].","annoyed","angryL")
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    m "Severus? Interesting..."
                    m "How did it go?"
                    call her_main("It was awful [genie_name]...","normal","frown")
                    her "I am sorry, but I really hate professor Snape, [genie_name]!"
                    m "I'm sure the feeling is mutual..."
                    m "Tell me what happened."
                    call her_main("Nothing happened, [genie_name]. He just laughed at me...","annoyed","frown")
                    call her_main("I may not have much feminine charm, but I tried to be nice...","annoyed","worriedL")
                    call her_main("And he just started laughing in my face!","scream","angryCl")
                    call her_main("...it is really scary to see professor Snape laugh...","angry","worriedCl",emote="05")
                    her "........"
                    her "I am awful at flirting, I am sorry [genie_name]..."
                    call her_main("But I know that professor Snape is \"dirty\"!","angry","angry")
                    her "If you were to send someone else to him the outcome would be different, I know it!"
                    m "Someone else?"
                    call her_main("Yes! Someone with more experience at this...","upset","wink")
                    her "Someone..."
                    her "Someone, uhm..."
                    m "Sluttier?"
                    call her_main("Yes, I suppose...","disgust","glance")
                    m "Don't you give up, [hermione_name]. We will make a slut err--"
                    m "I mean a woman out of you yet!"
                    call her_main("...................","annoyed","annoyed")

                    menu:
                        "\"Here are your points, [hermione_name].\"":
                            pass
                        "\"...But you get no points this time\"":
                            call her_main("But I did my best...","annoyed","angryL")
                            call her_main("And I feel so humiliated now...","angry","worriedCl",emote="05")
                            call her_main("But I understand and won't argue with your decision...","normal","worriedCl")
                            call music_block
                            
                            $ hg_pr_FlirtTeacher_OBJ.inProgress = False
                            jump could_not_flirt
                
                #Event C
                elif one_out_of_three == 3: ### Filch
                    stop music fadeout 1.0
                    call her_main("I tried to flirt with mr.Filch, [genie_name]...","open","worriedL",xpos="right",ypos="base")
                    m "I see. {size=-5}(No idea who that is.){/size}"
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Yes, I know that technically mr.Filch is not a teacher...","open","worried")
                    m "Huh?"
                    call her_main("But he is part of the school's staff...","base","base")
                    her "And we did hit it off quite well too!"
                    her "He was surprisingly sweet."
                    her "But I don't think he is \"dirty\", [genie_name]."
                    m "Gotcha... Mr.Fil{size=+7}TH{/size} is off the list then."
                    call her_main("It's \"Mr.Filch\", [genie_name]...","normal","frown")
                    m "What did I say?"
            
            #Second Level.
            elif whoring >= 6 and whoring < 9:

                #Event A
                if one_out_of_three == 1: ### Slughorn
                    stop music fadeout 1.0
                    call her_main("Well, professor Slughorn invited me over to one of his...","open","worriedL",xpos="right",ypos="base")
                    her "Rather disturbing tea-parties..."
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("There were plenty of girls...","open","closed")
                    her "But all of them were much younger then me..."
                    call her_main("Almost every guest was a freshman...","annoyed","suspicious")
                    call her_main("We had tea and some cake...","open","closed")
                    her "Everything was pretty harmless..."
                    m "Did you flirt with the man or not?"
                    her "I did..."
                    call her_main("Or at least I tried...","annoyed","suspicious")
                    her "Professor Slughorn seems to be more interested in much younger girls..."
                    m "You almost sound jealous, [hermione_name]."
                    call her_main("What?!","angry","wide")
                    call her_main("That is preposterous!","annoyed","angryL")
                    m "Here are your points..."
                    her "...................."
                
                #Event B
                elif one_out_of_three == 2: ### Lockhart
                    $ autograph = True #This unlocks the Lockheart tattoo in the wardrobe now.
                    $ h_request_wear_tattoos = True
                    $ hermione_wear_tattoos = True
                    $ hermione_tattoos_list.append("thigh/signature") #LOCKHEART TATTOO
                    
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("I had an amazing day, [genie_name]!","smile","happyCl",emote="06",xpos="right",ypos="base")
                    m "Do tell, [hermione_name]..."
                    call her_main("I had a class with professor Lockhart today...","grin","baseL")
                    her "[genie_name] Lockhart is so charming and smart and..."
                    call her_main("And perfect...","base","ahegao_raised")
                    m "Please spare me your schoolgirl crush, [hermione_name]."
                    call her_main("[genie_name] Lockhart was even kind enough to give me his autograph...","smile","happyCl",emote="06")
                    m "How kind of him indeed."
                    call her_main("Yes, I can't wait to show it to the girls!","grin","baseL")
                    m "Hm... Can I see it?"
                    call her_main("[genie_name]?","base","base")
                    m "The Autograph, [hermione_name]. Can I see it?"
                    call her_main("Well... Em... It's in a rather private area, [genie_name].","upset","wink")
                    m "What? Well, then professor Goldenheart surely is \"dirty\"!"
                    call her_main("It's professor Lockhart, [genie_name]...","annoyed","angryL")
                    her "And... Ehm..."
                    her "Well, it's not {size=+5}that{/size} private..."
                    m "Show it to me then!"
                    call her_main("No, [genie_name]! That would be inappropriate!","disgust","glance")

                    menu: 
                        "{size=-3}\"Lockhart will be out of this school in no time!\"{/size}":
                            call her_main("Because of me?","scream","wide_stare")
                            call her_main("[genie_name], please!","mad","worried",tears="soft")
                            m "Show me!"
                            call her_main("No, it's embarrassing!","scream","worriedCl")

                            menu:
                                "\"Fine. Here are your points.\"":
                                    call her_main("Thank you for understanding, [genie_name].","base","happyCl")
                                "\"Show me or I won't pay you!\"":
                                    call her_main("What?!","scream","wide_stare")
                                    call her_main("...............","annoyed","down")
                                    call her_main("..................","annoyed","worriedL")
                                    call her_main("Well, alright, but only to clear my idol's name...","angry","angry")
                                    pause.5
             
                                    call her_head("Here....","disgust","down_raised",cheeks="blush",xpos="mid",ypos="base",trans="fade")
                                    
                                    call set_hermione_action("lift_skirt")
                                    pause.5
                                    
                                    m "Hm..."
                                    call her_main("","angry","annoyed",emote="01",xpos="right",ypos="base")
                                    call ctc
                                    
                                    call her_main("As you can see Professor Lockhart is nothing but an embodiment of everything pure and courageous!","annoyed","annoyed")
                                    pause
                                    m "Do I? From this?"
                                    her "You should not worry about professor Lockhart, [genie_name]."
                                    her "He is not \"dirty\"."
                                    m "Ah, what do I care..."
                                    call her_main("............?","angry","annoyed",emote="01")
                                    
                                    call set_hermione_action("none")
                                    
                                    call her_main("","angry","angry")
                                    call ctc
                                    $ mad += 18

                        "\"Fine... Here are your points.\"":
                            call her_main("Thank you for understanding, [genie_name].","base","happyCl")
                           
                #Event C
                elif one_out_of_three == 3: ### Filch
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Well, I spent quite some time by flirting with mr.Filch today.","soft","base",xpos="right",ypos="base")
                    call her_main("What a well read and exceptionally well mannered gentleman mr.Filch is.","open","closed")
                    m "........"
                    call her_main("But I don't think anyone knows him like that...","soft","baseL")
                    her "I don't think anyone knows mr.Filch like I do."
                    call her_main("I feel like he really opened up to me, [genie_name].","base","base")
                    m "Right..."
                    m "This, mr.Fli{size=+7}nt{/size}--"
                    call her_main("It's mr.Filch, [genie_name].","open","angryCl")
                    m "Yeah, whatever... Is he a teacher here then?"
                    her "Mr.Filch? A teacher? No, [genie_name]..."
                    call her_main("He is the caretaker...","base","base")
                    m "A caretaker...?"
                    m "You mean he is a janitor?"
                    call her_main("Well...","open","worriedL")
                    m "[hermione_name], I did not send you out there to charm school janitors!"
                    call her_main("But mr.Filch is part of the school staff, [genie_name]!","open","base")

                    menu:
                        "\"Just take your points and go!\"":
                            call her_main(".........................","normal","base")
                        "\"Favour failed! No points for you!\"":
                            $ mad +=15
                            call her_main("But [genie_name]?","normal","frown")
                            m "You are dismissed, [hermione_name]."
                            call her_main(".........................................","angry","angry")
                            
                            $ hg_pr_FlirtTeacher_OBJ.inProgress = False
                            jump could_not_flirt
            
            #Third level.
            elif whoring >= 9:

                #Event A
                if one_out_of_three == 1: ### Filch
                    stop music fadeout 1.0
                    call her_main(".............................","normal","worriedCl",xpos="right",ypos="base")
                    her "....................................."
                    m "[hermione_name]?"
                    call her_main("[genie_name], I.....","angry","worriedCl",emote="05")
                    m "What is it? What happened?"
                    call her_main("Well...","annoyed","worriedL")
                    her "It's mr.Filch, [genie_name]..."
                    m "The janitor?"
                    call her_main("I flirted with him a little...","open","base")
                    her "And it went great at first..."
                    call her_main(".......................","annoyed","worriedL")
                    m "................?"
                    call her_main("And then...","open","base")
                    call her_main("Not sure if I should...","annoyed","worriedL")
                    m "[hermione_name], if you are not going to speak up, you may as well leave."
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("He showed me his \"thing\", [genie_name]!","scream","worriedCl")
                    m "His what?"
                    call her_main("His... manhood, [genie_name].","angry","worriedCl",emote="05")
                    g9 "Way to go, Janitor-guy!"
                    call her_main("What?!","scream","wide_stare")
                    m "*Khem* I mean, this is unspeakable!"
                    call her_main("Yes... Vile crooked thing all covered in veins...","angry","base",tears="soft")
                    m "Spare me the grisly details, [hermione_name]."
                    call her_main("Why would he do such a thing?","mad","worriedCl",tears="soft_blink")
                    her "One second we were just talking and then..."
                    m "Well, your noble  sacrifice shall not go unnoticed, [hermione_name]!"
                    m "Fifteen points to \"Gryf--"
                    call her_main("Professor, please wait.","soft","base",tears="soft")
                    m "Huh?"
                    call her_main("Well, aren't you going to do something about this?","open","base")
                    m "Well..."
                    call her_main("What if I am not the first victim..?","angry","angry")
                    her "Some unfortunate freshman could be traumatized for life!"
                    m "And who wouldn't be really?"
                    call her_main("Does this mean you will take action, [genie_name]?","open","base")
                    m "uhm... Yeah, sure..."
                    m "There! Putting it on my \"to-do-list\"..."
                    m "\"Take care of the creepy janitor-guy and his crooked cock.\"..."
                    m "Yes, first thing tomorrow."
                    call her_main("Thank you [genie_name].","open","closed")
                    call her_main("Can I have my points now?","smile","happyCl")
    
                #Event B
                elif one_out_of_three == 2: ### Snape
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("Professor Snape!","angry","angry",emote="01",xpos="right",ypos="base")
                    m "Ehm... Yeah, I'm pretty sure it's Dumbledore or something..."
                    call her_main("[genie_name], please, you need to listen to me!","open","base")
                    m "Yes, yes, [hermione_name], I'm listening."
                    call her_main("I just confirmed that professor Snape is corrupted and \"dirty\", [genie_name]!","open","angryCl")
                    m "Tell me what happened."
                    
                    hide screen hermione_main
                    hide screen blktone
                    call blkfade
                    
                    call her_head("Well, during classes today...","open","base",xpos="base",ypos="base")
                    call her_head("I have been doing my best to attract professor Snape's attention...","open","baseL")
                    call her_head("I have been giving him \"dreamy looks\"...","open","down")
                    call her_head("And I've been eyeing his crotch...","soft","baseL")
                    m "You..."
                    m "Eyed his crotch?"
                    call her_head("Yes... It's when you stare at a man's crotch and imagine that you are looking at something you want badly...","open","angryCl")
                    m "Where do you get this stuff?"
                    call her_head("Women's magazines...","open","worriedL")
                    call her_head("Well, anyway, it worked, [genie_name].","normal","frown")
                    
                    hide screen blkfade
                    show screen snape_groping
                    with fade
                    call ctc
                    
                    call her_head("As soon as the class was over, professor Snape grabbed my buttocks, [genie_name]!","angry","angry")
                    m "The fiend!"
                    m "Did you enjoy it, though?"
                    call her_head("[genie_name], I am only doing this--","scream","angryCl")
                    m "Go \"Gryffindors\"! honour and all that. Yes, I remember."
                    call ctc
                    
                    hide screen snape_groping
                    with fade
                    
                    m "Here are your points."
                    show screen blktone
                    call her_main("","disgust","glance",xpos="right",ypos="base")
  
                #Event C
                elif one_out_of_three == 3: ### Lockhart
                    stop music fadeout 1.0
                    call her_main("Professor Lockhart!","annoyed","frown",xpos="right",ypos="base")
                    m "Got it! Adding him to the \"Naughty list\"!"
                    call her_main("No, [genie_name], it's not that...","open","worried")
                    call her_main("Or...","annoyed","angryL")
                    her "I'm not sure..."
                    call her_main("I used to adore him...","open","worried")
                    call her_main("But he...","soft","baseL")
                    her "He just..."
                    call her_main("How is this possible?","mad","worriedCl",tears="soft_blink")
                    her "I can't believe this..."
                    hide screen hermione_main
                    with d3
                    call play_music("playful_tension")# SEX THEME.
                    m "{size=-4}(Agh! The suspense is killing me!){/size}" 
                    m "{size=-4}(Did he force her to blow him?){/size}"
                    m "{size=-4}(Did he rape her?){/size}"
                    g4 "What was it, [hermione_name]? Speak up!"
                    call her_main("Huh?","open","base")
                    m "What did Professor Lockhart do to you?"
                    call her_main("Ehm... Nothing, [genie_name]...","soft","baseL")
                    m "Nothing?!"
                    call her_main("Yes, I sort of cornered mr.Lockhart today...","open","worried")
                    call her_main("And I also may have sort of made a pass at him...","open","base")
                    m "Seriously?"
                    call her_main("Yes... Not sure what had gotten into me, [genie_name]...","angry","worriedCl",emote="05")
                    m "Way to go, [hermione_name]!"
                    call her_main("Hear me out first [genie_name], please!","scream","worriedCl")
                    m "My apologies. Please continue."
                    call her_main("Well, I always knew that mr.Lockhart was a true gentleman and...","open","base")
                    her "And... and I just wanted to clear his name from any suspicions once and for all..."
                    call her_main("...............","annoyed","worriedL")
                    her "Well mr.Lockhart did not reject me..."
                    m "You are killing me [hermione_name]!"
                    m "He didn't reject you, he didn't rape you..."
                    m "What the hell happened then?"
                    call her_main(".............","normal","worriedCl")
                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                    call her_main("I made him cry, [genie_name]...","angry","worriedCl",emote="05")
                    m "..............wait.......what?"
                    call her_main("He gave me a bewildered look and then started to sob...","angry","worried")
                    her "He looked like he was genuinely afraid of me, [genie_name]."
                    call her_main("I think...","annoyed","worriedL")
                    her "I think mr.Lockhart might be afraid of women..."
                    m "Afraid of women?"
                    m "What is that supposed to mean?"
                    call her_main("That he is into boys, [genie_name]?","angry","worriedCl",emote="05")
                    m "Oh..."
                    call her_main("............","upset","wink")
                    m "..........."
                    m "Well, I bet it was a traumatizing experience for you, [hermione_name]."
                    call her_main("It was, [genie_name]...","open","base")
                    m "Well, I hope these points will make you feel better."
    
    $ gryffindor +=15
    m "The \"Gryffindors\" gets 15 points!"
    her "Thank you, [genie_name]."
    
    $ hg_pr_FlirtTeacher_OBJ.points += 1
    $ hg_pr_FlirtTeacher_OBJ.inProgress = False
    
    if whoring <= 5:  # (if whoring >= 3 and whoring <= 5) - LEVEL 02
        $ whoring +=1
    if whoring >= 5 and hg_pr_FlirtTeacher_OBJ.points >= 2:
        $ hg_pr_FlirtTeacher_OBJ.complete = True
    
    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.

