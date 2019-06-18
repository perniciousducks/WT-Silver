

### Flash A Classmate ###

label hg_pr_flash:

    if hg_pr_flash.counter < 1:
        m "{size=-4}(Tell her to flash her tits to one of her classmates?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump hermione_favor_menu

    call her_main(face="happy", xpos="right", ypos="base", trans="fade")

    #Intro.
    if hg_pr_flash.counter == 0:
        m "[hermione_name]..."
        m "I would like to award \"Gryffindor\" with 25 house points today."
        call her_main("Really?","base","base")
        her "Thank you, [genie_name]!"
        m "Yes, but first I will require your help with something..."
        her "Of course, [genie_name]! Anything!"
        m "I need you to go out there and show off your tits to people..."
        stop music fadeout 1.0
        call her_main("...?","open","base")
        m "You know, flash your breasts to some boys..."
        call her_main("?!!","shock","wide")

        if her_tier < 3 or her_reputation < 6:
            jump too_much

        her "[genie_name]!"
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        call her_main("This is a completely new level of inappropriate, even for you, [genie_name]!","angry","angry")
        her "How can you ask one of your pupils to perform such a task?"
        m "So that's how you feel then? I see..."
        m "I suppose I will be awarding those points to some other house instead ..."
        m "\"Slytherin\" perhaps?"
        call her_main("................","disgust","glance")
        m "But, you know, no pressure..."
        call her_main("[genie_name]...","annoyed","angryL")
        her "The fate of my house is very important to me, but..."
        m "Is it really?"
        m "Why don't you show it to me then?"
        m "Yes. Show me how important it is to you exactly, [hermione_name]."
        call her_main("But this is inappropriate...","angry","angry")
        m "Are we really in any position to discuss what is appropriate and what is not at this point?"
        call her_main("..................","annoyed","angryL")
        m "I would say that ship has sailed a long time ago..."
        call her_main("..............","disgust","glance")
        m "All I ask you to do is to give some lucky boy a quick peek..."
        call her_main("But why? Why must I do things like this, [genie_name]?","annoyed","angryL")
        m "A minute of your time for 25 house points..."
        m "A pretty nifty deal, wouldn't you agree?"
        her "I suppose..."
        her "Well alright, I'll see what I can do..."

    elif her_tier < 4:
        m "I think you need to show off your tits some more, [hermione_name]."
        call her_main("You mean to you, [genie_name]?","upset","wink")
        m "No, to your classmates..."
        call her_main("Oh...","angry","base")
        m "Yes, go do that and then report back to me..."
        call her_main("Will I get paid for this?","annoyed","angryL")
        m "Of course you will get paid for this, [hermione_name]. Don't be silly."
        m "Thirty five house points. The usual rate..."
        call her_main(".................","annoyed","angryL")
        call her_main("Well alright... I will see what I can do, [genie_name]...","disgust","glance")

    elif her_tier < 5:
        m "[hermione_name]. I have a question for you."
        call play_music("chipper_doodle") # HERMIONE'S THEME.
        m "Why do you think women have breasts?"
        call her_main("...what do you mean, [genie_name]?","upset","wink")
        m "Alright, let me rephrase this..."
        m "What would you say is the most common application for the female mammary glands?"
        call her_main("Oh...","soft","base")
        call her_main("Production of milk?","annoyed","suspicious")
        m "Good. What else do women use their tits for?"
        call her_main("Hm..","soft","baseL")
        call her_main("...to attract men?","annoyed","suspicious")
        m "Yes. Let's concentrate on that."
        m "I need you to go out there..."
        m "Find some lucky bastard..."
        m "And flash him your tits..."
        call her_main("{size=-3}(I just knew that this was exactly where this conversation was heading...){/size}","disgust","glance")
        m "What was that, [hermione_name]?"
        call her_main("I said I'd better go then, [genie_name].","annoyed","angryL")
        her "my classes are about to start..."
        m "Thirty five house points will be waiting for you here upon your return, [hermione_name]."
        call her_main("..............","annoyed","annoyed")

    else:
        m "[hermione_name] I need you to go out there and flash your tits to one of your classmates."
        call her_main("I will do my best [genie_name].","open","closed")
        m "Really? Just like that? No complaints or anything?"
        call her_main("I am getting paid for this, am I not?","base","glance")
        m "Of course."
        call her_main("Why would I complain about a simple task like this then?","open","closed")
        her "Thirty five house points is a fair prices for a few seconds of excitement... err..."
        call her_main("...I mean, embarrassment.","base","happyCl")
        m "{size=-3}(She changed this much already?){/size}"
        g9 "{size=-3}(I'm so good at this training thing that it's starting to get creepy!){/size}"
        call her_main("Classes are about to start... I'd better leave now.","base","base")
        her "I will see you later tonight, [genie_name]."

    call her_walk(action="leave", speed=2.5)

    $ current_payout = 35
    $ hg_pr_flash.inProgress = True

    jump end_hermione_event


