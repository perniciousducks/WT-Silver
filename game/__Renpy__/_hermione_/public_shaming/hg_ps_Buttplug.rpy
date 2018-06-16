

### Wear A Buttplug ###

label hg_ps_Buttplug: 
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    $ current_payout = 55 #Used when haggling about price of the favour.
    
    if hg_ps_Buttplug_OBJ.points < 1:
        m "{size=-4}(Tell her to wear a buttplug around the school?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests
    else:
        m "{size=-4}(I feel like making her walk around with a buttplug again!){/size}"
                
    m "{size=-4}(But what Type?){/size}"
    menu:
        "-Small, regular-":
            $ buttplug_size = 1
        "-Medium, magical-" if hg_ps_Buttplug_OBJ.points >= 1:
            $ buttplug_size = 2
        "-Large, magical-" if buttplug_2_worn == True and whoring > 23:
            $ buttplug_size = 3
    
    #First event.
    if hg_ps_Buttplug_OBJ.points == 0 and buttplug_size == 1:
        m "[hermione_name], I want you to do something different today..."
        call her_main("...........","soft","base",xpos="right",ypos="base") from _call_her_main_6213
        call nar(">You pull a large size buttplug out from under your desk and place it in front of her.") from _call_nar_662
        if whoring <=10:
            m "I want you to wear a buttplug around the school."
            jump too_much
            
        $ buttplug_1_worn = True
        
        call her_main("and what is that supposed to be? Some sort of animals tail?","open","suspicious") from _call_her_main_6214
        m "Not exactly, it's a buttplug. I want you to put it in while you attend class today."
        stop music
        with hpunch
        call her_main("{size=+5}What?!!{/size}","shock","wide") from _call_her_main_6215
        call play_music("chipper_doodle") from _call_play_music_236 # HERMIONE'S THEME.
        call her_main("You expect me to put that massive thing in my...","angry","angry") from _call_her_main_6216
        her "and then parade myself around the school!"
        m "It just looks like a fake tail, No one will be able to tell what it really is."
        call her_main("{size=+5}That's not the point!{/size}","scream","angryCl") from _call_her_main_6217
        her "I'm not going to put that ridiculous thing anywhere near my butt!"
        call her_main("We are done here, [genie_name]!","angry","angry",emote="01") from _call_her_main_6218
        m "Alright, alright, calm down..."
        call her_main("I most certainly will not, [genie_name]! That thing is beyond absurd!","scream","angryCl") from _call_her_main_6219
        m "Alright, fine, maybe I underestimated how large it is..."
        call her_main("You think [genie_name]?! I'd like to see you try and fit it up your-","angry","angry") from _call_her_main_6220
        m "alright, alright..."
        call her_main(".........","annoyed","annoyed") from _call_her_main_6221
        m "How about we try one a little less... ambitious."
        call her_main("............","upset","closed") from _call_her_main_6222
        m "I'm willing to give \"Gryffindor\" fifty five points."
        m "and All I ask for..."
        call her_main("..........?","annoyed","suspicious") from _call_her_main_6223
        call nar(">You pull out the small buttplug from your desk.") from _call_nar_663
        m "...is that you wear this to class..."
        call her_main("!!!......","angry","angry") from _call_her_main_6224
        m "Oh, come on... Just a harmless little baby one."
        call her_main("...","disgust","glance") from _call_her_main_6225
        m "Fifty five house points..."
        call her_main("..............","annoyed","angryL") from _call_her_main_6226
        call her_main("Fine.","annoyed","annoyed") from _call_her_main_6227
        m "Fantastic."
        m "Will you be putting it in now then?"
        call her_main("........","annoyed","angryL") from _call_her_main_6228
        call her_main("I'll put it in in the girls bathroom [genie_name]","annoyed","angryL") from _call_her_main_6229
        m "Hmmm... we'll i'll See you tonight then."
    
    #Second Event.    
    elif buttplug_2_worn == False and buttplug_size == 2:
        m "[hermione_name], I want you to try something different today..."
        call her_main("...........","soft","base",xpos="right",ypos="base") from _call_her_main_6230
        call nar(">You pull the medium size buttplug out from under your desk and place it in front of her.") from _call_nar_664
        if whoring <=15:
            m "I want you to wear this buttplug around the school."
            jump too_much
            
        $ buttplug_2_worn = True
        
        call her_main("and what is this supposed to be?","open","suspicious") from _call_her_main_6231
        m "Can't you tell it's a buttplug? They shouldn't be new to you at this point."
        call her_main("...","annoyed","annoyed") from _call_her_main_6232
        call play_music("chipper_doodle") from _call_play_music_237 # HERMIONE'S THEME.
        call her_main("Why does it have a such a large tail attached to it...","annoyed","angry") from _call_her_main_6233
        her "you can't expect me to wear that around the school!"
        m "I can and do, unless you want our little trading game to come to a halt..."
        call her_main("but it's so long! everyone will be able to see it!","normal","worriedCl") from _call_her_main_6234
        m "That's the point, [hermione_name]..."
        call her_main("...........","angry","worriedCl",emote="05") from _call_her_main_6235
        call her_main("I want 100 points.","annoyed","angry") from _call_her_main_6236
        
        menu:
            "\"Fine, but I expect you to put it in now.\"":
                $ current_payout = 100
                call her_main("What? Right now!?.","angry","worriedCl") from _call_her_main_6237
                call her_main("In front of you?","angry","wink") from _call_her_main_6238
                m "100 points [hermione_name]..."
                call her_main("ugh... Fine...","angry","down_raised") from _call_her_main_6239
                call her_main("But I'm not turning around!","annoyed","annoyed") from _call_her_main_6240
                m "Whatever suits you best..."
                ">You hand her the buttplug"
                call her_main("{size=-7}It's so big...{/size}","clench","down_raised") from _call_her_main_6241
                ">Hermione lifts her skirt and presses it against her asshole."
                call her_main("ughh... it's too big...","shock","worriedCl") from _call_her_main_6242
                call her_main("It won't fit!","open","worriedCl") from _call_her_main_6243
                m "well then Try spitting on it."
                call her_main(".........","angry","down_raised") from _call_her_main_6244
                ">She spits on the end of it and then retries."
                call her_main("it didn't work, It's just too bi-","angry","base") from _call_her_main_6245
                stop music
                
                call set_h_buttplug("plug_b_on") from _call_set_h_buttplug_4 #Updates clothing and body.
                
                with hpunch
                call her_main("{size=+5}!!!!{/size}","shock","wide") from _call_her_main_6246
                call play_music("chipper_doodle") from _call_play_music_238 # HERMIONE'S THEME.
                call her_main(".............","angry","base") from _call_her_main_6247
                call her_main("...","angry","down_raised") from _call_her_main_6248
                call her_main("well.... ah, I... better get to.... class... then...","angry","wink") from _call_her_main_6249
                m "See you tonight [hermione_name]."

            "\"You'll get 70.\"":
                $ current_payout = 70
                call her_main("Hmmmph...","annoyed","angryL") from _call_her_main_6250
                call her_main("Alright then, just don't expect me to show it to you!","angry","angry") from _call_her_main_6251
                m "So long as you wear it to class then you'll get your 70 points."
                ">You hand her the buttplug."
                call her_main("Will that be all [genie_name]?.","annoyed","annoyed") from _call_her_main_6252
                m "Yes [hermione_name], see you tonight."
                call her_main("{size=-5}(cheap bastard...){/size}","annoyed","angryL") from _call_her_main_6253

    
    else: # <================================================================================ NOT FIRST TIME
        if whoring <= 15 and buttplug_size == 1: # LEVEL 06 FIRST EVENT.
            $ buttplug_1_worn = True
            
            m "Today's favour shall be..."
            call her_main(".........","angry","base",xpos="right",ypos="base") from _call_her_main_6254
            m "Wearing your favorite little buttplug to class!"
            call her_main("...again?","angry","down_raised") from _call_her_main_6255
            m "Sure, why not?"
            m "And another fifty five house points for the \"Gryffindor\" house of course."
            call her_main("..........","annoyed","worriedL") from _call_her_main_6256
            m "So... Are you ok with that, [hermione_name]?"
            call her_main("I suppose so...","annoyed","angryL") from _call_her_main_6257
            ">You hand her the buttplug."
            m "Fantastic! See you after class."
        
        elif whoring <= 20 and buttplug_size == 1: # LEVEL 07
            $ buttplug_1_worn = True
            
            ">You pull out the large buttplug."
            m "Ready to try out the dragon yet?"
            stop music fadeout 1.0
            call her_main("What?","scream","wide_stare",xpos="right",ypos="base") from _call_her_main_6258
            call her_main("Of course not! That thing would tear me--","scream","angryCl") from _call_her_main_6259
            ">you pull out the small buttplug"
            m "How about this one then?"
            call her_main("Oh, ok then!","smile","happyCl",emote="06") from _call_her_main_6260
            m "You'll do it that easily?"
            call her_main("Well for fifty five house points I'd be crazy not to.","base","closed") from _call_her_main_6261
            call her_main("Plus I don't hate the way it feels","open","baseL") from _call_her_main_6262
            ">You hand her the buttplug."
            m "why don't you put it in now."
            call her_main("you want me to put it in now? in front of you!","scream","wide_stare") from _call_her_main_6263
            m "I don't see the harm in it."
            call her_main("well... it does save me having to visit the girls bathroom before class...","annoyed","down") from _call_her_main_6264
            call her_main("alright then, I'll do it... but I want an extra five points!","smile","baseL") from _call_her_main_6265
            m "Done."
            $ current_payout += 5
            call her_main("well... here goes.","smile","baseL") from _call_her_main_6266
            ">Hermione lifts her skirt and sticks it in rather slowly."
            
            call set_h_buttplug("plug_a_on") from _call_set_h_buttplug_5 #Updates clothing and body.
            
            call her_main("{image=textheart}ah{image=textheart}...","grin","ahegao") from _call_her_main_6267
            call her_main("i better head to class...","soft","squintL") from _call_her_main_6268
            m "See you tonight [hermione_name]."
            call her_main("{size=-5}({image=textheart}it feels so good{image=textheart}){/size}","grin","ahegao") from _call_her_main_6269
        
        elif whoring >= 21 and buttplug_size == 1: # LEVEL 08+
            $ buttplug_1_worn = True
            
            call play_music("chipper_doodle") from _call_play_music_239 # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "What do you think about wearing a buttpl-?"
            call her_main("I'll do it.","grin","baseL",xpos="right",ypos="base") from _call_her_main_6270
            m "You're eager."
            call her_main("well... I mean it is a lot of points and... i've sort of grown fond of how it feels...","open","down") from _call_her_main_6271
            m "Great. Go have fun then!"
            ">You hand her the buttplug."
            ">Hermione turns around and lifts her skirt giving you a full view as she inserts it."
            
            call set_h_buttplug("plug_a_on") from _call_set_h_buttplug_6 #Updates clothing and body.
            
            call her_main("{image=textheart}ah{image=textheart}...","grin","ahegao") from _call_her_main_6272
            call her_main("I will, [genie_name]. Thank you.","base","happyCl") from _call_her_main_6273

        elif whoring <= 19 and buttplug_size == 2: # LEVEL 06 FIRST EVENT.
            $ buttplug_2_worn = True
            
            m "Today my gracious request will be..."
            call her_main(".........","angry","base",xpos="right",ypos="base") from _call_her_main_6274
            m "That you wear everyone's favorite magical buttplug to class!"
            call her_main("...again?","angry","down_raised") from _call_her_main_6275
            m "why not? This will be the easiest fifty five points you'll ever earn!"
            call her_main("..........","annoyed","worriedL") from _call_her_main_6276
            m "Do you have a problem with it, [hermione_name]?"
            call her_main("I suppose not...","annoyed","angryL") from _call_her_main_6277
            ">You hand her the buttplug."
            m "Fantastic! See you after class."
        
        elif whoring <= 23 and buttplug_size == 2: # LEVEL 07
            if buttplug_2_question == False:
                $ buttplug_2_question = True
                ">You pull out the buttplug."
                m "Ready to try out the phoenix again?"
                call her_main("Oh, I suppose so...","soft","squintL",xpos="right",ypos="base") from _call_her_main_6278
                call her_main("But is it alright if I ask you something first?","open","down") from _call_her_main_6279
                m "What's that [hermione_name]"
                call her_main("Don't you worry about us getting caught?","annoyed","base") from _call_her_main_6280
                m "Why would I?"
                call her_main("Well it's just that making me wear something like this is drawing a lot of attention...","open","worriedL") from _call_her_main_6281
                call her_main("and what if someone realises that it's you who's making me do all this...","open","worried") from _call_her_main_6282
                m "and who is going to suspect the great albis dumbledorf?"
                call her_main("...I suppose no one...","annoyed","worriedL") from _call_her_main_6283
                m "Then don't worry about it. If anyone asks just tell them you're going through an exhibitionist stage."
                m "Speaking of which..."
                ">You hand her the buttplug."
                call her_main("Oh... right...","base","down") from _call_her_main_6284
                ">Hermione lifts her skirt and pushes it in gently, taking her time."
                
                call set_h_buttplug("plug_b_on") from _call_set_h_buttplug_7 #Updates clothing and body.
                
                call her_main("{image=textheart}{image=textheart}{image=textheart}ah{image=textheart}{image=textheart}{image=textheart}...","grin","ahegao") from _call_her_main_6285
                call her_main("i better... head to class... now...","open","baseL") from _call_her_main_6286
                m "See you tonight [hermione_name]."
                call her_main("{size=-5}({image=textheart}it's... so... big...{image=textheart}){/size}","grin","ahegao") from _call_her_main_6287
            else:
                ">You pull out the buttplug."
                m "Ready for the phoenix again?"
                call her_main("Oh, alright then...","open","down",xpos="right",ypos="base") from _call_her_main_6288
                call her_main("but if you pay me and additional 5 points I'll turn around as I put it in...","soft","squintL") from _call_her_main_6289
                menu:
                    "\"Done\"":
                        $ current_payout += 5
                        call her_main("thank you [genie_name], you won't regret it...","open","baseL") from _call_her_main_6290
                    "\"Fifty five is all I can do.\"":
                        m "Any more and people might get suspicious."
                        call her_main("hmmmm I suppose you're right...","annoyed","angryL") from _call_her_main_6291
                        call her_main("but as a present i'll show you anyway...","base","down") from _call_her_main_6292
                        call her_main("although you better appreciate it...","base","suspicious") from _call_her_main_6293
                        m "I'm sure I will."
                ">You hand her the buttplug."
                call her_main("well... here goes...","base","down") from _call_her_main_6294
                ">Hermione turns around, lifts her skirt and pushes it in gently, taking her time."
                
                call set_h_buttplug("plug_b_on") from _call_set_h_buttplug_8 #Updates clothing and body.
                
                call her_main("{image=textheart}{image=textheart}{image=textheart}ah{image=textheart}{image=textheart}{image=textheart}...","grin","ahegao") from _call_her_main_6295
                call her_main("i better... head to class... now...","soft","squintL") from _call_her_main_6296
                m "See you tonight [hermione_name]."
                call her_main("{size=-5}({image=textheart}it's... so... good...{image=textheart}){/size}","grin","ahegao") from _call_her_main_6297
            
        elif whoring >= 24 and buttplug_size == 2: # LEVEL 08+
            call play_music("chipper_doodle") from _call_play_music_240 # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "What do you think about wearing a buttpl-?"
            call her_main("I'll do it.","grin","baseL",xpos="right",ypos="base") from _call_her_main_6298
            m "You're eager. I haven't even said what one yet..."
            call her_main("oh... can it be the big one... with the long tail...","open","down") from _call_her_main_6299
            call her_main("please...","soft","squintL") from _call_her_main_6300
            m "well seeing as how you asked so nicely..."
            ">You hand her the buttplug."
            ">Hermione turns around and lifts her skirt giving you a full view as she inserts it."
            
            call set_h_buttplug("plug_b_on") from _call_set_h_buttplug_9 #Updates clothing and body.
                
            call her_main("{image=textheart}ah{image=textheart}...","grin","ahegao") from _call_her_main_6301
            call her_main("Thank you [genie_name]!","open","baseL") from _call_her_main_6302
            call her_main("{size=-5}({image=textheart}it feels so good... I might have to buy my own...{image=textheart}){/size}","grin","ahegao") from _call_her_main_6303

        elif buttplug_size == 3 and not buttplug_3_worn: # Large buttplug first time
            call play_music("chipper_doodle") from _call_play_music_241 # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "What do you think about wearing a buttpl-?"
            call her_main("I'll do it.","grin","baseL",xpos="right",ypos="base") from _call_her_main_6304
            m "You're eager. I haven't even said which one yet..."
            call her_main("oh... can it be the big one... with the long tail...","open","down") from _call_her_main_6305
            call her_main("please...","soft","squintL") from _call_her_main_6306
            m "well seeing as how you did ask for the big one..."
            ">You hand her the buttplug."
            call her_main("!!!","angry","down_raised") from _call_her_main_6307
            call her_main("This isn't the one I meant [genie_name]...","angry","down_raised") from _call_her_main_6308
            m "Didn't you ask for the big one?"
            call her_main("I did-","grin","ahegao") from _call_her_main_6309
            m "Well here's the {b}big{/b} one."
            call her_main("I didn't know you had one this big!","open","baseL") from _call_her_main_6310
            call her_main("I don't even think this will fit...","grin","ahegao") from _call_her_main_6311
            m "Never say never!"
            call her_main("You can't be serious!","grin","ahegao") from _call_her_main_6312
            call her_main("This thing is ridiculous!","grin","ahegao") from _call_her_main_6313
            m "You said the same thing about the smaller one."
            call her_main("that was different...","grin","ahegao") from _call_her_main_6314
            m "I have confidence in you! Besides, you were pretty great when you were taking my cock up your ass!"
            call her_main("[genie_name]!","grin","ahegao") from _call_her_main_6315
            m "Come on..."
            call her_main("This is too much sir! even your cock wasn't this {p}{b}thick{/b}...","grin","ahegao") from _call_her_main_6316
            m "Nothing a little spit won't solve!"
            call her_main("I think this is beyond spit, [genie_name]. Unless you have some sort of actual {i}lubricant{/i} in your possession I don't think I'll be letting this thing anywhere near me.","grin","ahegao") from _call_her_main_6317
            if gift_item_inv[12] >= 1:# anal lubricant
                $ buttplug_3_worn = True
                call play_music("playful_tension") from _call_play_music_242# SEX THEME.
                m "well it just so happens that I recently came across the solution to your problem."
                call her_main("Which is?","grin","ahegao") from _call_her_main_6318
                m "Here."
                ">You hand hermione the jar of anal lubricant."
                $ gift_item_inv[12] -= 1
                call her_main("!!!","grin","ahegao") from _call_her_main_6319
                call her_main("I wasn't serious [genie_name]!","grin","ahegao") from _call_her_main_6320
                m "Now, now. No one likes a liar."
                call her_main("I didn't promise anything! Besides, I didn't actually expect you to have a jar of lube in your desk.","grin","ahegao") from _call_her_main_6321
                m "I bought it for just such an occasion..."
                call her_main("...","grin","ahegao") from _call_her_main_6322
                call her_main("ugh... fine. I'll {b}try{/b} to fit it in.","grin","ahegao") from _call_her_main_6323
                call her_main("but I'm not promising anything!","grin","ahegao") from _call_her_main_6324
                m "That's all I ask."
                ">You hand hermione the large buttplug."
                call her_main("I still don't think this is going to work...","grin","ahegao") from _call_her_main_6325
                ">Hermione slowly coats the massive buttplug with lube."
                call her_main("There's barely even enough here to cover it...","grin","ahegao") from _call_her_main_6326
                call her_main("(There's no way this thing will fit.)","grin","ahegao") from _call_her_main_6327
                ">Hermione slowly places the lubed up buttplug to her anus."
                call her_main("I'm telling you [genie_name], this isn't going to-","grin","ahegao") from _call_her_main_6328
                call her_main("{size=+10}!!!{/size}","grin","ahegao") from _call_her_main_6329
                call her_main("{size=+10}It's moving!{/size}","grin","ahegao") from _call_her_main_6330
                m "Really?"
                call her_main("{size=+5}ugh...{/size}","grin","ahegao") from _call_her_main_6331
                call her_main("{size=+5}it's forcing it's way inside me....{/size}","grin","ahegao") from _call_her_main_6332
                call her_main("{size=+5}it's stretching me out from the inside... [genie_name].{/size}","grin","ahegao") from _call_her_main_6333
                call her_main("ah...","grin","ahegao") from _call_her_main_6334
                call her_main("it's...{p}it's...","grin","ahegao") from _call_her_main_6335
                $ hermione_dribble = True
                call her_main("{size=+5}incredible!{/size}","grin","ahegao") from _call_her_main_6336
                ">You hear an audible pop as the buttplug forces it's way inside hermione."
                
                call set_h_buttplug("plug_c_on") from _call_set_h_buttplug_10 #Updates clothing and body.
                
                call her_main(".............","grin","ahegao") from _call_her_main_6337
                m "Are you alright [hermione_name]?"
                call her_main("..........................","grin","ahegao") from _call_her_main_6338
                call her_main("ah... y-yes...","grin","ahegao") from _call_her_main_6339
                m "Fantastic! I'll see you after class then."
                call her_main(".............","grin","ahegao") from _call_her_main_6340
                ">Hermione slowly leaves your office, barely able to walk in a straight line."
                pass
            else:
                m "afraid not..."
                call her_main("well then i think I better be off to class then.","grin","ahegao") from _call_her_main_6341
                call her_main("{size=-2}unless {size=-2}you {size=-2}have {size=-2}the {size=-2}smaller {size=-2}one.{/size}{image=textheart}","grin","ahegao") from _call_her_main_6342
                m "It just so happens that I do."
                ">You hand her the buttplug."
                ">Hermione turns around and lifts her skirt giving you a full view as she inserts it."
                
                call set_h_buttplug("plug_b_on") from _call_set_h_buttplug_11 #Updates clothing and body.
                
                call her_main("{image=textheart}ah{image=textheart}...","grin","ahegao") from _call_her_main_6343
                call her_main("Thank you [genie_name]!","open","baseL") from _call_her_main_6344
                call her_main("{size=-5}({image=textheart}it feels so good... I might have to buy my own...{image=textheart}){/size}","grin","ahegao") from _call_her_main_6345
                m "(I'll have to see if those Weasley boys have anything that could help...)"

        elif buttplug_size == 3: # Large buttplug repeat
            call play_music("chipper_doodle") from _call_play_music_243 # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "how do you feel about wearing another buttplug to class today?"
            call her_main("...","grin","baseL",xpos="right",ypos="base") from _call_her_main_6346
            call her_main("which one?","grin","baseL") from _call_her_main_6347
            m "how about the big one again?"
            call her_main("really?","open","down") from _call_her_main_6348
            call her_main("do i have to?","soft","squintL") from _call_her_main_6349
            m "you didn't seem to hate wearing it last time..."
            call her_main("...","open","down") from _call_her_main_6350
            call her_main("{size=-5}alright then...{/size}","open","down") from _call_her_main_6351
            ">You hand her the buttplug."
            ">Hermione turns around and lifts her skirt giving you a full view as she inserts it."
            ">You see it magically worm it's way inside her eager hole."
            
            call set_h_buttplug("plug_c_on") from _call_set_h_buttplug_12 #Updates clothing and body.
            
            call her_main("{image=textheart}ah{image=textheart}ah...","grin","ahegao") from _call_her_main_6352
            call her_main("Thank you [genie_name]!","open","baseL") from _call_her_main_6353
            call her_main("{size=-5}({image=textheart}it feels so good... I might have to buy my own...{image=textheart}){/size}","grin","ahegao") from _call_her_main_6354

    $ hg_ps_Buttplug_OBJ.inProgress = True
    
    jump hg_pr_transition_block
    if buttplug_size == 2:
        
        call set_h_buttplug("plug_b_on") from _call_set_h_buttplug_13 #Updates clothing and body.
        
    if buttplug_size == 3:
        
        call set_h_buttplug("plug_c_on") from _call_set_h_buttplug_14 #Updates clothing and body.
        
    jump day_main_menu
    
