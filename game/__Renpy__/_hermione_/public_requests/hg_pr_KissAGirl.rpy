

### Make Out With A Girl ###

##(Level 05) (45 pt.) (MAKE OUT WITH A GIRL). (Available during daytime only).
label hg_pr_KissAGirl: #LV.5 (Whoring = 12 - 14)
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pr_KissAGirl_OBJ.points < 1:
        m "{size=-4}(Tell her to go make out with one of her female classmates?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests
    
    call bld from _call_bld_46
    
    #Intro.
    if hg_pr_KissAGirl_OBJ.points == 0:
        m "Have You ever kissed another girl, [hermione_name]?"
        call her_main("?!","normal","frown",xpos="right",ypos="base") from _call_her_main_1136

        if whoring < 12 or hg_pr_FlashClassmate_OBJ.points < 2: # Counts how many times you sent Hermione to flash a classmate.
            jump too_much

        call play_music("chipper_doodle") from _call_play_music_54 # HERMIONE'S THEME.
        call her_main("I am not a... lesbian, [genie_name].","open","base") from _call_her_main_1137
        m "Silly girl... You don't need to be a lesbian to kiss girls."
        m "I mean, I do it and I am not a lesbian either."
        call her_main("...............","angry","angry") from _call_her_main_1138
        her "[genie_name]--"
        m "No, \"[genie_name]s\"! This is your task for today!"
        m "Go find a cute little thing and plant a \"smooch\" on her!"
        call her_main("[genie_name], but I am--","open","worried") from _call_her_main_1139
        m "Dismissed, [hermione_name]."
        call her_main("[genie_name]!......","normal","frown") from _call_her_main_1140
        m "I said you're dismissed."
        call her_main("*Humph!*...","annoyed","frown") from _call_her_main_1141
    
    #Second time event.
    else:
        m "[hermione_name], forty five house points are up for grabs today!"
        m "Are you interested?"

        if whoring >= 12 and whoring < 15: # LEVEL 05 FIRST EVENT.
            call play_music("chipper_doodle") from _call_play_music_55 # HERMIONE'S THEME.
            call her_main("It depends...","normal","base",xpos="right",ypos="base") from _call_her_main_1142
            her "Will I have to do something depraved again?"
            m "\"Depraved\"??! When did I ever--?"
            call her_main("Really, [genie_name]?","open","angryCl") from _call_her_main_1143
            m "Fine, fine... But all I want you to do today is to make out with another girl."
            call her_main("Oh, is that all?","angry","angry") from _call_her_main_1144 # :(
            m "Yes... Pretty basic stuff for you, right?"
            m "And you will be getting forty five house points afterwards of course."
            call her_main(".............","normal","frown") from _call_her_main_1145
            m "So... Are you up for it?"
            call her_main("I will see what I can do, [genie_name]...","annoyed","angryL") from _call_her_main_1146
            m "Great. See you after your classes then."
            call her_main("................","annoyed","annoyed") from _call_her_main_1147
        
        elif whoring >= 15 and whoring < 18: # LEVEL 06. Event level 02.
            call her_main("I suppose...","annoyed","ahegao",xpos="right",ypos="base") from _call_her_main_1148
            m "Great. All you need to do is make out with another girl."
            call her_main("I see...","annoyed","down") from _call_her_main_1149
            m "Up for the task, [hermione_name]?"
            call her_main("I suppose...","annoyed","worriedL") from _call_her_main_1150
            m "Great. See you after your classes then."
        
        elif whoring >= 18: # LEVEL 07+ Event level 03.
            call play_music("chipper_doodle") from _call_play_music_56 # HERMIONE'S THEME.
            call her_main("Sure, why not?","base","base",xpos="right",ypos="base") from _call_her_main_1151
            m "Great."
            m "I want you to make out with another girl today."
            call her_main("Alright.","soft","baseL") from _call_her_main_1152
            call her_main("I know a couple of girls who are hungry for attention and wouldn't mind putting on a little show.","smile","glance") from _call_her_main_1153
            m "Great. See you after your classes then."
    
    $ hg_pr_KissAGirl_OBJ.inProgress = True
    
    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.

    