label end_hg_pr_flash:
    $ gryffindor += current_payout
    m "The \"Gryffindor\" house gets [current_payout] points!"
    her "Thank you, [genie_name]."

    call her_walk(xpos="door", ypos="base", speed=2)
    pause.2

    show screen blktone
    if her_tier == 3:

        if one_out_of_three == 3:
            call her_main("(I can't believe I did that today...)","upset","closed", ypos="head")
            call her_main("(What if Harry or Ron saw me like that?)","angry","wide")
            call her_main("(Standing there...)")
            call her_main("(Pressing my breasts against that window glass...)")
            call her_main("(I would probably just die of embarrassment right there on the spot...)","angry","down_raised")
            call her_main("(No. Protecting the honor of the \"Gryffindor\" house is my number one priority.)","upset","closed")
            call her_main("(We must get the cup this year, no matter the cost...)")
            call her_main("(........)","angry","down_raised")
        else:
            call her_main("\"Slytherin\"...","upset","closed", ypos="head")

    else:
        call her_main(".........................","grin","dead", ypos="head")

    hide screen blktone
    call her_chibi(action="leave")

    $ hg_pr_flash.inProgress = False

    # Increase Points
    if her_tier == 3:
        if her_whoring < 12: # Points til 12
            $ her_whoring += 1

    if her_reputation < 12: # Points til 12
        $ her_reputation += 1

    jump end_hermione_event



### Tier 1 ###

label hg_pr_flash_T1_E1:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    #if her_whoring >= 9 and her_whoring < 12:

    call her_main("Good evening, [genie_name]...","open","base", xpos="right", ypos="base")
    m "[hermione_name]..."
    m "So, how did it go?"
    call her_main("Ehm... Not too well, actually...","angry","worriedCl",emote="05")
    her "................................"
    m "Just tell me what happened, [hermione_name]."
    call her_main("That is the thing, [genie_name]...","open","base")
    her "Nothing happened..."
    call her_main("I just couldn't bring myself to do it...","open","down")
    m "I see..."
    m "Well, I can't just give you the points for nothing, [hermione_name]."
    call her_main("Of course, [genie_name]... I understand...","open","closed")
    call her_main("I shall try harder next time... I promise...","annoyed","worriedL")
    m "Then I will just put these thirty five points aside for now..."
    call her_main("Thank you, [genie_name]...","annoyed","worriedL")
    her "..."
    her "I'd better go now."

    call her_walk(action="leave", speed=2.5)

    $ hg_pr_flash.inProgress = False

    jump end_hermione_event


label hg_pr_flash_T1_E2:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name], did you complete your task?"
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("Ehm... Sort of...","annoyed","worriedL")
    m "Sort of?"
    call her_main("Yes... uhm...","open","base")
    her "Well, I decided to try and flash them to this \"hufflepuff\" boy..."
    call her_main("I've been waiting for the right moment...","open","down")
    her "I was worried that something would go wrong..."
    call her_main("And, of course, everything that could - did...","annoyed","angryL")
    call her_main("When I tried to expose myself to the boy...","open","base")
    her "At first I only pulled up my vest..."
    her "Then I tried to pull my shirt up as well..."
    her "And one of my breasts got entangled in the fabric and was pulled up along with the shirt..."
    call her_main("So only one of my breasts was naked and I was desperately trying to free the other one.","scream","worriedCl")
    her "Other students started to pay attention to me..."
    her "So I had to fix my clothes back into place quickly..."
    her "And then the moment was gone..."
    call her_main("............","normal","worriedCl")
    m "Hm..."
    m "What about the boy? Did he see your tits or not?"
    call her_main("Well, I think he may have seen one of them...","open","base")
    her "But from the way he was looking at me..."
    her "I doubt that he understood that the whole commotion was for his benefit."
    call her_main("......................","annoyed","worriedL")
    call her_main("I'm sorry, [genie_name]...","open","base")
    m "That's alright..."
    m "I wouldn't expect you to perform perfectly this early in your training..."
    call her_main("(My training?)","angry","base")

    jump end_hg_pr_flash


