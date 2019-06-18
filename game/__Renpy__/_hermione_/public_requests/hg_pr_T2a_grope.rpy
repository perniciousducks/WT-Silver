

### Let Classmate Molest Her ###

label hg_pr_grope:

    if hg_pr_grope.counter < 1:
        m "{size=-4}(Tell her to go get touched by one of her classmates?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass

            "\"(Not right now.)\"":
                jump hermione_favor_menu

    call her_main(face="happy", xpos="right", ypos="base", trans="fade")

    #Intro.
    if hg_pr_grope.counter == 0:
        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base")
        m "You do like boys your age, don't you?"
        call her_main("...?","normal","base")
        m "one of your classmates maybe?"
        call her_main("Well...","open","worriedL")
        her "Must I really discuss things like this with you, [genie_name]?"
        call her_main("It's a bit embarrassing...","annoyed","worriedL")
        m "Sure, I understand. I don't need to know the details..."
        m "But here is what I need you to do today, [hermione_name]."
        m "Go confront that boy you fancy. The one you think is \"just so dreamy\"..."
        call her_main(".......?","open","base")
        m "And let him touch you..."

        if her_tier < 2 or her_reputation < 3:
            jump too_much

        call her_main("Let him... touch me, [genie_name]?","open","base")
        m "Yes, touch you. The way boys touch girls?"
        m "How old are you, [hermione_name]? You look mature enough..."
        m "Haven't you had \"the talk\" with your parents already?"
        call her_main("\"The talk\", [genie_name]?","angry","worriedCl", emote="05")
        m "Yes, \"the talk\"! About how boys are different than the girls...?"
        m "Boys have a \"pee-pee\" and girls like to put that  \"pee-pee\" in their mouths?"
        call her_main("!!!","normal","base")
        call her_main("What kind of demented parent would have such a talk with their child?","angry","angry")
        m "{size=-3}I wish mine did.{/size}"
        call her_main("I beg your pardon, [genie_name]?","annoyed","suspicious")
        m "*Khem!* I said, a responsible and caring one!"
        m "Well, in any case. That is your task for today, [hermione_name]."
        m "Find a way to persuade one of your classmates to fondle you a little..."
        call her_main("..........","annoyed","angryL")
        m "You are a pretty girl, it shouldn't be too hard."
        her "....................."
        call her_main("How many points would I receive after completing such a task, [genie_name]?","disgust","glance")
        m "Hm... Twenty five should do..."
        call her_main("Twenty five house points...","annoyed","angryL")
        her "...."
        call her_main("Well, so be it then...","disgust","glance")
        m "Great..."
        call her_main("I'd better go now. The classes are about to start...","angry","angry")

    elif her_tier < 3:
        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base")
        m "How about you go let one of your classmates molest you a little again?"
        call her_main("........","upset","closed")
        m "Twenty five house points, [hermione_name]."
        call her_main("[genie_name], it's just...","annoyed","angryL")
        call her_main("I do not understand why I must do things like that...","annoyed","annoyed")
        m "To help out your house?"
        call her_main("That's not what I meant...","disgust","glance")
        call her_main("Oh, never mind...","annoyed","angryL")
        her "The classes are about to start, I'd better go..."
        m "Will you do it?"
        call her_main("I don't know... Maybe...","disgust","glance")

    elif her_tier < 4:
        m "[hermione_name], I need you to go out there, and make one of your classmates molest you a little."
        call her_main("I understand, [genie_name]...","base","base")
        m "Off you go then."
        her "..........."

    else:
        m "[hermione_name], I need you to go out there..."
        m "Find a handsome guy and force yourself on him!"
        call her_main("You mean like...","base","base")
        call her_main("In a sexual way, [genie_name]?","angry","wink")
        m "What? No, I mean just let him get under your uniform that's all..."
        call her_main("Oh, I see...","grin","worriedCl", emote="05")
        call her_main("I wonder who it should be this time...","grin","baseL")
        call her_main("More than one boy, is not a problem, is it, [genie_name]?","angry","base")
        m "A problem? Of course not!"
        m "If anything - it is encouraged."
        call her_main("Great. I will see you after the classes then, [genie_name]. As usual.","angry","wink")
        m "Yes. Good luck."

    call her_walk(action="leave", speed=2.5)

    $ current_payout = 25
    $ hg_pr_grope.inProgress = True

    jump end_hermione_event


label end_hg_pr_grope:
    $ gryffindor += current_payout
    m "The \"Gryffindor\" house gets [current_payout] points!"
    her "Thank you, [genie_name]."

    call her_walk(action="leave", speed=2.5)

    $ hg_pr_grope.inProgress = False

    # Increase Points
    if her_tier == 2:
        if her_whoring < 6: # Points til 6
            $ her_whoring += 1

    if her_reputation < 9: # Points til 9
        $ her_reputation += 1

    jump end_hermione_event



