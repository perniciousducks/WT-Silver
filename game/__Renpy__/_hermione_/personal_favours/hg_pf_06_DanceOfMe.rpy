

### HERMIONE PERSONAL FAVOUR 6 ###

### DANCE FOR ME ###

label hg_pf_DanceForMe:
    hide screen hermione_main 
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_DanceForMe_OBJ.points < 1:
        m "{size=-4}(Ask her to dance for me?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests

    if hg_heartDancer_OBJ.purchased:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                call her_main("As what?","open","worriedL")
                m "A Dancer."
                if whoring >= 15:
                    call her_main("A Dancer?","scream","angryCl")
                    m "Don't worry, your nipples will be covered."
                    call her_main("...","angry","worriedCl",emote="05")
                    call her_main("Fine, let me go change.","normal","worriedCl")
                    call play_sound("door") #Sound of a door opening.
                    call set_hermione_outfit(hg_heartDancer_OBJ)
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass

    $ current_payout = 35 #Because will have option to pay extra.

    #First Time Event.
    if hg_pf_DanceForMe_OBJ.points == 0:
        
        call bld
        m "[hermione_name], I need you to dance for me a little."
        call her_main("You want me to...","open","worried")
        
        if whoring < 9:
            call her_main("...dance for you, [genie_name]?","open","worriedL")
            jump too_much
        else:
            call her_main("...dance for you, [genie_name]?","open","wink")
            
        $ new_request_11_heart = 1
        $ hg_pf_DanceForMe_OBJ.hearts_level = 1 #Event hearts level (0-3)

        m "Yes... You think you could manage that?"
        call her_main("Ehm... I suppose so...","soft","baseL")
        her "Am I getting paid for this?"
        m "Of course, [hermione_name]!"
        call her_main("So... Just a little dancing then...","annoyed","worriedL")
        m "Whenever you're ready..."
        her "................."
        hide screen hermione_main
        with d3

        call nar(">Hermione starts dancing...","start")
        stop music fadeout 1.0

        hide screen blktone8
        call her_chibi("dance","mid","base")
        with fade
        pause.2

        m "Hm..."
        call her_head("{size=-5}(...........................................){/size}","disgust","down_raised",cheeks="blush")
        call her_head( "{size=-5}(This is silly...){/size}","annoyed","angryL",cheeks="blush")
        call nar(">Hermione looks embarrassed but she keeps on \"dancing\"...")
        m "..................."
        call her_head( "{size=-5}(...........................................){/size}","annoyed","angryL",cheeks="blush")
        m "Alright, you can start undressing now."

        call her_chibi("stand","mid","base") #Hermione stands still.
        with hpunch

        show screen blktone
        call her_head("??!","mad","wide",cheeks="blush")
        call her_head("I thought all I had to do was dance?","angry","angry")
        call play_music("playful_tension")# SEX THEME.
        m "Really? That's adorable."
        m "Now start taking off those clothes."

        show screen blktone
        call her_head("You want me to... strip for you...?","disgust","down_raised",cheeks="blush")
        m "Yes. And I expect you to do it today, [hermione_name]."
        call her_head("[genie_name]!","angry","worriedCl",cheeks="blush")
        m "Don't you raise your voice at me, [hermione_name]!"
        call her_head(".....!!?","mad","wide",cheeks="blush")
        m "Nobody is forcing you to do this."
        m "I am doing you a favour!"
        m "If you don't need the points, please feel free to leave."
        call her_head(".....................","angry","angry")
        call her_head(".......................................","disgust","down_raised",cheeks="blush")

        hide screen blktone
        call nar(">Hermione is starting to dance again...")

        call her_chibi("dance","mid","base")
        with d5

        call her_head("{size=-5}(...........................................){/size}","angry","worriedCl",cheeks="blush")
        m "What are you waiting for then?"

        if hermione_wear_top and (h_top == "uni_top_1" or h_top == "uni_top_6"):
            m "Start with the vest."

            call her_head(".............................................................","disgust","down_raised",cheeks="blush")
            call nar(">Hermione gives you a confused look and then takes off her vest...")
        else:
            call nar(">Hermione gives you a confused look...")

        if hermione_wear_top and (h_top == "uni_top_1" or h_top == "uni_top_6"):
            if h_top == "uni_top_1":
                $ h_top = "uni_top_2"
            else:
                $ h_top = "uni_top_4"
            call update_her_uniform
            pause.2

        pause.5
        show screen blktone
        call her_main("{size=-5}(Am I really going to do this?){/size}","angry","worriedCl",cheeks="blush",trans="fade",xpos="base",ypos="base")
        call ctc

        menu:
            m "......................."
            "\"Now get rid of your skirt!\"":
                call her_main(".................................","angry","worriedCl",cheeks="blush")
                
                hide screen blktone
                call nar(">Hermione starts to unzip her skirt...","start")
                ">She seems very hesitant and takes her time..."
                call nar(">Finally the zipper is undone and she has no choice but to take the skirt off...","end")
                
                call her_main("{size=-5}(Here it comes then...){/size}","angry","worriedCl",cheeks="blush")
                call her_main("{size=-5}(For the honour of \"Gryffindor\"....){/size}","angry","worriedCl",cheeks="blush")

                call nar(">Hermione takes off her skirt...")
                pause.2

                $ hermione_wear_panties = True
                call set_hermione_action("lift_skirt")
                pause.5

                $ hermione_wear_bottom = False
                call set_hermione_action("None","skip_update")
                pause.5


                m "..............."
                call her_main("{size=-5}(.........................................){/size}","angry","worriedCl",cheeks="blush")
                call nar(">Hermione keeps on dancing...")
                m "Alright, your shirt is next!"
                call her_main("My shirt....?","disgust","down",cheeks="blush")
                hide screen hermione_main
                with d3
                
                hide screen blktone
                call nar(">Hermione looks extremely embarrassed...","start")
                call nar(">She clumsily fumbles with the buttons of her shirt...","end")
                
            "\"Now take off your shirt!\"":
                call her_main(".................................","angry","worriedCl",cheeks="blush")
                
                hide screen blktone
                call nar(">Hermione starts to unbutton her shirt...","start")
                ">She seems very hesitant and takes her time..."
                call nar(">Finally the last button is undone and she has no choice but to take the shirt off...","end")
                
                call her_main("{size=-5}(Alright, here it comes...){/size}","angry","worriedCl",cheeks="blush")
                call her_main("{size=-5}(For the honour of the \"Gryffindor\"!){/size}","angry","worriedCl",cheeks="blush")
                
                call nar(">Hermione takes off her shirt...")
                pause.2

                call set_hermione_action("lift_top")
                pause.5
                
                $ hermione_wear_top = False
                call set_hermione_action("None","skip_update")
                pause.5

                call her_main("{size=-5}(I actually did it...){/size}","angry","worriedCl",cheeks="blush")
                call her_main("{size=-5}([genie_name] can see my breasts while I'm dancing for him...){/size}","angry","worriedCl",cheeks="blush")
                call her_main("{size=-5}(This is so demeaning...){/size}","angry","worriedCl",cheeks="blush")
                call her_main("{size=-5}(But I am doing this for my house...){/size}","angry","worriedCl",cheeks="blush")

                m "Not bad...."
                call her_main("{size=-5}(.........................................){/size}","angry","worriedCl",cheeks="blush")
                
                call nar(">Hermione is topless now...","start")
                ">She keeps on dancing but seems very restricted in her movements now. Even more so than before..."
                call nar(">It seems like she's desperately trying to prevent her breasts from bouncing or swaying...","end")

                m "Alright, your skirt is next!"
                call her_main("....................","angry","worriedCl",cheeks="blush")
                hide screen hermione_main
                with d3

                hide screen blktone
                call nar(">Hermione looks extremely embarrassed...","start")
                call nar(">She fumbles with the zipper of her skirt...","end")

        stop music fadeout 1.0
        m "What's the problem, [hermione_name]?"
        call play_music("sad") # HERMIONE'S THEME.

        call her_head("I'm sorry, [genie_name]...","angry","worriedCl",cheeks="blush")
        call her_head("It's stuck...","angry","worriedCl",cheeks="blush")
        call her_head("It won't budge...","angry","worriedCl",cheeks="blush")
        call her_head("Why won't it budge?! *sob*","angry","worriedCl",cheeks="blush")
        call her_head("No, I can't do this, [genie_name]! *sob*","open","surprised",cheeks="blush",tears="messy")
        m "What?"
        call her_main("I thought I could, but...","angry","suspicious",cheeks="blush",trans="fade")
        call her_main("Stripping for points, [genie_name]?","angry","suspicious",cheeks="blush")
        call her_main("People look up to me in this school!","angry","suspicious",cheeks="blush")
        call her_main("I have a reputation...*sob*","angry","suspicious",cheeks="blush")
        call her_main("And If I do this...","scream","angry",cheeks="blush",tears="messy")
        call blkfade  
        
        ">Hermione quickly puts her uniform back on..."

        call h_action("None")
        call her_chibi("stand","desk","base")

        hide screen blkfade
        call her_main("[genie_name], I think I'd better go now... *Sob!*","angry","suspicious",cheeks="blush",tears="messy",trans="fade")
        
        menu:
            "\"Alright. I had fun. Here are your points.\"":
                call her_main("Really? I didn't ruin it completely then?","soft","baseL",tears="soft")
            "\"Sure. You will receive no points though.\"":
                call her_main("[genie_name]... I may not be very good at this...","open","base",tears="mascara_crying")
                call her_main("But I did my best... I think I deserve some--",tears="mascara_crying")
                m "Just make sure you try harder next time, [hermione_name]."
                call her_main("Next time?!","open","base",tears="mascara_crying")
                call her_main("I assure you, [genie_name], there will be no next time...","angry","angry",cheeks="blush",tears="mascara")
                m "We'll see..."
                call her_main("Tsk!","disgust","glance",tears="mascara")
                $ mad += 35
                call music_block
                jump could_not_flirt

    #Second Event
    if hg_pf_DanceForMe_OBJ.points == 1:

        $ new_request_11_heart = 2
        $ hg_pf_DanceForMe_OBJ.hearts_level = 2 #Event hearts level (0-3)
        
        call bld
        m "[hermione_name], I need you to dance for me."
        call her_main("That again, [genie_name]...?","disgust","glance")
        m "You will get paid accordingly of course..."
        call her_main("............................","annoyed","angryL")
        call her_main("And you expect me to... ehm...","annoyed","angryL")
        m "Take your clothes off. Naturally."
        stop music fadeout 1.0

        show screen blktone
        call her_main("......................","annoyed","angryL")
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("Well, why not?","disgust","glance")
        call her_main("Yes, I don't see why not!","scream","angry",emote="01")
        m "Hm...? {size=-4}(Look at her, so eager all of a sudden...){/size}"
        call her_main("After all, as a pupil I am meant to obey your every order, isn't that right, [genie_name]?!","scream","angryCl")
        m "...................."
        call her_main("If the Headmaster tells me to strip for him, Then I shall strip!!!","scream","angryCl")
        call her_main("Do I find this extremely inappropriate, disgraceful and humiliating?","angry","angry")
        call her_main("Of course not. What nonsense!","scream","angryCl")
        m ".............."
        call her_main("Ha! Might as well do this the proper way!","angry","angry")

        hide screen bld1
        hide screen blktone
        hide screen hermione_main
        with d3
        pause.2

        m "??!"

        call her_walk_desk_blkfade

        $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
        pause 3
        g4 "!!!!!!"
        ">To your surprise Hermione just hops onto your desk and starts dancing franticly..."
        call her_chibi("dance","on_desk","on_desk")
        hide screen blkfade
        with fade
        pause.5

        show screen blktone
        call her_main("If I must degrade myself in order to protect the honour of my house...","scream","angryCl",xpos="mid",ypos="base")

        if hermione_wear_top and (h_top == "uni_top_1" or h_top == "uni_top_6"):
            call nar(">Hermione is starting to take off her vest...")
        call her_main("So be it then!","scream","angry",emote="01")
        call her_main("Just...","open","down")
        call her_main("*groan*","clench","down_raised")
        
        if hermione_wear_top and (h_top == "uni_top_1" or h_top == "uni_top_6"):
            call nar(">Her vest seems to be stuck somehow, but the girl keeps pulling on at the fabric with anger...")
            call her_main("Why won't it....?!")
            call her_main("There!","annoyed","annoyed")
            call nar(">Hermione finally manages to untangle herself and sends the vest flying to the other side of the room...")
        
            if h_top == "uni_top_1":
                $ h_top = "uni_top_2"
            else:
                $ h_top = "uni_top_4"
            call update_her_uniform
            pause.2

            call her_main("","","")
            pause.1

        else:
            call nar(">The girl seems to contemplate about which piece of clothing she should take off first...")
            pause.1

        call her_main("The skirt is next, right?","scream","angryCl")

        menu:
            m "..."
            "\"Yes, that's right. Take it off!\"":
                call her_main("Of course!")
                call her_main("Here it goes!","open","down")
                pause.1
            "\"You need to calm down, [hermione_name]. \"":
                call her_main("Well, {size=+7}EXCUSE ME{/size}, [genie_name]!")
                call her_main("You told me to strip for you, but you never told me your preferences in regards to the pace!")
                m "Well, I'm telling you now, [hermione_name]!"
                call her_main("Too late!","angry","angry")
                pause.1

        $ hermione_wear_panties = True
        call set_hermione_action("lift_skirt")
        pause.5

        $ hermione_wear_bottom = False
        call set_hermione_action("None","skip_update")
        pause.2

        call nar(">Hermione sends her skirt flying across the room, just like she did with her vest a moment earlier...")

        m "{size=-4}(Wow, she is getting really worked up over this...){/size}"
        m "{size=-4}(Maybe it was still too early to--{/size}"
        call her_main("My shirt?!!","disgust","glance")

        $ hermione_wear_bra = True
        call set_hermione_action("lift_top")
        pause.2

        call her_main("{size=+9}I don't need it!{/size}","scream","angry",emote="01")
        pause.2

        $ hermione_wear_top = False
        call set_hermione_action("None","skip_update")
        pause.2

        call nar(">Hermione's shirt suddenly hits the floor.")
        call her_main("","angry","angry")
        pause.2
        g4 "{size=-4}(When did she??!){/size}"
        call ctc

        call her_main("Do you enjoy this, [genie_name]?")
        call her_main("","angry","angry")

        call set_hermione_action("lift_breasts")

        call her_main("Shall I shake my breasts for you like one of those harlots?","scream","angryCl")
        m "Well---"
        call her_main("Of course! Why wouldn't I degrade myself for your pleasure?!")
        call her_main("This is completely {size=+7}acceptable!{/size}","scream","angry",emote="01")
        call her_main("","angry","angry")

        call set_hermione_action("None","skip_update")
        pause.2

        call nar(">Hermione is starting to shake her naked breasts rather clumsily...","start")
        call nar(">As you watch the girl's tits sway right and left before your face you find yourself fighting the urge to...","end")

        menu:
            m "..."
            "-Grab them!-":
                g9 "{size=-4}(Yes, just get my hands on these ample titties, that's what I want to do!){/size}"
                g9 "{size=-4}(Maybe pull on them a little, yes...){/size}"
                call slap_her #Calls slapping sound and visual.
                call her_main("","disgust","wide")
                pause.2
                call slap_her #Calls slapping sound and visual.
                call her_main("","shock","shocked")
                pause.2

            "-Slap them!-":
                m "{size=-4}(I want to slap the crap out of her fun bags.){/size}"
                call slap_her #Calls slapping sound and visual.
                call her_main("","disgust","wide")
                pause.2
                g9 "{size=-4}(Yes, just slap them around a little...){/size}"
                call slap_her #Calls slapping sound and visual.
                call her_main("","shock","shocked")
                pause.2

            "-Bite on them!":
                m "{size=-4}(Is it weird that I feel like sinking my teeth into her tits?){/size}"
                m "{size=-4}(No, it's not weird!){/size}"
                m "{size=-4}(Just a couple of gentle love-bites!){/size}"
                call kiss_her
                call her_main("","shock","wide",tears="soft")
                pause.2
                g9 "{size=-4}(Yes... Maybe more than just a couple...){/size}"
                call her_main("","disgust","worriedCl",tears="soft_blink")
                pause.2
                call kiss_her
                call kiss_her
                pause.2

            "-Motorboat them!-":
                m "{size=-4}(I'm going to put my face right in between them!){/size}"
                call kiss_her
                call her_main("","shock","worriedCl")
                pause.2
                g9 "{size=-4}(Yes, motorboating these titties is be the best!){/size}"
                call her_main("","shock","shocked")
                pause.2

        call nar(">While you are having fun with her tits, Hermione keeps on dancing...")
        
        
        call her_main("(Dancing naked in front of the headmaster...)","soft","shocked")
        call her_main("(Letting him touch my breasts...)","disgust","shocked")
        call her_main("(If my parents knew about this they would lose their minds...)","soft","shocked")
        call her_main("(Especially my father...)","annoyed","closed")
        call nar(">Hermione is starting to shake her tits again...")
        call her_main("(Hermione Granger - the stripper...)")
        call her_main("(Forgive me father...)","annoyed","dead")
        pause.1

        call nar(">Hermione puts her hands on her tits and starts squeezing them...","start")
        ">You can only assume that she means to look seductive, but she just looks awkward and ashamed."
        call her_main("(I used to be a top student... Used to have standards...)")
        ">Hermione clutches her tits even harder and then gives them a couple of twists..."
        ">It almost looks as if she is mad at her own breasts and trying to punish them..."
        call nar(">You find the thought strangely arousing...","end")

        call her_chibi("image","on_desk","on_desk","dance/05_panties_01")
        call ctc

        call her_main("Well, I hope you enjoyed yourself, [genie_name]!","open","annoyed")
        m "What?"
        call her_main("I would like to get paid now...","open","angryCl")
        m "Aren't you forgetting something, [hermione_name]?"
        call her_main("[genie_name]...?","open","annoyed")
        m "Your panties...?"
        call her_main("My panties?","open","wide")
        call her_main("But, they always leave them on!")
        m "Who exactly are \"they\"?"
        m "Strippers in kid's cartoons?"
        m "Stripping is stripping, [hermione_name]!"
        m "Now take off your panties!"
        call her_main("................","angry","wide")

        call nar(">Hermione looks horror-struck. All of her anger is gone...","start")
        call her_main(".................","annoyed","closed")
        ">Without saying another word..."
        call nar(">She starts to pull down her panties...","end")

        $ hermione_wear_panties = False
        call update_her_uniform
        call her_chibi("image","on_desk","on_desk","dance/07_dance_01")
        call her_main("","annoyed","worriedCl",cheeks="blush")
        pause.2

        g9 "......................................."

        hide screen blktone
        hide screen bld1
        hide screen hermione_main
        with d1

        stop music 
        call play_sound("door") #Sound of a door opening.

        call sna_walk("door","mid",2)


        call sna_main("Listen, Genie. I've been thinki--","snape_01",xpos="base",ypos="base")

        hide screen snape_01 #Chibi
        show screen hermione_main
        with d3

        $ renpy.play('sounds/scratch.wav')
        with hpunch

        call sna_main("............................................","snape_11")
        with hpunch

        call her_main("(Professor Snape???????!)","angry","wide")
        call sna_main("Miss Granger?","snape_12")

        call h_action("covering")
        show screen bld1
        call her_main("(No, no... This is not happening. Please...)","shock","worriedCl",cheeks="blush",trans="d5")
        call play_music("playful_tension")# SEX THEME.
        m "...................................."

        menu:
            m "..."
            "\"Severus, I am busy right now.\"":
                call sna_main("Yes... I can see that...","snape_13")
                call her_main("{size=-7}(I want to die!){/size}","angry","worriedCl")
            "\"Severus! Please, come join us.\"":
                $ mad += 20
                #$ snape_invated_to_watch = True #Removed. Turns true on a new Snape event instead. (label special_date_with_snape_03)
                call sna_main("Seriously?","snape_14")
                call her_main("([genie_name], no, please.............................)","angry","worriedCl")
                call sna_main("A very tempting offer indeed...","snape_13")
                call her_main("!!!!!!.......","angry","wide")
                call sna_main("Well, maybe some other time...","snape_13")
                call her_main("{size=-5}(There will be no other time!){/size}","angry","worriedCl")
                call her_main("{size=-5}(I will stop selling favours from now on, I swear!){/size}")

        call sna_main("I shall postpone our conversation then, Geni-- *khem!* Albus.","snape_12")
        call sna_main("Miss Granger...","snape_13")
        call her_main(".................................","angry","worriedCl")

        hide screen bld1
        show screen snape_01
        hide screen snape_main
        hide screen hermione_main
        with fade
        pause.2

        call sna_walk("mid","leave",3)
        
        call blkfade
        ">Hermione hastily hops off your desk."
        ">She starts putting her clothes back on rather frantically..."

        call her_chibi("stand","desk","base")
        call hide_blkfade

        call her_main("My shirt! Where is my shirt?!","scream","worriedCl",xpos="mid",ypos="base")
        m "It's over there, by the fireplace..."

        hide screen hermione_main
        with d3
        pause.2

        call her_walk("desk","mid",1.5)

        call her_head("................................","disgust","down_raised",xpos="base",ypos="base")
        pause.2

        $ hermione_wear_panties = True
        $ hermione_wear_top = True
        $ hermione_wear_bottom = True

        call h_action("none")

        call her_chibi("stand","mid","base",flip=True)
        pause.2
        call her_walk("mid","desk",2)

        show screen bld1
        call her_main("........................","normal","worriedCl",xpos="base",ypos="base")
        stop music fadeout 2.0
        call her_main("Can I just get my points now, please?","angry","worriedCl",emote="05")
        pause.2
        call blkfade
        pause.5
            

    #Third Event.
    if hg_pf_DanceForMe_OBJ.points >= 2:

        $ new_request_11_heart = 3
        $ hg_pf_DanceForMe_OBJ.hearts_level = 3 #Event hearts level (0-3)

        call blktone

        if snape_invated_to_watch: #Turns TRUE after Dance Event 2 and the next Date with Snape.
            m "(Hm... Should I invite Snape to watch as well?)"

            menu:
                "-\"Yes! Hermione needs an audience!\"-":
                    if not invited_snape_once_already:
                        $ invited_snape_once_already = True #Makes sure this event takes place only once.
                        hide screen blktone
                        hide screen hermione_main
                        with d3
                        
                        m "Miss, Granger, I will be buying another favour from you today."

                        call her_main("Of course, [genie_name].","open","closed",xpos="base",ypos="base")
                        m "But before that, do you think you could go and fetch professor Snape for me?"
                        call her_main("...professor Snape?","annoyed","suspicious")
                        her "May I ask, why, [genie_name]?"
                        m "Oh, I just think you could use a bigger audience for your striptease performance."
                        call her_main("My striptease performance...?!!","shock","wide")
                        call her_main("With all due respect, [genie_name]...","angry","angry")
                        call her_main("{size=-5}(Which I have oh so little left for you...){/size}","normal","frown")
                        call her_main("I refuse to degrade myself for professor Snape's amusement!","scream","angryCl")
                        m "No, no, you got it all wrong, [hermione_name]."
                        call her_main("Hm..?","soft","base")
                        m "I want to prove that professor Snape is dirty, and I need your help."
                        call her_main("!!!","shock","wide")
                        m "Yes, I want to catch him in the act!"
                        call her_main("[genie_name], I didn't realize...","open","worried")
                        call her_main("I see now...","base","base")
                        her "I am sorry for doubting you [genie_name]..."
                        m "No biggy. Now go find professor Snape and bring him here."
                        call her_main("Right away [genie_name]!","smile","angry")
                        
                    else:
                        hide screen blktone
                        hide screen hermione_main
                        with d3
                        
                        m "Miss, Granger, I will be buying another favour from you today."

                        call her_main("Of course, [genie_name].","open","closed",xpos="base",ypos="base")
                        m "But before that, do you think you could go and fetch professor Snape again?"
                        call her_main("...professor Snape?","annoyed","suspicious")
                        her "may I ask, why, [genie_name]?"
                        m "Oh, I just want you to dance for us."
                        call her_main("!!!","open","base")
                        m "I want to prove that professor Snape is dirty, and I need your help."
                        call her_main("But didn't we already establish that last time I did this?","annoyed","worriedL")
                        m "Well, ehm... sure..."
                        m "But I will need more proof if I am to take this issue to the ministry of magic!"
                        call her_main(".....","angry","angry")
                        m "So, what do you say [hermione_name]?"
                        m "One more dance for the greater good?"
                        call her_main("Well, alright...","disgust","glance")
                        m "Good. Go find professor Snape then."

                    hide screen bld1
                    hide screen hermione_main
                    with d3

                    call her_walk("mid","leave",2.5,loiter=False)
                    call blkfade

                    stop music fadeout 1.0
                    ">...................{w}...................{w}...................{w}..................."
                    call play_sound("door") #Sound of a door opening.
                    with d3
                    call her_chibi("stand","desk","base")
                    call sna_chibi("stand","mid","base")
                    call hide_blkfade
                    pause.5

                    call play_music("dark_fog")

                    show screen blktone
                    call sna_main("Genie... err, I mean Albus, you wanted to see me?","snape_01",xpos="base",ypos="base")
                    m "Yes. Are you in the mood for a little striptease?"
                    call sna_main("Oh...?","snape_05")
                    sna "Miss Granger here will be performing I assume?"
                    call her_main("..............","angry","worriedCl",emote="05",xpos="mid",ypos="base")
                    m "Yes, our little mynx is more than happy to take off her clothes for our entertainment."
                    call her_main("............","angry","worriedCl",emote="05")
                    m "Aren't you [hermione_name]?"
                    hide screen blktone
                    hide screen hermione_main
                    hide screen snape_main
                    with d3
                    pause.5

                    call her_chibi("stand","desk","base",flip=True)
                    with d1
                    pause.8

                    call her_chibi("stand","desk","base")
                    with d1
                    pause.5

                    show screen blktone
                    show screen snape_main
                    call her_main("Yes, [genie_name].","angry","worriedCl",emote="05")
                    m "Let's get started then!"
                    hide screen hermione_main
                    with d3
                    pause.2
                    call sna_main("","snape_13")
                    pause.8

                    hide screen snape_main
                    call blkfade

                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
                    pause 3
                    call her_chibi("dance","on_desk","on_desk")
                    call sna_chibi("stand","desk_close","base")

                    call her_head(".............","open","closed")
                    
                    call sna_head("......................","snape_05")
                    
                    m ".........................."
                    
                    hide screen blktone
                    call hide_blkfade
                    pause.8

                    call blktone
                    m "So... Severus... How's life?"
                    
                    call sna_main("Well, you know... same old, same old...","snape_09")
                    call sna_main(" The Students are causing me grief...","snape_06")
                    call sna_main("In fact, miss Granger here managed to cause me more stress than any other student...","snape_03")
                    pause.2
                    call her_main("...............................","grin","baseL")
                    m "Oh, I am sure she is very sorry about that..."
                    call her_main("{size=-4}(Not even a little bit!){/size}","base","happyCl")
                    m "And will make up for it today, won't you, [hermione_name]?"
                    pause.2

                    call her_main("Uhm... Yes, [genie_name].","base","squint")
                    pause.2

                    if hermione_wear_top and (h_top == "uni_top_1" or h_top == "uni_top_6"):
                        call nar(">Hermione takes her vest off and starts to sway her hips seductively.")

                        if h_top == "uni_top_1":
                            $ h_top = "uni_top_2"
                        else:
                            $ h_top = "uni_top_4"
                        call update_her_uniform
                        pause.2

                        call her_main("","","")
                        pause.1

                    else:
                        call nar(">Hermione starts to sway her hips seductively.")
                        pause.1

                    call ctc

                    call her_main("...................","open","down")
                    call sna_main("Hm... You are being suspiciously quiet, Miss Granger.","snape_05")
                    call her_main("{size=-4}(Oh no! Is he onto us?){/size}","shock","wide")
                    call her_main("I'm just doing what the headmaster told me to, Professor Snape...","grin","worriedCl",emote="05")
                    call sna_main("Aren't you going to lecture me on the \"corruption that is taking over Hogwarts\" like you do every other day?","snape_03")
                    m "Severus..."
                    call sna_main("No, Albus I want to hear little miss perfect's answer.","snape_03")
                    call her_main("I just want you to have a good time, Professor Snape...","grin","worriedCl",emote="05")
                    call sna_main("Oh! It's \"Professor Snape\" now, is it?","snape_03")
                    call sna_main("What happened to \"snape'o'doodle\" and \"Professor Snivellus\"??!","snape_10")
                    g9 "{size=-5}( \"snape'o'doodle\, heh... that's funny.){/size}"
                    call her_main(".............","grin","worriedCl",emote="05")
                    call sna_main("Yes, I know what are you calling me behind my back, you wretched girl!","snape_08")
                    call her_main("Well, maybe that's because you deserve it... Snivellus.","scream","angry",emote="01")
                    call sna_main("What?!","snape_10")
                    call sna_main("How dare you....?")
                    call sna_main("Who do you think you are? You filthy mu--","snape_15")
                    call her_main("[genie_name], one of your staff is verbally abusing me!","scream","angryCl")
                    call her_main("Are you going to allow this?")
                    call sna_main("Verbally abusing...?! You have some nerve, girl!","snape_08")
                    call sna_main("Albus, will you allow her to talk back to a teacher like that?","snape_10")
                    call her_main("[genie_name]!","scream","angryCl")
                    call sna_main("Albus!","snape_10")

                    menu:
                        m "..."
                        "\"[hermione_name], show some respect!\"":
                            $ mad += 9
                            call her_main("What?","annoyed","angry")
                            call her_main("But [genie_name]!")
                            m "Young lady, you {size=+4}will{/size} calm down now."
                            call her_main("Tsk!","disgust","glance")
                            m "And take off your skirt already, would you?"
                            call her_main(".......","annoyed","angryL")
                            call sna_main("...........","snape_13")
                        "\"Severus, you started this.\"":
                            call sna_main("What? Me?!","snape_10")
                            call her_main("Thank you, [genie_name].","base","base")
                            call sna_main("Albus, you are spoiling the girl! She must be taught a lesson!","snape_08")
                            m "...............Severus."
                            g4 "Did you hit your head?!"
                            call sna_main("I beg your pardon?","snape_03")
                            g4 "The girl is already stripping for you!"
                            g4 "What punishment are you talking about?"
                            call sna_main("Tsk... How about a flogging?","snape_16")
                            g4 "Severus!"
                            call sna_main("Alright, alright, I see your point...","snape_17")
                            m "[hermione_name], are you going to strip or are you going to climb on my desk to give us a better view?"
                            call her_main("Ehm...","open","down")
                            m "Take of your skirt, [hermione_name]!"
                            call her_main("Yes, [genie_name]...","soft","base")
                        "\"Both of you, calm the fuck down.\"":
                            m "You, tall-dark-and-handsome, calm down a bit, would you?"
                            call sna_main("I beg your pardon?","snape_03")
                            call her_main("Yes! You tell him profess--","annoyed","angryL")
                            m "You as well, you perverted little mynx!"
                            m "Calm down and take your skirt off already."
                            call her_main("I am not perverted...","annoyed","annoyed")
                            m "The skirt, [hermione_name]!"
                            call her_main("......","annoyed","angryL")
                            call sna_main(".............","snape_13")
                        "-HARDCORE-" if hardcore_difficulty_active: #Hardcore difficulty dialogue.
                            $ mad += 18
                            m "Both of you,..."
                            stop music
                            with hpunch
                            g4 "Shut the fuck up!!!"
                            g4 "You!... You good for nothing, ugly-faced, crooked-nosed-wannabe-wizard!"
                            with hpunch
                            call sna_main("(...)","snape_11")
                            call her_main("(... yikes!)","angry","wink")
                            call sna_main("(What did he just say to me?!)","snape_08")
                            g4 "Shut your stupid mouth or I will send you flying out that bloody window!"
                            g4 "That Bitch is already stripping for you, so what more do you want?!"
                            call her_main("(B-Bi--","shock","wide")
                            g4 "And you,... stripper-whore!"
                            g4 "Do what you are payed for and start stripping already!!!"
                            call her_main("......","angry","angryCl",emote="01")
                            call sna_main(".............","snape_05")
                            call her_main("...","mad","frown")
                    pause.2

                    $ hermione_wear_panties = True
                    call set_hermione_action("lift_skirt")
                    pause.5

                    $ hermione_wear_bottom = False
                    call set_hermione_action("None","skip_update")
                    pause.2

                    call nar(">Hermione swiftly takes off her \"Hogwarts\" skirt...")
                    call ctc

                    sna "Hm..."
                    call her_main("........................","open","down")
                    m "Yes, much better!"

                    call nar(">Hermione keeps on dancing, while she's Wearing nothing but her shirt now...")

                    menu:
                        m "..."
                        "\"Severus, what about that Potter boy?\"":
                            call her_main("(.....?)","soft","base")
                            call sna_main("What about him?","snape_09")
                            m "Is he still causing you grief?"
                            call sna_main("Oh...","snape_09")
                            call sna_main("Not really, no...")
                            call sna_main("To be honest I never really had a problem with the boy himself...","snape_06")
                            sna "Although I did plan to make his life here miserable because of his father..."
                            call sna_main("But lately I have way more interesting projects to occupy myself with...","snape_02")
                            call her_main("...................","soft","base")
                        "\"Severus, what about the Weasleys?\"":
                            call sna_main("What about them?","snape_09")
                            m "Are they still causing you trouble?"
                            call sna_main("Yes... More than ever.","snape_09")
                            m "Hm...?"
                            m "You seem surprisingly indifferent about that..."
                            call sna_main("That's because I know that they will get what they deserve eventually...","snape_05")
                            m "Revenge? Cool! What do you have in mind?"
                            call her_main("!!!","soft","base")
                            call sna_main("Hm... Can't discuss this with \"the enemy\" present.","snape_06")
                            call her_main("Tsk!","annoyed","angryL")
                            call sna_main("All I can say is that it involves their beloved little sister Ginny...","snape_13")
                            m "Ginny? Hm... What a curious name for a girl..."
                            m "............."
                            m "So, you plan to fuck her then?"
                            call sna_main("!!?","snape_08")
                            call sna_main("Albus, please, not in front of the girl!","snape_17")
                            m "Alright, alright..."
                            
                            #if not snapes_plan_for_ginny:
                            #    call nar(>Your curiosity about Ginny grows!)
                            #$ snapes_plan_for_ginny = True
                
                            call her_main("{size=-5}(Ginny...){/size}","open","down")
                        "\"How would you grade Hermione's butt?\"":
                            call sna_main("miss Granger's buttocks?","snape_05") 
                            call her_main("!!!............","annoyed","angryL")
                            m "Sure! As you would grade a paper."
                            call sna_main("Hm...","snape_13")
                            pause.1
                            call nar(">Professor Snape gives Hermione's buttocks an appraising look...")
                            call her_main(".........?","upset","wink")
                            call sna_main("I would say...","snape_13")
                            call her_main("............?!","base","down")
                            call sna_main("Yes... \"{size=+5}F-{/size}\".","snape_09")
                            call her_main("(What?!)","shock","wide")
                            call sna_main("Unsatisfactory...","snape_09")
                            sna "Look at that pitiful thing. Tiny and skinny... That's a boy's butt."
                            call her_main("!!!!!!!!!!","angry","annoyed",emote="01")

                    call nar(">One after another, Hermione undoes the buttons of her shirt...")
                    pause.2

                    $ hermione_wear_bra = False
                    call set_hermione_action("lift_top")
                    pause.5

                    $ hermione_wear_top = False
                    call set_hermione_action("None","skip_update")
                    pause.2

                    call nar(">Then takes it off...")
                   
                    m "Alright! We Finally get to the good stuff!"
                    call sna_main("Hm...","snape_13")
                    
                    call her_main("........","annoyed","closed")

                    menu:
                        m "..."
                        "-Start jerking off-":
                            call play_music("playful_tension")# SEX THEME
                            pause.2
                            
                            call blkfade
                            hide screen hermione_main
                            hide screen snape_main
                            pause.2

                            call her_head("[genie_name]?!","open","wide")
                            m "It's alright, [hermione_name]. Don't mind me..."
                            call sna_head("Oh, we're doing it like this then?","snape_12",xpos="base",ypos="base")
                            call sna_head("Well, don't mind if I do...","snape_12")
                            call her_head("!!!")

                            hide screen genie
                            show screen chair_02
                            call gen_chibi("jerking_off","behind_desk","base")
                            hide screen desk
                            show screen desk
                            call her_chibi("stand","on_desk","on_desk")
                            call sna_chibi("jerking_off","desk","base")
                            hide screen blktone
                            call hide_blkfade
                            call ctc

                            show screen bld1
                            call her_main("No, guys... err I mean, sirs... Ehm, professors!","angry","wide")
                            m "Don't you mind us [hermione_name], just keep on doing your thing."
                            call her_main("But...")
                            call her_main("No! I refuse to dance with those things pointed at me!","angry","worriedCl")
                            call her_main("You need to put them away or the dance is over!")
                            m "You aren't in any position to give us orders, [hermione_name]."
                            call her_main("that was not an order, [genie_name]. It was an ultimatum.","clench","angry",emote="01")

                            menu:
                                m "..."
                                "\"Alright Severus, let's be civil...\"":
                                    hide screen hermione_main
                                    with d3
                                    pause.2
                                    call sna_head("I see Miss Granger manages to remain exceptionally stubborn in any situation...","snape_03")
                                    call blkfade

                                    hide screen chair_02
                                    hide screen desk
                                    show screen genie
                                    call her_chibi("stand","on_desk","on_desk")
                                    call sna_chibi("stand","desk","base")
                                    pause.3
                                    hide screen snape_main
                                    hide screen hermione_main
                                    hide screen bld1
                                    hide screen blktone
                                    call hide_blkfade
                                    jump civil_with_snape
                                    
                                "\"(Pst! Remember why we are doing this!)\"":

                                    #Hermione is ok with it.
                                    if whoring >= 15:

                                        call her_main("Oh, right...","shock","wide")
                                        call sna_head("What was that?","snape_05")
                                        call her_main("Please don't mind what I just said...","silly","worriedCl",emote="05")
                                        call sna_head("Hm...?","snape_05")
                                        call her_main("I do not mind you touching yourself in front of me...","silly","worriedCl",emote="05")
                                        call her_main("Yes, I do not mind it at all...")
                                        call her_main("I will just keep on dancing then...")
                                        
                                        call nar(">You keep on jerking off while you're watching Hermione dance...","start")
                                        call nar(">Hermione squeezes her breasts and shakes her hips slightly...","end")
                                        
                                        m "Yes, [hermione_name]. Very good."
                                        call sna_head("*Khem!* Acceptable performance, miss Granger.","snape_12")
                                        call her_main("....................","angry","worriedCl")
                                        m "Heh..."
                                        m "So, how would you grade her tits?"
                                        call her_main("......","open","wide")
                                        call sna_head("Hm......","snape_13")
                                        call her_main("........","annoyed","angryL")
                                        call sna_head("\"B+\"!","snape_12")
                                        call her_main("!!!","open","wide")
                                        m "Really?"
                                        call sna_head("Yes. I do give credit where credit is due.","snape_12")
                                        call her_main("(Professor...)","annoyed","closed")
                                        call her_main("(Time for my finishing act then!)","open","closed")
                                        pause.1
                            
                                        $ hermione_wear_panties = False
                                        call set_hermione_action("pinch")
                                        pause.5
                                        
                                        call nar(">Hermione bends over and slides her panties down.","start")
                                        ">Her movements lack grace..."
                                        ">But a pretty pussy is always a welcome sight nonetheless..."
                                        hide screen blktone
                                        call nar(">You show your appreciation by stroking your cock even faster...","end")
                                        call ctc

                                        show screen blktone
                                        call sna_head("Yes... Yes!!!","snape_18")
                                        call sna_head("Now shake those B+ titties for me, you harlot!")
                                        call her_main(".......","angry","worriedCl")
                            
                                        call set_hermione_action("none","skip_update")
                                        pause.5

                                        call nar(">Hermione suddenly breaks into a series of rather complex pirouettes.")
                                        call sna_head("Yes, such grace...","snape_19")
                                        call sna_head("That lithe, young body!","snape_20")
                                        call her_main(".........","grin","ahegao")
                                        call sna_head("Oh, yes!","snape_20")
                                        call her_main("{size=-5}(Three-two-one... Three-two-one... And step!){/size}","grin","ahegao")
                                        call nar(">Hermione seems very focused on her dancing routine...")
                                        call sna_head("Yes, and now another pirouette!","snape_19")
                                        call sna_head("Magnificent!")
                                        call sna_head("I would applaud you but one of my hands is very busy at the moment.","snape_13")
                                        m "{size=-4}(Was that an attempt at a joke?){/size}"
                                        m "{size=-4}(Man, horny Snape is weird...){/size}"
                                        call blkfade

                                        ">Hermione performs another set of movements and pirouettes..."
                                        ">Gives a little curtsy bow to the imaginary public..."
                                        ">And then slumps down on her butt exhausted."

                                        call her_chibi("sit_naked","on_desk","on_desk")

                                        hide screen snape_main
                                        hide screen hermione_main
                                        hide screen blktone
                                        hide screen bld1
                                        call hide_blkfade
                                        call ctc

                                        show screen bld1
                                        call her_main("Whew... This was--","open","closed")
                                        with hpunch

                                        g4 "ARGH! YOU FUCKING WHORE!"

                                        hide screen bld1
                                        with d3

                                        call cum_block

                                        call gen_chibi("cumming","behind_desk","base")
                                        pause.2

                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ u_sperm = "characters/hermione/face/auto_04.png"

                                        call her_main("??!!!","shock","wide")
                                        call her_main("","angry","worriedCl")
                                        call ctc

                                        call sna_head("Good job, you harlot!","snape_18")
                                        call sna_head("Here is your reward!","snape_21")

                                        call cum_block

                                        call sna_chibi("cumming","desk","base")
                                        pause.2

                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ u_sperm = "characters/hermione/face/auto_05.png"

                                        call her_main("!!!!!!!!!!!","shock","wide")
                                        call ctc

                                        call sna_head("Oh... Yes...","snape_21")
                                        g4 "Little slut!"
                                        call her_main("...............................","grin","ahegao")
                                
                                        $ s_c_c_u_pic = "images/animation/11_cum_18.png"
                                        $ g_c_c_u_pic = "images/animation/09_cum_18.png"

                                        call sna_head("Ha-ha-ha! This is magnificent!","snape_21")
                                        g9 "I know, right!?"

                                        call gen_chibi("hold_dick","behind_desk","base")
                                        call sna_chibi("hold_dick","desk","base")
                                        pause.2

                                        call bld
                                        call sna_head("Yes... We should do this more often.","snape_22")
                                        call her_main(".................","grin","ahegao")

                                        call sna_head("Your performance was acceptable, miss Granger...","snape_20")
                                        call her_main("Thank you................","annoyed","dead")
                                        call sna_head("But if I were to grade it...","snape_19")
                                        call her_main("...........","annoyed","dead")
                                        call sna_head("Hm....","snape_22")
                                        call her_main("............","annoyed","dead")
                                        call sna_head("\"{size=+5}F+{/size}\"!","snape_10")
                                        stop music
                                        
                                        hide screen bld1
                                        show screen blktone
                                        call her_main("{size=+5}WHAT?!!!{/size}","shock","wide")
                                        call sna_head("Yes... Quite a few things could use some improvement actually.","snape_09")
                                        call play_music("chipper_doodle") # HERMIONE'S THEME.
                                        call her_main("I cannot believe this!","clench","angry",emote="01")
                                        call ctc
                                        call blkfade

                                        ">Hermione furiously jumps off your desk."
                                        pause 2
                                        hide screen hermione_main
                                        hide screen chair_02
                                        hide screen desk
                                        show screen genie
                                        call sna_chibi("hold_dick","mid","base")
                                        call her_chibi("stand","desk","base",flip=True)
                                        hide screen bld1
                                        hide screen blktone
                                        call hide_blkfade
                                        call ctc

                                        $ flip = True # Flips hermione_main screen.
                                        $ u_sperm = "characters/hermione/face/auto_05.png"

                                        show screen bld1
                                        call her_main("I demand a higher grade than that!","soft","angry",xpos="right",ypos="base")
                                        call sna_head("You do not demand a grade miss Granger, you earn it.","snape_09")
                                        call her_main("I did earn it!","open","baseL")
                                        call her_main("And could you at least have the decency to stop touching yourself, professor!","annoyed","angryL")
                                        call sna_head("Tch...","snape_12")
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3   
                                        m "(Are they for real?)"
                                        hide screen bld1
                                        with d3
                                        pause.2
                                        call blkfade

                                        ">You watch Snape with his dick still hanging out and the cum-covered Hermione argue loudly about her imaginary grade."
                                        ">After a while Professor Snape agrees to change Hermione's grade from \"F+\" to \"D-\"."
                                        ">Then he beats a hasty retreat before Hermione has a chance to start another argument..."
                                        pause 2

                                        $ flip = False # Flips hermione_main
                                        $ aftersperm = True #Show cum stains.
                                        $ uni_sperm = False #Don't show cum.
                                        call sna_chibi("stand","mid","base",flip=True)
                                        call hide_blkfade

                                        call sna_walk("mid","leave",2)
                                        pause.5

                                        call her_chibi("stand","desk","base")
                                        pause.2

                                        show screen bld1
                                        call her_main("Well...","annoyed","worriedL",xpos="mid",ypos="base")
                                        her "Was our mission a success, [genie_name]?"

                                        menu:
                                            m "..."
                                            "\"Huh? What mission?\"":
                                                $ mad += 7
                                                call her_main("I only agreed to this so that you could catch professor Snape in the act, [genie_name]!","scream","worriedCl")
                                                call her_main("So that we would have definite proof that he is \"dirty\"!","normal","worriedCl")
                                                m "Oh, that mission..."
                                                m "Yes. Mission accomplished!"
                                            "\"Yes! Thanks to you!\"":
                                                pass

                                        m "Good job, [hermione_name]."
                                        call her_main("I am happy to have been of help, [genie_name]!","normal","worriedCl")
                                        pause.5
                                        call blkfade

                                        call her_head("...Can I get paid now, please?","angry","worriedCl",emote="05")
                                        jump done_with_dancing #Blkfade needs to be active!

                                    #Hermione is ok with it.
                                    else:

                                        call her_head("Oh...","open","wide")
                                        call her_head("No, I can't! This is just not worth it!","angry","worriedCl")
                                        call blkfade

                                        ">Hermione jumps off the desk and starts to put her clothes back on."
                                        call sna_head("Well, this was awfully anticlimactic...","snape_03")
                                        g4 "You don't say..."
                                        call sna_head("May as well leave now I suppose. I will talk to you later, Albus.","snape_03")
                                        m "Yes, later, Severus."
                                        call sna_head("Miss Granger...","snape_04")
                                        call her_head("Professor...","angry","worriedCl")

                                        call sna_chibi("hide")
                                        call her_chibi("stand","desk","base")
                                        call play_sound("door")
                                        ">Professor Snape leaves..."
                                        stop music fadeout 1.0

                                        call her_head("....................","annoyed","dead")
                                        pause.5
                                        ">.................{w}.................{w}.................{w}................."
                                
                                        call her_head("...Can I get paid now... [genie_name]...?","normal","worriedCl")
                                        jump done_with_dancing #Blkfade needs to be active!


                        "-Just keep on watching-":
                            label civil_with_snape:
                                call play_music("dark_fog")

                            call her_chibi("dance","on_desk","on_desk")
                            pause.5

                            show screen blktone
                            call her_main("I will just keep on dancing then...","open","closed")
                            call ctc

                            call nar(">Hermione squeezes her breasts and shakes her hips slightly...")
                            
                            m "Yes, [hermione_name]. Very good."
                            call sna_main("*Khem!* Acceptable performance, miss Granger.","snape_12")
                            call her_main("....","open","closed")
                            m "Heh..."
                            m "So,... how would you grade her tits?"
                            call her_main("......","annoyed","closed")
                            call sna_main("Hm......","snape_20")
                            call her_main("........","annoyed","closed")
                            call sna_main("\"B+\"!","snape_12")
                            call her_main("!!!","open","wide")
                            m "Really?"
                            call sna_main("Yes. I do give credit where it's due.","snape_12")
                            call her_main("(Professor...)","angry","wide")
                            call her_main("(Time for my finishing act then!)","open","closed")
                            pause.1
                            
                            $ hermione_wear_panties = False
                            call set_hermione_action("pinch")
                            pause.5

                            call nar(">Hermione bends over and slides her panties down.","start")
                            ">Her movements lack grace..."
                            hide screen blktone
                            call nar(">But a pretty pussy is always a welcome sight nonetheless...","end")
                            call ctc
                            
                            show screen blktone
                            call sna_main("Yes... Yes...","snape_20")
                            sna "Now shake those B+ titties for me, you harlot!"
                            call her_main(".......","angry","worriedCl")
                            
                            call set_hermione_action("none","skip_update")
                            pause.5

                            call nar(">Hermione suddenly breaks into a series of rather complex pirouettes.")
                            call sna_main("Yes, such grace...","snape_19")
                            call sna_main("That lithe, young body!","snape_20")
                            call her_main("{size=-5}(Three-two-one... Three-two-one... And step!){/size}","open","closed")
                            call nar(">Hermione seems very focused on her dancing routine...")
                            call sna_main("Yes, and now another pirouette!","snape_19")
                            call sna_main("Magnificent!")
                            call blkfade

                            ">Hermione performs another set of movements and pirouettes..."
                            ">Gives a little curtsy bow to the imaginary public..."
                            ">And then slumps down on her butt exhausted."

                            call her_chibi("sit_naked","on_desk","on_desk")

                            hide screen snape_main
                            hide screen hermione_main
                            hide screen blktone
                            hide screen bld1
                            call hide_blkfade
                            call ctc

                            show screen bld1
                            call sna_main("Good job, you harlot!","snape_22")
                            call her_main(".............","soft","squintL")

                            if daytime:
                                call sna_main("Well, my class is about to start so I will be leaving now.","snape_22")
                                sna "Don't you have potion class with me today, Miss Granger?"
                                call her_main("Yes, [genie_name]...","annoyed","dead")
                                call sna_main("Well, don't be late, girl...","snape_22")
                            else:
                                call sna_main("Well, it is getting rather late. I think I will be leaving now.","snape_22")
                                sna "Good night, Albus."
                                m "Severus."
                                call sna_main("Harlot.","snape_22")
                                call her_main("Professor...","annoyed","dead")

                            call ctc

                            hide screen hermione_main
                            hide screen snape_main
                            call blkfade

                            ">Professor Snape leaves..."
                            stop music fadeout 1.0
                            call her_head("....................","annoyed","dead")
                            pause.5
                            ">.................{w}.................{w}.................{w}................."
                            
                            call her_head("May I... may get paid now... [genie_name]...?","normal","worriedCl")
                            jump done_with_dancing #Blkfade needs to be active!

                ### SNAPE NOT INVITED ###
                "-\"Nah... That's not a good idea...\"-":
                    label no_snape_watching: 
                    hide screen blktone
                    hide screen hermione_main
                    with d3

                    m "[hermione_name], how about another strip?"     
                    call her_main("..............","disgust","glance",xpos="base",ypos="base")
                    her "I would really rather not, [genie_name]..."
                    m "Why? You are getting quite good at it."
                    call her_main(".........................","annoyed","annoyed")
                    call her_main("Thirty five house points?","open","down")
                    m "Sure! The usual rate."
                    call her_main("...................","annoyed","angryL")
                    hide screen hermione_main
                    hide screen bld1
                    with d3
                    pause.5
                    
                    
                    #Walks to the door
                    call her_walk("mid","door",2)
                    pause.2
                    $ tt_xpos=670
                    $ tt_ypos=200
                    show screen thought 
                    with d3
                    pause.5
                    $ renpy.play('sounds/09_lock.wav') #Sound of a door opening.
                    hide screen thought
                    with d3
                    pause.2
                    
                    #Returns from the door
                    m "??!"
                    pause.2
                    
                    call her_chibi("stand","door","base")
                    pause.1

                    call her_walk("door","mid",3)
                    pause.2
                    
                    show screen bld1
                    call her_main("Just in case...","annoyed","angryL")
                    stop music fadeout 1.0

                    hide screen bld1
                    with d3
        
                    call her_walk("mid","desk",3, redux_pause = 2,loiter=False)
                    call blkfade
                    pause.5
        
                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
                    pause 3
                    call her_chibi("dance","on_desk","on_desk")

                    call her_head("Just for the record...","open","closed")
                    call her_head("I still consider this a highly inappropriate favour to be buying from one of your students, [genie_name].","annoyed","suspicious")
                    m "Right. And an equally inappropriate favour to be selling to your headmaster. Woulnd't you agree?"
                    call her_head("..........","annoyed","angryL")

                    call hide_blkfade
                    call ctc
                    
                    call play_music("playful_tension")# SEX THEME.
                    show screen blktone
                    call her_main("..............","open","down",xpos="mid",ypos="base")
                    call her_main("What if my parents were to find out about this, [genie_name]?","disgust","down_raised")
                    call her_main("Mother would never understand...")
                    call her_main("As for my father...","upset","wink")

                    menu:
                        m "..."
                        "{size=-3}\"Your father would be proud of you!\"{/size}":
                            call her_main("I doubt it...")
                            call her_main("Yes, I am doing this for the right reasons, but...")
                            call her_main("He would never see it that way...","annoyed","angry")
                            call her_main("He must never know about this...")
                        "{size=-3}\"Your father would spank you hard!\"{/size}":
                            call her_main("He would not!","shock","wide")
                            call her_main("And I am too old for that anyways...","upset","wink")
                            g9 "I would say that you are in the perfect age for that..."
                            call her_main("Huh?")
                            call her_main("I do not know what you mean, [genie_name].","grin","worriedCl",emote="05")
                        "{size=-3}\"Your father would disown you!\"{/size}":
                            call her_main("You are probably right, [genie_name]...","angry","worriedCl",emote="05")
                            call her_main("(Oh father, I am so sorry...)","angry","base",tears="soft")
                            call her_main("he must never find out...","angry","base",tears="soft")
                        "{size=-3}\"Your father love to would watch you strip!\"{/size}":
                            call her_main("He would not! He would be ashamed of me!","normal","worriedCl")
                            m "Are you sure about that?"
                            call her_main("absolutely! My father is a man of integrity!","scream","worriedCl")
                            m "But he {size=+4}is{/size} a {size=+4}man{/size}, right?"
                            call her_main(".....................","annoyed","annoyed")
                            call her_main("My father must never know about this...","annoyed","worriedL")

                    call nar(">Hermione is starting to sway her hips rather seductively...")

                    $ hermione_wear_panties = True
                    call set_hermione_action("lift_skirt")
                    pause.5

                    $ hermione_wear_bottom = False
                    call set_hermione_action("None","skip_update")
                    pause.2

                    call nar(">While she slides her skirt down...")
                    call ctc
                    
                    call her_main("[genie_name]?","open","base")
                    m "Huh?"
                    call her_main("Can I ask you a question?","upset","wink")
                    m "Go ahead..."
                    call her_main("...............","normal","worriedCl")
                    call her_main("Have you ever been in love...?","grin","worriedCl",emote="05")

                    menu:
                        m "..."
                        "\"Don't be ridiculous! Love is a lie!\"":
                            call her_main("I am sorry you think that way, [genie_name]!","annoyed","worriedL")
                            call her_main("But you couldn't be more wrong!","annoyed","annoyed")
                            call her_main("I believe that true love is what makes the earth turn!","base","baseL")
                            m "Actually the conservation of angular momentum is responsible for that."
                            call her_main("Huh?","upset","wink")
                            m "Never mind. Just take off your shirt already?"
                            call her_main("............","annoyed","annoyed")      
                        "\"Be quiet and keep on dancing!\"":
                            call her_main("But you said I could ask you a question...","annoyed","annoyed")
                            m "And you did, didn't you?"
                            call her_main("!!!............","open","base")
                            call her_main("....................................","annoyed","annoyed")
                            m "Now, hush and take your shirt off."
                            call her_main("........","annoyed","angryL")
                        "\"Yes... a very long time ago...\"":
                            m "Yes... a very long time ago..."
                            call her_main("!!!!!??..............................","open","base")
                            m "Her name was Eden..."
                            call her_main("Was she beautiful?","base","base")
                            m "She was so much more than that..."
                            m "She was smart, green and perfect..."
                            call her_main("She was... \"green\"...?","open","down")
                            call her_main("Are you making fun of me, [genie_name]?","angry","angry")
                            m "Oh, you humans know nothing of true love..."
                            call her_main(".....................................?","soft","base")
                            m "Err... I mean, take off that shirt, [hermione_name]!"
                            call her_main(".................","annoyed","angryL")
                        "\"I feel like I'm in love right now!\"":
                            call her_main("You don't have to be vulgar, [genie_name].","annoyed","angryL")
                            m "Oh, but I mean it!"
                            call her_main("[genie_name], please!","disgust","glance")
                            call her_main("I am one of your students!","soft","base")
                            call her_main("And you are older than my father!","grin","worriedCl",emote="05")
                            m "{size=-4}(You have no idea, girl.){/size}"
                            call her_main("Although some scientists insist that what we consider \"love\" is actually nothing but a chemical reaction...","soft","base")
                            call her_main("And when a man is experiencing sexual arousal, the same type of hormones--","open","closed")
                            m "[hermione_name]!"
                            call her_main("Yes, [genie_name]?","soft","base")
                            m "Did you forget where you are?"
                            call her_main("Oh, my apologies, [genie_name]... I get distracted sometimes.","grin","worriedCl",emote="05")
                            m "Take off your shirt already, would you?!"
                            call her_main("Right...","annoyed","worriedL")

                    call nar(">Hermione undoes the last button of her shirt...")

                    $ hermione_wear_bra = False
                    call set_hermione_action("lift_top")
                    pause.5

                    $ hermione_wear_top = False
                    call set_hermione_action("None","skip_update")
                    pause.2

                    call nar(">And takes it off somewhat gracefully...")
                    call ctc

                    g9 "Yes! The tits!"
                    
                    call her_main("Must you be so vulgar, [genie_name]?","annoyed","closed")

                    menu: 
                        "-Take your cock out, start jerking off-":
                            call blkfade
                            
                            call her_head("[genie_name]?!","open","wide")
                            m "It's alright, [hermione_name]. Don't mind me..."
                            
                            
                            hide screen genie
                            hide screen no_shirt_no_skirt_dance
                            show screen chair_02
                            call gen_chibi("jerking_off","behind_desk","base")
                            hide screen desk
                            show screen desk
                            call her_chibi("dance","on_desk","on_desk")
                            hide screen blktone
                            call hide_blkfade
                            call ctc
                            
                            call bld
                            call her_head("B-but...","angry","wide")
                            call her_head("Your...")
                            m "Yes... Ah, yes, this is good..."
                            call her_head("[genie_name]!!!","scream","worriedCl")
                            call her_head("I must insist that you put away your...","angry","worriedCl")
                            call her_head("...thing.")
                            
                            menu:
                                m "..."
                                "\"I said, keep on dancing, [hermione_name]!\"":
                                    if whoring >= 15: #LEVEL 06. You jerk off your cock and Hermione is OK with it.
                                        call her_head("But...","angry","worriedCl")
                                        call her_head(".............................")
                                        call her_head("Well, alright, but only if you will promise me not to....finish, [genie_name].","soft","angry")
                                        menu:
                                            m "..."
                                            "-Promise her to hold it-":
                                                    $ d_flag_07 = True #Promised to hold it.
                                                    call her_head("Well, alright then...","open","closed")
                                            "-Give her no such promise-":
                                                $ d_flag_07 = False #Did not promise to hold it.
                                                m "\"Not to finish\"? That would be like torture!"
                                                m "Please keep your sadistic urges to yourself, [hermione_name]."
                                                call her_head("I don't have any... sadistic urges, [genie_name]!","annoyed","angryL")
                                                call her_head("I just don't want to...")
                                                g9 "Yes... Those are some nice tits you have..."
                                                call her_head("............","angry","worriedCl")
                                                g9 "A-ah... Yes..."
                                                call her_head("..........","angry","worriedCl")
                                                call her_head("Fine! Have it your way, [genie_name]!","angry","worriedCl")
                                                call her_head("{size=-5}(As usual...){/size}","annoyed","angryL")
                                                
                                        hide screen bld1
                                        show screen blktone
                                        call nar(">You keep on wanking while you watch Hermione's dance...")
                                        call her_main("Time for the finishing act I suppose...","annoyed","closed")
                                        m "Yes, [hermione_name]! Take them off!"
                                        call her_main("........","annoyed","dead")
                                        if h_request_wear_panties or hermione_wear_panties:
                                            call nar(">Hermione bends over slightly and slides her panties down...")
                                        
                                            $ hermione_wear_panties = False
                                            call set_hermione_action("pinch")
                                            pause.5

                                            call set_hermione_action("None","skip_update")
                                            pause.2

                                        call nar(">You can see that she is doing her best to be graceful...","start")
                                        call nar(">But she looks rather ridiculous in her attempts to act like a professional stripper...","end")
                                        call ctc
                                        
                                        call nar(">None the less you decide to show her some appreciation...","start")
                                        call nar(">By stroking your cock even faster!","end")
                                        call her_main("..........","annoyed","dead")
                                        call nar(">Suddenly Hermione breaks into a whole series of rather complex pirouettes...")
                                        m "{size=-4}(This looks quite impressive actually...){/size}"
                                        
                                        call set_hermione_action("fingering")
                                        pause.5

                                        call nar(">Hermione gives her breasts a squeeze followed by another series of rather complex (and naughty) movements...")
                                        call ctc
                                        
                                        m "{size=-4}(Did she practice this?){/size}"
                                        g9 "Oh, what do I care?"
                                        call nar(">You stroke your diamond-hard cock furiously.")
                                        call her_main("{size=-5}(Three-two-one... Three-two-one... And step!){/size}","open","closed")
                                        
                                        call set_hermione_action("none","skip_update")
                                        pause.5

                                        call nar(">Hermione performs another set of movements that could be considered classy...","start")
                                        call nar(">if not for her naked tits bouncing all over the place...","end")
                                        
                                        g9 "Yes, yes, you little whore!"
                                        call nar(">A few more movements, a couple of gestures and a little curtsy bow to the imaginary public...")
                                        call blkfade
                                        
                                        call her_chibi("sit_naked","on_desk","on_desk")
                                        
                                        ">And then Hermione slumps on her butt, completely exhausted."
                                        
                                        hide screen hermione_main
                                        hide screen blktone
                                        call hide_blkfade
                                        call ctc
                                        
                                        call her_head("Whew... This was--","open","closed")
                                        with hpunch
                                        g4 "ARGH! YOU FUCKING CUNT!"
                                        
                                        call cum_block
                                        
                                        call gen_chibi("cumming","behind_desk","base")
                                        call ctc
                                        
                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ u_sperm = "characters/hermione/face/auto_04.png"
                                        
                                        call her_chibi("sit_naked_shocked","on_desk","on_desk")
                                        
                                        call her_head("??!!!","shock","wide")
                                        
                                        call bld
                                        call her_head("[genie_name]!!!","angry","worriedCl")
                                        
                                        call gen_chibi("hold_dick","behind_desk","base")
                                            
                                        $ g_c_c_u_pic = "images/animation/09_cum_18.png"
                                        $ genie_cum_chibi_xpos = -45
                                        $ genie_cum_chibi_ypos = 5
                                        show screen g_c_c_u
                                        
                                        if d_flag_07: #Promised to hold it.
                                            call her_head("No, [genie_name]! You promised!","angry","worriedCl")
                                            g4 "Oh, man... This was pretty intense..."
                                            call her_head("You went back on your word, [genie_name]!","scream","worriedCl")
                                            m "Huh? What are you talking about?"
                                            call her_head("How could you do this to me, [genie_name]?","shock","angry",tears="crying_blink")
                                            m "Oh, calm down, [hermione_name]."
                                            m "You earned your points today."
                                            m "Now, just get dressed and leave before somebody discovers you like this."
                                            call her_head("*sob!*........................","shock","angryL",tears="messy")
                                            $ mad += 30
                                            call blkfade
                                            
                                            $ uni_sperm = False #Sperm layer is not displayed.
                                            $ aftersperm = True #Aftersperm layer is displayed. 
                                            stop music fadeout 5.0
                                            ">.................{w}.................{w}.................{w}................."
                                            call her_head("...Can I just get paid now, [genie_name]... please?","annoyed","angryL")
                                            jump done_with_dancing
                                            
                                        else:
                                            call her_head("it's so hot...","angry","worriedCl")
                                            call gen_chibi("hold_dick","behind_desk","base")
                                            m "Aha... Yeah... This feels great..."
                                            call her_head("You came all over me...","soft","squintL")
                                            call her_head("I am your pupil and...")
                                            call her_head("You just came on me...","grin","ahegao")
                                            g9 "I know! Pretty exciting stuff, huh?!"
                                            call her_head("Nothing of that sort!","open","baseL")
                                            #her "You should not have done this, [genie_name]!"
                                            call her_head("You should have restrained yourself like a proper headmaster would!")
                                            m "Really? What did you expect me to do?"
                                            m "Aim at the wall or just put it back in my pants and start cumming?"
                                            call her_head("........","soft","squintL")
                                            call her_head("Still, you should not have...","soft","angry")
                                            call her_head("I agreed to perform a striptease for you...","open","closed")
                                            call her_head("But I didn't agree to be defiled like this.")
                                            m "I think I know where this is going..."
                                            call her_head("I demand to be paid extra!","base","angry")
                                            m "Of course you do..."
                                            
                                            menu:
                                                m "..."
                                                "\"You get 1 extra point.\"":
                                                    call play_music("chipper_doodle") # HERMIONE'S THEME.
                                                    call her_head("One extra point?","soft","angry")
                                                    call her_head("One meager extra point for letting you do this to me?","scream","worriedCl")
                                                    call her_head("Now, that is just insulting, [genie_name]!","soft","angry")
                                                    m "One extra point, [hermione_name]. Take it or leave it."
                                                    hide screen g_c_c_u
                                                    call her_chibi("sit_naked","on_desk","on_desk")
                                                    show screen g_c_c_u
                                                    
                                                    call her_head(".............","annoyed","angryL")
                                                    call her_head("I'll take it.","soft","angry")
                                                    $ mad += 30
                                                    $ current_payout = 36
                                                    hide screen bld1
                                                    call ctc
                                                    
                                                    call blkfade
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                    
                                                "\"You get 10 extra points.\"":
                                                    $ current_payout = 45
                                                    call her_head("Ten extra points [genie_name]?","soft","angry")
                                                    call her_head("But that is not even nearly enough!")
                                                    m "Ten extra points. Take'em or leave'em [hermione_name]."
                                                    hide screen g_c_c_u
                                                    call her_chibi("sit_naked","on_desk","on_desk")
                                                    show screen g_c_c_u
                                                    
                                                    call her_head("...............","annoyed","angryL")
                                                    call her_head("Well, alright... Better than nothing I suppose...","soft","angry")
                                                    $ mad += 11
                                                    hide screen bld1
                                                    call ctc
                                                    
                                                    call blkfade
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                    
                                                "\"You get 25 extra points.\"":
                                                    $ current_payout = 60
                                                    hide screen g_c_c_u
                                                    call her_chibi("sit_naked","on_desk","on_desk")
                                                    show screen g_c_c_u
                                                    
                                                    call her_head("Yes, I believe this would be an appropriate amount.","open","closed")
                                                    m "are we good then?"
                                                    call her_head("Yes, [genie_name]. Thank you [genie_name].","open","closed")
                                                    hide screen bld1
                                                    with d3
                                                    call ctc
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                    
                                                "\"You get 50 extra points.\"":
                                                    $ current_payout = 85
                                                    call her_head("Seriously?!","angry","wide")
                                                    hide screen g_c_c_u
                                                    call her_chibi("sit_naked","on_desk","on_desk")
                                                    show screen g_c_c_u
                                                    
                                                    call her_head("Oh, I don't know what to say...","open","wide")
                                                    m "I enjoyed your performance [hermione_name]."
                                                    call her_head("Thank you [genie_name]...","base","glance")
                                                    m "I also enjoyed plastering your agile little body with cum..."
                                                    call her_head("[genie_name]......","silly","worriedCl",emote="05")
                                                    m "So, just allow me to show my appreciation."
                                                    m "Fifty extra points. Well deserved, [hermione_name]."
                                                    call her_head("Thank very much, [genie_name].","silly","worriedCl",emote="05")
                                                    hide screen bld1
                                                    call ctc
                                                    
                                                    call blkfade
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                    
                                                "\"You're not getting shit!\"":
                                                    stop music fadeout 1.0
                                                    call her_head("What? Not even my usual pay?","shock","wide")
                                                    menu:
                                                        m "..."
                                                        "\"Oh, no, you are still getting that.\"":
                                                            $ mad += 30
                                                            call her_head("How generous of you, [genie_name].","soft","angry")
                                                            hide screen bld1
                                                            call ctc
                                                            
                                                            call blkfade
                                                            $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                            jump done_with_dancing
                                                            
                                                        "\"No, not even that!\"":
                                                            call play_music("chipper_doodle") # HERMIONE'S THEME.
                                                            call her_head("!!!?","shock","wide")
                                                            call her_head("I danced for you, [genie_name]...")
                                                            call her_head("I degraded myself for your amusement...","soft","squintL")
                                                            call her_head("I let you cum on me...","open","baseL")
                                                            with hpunch
                                                            call her_head("And I get NOTHING?!","clench","angry",emote="01")
                                                            m "You are dismissed, [hermione_name]!"
                                                            call her_head("Oh, this is a new low even for you, [genie_name]!","soft","angry")
                                                            m "I said you are dismissed."
                                                            call her_head("*GROAN!*","clench","angry",emote="01")
                                                            $ mad += 50
                                                            hide screen bld1
                                                            call ctc
                                                            
                                                            call blkfade
                                                            call gen_chibi("hide")
                                                            hide screen g_c_c_u # Genie's sperm. Universal.
                                                            hide screen chair_02
                                                            hide screen desk
                                                            show screen genie
                                                            show screen bld1
                                                            call her_chibi("stand","desk","base")
                                                            pause.1
                                                            call hide_blkfade
                                                            call music_block
                                                            jump could_not_flirt #Leaves without getting any points.
                                                        

                                    else: # You jerk off your cock and Hermione is NOT OK with it.
                                        stop music fadeout 1.0
                                        
                                        call her_head("No, [genie_name]!","annoyed","angryL")
                                        m "Huh?"
                                        call blkfade
                                        
                                        ">Hermione jumps off your desk and starts to put her clothes back on while glaring at you..."
                                        m "Oh, come on! Don't leave me like that!"
                                        
                                        call her_head("The dance is over, [genie_name]!","soft","angry")
                                        pause 1
                                        call her_head("I would like to get paid now!","annoyed","annoyed")
                                        m "Stubborn [hermione_name]..."
                                        ">You reluctantly put your cock away..."
                                        call her_head("I would like to get paid now.","annoyed","annoyed")
                                        jump done_with_dancing
                                        
                                "\"Fine. There is no need for drama!\"": 
                                    call her_head("......................","annoyed","angryL")
                                    pause.1
                                    
                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen desk
                                    call gen_chibi("hide")
                                    show screen genie
                                    call her_chibi("dance","on_desk","on_desk")
                                    hide screen blktone
                                    hide screen bld1
                                    with fade
                                    pause.5
                                    
                                    pass
                                    
                        "-Show some manners, just watch-":
                            pass


                    # JUST WATCHING.
                    call blktone
                    call nar(">You watch Hermione Dance...")
                    call her_main("(Time for the finishing act I suppose...)","angry","worriedCl")
                    if h_request_wear_panties or hermione_wear_panties:
                        m "Yes, [hermione_name]! Take them off!"
                        call her_main("........","annoyed","closed")
                    
                        $ hermione_wear_panties = False
                        call set_hermione_action("pinch")
                        pause.5

                        call set_hermione_action("None","skip_update")
                        pause.2
                    
                        call nar(">Hermione bends over slightly and slides her panties down...")
                        
                    call nar(">You can see that she is doing her best to be graceful...","start")
                    call nar(">But she looks rather ridiculous in her attempts to act like a professional stripper...","end")
                    call ctc
                    
                    call her_main("..........","base","glance")
                    
                    call nar(">Suddenly Hermione breaks into a whole series of rather complex pirouettes...")
                    m "{size=-4}(This looks quite impressive actually...){/size}"
                                        
                    call set_hermione_action("fingering")
                    pause.5

                    call nar(">Hermione gives her breasts a squeeze followed by another series of rather complex (and naughty) movements...")
                    call ctc
                                        
                    m "{size=-4}(Did she practice this?){/size}"
                    g9 "Oh, why would I care?"
                    call her_main("{size=-5}(Three-two-one... Three-two-one... And step!){/size}","open","closed")
                                        
                    call set_hermione_action("none","skip_update")
                    pause.5

                    call nar(">Hermione performs another set of movements that could be considered classy...","start")
                    call nar(">if not for her naked tits bouncing all over the place...","end")
                                        
                    g9 "Yes, yes, you little harlot!"
                    
                    call nar(">A few more movements, a couple of gestures and a little curtsy bow to the imaginary public...")
                    call blkfade
                                        
                    call her_chibi("sit_naked","on_desk","on_desk")               
                    
                    ">And then Hermione slumps on her butt, completely exhausted."
                                        
                    hide screen hermione_main
                    hide screen blktone
                    call hide_blkfade
                    call ctc
                    
                    call her_head("Whew... This was rather exciting...","silly","worriedCl",emote="05")
                    menu:

                        m "..."
                        "{size=-3}\"Good job, [hermione_name]! You sure know how to dance!\"{/size}":
                            m "Good job [hermione_name]!"
                            call her_head("Really?","base","glance")
                            m "Yes! You have a lot of talent for this!"
                            call her_head("Thank you [genie_name].","silly","worriedCl",emote="05")
                        "{size=-3}\"Hm... This was quite awful...\"{/size}":
                            call her_head("Oh... I'm sorry...","soft","squintL")
                            m "That's OK... You just need to practice more..."
                            call her_head("Em... I will keep that in mind, [genie_name]...","open","baseL")
                        "{size=-3}\".................................................\"{/size}":
                            call her_head(".......................","silly","worriedCl",emote="05")
                            call her_chibi("sit_naked_shocked","on_desk","on_desk")

                    hide screen bld1
                    call ctc
                    
                    call blkfade

                            
        else: #Stripping only for Genie.
            jump no_snape_watching 

        
        
    label done_with_dancing:       
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen s_c_c_u # Snape's sperm. Universal.
    hide screen chair_02
    hide screen desk
    call gen_chibi("hide")
    call sna_chibi("hide")
    show screen genie
    call her_chibi("stand","desk","base")

    call h_action("none")

    show screen bld1
    call hide_blkfade
    
    m "Yes, [hermione_name]. [current_payout] to the \"Gryffindor\" house."
    
    call her_main("Thank you, [genie_name]...","soft","baseL",xpos="base",ypos="base")
    hide screen hermione_main
    hide screen bld1
    with d3

    $ sperm_on_tits = False
    $ uni_sperm = False
    
    pause.2
    call her_walk("desk","leave",3)
    
    call reset_hermione_main

    if whoring < 12: #Adds points till 12.
        $ whoring +=1

    $ hg_pf_DanceForMe_OBJ.points += 1
    
    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if daytime:
        call play_music("day_theme")
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        call play_music("night_theme")
        $ hermione_sleeping = True
        jump night_main_menu     
    