label hg_pr_flash_T1_E3:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="neutral", xpos="right", ypos="base")
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    m "[hermione_name], did you complete your task?"
    show screen blkfade
    with d3

    $ sc34CG(3, 5)

    show screen blktone
    hide screen blkfade
    call her_main("Yes I did, [genie_name].","annoyed","worriedL", xpos="base", ypos="base", trans="fade")
    m "Good. Tell me more."
    $ sc34CG(3, 4)
    call her_main("Ehm... There is not much to tell, really...","open","base")
    call her_main("I spent the first half of the day with studying in the library...")
    call her_main("It is usually quite deserted during that time...")
    call her_main("Apart from me there was only one student...")
    $ sc34CG(3, 6)
    call her_main("Some boy from \"Ravenclaw\"...","upset","closed")
    call her_main("So I waved to him and when he looked up at me...")
    $ sc34CG(3, 7)
    call her_main("I quickly pulled my shirt up...","angry","base")
    m "Good job."
    m "How did he react to the sight of your naked tits?"
    $ sc34CG(3, 8)
    call her_main("I'm not sure...","angry","down_raised")
    $ sc34CG(3, 9)
    call her_main("He looked rather shocked I suppose...","angry","base")
    $ sc34CG(3, 10)
    call her_main("After I showed him my breasts it got too embarrassing for me to stay there any longer...","angry","down_raised")
    $ sc34CG(3, 11)
    call her_main("So I just gathered all my books and left...","angry","base")
    $ sc34CG(3, 6)
    m "I see..."
    show screen blkfade
    hide screen sccg

    jump end_hg_pr_flash


label hg_pr_flash_T2_E1:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    #elif her_whoring >= 12 and her_whoring < 15:

    stop music fadeout 1.0
    show screen blktone
    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name]. Did you complete your task?"
    call her_main("Yes I did, [genie_name].","upset","wink")
    call her_main(".............","angry","down_raised")
    m "Well? How did it go?"
    call her_main("................","angry","down_raised")
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("Just for the record, [genie_name]...","annoyed","angryL")
    m "Hm?"
    call her_main("I think that forcing your pupils to do things like this...","scream","angryCl")
    call her_main("Is beneath an esteemed wizard such as yourself...","upset","closed")
    m "\"Forcing\"? Nobody is forcing you to do anything, [hermione_name]."
    m "You came to me, remember?"
    call her_main("..........","open","base")
    m "You begged me to buy a sexual favour from you."
    call her_main("...I....","annoyed","worriedL")
    call her_main("I never said \"sexual\"...","open","base")
    m "Nevertheless, you can stop selling me these favours at any moment, [hermione_name]."
    call her_main("I suppose...","annoyed","angryL")
    m "And yet you keep on coming back..."
    call her_main("............................","angry","down_raised")
    m "I think you may actually be taking some twisted form of pleasure from this."
    call her_main("What?","angry","angry")
    m "Shame on you, [hermione_name]. Shame on you."
    call her_main("[genie_name], I never...!","angry","angry")
    m "Enough of this. Did you complete your task or not?"
    call her_main("Yes I did...","upset","closed")
    m "And?"
    call her_main("And that is all I am going to say...","open","down")
    call her_main("........","upset","closed")
    m ".........."
    her "........"
    m "Oh, whatever. Just take your points and go."
    call her_main("Thank you, [genie_name].","upset","closed")

    jump end_hg_pr_flash