label hg_pr_grope_intro:

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call her_main("Good evening, [genie_name].","base","base",xpos="right",ypos="base")
    m "[hermione_name]..."
    m "Did you complete your task?"
    her "I did as you asked [genie_name]..."

    if hg_pr_grope.points > 4: # If you have seen all events in this tier once, you get the choice to skip it.
        menu:
            "\"Great. Here are your points.\"":
                jump end_hg_pr_grope

            "\"Give me the details.\"":
                pass

    show screen blktone
    with d3

    if her_whoring < 9:
        stop music fadeout 3.0
        call her_main("......","annoyed","angryL")
        call her_main("Well... Em...","soft","baseL")
        m "Speak up, [hermione_name]."
        m "Did you let some lucky guy feel you up or what?"

    return



### Tier 1 ###

label hg_pr_grope_T1_E1:

    call hg_pr_grope_intro

    m "So? Tell me more."
    her "Well, there is not much to tell..."
    call her_main("I told that one guy I know that he could touch me a little if he wants...","open","base")
    call her_main("He thought I was joking at first...","annoyed","worriedL")
    call her_main("So embarrassing...","normal","worriedCl")
    m "So, did he cop a feel or not?"
    call play_music("playful_tension") # SEX THEME.
    call her_main("He did...","normal","worriedCl")
    m "Well, where did he touch you, [hermione_name]?"
    call her_main("Ehm... My legs...","annoyed","worriedL")
    her "And my breasts a little I suppose..."
    m "That's all?"
    call her_main("Yes, [genie_name]...","open","base")
    call her_main("It's getting late... I think I'd better leave now...","normal","worriedCl")
    call her_main("I'm sorry, [genie_name]...","angry","worriedCl", emote="05")
    m "Nothing to be sorry about, [hermione_name]."
    m "You did good. This will do for now."

    jump end_hg_pr_grope


label hg_pr_grope_T1_E2:

    call hg_pr_grope_intro

    stop music fadeout 3.0
    call her_main("But it was all very awkward and embarrassing...","annoyed","angryL")
    m "That's the whole point of it, [hermione_name]."
    m "Tell me where you were touched today..."
    call play_music("playful_tension") # SEX THEME.
    her "Ehm..."
    call her_main("Well he touched me under my skirt a little...","angry","base")
    her "Then I let him rub my..."
    call her_main("...my pussy through the panties, [genie_name].","angry","down_raised")
    m "Very good. Then what happened?"
    call her_main("Then he sort of started to touch himself [genie_name]...","open","worriedCl")
    her "So, I decided to leave..."
    m "I see..."
    call her_main(".............","normal","worriedCl")

    jump end_hg_pr_grope


label hg_pr_grope_T1_E3:

    call hg_pr_grope_intro

    call play_music("playful_tension") # SEX THEME.
    call her_main("I led this one guy from \"Hufflepuff\" to an empty classroom and I told him that he can touch me if he wants.","open","base")
    her "That I don't mind..."
    call her_main("...........","annoyed","worriedL")
    m "And?"
    call her_main("Well, he did touch me a little at first...","open","base")
    call her_main("......","normal","worriedCl")
    m "Don't make me pull every word out of you, [hermione_name]!"
    m "Then what happened?"
    call her_main("Well...","open","down")
    stop music fadeout 1.0
    her "I think he was more interested in {size=+5}me{/size} molesting {size=+5}him{/size}..."
    call her_main("He asked me to call him a \"sissy boy\"...","upset","wink")
    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
    call her_main("And he kept on reassuring me that he has a very small penis...","open","base")
    call her_main("He just kept repeating that *sob!*...","angry","base", tears="soft")
    call her_main("Why would anyone be like this?","angry","base", tears="soft")
    her "*Sob!* I Could not stay in his company a moment longer, so I just ran."
    m "I'm sorry to hear this..."
    call her_main("It was truly awful, [genie_name]...","angry","base", tears="soft")
    m "There, there..."
    call her_main("*Sob!*","normal","baseL", tears="soft")
    m "Will ten extra points make you feel better?"
    call her_main("Huh? That would be very sweet of you [genie_name].","soft","base", tears="soft")
    m "Of course... Ten extra points to \"Gryffindor\"."
    call her_main("Thank you [genie_name]...","clench","worried", cheeks="blush", tears="soft")
    m "And the rest of your payment..."

    jump end_hg_pr_grope