label hg_ps_Buttplug_complete:
    
    call play_sound("door") from _call_play_sound_203
    call her_walk("door","mid",2) from _call_her_walk_124
    pause.5
    
    if whoring <= 15 and buttplug_size == 1: # LEVEL 06                    
        if one_out_of_three == 1: ### EVENT (A)
            m "[hermione_name], how did it go?"
            call play_music("chipper_doodle") from _call_play_music_244 # HERMIONE'S THEME.
            show screen blktone
            $ sc34CG(1, 8)
            call her_main("It was awful... of course...","annoyed","frown",xpos="base",ypos="base") from _call_her_main_6355
            m "Just tell me what happened, [hermione_name]..."
            call her_main("I've never been so uncomfortable in my life [genie_name]!","disgust","glance") from _call_her_main_6356
            call her_main("I wasn't able to focus on anything all day!","annoyed","annoyed") from _call_her_main_6357
            m "Why's that?"
            call her_main("Whenever I was sitting down in class it just kept prodding me...","annoyed","angryL") from _call_her_main_6358
            her "So naturally I had to adjust the way I was sitting, [genie_name]..."
            $ sc34CG(1, 9)
            call her_main("but that just made it worse...","annoyed","angryL") from _call_her_main_6359
            m "Do you think anyone else noticed you?"
            call her_main("I've got no idea...","annoyed","annoyed") from _call_her_main_6360
            $ sc34CG(1, 10)
            call her_main("I could hardly think straight... Let alone notice other people.","annoyed","annoyed") from _call_her_main_6361
            m "So it felt good then?"
            call her_main("Good?","open","base") from _call_her_main_6362
            $ sc34CG(1, 12)
            call her_main("If you call getting your... butt teased all day good...","annoyed","down") from _call_her_main_6363
            call her_main("Then yes, I suppose it did...","annoyed","ahegao") from _call_her_main_6364
            $ sc34CG(1, 13)
            call her_main("Still... being this distracted during class could really damage my grades...","angry","base") from _call_her_main_6365
            m "I wouldn't worry about that. Just think of Gryffindor!"
            hide screen sccg
            call her_main("Speaking of that...","annoyed","annoyed",xpos="right",ypos="base",trans="fade") from _call_her_main_6366
            m "Oh yes, quite right."
        
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], how did it go?"
            show screen blktone
            call her_main("It went well, [genie_name]...","open","base",xpos="right",ypos="base") from _call_her_main_6367
            call play_music("playful_tension") from _call_play_music_245# SEX THEME.
            her "Barely anybody noticed that I was wearing it..."
            call her_main("...Except for a few girls from Ravenclaw...","open","base",cheeks="blush") from _call_her_main_6368
            m "What happened?"
            call her_main("I was walking down the hall, on my way to potions class...","open","closed") from _call_her_main_6369
            call her_main("And suddenly a gust of wind came and blew my skirt up...","upset","wink") from _call_her_main_6370
            m "A gust of wind? inside?"
            call her_main("It must have been from a window...","soft","baseL") from _call_her_main_6371
            call her_main("Anyway the three girls walking behind me may have... seen it.","open","down") from _call_her_main_6372
            m "Did they say anything to you?"
            call her_main("No... But I did hear them giggling afterwards...","clench","down_raised") from _call_her_main_6373
            m "Well, it sounds like a job well done..."
        
        elif one_out_of_three == 3: ### EVENT (C) Event level: 01.
            m "[hermione_name], how did it go?"
            call play_music("chipper_doodle") from _call_play_music_246 # HERMIONE'S THEME.
            show screen blktone
            call her_main("Awful, [genie_name]. Simply awful...","scream","worriedCl",xpos="right",ypos="base") from _call_her_main_6374
            m "What happened?"
            call her_main("Moaning Myrtle happened!","normal","worriedCl") from _call_her_main_6375
            m "Moaning Mittle?"
            call her_main("That pesky little ghost!","annoyed","angryL") from _call_her_main_6376
            call her_main("This thing left me so frustrated that in my free period I went to the girls toilets to...","annoyed","angryL") from _call_her_main_6377
            call her_main("Relieve myself...","annoyed","worriedL") from _call_her_main_6378
            call her_main("When all of a sudden that annoying ghost poked her head through the door!","scream","angryCl") from _call_her_main_6379
            call her_main("As it if wasn't bad enough that she saw me...","open","down") from _call_her_main_6380
            call her_main("She then started yelling \'Hermione has a buttplug\' to everyone in the toilets!","scream","angry",emote="01") from _call_her_main_6381
            call her_main("Luckily the stalls where empty! Imagine if they weren't!","annoyed","annoyed") from _call_her_main_6382
            m "Well, it certainly sounds like you've earned your points."
    
    elif whoring <= 20 and buttplug_size == 1: # LEVEL 07                    
        if one_out_of_three == 1: ### EVENT (A)
            call play_music("chipper_doodle") from _call_play_music_247 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Of course.","open","base",xpos="right",ypos="base") from _call_her_main_6383
            m "Did anyone notice?"
            call her_main("Yes... well I might have...","base","down") from _call_her_main_6384
            call her_main("shown someone...","base","glance") from _call_her_main_6385
            her "I was in the library fetching some books when I saw Luna..."
            her "She was reading at a desk..."
            call her_main("So I decided to walk over to her and have a chat...","grin","baseL") from _call_her_main_6386
            call her_main("She was talking about something nonsensical...","base","baseL") from _call_her_main_6387
            her "And I figured that if she saw it..."
            her "no one would believe her..."
            m "alright..."
            call her_main("So I feigned dropping my quill...","grin","baseL") from _call_her_main_6388
            m "Go on..."
            call her_main("then I turned around in front of her...","base","down") from _call_her_main_6389
            her "and bent over..."
            her "...keeping my knees straight..."
            call her_main("...giving her a full view...","base","ahegao_raised") from _call_her_main_6390
            m "I see..."
            m "Did she say anything?"
            call her_main("No, [genie_name]...","soft","squintL") from _call_her_main_6391
            her "But when I turned back around she didn't make eye contact..."
            m "Hm..."
            call her_main("I don't think I've seen anyone blush so hard...","base","glance") from _call_her_main_6392
            m "Well it sounds like you've earned your points and then some."
        
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            $ sc34CG(1, 9, 1)
            call her_main("I did, [genie_name]...","open","closed",xpos="base",ypos="base") from _call_her_main_6393
            call her_main("Although I am still not sure how I feel about all of this...","annoyed","worriedL") from _call_her_main_6394
            $ sc34CG(1, 11, 1)
            call her_main("It's starting to really affect my grades...","annoyed","worriedL") from _call_her_main_6395
            call her_main("I couldn't even tell you what potions we were taught today...","open","base") from _call_her_main_6396
            call play_music("playful_tension") from _call_play_music_248# SEX THEME.
            call her_main("Me, Hermione Granger...","open","down") from _call_her_main_6397
            $ sc34CG(1, 12, 1)
            call her_main("Not learning in class...","angry","down_raised") from _call_her_main_6398
            m "Well you could try relieving yourself in between lessons."
            $ sc34CG(1, 13, 1)
            call her_main("Oh, i've tried that... but it doesn't work...","angry","base") from _call_her_main_6399
            her "It just makes the next class harder..."
            $ sc34CG(1, 12, 1)
            call her_main("today, After potions I went to my room to... calm myself...","open","baseL") from _call_her_main_6400
            call her_main("But it just made herbology worse...","open","down") from _call_her_main_6401
            $ sc34CG(1, 11, 1)
            call her_main("I was forced into touching myself in the middle of class...","clench","down_raised") from _call_her_main_6402
            call her_main("Do you think anyone noticed, [genie_name]?","open","squint",cheeks="blush") from _call_her_main_6403
            $ sc34CG(1, 9, 1)
            
            menu:
                "\"What? Of course not, [hermione_name]!\"":
                    $ sc34CG(1, 8, 2)
                    call her_main("..............","base","baseL",cheeks="blush") from _call_her_main_6404
                    call her_main("You are right, [genie_name]...","base","down") from _call_her_main_6405
                    her "I was very discreet..."
                    $ sc34CG(1, 12, 3)
                    call her_main("very quiet...","soft","ahegao") from _call_her_main_6406
                    call her_main("barely making a sound...","grin","baseL") from _call_her_main_6407
                    hide screen sccg
                    call her_main("[genie_name], can I get paid now, please?","base","glance",xpos="right",ypos="base",trans="fade") from _call_her_main_6408
                    her "......"
                "\"Of course they did!\"":
                    $ sc34CG(1, 13, 2)
                    m "Do you honestly believe that no one noticed you touching yourself?"
                    call her_main("I was afraid that you would say that, [genie_name]...","mad","worriedCl",tears="soft_blink") from _call_her_main_6409
                    m "You were surrounded by people!"
                    call her_main("........","mad","worriedCl",tears="soft_blink") from _call_her_main_6410
                    hide screen sccg
                    call her_main("[genie_name], can I get paid now, please?","angry","base",tears="soft",xpos="right",ypos="base",trans="fade") from _call_her_main_6411
            m "Certainly."
        
        elif one_out_of_three == 3: ### EVENT (C)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            $ sc34CG(1, 11)
            call her_main("Yes, [genie_name]. I did.","open","closed",xpos="base",ypos="base") from _call_her_main_6412
            m "Great. Tell me more."
            call play_music("playful_tension") from _call_play_music_249# SEX THEME.
            call her_main("Well, there's not much to tell...","open","base") from _call_her_main_6413
            $ sc34CG(1, 12)
            her "I attended classes..."
            her "tried to take notes."
            her "all in all it was a fairly regular day..."
            $ sc34CG(1, 13)
            call her_main("Well as regular as it could have been with a plug up my butt.","annoyed","angryL") from _call_her_main_6414
            m "and Nobody noticed?"
            call her_main("I don't think so, [genie_name].","annoyed","annoyed") from _call_her_main_6415
            $ sc34CG(1, 11)
            m "Well I suppose something interesting can't happen everyday."
            hide screen sccg
            call her_main("...","annoyed","baseL",xpos="right",ypos="base",trans="fade") from _call_her_main_6416
            
    
    elif whoring >= 21 and buttplug_size == 1: # LEVEL 08+                    
        if one_out_of_three == 1: ### EVENT (A)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes I did, [genie_name].","base","base",xpos="right",ypos="base") from _call_her_main_6417
            m "Well? How was your day?"
            call her_main("great, [genie_name]...","base","ahegao_raised") from _call_her_main_6418
            m "go on..."
            call play_music("playful_tension") from _call_play_music_250# SEX THEME.
            $ sc34CG(1, 14, 1)
            call her_main("Well I've worked out how to deal with this thing being in me all day...","soft","squintL",xpos="base",ypos="base") from _call_her_main_6419
            m "Really? And how is that?"
            call her_main("before now I've been going around it the wrong way...","open","baseL") from _call_her_main_6420
            call her_main("I just tried to ignore it...","open","closed") from _call_her_main_6421
            her "and pay attention in class..."
            call her_main("But that didn't work at all...","upset","wink") from _call_her_main_6422
            call her_main("I was just too... distracted...","base","down") from _call_her_main_6423
            $ sc34CG(1, 15, 2)
            call her_main("So I thought to myself that I've just got to focus on it...","base","ahegao_raised") from _call_her_main_6424
            $ sc34CG(1, 16, 3)
            call her_main("block out everything else...","base","down") from _call_her_main_6425
            $ sc34CG(1, 17, 2)
            call her_main("...embrace it...","grin","dead") from _call_her_main_6426
            m "and how did you do that?"
            call her_main("well if I rock my hips while I'm sitting in class it's almost enough...","base","glance") from _call_her_main_6427
            $ sc34CG(1, 16, 3)
            call her_main("but if I sit of the edge of my chair while I rock my hips...","base","suspicious") from _call_her_main_6428
            $ sc34CG(1, 17, 2)
            call her_main("{image=textheart}{image=textheart}{image=textheart}","soft","ahegao") from _call_her_main_6429
            m "So you worked out how to pleasure yourself in class."
            call her_main("I did [genie_name].","base","down") from _call_her_main_6430
            her "Although I worry that it will really start to affect my grades..."
            m "Well I'm sure that missing one class a day is something you can catch up on."
            $ sc34CG(1, 15, 2)
            call her_main("only One?","angry","wink") from _call_her_main_6431
            m "You mean to say that you spent all your class time pleasuring yourself?"
            $ sc34CG(1, 17, 2)
            call her_main("..........","soft","ahegao") from _call_her_main_6432
            hide screen sccg
            call her_main(xpos="right",ypos="base",trans="fade") from _call_her_main_6433
            m "Nice work, [hermione_name]."
        
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes I did, [genie_name].","base","base",xpos="right",ypos="base") from _call_her_main_6434
            call her_main("But, umm...","open","worried") from _call_her_main_6435
            m "...?"
            call her_main("Well, I may have gotten a bit more attention than I had hoped for...","disgust","down_raised") from _call_her_main_6436
            call her_main("...............","clench","down_raised") from _call_her_main_6437
            m "Tell me what happened, [hermione_name]."
            call play_music("playful_tension") from _call_play_music_251# SEX THEME.
            call her_main("I might have had a few photos taken...","open","down") from _call_her_main_6438
            m "Photos..."
            call her_main("Well I was in the library minding my own business...","annoyed","closed") from _call_her_main_6439
            her "When I went to get a copy of Zygmunt Budge's book of potions."
            call her_main("as it was on the bottom shelf I had to kneel down to reach it...","annoyed","base") from _call_her_main_6440
            call her_main("When all of a sudden I heard the flash of a camera!","annoyed","angryL") from _call_her_main_6441
            her "I turned around and there was Colin Creevey..."
            her "with the biggest grin on his face!"
            m "You let your photo be taken?!"
            call her_main("I didn't let anything of the sort happen! It was without my consent!","scream","angry",emote="01") from _call_her_main_6442
            call her_main("I even made him promise not to show anyone the photo...","open","down") from _call_her_main_6443
            her "...in exchange I did have to let him take a few more..."
            her "but he insisted that he wouldn't show anyone else..."
            m "And you believe him?"
            call her_main("Of course [genie_name], he's a Gryffindor.","annoyed","closed") from _call_her_main_6444
            call her_main("Although the thought did cross my mind.","open","down") from _call_her_main_6445
            call her_main("What if he were to distribute the photos around the school.","clench","down_raised") from _call_her_main_6446
            call her_main("Imagine everyone looking at photos of me...","open","baseL") from _call_her_main_6447
            her "Everyone would know what I was wearing..."
            call her_main("Any time someone saw me they'd think about whether or not it was in...","base","down") from _call_her_main_6448
            m "That's quite the thought process."
            call her_main("Yes, well I certainly don't want that happening...","base","suspicious") from _call_her_main_6449
            m "I'm sure..."
            call her_main("","base","glance") from _call_her_main_6450
            m "It sounds like a job well done [hermione_name]."
        
        elif one_out_of_three == 3: 
            call play_music("chipper_doodle") from _call_play_music_252 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes, I did [genie_name]...","base","suspicious",xpos="right",ypos="base") from _call_her_main_6451
            m "Did anyone notice?"
            her "maybe a few third years..."
            m "well go on."
            call her_main("It was the stairs...","base","glance") from _call_her_main_6452
            her "I may have gotten a little carried away with myself..."
            m "What happened, [hermione_name]?"
            call her_main("Well as I was walking to divination class I ended up in front of a group of third year students...","base","suspicious") from _call_her_main_6453
            call her_main("And seeing as how they were behind me on the stairs they may have been able to... see it.","base","glance") from _call_her_main_6454
            m "So you intentionally showed it to a group of boys? You don't expect me to grant you extra points for showing them, do you?"
            call her_main("Of course not, [genie_name].","base","baseL",cheeks="blush") from _call_her_main_6455
            m "Then why do it?"
            call her_main("Well, it just sort of just happened...","open","squint",cheeks="blush") from _call_her_main_6456
            call her_main("plus the look on their faces when they noticed it...","grin","dead") from _call_her_main_6457
            call her_main("they could barely hide their...","soft","ahegao") from _call_her_main_6458
            m "So you like being seen then?"
            call her_main("well...","open","baseL") from _call_her_main_6459
            m "Well done, [hermione_name]."
            call her_main("","base","down") from _call_her_main_6460

    elif whoring <= 19 and buttplug_size == 2: # LEVEL 06                    
        if one_out_of_three == 1: ### EVENT (A)
            m "[hermione_name], how was it?"
            call play_music("chipper_doodle") from _call_play_music_253 # HERMIONE'S THEME.
            show screen blktone
            call her_main("It was awful... simply awful...","annoyed","frown",xpos="right",ypos="base") from _call_her_main_6461
            m "what happened, [hermione_name]..."
            call her_main("It was that nasty professor snape, [genie_name]!","annoyed","angryL") from _call_her_main_6462
            call her_main("I've never been so embarassed in my life!","annoyed","annoyed") from _call_her_main_6463
            m "What did he do?"
            call her_main("Well in potions class I may have corrected him about the proper way to crush a Sopophorous bean...","annoyed","angryL") from _call_her_main_6464
            her "so he made me stand out the front and show him the \'correct\' way..."
            call her_main("and what's worse is that he made me do it facing away from the class...","annoyed","annoyed") from _call_her_main_6465
            m "Do you think anyone saw it?"
            call her_main("Everyone saw it!","disgust","down_raised") from _call_her_main_6466
            call her_main("I could barely even crush the bean my legs were shaking that hard...","clench","down_raised") from _call_her_main_6467
            m "Well it sounds like you earned your points."
            call her_main(".......","annoyed","down") from _call_her_main_6468
        
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], how did it go?"
            show screen blktone
            call her_main("It went well, [genie_name]...","open","base",xpos="right",ypos="base") from _call_her_main_6469
            call play_music("playful_tension") from _call_play_music_254# SEX THEME.
            her "A group of second years from \"hufflepuff\" even complemented me on it..."
            call her_main("...they said that it looked cute...","grin","baseL") from _call_her_main_6470
            m "did anything else happen?"
            call her_main("well seeing as how they were so nice...","base","down") from _call_her_main_6471
            call her_main("I might have flicked my skirt up for them...","soft","squintL") from _call_her_main_6472
            m "you showed it to them?"
            call her_main("well they were so kind...","open","baseL") from _call_her_main_6473
            call her_main("and they could already see most of it...","base","down") from _call_her_main_6474
            m "Did they say anything to you?"
            call her_main("No... But the looks on their faces...","base","glance") from _call_her_main_6475
            m "Well, it sounds like a job well done..."
        
        elif one_out_of_three == 3: ### EVENT (C) cat swatting it
            label buttplug_magic_show:
                pass
            $ buttplug_magic_known = True
            m "[hermione_name], how did it go?"
            call play_music("chipper_doodle") from _call_play_music_255 # HERMIONE'S THEME.
            show screen blktone
            call her_main("what on earth did you do to this thing?!","scream","worriedCl",xpos="right",ypos="base") from _call_her_main_6476
            m "What happened?"
            call her_main("Why did you not tell me this \'thing\' was cursed!","normal","worriedCl") from _call_her_main_6477
            m "Cursed?"
            call her_main("It vibrates!","annoyed","angryL") from _call_her_main_6478
            m "Really? When?"
            call her_main("when something else touches it...","annoyed","angryL") from _call_her_main_6479
            m "Wouldn't your skirt set it off then?"
            call her_main("I think it has to be alive...","annoyed","worriedL") from _call_her_main_6480
            call her_main("All I know is that when my cat crookshanks swatted at it went off!","scream","angryCl") from _call_her_main_6481
            m "How bad was it?"
            call her_main("It was ridiculous! I was barely able to stand...","open","worriedCl") from _call_her_main_6482
            call her_main("but then crookshanks thought it was some sort of game... he wouldn't leave it alone...","shock","worriedCl") from _call_her_main_6483
            call her_main("the vibrations were so intense that my knees gave out and I collapsed onto my bed!","angry","down_raised") from _call_her_main_6484
            call her_main("then he just played with it for hours...","angry","wink") from _call_her_main_6485
            m "are you still up for wearing it in the future?"
            call her_main("I suppose... So long as I know how it works now.","upset","closed") from _call_her_main_6486
            call her_main("I'll just have to keep it away from crookshanks...","angry","down_raised") from _call_her_main_6487
            call her_main("{size=-6}or not...{/size}","soft","ahegao") from _call_her_main_6488
            m "Well good work then [hermione_name]"
    
    elif whoring <= 23 and buttplug_size == 2: # LEVEL 07                    
        if one_out_of_three == 1: ### EVENT (A) luna plays with it in the library
            if not buttplug_magic_known:
                jump buttplug_magic_show
            call play_music("chipper_doodle") from _call_play_music_256 # HERMIONE'S THEME.
            m "[hermione_name], did you have fun?"
            show screen blktone
            call her_main("I suppose you could say that.","base","down",xpos="right",ypos="base") from _call_her_main_6489
            m "Anything interesting happen?"
            call her_main("Yes... well I might have...","base","down") from _call_her_main_6490
            call her_main("had someone...","base","worriedCl") from _call_her_main_6491
            call her_main("touch it...","base","glance") from _call_her_main_6492
            m "hmmmm..."
            call her_main("It was luna lovegood again.","grin","baseL") from _call_her_main_6493
            call her_main("We ended up sitting next to each other in class.","soft","baseL") from _call_her_main_6494
            her "we were talking about school, clothes..."
            m "Yes, yes, spit it out..."
            call her_main("well she said that she thought my tail was cute...","grin","baseL") from _call_her_main_6495
            m "Go on..."
            call her_main("then she asked so politely if she could touch it...","base","down") from _call_her_main_6496
            call her_main("I could hardly say no...","open","baseL") from _call_her_main_6497
            call her_main("so I... let her spend the rest of the lesson... playing with it...","soft","squintL") from _call_her_main_6498
            m "I see..."
            m "Did she realise what was happening?"
            call her_main("maybe... it felt so good that it was hard to keep it hidden.","soft","ahegao") from _call_her_main_6499
            her "But I think that just made her want to touch it more..."
            m "Hm..."
            call her_main("I don't think I've ever had a better lesson...","grin","dead") from _call_her_main_6500
            m "Well it sounds like you've earned your points and then some."
        
        elif one_out_of_three == 2: ### EVENT (B) 
            if not buttplug_magic_known:
                jump buttplug_magic_show
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("I did, [genie_name].","open","closed",xpos="right",ypos="base") from _call_her_main_6501
            call her_main("Only... ehm...","grin","baseL") from _call_her_main_6502
            m "What is it this time [hermione_name]?"
            call her_main("Well... you know my friend...","base","base") from _call_her_main_6503
            her "Ginny Weasley..."
            call her_main("well I told her about the tail...","base","baseL",cheeks="blush") from _call_her_main_6504
            her "and how it worked and well..."
            m "Just say it, [hermione_name]."
            call her_main("Well, we decided to skip herbology class together...","open","baseL") from _call_her_main_6505
            call play_music("playful_tension") from _call_play_music_257# SEX THEME.
            call her_main("And then she sort of grabbed it...","grin","ahegao") from _call_her_main_6506
            call her_main("And she just played with it so aggressively...","grin","dead") from _call_her_main_6507
            her "I was a mess afterwards..."
            g9 "And did you return the favour?"
            if touched_by_boy == True:
                call her_main("Err... maybe...","open","squint",cheeks="blush") from _call_her_main_6508
                m "What did you do?"
                call her_main("well I don't want to say too much [genie_name].","base","baseL",cheeks="blush") from _call_her_main_6509 # :)
                her "but after she saw what it was doing to me..."
                her "she insisted that I let her have a go..."
                call her_main("and that's all I'll say...","base","down") from _call_her_main_6510 # :)
                m "Hmmmm, well you did earn your points [hermione_name], even if you are secretive about it..."
            else:
                call her_main("...No.","open","down") from _call_her_main_6511
                m "Why not?"
                call her_main("well I don't mind letting her touch the tail [genie_name].","annoyed","base") from _call_her_main_6512 # :)
                her "but anything else..."
                m "Very good [hermione_name]..."
        
        elif one_out_of_three == 3: ### EVENT (C) called a slut by slytherin
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes, [genie_name]. I did.","annoyed","angryL",xpos="right",ypos="base") from _call_her_main_6513
            m "Great. Tell me more."
            call play_music("playful_tension") from _call_play_music_258# SEX THEME.
            call her_main("Well, there's not much to tell...","open","down") from _call_her_main_6514
            her "I attended classes..."
            her "studied for the upcoming potions exam..."
            call her_main("it was a normal day except for a group of those nasty \"slytherin\" tramps...","annoyed","angryL") from _call_her_main_6515
            call her_main("I was minding my business on the way to class when they called me a \"butt slut\".","angry","down_raised") from _call_her_main_6516
            m "did you say anything back to them?"
            call her_main("and sink to their level...","annoyed","angryL") from _call_her_main_6517
            m "Well I suppose it's for the best."
            
    
    elif whoring >= 24 and buttplug_size == 2: # LEVEL 08+                    
        if one_out_of_three == 1: ### EVENT (A) groped by first years
            if not buttplug_magic_known:
                jump buttplug_magic_show
            m "[hermione_name], how was your day?"
            show screen blktone
            call her_main("Awful, I was attacked by a group of rabid students, [genie_name].","scream","angryCl",xpos="right",ypos="base") from _call_her_main_6518
            m "Attacked? By How many?"
            call her_main("six first years, [genie_name]...","annoyed","angry") from _call_her_main_6519
            m "you were attacked by first years?"
            call play_music("playful_tension") from _call_play_music_259# SEX THEME.
            call her_main("I may have been exaggerating slightly...","open","worriedL") from _call_her_main_6520
            m "what happened?"
            call her_main("well I was sitting in the library, minding my own business...","annoyed","angryL") from _call_her_main_6521
            call her_main("when all of a sudden a group of first year students came from nowhere asking me all these questions...","angry","worriedCl") from _call_her_main_6522
            call her_main("\"is it fluffy\"...","annoyed","angryL") from _call_her_main_6523
            call her_main("\"why are you wearing it\"...","angry","down_raised") from _call_her_main_6524
            call her_main("\"does it feel nice\"...","base","down") from _call_her_main_6525
            call her_main("\"can we touch it\"...","base","down") from _call_her_main_6526
            call her_main("\"can you make it wag\"...","angry","wink") from _call_her_main_6527
            m "what did you do?"
            call her_main("well I made them promise to keep quiet about it...","upset","closed") from _call_her_main_6528
            call her_main("but in exchange I may have had to let them touch it...","open","down") from _call_her_main_6529
            call her_main("{image=textheart}{image=textheart}{image=textheart}","soft","ahegao") from _call_her_main_6530
            m "So you let a group of innocent first years touch your buttplug..."
            call her_main("It sounds sinister when you put it like that.","annoyed","angryL") from _call_her_main_6531
            her "All I did was take them to a secluded part of the library and let them touch my tail..."
            m "Well that's alright then..."
            call her_main(".......","base","down") from _call_her_main_6532
            m "So did you enjoy it?"
            call her_main("..........","angry","base") from _call_her_main_6533
            call her_main("Truthfully [genie_name].... It was the most one of the most pleasurable experiences of my life...","grin","dead") from _call_her_main_6534
            call her_main("all their hands touching it...","soft","ahegao") from _call_her_main_6535
            call her_main("taking turns...","grin","ahegao") from _call_her_main_6536
            call her_main("all the while it was vibrating away...","base","down") from _call_her_main_6537
            call her_main("I nearly passed out.","silly","dead") from _call_her_main_6538
            call her_main("I even tried to make them stop...","silly","ahegao") from _call_her_main_6539
            call her_main("but they just kept going...","grin","ahegao") from _call_her_main_6540
            m "Nice work, [hermione_name]."
        
        elif one_out_of_three == 2: ### EVENT (B) glory hole with astoria
            if not buttplug_magic_known:
                jump buttplug_magic_show
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes I did, [genie_name]...","base","base",xpos="right",ypos="base") from _call_her_main_6541
            call her_main("Did you know there are holes between the stalls in the girls bathroom?","soft","base") from _call_her_main_6542
            m "i did not, but What does that have to do with your buttplug?"
            call her_main("Well, I noticed that the hole is the same height as the tail...","grin","baseL") from _call_her_main_6543
            call her_main("...............","grin","worriedCl") from _call_her_main_6544
            m "go on, [hermione_name]."
            call play_music("playful_tension") from _call_play_music_260# SEX THEME.
            call her_main("I might have put it through...","base","down") from _call_her_main_6545
            m "what?"
            call her_main("Well I was in the stall finishing up...","base","baseL") from _call_her_main_6546
            her "When a girl entered the other stall."
            call her_main("I wasn't sure but I thought that it may have been a \"slytherin\"...","upset","wink") from _call_her_main_6547
            call her_main("So I decided to press my cheeks to the wall and stick my tail through!","smile","baseL") from _call_her_main_6548
            m "did they touch it?"
            call her_main("not immediately...","base","baseL") from _call_her_main_6549
            call her_main("but after I gave it a little wiggle she eventually came around...","grin","baseL") from _call_her_main_6550
            call her_main("she was curious at first but eventually she started to really play with it...","open","baseL") from _call_her_main_6551
            call her_main("stroking it... flicking it... I even think she may have licked it...","soft","ahegao") from _call_her_main_6552
            her "...imagine that... a slytherin, licking something that was inside my..."
            her "It was incredible... I could barely stand while it happened..."
            m "did you find out who it was?"
            call her_main("I did [genie_name].","open","worried") from _call_her_main_6553
            call her_main("It was at lunch, in the great hall.","open","closed") from _call_her_main_6554
            call her_main("I was walking past the slytherin table on my way to sit down...","open","closed") from _call_her_main_6555
            call her_main("when I saw that little... vixen, astoria greengrass.","base","suspicious") from _call_her_main_6556
            her "she couldn't take her eyes off of it..."
            call her_main("imagine that... astoria greengrass... pureblood, licking my...","grin","ahegao") from _call_her_main_6557
            call her_main("{image=textheart}........{image=textheart}","soft","ahegao") from _call_her_main_6558
            m "It sounds like you've earned your points today then [hermione_name]."
            call her_main("...{size=-7}(I would have done this for free...){/size}","base","down") from _call_her_main_6559
        
        elif one_out_of_three == 3: 
            call play_music("chipper_doodle") from _call_play_music_261 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes, I did [genie_name]...","base","suspicious",xpos="right",ypos="base") from _call_her_main_6560
            m "Anything interesting happen?"
            her "do you know that Patil twins [genie_name]?"
            m "no but do continue."
            call her_main("well they were walking down the hall behind me...","base","glance") from _call_her_main_6561
            her "I swear I could hear them whispering to each other..."
            call her_main("and I thought I may as well give them something to talk about...","base","suspicious") from _call_her_main_6562
            call her_main("So I stopped, kept my knees straight and bent over as far as I could...","base","glance") from _call_her_main_6563
            m "You exposed yourself just like that?"
            call her_main(".......","base","baseL",cheeks="blush") from _call_her_main_6564
            m "Very good, [hermione_name]!"
            
    elif buttplug_size == 3:                 
        if one_out_of_three == 1: #Groped by first years again...
            m "[hermione_name], how was your day?"
            show screen blktone
            call her_main("Awful, I was attacked by a group of rabid students, [genie_name].","scream","angryCl",xpos="right",ypos="base") from _call_her_main_6565
            m "Attacked? By How many?"
            call her_main("six first years, [genie_name]...","annoyed","angry") from _call_her_main_6566
            m "you were attacked by first years?"
            call play_music("playful_tension") from _call_play_music_262# SEX THEME.
            call her_main("I may have been exaggerating slightly...","open","worriedL") from _call_her_main_6567
            m "what happened?"
            call her_main("well I was sitting in the library, minding my own business...","annoyed","angryL") from _call_her_main_6568
            call her_main("when all of a sudden a group of first year students came from nowhere asking me all these questions...","angry","worriedCl") from _call_her_main_6569
            call her_main("\"is it fluffy\"...","annoyed","angryL") from _call_her_main_6570
            call her_main("\"why are you wearing it\"...","angry","down_raised") from _call_her_main_6571
            call her_main("\"does it feel nice\"...","base","down") from _call_her_main_6572
            call her_main("\"can we touch it\"...","base","down") from _call_her_main_6573
            call her_main("\"can you make it wag\"...","angry","wink") from _call_her_main_6574
            m "what did you do?"
            call her_main("well I made them promise to keep quiet about it...","upset","closed") from _call_her_main_6575
            call her_main("but in exchange I may have had to let them touch it...","open","down") from _call_her_main_6576
            call her_main("{image=textheart}{image=textheart}{image=textheart}","soft","ahegao") from _call_her_main_6577
            m "So you let a group of innocent first years touch your buttplug..."
            call her_main("It sounds sinister when you put it like that.","annoyed","angryL") from _call_her_main_6578
            her "All I did was take them to a secluded part of the library and let them touch my tail..."
            m "Well that's alright then..."
            call her_main(".......","base","down") from _call_her_main_6579
            m "So did you enjoy it?"
            call her_main("..........","angry","base") from _call_her_main_6580
            call her_main("Truthfully [genie_name].... It was the most one of the most pleasurable experiences of my life...","grin","dead") from _call_her_main_6581
            call her_main("all their hands touching it...","soft","ahegao") from _call_her_main_6582
            call her_main("taking turns...","grin","ahegao") from _call_her_main_6583
            call her_main("all the while it was vibrating away...","base","down") from _call_her_main_6584
            call her_main("I nearly passed out.","silly","dead") from _call_her_main_6585
            call her_main("I even tried to make them stop...","silly","ahegao") from _call_her_main_6586
            call her_main("but they just kept going...","grin","ahegao") from _call_her_main_6587
            m "Nice work, [hermione_name]."
        
        elif one_out_of_three == 2: ### Speech in McGonagall's class
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes I did, [genie_name]...","base","base",xpos="right",ypos="base") from _call_her_main_6588
            call her_main("Did you know there are holes between the stalls in the girls bathroom?","soft","base") from _call_her_main_6589
            m "i did not, but What does that have to do with your buttplug?"
            call her_main("Well, I noticed that the hole is the same height as the tail...","grin","baseL") from _call_her_main_6590
            call her_main("...............","grin","worriedCl") from _call_her_main_6591
            m "go on, [hermione_name]."
            call play_music("playful_tension") from _call_play_music_263# SEX THEME.
            call her_main("I might have put it through...","base","down") from _call_her_main_6592
            m "what?"
            call her_main("Well I was in the stall finishing up...","base","baseL") from _call_her_main_6593
            her "When a girl entered the other stall."
            call her_main("I wasn't sure but I thought that it may have been a \"slytherin\"...","upset","wink") from _call_her_main_6594
            call her_main("So I decided to stick my tail through!","smile","baseL") from _call_her_main_6595
            m "did they touch it?"
            call her_main("not immediately...","base","baseL") from _call_her_main_6596
            call her_main("but after I gave it a little wiggle she eventually came around...","grin","baseL") from _call_her_main_6597
            call her_main("she was curious at first but eventually she started to really play with it...","open","baseL") from _call_her_main_6598
            call her_main("stroking it... flicking it... I even think she may have licked it...","soft","ahegao") from _call_her_main_6599
            her "...imagine that... a slytherin, licking something that was in my..."
            her "It was incredible... I could barely stand while it happened..."
            m "did you find out who it was?"
            call her_main("I did [genie_name].","open","worried") from _call_her_main_6600
            call her_main("It was at lunch, in the great hall.","open","closed") from _call_her_main_6601
            call her_main("I was walking past the slytherin table on my way to sit down...","open","closed") from _call_her_main_6602
            call her_main("when I saw that little... vixen, astoria greengrass.","base","suspicious") from _call_her_main_6603
            her "she couldn't take her eyes off of it..."
            call her_main("imagine that... astoria greengrass... pureblood, licking my...","grin","ahegao") from _call_her_main_6604
            call her_main("{image=textheart}........{image=textheart}","soft","ahegao") from _call_her_main_6605
            m "It sounds like you've earned your points today then [hermione_name]."
            call her_main("...{size=-7}(I would have done this for free...){/size}","base","down") from _call_her_main_6606
        
        elif one_out_of_three == 3: ### Sits down in hall with it showing
            call play_music("chipper_doodle") from _call_play_music_264 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes, I did [genie_name]...","base","suspicious",xpos="right",ypos="base") from _call_her_main_6607
            m "Anything interesting happen?"
            her "do you know that Patil twins [genie_name]?"
            m "no but do continue."
            call her_main("well they were walking down the hall behind me...","base","glance") from _call_her_main_6608
            her "I swear I could hear them whispering to each other..."
            call her_main("and I thought I may as well give them something to talk about...","base","suspicious") from _call_her_main_6609
            call her_main("So I stopped, kept my knees straight and bent over as far as I could...","base","glance") from _call_her_main_6610
            m "You exposed yourself just like that?"
            call her_main(".......","base","baseL",cheeks="blush") from _call_her_main_6611
            m "Very good, [hermione_name]!"
    
    $ gryffindor += current_payout #55
    m "The \"Gryffindor\" house gets [current_payout] points!"
    her "Thank you, [genie_name]."
    
    $ hg_ps_Buttplug_OBJ.points += 1
    $ hg_ps_Buttplug_OBJ.complete = True
    $ hg_ps_Buttplug_OBJ.inProgress = False
    
    call set_h_buttplug("remove") from _call_set_h_buttplug_15
    
    jump hg_pr_transition_block
    
    
    