label hg_pr_flash_T2_E2:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name]..."
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    show screen blktone
    call her_main("Good evening, [genie_name]...","normal","worriedCl")
    m "Did you complete your task?"
    call her_main("Yes, I did, [genie_name]...","open","base")
    call her_main("..........","normal","worriedCl")
    m "................"
    her "..............."
    m "Well?"
    call her_main("Can I get paid now please?","open","base")
    m "Not before you tell me what exactly you did today."
    call her_main("....................","normal","worriedCl")
    call her_main("Do I really have to, [genie_name]?","open","base")
    m "When you are being coy like this..."
    m "It only makes me more curious. You know that, right?"
    call her_main("Aww...","angry","base")
    call her_main("Well... Ehm...","angry","down_raised")
    her "Well, alright, here it goes..."
    call her_main("I flashed my tits to that \"Slytherin\" underclassman in a corridor...","scream","worriedCl")
    her "But I was standing too close to him..."
    call her_main("....","normal","worriedCl")
    her "...."
    call her_main("Well, he sort of grabbed one of my breasts, [genie_name]...","open","base")
    her "he squeezed it hard and just wouldn't let go..."
    call her_main("He made me promise to meet him after my classes...","angry","base")
    her "And let him..."
    call her_main("\"Play with my tits\" some more...","open","worriedCl")
    call her_main("You see, that is why I hate \"slytherin\" boys, [genie_name]...","angry","down_raised")
    her "They don't have a shred of honour.."
    her "..."
    m "Did you keep your promise?"
    call her_main("No, not yet...","angry","base")
    her "I'm planning to meet that awful boy after we are done here, [genie_name]."
    m "I see..."
    m "Well, I shouldn't keep you waiting then, should I?"

    jump end_hg_pr_flash


label hg_pr_flash_T2_E3:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name], did you complete your task?"
    show screen blktone
    call her_main("I did [genie_name]...","open","base")
    m "I'm listening..."
    call her_main("Well...","open","base")
    her "I had to spend a big portion of the day at the school library..."
    her "So I didn't really have the time to perform your task properly, [genie_name]..."
    m "Hm...?"
    call play_music("playful_tension") # SEX THEME.
    her "Instead I just went to the library window and..."
    call her_main("...I just pulled my shirt up and pressed my bare breasts against the glass...","angry","down_raised")
    her "I stood there like that for several seconds..."
    her "To make sure that at least someone sees me from the outside..."
    call her_main("I hope this still counts, [genie_name]...","angry","base")
    m "Hm..."
    m "How many students would you say saw you standing behind that window?"
    call her_main("I am not sure, [genie_name]... A couple maybe...?","angry","down_raised")
    m "\"Maybe\"?"
    call her_main("I don't know, [genie_name]...","open","worriedCl",cheeks="blush")
    her "To be honest I kept my eyes closed..."
    m "How do you know that anyone saw you at all then, [hermione_name]?"
    call her_main("I heard someone shout: \"Look! At that window over there!\".","angry","suspicious",cheeks="blush")
    her "When I heard that I covered up and quickly left..."
    call her_main("....","angry","base")
    m "Hm..."
    m "Well, alright... I think this counts..."

    jump end_hg_pr_flash


label hg_pr_flash_T3_E1:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    #elif her_whoring >= 15:

    call her_main(face="neutral", xpos="right", ypos="base")
    m "[hermione_name], did you complete your task?"
    show screen blktone
    call her_main("I did [genie_name]...","base","base")
    m "I'm listening..."
    show screen blkfade
    with d3

    $ sc34CG(3, 5)

    hide screen blkfade
    call her_main("Well... I had to spend a big portion of the day in the school library...","upset","wink", xpos="base", ypos="base", trans="fade")
    call her_main("So I didn't really have the time to perform your task properly, [genie_name]...")
    m "Hm...?"
    $ sc34CG(3, 6)
    call her_main("Instead I just made sure there were no teachers around...","angry","base")
    call play_music("playful_tension") # SEX THEME.
    $ sc34CG(3, 7)
    call her_main("Pulled my shirt up...")
    call her_main("And then I just sat there like that for a while...","open","base")
    $ sc34CG(3, 12)
    call her_main("trying to get some studying done...","open","down")
    her "I don't think there were many people around..."
    call her_main("Or at least I hope so...","angry","down_raised")
    $ sc34CG(3, 13)
    call her_main("But they definitely saw my breasts, [genie_name]...","angry","base")
    $ sc34CG(3, 7)
    call her_main("eventually A few first years seemed to notice...","angry","down_raised")
    $ sc34CG(3, 10)
    call her_main("I had to leave pretty quickly after that...","angry","base")
    m "Hm..."
    m "How many people would you say saw your tits today, [hermione_name]?"
    $ sc34CG(3, 9)
    call her_main("Hard to say, [genie_name]...","open","base")
    call her_main("Two dozen boys or so I suppose...")
    $ sc34CG(3, 12)
    call her_main("A few girls as well...","annoyed","worriedL")
    $ sc34CG(3, 11)
    call her_main("I think the school librarian may have seen me too...")
    m "Hm... Well, I'd say that's a job well done."

    show screen blkfade
    hide screen sccg

    jump end_hg_pr_flash