label hg_pr_grope_T2_E1:

    call hg_pr_grope_intro

    #elif her_whoring >= 9 and her_whoring <= 11: # LEVEL 04

    call her_main("Well... There is not much to tell...","open","closed")
    her "I found this one boy from \"Ravenclaw\"..."
    her "Led him to one of the empty classrooms in the eastern wing..."
    her "He thought I wanted to make out with him..."
    her "But I told him that I just want him to touch me..."
    call her_main("...so he did.","normal","worriedCl")
    m "I see..."
    m "Well done, [hermione_name]."
    call her_main("Will I be getting my points now?","upset","wink")
    m "In a minute, [hermione_name]. I have a question I would like to ask you before that."
    call her_main("???","open","base")
    m "Did you enjoy it?"
    m "Did it feel good to be touched by that boy?"
    call her_main("Oh...","open","closed")
    her "Well, he was rather handsome I suppose..."
    call her_main("I didn't hate it, if that's what you mean, [genie_name]...","upset","closed")
    m "I see..."

    jump end_hg_pr_grope


label hg_pr_grope_T2_E2:

    call hg_pr_grope_intro

    call her_main("Well...","open","closed")
    her "I'm not sure whether or not this counts, but..."
    her "During the herbology class today..."
    call her_main("I let this one boy slide his hand under my skirt...","upset","wink")
    her "So while Professor Sprout explained the differences between \"mandrake\" and \"mandragore\"..."
    call her_main("Something I already knew of course...","open","suspicious")
    call her_main("I let my lab partner massage my buttocks...","upset","wink")
    her "And that is all..."
    m "Hm..."

    menu:
        "\"You can do better than that, [hermione_name].\"":
            call her_main("Yes, I know, [genie_name]. I am sorry.","open","base")
            m "Just make sure you try harder next time."
            her "I will, [genie_name]."

            jump end_hg_pr_grope

        "\"Kudos on doing this during class.\"":
            call her_main("Thank you, [genie_name].","base","happyCl")
            m "I say you deserve to get paid."

            jump end_hg_pr_grope


label hg_pr_grope_T2_E3:

    call hg_pr_grope_intro

    stop music fadeout 1.0
    call her_main(".................","annoyed","angryL")
    m "???"
    call play_music("playful_tension") # SEX THEME.
    call her_main("I don't want to talk about it, [genie_name]...","annoyed","angryL")
    m "What happened, [hermione_name]. Spit it out."
    call her_main(".................","annoyed","annoyed")
    call her_main("But... it's so embarrassing...","open","base")
    call her_main("Do I really have to, [genie_name]?","normal","worriedCl")
    m "Yes, I happen to love embarrassing things!"
    call her_main(".................","annoyed","angryL")
    her "Well, alright..."
    her "I approached this one guy that I always found attractive..."
    her "Managed to muster up enough courage to ask him to follow me..."
    call her_main("Normally I wouldn't dare...","open","base")
    her "But the fact that I was doing this as a task entrusted to me by someone else..."
    her "made it easier somehow..."
    m "Happy to help, [hermione_name]."
    call her_main("I led him to the library...","open","down")
    her "We found a secluded spot behind one of the book shelves..."
    her "And I told him that he can touch me wherever he wants..."
    her "And...."
    call her_main("..........","clench","down_raised")
    m "What?"
    call her_main(".....................","normal","worriedCl")
    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
    call her_main("He started to touch my... feet, [genie_name].","scream","worriedCl")
    m "Huh?"
    m "Your \"Feet\"? Is that what kids call tits these days?"
    call her_main("I'd wish, [genie_name]...","disgust","glance")
    her "He asked me to take off my shoes..."
    her "Then he..."
    call her_main("He started to smell my toes, [genie_name]!","angry","base", tears="soft")
    call her_main("I felt so... violated!","angry","base", tears="soft")
    m "So he didn't touch your tits, or your butt?"
    call her_main("No, [genie_name]... *sob!*","shock","down_raised", cheeks="blush", tears="crying")
    m "Alright, then what happened?"
    call her_main("Nothing! I couldn't bear the humiliation... I just ran...","angry","dead", cheeks="blush", tears="crying")
    her "I even left my shoes behind and had to come back later to pick them up..."
    call her_main("*Sob!*............","angry","suspicious", cheeks="blush", tears="messy")
    m "Hm..."
    m "Well, you did get molested..."
    m "Although in a rather unconventional manner..."
    call her_main("*Sob!* I wish he would have just touched my breasts like a descent boy would, [genie_name]... *Sob!*","angry","suspicious", cheeks="blush", tears="messy")
    m "There, there..."
    m "You earned you pay today..."

    jump end_hg_pr_grope


