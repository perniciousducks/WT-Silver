

### Wear A Buttplug ###

label hg_ps_buttplug:

    call reset_menu_position

    $ current_payout = 55 #Used when haggling about price of the favour.

    if hg_ps_buttplug.points < 1:
        m "{size=-4}(Tell her to wear a buttplug around the school?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu
    else:
        m "{size=-4}(I feel like making her walk around with a buttplug again!){/size}"

    m "{size=-4}(But what Type?){/size}"
    menu:
        "-Small, regular-":
            $ buttplug_size = 1
        "-Medium, magical-" if hg_ps_buttplug.points >= 1:
            $ buttplug_size = 2
        "-Large, magical-" if buttplug_2_worn == True and her_whoring > 23:
            $ buttplug_size = 3

    #First event.
    if hg_ps_buttplug.points == 0 and buttplug_size == 1:
        m "[hermione_name], I want you to do something different today..."
        call her_main("...........","soft","base",xpos="right",ypos="base")
        call nar(">You pull a large size buttplug out from under your desk and place it in front of her.")
        if her_whoring <=10:
            m "I want you to wear a buttplug around the school."
            jump too_much

        $ buttplug_1_worn = True

        call her_main("and what is that supposed to be? Some sort of animals tail?","open","suspicious")
        m "Not exactly, it's a buttplug. I want you to put it in while you attend class today."
        stop music
        with hpunch
        call her_main("{size=+5}What?!!{/size}","shock","wide")
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("You expect me to put that massive thing in my...","angry","angry")
        her "and then parade myself around the school!"
        m "It just looks like a fake tail, No one will be able to tell what it really is."
        call her_main("{size=+5}That's not the point!{/size}","scream","angryCl")
        her "I'm not going to put that ridiculous thing anywhere near my butt!"
        call her_main("We are done here, [genie_name]!","angry","angry",emote="01")
        m "Alright, alright, calm down..."
        call her_main("I most certainly will not, [genie_name]! That thing is beyond absurd!","scream","angryCl")
        m "Alright, fine, maybe I underestimated how large it is..."
        call her_main("You think [genie_name]?! I'd like to see you try and fit it up your-","angry","angry")
        m "alright, alright..."
        call her_main(".........","annoyed","annoyed")
        m "How about we try one a little less... ambitious."
        call her_main("............","upset","closed")
        m "I'm willing to give \"Gryffindor\" fifty five points."
        m "and All I ask for..."
        call her_main("..........?","annoyed","suspicious")
        call nar(">You pull out the small buttplug from your desk.")
        m "...is that you wear this to class..."
        call her_main("!!!......","angry","angry")
        m "Oh, come on... Just a harmless little baby one."
        call her_main("...","disgust","glance")
        m "Fifty five house points..."
        call her_main("..............","annoyed","angryL")
        call her_main("Fine.","annoyed","annoyed")
        m "Fantastic."
        m "Will you be putting it in now then?"
        call her_main("........","annoyed","angryL")
        call her_main("I'll put it in in the girls bathroom [genie_name]","annoyed","angryL")
        m "Hmmm... we'll i'll See you tonight then."

    #Second Event.
    elif buttplug_2_worn == False and buttplug_size == 2:
        m "[hermione_name], I want you to try something different today..."
        call her_main("...........","soft","base",xpos="right",ypos="base")
        call nar(">You pull the medium size buttplug out from under your desk and place it in front of her.")
        if her_whoring <=15:
            m "I want you to wear this buttplug around the school."
            jump too_much

        $ buttplug_2_worn = True

        call her_main("and what is this supposed to be?","open","suspicious")
        m "Can't you tell it's a buttplug? They shouldn't be new to you at this point."
        call her_main("...","annoyed","annoyed")
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("Why does it have a such a large tail attached to it...","annoyed","angry")
        her "you can't expect me to wear that around the school!"
        m "I can and do, unless you want our little trading game to come to a halt..."
        call her_main("but it's so long! everyone will be able to see it!","normal","worriedCl")
        m "That's the point, [hermione_name]..."
        call her_main("...........","angry","worriedCl",emote="05")
        call her_main("I want 100 points.","annoyed","angry")

        menu:
            "\"Fine, but I expect you to put it in now.\"":
                $ current_payout = 100
                call her_main("What? Right now!?.","angry","worriedCl")
                call her_main("In front of you?","angry","wink")
                m "100 points [hermione_name]..."
                call her_main("ugh... Fine...","angry","down_raised")
                call her_main("But I'm not turning around!","annoyed","annoyed")
                m "Whatever suits you best..."
                ">You hand her the buttplug"
                call her_main("{size=-7}It's so big...{/size}","clench","down_raised")
                ">Hermione lifts her skirt and presses it against her asshole."
                call her_main("ughh... it's too big...","shock","worriedCl")
                call her_main("It won't fit!","open","worriedCl")
                m "well then Try spitting on it."
                call her_main(".........","angry","down_raised")
                ">She spits on the end of it and then retries."
                call her_main("it didn't work, It's just too bi-","angry","base")
                stop music

                call set_her_buttplug("plug_b_on") #Updates clothing and body.

                with hpunch
                call her_main("{size=+5}!!!!{/size}","shock","wide")
                call play_music("chipper_doodle") # HERMIONE'S THEME.
                call her_main(".............","angry","base")
                call her_main("...","angry","down_raised")
                call her_main("well.... ah, I... better get to.... class... then...","angry","wink")
                m "See you tonight [hermione_name]."

            "\"You'll get 70.\"":
                $ current_payout = 70
                call her_main("Hmmmph...","annoyed","angryL")
                call her_main("Alright then, just don't expect me to show it to you!","angry","angry")
                m "So long as you wear it to class then you'll get your 70 points."
                ">You hand her the buttplug."
                call her_main("Will that be all [genie_name]?.","annoyed","annoyed")
                m "Yes [hermione_name], see you tonight."
                call her_main("{size=-5}(cheap bastard...){/size}","annoyed","angryL")


    else: # <================================================================================ NOT FIRST TIME
        if her_whoring <= 15 and buttplug_size == 1: # LEVEL 06 FIRST EVENT.
            $ buttplug_1_worn = True

            m "Today's favour shall be..."
            call her_main(".........","angry","base",xpos="right",ypos="base")
            m "Wearing your favourite little buttplug to class!"
            call her_main("...again?","angry","down_raised")
            m "Sure, why not?"
            m "And another fifty five house points for the \"Gryffindor\" house of course."
            call her_main("..........","annoyed","worriedL")
            m "So... Are you ok with that, [hermione_name]?"
            call her_main("I suppose so...","annoyed","angryL")
            ">You hand her the buttplug."
            m "Fantastic! See you after class."

        elif her_whoring <= 20 and buttplug_size == 1: # LEVEL 07
            $ buttplug_1_worn = True

            ">You pull out the large buttplug."
            m "Ready to try out the dragon yet?"
            stop music fadeout 1.0
            call her_main("What?","scream","wide_stare",xpos="right",ypos="base")
            call her_main("Of course not! That thing would tear me--","scream","angryCl")
            ">you pull out the small buttplug"
            m "How about this one then?"
            call her_main("Oh, ok then!","smile","happyCl",emote="06")
            m "You'll do it that easily?"
            call her_main("Well for fifty five house points I'd be crazy not to.","base","closed")
            call her_main("Plus I don't hate the way it feels","open","baseL")
            ">You hand her the buttplug."
            m "why don't you put it in now."
            call her_main("you want me to put it in now? in front of you!","scream","wide_stare")
            m "I don't see the harm in it."
            call her_main("well... it does save me having to visit the girls bathroom before class...","annoyed","down")
            call her_main("alright then, I'll do it... but I want an extra five points!","smile","baseL")
            m "Done."
            $ current_payout += 5
            call her_main("well... here goes.","smile","baseL")
            ">Hermione lifts her skirt and sticks it in rather slowly."

            call set_her_buttplug("plug_a_on") #Updates clothing and body.

            call her_main("{image=textheart}ah{image=textheart}...","grin","ahegao")
            call her_main("i better head to class...","soft","squintL")
            m "See you tonight [hermione_name]."
            call her_main("{size=-5}({image=textheart}it feels so good{image=textheart}){/size}","grin","ahegao")

        elif her_whoring >= 21 and buttplug_size == 1: # LEVEL 08+
            $ buttplug_1_worn = True

            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "What do you think about wearing a buttpl-?"
            call her_main("I'll do it.","grin","baseL",xpos="right",ypos="base")
            m "You're eager."
            call her_main("well... I mean it is a lot of points and... i've sort of grown fond of how it feels...","open","down")
            m "Great. Go have fun then!"
            ">You hand her the buttplug."
            ">Hermione turns around and lifts her skirt giving you a full view as she inserts it."

            call set_her_buttplug("plug_a_on") #Updates clothing and body.

            call her_main("{image=textheart}ah{image=textheart}...","grin","ahegao")
            call her_main("I will, [genie_name]. Thank you.","base","happyCl")

        elif her_whoring <= 19 and buttplug_size == 2: # LEVEL 06 FIRST EVENT.
            $ buttplug_2_worn = True

            m "Today my gracious request will be..."
            call her_main(".........","angry","base",xpos="right",ypos="base")
            m "That you wear everyone's favourite magical buttplug to class!"
            call her_main("...again?","angry","down_raised")
            m "why not? This will be the easiest fifty five points you'll ever earn!"
            call her_main("..........","annoyed","worriedL")
            m "Do you have a problem with it, [hermione_name]?"
            call her_main("I suppose not...","annoyed","angryL")
            ">You hand her the buttplug."
            m "Fantastic! See you after class."

        elif her_whoring <= 23 and buttplug_size == 2: # LEVEL 07
            if buttplug_2_question == False:
                $ buttplug_2_question = True
                ">You pull out the buttplug."
                m "Ready to try out the phoenix again?"
                call her_main("Oh, I suppose so...","soft","squintL",xpos="right",ypos="base")
                call her_main("But is it alright if I ask you something first?","open","down")
                m "What's that [hermione_name]"
                call her_main("Don't you worry about us getting caught?","annoyed","base")
                m "Why would I?"
                call her_main("Well it's just that making me wear something like this is drawing a lot of attention...","open","worriedL")
                call her_main("and what if someone realises that it's you who's making me do all this...","open","worried")
                m "and who is going to suspect the great albis dumbledorf?"
                call her_main("...I suppose no one...","annoyed","worriedL")
                m "Then don't worry about it. If anyone asks just tell them you're going through an exhibitionist stage."
                m "Speaking of which..."
                ">You hand her the buttplug."
                call her_main("Oh... right...","base","down")
                ">Hermione lifts her skirt and pushes it in gently, taking her time."

                call set_her_buttplug("plug_b_on") #Updates clothing and body.

                call her_main("{image=textheart}{image=textheart}{image=textheart}ah{image=textheart}{image=textheart}{image=textheart}...","grin","ahegao")
                call her_main("i better... head to class... now...","open","baseL")
                m "See you tonight [hermione_name]."
                call her_main("{size=-5}({image=textheart}it's... so... big...{image=textheart}){/size}","grin","ahegao")
            else:
                ">You pull out the buttplug."
                m "Ready for the phoenix again?"
                call her_main("Oh, alright then...","open","down",xpos="right",ypos="base")
                call her_main("but if you pay me and additional 5 points I'll turn around as I put it in...","soft","squintL")
                menu:
                    "\"Done\"":
                        $ current_payout += 5
                        call her_main("thank you [genie_name], you won't regret it...","open","baseL")
                    "\"Fifty five is all I can do.\"":
                        m "Any more and people might get suspicious."
                        call her_main("hmmmm I suppose you're right...","annoyed","angryL")
                        call her_main("but as a present i'll show you anyway...","base","down")
                        call her_main("although you better appreciate it...","base","suspicious")
                        m "I'm sure I will."
                ">You hand her the buttplug."
                call her_main("well... here goes...","base","down")
                ">Hermione turns around, lifts her skirt and pushes it in gently, taking her time."

                call set_her_buttplug("plug_b_on") #Updates clothing and body.

                call her_main("{image=textheart}{image=textheart}{image=textheart}ah{image=textheart}{image=textheart}{image=textheart}...","grin","ahegao")
                call her_main("i better... head to class... now...","soft","squintL")
                m "See you tonight [hermione_name]."
                call her_main("{size=-5}({image=textheart}it's... so... good...{image=textheart}){/size}","grin","ahegao")

        elif her_whoring >= 24 and buttplug_size == 2: # LEVEL 08+
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "What do you think about wearing a buttpl-?"
            call her_main("I'll do it.","grin","baseL",xpos="right",ypos="base")
            m "You're eager. I haven't even said what one yet..."
            call her_main("oh... can it be the big one... with the long tail...","open","down")
            call her_main("please...","soft","squintL")
            m "well seeing as how you asked so nicely..."
            ">You hand her the buttplug."
            ">Hermione turns around and lifts her skirt giving you a full view as she inserts it."

            call set_her_buttplug("plug_b_on") #Updates clothing and body.

            call her_main("{image=textheart}ah{image=textheart}...","grin","ahegao")
            call her_main("Thank you [genie_name]!","open","baseL")
            call her_main("{size=-5}({image=textheart}it feels so good... I might have to buy my own...{image=textheart}){/size}","grin","ahegao")

        # Large buttplug first time
        elif buttplug_size == 3 and not buttplug_3_worn:
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "What do you think about wearing a buttpl-?"
            call her_main("I'll do it.","grin","baseL",xpos="right",ypos="base")
            m "You're eager. I haven't even said which one yet..."
            call her_main("oh... can it be the big one... with the long tail...","open","down")
            call her_main("please...","soft","squintL")
            m "well seeing as how you did ask for the big one..."
            call nar(">You hand her the buttplug.")
            call her_main("!!!","angry","down_raised")
            call her_main("This isn't the one I meant [genie_name]...","angry","down_raised")
            m "Didn't you ask for the big one?"
            call her_main("I did-","grin","ahegao")
            m "Well here's the {b}big{/b} one."
            call her_main("I didn't know you had one this big!","disgust","down")
            call her_main("I don't even think this will fit...","disgust","base",cheeks="blush")
            m "Never say never!"
            call her_main("You can't be serious!","scream","down")
            call her_main("This thing is ridiculous!","open","closed")
            m "You said the same thing about the smaller one."
            call her_main("That was different...","disgust","down_raised")
            m "I have confidence in you! Besides, you were pretty great when you were taking my cock up your ass!"
            call her_main("[genie_name]!","shock","wide_stare",cheeks="blush")
            m "Come on..."
            call her_main("This is too much sir! even your cock wasn't this {b}thick{/b}...","open","angryL")
            m "Nothing a little spit won't solve!"
            call her_main("Don't be ridiculous! This is beyond spit!","open","closed")
            call her_main("Unless you have some sort of actual {i}lubricant{/i} in your possession, I don't think I'll be letting this thing anywhere near me...","open","angry")

            menu:
                "-Use anal lube-" if anal_lube_ITEM.number >= 1:
                    $ buttplug_3_worn = True
                    call play_music("playful_tension") # SEX THEME.
                    m "well it just so happens that I recently came across the solution to your problem."
                    call her_main("Which is?","disgust","wink")
                    m "Here."

                    call give_gift(">You hand hermione the jar of anal lubricant.",anal_lube_ITEM)

                    call her_main("!!!","clench","wide")
                    call her_main("I wasn't serious, [genie_name]!","scream","angry")
                    m "Now, now. No one likes a liar."
                    call her_main("I didn't promise anything! Besides, I didn't actually expect you to have a jar of lube in your desk.","open","angryL")
                    m "I bought it for just such an occasion..."
                    call her_main("...","annoyed","angry")
                    call her_main("ugh... fine. I'll {b}try{/b} to fit it in.","disgust","down")
                    call her_main("but I'm not promising anything!","open","closed")
                    m "That's all I ask."
                    call nar(">You hand hermione the large buttplug.")
                    call her_main("I still don't think this is going to work...","open","base")
                    call nar(">Hermione slowly coats the massive buttplug with lube.")
                    call her_main("There's barely even enough here to cover it...","open","down")
                    call her_main("(There's no way this thing will fit.)","disgust","down_raised")
                    call nar(">Hermione slowly places the lubed up buttplug to her anus.")
                    call her_main("I'm telling you, [genie_name], this isn't going to-","open","closed")
                    call her_main("{size=+10}!!!{/size}","soft","wide",cheeks="blush",trans="hpunch")
                    call her_main("{size=+10}It's moving!{/size}","disgust","worriedCl")
                    m "Really?"
                    call her_main("{size=+5}ugh...{/size}","disgust","worriedCl")
                    call her_main("{size=+5}it's forcing it's way inside me....{/size}","open","shocked")
                    call her_main("ah...","shock","worriedCl")
                    call her_main("it's...{p}it's...","open","wide")

                    call play_sound("pop")
                    $ hermione_dribble = True
                    call set_her_buttplug("plug_c_on") #Updates clothing and body.

                    call her_main("","soft","ahegao",cheeks="blush")
                    call ctc

                    call her_main("{size=+5}incredible!{/size}","soft","ahegao",cheeks="blush")


                    call her_main(".............","disgust","ahegao")
                    m "Are you alright, [hermione_name]?"
                    call her_main("..........................","soft","ahegao_raised")
                    call her_main("ah... y-yes...","open","glance")
                    m "Fantastic! I'll see you after class then."
                    call her_main(".............","disgust","down",cheeks="blush")
                    call nar(">Hermione slowly leaves your office, barely able to walk in a straight line.")

                "{color=#858585}-Use anal lube ?-{/color}" if anal_lube_ITEM.number <= 0:
                    call nar(">You do not have this item.")
                    m "afraid not..."
                    call her_main("well then i think I better be off to class then.","open","closed")
                    call her_main("{size=-2}unless {size=-2}you {size=-2}have {size=-2}the {size=-2}smaller {size=-2}one?{/size}{image=textheart}","soft","glanceL",cheeks="blush")
                    g9 "It just so happens that I do!"
                    call nar(">You hand her the buttplug.")

                    call set_her_buttplug("plug_b_on") #Updates clothing and body.

                    call her_main("{image=textheart}ah{image=textheart}...","silly","ahegao")
                    call her_main("Thank you, [genie_name].","base","glance")
                    call her_main("{size=-5}({image=textheart}it feels so good... I might have to buy my own...{image=textheart}){/size}","soft","ahegao")
                    hide screen hermione_main
                    with d3
                    pause.2
                    m "(Maybe those Weasley boys have anything that could help me with my friction problem...)"

        elif buttplug_size == 3: # Large buttplug repeat
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "how do you feel about wearing another buttplug to class today?"
            call her_main("...","base","baseL",xpos="right",ypos="base")
            call her_main("which one?","grin","base")
            m "how about the big one again?"
            call her_main("really?","open","down")
            call her_main("do i have to?","soft","squintL")
            m "you didn't seem to hate wearing it last time..."
            call her_main("...","open","down")
            call her_main("{size=-5}alright then...{/size}","open","down")
            call nar(">You hand her the buttplug.","start")
            call nar(">You watch it magically worm it's way inside her eager butt-hole.","end")

            call set_her_buttplug("plug_c_on") #Updates clothing and body.

            call her_main("{image=textheart}ah{image=textheart}ah...","grin","ahegao")
            call her_main("Thank you, [genie_name]!","base","glance")
            call her_main("{size=-5}({image=textheart}it feels so good... I might have to buy my own...{image=textheart}){/size}","soft","ahegao")

    call her_walk(action="leave", speed=2.5)

    $ hg_ps_buttplug.inProgress = True

    jump end_hermione_event