label hg_pr_flash_T3_E2:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    stop music fadeout 1.0
    call her_main(face="happy", xpos="right", ypos="base")
    m "[hermione_name], did you complete your task?"
    show screen blktone
    call her_main("Yes I did, [genie_name].","base","base")
    m "Well, tell me all about it, then."
    call her_main("Ehm... Alright...","open","base")
    her "I was flashing my tits to this boy in the \"Gryffindor\" common room..."
    call her_main("When my friend, Ginny walked in on us...","open","base")
    m "Another boy?"
    call her_main("A boy? No, Ginny is a girl's name, [genie_name].","soft","baseL")
    m "....."
    call her_main("Ginny Weasley, [genie_name].","open","base")
    m "Alright, fine, continue..."
    call her_main("uhm...","soft","baseL")
    her "......."
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("*Giggle*","grin","worriedCl",emote="05")
    m "Hm...?"
    call her_main("Then Ginny grabbed my breasts...","smile","baseL")
    her "And started to squeeze them..."
    her "then she started to kiss my breasts passionately..."
    m "............"
    call her_main("to kiss and suck on my nipples...","smile","angry")
    call her_main("And I couldn't help myself - I started to moan...","base","glance")
    m ".............."
    call her_main("And then the boy took out his throbbing cock...","base","suspicious")
    her "And sprayed his hot spunk all over me and Ginny!"
    call her_main("And then me and Ginny, we licked his hot sperm off of our young bodies...","smile","angry")
    m ".............."
    m "Are you making this up, [hermione_name]?"
    call her_main("...maybe.","grin","worriedCl",emote="05")
    call her_main("I just thought that you would like to hear something like that, [genie_name]...","base","glance")
    m "What I would like to hear, [hermione_name], is the truth."
    call her_main("Even if it's incredibly dull, [genie_name]?","open","closed")
    m "Dull or not..."
    m "I only want to know what actually happened..."
    m "Keep your fantasies to yourself, [hermione_name]."
    call her_main("As you wish, [genie_name].","annoyed","ahegao")
    her "My friend Ginny walked in on my flashing my tits to that guy."
    her "But She promised me that she won't tell anyone."
    call her_main("And that's all that happened, [genie_name]...","soft","base")
    m "I see..."
    m "I still prefer this to some made up stories..."

    jump end_hg_pr_flash


label hg_pr_flash_T3_E3:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main(face="happy", xpos="right", ypos="base")
    m "[hermione_name], did you complete your task?"
    show screen blktone
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("Yes I did, [genie_name]...","base","base")
    m "Alright, tell me how did it go."
    call her_main("Well, let's see...","annoyed","worriedL")
    her "First I flashed them to that one boy from \"Ravenclaw\"..."
    call her_main("Then to that upperclassman from \"Hufflepuff\"...","open","base")
    call her_main("Then there was this other boy from \"Ravenclaw\".","base","base")
    m "???"
    call her_main("After that I flashed my tits to some \"Gryffindor\" underclassman by mistake...","angry","worriedCl",emote="05")
    call her_main("No, wait...  the boy from \"Gryffindor\" was after that other boy...","annoyed","worriedL")
    m "How many boys did you flash your tits to today, [hermione_name]?"
    call her_main("Half a dozen or so?","angry","base")
    call her_main("I had an opening in my schedule...","angry","wink")
    her "So I decided to go for some extra credit with your assignment, [genie_name]."
    m "This is not an assignment, [hermione_name]..."
    m "And there are no extra credits..."
    call her_main("Oh...?","open","base")
    m "You are still getting your usual payment, [hermione_name], and that's it."
    call her_main("Oh... I see...","annoyed","worriedL")
    m "But, [hermione_name]..."
    call her_main("Yes, [genie_name]?","open","base")
    g9 "That was very well done."
    call her_main("Thank you, [genie_name].","base","glance")

    jump end_hg_pr_flash