label hg_pr_grope_T3_E1:

    call hg_pr_grope_intro

    #elif her_whoring >= 12: # LEVEL 05+

    stop music fadeout 1.0
    call her_main("......","annoyed","worriedL")
    call her_main("Well...","open","base")
    her "During the potions class today..."
    her "I wrote a note on a piece of paper..."
    her "I was about to slide it to my lab partner when..."
    call play_music("chipper_doodle") # HERMIONE'S THEME.
    call her_main("Professor Snape snatched it right out of my hand...","annoyed","angryL")
    call her_main("He then read it out loud before the entire class...","annoyed","annoyed")
    m "What did the note say?"
    call her_main("Well...","open","down")
    her "It said: \"You can touch my butt if you want. I bet professor Snape would never notice.\""
    call her_main("Everyone was laughing...","angry","down_raised")
    her "It was so embarrassing I wanted to die..."
    call her_main("I really hate professor Snape, [genie_name]...","angry","angry")
    m "What happened then?"
    call her_main("Nothing...","open","down")

    call play_music("playful_tension") # SEX THEME.
    hide screen hermione_main
    with d3
    $ sc34CG(2, 19, 6, 5)

    call her_main("But when the class was over...",xpos="base",ypos="base")
    call her_main("These two nasty-looking boys from \"Slytherin\" cornered me...")
    call her_main("Actually they weren't mean to me or anything...")
    call her_main("So we just waited for everyone to leave the classroom...")
    $ sc34CG(2, 16, 6, 9)
    call ctc

    call her_main("And then I let them touch me...","angry","base")
    $ sc34CG(2, 17, 6, 9)
    call her_main("They touched me everywhere, [genie_name]...")
    m "\"Everywhere\", huh?"
    call her_main("Yes... Everywhere, [genie_name]...","soft","ahegao")
    call her_main("There were hands under my skirt, under my shirt...","base","glance")
    $ sc34CG(2, 16, 6, 9)
    call her_main("And then I started to breathe heavily...")
    call her_main("So one of them just put his hand over my mouth...","soft","ahegao")
    her "And their hands were so... thorough..."
    $ sc34CG(2, 17, 6, 9)
    call her_main("My head started to spin...")
    $ sc34CG(2, 16, 6, 9)
    call her_main("It was most exhilarating, [genie_name].","base","glance")
    m "Very good, [hermione_name]. Very good indeed."

    show screen blkfade
    hide screen sccg

    jump end_hg_pr_grope


label hg_pr_grope_T3_E2:

    call hg_pr_grope_intro

    call her_main("Actually something quite unexpected happened to me today, [genie_name]...","base","base")
    her "Right after the Defence Against the Dark Arts class..."
    her "This stocky \"Hufflepuff \" boy came up to me..."
    call play_music("playful_tension") # SEX THEME.
    call her_main("He said someone told him that I let boys touch me...","angry","wink")
    call her_main("Normally I would deny everything...","base","glance")
    her "But I decided not to waste the opportunity..."
    call her_main("I took the boy to a quiet spot and let him touch me...","base","ahegao_raised")
    her "I let him run his hands up and down my thighs..."
    her "I let him fondle my breasts..."
    call her_main("All the usual things...","base","glance")
    m "Well done, [hermione_name]."

    jump end_hg_pr_grope


label hg_pr_grope_T3_E3:

    call hg_pr_grope_intro

    stop music fadeout 1.0
    call her_main("Well...","upset","wink")
    her "I did what you told me to do, [genie_name]..."
    her "But... it sort of... ehm..."
    call her_main("Well, it sort of escalated into something else...","base","ahegao_raised")
    call play_music("playful_tension") # SEX THEME.
    m "Hm?"
    call her_main("uhm...","upset","wink")
    her "I sort of... got caught while I was letting this one boy fondle my breasts..."
    m "You got caught? By one of the teachers?"
    call her_main("No, [genie_name]...","base","base")
    call her_main("By the boy's girlfriend...","smile","baseL")
    m "Interesting..."
    call her_main("She was furious with him at first...","angry","base")
    call her_main("But then...","angry","wink")
    call her_main("Ehm... She started to touch my breasts as well...","base","down")
    call her_main("Almost the same way her boyfriend did just a moment ago...","smile","angry")
    her "Then she turned to him and she said..."
    call her_main("\"I love you baby, and I want to share everything with you...\"","open","closed")
    her "\"...And that includes your whores.\""
    call her_main("I did not appreciate being called a whore of course...","angry","base")
    call her_main("But that was such a sweet and romantic gesture...","base","base")
    her "Wouldn't you agree, [genie_name]?"
    m "Totally..."
    m "Seems that true love {size=+5}does{/size} exist after all."
    m "Then what happened?"
    call her_main("Ehm... Well, they kissed of course...","grin","worriedCl", emote="05")
    call her_main("And then they both started to touch me again...","upset","wink")
    call her_main("And then he was kind of only touching her and she was only touching him...","annoyed","worriedL")
    her "And they kissed..."
    her "I suddenly felt like the third wheel in that situation, so I just slipped away quietly..."
    m "I see..."

    jump end_hg_pr_grope