label hg_ps_buttplug_complete:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call bld
    if her_whoring <= 15 and buttplug_size == 1: # LEVEL 06
        if one_out_of_three == 1: ### EVENT (A)
            m "[hermione_name], how did it go?"
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            show screen blktone
            $ sc34CG(1, 8)
            call her_main("It was awful... of course...","annoyed","frown",xpos="base",ypos="base")
            m "Just tell me what happened, [hermione_name]..."
            call her_main("I've never been so uncomfortable in my life [genie_name]!","disgust","glance")
            call her_main("I wasn't able to focus on anything all day!","annoyed","annoyed")
            m "Why's that?"
            call her_main("Whenever I was sitting down in class it just kept prodding me...","annoyed","angryL")
            her "So naturally I had to adjust the way I was sitting, [genie_name]..."
            $ sc34CG(1, 9)
            call her_main("but that just made it worse...","annoyed","angryL")
            m "Do you think anyone else noticed you?"
            call her_main("I've got no idea...","annoyed","annoyed")
            $ sc34CG(1, 10)
            call her_main("I could hardly think straight... Let alone notice other people.","annoyed","annoyed")
            m "So it felt good then?"
            call her_main("Good?","open","base")
            $ sc34CG(1, 12)
            call her_main("If you call getting your... butt teased all day good...","annoyed","down")
            call her_main("Then yes, I suppose it did...","annoyed","ahegao")
            $ sc34CG(1, 13)
            call her_main("Still... being this distracted during class could really damage my grades...","angry","base")
            m "I wouldn't worry about that. Just think of Gryffindor!"
            hide screen sccg
            call her_main("Speaking of that...","annoyed","annoyed",xpos="right",ypos="base",trans="fade")
            m "Oh yes, quite right."

        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], how did it go?"
            show screen blktone
            call her_main("It went well, [genie_name]...","open","base",xpos="right",ypos="base")
            call play_music("playful_tension") # SEX THEME.
            her "Barely anybody noticed that I was wearing it..."
            call her_main("...Except for a few girls from Ravenclaw...","open","base",cheeks="blush")
            m "What happened?"
            call her_main("I was walking down the hall, on my way to potions class...","open","closed")
            call her_main("And suddenly a gust of wind came and blew my skirt up...","upset","wink")
            m "A gust of wind? inside?"
            call her_main("It must have been from a window...","soft","baseL")
            call her_main("Anyway the three girls walking behind me may have... seen it.","open","down")
            m "Did they say anything to you?"
            call her_main("No... But I did hear them giggling afterwards...","clench","down_raised")
            m "Well, it sounds like a job well done..."

        elif one_out_of_three == 3: ### EVENT (C) Event level: 01.
            m "[hermione_name], how did it go?"
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            show screen blktone
            call her_main("Awful, [genie_name]. Simply awful...","scream","worriedCl",xpos="right",ypos="base")
            m "What happened?"
            call her_main("Moaning Myrtle happened!","normal","worriedCl")
            m "Moaning Mittle?"
            call her_main("That pesky little ghost!","annoyed","angryL")
            call her_main("This thing left me so frustrated that in my free period I went to the girls toilets to...","annoyed","angryL")
            call her_main("Relieve myself...","annoyed","worriedL")
            call her_main("When all of a sudden that annoying ghost poked her head through the door!","scream","angryCl")
            call her_main("As it if wasn't bad enough that she saw me...","open","down")
            call her_main("She then started yelling \'Hermione has a buttplug\' to everyone in the toilets!","scream","angry",emote="01")
            call her_main("Luckily the stalls where empty! Imagine if they weren't!","annoyed","annoyed")
            m "Well, it certainly sounds like you've earned your points."

    elif her_whoring <= 20 and buttplug_size == 1: # LEVEL 07
        if one_out_of_three == 1: ### EVENT (A)
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Of course.","open","base",xpos="right",ypos="base")
            m "Did anyone notice?"
            call her_main("Yes... well I might have...","base","down")
            call her_main("shown someone...","base","glance")
            her "I was in the library fetching some books when I saw Luna..."
            her "She was reading at a desk..."
            call her_main("So I decided to walk over to her and have a chat...","grin","baseL")
            call her_main("She was talking about something nonsensical...","base","baseL")
            her "And I figured that if she saw it..."
            her "no one would believe her..."
            m "alright..."
            call her_main("So I feigned dropping my quill...","grin","baseL")
            m "Go on..."
            call her_main("then I turned around in front of her...","base","down")
            her "and bent over..."
            her "...keeping my knees straight..."
            call her_main("...giving her a full view...","base","ahegao_raised")
            m "I see..."
            m "Did she say anything?"
            call her_main("No, [genie_name]...","soft","squintL")
            her "But when I turned back around she didn't make eye contact..."
            m "Hm..."
            call her_main("I don't think I've seen anyone blush so hard...","base","glance")
            m "Well it sounds like you've earned your points and then some."

        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            $ sc34CG(1, 9, 1)
            call her_main("I did, [genie_name]...","open","closed",xpos="base",ypos="base")
            call her_main("Although I am still not sure how I feel about all of this...","annoyed","worriedL")
            $ sc34CG(1, 11, 1)
            call her_main("It's starting to really affect my grades...","annoyed","worriedL")
            call her_main("I couldn't even tell you what potions we were taught today...","open","base")
            call play_music("playful_tension") # SEX THEME.
            call her_main("Me, Hermione Granger...","open","down")
            $ sc34CG(1, 12, 1)
            call her_main("Not learning in class...","angry","down_raised")
            m "Well you could try relieving yourself in between lessons."
            $ sc34CG(1, 13, 1)
            call her_main("Oh, i've tried that... but it doesn't work...","angry","base")
            her "It just makes the next class harder..."
            $ sc34CG(1, 12, 1)
            call her_main("today, After potions I went to my room to... calm myself...","open","baseL")
            call her_main("But it just made herbology worse...","open","down")
            $ sc34CG(1, 11, 1)
            call her_main("I was forced into touching myself in the middle of class...","clench","down_raised")
            call her_main("Do you think anyone noticed, [genie_name]?","open","squint",cheeks="blush")
            $ sc34CG(1, 9, 1)

            menu:
                "\"What? Of course not, [hermione_name]!\"":
                    $ sc34CG(1, 8, 2)
                    call her_main("..............","base","baseL",cheeks="blush")
                    call her_main("You are right, [genie_name]...","base","down")
                    her "I was very discreet..."
                    $ sc34CG(1, 12, 3)
                    call her_main("very quiet...","soft","ahegao")
                    call her_main("barely making a sound...","grin","baseL")
                    hide screen sccg
                    call her_main("[genie_name], can I get paid now, please?","base","glance",xpos="right",ypos="base",trans="fade")
                    her "......"
                "\"Of course they did!\"":
                    $ sc34CG(1, 13, 2)
                    m "Do you honestly believe that no one noticed you touching yourself?"
                    call her_main("I was afraid that you would say that, [genie_name]...","mad","worriedCl",tears="soft_blink")
                    m "You were surrounded by people!"
                    call her_main("........","mad","worriedCl",tears="soft_blink")
                    hide screen sccg
                    call her_main("[genie_name], can I get paid now, please?","angry","base",tears="soft",xpos="right",ypos="base",trans="fade")
            m "Certainly."

        elif one_out_of_three == 3: ### EVENT (C)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            $ sc34CG(1, 11)
            call her_main("Yes, [genie_name]. I did.","open","closed",xpos="base",ypos="base")
            m "Great. Tell me more."
            call play_music("playful_tension") # SEX THEME.
            call her_main("Well, there's not much to tell...","open","base")
            $ sc34CG(1, 12)
            her "I attended classes..."
            her "tried to take notes."
            her "all in all it was a fairly regular day..."
            $ sc34CG(1, 13)
            call her_main("Well as regular as it could have been with a plug up my butt.","annoyed","angryL")
            m "and Nobody noticed?"
            call her_main("I don't think so, [genie_name].","annoyed","annoyed")
            $ sc34CG(1, 11)
            m "Well I suppose something interesting can't happen everyday."
            hide screen sccg
            call her_main("...","annoyed","baseL",xpos="right",ypos="base",trans="fade")


    elif her_whoring >= 21 and buttplug_size == 1: # LEVEL 08+
        if one_out_of_three == 1: ### EVENT (A)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes I did, [genie_name].","base","base",xpos="right",ypos="base")
            m "Well? How was your day?"
            call her_main("great, [genie_name]...","base","ahegao_raised")
            m "go on..."
            call play_music("playful_tension") # SEX THEME.
            $ sc34CG(1, 14, 1)
            call her_main("Well I've worked out how to deal with this thing being in me all day...","soft","squintL",xpos="base",ypos="base")
            m "Really? And how is that?"
            call her_main("before now I've been going around it the wrong way...","open","baseL")
            call her_main("I just tried to ignore it...","open","closed")
            her "and pay attention in class..."
            call her_main("But that didn't work at all...","upset","wink")
            call her_main("I was just too... distracted...","base","down")
            $ sc34CG(1, 15, 2)
            call her_main("So I thought to myself that I've just got to focus on it...","base","ahegao_raised")
            $ sc34CG(1, 16, 3)
            call her_main("block out everything else...","base","down")
            $ sc34CG(1, 17, 2)
            call her_main("...embrace it...","grin","dead")
            m "and how did you do that?"
            call her_main("well if I rock my hips while I'm sitting in class it's almost enough...","base","glance")
            $ sc34CG(1, 16, 3)
            call her_main("but if I sit of the edge of my chair while I rock my hips...","base","suspicious")
            $ sc34CG(1, 17, 2)
            call her_main("{image=textheart}{image=textheart}{image=textheart}","soft","ahegao")
            m "So you worked out how to pleasure yourself in class."
            call her_main("I did [genie_name].","base","down")
            her "Although I worry that it will really start to affect my grades..."
            m "Well I'm sure that missing one class a day is something you can catch up on."
            $ sc34CG(1, 15, 2)
            call her_main("only One?","angry","wink")
            m "You mean to say that you spent all your class time pleasuring yourself?"
            $ sc34CG(1, 17, 2)
            call her_main("..........","soft","ahegao")
            hide screen sccg
            call her_main(xpos="right",ypos="base",trans="fade")
            m "Nice work, [hermione_name]."

        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes I did, [genie_name].","base","base",xpos="right",ypos="base")
            call her_main("But, umm...","open","worried")
            m "...?"
            call her_main("Well, I may have gotten a bit more attention than I had hoped for...","disgust","down_raised")
            call her_main("...............","clench","down_raised")
            m "Tell me what happened, [hermione_name]."
            call play_music("playful_tension") # SEX THEME.
            call her_main("I might have had a few photos taken...","open","down")
            m "Photos..."
            call her_main("Well I was in the library minding my own business...","annoyed","closed")
            her "When I went to get a copy of Zygmunt Budge's book of potions."
            call her_main("as it was on the bottom shelf I had to kneel down to reach it...","annoyed","base")
            call her_main("When all of a sudden I heard the flash of a camera!","annoyed","angryL")
            her "I turned around and there was Colin Creevey..."
            her "with the biggest grin on his face!"
            m "You let your photo be taken?!"
            call her_main("I didn't let anything of the sort happen! It was without my consent!","scream","angry",emote="01")
            call her_main("I even made him promise not to show anyone the photo...","open","down")
            her "...in exchange I did have to let him take a few more..."
            her "but he insisted that he wouldn't show anyone else..."
            m "And you believe him?"
            call her_main("Of course [genie_name], he's a Gryffindor.","annoyed","closed")
            call her_main("Although the thought did cross my mind.","open","down")
            call her_main("What if he were to distribute the photos around the school.","clench","down_raised")
            call her_main("Imagine everyone looking at photos of me...","open","baseL")
            her "Everyone would know what I was wearing..."
            call her_main("Any time someone saw me they'd think about whether or not it was in...","base","down")
            m "That's quite the thought process."
            call her_main("Yes, well I certainly don't want that happening...","base","suspicious")
            m "I'm sure..."
            call her_main("","base","glance")
            m "It sounds like a job well done [hermione_name]."

        elif one_out_of_three == 3:
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes, I did [genie_name]...","base","suspicious",xpos="right",ypos="base")
            m "Did anyone notice?"
            her "maybe a few third years..."
            m "well go on."
            call her_main("It was the stairs...","base","glance")
            her "I may have gotten a little carried away with myself..."
            m "What happened, [hermione_name]?"
            call her_main("Well as I was walking to divination class I ended up in front of a group of third year students...","base","suspicious")
            call her_main("And seeing as how they were behind me on the stairs they may have been able to... see it.","base","glance")
            m "So you intentionally showed it to a group of boys? You don't expect me to grant you extra points for showing them, do you?"
            call her_main("Of course not, [genie_name].","base","baseL",cheeks="blush")
            m "Then why do it?"
            call her_main("Well, it just sort of just happened...","open","squint",cheeks="blush")
            call her_main("plus the look on their faces when they noticed it...","grin","dead")
            call her_main("they could barely hide their...","soft","ahegao")
            m "So you like being seen then?"
            call her_main("well...","open","baseL")
            m "Well done, [hermione_name]."
            call her_main("","base","down")

    elif her_whoring <= 19 and buttplug_size == 2: # LEVEL 06
        if one_out_of_three == 1: ### EVENT (A)
            m "[hermione_name], how was it?"
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            show screen blktone
            call her_main("It was awful... simply awful...","annoyed","frown",xpos="right",ypos="base")
            m "what happened, [hermione_name]..."
            call her_main("It was that nasty professor snape, [genie_name]!","annoyed","angryL")
            call her_main("I've never been so embarassed in my life!","annoyed","annoyed")
            m "What did he do?"
            call her_main("Well in potions class I may have corrected him about the proper way to crush a Sopophorous bean...","annoyed","angryL")
            her "so he made me stand out the front and show him the \'correct\' way..."
            call her_main("and what's worse is that he made me do it facing away from the class...","annoyed","annoyed")
            m "Do you think anyone saw it?"
            call her_main("Everyone saw it!","disgust","down_raised")
            call her_main("I could barely even crush the bean my legs were shaking that hard...","clench","down_raised")
            m "Well it sounds like you earned your points."
            call her_main(".......","annoyed","down")

        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], how did it go?"
            show screen blktone
            call her_main("It went well, [genie_name]...","open","base",xpos="right",ypos="base")
            call play_music("playful_tension") # SEX THEME.
            her "A group of second years from \"hufflepuff\" even complemented me on it..."
            call her_main("...they said that it looked cute...","grin","baseL")
            m "did anything else happen?"
            call her_main("well seeing as how they were so nice...","base","down")
            call her_main("I might have flicked my skirt up for them...","soft","squintL")
            m "you showed it to them?"
            call her_main("well they were so kind...","open","baseL")
            call her_main("and they could already see most of it...","base","down")
            m "Did they say anything to you?"
            call her_main("No... But the looks on their faces...","base","glance")
            m "Well, it sounds like a job well done..."

        elif one_out_of_three == 3: ### EVENT (C) cat swatting it
            label buttplug_magic_show:
                pass
            $ buttplug_magic_known = True
            m "[hermione_name], how did it go?"
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            show screen blktone
            call her_main("what on earth did you do to this thing?!","scream","worriedCl",xpos="right",ypos="base")
            m "What happened?"
            call her_main("Why did you not tell me this \'thing\' was cursed!","normal","worriedCl")
            m "Cursed?"
            call her_main("It vibrates!","annoyed","angryL")
            m "Really? When?"
            call her_main("when something else touches it...","annoyed","angryL")
            m "Wouldn't your skirt set it off then?"
            call her_main("I think it has to be alive...","annoyed","worriedL")
            call her_main("All I know is that when my cat crookshanks swatted at it went off!","scream","angryCl")
            m "How bad was it?"
            call her_main("It was ridiculous! I was barely able to stand...","open","worriedCl")
            call her_main("but then crookshanks thought it was some sort of game... he wouldn't leave it alone...","shock","worriedCl")
            call her_main("the vibrations were so intense that my knees gave out and I collapsed onto my bed!","angry","down_raised")
            call her_main("then he just played with it for hours...","angry","wink")
            m "are you still up for wearing it in the future?"
            call her_main("I suppose... So long as I know how it works now.","upset","closed")
            call her_main("I'll just have to keep it away from crookshanks...","angry","down_raised")
            call her_main("{size=-6}or not...{/size}","soft","ahegao")
            m "Well good work then [hermione_name]"

    elif her_whoring <= 23 and buttplug_size == 2: # LEVEL 07
        if one_out_of_three == 1: ### EVENT (A) luna plays with it in the library
            if not buttplug_magic_known:
                jump buttplug_magic_show
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], did you have fun?"
            show screen blktone
            call her_main("I suppose you could say that.","base","down",xpos="right",ypos="base")
            m "Anything interesting happen?"
            call her_main("Yes... well I might have...","base","down")
            call her_main("had someone...","base","worriedCl")
            call her_main("touch it...","base","glance")
            m "hmmmm..."
            call her_main("It was luna lovegood again.","grin","baseL")
            call her_main("We ended up sitting next to each other in class.","soft","baseL")
            her "we were talking about school, clothes..."
            m "Yes, yes, spit it out..."
            call her_main("well she said that she thought my tail was cute...","grin","baseL")
            m "Go on..."
            call her_main("then she asked so politely if she could touch it...","base","down")
            call her_main("I could hardly say no...","open","baseL")
            call her_main("so I... let her spend the rest of the lesson... playing with it...","soft","squintL")
            m "I see..."
            m "Did she realise what was happening?"
            call her_main("maybe... it felt so good that it was hard to keep it hidden.","soft","ahegao")
            her "But I think that just made her want to touch it more..."
            m "Hm..."
            call her_main("I don't think I've ever had a better lesson...","grin","dead")
            m "Well it sounds like you've earned your points and then some."

        elif one_out_of_three == 2: ### EVENT (B)
            if not buttplug_magic_known:
                jump buttplug_magic_show
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("I did, [genie_name].","open","closed",xpos="right",ypos="base")
            call her_main("Only... ehm...","grin","baseL")
            m "What is it this time [hermione_name]?"
            call her_main("Well... you know my friend...","base","base")
            her "Ginny Weasley..."
            call her_main("well I told her about the tail...","base","baseL",cheeks="blush")
            her "and how it worked and well..."
            m "Just say it, [hermione_name]."
            call her_main("Well, we decided to skip herbology class together...","open","baseL")
            call play_music("playful_tension") # SEX THEME.
            call her_main("And then she sort of grabbed it...","grin","ahegao")
            call her_main("And she just played with it so aggressively...","grin","dead")
            her "I was a mess afterwards..."
            g9 "And did you return the favour?"

            if hg_pr_kiss.counter >= 1:
                call her_main("Err... maybe...","open","squint",cheeks="blush")
                m "What did you do?"
                call her_main("well I don't want to say too much [genie_name].","base","baseL",cheeks="blush") # :)
                her "but after she saw what it was doing to me..."
                her "she insisted that I let her have a go..."
                call her_main("and that's all I'll say...","base","down") # :)
                m "Hmmmm, well you did earn your points [hermione_name], even if you are secretive about it..."
            else:
                call her_main("...No.","open","down")
                m "Why not?"
                call her_main("well I don't mind letting her touch the tail [genie_name].","annoyed","base") # :)
                her "but anything else..."
                m "Very good [hermione_name]..."

        elif one_out_of_three == 3: ### EVENT (C) called a slut by slytherin
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes, [genie_name]. I did.","annoyed","angryL",xpos="right",ypos="base")
            m "Great. Tell me more."
            call play_music("playful_tension") # SEX THEME.
            call her_main("Well, there's not much to tell...","open","down")
            her "I attended classes..."
            her "studied for the upcoming potions exam..."
            call her_main("it was a normal day except for a group of those nasty \"slytherin\" tramps...","annoyed","angryL")
            call her_main("I was minding my business on the way to class when they called me a \"butt slut\".","angry","down_raised")
            m "did you say anything back to them?"
            call her_main("and sink to their level...","annoyed","angryL")
            m "Well I suppose it's for the best."


    elif her_whoring >= 24 and buttplug_size == 2: # LEVEL 08+
        if one_out_of_three == 1: ### EVENT (A) groped by first years
            if not buttplug_magic_known:
                jump buttplug_magic_show
            m "[hermione_name], how was your day?"
            show screen blktone
            call her_main("Awful, I was attacked by a group of rabid students, [genie_name].","scream","angryCl",xpos="right",ypos="base")
            m "Attacked? By How many?"
            call her_main("six first years, [genie_name]...","annoyed","angry")
            m "you were attacked by first years?"
            call play_music("playful_tension") # SEX THEME.
            call her_main("I may have been exaggerating slightly...","open","worriedL")
            m "what happened?"
            call her_main("well I was sitting in the library, minding my own business...","annoyed","angryL")
            call her_main("when all of a sudden a group of first year students came from nowhere asking me all these questions...","angry","worriedCl")
            call her_main("\"is it fluffy\"...","annoyed","angryL")
            call her_main("\"why are you wearing it\"...","angry","down_raised")
            call her_main("\"does it feel nice\"...","base","down")
            call her_main("\"can we touch it\"...","base","down")
            call her_main("\"can you make it wag\"...","angry","wink")
            m "what did you do?"
            call her_main("well I made them promise to keep quiet about it...","upset","closed")
            call her_main("but in exchange I may have had to let them touch it...","open","down")
            call her_main("{image=textheart}{image=textheart}{image=textheart}","soft","ahegao")
            m "So you let a group of innocent first years touch your buttplug..."
            call her_main("It sounds sinister when you put it like that.","annoyed","angryL")
            her "All I did was take them to a secluded part of the library and let them touch my tail..."
            m "Well that's alright then..."
            call her_main(".......","base","down")
            m "So did you enjoy it?"
            call her_main("..........","angry","base")
            call her_main("Truthfully [genie_name].... It was the most one of the most pleasurable experiences of my life...","grin","dead")
            call her_main("all their hands touching it...","soft","ahegao")
            call her_main("taking turns...","grin","ahegao")
            call her_main("all the while it was vibrating away...","base","down")
            call her_main("I nearly passed out.","silly","dead")
            call her_main("I even tried to make them stop...","silly","ahegao")
            call her_main("but they just kept going...","grin","ahegao")
            m "Nice work, [hermione_name]."

        elif one_out_of_three == 2: ### EVENT (B) glory hole with astoria
            if not buttplug_magic_known:
                jump buttplug_magic_show
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes I did, [genie_name]...","base","base",xpos="right",ypos="base")
            call her_main("Did you know there are holes between the stalls in the girls bathroom?","soft","base")
            m "i did not, but What does that have to do with your buttplug?"
            call her_main("Well, I noticed that the hole is the same height as the tail...","grin","baseL")
            call her_main("...............","grin","worriedCl")
            m "go on, [hermione_name]."
            call play_music("playful_tension") # SEX THEME.
            call her_main("I might have put it through...","base","down")
            m "what?"
            call her_main("Well I was in the stall finishing up...","base","baseL")
            her "When a girl entered the other stall."
            call her_main("I wasn't sure but I thought that it may have been a \"slytherin\"...","upset","wink")
            call her_main("So I decided to press my cheeks to the wall and stick my tail through!","smile","baseL")
            m "did they touch it?"
            call her_main("not immediately...","base","baseL")
            call her_main("but after I gave it a little wiggle she eventually came around...","grin","baseL")
            call her_main("she was curious at first but eventually she started to really play with it...","open","baseL")
            call her_main("stroking it... flicking it... I even think she may have licked it...","soft","ahegao")
            her "...imagine that... a slytherin, licking something that was inside my..."
            her "It was incredible... I could barely stand while it happened..."
            m "did you find out who it was?"
            call her_main("I did [genie_name].","open","worried")
            call her_main("It was at lunch, in the great hall.","open","closed")
            call her_main("I was walking past the slytherin table on my way to sit down...","open","closed")
            call her_main("when I saw that little... vixen, astoria greengrass.","base","suspicious")
            her "she couldn't take her eyes off of it..."
            call her_main("imagine that... astoria greengrass... pureblood, licking my...","grin","ahegao")
            call her_main("{image=textheart}........{image=textheart}","soft","ahegao")
            m "It sounds like you've earned your points today then [hermione_name]."
            call her_main("...{size=-7}(I would have done this for free...){/size}","base","down")

        elif one_out_of_three == 3:
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes, I did [genie_name]...","base","suspicious",xpos="right",ypos="base")
            m "Anything interesting happen?"
            her "do you know that Patil twins [genie_name]?"
            m "no but do continue."
            call her_main("well they were walking down the hall behind me...","base","glance")
            her "I swear I could hear them whispering to each other..."
            call her_main("and I thought I may as well give them something to talk about...","base","suspicious")
            call her_main("So I stopped, kept my knees straight and bent over as far as I could...","base","glance")
            m "You exposed yourself just like that?"
            call her_main(".......","base","baseL",cheeks="blush")
            m "Very good, [hermione_name]!"

    elif buttplug_size == 3:
        if one_out_of_three == 1: #Groped by first years again...
            m "[hermione_name], how was your day?"
            show screen blktone
            call her_main("Awful, I was attacked by a group of rabid students, [genie_name].","scream","angryCl",xpos="right",ypos="base")
            m "Attacked? By How many?"
            call her_main("six first years, [genie_name]...","annoyed","angry")
            m "you were attacked by first years?"
            call play_music("playful_tension") # SEX THEME.
            call her_main("I may have been exaggerating slightly...","open","worriedL")
            m "what happened?"
            call her_main("well I was sitting in the library, minding my own business...","annoyed","angryL")
            call her_main("when all of a sudden a group of first year students came from nowhere asking me all these questions...","angry","worriedCl")
            call her_main("\"is it fluffy\"...","annoyed","angryL")
            call her_main("\"why are you wearing it\"...","angry","down_raised")
            call her_main("\"does it feel nice\"...","base","down")
            call her_main("\"can we touch it\"...","base","down")
            call her_main("\"can you make it wag\"...","angry","wink")
            m "what did you do?"
            call her_main("well I made them promise to keep quiet about it...","upset","closed")
            call her_main("but in exchange I may have had to let them touch it...","open","down")
            call her_main("{image=textheart}{image=textheart}{image=textheart}","soft","ahegao")
            m "So you let a group of innocent first years touch your buttplug..."
            call her_main("It sounds sinister when you put it like that.","annoyed","angryL")
            her "All I did was take them to a secluded part of the library and let them touch my tail..."
            m "Well that's alright then..."
            call her_main(".......","base","down")
            m "So did you enjoy it?"
            call her_main("..........","angry","base")
            call her_main("Truthfully [genie_name].... It was the most one of the most pleasurable experiences of my life...","grin","dead")
            call her_main("all their hands touching it...","soft","ahegao")
            call her_main("taking turns...","grin","ahegao")
            call her_main("all the while it was vibrating away...","base","down")
            call her_main("I nearly passed out.","silly","dead")
            call her_main("I even tried to make them stop...","silly","ahegao")
            call her_main("but they just kept going...","grin","ahegao")
            m "Nice work, [hermione_name]."

        elif one_out_of_three == 2: ### Speech in McGonagall's class
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes I did, [genie_name]...","base","base",xpos="right",ypos="base")
            call her_main("Did you know there are holes between the stalls in the girls bathroom?","soft","base")
            m "i did not, but What does that have to do with your buttplug?"
            call her_main("Well, I noticed that the hole is the same height as the tail...","grin","baseL")
            call her_main("...............","grin","worriedCl")
            m "go on, [hermione_name]."
            call play_music("playful_tension") # SEX THEME.
            call her_main("I might have put it through...","base","down")
            m "what?"
            call her_main("Well I was in the stall finishing up...","base","baseL")
            her "When a girl entered the other stall."
            call her_main("I wasn't sure but I thought that it may have been a \"slytherin\"...","upset","wink")
            call her_main("So I decided to stick my tail through!","smile","baseL")
            m "did they touch it?"
            call her_main("not immediately...","base","baseL")
            call her_main("but after I gave it a little wiggle she eventually came around...","grin","baseL")
            call her_main("she was curious at first but eventually she started to really play with it...","open","baseL")
            call her_main("stroking it... flicking it... I even think she may have licked it...","soft","ahegao")
            her "...imagine that... a slytherin, licking something that was in my..."
            her "It was incredible... I could barely stand while it happened..."
            m "did you find out who it was?"
            call her_main("I did [genie_name].","open","worried")
            call her_main("It was at lunch, in the great hall.","open","closed")
            call her_main("I was walking past the slytherin table on my way to sit down...","open","closed")
            call her_main("when I saw that little... vixen, astoria greengrass.","base","suspicious")
            her "she couldn't take her eyes off of it..."
            call her_main("imagine that... astoria greengrass... pureblood, licking my...","grin","ahegao")
            call her_main("{image=textheart}........{image=textheart}","soft","ahegao")
            m "It sounds like you've earned your points today then [hermione_name]."
            call her_main("...{size=-7}(I would have done this for free...){/size}","base","down")

        elif one_out_of_three == 3: ### Sits down in hall with it showing
            call play_music("chipper_doodle") # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            call her_main("Yes, I did [genie_name]...","base","suspicious",xpos="right",ypos="base")
            m "Anything interesting happen?"
            her "do you know that Patil twins [genie_name]?"
            m "no but do continue."
            call her_main("well they were walking down the hall behind me...","base","glance")
            her "I swear I could hear them whispering to each other..."
            call her_main("and I thought I may as well give them something to talk about...","base","suspicious")
            call her_main("So I stopped, kept my knees straight and bent over as far as I could...","base","glance")
            m "You exposed yourself just like that?"
            call her_main(".......","base","baseL",cheeks="blush")
            m "Very good, [hermione_name]!"

    $ gryffindor += current_payout #55
    m "The \"Gryffindor\" house gets [current_payout] points!"
    her "Thank you, [genie_name]."

    call her_walk(action="leave", speed=2.5)

    $ hg_ps_buttplug.points += 1
    $ hg_ps_buttplug.complete = True
    $ hg_ps_buttplug.inProgress = False

    call set_her_buttplug("remove")

    # Stats
    $ hg_ps_buttplug.counter += 1

    jump end_hermione_event
