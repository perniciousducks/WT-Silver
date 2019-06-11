

label luna_favour_5: #Luna jerks Genie off onto Hermione's face #DONE

    if lun_whoring <= 11:
        $ lun_whoring += 1
        m "[lun_name], how would you feel about selling another favour?"
        call lun_main("...","base","seductive","angry","mid")
        call lun_main("What is it this time [lun_genie_name]?","base","angry","angry","R")
        m "Well, do you remember how we had a little fun with miss granger the other day?"
        call lun_main("...","base","seductive","angry","mid")
        call lun_main("go on...","base","suspicious","angry","R")
        m "how would you feel about bringing her up her for a little more fun?"
        call lun_main("You really are a disgusting pervert aren't you?","base","angry","mad","mid")
        m "..."
        call lun_main("Aren't you...","normal","suspicious","angry","mid")
        m "Yes..."
        call lun_main("at least you're honest about it...","base","mad","sad","R")
        call lun_main("Which is more than I can say for that two-faced slut hermione...","upset","wide","mad","mid")
        m "So you're OK with having a little fun with her?"
        call lun_main("on one condition.","base","angry","mad","mid")
        m "Name it."
        call lun_main("I'm in control. No matter what.","normal","mad","angry","R")
        call lun_main("Even if you think what's happening is too mean...","upset","mad","angry","mid")
        call lun_main("I am in control... got it?","normal","suspicious","mad","mid")
        m "Done."
        call lun_main("alright then...","base","happyCl","sad","mid")
        call lun_main("I also expect to be paid 150 gold for my troubles...","normal","angry","sad","mid")
        m "Certainly."
        call lun_main("...","base","seductive","angry","R")
        call lun_main("Now [lun_genie_name]...","upset","angry","mad","mid")
        m "Alright then..."
        ">You pay Luna 150 gold."
        $ gold -=150
        $ luna_gold += 150
        call lun_main("thank you [lun_genie_name]...","normal","angry","sad","R")
        call lun_main("...","normal","angry","raised","mid")
        call lun_main("Well come on then, summon her...","pout","mad","angry","mid")
        ">You summon Hermione. Somehow..."

        call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

        $ luna_flip = -1
        $ luna_r_arm = 2
        $ luna_xpos = 390
        call update_her_uniform

        call her_main("hello Prof-","soft","baseL",xpos="right",ypos="base")
        call her_main("Luna! what are you doing here?","angry","wide")
        call lun_main("same thing as you...","base","seductive","angry","mid")
        call her_main("Oh, um... you must be here to... help Professor dumbledore then...","open","worriedL")
        call lun_main("Mhmmm...","base","angry","sad","mid")
        call her_main("So, ugh... what does dumbledore need our help with?","open","worried")
        call lun_main("Probably emptying those nasty balls of his...","upset","mad","angry","mid")
        call her_main("!!!","angry","wide")
        call her_main("Luna! what are you talking about?","angry","worried")
        call her_main("are you feeling ok?","annoyed","worriedL")
        call lun_main("come on now hermione... it wouldn't be the first time you've helped old dumbledore like this?","base","angry","angry","R")
        call lun_main("would it...?","normal","angry","angry","mid")
        call her_main("I have no idea what you're talking about!","scream","angryCl")
        call her_main("Professor dumbledore must be mistaken...","scream","angryCl")
        call her_main("M-Maybe he needs to go to the nurses and have his mind checked...","scream","angryCl")
        call lun_main("So you're not selling favours to dumbledore in exchange for points?","normal","suspicious","raised","mid")
        call her_main("certainly not! I'd never do something so underhanded!","scream","worriedCl")
        call lun_main("Really?","upset","angry","raised","mid")
        call her_main("Of course not! I'm shocked you even have to ask!","annoyed","worriedL")
        call lun_main("So you're comfortable saying that after you've had a sip of some veritaserum?","normal","mad","mad","mid")
        call her_main("!!!","angry","wide")
        call her_main("O-O-Of course... but as you know, that potion's banned...","open","closed")
        call lun_main("Not for the illustrious Professor dumbledore!","base","seductive","sad","R")
        call lun_main("Isn't that right sir?","upset","angry","mad","R")
        m "Oh, um yes of course I can get that easily..."
        m "(What the hell is veribatium?)"
        call her_main("!!!","annoyed","frown") #angry face
        call her_main("surely you know there's no need for that sir!","normal","frown") #angry face
        m "..."
        call her_main("...","annoyed","frown")
        call lun_main("...","base","angry","base","mid")
        call her_main("Fine! I admit it!","scream","worriedCl")
        call lun_main("See... Isn't it better to tell the truth?","base","mad","sad","mid")
        call her_main("...","normal","worriedCl")
        call her_main("So is that why I've been brought here? To be ridiculed!?","angry","angry")
        call her_main("I'm not ashamed of what I've done for my house!","annoyed","annoyed")
        call lun_main("No, you've been brought here to sell dumbledore one of those favours.","base","seductive","angry","mid")
        call her_main("What?","upset","wink")
        call her_main("Why are you here then?","soft","base")
        call lun_main("To help you.","base","angry","sad","mid")
        call her_main("...","annoyed","angry")
        call her_main("Help how?","disgust","glance")
        call lun_main("Why don't you take your clothes off and I'll show you...","base","mad","sad","mid")
        call her_main("[genie_name]... please...","scream","worriedCl")
        m "I'm sorry [hermione_name], my hands are tied..."
        call her_main("...","normal","worriedCl")
        call her_main("Do I have to?","angry","worriedCl",emote="05")
        call lun_main("Of course not... So long as you don't mind me telling your precious \"MRM\" what's been going on.","base","mad","mad","mid")
        call her_main("...","mad","worried",tears="soft")
        call her_main("FINE!","mad","worriedCl",tears="soft_blink")
        call her_main("I see how it is!","annoyed","annoyed",tears="crying")
        ">Hermione pulls off her top in a huff."

        hide screen hermione_main
        $ hermione_wear_top = False
        $ hermione_wear_bra = False

        call her_main("Feel free to humiliate me!","angry","angry",tears="crying")
        ">Hermione angrly removes her skirt."

        call set_her_action("strip")

        call her_main("for trying to do what's right!","annoyed","annoyed",tears="crying")
        ">Hermione stands naked before you and Luna. Her face is contorted in what seems like an equal mix of rage and embarrassment."
        call her_main("there! are you happy now you two?","annoyed","annoyed")
        m "Ye-"
        call lun_main("almost...","base","seductive","sad","down")
        call lun_main("now why don't you get on your knees...","upset","angry","angry","mid")
        call her_main("!!!","angry","wide",tears="crying")
        call her_main("please, luna... I'm {size=-2}sorry {size=-2}about {size=-2}what I said to you the other day...{/size}","annoyed","down",tears="crying")
        call lun_main("then kneel...","normal","suspicious","sad","mid")

        hide screen hermione_main
        $ her_chibi_xpos = 40 #40 = Near Luna
        $ her_chibi_ypos = 60
        $ h_c_u_pic = "characters/hermione/chibis/dance/sit_naked_blink.png"
        $ hermione_xpos=590
        show screen h_c_u
        with d3

        call her_kneel("...","annoyed","ahegao")
        call lun_main("there... isn't this simpler? Is this not your natural state?","normal","base","angry","down")
        call her_kneel("...","annoyed","down")
        call lun_main("now... I'll need your help for this next bit Professor.","base","seductive","sad","R")
        m "What do I need to do?"
        call lun_main("come and stand before your star student.","base","angry","angry","down")
        ">You get up out of your chair and walk over to the two girls."

        show screen blkfade
        hide screen bld1
        with d3

        hide screen genie
        show screen chair_left
        show screen desk
        $ gen_chibi_xpos = -20
        $ gen_chibi_ypos = 10
        $ g_c_u_pic = "characters/hermione/chibis/grope_breasts/masturbate_01.png"
        show screen g_c_u
        hide screen blkfade
        with d5
        call ctc

        ">Hermione looks up at you with a pleading expression."
        call her_kneel("[genie_name]... please... what's going on?","mad","worried",tears="soft")
        call lun_main("I said that you're here to sell a favour.","normal","angry","angry","down")
        call lun_main("Isn't that you want? To sell favours to dumbledore?","base","seductive","sad","mid")
        call her_kneel("I want... I want \"gryffindor\" to win the house cup...","open","down")

        if gryffindor > slytherin:
            call lun_main("But \"gryffindor\" is already ahead by "+str(gryffindor-slytherin)+" points...","pout","angry","raised","down")
            call lun_main("do you really think that they need any more points to win?","base","angry","sad","down")
            call her_kneel("...","soft","squintL")
        else:
            call lun_main("do you really think it's fair for you to win by selling your body?","normal","mad","angry","down")
            call lun_main("*tch* *tch* *tch* what would your parents think?","pout","angry","angry","down")
            call her_kneel("they wouldn't understand...","annoyed","angryL")

        ">Luna puts her hand in your robes and quickly pulls out your hardening cock."
        $ luna_r_arm = 3
        $ luna_flip = 1
        $ luna_xpos = 640
        $ hermione_xpos = 590
        $ hermione_ypos = 390

        hide screen genie_main
        $ genie_xpos = 550
        $ genie_ypos = 0
        $ genie_base = "characters/genie/base/open.png"
        call gen_main("!!!","grin")
        call lun_main("Just admit it...","base","mad","sad","mid")
        call lun_main("you're a slut...","base","suspicious","base","mid")
        call her_kneel("{size=-5}no... I'm... a good student...{/size}","open","baseL")
        call ctc

        ">Luna starts sliding her smooth hand up and down your cock."
        call lun_main("hmmmm... I'm not so sure a good student would do this...","pout","seductive","sad","R")
        call her_kneel("...","soft","squintL")
        call lun_main("kneel willingly in front of their headmaster..","base","angry","angry","down")
        call her_kneel("...","grin","ahegao")
        call lun_main("naked...","base","mad","angry","mid")
        call her_kneel("...","angry","down_raised")
        call lun_main("While another student jerks him off...","base","seductive","sad","R")
        call her_kneel("...","soft","ahegao")
        call lun_main("Waiting patiently to be covered in cum...","grin","mad","sad","down")
        call her_kneel("{image=textheart}{image=textheart}{image=textheart}","grin","dead")
        call ctc

        call lun_main("in fact, I can think of only one sort of student who'd do that...","base","seductive","angry","down")
        call lun_main("do you know what sort of student that is hermione?","base","angry","sad","mid")
        call her_kneel("ah...{image=textheart} a...","soft","squintL")
        call lun_main("Mhmmm, go on...","base","seductive","angry","down")
        call her_kneel("ah... {p}a slut...{image=textheart}","open","baseL")
        call lun_main("good girl...","base","seductive","sad","down")
        call her_kneel("{image=textheart}{image=textheart}{image=textheart}","grin","dead")
        m "Ah... almost there [lun_name]..."
        ">Luna gives your cock a hard squeeze."
        g9 "Ah!"
        call lun_main("not yet old man!","upset","mad","mad","mid")
        call lun_main("she hasn't learnt her lesson yet!","base","mad","mad","down")
        m "What else does she need to do?"
        call lun_main("...","pout","angry","angry","R")
        call lun_main("Lick it...","upset","mad","sad","down")
        call her_kneel("...","shock","wide")
        call her_kneel("OK...","soft","squintL")
        ">Hermione opens her mouth and puts out her tongue."
        call her_kneel("ah...","open_wide_tongue","squintL")
        call lun_main("...","upset","angry","angry","mid")
        call lun_main("seems like I have to do everything then...","normal","suspicious","angry","R")
        ">Luna pulls you forward, harshly, by your cock into Hermione's open mouth."
        g4 "!!!"

        $ luna_xpos += 45
        $ genie_xpos += 45
        $ luna_xpos += 10
        $ genie_xpos += 10
        $ hermione_kneel_cock = True

        call her_kneel("...","open_wide_tongue","ahegao")
        ">Hermione starts running her tongue along the length of your cock, lubricating it while Luna continues to stroke."
        g4 "Ah!!!"
        g4 "This is it sluts!"
        call lun_main("do it...","base","seductive","sad","mid")
        call her_kneel("mmmm...{image=textheart}{image=textheart}{image=textheart}","open_wide_tongue","ahegao")
        call lun_main("cover the slut...","base","angry","mad","down")
        g9  "Argh! by the gods {size=+10}YES!{/size}"

        $ luna_xpos -= 45
        $ genie_xpos -= 45
        $ luna_xpos -= 10
        $ genie_xpos -= 10
        $ hermione_kneel_cock = False

        g9  "{size=+10}TAKE IT ALL YOU sLUT!{/size}"
        show screen white
        pause.1
        $ luna_r_arm = 4
        hide screen white
        pause.2
        $ uni_sperm = True
        $ u_sperm = "characters/hermione/face/auto_07.png"
        show screen white
        pause .1
        hide screen white
        with hpunch
        $ luna_r_arm = 3

        ">You erupt over Hermione's face, coating her in a thick layer of spunk."
        call her_kneel("!!!!","silly","ahegao_raised",cheeks="blush")
        g9 "{size=+10}YES!{/size}"
        call lun_main("mmmm, good girl...","base","seductive","sad","down")
        ">Luna's hand slowly continues to stroke your cock, jerking out the last couple of drops of sperm onto Hermione's nose."
        call ctc

        call lun_main("perfect...","base","base","sad","down")
        call her_kneel("...","grin","dead")
        m "that was fantastic!"

        $ luna_r_arm = 1
        hide screen genie_main
        with d3
        hide screen bld1
        show screen genie
        hide screen chair_left
        hide screen desk
        hide screen g_c_u

        call lun_main("...","base","seductive","sad","mid")
        $ luna_flip = -1
        $ luna_xpos = 300

        if luna_addicted == True:
            call lun_main("well it's not over yet...","base","seductive","sad","R")
            call her_kneel("...what?","mad","wide",cheeks="blush")
            call her_kneel("why?","open","baseL",cheeks="blush")
            call lun_main("Just look at you!","grin","wide","sad","down")
            call lun_main("Covered in the [lun_genie_name]s delicous cum!","base","seductive","sad","down")
            call her_kneel("delicous...","disgust","down_raised")
            call her_kneel("Do you want me to clean myself up?","upset","wink")
            call lun_main("And waste all that perfectly good cum one some tart like you?!","upset","wide","angry","down")
            call lun_main("No, I think I'll have to clean this mess up myself...","base","wide","sad","down")
            ">You notice a hunger in Luna's eyes..."
            call her_kneel("does that mean...","disgust","glance")
            call lun_main("come on hermione, we don't have all day...","normal","angry","angry","R")
            call lun_main("tranfiguration starts in 5 minutes...","upset","angry","mad","R")
            call lun_main("so hurry up...","normal","angry","angry","down")
            call her_kneel("(I can't be late to mcgonagall's class...)","annoyed","down")
            call her_kneel("I'm not sure what you want me to do...","annoyed","angryL")
            call lun_main("stand up now slut...","normal","suspicious","mad","down")
            call her_kneel("...","annoyed","angry")

            hide screen hermione_kneel
            $ hermione_xpos = 480
            show screen hermione_main
            with d3

            ">Hermione slowly stands up, her face still covered in cum..."
            call lun_main("mmmmm... look at you... you smell so good...","base","base","sad","empty", cheeks="blush")
            $ luna_xpos = 600
            $ luna_r_arm = 2
            ">Luna moves closer to Hermione before picking up a strand of cum with her finger and moving it to her mouth."
            call her_main("!!!","angry","wide")
            m "(woah...)"
            $ luna_xpos = 630
            call lun_main("mmmmm... you taste even better...","base","happyCl","sad","mid")
            call her_main("...","open","worriedCl")
            ">Hermione stands still, letting luna slowly wipe the cum from her face..."
            $ u_sperm = "characters/hermione/face/auto_08.png"
            call her_main("...","shock","worriedCl")
            call lun_main("mmmmm...","full","happyCl","sad","mid")
            ">Luna slowly fills her mouth with cum before eventually swallowing."
            call lun_main("*gulp*","base","seductive","sad","empty")
            ">Eventually she finally gets the last strand into her mouth."
            $ uni_sperm = False
            call her_main("...","disgust","down_raised")
            call lun_main("...","full","happyCl","sad","mid")
            call lun_main("*gulp*","base","seductive","sad","empty")
            call her_main("...","annoyed","worriedL")
            $ luna_l_arm = 2
            $ luna_flip = 1
            $ luna_xpos = 300
            call lun_main("Well, I better be off to... class...","base","base","angry","R")
            call lun_main("Good bye [lun_genie_name]...","base","seductive","sad","mid")
            call lun_main("Good bye slut...","normal","angry","angry","R")

            call lun_chibi("leave")

            ">Luna quietly exits the room."
            call reset_luna
            $ luna_busy = True

            ">Hermione quietly gets dressed, a shocked look on her face..."

        else:
            call lun_main("well it's not over yet...","base","suspicious","angry","R")
            call her_kneel("...what?","mad","wide",cheeks="blush")
            call her_kneel("why?","open","baseL",cheeks="blush")
            call lun_main("Just look at the mess you made!","normal","angry","angry","down")
            call lun_main("You'll have to clean that up before you can go to class!","base","angry","mad","down")
            call her_kneel("well normally I just go the prefect bathroom...","annoyed","worriedL")
            call her_kneel("or I use a towel...","annoyed","down")
            call her_kneel("{size=-5}but never scourgify for some reason...{/size}","annoyed","angryL")
            call lun_main("And waste all that perfectly good cum the Professor gave you?!","upset","wide","angry","down")
            call lun_main("No, I think I'll have to stay here and make sure you dispose of it properly...","base","angry","angry","down")
            call her_kneel("does that mean...","angry","wide")
            call lun_main("come on hermione, we don't have all day...","base","seductive","sad","down")
            call lun_main("tranfiguration starts in 5 minutes...","normal","angry","angry","down")
            call her_kneel("(I can't be late to mcgonagall's class...)","angry","down_raised")
            call lun_main("now dispose of that cum like a good little slut...","base","mad","sad","down")
            call her_kneel("...","soft","ahegao")
            ">Hermione slowly starts using her fingers to push your cum into her mouth."
            $ luna_l_arm = 4
            call lun_main("mmmmm... that's it... make sure you get it all slut...","base","seductive","sad","down", cheeks="blush")
            m "(woah...)"
            ">Hermione slowly continues to clear her face of cum."
            $ u_sperm = "characters/hermione/face/auto_08.png"
            call her_kneel("...","full_cum","dead") #Cheek full
            ">She fills her mouth with cum before eventually swallowing."
            call her_kneel("*gulp*","cum","worriedCl")
            ">Eventually she finally gets the last strand into her mouth."
            $ uni_sperm = False
            call her_kneel("...","full_cum","dead") #Cheek full
            call lun_main("see, good sluts don't waste anyting do they?","grin","seductive","sad","down")
            call her_kneel("...","full_cum","dead") #Cheek full
            $ luna_l_arm = 2
            call lun_main("Well, I better be off to... class...","base","base","angry","R")
            call lun_main("Good bye [lun_genie_name]...","base","seductive","sad","mid")
            call lun_main("Good bye slut...","normal","angry","angry","R")

            call lun_chibi("leave")

            call her_kneel("","cum","worriedCl")
            ">Hermione swallows the last mouthful of your cum."
            call her_kneel("*gulp*","cum","worriedCl")
            call her_kneel("mmmm...{image=textheart}{image=textheart}{image=textheart}","grin","dead")
            ">She picks herself up from the floor gracefully. Getting dressed before turning to address you."

        call set_her_action("none","update")

        call her_chibi("stand","mid","base")
        call update_her_uniform
        hide screen hermione_kneel

        call her_main("[genie_name], what on earth was that all about?!","scream","angryCl")
        call her_main("Why on earth was Luna in here?","annoyed","angryL")
        call her_main("how on earth does she know about me selling favours?","angry","angry")
        if luna_addicted == True:
            call her_main("And {size=+5}why on earth{/size} does she love the taste of your cum?","angry","angry",emote="01")
        m "I can explain everything..."
        call her_main("Please do...","annoyed","annoyed")
        m "do you remember how you yourself described Luna lovegood as crazy?"
        call her_main("Of course. Everyone knows she's Loony Luna.","annoyed","angryL")
        m "Well I was testing out some new magic..."
        m "And I'm attempting to cure her of her previous condition..."
        m "(I hope she believes this schlock...)"
        call her_main("Really?","shock","wide")
        call her_main("But isn't messing around with her mind a little...","soft","squintL")
        call her_main("unethical?","angry","down_raised")
        m "Yes, well normally you'd be right, but this is more of a curing of an existing mental condition."
        m "Think about it like I'm trying to cure her of Aspergers disease."
        call her_main("Actually sir, Aspergers has been reclassified as part of the autism spectrum and is no longer considered it's own disease.","open","closed")
        m "..."
        m "(Of course she'd know that...)"
        m "Well anyway, my point is there's nothing untoward happening."
        call her_main("...","annoyed","angryL")
        call her_main("Alright then...","open","closed")
        call her_main("But why is she so mean?","open","worriedCl")
        m "I'm not sure. Maybe that's the true her."
        call her_main("I guess that's not impossible...","annoyed","down")
        call her_main("But why was she jerking you off?","open","down")
        m "Oh um..."
        m "Well that sort of just happened during my evaluation..."
        m "She wanted to help her fathers magazine anyway possible, and one thing led to another..."
        if luna_addicted == True:
            call her_main("what about the her loving the taste of your sperm?","angry","suspicious",cheeks="blush")
            m "Honestly I'm not really sure about that."
            m "I think that's just her being weird..."
        call her_main("...","annoyed","angry")
        call her_main("ugh, fine...","annoyed","baseL")
        call her_main("I guess...","annoyed","angryL",cheeks="blush")
        m "So you don't mind helping out with her in the future?"
        call her_main("What? I have to spend more time with her?","soft","wide")
        call her_main("But she's weird...","open","worriedCl",cheeks="blush")
        m "We can work on that. Besides, don't you want to help out one of your friends?"
        call her_main("Hmmm, I suppose that you're right [genie_name].","annoyed","closed")
        call her_main("I can't imagine that the daydreaming Luna would do too well in the real world.","open","squint",cheeks="blush")
        call her_main("and as her friend It's my responsibility to try and save her from that!","open","baseL",cheeks="blush")
        call her_main("!!!","soft","wide")
        call her_main("Maybe we could even have study sessions together!","grin","baseL")
        call her_main("I've always wanted someone to study with! Normally it's only ever Harry and I'm pretty sure he's just there to stare at my boobs...","annoyed","annoyed")
        call her_main("(Not that I mind...)","open","baseL")

        menu:
            "-Encourage friendship-":
                $ luna_friendship = 1
                $ luna_hatred = 0
                m "I'm sure she'd be happy to spend some more time with you."
                call her_main("Do you think so sir? She seemed pretty mean today.","open","down")
                m "She'll come around, just give it time."
                call her_main("I hope so sir! A ravenclaw study buddy would be great!","smile","happyCl",emote="06")
                m "(more like fuck buddy...)"
                call her_main("...","base","happyCl")
            "-discourage friendship-":
                $ luna_friendship = 0
                $ luna_hatred = 1
                m "I'm not so sure about that. She seemed pretty harsh today."
                call her_main("hmmm, you're probably right.","annoyed","base")
                m "Maybe you should fight fire with fire?"
                call her_main("And be mean in return?","disgust","down_raised")
                call her_main("I don't know, [genie_name]... She is my friend...","clench","down_raised")

        m "Anyway, thanks for your help today."
        call her_main("anything for my friends [genie_name]...","soft","squintL")
        m "(Does that mean me?)"
        m "Yes, well, 60 points to \"gryffindor\"!"
        $ gryffindor += 60
        call her_main("Thank you [genie_name]...","open","baseL")

        call her_walk(action="leave", speed=2.5)

        $ luna_busy = True
        $ hermione_busy = True

        jump end_hermione_event

    elif lun_whoring <= 12: #second time
        $ lun_whoring += 1
        $ luna_payout = 150
        $ hermione_payout = 40
        m "How would you feel about another handjob involving Miss Granger?"
        call lun_main("Really?","normal","angry","raised","mid")
        call lun_main("You want to bring her into this again?","upset","mad","angry","mid")
        m "If it's not too much of an issue..."
        call lun_main("*Hmph* so long as you pay me I don't care about you dragging that little hussie up here...","normal","suspicious","angry","R")
        m "Fantastic! I'll summon her now."
        call lun_main("...","upset","suspicious","angry","R")

        ">You summon Hermione to your office."

        call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

        $ luna_flip = -1
        $ luna_r_arm = 2
        $ luna_xpos = 390
        call update_her_uniform

        call her_main("Hello [genie_name]...","base","base",xpos="right",ypos="base")
        call her_main("Hello Luna...","open","suspicious")
        call lun_main("Hermione...","normal","suspicious","angry","mid")
        call her_main("What are you doing here?","annoyed","angryL")
        call lun_main("Getting ready to Jerk dumbledore off onto your face...","base","seductive","angry","mid")
        call her_main("Oh...","annoyed","base")
        call her_main("again?","upset","wink")
        m "Can you blame me?"
        call her_main("I suppose not...","grin","baseL")
        call lun_main("well then...","normal","mad","angry","mid")
        call her_main("what?","annoyed","angry")
        call lun_main("hurry up and strip so we can get this over with...","normal","suspicious","angry","R")
        call her_main("Why do I always have to strip?","scream","angryCl")
        call lun_main("because I said so...","upset","suspicious","base","mid")
        call lun_main("unless you don't want to...","normal","angry","base","R")
        call her_main("I suppose I don't mind. It just seems a little unfair that it's only me though...","annoyed","ahegao")
        call lun_main("tough.","upset","suspicious","mad","mid")

        menu:
            "-make luna strip-":
                m "Now, now, Miss Granger is right. It seems only fair for both of you to go nude."
                call lun_main("...","normal","wide","angry","R")
                call her_main("Come on Luna... we're both girls, there's no need to be embarrassed.","grin","baseL")
                call lun_main("embarrassed? hardly.","normal","suspicious","angry","R")
                call her_main("well hurry up and strip then. I thought you wanted to get this over with?","smile","baseL")
                call lun_main(".........","normal","angry","mad","mid")
                call lun_main("Fine... But I expect extra for this [lun_genie_name]!","normal","base","angry","R")
            "-agree with Luna-":
                m "Now, now, Listen to luna [hermione_name]."
                call her_main("What? Why?","angry","angry")
                m "Well, if we're being honest, it's mainly because I want to see your naked body again..."
                call her_main("oh... well alright then.","base","squint")
                call lun_main("and you don't want to see me naked?","normal","mad","angry","mid")
                m "I didn't mean it like-"
                call lun_main("*hmph* I suppose I'll strip then [lun_genie_name]... Just so you remember who has the better body.","normal","seductive","angry","mid")
                call lun_main("But I expect extra for this [lun_genie_name]!","upset","angry","angry","R")
        m "sure. I'll add another 40 gold."
        $ luna_payout += 40
        call her_main("If she's getting extra then I want some more points!","scream","angryCl")
        m "whatever. An extra 20 points for gryffindor then."
        $ hermione_payout += 20
        call her_main("yay!","smile","baseL")
        call lun_main("I still can't believe you get excited over points.","normal","suspicious","angry","up")
        call her_main("Why? Don't you want to see that look of excitement on your friends faces when they win the house cup?","base","squint")
        call her_main("and the look of dissapointment on those nasty slytherins faces when they lose!","base","ahegao_raised")
        call lun_main("pfft, friends...","normal","base","mad","R")
        call her_main("aww... Luna...","open","worried")
        call lun_main("Just shut up and strip slut.","upset","mad","mad","mid")
        call her_main("fine...","annoyed","down")
        show screen blkfade
        with d3

        ">Luna and Hermione both strip in front of you."
        ">You can hardly believe your eyes as they slowly strip down in front of each other."
        ">As they're putting their clothes in a pile you slowly get up from your desk and whip your cock out from in between your robes."
        call lun_main("On your knees then, slut...","base","seductive","angry","mid")
        hide screen hermione_main
        $ her_chibi_xpos = 40 #40 = Near Luna
        $ her_chibi_ypos = 60
        $ h_c_u_pic = "characters/hermione/chibis/dance/sit_naked_blink.png"
        $ hermione_xpos=590
        show screen h_c_u
        with d3

        hide screen bld1
        hide screen genie
        show screen chair_left
        show screen desk
        $ gen_chibi_xpos = -20
        $ gen_chibi_ypos = 10
        $ g_c_u_pic = "characters/hermione/chibis/grope_breasts/masturbate_01.png"
        show screen g_c_u
        with fade

        $ luna_r_arm = 3
        $ luna_flip = 1
        $ luna_xpos = 640
        $ hermione_xpos = 590
        $ hermione_ypos = 390
        $ genie_xpos = 550
        $ genie_ypos = 0
        show screen genie_main

        $ luna_wear_top = False
        $ luna_wear_bra = False
        $ luna_wear_bottom = False
        $ luna_wear_panties = False
        hide screen blkfade
        with d3

        call her_kneel("...","base","closed")
        ">Luna slowly starts jerking your cock in front of Hermione's face."
        ">Her technique is rough and inexperienced, but decent enough."
        $ luna_r_arm = 3
        call lun_main("mmmm, that's it [lun_genie_name]...","base","seductive","angry","mid")
        call her_kneel("...","annoyed","worriedL")
        call her_kneel("......","annoyed","angry")
        call her_kneel(".........","annoyed","annoyed")
        call lun_main("something wrong hermione?","normal","angry","angry","down")
        call her_kneel("no...","annoyed","down")
        call lun_main("good. maybe you sh-","base","seductive","angry","down")
        call her_kneel("You're doing it all wrong!","scream","angry",emote="01")
        call lun_main("What?","normal","wide","base","down")
        call her_kneel("that's not how he likes it.","annoyed","angryL")
        call lun_main("are you sure? He seems to be enjoying it to me...","upset","angry","angry","down")
        call her_kneel("he's just being nice. You need to focus on the tip with the palm of your hand more.","annoyed","angry")
        call her_kneel("otherwise he doesn't shoot nearly as much...","annoyed","annoyed")
        call lun_main("*hmph*","normal","angry","angry","R")
        call lun_main("Why don't we ask the old pervert who he prefers then...","normal","mad","mad","down")
        call her_kneel("alright. Who do you prefer [genie_name]?","annoyed","base")

        menu:
            "-Luna-":
                call her_kneel("What!","angry","angry",emote="01")
                call her_kneel("That's ridiculous! I'm much better than her at giving handjobs!","annoyed","annoyed")
                call lun_main("It's about more than just jerking his cock hermione.","base","angry","base","mid")
                call her_kneel("like what?","annoyed","angryL")
                call lun_main("it's about excitement...","base","seductive","angry","mid")
                ">Luna gives your cock light squeeze."
                m "Ah..."
                call her_kneel("*hmph* at least let me show you how it's done...","disgust","glance")
                call her_kneel("i'm sure you'll find plenty of ways to \'excite\' him from the floor.","annoyed","annoyed")
            "-Hermione-":
                call lun_main("WHAT?","upset","wide","base","mid")
                ">Luna gives your cock a painful squeeze, bordering on bruising it."
                $ genie_base = "characters/genie/base/hard.png"
                call gen_main("AH!","angry")
                call her_kneel("Don't take it too hard Luna, I just have a \'little\' more experience.","base","happyCl")
                ">Luna lets go of your cock."
                $ genie_face = "characters/genie/face/base.png"
                $ luna_r_arm = 1
                call lun_main("*hmph*, I suppose you're right. You've probably spent all year with your hands wrapped around any cock you could find.","upset","suspicious","mad","mid")
                call her_kneel("Hey!","annoyed","annoyed")
                call lun_main("Am I wrong?","base","angry","angry","mid")
                call her_kneel("...","disgust","down_raised")
                call her_kneel("at least let me show you how it's done...","annoyed","annoyed")

        call lun_main("whatever...","normal","suspicious","angry","R")
        call her_kneel("...","base","baseL")
        show screen blkfade
        with d3

        $ hermione_zorder = 4 #CHANGE BACK TO 5 AFTER THIS
        hide screen hermione_kneel
        ">Hermione grabs a hold of your cock as she and Luna switch places."
        ">You're unable to deny that she's much more experienced that Luna, quickly bringing you to the edge."
        $ luna_ypos = 250
        $ hermione_right_arm = "characters/hermione/body/arms/right/dick.png"
        $ genie_base = "characters/genie/base/open.png"
        $ genie_face = "characters/genie/face/grin.png"
        $ hermione_xpos = 590


        call set_her_action("strip")
        call update_her_uniform

        show screen hermione_main
        hide screen blkfade
        with d3

        m "Ah... this is it [hermione_name]... not long now."
        call her_main("mmm, that's it [genie_name]. just enjoy yourself.","open","baseL")
        call lun_main("as if he could...","normal","angry","angry","R")
        g9 "ah..."
        call lun_main("go on [lun_genie_name], tell her i'm better.","normal","mad","angry","up")
        ">you can barely mutter more than a guttural moan in response."
        g9 "Ugh..."
        call lun_main("...","normal","suspicious","angry","up")
        call lun_main("tell her i'm better!","upset","suspicious","mad","up")
        g9 "mmmm"
        call her_main("I'm not sure he can hear you... He must be enjoying himself too much.","open","down")
        call her_main("speaking of which... are you ready [genie_name]?","soft","squintL")
        g9 "Ugh... yes... here it comes sluts!"
        call her_main("well why don't I show Luna here how to give a proper handjob.","base","down")
        call lun_main("...","normal","seductive","sad","R")
        call her_main("See, he likes it when you do this with your palm...","base","suspicious")
        call cum_block

        $ luna_cum = 12
        $ luna_wear_cum = True
        g4 "{size=+5}ARGH! by the gods YES!!!{/size}"
        g4 "{size=+5}WHAT ARE YOU DOING GIRL!?!?!{/size}"
        ">Your cock explodes over Luna's face, covering her until you can barely make out her features."
        $ luna_cum = 12
        $ luna_wear_cum = True
        call lun_main("mmmmm...","base","wide","sad","mid")
        call her_main("that's it, just let out all that {b}nasty{/b} cum.","grin","ahegao")
        $ g_c_u_pic = "characters/hermione/chibis/grope_breasts/masturbate_01.png"
        $ genie_base = "characters/genie/base/open.png"
        $ luna_cum = 12
        ">Luna then collects a stand of cum on the end of her finger starting at it intently before putting it into her mouth."
        call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","angry","angry","mid")
        call lun_main("it's not nasty!","base","seductive","angry","mid")
        call her_main("oh that's right... I almost forgot how much of a cumslut you are.","angry","down_raised")
        call lun_main("I am not!","normal","angry","angry","up")
        call her_main("so you're not going to eat all of that \'delicous\' cum on your face then?","base","suspicious")
        call lun_main("...","base","seductive","angry","mid")
        ">You watch in awe as Luna slowly heaps your cum in her mouth and swallows it."
        $ luna_cum = 13
        call lun_main("...","full","seductive","sad","empty")
        call her_main("that's it Cumslut...","base","glance")
        call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","happyCl","sad","mid")
        call ctc

        $ luna_cum = 14
        call lun_main("...","full","seductive","sad","empty")
        call her_main("keep going...","base","down")
        call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","happyCl","sad","mid")
        $ luna_cum = 15
        call lun_main("...","full","seductive","sad","empty")
        call her_main("mmmm...","grin","baseL")
        call lun_main("{image=textheart}{image=textheart}{image=textheart}","base","happyCl","sad","mid")
        $ luna_wear_cum = False
        call lun_main("...","full","seductive","sad","empty")
        call lun_main("*gulp*","base","happyCl","sad","mid")
        call lun_main("ah...","base","happyCl","sad","mid")
        call lun_main("amazing...","base","seductive","sad","up")
        call lun_main("I didn't know it was possible for someone to cum so much...","base","base","sad","up")
        call her_main("well of course you didn't. I'm surprised you were able to make [genie_name] cum at all!","open","closed")
        call her_main("what with that shoddy technique of yours...","annoyed","suspicious")
        call lun_main("it's not that bad...","normal","angry","sad","up")
        call her_main("whatever you have to tell yourself...","open","closed")
        call lun_main("...","normal","mad","angry","up")
        call lun_main("fine... i'm not as good at giving hand jobs as you...","normal","suspicious","base","R")
        call lun_main("but that's only because you've spent the entire year in here Whoring yourself out to our headmaster!","normal","suspicious","mad","up")
        call her_main("well I can teach you a few things if you'd like.","smile","baseL")
        call lun_main("what?","pout","angry","base","up")
        call lun_main("why would you help me?","normal","angry","sad","up")
        call her_main("I wouldn't be doing it for free...","open","baseL")
        call lun_main("...","normal","seductive","angry","mid")
        call lun_main("what do you want?","upset","suspicious","sad","up")
        call her_main("before I tell you, you have to answer one question...","open","baseL")
        call lun_main("alright...","normal","suspicious","angry","mid")
        m "(ugh... I need to sit down after all that.)"
        hide screen hermione_main
        hide screen luna_main
        hide screen genie_main
        show screen blkfade
        with d3

        ">You slowly move back to your desk and sit down while hermione and luna continue talking."
        $ hermione_xpos = 550
        $ luna_ypos = 0
        $ luna_xpos = 450
        $ luna_l_arm = "1"
        $ luna_r_arm = "1"
        $ luna_flip = -1

        $ hermione_right_arm = "characters/hermione/body/arms/right/right_1.png"
        $ hermione_zorder = 5

        call load_hermione_clothing_saves
        call update_her_uniform

        call gen_chibi("sit_behind_desk")
        call her_chibi("stand","mid","base")
        show screen hermione_main
        hide screen blkfade
        call lun_main("","normal","suspicious","angry","mid",xpos="mid",ypos="base")

        call her_main("how are your grades?","soft","glance")
        call lun_main("WHAT?","open","wide","sad","mid")
        call lun_main("my grades? why do you care?","pout","angry","angry","mid")
        call her_main("it's a simple question...","base","down")
        call lun_main("well I'm not going to answer it...","upset","mad","mad","mid")
        call her_main("if you don't want to answer, I'm sure dumbledore would be more than happy to...","base","glance")
        call lun_main("...","upset","suspicious","mad","mid")
        call lun_main("......","upset","mad","angry","mid")
        call lun_main(".........","normal","angry","angry","mid")
        call lun_main(".............","normal","suspicious","angry","R")
        call lun_main("fine...","normal","suspicious","sad","R")
        ">Luna slowly lists her marks across all subjects, most of them bordering on a pass and fail with the exception of divination."
        call her_main("what? so low? How do you expect to get a job at the ministry of magic with marks like that?","scream","wide_stare")
        call lun_main("...","normal","suspicious","sad","down")
        call her_main("at this rate you'll have to get a job in the muggle world.","disgust","down_raised")
        call lun_main("you think I don't know that? why do you think I agreed to all this in the first place...","upset","angry","angry","mid")
        call lun_main("Just stop humiliating me and list your stupid demand!","upset","mad","angry","mid")
        call lun_main("What is it anyway? Do you expect me to walk around the school half naked?","upset","suspicious","angry","R")
        call her_main("Of course not...","open","worried")
        call lun_main("then what?","normal","angry","mad","mid")
        call her_main("In exchange for me teaching you how to be a better lover, I want you to be my study buddy.","open","closed")
        call lun_main("...","upset","suspicious","angry","mid")
        call lun_main("what?","normal","wide","sad","mid")
        call lun_main("why would you of all people need a study buddy? Aren't your grades perfect?","normal","suspicious","angry","mid")
        call her_main("of course... but that's not why I want a study buddy.","soft","baseL")
        call her_main("It gets lonely in the library sometimes...","annoyed","angryL")
        call her_main("Plus I've always wanted a ravenclaw to study with, but all the other girls refuse to even talk to me.","open","worried")
        call her_main("and harry and ron have just started staring at my tits the whole time.","open","angryCl")
        call her_main("{size=-5}not that I really mind...{/size}","base","ahegao_raised")
        call her_main("but think about all the fun we can have! you can even quiz me on advanced transmogrification spells!","smile","happyCl")
        call lun_main("...","normal","angry","angry","mid")
        call her_main("not to mention we can work on your grades as well!","base","happyCl")
        call her_main("If you work hard we can probably get them up before the O.W.L.s!","grin","baseL")
        call lun_main("whatever... as long as you teach me how to wring as much gold out of the old mans balls as possible I don't care...","pout","suspicious","angry","R")
        call her_main("YAY!","grin","worriedCl")
        m "I'm still here you know!"
        call her_main("of course Professor...","grin","baseL")
        call lun_main("...","normal","suspicious","base","R")
        call her_main("well come on then luna, we've still got a bit of time before classes, let's head to the library!","smile","baseL")
        call lun_main("you want to start now?","normal","wide","angry","mid")
        call her_main("no offense, but with your grades the way they are...","grin","worriedCl",emote="05")
        call her_main("well we don't have much time to spare...","base","worriedCl")
        m "This isn't going to impact our \"lessons\" is it [hermione_name]?"
        call her_main("of course not [genie_name]...","grin","baseL")
        call lun_main("it better not...","normal","angry","angry","mid")
        m "alright then, in that case, here's your payment."
        $ gryffindor += hermione_payout
        m "[hermione_payout] points to \'gryffindor\'!"
        call her_main("thank you [genie_name].","base","closed")
        $ luna_gold += luna_payout
        $ gold -= luna_payout
        m "And [luna_payout] gold for Luna."
        ">You hand Luna the pile of coins."
        $ luna_flip = 1
        call lun_main("Thank you, [lun_genie_name]...","normal","closed","mad","R")

        hide screen luna_main
        hide screen hermione_main
        show screen blkfade
        with d3

        ">Luna and hermione quickly get dressed before quickly leaving the room together."

        call load_luna_clothing_saves
        call load_hermione_clothing_saves

        call update_lun_uniform
        call update_her_uniform

        show screen luna_main
        show screen hermione_main
        hide screen blkfade
        with d3

        call her_main("this is going to be so much FUN!","grin","ahegao")

        call her_walk(action="leave", speed=2.5)

        call lun_main("(What have I agreed to)","normal","suspicious","sad","down")
        hide screen luna_main
        call lun_chibi("leave")

        $ luna_busy = True
        $ hermione_busy = True

        jump end_hermione_event


    else: #third handjob event, needs to be repeatable
        if lun_whoring <= 13:
            $ lun_whoring += 1
        label luna_handjob_hermione_call:
            pass
        m "How about another handjob, [lun_name]?"
        call lun_main("sure... do you want hermione here as well?","normal","suspicious","angry","R")
        m "You read my mind!"
        call lun_main("alright. but I expect to be the one doing the... job.","normal","angry","base","R")
        m "if you insist."
        call lun_main("...","normal","seductive","base","mid")
        call lun_main("just hurry up and bring her up here...","normal","seductive","base","R")
        call nar(">You summon hermione to your office.")
        call play_sound("door") #Sound of a door opening.

        call her_chibi("stand","mid","base")

        call load_hermione_clothing_saves
        call update_her_uniform

        $ luna_flip = -1
        call lun_main("",xpos="mid",ypos="base")

        call her_main("hello, [genie_name]!","base","happyCl",xpos="base",ypos="base")
        call her_main("hello, luna!","smile","happyCl")
        m "You seem cheerful."
        call her_main("why wouldn't I be? are we going to work on handjobs today?","open","baseL")
        call lun_main("just hurry up and get on your knees slut...","upset","seductive","angry","mid")
        call her_main("someone's eager!","smile","happyCl",emote="06")
        call lun_main("...","base","suspicious","angry","mid")
        hide screen hermione_main
        hide screen luna_main
        hide screen bld1
        show screen blkfade
        with d3

        ">You stand up from your desk while hermione slowly strips and kneels in front of you."

        call set_her_action("strip")

        $ luna_r_arm = 2
        $ luna_flip = 1
        $ luna_xpos = 640
        $ hermione_xpos = 590
        $ hermione_ypos = 390
        $ genie_xpos = 550
        $ genie_ypos = 0
        $ genie_base = "characters/genie/base/hard.png"

        call her_chibi("sit_naked","mid","base")

        show screen chair_left
        show screen desk
        call gen_chibi("jerking_off","desk","base")

        hide screen blkfade
        with fade
        call ctc

        show screen hermione_kneel
        show screen luna_main
        show screen genie_main
        show screen bld1
        with d3

        call her_kneel("Aren't you going to get naked as well Luna?","annoyed","angryL")
        call lun_main("I don't see why I should have to...","normal","angry","mad","R")
        call her_kneel("I told you before, he like's it better if you're naked while you stroke it.","annoyed","angryL")
        call lun_main("...","normal","angry","angry","mid")
        call lun_main("fine...","normal","suspicious","sad","R")
        call her_kneel("good.","base","base")
        call lun_main("but I expect extra for this [lun_genie_name]!","normal","seductive","angry","R")
        m "that seems fair."
        call lun_main("...","normal","suspicious","angry","mid")
        hide screen luna_main
        show screen blkfade
        with d3

        ">Luna slowly strips as well, carefully putting her clothes in a pile next to hermione's."
        $ luna_wear_bottom = False
        $ luna_wear_top = False
        $ luna_wear_panties = False
        $ luna_wear_bra = False
        show screen luna_main
        hide screen blkfade
        with d3

        call lun_main("happy now?","normal","angry","angry","mid")
        m "Very."
        call lun_main("good... let's just get this over with.","normal","angry","mad","R")
        call her_kneel("...","annoyed","frown")
        call lun_main("what is it now hermione?","normal","suspicious","angry","mid")
        call her_kneel("Just try and act like you like it a little more, ok?","open","suspicious")
        call lun_main("whatever...","normal","suspicious","angry","R")
        call her_kneel("great!","base","down")
        $ luna_r_arm = 3
        ">Luna spits into her hand before wrapping it around your cock."
        ">She's barely started to stroke it yet you can already tell her technique has improves significantly."
        m "Mmmm, yes that's it slut."
        m "just like that."
        call lun_main("...","base","seductive","angry","mid")
        call her_kneel("that's good luna... now try focusing on the tip a little more, like we talked about.","base","glance")
        call lun_main("like this?","normal","seductive","sad","mid")
        ">Luna wraps her hand around the head of your cock, rotating her hand slightly as she pumps her hand."
        m "Ugh... yes..."
        call her_kneel("good work. now go back to the rest of the shaft.","open","closed")
        call her_kneel("try no to focus on one area too long...","open","closed")
        call lun_main("ok...","base","angry","sad","mid")
        ">This continues for a while longer, Luna listening intently to hermione's instructions."
        g9 "Ugh... I'm getting close!"
        call her_kneel("alright, when this happens you need to slow down a little...","base","down")
        call lun_main("really? but isn't he about to cum?","upset","wide","sad","mid")
        g9 "Don't slow down now!"
        call her_kneel("shhh [genie_name], I'm trying to give a lesson here!","upset","closed")
        g9 "..."
        ">Luna slows her hand back down, bringing you almost painfully back from the edge of orgasm."
        call her_kneel("he {b}was{/b} about to cum, but if you build him up and then bring him back down he'll eventually cum much harder.","grin","dead")
        call her_kneel("I read about this technique in witches weekly... it's called edging!","base","down")
        call lun_main("hmmm, and you're sure it feels better?","normal","seductive","raised","mid")
        call lun_main("he almost seems like he's in pain...","base","seductive","angry","mid")
        ">luna gives your cock a hard squeeze as she looks sadistically at your cock."
        $ genie_face = "characters/genie/face/angry.png"
        g4 "ah!"
        $ genie_face = "characters/genie/face/grin.png"
        call her_kneel("believe me, he'll like this much more...","open","closed")
        call her_kneel("just wait to you see how much he'll shoot once you finally {i}let{/i} him cum.","grin","ahegao")
        call lun_main("mmmmm... I like the sound of that.","base","mad","mad","mid")
        call lun_main("so how much longer should I do this...","base","seductive","base","mid")
        $ genie_face = "characters/genie/face/angry.png"
        g4 "I can't take much more of this!"
        call her_kneel("probably not too much longer...","angry","wink")
        call her_kneel("it can get a little... frustrating if you do it for too long.","base","down")
        call lun_main("really? I don't mind that...","base","mad","mad","mid")
        g4 "I do!"
        call lun_main("alright then... how should I finish him off?","base","seductive","angry","down")
        call her_kneel("hmmm...","base","suspicious")
        show screen blkfade
        with d3

        $ genie_face = "characters/genie/face/base.png"
        ">Hermione slowly stands up and whispers something into Luna's ear before kneeling back down."
        hide screen blkfade
        with d3

        call lun_main("are you sure he'll like that?","base","wide","sad","mid")
        call her_kneel("trust me, he'll love it...","grin","baseL")
        m "like what?"
        call lun_main("quiet [lun_genie_name]!","normal","mad","angry","mid")
        ">luna gives your cock another painful squeeze before resuming stroking the length of it."
        $ genie_face = "characters/genie/face/angry.png"
        g4 "Ah!"
        $ genie_face = "characters/genie/face/open.png"
        m "can you stop that?"
        call lun_main("I'll stop it once you learn to be quiet.","pout","suspicious","angry","mid")
        $ genie_face = "characters/genie/face/base.png"
        m "..."
        call her_kneel("mmmm... that's it Luna...","soft","ahegao")
        call her_kneel("he's almost there... do it now.","grin","dead")
        call her_kneel("ah...","open_wide_tongue","squintL")
        ">Hermione opens her mouth as wide as she can while luna pulls you forward by your cock into her eager hole."
        $ luna_xpos += 45
        $ genie_xpos += 55
        $ hermione_kneel_cock = True
        $ genie_face = "characters/genie/face/angry.png"
        g4 "!!!"
        call her_kneel("mmm...","open_wide_tongue","ahegao")
        call lun_main("there we go...","base","seductive","sad","mid")
        $ hermione_xpos -= 10
        $ hermione_ypos -= 5
        ">Hermione starts eagerly lapping at the head of your cock while luna starts furiously stroking your shaft."
        g4 "{size=+5}FUCK YES!!!{/size}"
        g4 "{size=+5}here it comes sluts!{/size}"

        ">Luna continues stroking your cock at a blistering pace while hermione moves backwards slightly, leaving her mouth open and waiting."
        $ luna_xpos -= 55
        $ genie_xpos -= 55
        $ hermione_xpos += 10
        $ hermione_ypos += 5
        $ hermione_kneel_cock = False

        g4 "{size=+10}ARGHHH!!!!{/size}"
        show screen white
        pause.1
        $ uni_sperm = True
        $ u_sperm = "characters/hermione/face/auto_16.png"
        hide screen white
        pause.2
        show screen white
        pause .1
        hide screen white
        with hpunch

        g4 "{size=+5}ugh! YES!!!{/size}"
        call lun_main("so much...","base","wide","sad","mid")
        call her_kneel("...","full_cum","dead")
        call her_kneel("*gulp*","cum","worriedCl")
        call her_kneel("mmm... I told you it would make him cum more...","grin","dead")
        call lun_main("even so...","base","seductive","sad","mid")
        ">Luna stares at hermione with a fierce hunger in her eyes."
        call lun_main("stand up... please...","normal","seductive","sad","mid")
        ">Exhausted after the marathon handjob you decide to take a seat while hermione and luna clean up."
        call her_kneel("only because you asked nicely...","open","baseL")
        hide screen genie_main
        hide screen hermione_kneel
        hide screen luna_main
        show screen blkfade
        with d3

        ">Hermione slowly stands up, her face simply drenched in cum..."

        $ luna_flip = -1
        $ hermione_right_arm = "characters/hermione/body/arms/right/right_1.png"
        $ genie_base = "characters/genie/base/base.png"
        $ hermione_zorder = 5
        $ luna_r_arm = 1

        call gen_chibi("sit_behind_desk")
        call her_chibi("stand","mid","base")
        call update_her_uniform

        show screen luna_main
        show screen hermione_main
        show screen bld1
        hide screen blkfade
        with d3

        call lun_main("mmmmm... just look at you... you look so... delicous...","base","base","sad","empty", cheeks="blush")
        call her_main("...","open","baseL")
        $ luna_xpos = 500
        $ luna_r_arm = 2
        ">Luna moves closer to Hermione before picking up a strand of cum with her finger and moving it to her mouth."
        call her_main("go on...","soft","ahegao")
        m "(mmmm...)"
        $ luna_xpos = 530
        call lun_main("mmmmm... you taste even better...","base","happyCl","sad","mid")
        call her_main("...","grin","dead")
        ">Hermione stands still, letting luna slowly wipe the cum from her face..."
        $ u_sperm = "characters/hermione/face/auto_08.png"
        call her_main("that's it... make sure you get it all...","base","down")
        call lun_main("mmmmm...","full","happyCl","sad","mid")
        ">Luna slowly fills her mouth with cum before eventually swallowing."
        call lun_main("*gulp*","base","seductive","sad","empty")
        ">Eventually she finally gets the last strand into her mouth."
        $ uni_sperm = False
        call her_main("better?","base","glance")
        call lun_main("...","full","happyCl","sad","mid")
        call lun_main("*gulp*","base","seductive","sad","empty")
        call lun_main("much.","base","seductive","sad","empty")
        call her_main("good.","base","suspicious")

        menu:
            "-Ask about study sessions-":
                m "So how have your recent study sessions been going?"
                $ luna_l_arm = 2
                $ luna_flip = 1
                $ luna_xpos = 300
                call lun_main("they've been OK...","normal","suspicious","sad","R")
                call her_main("stop being such a negative nancy luna, they have been amazing [genie_name]!","smile","happyCl",emote="06")
                call lun_main("...","normal","suspicious","sad","down")
                call her_main("Luna quizzed me on advanced transmogrification spells, advanced potion recipes and even complex herbology!","smile","happyCl")
                call lun_main("I don't even thinks she needs quizzing, she got everything right...","upset","angry","angry","R")
                call her_main("well the tutoring was even better!","base","happyCl")
                call her_main("we studied transfiguration, D.A.D.A, handjobs, potions, titjobs, spells, dirty talk and herbology!","grin","baseL")
                m "sounds like quite the lesson..."
                call lun_main("......","normal","seductive","sad","R")
                call her_main("If we keep these sessions up I'm sure Luna will pass her o.w.l.s with flying colours!","base","squint")
                call lun_main(".........","base","seductive","sad","down")

                if not luna_herm_talk:
                    $ luna_herm_talk = True
                    call her_main("I can't wait to see what mark she gets when she has to do them!","smile","happyCl",emote="06")
                    $ luna_flip = -1
                    call lun_main("I think you mean when {b}we{/b} have to do them...","normal","suspicious","angry","mid")
                    call her_main("Oh, I don't have to do my o.w.l.s anymore...","base","happyCl")
                    call lun_main("What? Why not?","normal","wide","sad","mid")
                    call her_main("Do you want to tell her or should I?","base","down")
                    m "(I have no idea what she's talking about.)"
                    m "Why don't you fill her in."
                    call her_main("alright then...","base","glance")
                    call her_main("I already did my o.w.l.s last year.","grin","worriedCl",emote="05")
                    call lun_main("Really? How?","normal","angry","sad","mid")
                    call her_main("Well, I'd already been testing myself on past years exams since I was a 3rd year.","grin","worriedCl")
                    call her_main("Last year I finally felt that I was ready for the real thing. So I spoke to Professor dumbledore and Professor McGonagal.","base","baseL")
                    call her_main("I explained my situation and they agreed to test me early.","base","baseL")
                    call her_main("I got the highest mark since dumbledore himself took them!","smile","happyCl",emote="06")
                    call lun_main("Wait... If you've already completed your o.w.l.s, why are you still at school?","upset","suspicious","angry","mid")
                    call her_main("I didn't want to miss out on school work or spending time with my friends...","base","happyCl")
                    call her_main("So I've just been doing additional study in the library after classes in exhchange for a special reccomendation from the school.","smile","happyCl")
                    call her_main("although recently I've been spending most of my free time in here...","base","down")
                    call lun_main("but why did you want to study with me then? Surely you don't need the quizzing anymore?","normal","mad","raised","mid")
                    call her_main("I've always wanted to practice teaching and I get to help out my friend while I do it!","grin","baseL")
                    call lun_main("Friend?","normal","suspicious","sad","mid")
                    call her_main("of course we're friends luna! Maybe even best friends after all this...","base","squint")
                    call lun_main("...","normal","seductive","sad","mid")
                    call lun_main("whatever...","normal","angry","angry","R",tears="soft")
                    $ luna_flip = 1
                    hide screen luna_main

                    call lun_main("if you two are done talking I'm going to class...","normal","mad","angry","mid",tears="soft")

                    call lun_walk("mid","leave",2.5)

                    call load_luna_clothing_saves

                    call her_main("...","annoyed","worriedL")
                    call her_main("did she seem ok to you sir?","annoyed","worriedL")
                    m "I think so. She's probably just not used to you being nice to her."
                    call her_main("maybe... If it's alright with you I might go check up on her.","angry","worried")
                    m "Suit yourself. I'm getting pretty sleepy anyway."
                    call her_main("thank you, [genie_name].","base","worriedCl")
                    hide screen hermione_main
                    with d3

                    call load_hermione_clothing_saves
                    call update_her_uniform

                    call her_walk(action="leave", speed=2.5)

                else:
                    jump luna_her_hj_end

            "-let them go-":
                label luna_her_hj_end:
                    m "Alright, you two can go now."
                    $ luna_l_arm = 2
                    $ luna_flip = 1
                    $ luna_xpos = 300
                    call lun_main("*hmph*, not before you pay us!","normal","angry","angry","mid")
                    m "Right, nearly forgot."
                    call her_main("...","annoyed","suspicious")
                    $ gryffindor += 50
                    m "50 points to \'gryffindor\'!"
                    call her_main("thank you [genie_name]...","base","closed")
                    call lun_main("...","normal","seductive","base","R")
                    $ luna_gold += 150
                    $ gold -= 150
                    m "150 gold for Luna."
                    call lun_main("thanks [lun_genie_name]...","normal","seductive","base","R")
                    call her_main("...","annoyed","angryL")
                    m "if that's all, I think I need a nap."
                    call her_main("alright then...","base","base")
                    ">Hermione and Luna get dressed before leaving your office together."
                    hide screen luna_main
                    hide screen hermione_main

                    call load_luna_clothing_saves
                    call load_hermione_clothing_saves

                    call update_lun_uniform
                    call update_her_uniform

                    with d3
                    pause.8


                    ">You can hear them talking and laughing together as they shut your door."

    call play_sound("door") #Sound of a door opening.
    hide screen luna_main
    call lun_chibi("hide")
    call her_chibi("hide")

    $ luna_busy = True
    $ hermione_busy = True

    jump end_hermione_event