label hg_pr_KissAGirl_complete:

    call play_sound("door") from _call_play_sound_49 #Sound of a door opening.
    call her_walk("door","mid",2) from _call_her_walk_33
    call bld from _call_bld_47
    

    #First time event.
    if whoring >= 12 and whoring < 15: # LEVEL 05  

        #Event A
        if one_out_of_three == 1:
            stop music fadeout 1.0
            m "[hermione_name]..."
            m "Did you succeed in completing your task?"
            show screen blktone
            call her_main("I...","open","worried",xpos="right",ypos="base") from _call_her_main_1154
            m "I told you to make out with another girl..."
            m "Did you do it?"
            call her_main("I...","open","worriedL") from _call_her_main_1155
            her "I tried, [genie_name]. I really did."
            m "And?"
            call her_main("Well...","annoyed","worriedL") from _call_her_main_1156
            call play_music("chipper_doodle") from _call_play_music_57 # HERMIONE'S THEME.
            her "It was awkward and embarrassing..."
            m "did you do it or not?"
            call her_main("...no I did not, [genie_name]...","annoyed","angryL") from _call_her_main_1157
            her "All I did was making a complete fool out of myself..."
            call her_main("In front of the entire class...","angry","angry") from _call_her_main_1158
            m "Tell me what happened, [hermione_name]."
            call her_main("No, I will not, [genie_name].","annoyed","angryL") from _call_her_main_1159
            her "Not in a million years!"
            call her_main("Why do I have to perform such ridiculous tasks anyway?!","shock","worriedCl") from _call_her_main_1160
            her "What is the point of all this?"
            call her_main("I hate this!","scream","angryCl") from _call_her_main_1161
            call her_main("...............","annoyed","angryL") from _call_her_main_1162
            her "................."
            m ".............."
            m "You are not getting paid, you know that, right?"
            call her_main("I don't care...","scream","angryCl") from _call_her_main_1163
            $ mad +=25
                
            $ hg_pr_KissAGirl_OBJ.inProgress = False
            jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
        
        #Event A
        elif one_out_of_three == 2:
            call play_music("chipper_doodle") from _call_play_music_58 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("I did, [genie_name]...","open","closed",xpos="right",ypos="base") from _call_her_main_1164
            m "Good. Give me the details."
            call her_main("Well, I kissed a girl. Just like you told me to, [genie_name].","annoyed","suspicious") from _call_her_main_1165
            m "I guess it was embarrassing for you, girl?"
            call her_main("Very much so, [genie_name].","annoyed","angryL") from _call_her_main_1166 # :( D: :D::D:D:D::D::D::D::DDD:DD
            m "Did you enjoy it though?"
            call her_main("*Humph!*...","annoyed","annoyed") from _call_her_main_1167
            m "So you kissed a girl and you liked it?"
            call her_main("Yes...","disgust","glance") from _call_her_main_1168
            m "Did your tongues touch?"
            call her_main("Yes...","disgust","glance") from _call_her_main_1169
            her "It was a proper deep kiss, if that's what you want to know."
            her "Can I just get my payment now?"
            call her_main("Please, [genie_name]...","annoyed","angryL") from _call_her_main_1170
            m "Well, alright..."
        
        #Event C
        elif one_out_of_three == 3:
            call play_music("chipper_doodle") from _call_play_music_59 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes, I did, [genie_name].","open","closed",xpos="right",ypos="base") from _call_her_main_1171
            m "Good. Tell me how it went."
            call her_main("It went well, [genie_name].","open","closed") from _call_her_main_1172
            m "Great. Give me the details."
            call her_main("What would you like to know, [genie_name]?","open","angryCl") from _call_her_main_1173
            m "Tell me everything! Was the girl pretty?"
            m "Did she return your kiss?"
            call her_main("She was relatively pretty, [genie_name].","open","suspicious") from _call_her_main_1174
            her "And she did return my kiss..."
            call her_main("...........","annoyed","closed") from _call_her_main_1175
            call her_main("Anything else, [genie_name]?","open","suspicious") from _call_her_main_1176
            m "...."
            m "Why are you being difficult, [hermione_name]?"
            call her_main("With all due respect, [genie_name]...","open","angryCl") from _call_her_main_1177
            her "You told me to make out with another girl, and I did..."
            call her_main("Now, I would like to get paid if you would be so kind.","normal","base") from _call_her_main_1178
            m "......................"

            menu:   
                "\"Fine. Here is your payment, girl.\"":
                    pass
                "\"I don't appreciate your attitude, [hermione_name].\"":
                    call her_main("Well, that is unfortunate, [genie_name].","open","angryCl") from _call_her_main_1179
                    m "Sure is..."
                    m "Because you are not getting paid you insolent, little witch."
                    stop music fadeout 1.0
                    call her_main("What?","normal","base") from _call_her_main_1180
                    call her_main("[genie_name], you can't do that!","open","worried") from _call_her_main_1181
                    m "Dismissed."
                    call her_main("B-but--","open","worriedL") from _call_her_main_1182
                    call her_main("[genie_name], please!","open","worried") from _call_her_main_1183
                    her "The girl was from \"Hufflepuff\" and--"
                    m "Too late for that, [hermione_name]."
                    m "You are dismissed."
                    call her_main("......","angry","base",tears="soft") from _call_her_main_1184
                    $ mad +=25
                
                    $ hg_pr_KissAGirl_OBJ.inProgress = False
                    jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
                         
    
    elif whoring >= 15 and whoring <= 17: # LEVEL 06. Event level 02. 
        
        #Event A    
        if one_out_of_three == 1:
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("I did, [genie_name]...","open","closed",xpos="right",ypos="base") from _call_her_main_1185
            m "Well, don't just stand there. Give me the details."
            call her_main("Ehm, alright...","open","base") from _call_her_main_1186
            her "The girl was from \"Ravenclaw\"..."
            call her_main("I think she may have been an underclassman, but I did not ask...","soft","baseL") from _call_her_main_1187
            her "We got to talking about boys..."
            call her_main("And she told me that she never kissed one...","open","closed") from _call_her_main_1188
            her "And that she is worried that she might be very bad at it..."
            call her_main("So I just offered my help...","base","base") from _call_her_main_1189
            call play_music("playful_tension") from _call_play_music_60# SEX THEME.
            her "And then we spent some time in one of the bathroom stalls..."
            call her_main("Making out...","base","base") from _call_her_main_1190
            call her_main("She caught on real quick... I think she could be really good at it with some practice...","open","base") from _call_her_main_1191
            call her_main("Also she was quite adorable...","base","base") from _call_her_main_1192
            call her_main("She kept calling me \"[hermione_name]\"...","smile","baseL") from _call_her_main_1193
            m "Hm..."
            m "I Don't recall sending you out with a task to confuse little kids, [hermione_name]."
            call her_main("\"Little kids\"? [genie_name], please...","smile","glance") from _call_her_main_1194
            her "You should have seen that girl..."
            her "A little petite? Maybe... But definitely not a \"kid\"."
            call her_main("And I assure you that she was anything but confused.","smile","angry") from _call_her_main_1195
            her "In fact, at the end of our \"Study session\" she got rather obnoxious..."
            call her_main("And it sort of felt as if she was taking advantage of me...","open","base") from _call_her_main_1196
            m "Oh... Well, in that case..."
            call her_main("","base","base") from _call_her_main_1197
        
        #Event B    
        elif one_out_of_three == 2:
            m "[hermione_name]. Did you complete your task?"
            show screen blktone
            call play_music("chipper_doodle") from _call_play_music_61 # HERMIONE'S THEME.
            call her_main("I did, [genie_name].","open","closed",xpos="right",ypos="base") from _call_her_main_1198
            m "Tell me how it went."
            call her_main("Well... Ehm...","open","base") from _call_her_main_1199
            her "There is this one girl who is into girls..."
            her "I thought she would be the ideal candidate for my task..."
            her "so I told her that I am curious and that I would like to kiss her..."
            call her_main("She said that we should go to the girls' restroom for that...","open","down") from _call_her_main_1200
            her "But I just kissed her right there in the corridor..."
            call her_main("And she kissed me back but...","open","base") from _call_her_main_1201
            call her_main("It got weird really fast...","angry","down_raised") from _call_her_main_1202
            her "The way she kissed me..."
            call her_main("She did it like a boy would, [genie_name]...","angry","base") from _call_her_main_1203
            call her_main("Aggressive but confident...","angry","down_raised") from _call_her_main_1204
            call her_main("Naturally a small group of spectators gathered up around us right away...","upset","closed") from _call_her_main_1205
            call her_main("Mostly boys of course...","open","base",cheeks="blush") from _call_her_main_1206
            call her_main("Some of them even cheered us on...","open","worriedCl",cheeks="blush") from _call_her_main_1207
            call her_main(".....","base","suspicious") from _call_her_main_1208
            her "By the way, the girl I kissed, [genie_name]..."
            m "Hm...?"
            call her_main("She is one of those unpopular kids...","open","closed") from _call_her_main_1209
            her "I know that other students make fun of her sometimes..."
            call her_main("But today changed everything...","base","suspicious") from _call_her_main_1210
            her "I Single-handedly turned that girl from a social outcast..."
            call her_main("Into \"that lesbian girl who made out with Hermione Granger\"!","smile","angry") from _call_her_main_1211
            m "Wow... You are just like some kind of hero or something..."
            call her_main("I suppose I am, [genie_name]...","base","glance") from _call_her_main_1212
            her "I changed that poor girl's life..."
            m "Now you are just pulling on my heartstrings..."
        
        #Event C
        elif one_out_of_three == 3:
            show screen blktone
            call play_music("chipper_doodle") from _call_play_music_62 # HERMIONE'S THEME.
            call her_main("[genie_name]?","open","closed",xpos="right",ypos="base") from _call_her_main_1213
            m "Yes, [hermione_name]?"
            call her_main("May I ask you a question, [genie_name]?","open","base") from _call_her_main_1214
            m "By all means."
            call her_main("Ehm...","annoyed","angryL") from _call_her_main_1215
            call her_main("Why are boys so into watching girls make out with each other, [genie_name]?","disgust","glance") from _call_her_main_1216
            menu:
                m "..."
                "\"Who knows? Boys are weird.\"":
                    call her_main("Yes, they are, aren't they...?","angry","down_raised") from _call_her_main_1217
                    m "Yes, yes..."
                    m "And that is why young girls such as yourself...."
                    m "Are often interested in a much older gentleman..."
                    call her_main("??!","angry","base") from _call_her_main_1218
                    call her_main("That is not what I meant, [genie_name]...","annoyed","annoyed") from _call_her_main_1219
                "\"You wouldn't understand, girl.\"":
                    call her_main("Hm...","upset","closed") from _call_her_main_1220
                    call her_main("What about you, [genie_name]?","angry","base") from _call_her_main_1221
                    her "Where you like that when you were a boy?"
                    m "You mean if I enjoyed watching two girls going at it?"
                    m "Well of course."
                    m "I still do..."
                    call her_main("Oh...","upset","closed") from _call_her_main_1222
                "\"Kissing girls? Where?!!\"":
                    call her_main("Tsk!......................","angry","angry",emote="01") from _call_her_main_1223 # :(
            call her_main("Well, I am only asking you this, [genie_name], because...","open","down") from _call_her_main_1224
            call her_main("...it is sort of becoming a new trend in our school...","angry","base") from _call_her_main_1225
            her "Some girls are willing to do this simply to catch the attention of the boy they fancy..."
            m "Are you one of those girls, [hermione_name]?"
            call her_main("I suppose...","angry","down_raised") from _call_her_main_1226
            call her_main("I mean, only because of the favours you buy from me, [genie_name]...","upset","closed") from _call_her_main_1227
            m "Good... Tell me more."
            call her_main("Well, as you know, I am quite popular...","smile","happyCl",emote="06") from _call_her_main_1228
            call her_main("So all I had to do is just mention that I would not mind doing it today...","base","happyCl") from _call_her_main_1229
            her "And I had half a dozen girls lined up instantly..."
            call her_main("I chose a girl from \"Gryffindor\" of course...","base","base") from _call_her_main_1230
            call her_main("And we put on a little show right in the middle of the classroom...","open","base") from _call_her_main_1231
            m "Good... Tongue and everything?"
            call her_main("Tongue and everything, [genie_name].","annoyed","worriedL") from _call_her_main_1232
            m "Nicely done."
            call her_main("","base","base") from _call_her_main_1233
    
    elif whoring >= 18: # LEVEL 07+  
        
        #Event A                    
        if one_out_of_three == 1: #Snowballing
            label snowballing:
                pass
            m "[hermione_name]..."
            show screen blktone
            call play_music("chipper_doodle") from _call_play_music_63 # HERMIONE'S THEME.
            call her_main("Good evening, [genie_name].","open","closed",xpos="right",ypos="base") from _call_her_main_1234
            m "Did you complete your task, girl?"
            call her_main("I did, [genie_name].","soft","base") from _call_her_main_1235
            m "I'm all ears..."
            call her_main("Well, I kissed that annoying blond girl from \"Slytherin\"...","annoyed","suspicious") from _call_her_main_1236
            m "Hm... \"annoying\", huh?"
            m "Because she happens to be from \"Slytherin\"."
            call her_main("Precisely so, [genie_name].","open","closed") from _call_her_main_1237
            m "Hm..."
            m "Don't you think that that's a little bit of prejudice on your part?"
            m "Or shall I say that you are being a \"housist\"?"
            call her_main("...a \"housist\", [genie_name]?","annoyed","annoyed") from _call_her_main_1238
            m "Well, you know... It's like \"sexist\" or \"ageist\"..."
            m "You just put an \"ist\" after something and it automatically becomes a bad thing..."
            call her_main("\"housist\" is not an actual word, [genie_name]...","soft","baseL") from _call_her_main_1239
            m "It's not? Well, give it time..."
            call her_main(".............?","annoyed","annoyed") from _call_her_main_1240
            m "\"Housophobic\"...?"
            m "No, wait, I got it!"
            m "\"Housophobe\"!"
            call her_main("Stop it, [genie_name]. I am not any of those weird words...","normal","frown") from _call_her_main_1241
            her "\"Slytherins\" are evil and annoying. Nobody likes them, and that is a fact!"
            m "Fine, whatever. Back to the \"girl-kissing\" then."
            call her_main("...............","annoyed","worriedL") from _call_her_main_1242
            her "Like I was saying..."
            call her_main("I kissed that girl from \"Slytherin\"...","open","base") from _call_her_main_1243
            call her_main("Normally I would never do it, of course...","annoyed","angryL") from _call_her_main_1244
            her "Not with someone from that wretched house anyways..."
            call her_main("But she approached me first and practically begged me to do it with her...","annoyed","annoyed") from _call_her_main_1245
            call her_main("And today of all days...","annoyed","angryL") from _call_her_main_1246
            her "to be honest..."
            call her_main("She was quite attractive...","annoyed","annoyed") from _call_her_main_1247
            call her_main("For someone from \"slytherin\" that is...","upset","closed") from _call_her_main_1248
            call her_main("I did not ask her why she needed this so desperately...","open","closed") from _call_her_main_1249
            her "She was probably just trying to boost her own popularity at my expense..."
            her "Or it could also be that someone from the school staff bought this favour from her..."
            call her_main("The same way you buy favours from me, [genie_name]...","open","annoyed",cheeks="blush") from _call_her_main_1250
            m "(Snape?)"
            call her_main("If that is the case I am sure that it was professor Snape...","angry","angry") from _call_her_main_1251
            m "What? He would never..."
            call her_main("You should really investigate Professor Snape's activities, [genie_name]...","annoyed","angryL") from _call_her_main_1252
            m "Of course..."
            m "Putting him on my \"naughty boys list\" as we speak..."
            call her_main("..........","disgust","glance") from _call_her_main_1253
            m "What happened next, [hermione_name]?"
            call her_main("Oh, right...","open","down") from _call_her_main_1254
            her "Well, we made out for a while..."
            her "She was very... passionate."
            call her_main("So I imagine it was quite a spectacle...","angry","wink") from _call_her_main_1255
            her "The boys were cheering and whistling..."
            call her_main("So we decided to \"snowball\" a little...","base","down") from _call_her_main_1256
            m "I'm sorry, you decided to do what?"
            call her_main("To \"snowball\", [genie_name].","angry","wink") from _call_her_main_1257
            call her_main("It is when one girl spits into another girl's mouth...","base","glance") from _call_her_main_1258
            her "We call it \"snowballing\"..."
            her "The boys really go crazy from that for some reason..."
            m "I imagine they do..."
            call her_main("So she spat into my mouth...","open","closed") from _call_her_main_1259
            her "And then I spat into hers..."
            call her_main("Although I would much rather spit in her face!","angry","angry",cheeks="blush") from _call_her_main_1260
            call her_main("Then she returned my spit...","annoyed","angryL") from _call_her_main_1261
            call her_main("And I had to fight the urge to slap her smug face for doing that...","angry","angry",cheeks="blush") from _call_her_main_1262
            call her_main("But I don't think the boys would appreciate that...","upset","closed") from _call_her_main_1263
            m "Well... You would be surprised..."
            call her_main("In any case, After that we kissed some more...","base","down") from _call_her_main_1264
            her "And then the break was over..."
            call her_main("And we had to run to class...","angry","wink") from _call_her_main_1265
            m "*Sigh...* Nonchalant and innocent schooldays..."
            m "Home assignments... Classes..."
            m "Schoolgirls \"snowballing\" in the courtyard..."
            m "Well done, [hermione_name]."
            call her_main("","grin","baseL") from _call_her_main_1266
        
        #Event B
        elif one_out_of_three == 2:
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("I did, [genie_name].","open","closed",xpos="right",ypos="base") from _call_her_main_1267
            call her_main("Only... ehm...","grin","baseL") from _call_her_main_1268
            m "What is it?"
            call her_main("Well... I have this friend...","base","base") from _call_her_main_1269
            her "Her name is Ginny Weasley..."
            call her_main("And... uhm...","base","baseL",cheeks="blush") from _call_her_main_1270
            her "I'm Not sure how to say this..."
            m "Just say it, [hermione_name]."
            call her_main("Well, we decided to skip the potions class together...","open","base") from _call_her_main_1271
            her "And study for the upcoming Herbology test instead..."
            her "So me and Ginny, we were studying..."
            her "And we got to talking about boys..."
            m "Naturally..."
            call play_music("playful_tension") from _call_play_music_64# SEX THEME.
            call her_main("And then I sort of kissed her...","open","baseL",cheeks="blush") from _call_her_main_1272
            call her_main("And Ginny returned my kiss with such passion...","base","glance") from _call_her_main_1273
            her "that we sort of ended up doing more than just kissing..."
            
            #if not kissed_ginny:
            #    call nar(>Your curiosity about Ginny grows!)
            #$ kissed_ginny = True
            
            g9 "And afterwards you had a pillow fight in lingerie?"
            call her_main("Err... No...","open","squint",cheeks="blush") from _call_her_main_1274
            m "What did you do then?"
            call her_main("I am not telling you, [genie_name].","base","baseL",cheeks="blush") from _call_her_main_1275 # :)
            her "You sent me out to kiss a girl..."
            her "And I did just that."
            call her_main("The rest shall remain private.","angry","wink") from _call_her_main_1276
            m "Now you are just being cruel, you little witch."
            call her_main("My points please.","smile","glance") from _call_her_main_1277 # :)
            m "Fine..."
        
        #Event C #Removed
        elif one_out_of_three == 3: ### EVENT (C) Only takes place once
            if lazy_aka_not_yet:
                jump snowballing #Removed "Pass"
            else:
                jump snowballing

            $ lazy_aka_not_yet = False #Makes sure this event only takes place once.
            call play_music("chipper_doodle") from _call_play_music_65 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("Yes I did, [genie_name].","base","base",xpos="right",ypos="base") from _call_her_main_1278
            m "Splendid. Tell me more."
            show screen blktone
            with d3
            call her_main("Of course.","smile","glance") from _call_her_main_1279
            her "I decided to go for a different approach today..."                                                                                                                                                                                                              
            stop music
            call her_main("I figured that iffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff","open","base",xpos=500) from _call_her_main_1280
            m "Huh?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            her "If I coulddddddddddddddddddd"
            pause
            pause
            pause
            with hpunch
            g4 "{size=+5}Goddammit!!!{/size}"
            g4 "{size=+5}AKABUR?!!!{/size}"
            a4 "Huh...? WHAT?!! What do you want from me?"
            a4 "There is no release date set! Stop asking me!"
            g4 "What are you talking about?"
            a5 "I mean, I'm not sleeping..." 
            a7 "*Yawn*..."
            a5 "................"
            m "So Is Hermione going to stutter from now on? Is that what this is?"
            pause
            pause
            g4 "Are you still there?"
            a1 "I'm not sleeping..."
            a5 "Just resting my eyes..."
            g4 "Dammit, man."
            g4 "Just go catch up on some sleep before you ruin the whole thing."
            m "Get some shuteye and then finish this event properly."
            a1 "I can't..."
            a1 "I want this game to be released as soon as possible..."
            a1 "No, scratch that. I want it to be released sooner than possible..."
            a1 "People trust me... and..."
            a7 "*yawn*..."
            a1 "And...."
            pause
            pause
            m "Akabur?"
            m "Dude?"
            pause
            pause
            m "*Sigh*...well, we could let this one event slide I suppose."
            m "Just this once though..."
            m "And Hermione's \"perversion\" level did increase..."
            m "So there is no need for save-scumming..."
            aa "Zzzz....zzz....."
            aa "Zzz.... Lola? no... Put your tits away I said... Zzzz....."
            aa "Zzz.... And don't call me that.... Zzz...."
            m "*Sigh...* That's just sad..."
    
    $ gryffindor +=45
    m "The \"Gryffindor\" house gets 45 points!"
    her "Thank you, [genie_name]."
    
    $ hg_pr_KissAGirl_OBJ.points += 1
    $ hg_pr_KissAGirl_OBJ.inProgress = False
    
    if hg_pr_KissAGirl_OBJ.points >= 2:
        $ hg_pr_KissAGirl_OBJ.complete = True
    
    jump hg_pr_transition_block #hides labels. Shows walkout. Jumps to next day.
    
