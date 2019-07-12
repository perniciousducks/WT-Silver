label l_tutoring_check:
    if her_tutoring == 0:
        jump l_tutoring
    elif her_tutoring == 1 and her_whoring >= 1:
        jump l_tutoring
    elif her_tutoring == 2 and her_whoring >= 2:
        jump l_tutoring
    elif her_tutoring == 3 and her_whoring >= 3:
        jump l_tutoring
    elif her_tutoring == 4 and her_whoring >= 5:
        jump l_tutoring
    elif her_tutoring == 5 and her_whoring >= 8:
        jump l_tutoring
    elif her_tutoring == 6 and her_whoring >= 11:
        jump l_tutoring
    elif her_tutoring == 7 and her_whoring >= 14:
        if adult_mag_ITEM.number >= 1:# Adult magazines
            jump l_tutoring
        else:
            m "I need to buy adult magazines for this lesson."
    elif her_tutoring == 8 and her_whoring >= 17:
        if porn_mag_ITEM.number >= 1:# Porn magazines
            jump l_tutoring
        else:
            m "I need to buy porn magazines for this lesson."
    elif her_tutoring == 9 and her_whoring >= 20:
        if vibrator_ITEM.number >= 1:# Vibrator
            jump l_tutoring
        else:
            m "I need to buy a vibrator for this lesson."
    elif her_tutoring == 10 and her_whoring >= 23:
        if anal_plugs_ITEM.number >= 1:# Anal plugs
            jump l_tutoring
        else:
            m "I need to buy anal plugs for this lesson."
    elif her_tutoring == 11 and her_whoring >= 23:
        jump l_tutoring
    elif her_tutoring == 12 and her_whoring >= 23:
        jump l_tutoring
    elif her_tutoring == 13 and her_whoring >= 23:
        jump l_tutoring
    else:
        m "Not the right time. Soon..."

    jump hermione_requests

label l_tutoring:
    $ d_flag_01 = False

    if her_tutoring == 0:   # Whoring lvl 0
        call her_main("Again, thank you for doing this for me, sir...","open","base",xpos="base",ypos="base",trans="fade")
        call her_main("Shall I go and fetch my books?","open","suspicious")
        m "What?"
        call her_main("My Books, [genie_name]. I need to study them more for my tests.","soft","baseL")
        call her_main("All the knowledge I need is in those books!","annoyed","angryL")
        m "Books can't teach you everything, girl... Some knowledge only comes with practice and experience!"
        m "(I'm really just going to make this shit up as I go, ain't I?)"
        call her_main("Maybe... I mean, you're not chosen as the head of Hogwarts by chance.","annoyed","suspicious")
        m "Sometimes you seem to forget that, Miss Granger."
        call her_main("That sounded like something professor Snape would say...","open","suspicious")
        call her_main(".........","annoyed","suspicious")
        call her_main("Sorry about that, he thinks he's always right and it annoys me.","smile","happyCl")
        m "..........."
        call her_main("Sir?","soft","baseL")
        g4 "It's time to talk about your future, child."
        stop music fadeout 1.0
        call her_main("I'm not a child anymore, professor!","normal","frown")
        m "In a way you're right, but..."
        her "..........."
        m "I can tutor you, but you need to understand certain things about magic."
        m "With proper training, you can learn to increase your magic ability."
        play music ms_manatees fadein 1 fadeout 1
        call her_main("Yes?","soft","baseL")
        m "Certain emotions like love and hate, pleasure and pain..."
        g9 "{size=-2}(If she falls for that, I'm a true genius!){/size}"
        call her_main("I've been studying magic for years and I've never heard of such a thing.","normal","base")
        g4 "{size=-2}(Shit.){/size}"
        m "And that's exactly why you're still a child. You still have much to learn about magic."
        call her_main("Please stop that, professor. Nobody considers me a child anymore.","open","base")
        m "Yes, technically..."
        call her_main("Technically?!","open","base")
        g4 "Enough of this. You came to me to ask for my help, and if it starts like that..."
        call her_main("Yes, I suppose you are right...","angry","angry")
        call her_main("Alright, I'm ready to study hard with you!","base","base")
        g9 "{size=-2}(Yes!){/size}"
        call her_main("What was that?","open","annoyed",cheeks="blush")
        m "Uh, yes I'm glad you're beginning to understand, child."
        her "..........."
        m "Alright, I want you to take some time and think about what I've said. Next time we'll start with your first lesson."
        call her_main("Can't we start now?","open","base")
        m "Miss Granger, you're not the only student I must take care of."
        call her_main("You're tutoring someone else?","open","base")
        m "{size=-2}(If only...){/size}"
        m "I must take care of all the students of this school."
        m "But yes, there is another girl who needs..."
        call her_main("A Slytherin girl?!","scream","wide")
        g9 "That is none of your business, miss Granger."
        call her_main("Yes, professor. I'm sorry, but with all the recent events I'm a little on edge.","angry","angry")
        m "Apology accepted, and now goodnight!"
        call her_main("Good night, professor, and thanks again for taking some of your precious time to help me.","base","base")
        hide screen hermione_main

        call nar("You dismiss Hermione.")

        call her_walk(xpos="door", ypos="base", speed=3)

        call her_main("{size=-4}(I'm glad the professor agreed to tutor me!){/size}","base","worriedCl",cheeks="blush",ypos="head")
        call her_main("{size=-4}(But pleasure and pain? I don't understand where this is going...){/size}","annoyed","baseL",ypos="head")

        call her_chibi(action="leave")

        $ her_tutoring = 1
        $ aftercum = False
        jump day_start

    if her_tutoring == 1:   # Whoring lvl 1
        call her_main("","base","base",xpos="base",ypos="base",trans="fade")
        m "Miss Granger, time for your first lesson."
        call her_main("Yes, professor.","soft","baseL")
        m "Have you thought about what we discussed?"
        call her_main("Not really, I'm not sure what you mean by \"emotions\".","normal","base")
        g9 "{size=-2}(You'll learn soon enough, girl.){/size}"
        m "For example, what was your state of mind when you heard those rumours about the Slytherin girls?"
        call her_main("Please don't bring that up, sir! it really makes me mad!","scream","wide")
        m "And what is this feeling?"
        call her_main("...{w=0.5}an emotion, I suppose...","normal","base")
        m "Yes, and don't you have emotions you prefer over others?"
        call her_main("When I have the best score at a test.","smile","happyCl")
        m "{size=-2}(This girl is a monomaniac...){/size}"
        m "Don't you have other passions, things you like to do?"
        call her_main("Yes! Studying and reading books.","smile","happyCl")
        g4 "{size=-2}(By all the ancient gods...){/size}"
        m "Things are not going in the right direction..."
        call her_main("And what direction is that, sir?","normal","base")
        g9 "{size=-2}(You impaled on my cock!){/size}"
        m "Adulthood, Miss Granger, adulthood..."
        call her_main("I am by far the most mature of my peers, professor. What more can you ask?","open","closed")
        m "......{w=0.5}Miss Granger, did we not discuss this already? You need to accept you still have much to learn."
        m "I'm tired of all this, and I have work to do. Goodnight, child."
        call her_main("Tutoring one of those filthy Slytherin girls, maybe?","open","annoyed",cheeks="blush")
        m "Maybe that's the right direction, think about what all those girls do with professors."
        call her_main("But...{w=0.5} that's so wrong...{w=0.8} I don't know if I want to think about that.","open","base")
        m "If you want to progress and to restore the Gryffindor pride, you must!"
        call her_main("Yes, you're right! It's my mission! I'll do my best, professor.","grin","angry",cheeks="blush")
        g9 "{size=-2}(She is so naive, it's adorable.){/size}"
        m "Good, now time to go to bed, child."
        call her_main("{size=-2}(Tsh... Like I'm going to bed at this time, I need to study more.){/size}","normal","frown")
        hide screen hermione_main
        call nar("You dismiss Hermione.")

        call her_walk(xpos="door", ypos="base", speed=2)

        call her_main("{size=-4}(Filthy whores...){/size}","angry","angryCl",cheeks="blush",ypos="head")
        call her_main("{size=-4}(Oh, I should not talk like that...{w=0.5} but it feels so good!){/size}","base","worriedCl",cheeks="blush",ypos="head")

        call her_chibi(action="leave")

        $ her_tutoring = 2
        $ aftercum = False
        jump day_start

    elif her_tutoring == 2:   # Whoring lvl 2
        m "So, have you thought about emotions and their usefulness in the practice of magic?"
        call her_main("Yes, first I tried to cast a spell while thinking of the behaviour of those Slytherin girls.","open","closed")
        call her_main("It made me so angry and confused that I lost my focus and failed miserably.","annoyed","base")
        call her_main("I don't think it helps at all.","annoyed","suspicious")
        m "That's your problem Miss Granger, you think you already know the answer and don't follow my instructions."
        m "I don't care about the behaviour of those girls."
        call her_main("What? Professor! You don't care?!","scream","wide_stare")
        g9 "{size=-2}(Oh, I do care, just not in the way you think.){/size}"
        m "For this exercise, Miss Granger, for this exercise. Don't get on your high horse."
        call her_main(".........","annoyed","ahegao")
        call her_main("Sorry about that, {w=0.5}again.","open","suspicious")
        m "I need you to focus on what those girls do with professors, not their behaviour in general."
        call her_main("But...","open","base",cheeks="blush")
        m "Last time you were talking about your sacred duty and at the first hurdle you hesitate."
        call her_main("{size=-2}(\"Sacred\"? Don't exaggerate, old man){/size}","annoyed","down")
        call her_main("{size=-2}(Or not! Maybe I'll be remembered later for being the saviour of Gryffindor house!){/size}","open","worriedCl",cheeks="blush")
        call her_main("Yes, you're right! It {b}is{/b} my sacred duty!","smile","baseL")
        g9 "{size=-2}(It works every time, it's too easy... She looks so proud of herself.){/size}"
        call her_main("I'll do my best, professor!","open","base",cheeks="blush")
        g9 "I'm excited too... uh, I'm sure you will."
        call her_main("I'm glad you have such high confidence in me.","grin","worriedCl")
        m "And I'm glad you're starting to believe in this. I think you have the potential to master this branch of magic."
        call her_main("You seem tired, professor.","open","suspicious")
        g11 "{size=-2}(Tired of waiting to annihilate your ass.){/size}"
        call her_main("Yes, professor?","annoyed","base")
        g9 "Yes we can!"
        m "Uh, I mean, I'm sure I'll tire you out soon enough, Miss Granger. How about you get some sleep?"
        call her_main("Sleep? I must study first.","open","closed")
        m "I wasn't thinking about that, but you're right, time to go to bed!"
        m "Just make sure to think about what you learned today."
        hide screen hermione_main
        call nar("You dismiss Hermione.")

        call her_walk(xpos="door", ypos="base", speed=2)

        call her_main("{size=-4}(Hmm, I wonder what he {b}was{/b} thinking about.){/size}","base","down_raised",cheeks="blush",ypos="head")
        call her_main("{size=-4}(Probably all the problems caused by those harlots.){/size}","base","glance",cheeks="blush",ypos="head")
        call her_main("{size=-4}(Well, I will never be like them, so no need to worry.){/size}","silly","glance",cheeks="blush",ypos="head")

        call her_chibi(action="leave")

        $ her_tutoring = 3
        $ aftercum = False
        jump day_start

    elif her_tutoring == 3:   # Whoring lvl 3
        call her_main("Sir, I want to apologize for doubting you.","open","base")
        m "Yes?"
        call her_main("Your \"atypical\" method works!","angry","worriedCl",emote="05")
        m "{size=-2}(Impossible!){/size}"
        m "It works? I mean, yes, naturally it works!"
        m "I'm glad you've succeeded. Now tell me more."
        call her_main("I managed to levitate a heavy rock while thinking about the behaviour of two girls I saw earlier in the library.","open","closed")
        call her_main("Usually I only manage to move small rocks. I don't know, I felt kind of warm inside thinking about that.","mad","angry",cheeks="blush")
        her "It felt weird but... {w=0.5}good at the same time."
        m "{size=-2}(She is so ignorant of life! Unbelievable.){/size}"
        m "You've never felt such a sensation before?"
        call her_main("Generally I get angry and rush to stop such behaviour.","clench","worried",cheeks="blush",tears="soft")
        call her_main("But yesterday, I don't know, I just watched without interrupting them.","open","worriedCl",cheeks="blush")
        call her_main("And when I pictured it, as you told me to, it worked.","open","base",cheeks="blush")
        call her_main("I feel at the same level as those harlots, I'm so ashamed.","angry","angry",cheeks="blush")
        m "But you succeeded."
        g9 "{size=-2}(To my surprise...){/size}"
        call her_main("Yes! With this method I'll have better grades in my tests and win the House Cup for Gryffindor!","angry","worriedCl",cheeks="blush",emote="05")
        g9 "{size=-2}(In your dreams.){/size}"
        m "Good, good. Now I want to know more about those two girls."
        call her_main("It's not very relevant, professor. And I'm not sure this is appropriate.","annoyed","angryL",cheeks="blush")
        m "How will you improve yourself if I can't guide you?"
        m "And for that, I must know more."
        call her_main("Alright, but it's embarrassing.","annoyed","angryL",cheeks="blush")
        g9 "{size=-2}(Ooh, I hope they were naked!){/size}"
        call her_main("I went to the library to study interactions between plants...","open","closed")
        g11 "{size=-2}(Yeah, yeah, come on...){/size}"
        call her_main("... and I heard muffled sounds.","base","baseL",cheeks="blush")
        call her_main("I was hoping to catch a teacher doing bad things with one of those Slytherin whores.","annoyed","angryL",cheeks="blush")
        call her_main("I slowly headed towards the sounds and I discovered two girls in an alcove.","open","base",cheeks="blush")
        call her_main("I remained hidden to observe them.","grin","wink",cheeks="blush")
        g11 "{size=-2}(Come on!){/size}"
        call her_main("Yes, professor?","base","ahegao_raised",cheeks="blush")
        m "Yes, no, please continue."
        call her_main("They were kissing passionately.","open","worriedCl",cheeks="blush")
        g9 "And? And?"
        call her_main("And a moment later they began to...","open","closed")
        call her_main("They began to...","open","worriedCl",cheeks="blush")
        call her_main("They began to touch their breasts!","scream","wide",cheeks="blush")
        m "They were naked, I hope?"
        call her_main("What?","open","squint",cheeks="blush")
        her "No, fortunately they were dressed."
        call her_main("How can such a thing happen in our beloved school!","angry","angry",cheeks="blush")
        m "But you kept watching, didn't you?"
        call her_main("Only for educational purposes.","annoyed","angryL",cheeks="blush")
        g9 "{size=-2}(\"Educational purposes\"... ha-ha, I've never heard a worse excuse!){/size}"
        m "And during all this time you didn't feel a certain need?"
        call her_main("To my shame, yes. Like I said before, I felt kind of warm inside.","annoyed","angryL",cheeks="blush")
        call her_main("Like when I have to pee but... different. Better.","disgust","down_raised",cheeks="blush")
        m "This good sensation... next time you experience it, let it come."
        call her_main("But...","open","base",cheeks="blush")
        m "It's the only way to get better, Miss Granger."
        m "If you suppress it, it won't work."
        call her_main("Ok...{w=0.3} I'll try my best.","annoyed","angryL",cheeks="blush")
        her "But to be honest, sir, I thought you were going to punish those two sluts."
        m "Can you provide proof of their crime? No?"
        m "Even I can't punish students without proof of any wrongdoing."
        g11 "{size=-2}(With the possible exception of you!){/size}"
        m "Anyway, you've done well. I think it will be enough for this lesson."
        m "Remember what I've told you, and good night!"
        call her_main("Good night, professor.","base","base")
        hide screen hermione_main
        call nar("You dismiss Hermione.")

        call her_walk(xpos="door", ypos="base", speed=2)

        call her_main("{size=-4}(Well, I'll try to investigate those two girls again.){/size}","disgust","down_raised",cheeks="blush",ypos="head")
        call her_main("{size=-4}(Like a real anthropologist!){/size}","base","glance",cheeks="blush",ypos="head")
        call her_main("{size=-4}(Yes, that's right. Hermione the anthropologist!){/size}","base","worriedCl",cheeks="blush",ypos="head")

        call her_chibi(action="leave")

        $ her_tutoring = 4
        $ aftercum = False
        jump day_start

    elif her_tutoring == 4:   # Whoring lvl 5
        m "So, any luck with your \"studies\"?"
        call her_main("Yes! When you hear the results of my hunt, you'll be proud of me!","base","happyCl")
        m "{size=-2}(\"Hunt\"?){/size}"
        m "Your \"hunt\", Miss Granger?"
        call her_main("Yes, professor!","smile","happyCl")
        call her_main("Like an explorer in the wild jungle, I tracked those two filthy animals.","base","concerned",cheeks="blush",tears="soft")
        call her_main("With success, sir!","smile","happyCl",cheeks="blush",emote="06")
        call her_main("Hogwarts has so many dark and discreet corners...","annoyed","base")
        call her_main("Believe me, it wasn't easy, professor.","base","concerned",cheeks="blush",tears="soft")
        m "I'm sure you gave it your best."
        m "But right now I await your report."
        call her_main("Yes, but before that I want to clarify that my report is purely for scientific purposes.","base","ahegao_raised",cheeks="blush")
        m "{size=-2}(Sure...){/size}"
        call her_main("So I tracked down those two tarts to an area in the attic.","open","closed")
        call her_main("Which, by the way, seems to be the meeting place for girls of this... sort.","annoyed","suspicious")
        m "And what is your opinion on them?"
        call her_main("At least they don't sleep with professors in exchange for house points.","open","suspicious")
        call her_main("","annoyed","suspicious")
        m "And that's it? No \"this behavior must be severely punished\"?"
        m "Are you attracted to girls of this sort, Miss Granger?"
        call her_main("What? Lesbians? I'm not... I... No way, I...","open","base",cheeks="blush")
        m "Alright, alright, back to your report, if you please."
        call her_main("{size=-2}(I'm not a lesbian...{w=0.3} I think...){/size}","disgust","down_raised",cheeks="blush")
        call her_main("{size=-2}(Hermione, girl, pull yourself together! You're not a harlot!){/size}","mad","wide",cheeks="blush")
        call her_main("No, I'm not!","annoyed","closed",cheeks="blush")
        m "Excuse me?"
        call her_main("Uh... Yes, my report. My {b}scientific{/b} report.","open","base",cheeks="blush")
        m "{size=-2}(Yeah, we get it...){/size}"
        call her_main("So, like before, they started by kissing passionately.","open","worriedCl",cheeks="blush")
        call her_main("With the tongue and everything!","open","baseL",cheeks="blush")
        menu:
            "-Start to jerk off while she is talking-":
                $ d_flag_01 = True
                hide screen hermione_main
                hide screen blktone
                call nar(">You reach under the desk and grab your cock...")
                hide screen genie
                show screen genie_jerking_off
                with d3
                call ctc
            "Do nothing.":
                pass
        call her_main("","open","base",cheeks="blush")
        g9 "And? And?"
        call her_main("They pulled up their shirts and caressed each others breasts.","open","worriedCl",cheeks="blush")
        call her_main("{size=-2}(Their beautiful and tempting breasts...){/size}","open","ahegao_raised",cheeks="blush")
        call her_main("Later those nasty girls raised their skirts and started to touch each other \"there\" while kissing.","silly","ahegao_raised",cheeks="blush")
        call her_main("{size=-2}(I can't believe I said that!){/size}","base","ahegao_raised",cheeks="blush",tears="sweat")
        call her_main("They were very excited, and I could see their panties become wet.","open","ahegao_raised",cheeks="blush")
        call her_main("Disgusting.","annoyed","ahegao_raised",cheeks="blush")
        if d_flag_01:
            g9 "{size=-2}(Yes... yes...){/size}"
        call her_main("One of the girls went crazy and inserted her fingers into the other's \"thing\" and worked them furiously.","silly","worried",cheeks="blush",tears="soft")
        call her_main("Soon imitated by her girlfriend.","silly","ahegao_raised",cheeks="blush")
        call her_main("Those whores came so hard I'm sure they heard the screams on the other side of the grounds!","open_wide_tongue","ahegao_mad",cheeks="blush")
        if d_flag_01:
            her "{size=-2}(And I had to bite my lip, or else they would've heard me too...){/size}"
            hide screen hermione_main
            with d3

            call cum_block

            g11 "Yes! That's the stuff!"
            hide screen bld1
            with d1
            show screen genie_jerking_sperm
            call cum_block
            call ctc

            call gen_chibi("cum_on_desk")
            with d3

            call her_main("Professor!","angry","angry",cheeks="blush")

            m "You enjoyed it too, so don't act all innocent."

            $ her_mood += 7
            $ d_flag_01 = False
        else:
            m "You enjoyed it too."
        call her_main("Maybe...","annoyed","angryL",cheeks="blush")
        m "Anyway, I hope it was revealing."
        call her_main("\"Revealing\"? I'm not sure what you mean by that.","open","suspicious")
        call her_main("You're the headmaster, act as such!","open","base")
        call her_main("Do all you can to stop those acts of debauchery!")
        call her_main("","annoyed","angryL")
        m "Yes, of course."
        m "{size=-2}(Hypocrite...){/size}"
        her "{size=-2}(Old pervert...){/size}"
        m "You said that those girls became wet."
        g9 "Weren't you a little too?"
        call her_main("When I went to bed I noticed it, yes.","disgust","down_raised",cheeks="blush")
        call her_main("Apparently bad fluids are released from your body when you have faced such acts.","mad","wide",cheeks="blush")
        m "No, they aren't bad. It happens when you're excited."
        call her_main("No way! I can control myself!","scream","worriedCl",cheeks="blush",tears="soft_blink")
        call her_main("","angry","angry",cheeks="blush")
        m "No one can control their base desires."
        m "Consider this well, and enjoy your night, Miss Granger."
        call her_main("Good night, professor.","annoyed","worriedL")
        hide screen hermione_main
        call nar("You dismiss Hermione.")

        call her_walk(xpos="door", ypos="base", speed=2)

        call her_main("{size=-4}(I enjoyed it too much. Maybe I'm becoming a pervert as well){/size}","base","ahegao_raised",cheeks="blush",ypos="head")
        call her_main("{size=-4}(I lost control, it won't happen again!){/size}","shock","down_raised",cheeks="blush",ypos="head")
        call her_main("{size=-4}(Good thing I'm not a degenerate like those filthy girls!){/size}","base","glance",cheeks="blush",ypos="head")

        call her_chibi(action="leave")

        $ her_tutoring = 5
        $ aftercum = False
        jump day_start

    elif her_tutoring == 5:   # Whoring lvl 8
        m "Bravo, last time you experienced your first \"emotion\"."
        call her_main("Yes, I remember but I still don't see the link with magic.","open","suspicious")
        m "{size=-2}(Me neither...){/size}"
        m "If you want to progress, you have to go a little further than a simple observation."
        m "You'll need to participate."
        call her_main("What! No way I'll participate in such debauchery!","scream","closed",cheeks="blush")
        call her_main("How can you even suggest such a thing!","angry","angry")
        m "Oh you don't have to go that far in one go."
        call her_main("I'm not sure I want to go there at all.","open","closed")
        m "How many times do I have to remind you why you're doing this?"
        call her_main("Yes but...","open","base")
        m "But what?"
        call her_main("A girl like me shouldn't stoop to such practices.","annoyed","suspicious")
        m "A girl like you should use all means at their disposal in order to excel."
        her "..........."
        call her_main("Alright, but this must remain between us.","annoyed","angryL",cheeks="blush")
        call her_main("You cannot disclose this to other professors, especially professor Snape!","annoyed","down")
        m "Oh, I have no intention of shar.. speaking of you with professor Snape."
        g9 "{size=-2}(You're mine.){/size}"
        call her_main("Well, what must I do now?","open","closed")
        m "Come here."
        hide screen hermione_main
        hide screen bld1
        with d3

        call her_walk_desk_blkfade

        hide screen genie
        show screen no_groping_01
        call hide_blkfade
        call ctc

        call bld
        m "Have you ever touched yourself?"
        call her_main("Professor!","base","concerned",cheeks="blush",tears="soft",xpos="mid",ypos="base")
        show screen groping_01
        with d7
        call nar(">You touch her leg with your hands.")
        m "Please answer the question, Miss Granger. Have you ever touched yourself?"
        call her_main("No, it's... it's wrong!","annoyed","angryL",cheeks="blush")
        m "But when you looked at these girls, you felt certain emotions."
        call her_main("Yes and ?","grin","wink",cheeks="blush")
        m "You didn't feel the need to touch yourself?"
        call her_main("Yes... but I resisted.","base","ahegao_raised",cheeks="blush")
        call nar(">You start to caress her thigh.")
        call her_main("Professor...","open","worriedCl",cheeks="blush")
        m "And you felt those emotions without even touching yourself."
        call her_main("Yes...","open","base",cheeks="blush")
        g9 "{size=-2}(What a slut!){/size}"
        if her_whoring <= 12 or hermione_wear_bra:
            call nar(">You move forward to her panties.")
        else:
            call nar(">You move forward to her pussy.")
        call her_main("","open","worriedCl",cheeks="blush")
        m "Good."
        hide screen groping_01
        show screen no_groping_01
        with d3
        call nar(">You stop caressing her.")
        call her_main("Why... why did you stop?","mad","wide",cheeks="blush")
        m "Oh, because I need you to think about all this before we meet again."
        call her_main("But...","mad","wide",cheeks="blush")
        m "Good night, my dear."
        call her_main("Good night, professor.","annoyed","worriedL")

        hide screen hermione_main
        call blkfade

        hide screen no_groping_01
        "You dismiss Hermione."
        call her_chibi("stand","desk","base")
        show screen genie
        hide screen bld1
        call hide_blkfade

        call her_walk(xpos="door", ypos="base", speed=2.5)

        call her_main("{size=-4}(This is wrong...){/size}","disgust","down_raised",cheeks="blush",ypos="head")
        call her_main("{size=-4}(I shouldn't listen to him.){/size}","angry","worriedCl",cheeks="blush",ypos="head")
        call her_main("{size=-4}(And yet...){/size}","base","down_raised",cheeks="blush",ypos="head")

        call her_chibi(action="leave")

        $ her_tutoring = 6
        $ aftercum = False
        jump day_start

    elif her_tutoring == 6:   # Whoring lvl 11
        m "So, have you started practising my teachings?"
        call her_main("I don't even know where to start.","open","suspicious")
        m "You see, the secret is to stimulate appropriate areas."
        m "Areas which are more sensitive than others."
        call her_main("You mean my intimate areas, sir?!","annoyed","angryL",cheeks="blush")
        m "Well, they're called intimate for a reason."
        m "You said you've never touched yourself because it was wrong."
        m "But it's never wrong to exercise ones body in order to reach a new level of consciousness."
        g4 "{size=-2}(The things I have to make up...){/size}"
        m "You can begin with your breasts, for example."
        m "But you shouldn't only caress your nipples but also grab your tits and squeeze them."
        m "And in the meanwhile, you can think of those two girls."
        g9 "Or what you want to do with those girls."
        call her_main("What makes you think... No, I don't want...","angry","worriedCl",cheeks="blush",emote="05")
        call her_main("I definitely don't want to have {b}anything{/b} to do with those harlots!","scream","worriedCl",cheeks="blush")
        m "Don't lie to yourself. It's obvious that you feel a form of attraction to those two girls."
        call her_main("I...{w=0.3} I honestly don't know what to think anymore.","mad","angry",cheeks="blush")
        her "At the moment my feelings are so confusing..."
        g9 "{size=-2}(Exactly what I was hoping!){/size}"
        call her_main("I'm happy to earn points for my house and at the same time I feel so ashamed.","angry","suspicious",cheeks="blush",tears="messy")
        her "And the same goes for your lessons."
        m "Yet you can't deny your progress in the practice of magic."
        call her_main("...{w=0.2} Yes...{w=0.2} perhaps you're right.","base","concerned",cheeks="blush",tears="soft",tears="sweat")
        m "You have to let it go, Miss Granger, follow your instincts!"
        g9 "{size=-2}(Grab my cock and wank it savagely!){/size}"
        call her_main("I'm not sure if...","open","concerned",cheeks="blush",tears="mascara")
        m "Enough procrastination, time for practice!"
        m "Come here."
        hide screen hermione_main
        hide screen bld1
        with d3

        call her_walk_desk_blkfade

        ">Hermione walks towards your desk."
        ">You grab her tits and massage them softly."
        pause.5

        hide screen genie
        show screen groping_03
        with d1
        hide screen blkfade
        call her_main("","open","worriedCl",cheeks="blush",xpos="mid",ypos="base")
        call ctc

        call bld
        m "Like I said, it's important you learn how to properly stimulate your \"emotional\" body areas."
        m "It's not enough if I do it myself, you need to practice when you're alone."
        call her_main("","upset","worriedCl",cheeks="blush")
        m "Like in your bed or in the shower, for example."
        call nar(">You keep massaging her tits...")
        call her_main("","open","worriedCl",cheeks="blush")
        call nar(">You feel her nipples becoming hard.")
        call her_main("Yes but...{w=0.3} Professor, it's inappropriate for a girl of good education!","open","base",cheeks="blush")
        m "Don't let old prejudices weigh you down. You're a girl with great potential."
        call nar(">You gently squeeze her nipples through the fabric.")
        call her_main("Ah, thank you professor.","open","ahegao_raised",cheeks="blush")
        m "A girl with a brilliant mind."
        call nar(">You increase your grip on her nipples.")
        m "A girl who will become a woman of exception."
        call her_main("Ahh yes... I'm already a woman of exception you fool.","grin","angry",cheeks="blush")
        m "Fool?"
        call nar(">You firmly pinch her nipples.")
        call her_main("Ahhh yesss, not that hard, yesss...","silly","worried",cheeks="blush",tears="soft")
        call nar(">You abruptly stop.")

        call blkfade
        pause.5

        call her_main("Don't stop, you idiot!","scream","angry",cheeks="blush",emote="01",ypos="head")

        hide screen hermione_main
        hide screen groping_03
        show screen genie_and_hermione
        hide screen genie_and_hermione
        show screen genie
        show screen hermione_stand
        call hide_blkfade

        call her_main("...........","mad","wide",cheeks="blush")

        call her_chibi("stand","desk","base")
        show screen genie
        hide screen bld1
        call hide_blkfade

        call her_main("Sorry, professor.","angry","angry",cheeks="blush")
        m "Lesson is over. Time to practice by yourself."
        m "Good night my little witch."
        call her_main("Good night, professor, and thank you for this lesson.","base","happyCl")
        call her_main("{size=-2}(I just wish it had lasted longer...){/size}","annoyed","suspicious")
        hide screen bld1
        hide screen hermione_main
        with d3

        call her_walk(xpos="door", ypos="base", speed=2.5)

        call her_main("{size=-4}(\"My little witch?\"){/size}","annoyed","angryL",cheeks="blush",ypos="head")
        call her_main("{size=-4}(Why not, after all...){/size}","base","ahegao_raised",cheeks="blush",ypos="head")

        call her_chibi(action="leave")

        $ her_tutoring = 7
        $ aftercum = False
        jump day_start

    elif her_tutoring == 7:   # Whoring lvl 14
        m "So, Miss Granger, have you practised my teachings?"
        call her_main("Yes...{w=0.2} a little.","annoyed","angryL",cheeks="blush")
        m "And?"
        call her_main("It feels even better when I'm naked.","smile","happyCl",cheeks="blush",emote="06")
        call her_main("{size=-2}(Oh no, I shouldn't have said that...){/size}","mad","wide",cheeks="blush")
        m "Well come here and undress, we'll practice."
        call her_main("Completely?!","mad","angry",cheeks="blush")
        m "No, only the top will suffice."
        g9 "{size=-2}(For the moment...){/size}"
        call her_main("I'll be showing you my breasts without even earning any points?","open","suspicious")
        m "You can't have both points and lessons."
        call her_main("Ok...","angry","worriedCl",cheeks="blush",emote="05")

        hide screen hermione_main
        $ hermione_wear_robe = False
        call her_chibi("lift_top")

        call set_her_action("lift_top")

        hide screen hermione_main
        $ hermione_wear_robe = False
        $ hermione_wear_top = False
        call set_her_action("none")

        call her_main("Like that?","annoyed","angryL",cheeks="blush")

        if hermione_wear_bra:
            m "Without your bra Miss Granger..."
            hide screen hermione_main
            $ hermione_wear_bra = False
            call update_her_body
            call her_main()

        m "Yes, and now come here."
        call her_main("........","annoyed","closed",cheeks="blush")
        call her_main("","base","closed")
        m "Now."

        call her_walk_desk_blkfade

        ">Hermione slowly walks towards your desk."
        ">She tries not to bounce her tits without much success..."
        call her_chibi("hide")
        hide screen genie
        show screen genie_and_tits_01
        with d1

        hide screen blkfade
        call her_main("","base","closed",xpos="mid",ypos="base")
        call ctc

        call bld
        m "Now let's get serious if you want to."
        g9 "{size=-2}(Well, even if you don't...){/size}"

        hide screen hermione_main
        call blkfade

        ">You grab her tits and squeeze them gently."

        show screen chair_left
        hide screen genie_and_tits_01
        show screen groping_naked_tits
        call hide_blkfade
        call ctc

        call her_main("Professor, what are you doing?","disgust","down_raised",cheeks="blush")
        g9 "Teaching you, dear, teaching you."
        m "Doesn't it feel good?"
        call her_main("A little...","base","closed")
        m "Your hard nipples say the contrary."
        m "I can stop if you want."
        call her_main("Yeah sure!","grin","angry",cheeks="blush")
        call her_main("Suck them professor.","silly","ahegao_raised",cheeks="blush")
        g9 "As you wish, princess."
        call her_main("","silly","ahegao_raised",cheeks="blush")
        call nar(">You suck her nipples with devotion.")
        call her_main("Yes {image=textheart} like that.","silly","ahegao_raised",cheeks="blush",tears="sweat")
        call nar(">You start to chew on her nipples.")
        call her_main("Ah, noo, don't...","open_tongue","ahegao_raised",cheeks="blush")
        call nar(">You chew on them even harder.")
        call her_main("Not that hard, I will...","open_wide_tongue","ahegao_mad",cheeks="blush")
        g9 "{size=-2}(Time for the grand finale!){/size}"

        if hermione_wear_panties:
            ">You quickly slip your hand into her panties and rub her pussy furiously."
        else:
            ">You quickly move your hand toward her pussy and rub it furiously."

        call her_main("Yes! {image=textheart}","angry","dead",cheeks="blush",tears="crying")
        her "I... I..."
        g9 "Came, my dear."

        hide screen hermione_main
        call blkfade
        call ctc

        call set_her_action("none","update")

        hide screen chair_left
        hide screen groping_naked_tits
        hide screen genie
        show screen genie_and_hermione
        call hide_blkfade

        call her_main("Is the lesson over professor?","grin","glance",cheeks="blush",tears="mascara")
        m "Not if you don't want it to be."
        her "Maybe it's enough for tonight."
        call her_main("After all, you have a lot of work to do.","grin","concerned",cheeks="blush",tears="mascara")
        m "Sure."
        m "But before that I have a little present for you."

        call give_gift(">You give an assortment of adult magazines to Hermione.",adult_mag_ITEM)

        m "I hope this will help you in your studies."
        call her_main("Yes, certainly.","grin","closed",cheeks="blush",tears="mascara")
        her "Thank you and good night professor."
        m "Good night dear child."

        hide screen hermione_main
        call blkfade

        hide screen genie_and_hermione
        "You dismiss Hermione."
        call her_chibi("stand","desk","base")
        show screen genie
        call hide_blkfade

        call her_walk(xpos="door", ypos="base", speed=2.5)

        call her_main("{size=-4}(I'm such a slut...){/size}","base","ahegao_raised",cheeks="blush",ypos="head")
        call her_main("{size=-4}(Cumming in front of my professor...){/size}","base","down_raised",cheeks="blush",ypos="head")
        call her_main("{size=-4}(I definitely need to do that again!){/size}","base","glance",cheeks="blush",ypos="head")

        call her_chibi(action="leave")

        $ her_tutoring = 8
        $ aftercum = False
        jump day_start

    elif her_tutoring == 8:   # Whoring lvl 17
        m "So tell me, were your readings enlightening?"
        call her_main("I'm not sure if \"readings\" is the right term but yes. Very \"stimulating\" too.","angry","worriedCl",cheeks="blush")
        m "Maybe it's time to discover new areas to stimulate."
        call her_main("You mean my pussy, right?","open","suspicious")
        call her_main("I'm not an idiot, professor.","annoyed","angryL")
        m "If it doesn't suit you, we can stop here."
        call her_main("And if I said stop?","annoyed","suspicious")
        g4 ".........."
        call her_main("Haha, you should have seen your face!","smile","angry",cheeks="blush")
        call her_main("With all your recent lessons you can imagine that this area isn't a *no man's land* any more.","smile","baseL")
        g4 "Have you slept..."
        call her_main("No I haven't! I'm not a harlot who offers her pussy to every boy around.","scream","closed",cheeks="blush")
        m "{size=-2}(Good, your pussy is mine alone!){/size}"
        call her_main("","annoyed","ahegao")
        g9 "{size=-2}(Although I may agree to share it with other girls...){/size}"
        m "I'm happy you're behaving honourably, Miss Granger."
        call her_main("Ha, who'd have guessed!","annoyed","angryL",cheeks="blush")
        m "Yes, I'm glad that my favourite student is not wasting her precious time with boys."
        her "Sure...{w=0.3} {size=-4}old hypocrite{/size}."
        m "Enough of this! Now take off your shirt and come here."
        call her_main("Here we go for another \"lesson\".","open","suspicious")

        call her_walk_desk_blkfade

        $ hermione_wear_robe = False
        $ hermione_wear_top = False
        call update_her_body

        if hermione_wear_bra:
            call her_main("...",ypos="head")
            m "And your bra..."

            $ hermione_wear_bra = False
            call update_her_body

        call her_main("........","annoyed","closed",cheeks="blush",ypos="head")

        call her_chibi("hide")
        hide screen genie
        show screen no_groping_06
        call hide_blkfade
        call ctc

        call her_main("And free tits again, enjoy!","grin","angry",cheeks="blush",xpos="mid",ypos="base")
        m "I definitely intend to."
        g9 "Now take off your skirt."
        pause.8

        call set_her_action("lift_skirt")
        pause.5

        $ hermione_wear_bottom = False
        call set_her_action("None")
        pause.5

        call her_main("","base","baseL",cheeks="blush")
        call ctc

        if hermione_wear_panties:
            call her_main("You love my pussy don't you?","base","ahegao_raised",cheeks="blush")
            g9 "Oh yes, I love your smell, especially when you're wet."
            call her_main("Professor...","angry","worriedCl",cheeks="blush",emote="05")
            hide screen no_groping_01
            show screen groping_06
            with d3
            call nar(">You caress her clit.")
            call her_main("Professor!","mad","wide",cheeks="blush")
        else:
            call her_main("You love my panties don't you?","base","ahegao_raised",cheeks="blush")
            g9 "Oh yes, I love their smell, especially when you're wet."
            call her_main("Professor...","angry","worriedCl",cheeks="blush",emote="05")
            hide screen no_groping_01
            show screen groping_06
            with d3
            call nar(">You caress her clit through the fabric.")
            call her_main("Professor!","mad","wide",cheeks="blush")
            m "Now take them off."

            $ hermione_wear_panties = False
            call set_her_action("pinch")

            call nar(">She slowly lowers her panties.")

            call set_her_action("None")

            hide screen groping_06
            show screen no_groping_06
            $ b_her_panties_off = True
            call her_main("","base","closed")
            call ctc

        m "What's great, you see, is that I have two hands."
        m "One can caress your clit while the other can play with your pussy."
        call nar(">You move from words to deeds and penetrate her already wet pussy with ease.")

        hide screen no_groping_06
        show screen groping_06
        with d3

        call her_main("Yes, you're probably right.","grin","angry",cheeks="blush")
        m "Probably?!"
        call nar(">While you're moving your finger in her pussy, you take over her clit with your thumb.")
        call her_main("Haa {image=textheart}, I'm only your humble student, I wouldn't know such naughty things.","silly","ahegao_raised",cheeks="blush")
        m "One finger is rarely enough even with a tight pussy like yours."
        call nar(">You insert a second finger in her tight and warm pussy...")
        call her_main("Yesss {image=textheart}, I'll try to remember your teachings.","silly","ahegao_raised",cheeks="blush")
        call nar(">You increase the pace and feel her pussy tighten on your fingers.")
        m "Maybe a third finger?"
        call her_main("Don't be so bold.","grin","angry",cheeks="blush",tears="soft")
        call nar(">Her whole body starts shaking as you increase your ramming.")

        hide screen groping_06
        show screen groping_06b
        with d3

        call her_main("Noo {image=textheart}{w=0.2} not so fast I will...","open_tongue","ahegao_raised",cheeks="blush")
        call nar(">You increase your pace even more.")
        call her_main("I will I will...","open_wide_tongue","ahegao_mad",cheeks="blush")
        g9 "Time to get serious."
        call nar(">You force your soaked thumb into her butthole.")
        call her_main("Haaaaa {image=textheart} yesss {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        g9 "Lucky girl."

        call blkfade

        hide screen hermione_main
        hide screen groping_06b
        hide screen genie
        show screen no_groping_01
        call hide_blkfade

        call her_main("I'm sure this lesson will be of great help tonight.","grin","glance",cheeks="blush",tears="mascara")
        call her_main("And the other nights {image=textheart}.","silly","worried",cheeks="blush",tears="soft")
        m "Always glad to help my little witch in her studies."
        call her_main("\"Studies\", yes, that's right.","grin","glance",cheeks="blush",tears="mascara")
        m "And to aid your studies I have even more scientific materials."

        call give_gift(">You give an assortment of porn magazines to Hermione.",porn_mag_ITEM)

        call her_main("I promise to study them every night until I commit their lessons to memory!","grin","closed",cheeks="blush",tears="mascara")
        call her_main("Thank you and good night professor.","grin","glance",cheeks="blush",tears="mascara")
        m "Good night, my favourite little witch."

        hide screen hermione_main
        call blkfade

        hide screen no_groping_01
        "You dismiss Hermione."

        call set_her_action("none","update") #Resets clothes.

        call her_chibi("stand","desk","base")
        show screen genie
        call hide_blkfade

        call her_walk(xpos="door", ypos="base", speed=2.5)

        call her_main("{size=-4}(Favourite...){/size}","base","ahegao_raised",cheeks="blush",ypos="head")
        call her_main("{size=-4}(There's another one?){/size}","mad","wide",cheeks="blush",ypos="head")
        call her_main("{size=-4}(I'll do my best to remain his favourite!){/size}","base","worriedCl",cheeks="blush",ypos="head")

        call her_chibi(action="leave")

        $ her_tutoring = 9
        $ aftercum = False
        jump day_start

    elif her_tutoring == 9:   # Whoring lvl 20
        m "So, Miss Granger, have you had an enjoyable night?"
        call her_main("You shouldn't ask such things, Professor.","open","closed")
        m "I have to make sure my students have a pleasant nights rest."
        call her_main("With your teachings and your \"scientific\" literature, indeed.","base","concerned",cheeks="blush",tears="soft")
        call her_main("I'll become proficient in human anatomy with all this documentation.","angry","worriedCl",cheeks="blush")
        m "Do you need some scientific instruments for your research?"
        call her_main("They could come in handy.","grin","wink",cheeks="blush")
        call her_main("As long as it's not your dick.","annoyed","angryL",cheeks="blush")
        call her_main("{size=-2}(Not that I don't appreciate it but no points no cock!){/size}","smile","angry",cheeks="blush")
        m "Miss Granger! This is a serious matter!"
        call her_main("Sure...","annoyed","suspicious")
        m ".........."
        call her_main("So what's my gift this time?","open","suspicious")

        call give_gift(">You give the vibrator to Hermione",vibrator_ITEM)

        call her_main("And I suppose you want me to test this in front of you?","open","closed")
        g9 "Of course."
        call her_main("Where is the educational purpose in all of this?","annoyed","suspicious")
        m "Good question. Improving your skills?"
        call her_main("At what? Magic?","mad","angry",cheeks="blush")
        m "Certainly."
        her "........."
        call her_main("I have one request though.","open","baseL",cheeks="blush")
        call her_main("If I'm going to masturbate I don't want to be the only one. So enjoy the free show.","open","worriedCl",cheeks="blush")
        g9 "With pleasure!"
        call nar(">You reach under the desk and grab your cock.")

        hide screen hermione_main
        call blkfade

        hide screen genie
        show screen genie_jerking_off
        with d3

        call hide_blkfade

        call her_main("{size=-2}(Thinking of the headmaster masturbating makes me wet already {image=textheart}){/size}",xpos="mid",ypos="base")
        call her_main("{size=-2}(I've become such a whore. Not that I don't enjoy it...){/size}","smile","angry",cheeks="blush")
        call her_main("So... where do we start?","open","squint",cheeks="blush")

        if hermione_wear_bra:
            m "Take off your shirt and bra, I want to see your tits."
            pause.5

            call set_her_action("lift_top")
            pause.5

            $ hermione_wear_robe = False
            $ hermione_wear_top = False
            $ hermione_wear_bra = False
            call set_her_action("None")
            pause.5

        else:
            m "Take off your shirt, I want to see your tits."
            pause.5

            call set_her_action("lift_top")
            pause.5

            $ hermione_wear_robe = False
            $ hermione_wear_top = False
            call set_her_action("None")
            pause.5

        her "You love them don't you?"
        g9 "Oh yes..."
        her "Having watched the other girls I now know why."
        her "Those breasts are so tempting."
        call her_main("Big or small, I want to hold them in my hands and suck the nipples.","open_tongue","ahegao_raised",cheeks="blush")
        g9 "Me too, me too!"
        m "Now remove your skirt!"
        pause.5

        call set_her_action("lift_skirt")
        pause.5

        $ hermione_wear_bottom = False
        call set_her_action("None")
        pause.5

        call ctc

        her "Good idea."
        call her_main("Sometimes I wish I could do this with others girls.","open","squint",cheeks="blush")
        call her_main("Masturbate naked in front of each other.","open","ahegao_raised",cheeks="blush")
        if hermione_wear_panties:
            g9 "Yes go on, take off your panties!"
            her "Your wish is my command."
            pause.5

            call set_her_action("pinch")
            pause.5

            $ hermione_wear_panties = False
            call set_her_action("None")
            pause.5

            $ u_tears_pic = "characters/hermione/face/e_her_tears_02b.png"
            call ctc

            call her_main("And mine is to touch another girl's pussy.","silly","ahegao_raised",cheeks="blush")
        else:
            call her_main("Touch her pussy like I'm touching mine now.","silly","ahegao_raised",cheeks="blush")

        call set_her_action("pinch")
        pause.5

        call her_main("Caress it.","open_tongue","ahegao_raised",cheeks="blush")

        call set_her_action("fingering")
        pause.2

        call her_main("Insert my fingers into her wet pussy.","open_tongue","ahegao_raised",cheeks="blush")
        g11 "Yes, yes! Now the vibrator!"

        hide screen hermione_main
        call blkfade

        ##call her_pose("vibrator")
        $ vibrator = True
        show screen hermione_main

        call hide_blkfade
        call ctc

        her "Oh I had forgotten about it already."
        call her_main("I want to hear her moan as I work my fingers.","open_wide_tongue","ahegao_mad",cheeks="blush")
        her "Hear her cum!"
        call her_main("Like me! Aaah yesssss! {image=textheart} {image=textheart}","open_wide_tongue","ahegao_mad",cheeks="blush")
        #$ b_her_squirt = True # the squirting needs some work. Graphically, I mean.
        call ctc
        g11 "Ahh! You little whore!!!"
        show screen genie_jerking_sperm
        her "The vibrator... aaah I'm still cumming!!"
        show screen genie_jerking_sperm_02
        g11 "Take this!"

        hide screen hermione_main
        call blkfade

        ">Hermione catches her breath and puts her clothes back on."

        call set_her_action("none","update") #Resets clothes.

        hide screen her_naked
        call her_chibi("stand","desk","base")
        call gen_chibi("cum_on_desk")
        call hide_blkfade

        #$ aftercum = True   # the aftercum skirt is a bit overkill IMO. Maybe reduce the height of the stains and add some dripping down the legs.

        call her_main("I hope you enjoyed it as much I did.","open","concerned",cheeks="blush",tears="mascara",xpos="right",ypos="base")
        m "Oh fuck yes, you're doing great, my little witch!"
        g9 "Very good!"
        call her_main("Thank you, professor.","grin","concerned",cheeks="blush",tears="mascara")
        m "After all this, you need to rest."
        call her_main("Oh yes. Good night professor.","grin","closed",cheeks="blush",tears="mascara")
        m "Good night, my dirty little slut."
        call nar("You dismiss Hermione.")

        call her_walk(xpos="door", ypos="base", speed=2.5)

        call her_main("{size=-4}(Rest...){/size}","base","down_raised",cheeks="blush",ypos="head")
        call her_main("{size=-4}(Not before I've played with this marvelous toy again){/size}","base","glance",cheeks="blush",ypos="head")
        call her_main("{size=-4}(And again){/size}","silly","glance",cheeks="blush",ypos="head")

        call her_chibi(action="leave")

        $ her_tutoring = 10
        $ aftercum = False
        jump day_start

    elif her_tutoring == 10:   # Whoring lvl 23
        m "So... I hope my lessons are paying off."
        call her_main("You mean, by making me more \"open\" to the wonders of adulthood?","open","suspicious")
        m "Among other things..."
        call her_main("That's what I thought.","annoyed","suspicious")
        call her_main("But to be honest, I was looking forward to this lesson.","open","closed")
        call her_main("{size=-2}(Maybe, I shouldn't have said that){/size}","angry","wide")
        her "{size=-2}(This will drive him crazy and he'll rape me savagely on his desk){/size}"
        call her_main("{size=-2}(Not that I would mind...){/size}","angry","worriedCl",cheeks="blush")
        call her_main("{size=-2}(And I could ask him for points afterwards){/size}","smile","baseL")
        m "Miss Granger? Are you alright?"
        call her_main("Yes professor! Sorry, I was thinking of my next exam.","grin","wink",cheeks="blush")
        m "Oh, I'm sure it's an important one. Maybe next lesson I can help you revise."
        call her_main("I would love that!","open","worriedCl",cheeks="blush")
        m "So, anal stimulation..."
        call her_main("Ah! I knew you would say that.","smile","angry",cheeks="blush")
        her "{size=-2}(Once again, not that I mind...){/size}"
        call her_main("{size=-2}(I'm such a whore, even the Slytherin girls can't compete...){/size}","base","ahegao_raised",cheeks="blush")
        m "Come again, Miss Granger?"
        call her_main("In this school nobody can compete with me, right professor?","smile","happyCl",cheeks="blush",emote="06")
        call her_main("In any field!","smile","angry",cheeks="blush")
        m "In any field? I'm not sure."
        m "You still have things to learn..."
        call her_main("What?! What are we waiting for then?","scream","closed",cheeks="blush")

        call set_her_action("lift_top")
        pause.2

        $ hermione_wear_robe = False
        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call set_her_action("None")

        ">She rips off her shirt and rushes to your desk."

        call her_walk_desk_blkfade

        hide screen genie
        show screen groping_05
        call hide_blkfade
        call ctc

        call bld
        m "We haven't even started yet and you're already wet, my adorable slut."

        show screen blktone
        call her_main("It's you and your dirty talk!","annoyed","angryL",cheeks="blush",xpos="mid",ypos="base")
        her "Talking about anal insertions, asshole licking and... and..."
        call her_main("Fisting!","open","ahegao_raised",cheeks="blush")
        m "I never mentioned any of that."
        call her_main("Oh. You didn't?","annoyed","ahegao_raised",cheeks="blush")
        call her_main("Well maybe you didn't but you {b}were{/b} thinking about it!","base","ahegao_raised",cheeks="blush")
        g9 "Maybe."
        g9 "Your ass is so luscious I could eat it."
        call her_main("My point exactly!","angry","worriedCl",cheeks="blush")
        call her_main("Enough talking, old man. Get to work!","base","concerned",cheeks="blush",tears="soft")
        m "I haven't even given you your gift yet!"
        m "I'll just put it where you'll be sure to find it."
        m "So, can we start the lesson?"
        call her_main("Yes for Merlin's sake!","open","base",cheeks="blush")
        m "But before that..."
        call her_main("If you say another word I swear I will go back to my dorm right now!","scream","angry",cheeks="blush",emote="01")
        call nar(">You suddenly insert the anal plug.")
        call her_main("Yesss {image=textheart} like that!","silly","ahegao_raised",cheeks="blush")
        call nar(">You remove it just as quickly while giving her butt a loud slap.")

        play sound sd_boing1
        with flashbulb
        play sound sd_slap
        with hpunch

        call her_main("Yessss more {image=textheart}.","open_tongue","ahegao_raised",cheeks="blush")
        g9 "As you wish, princess."
        call nar(">You promptly insert and remove it.")

        play sound sd_boing1
        pause.1
        play sound sd_slap
        with hpunch

        call her_main("More!!","open_tongue","ahegao_raised",cheeks="blush")

        play sound sd_boing1
        pause.1
        play sound sd_slap
        with hpunch

        $ u_tears_pic = "characters/hermione/face/e_her_tears_03b.png"
        call her_main("Aaaah {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")

        play sound sd_boing1
        pause.1
        play sound sd_slap
        with hpunch

        m "You can touch yourself too, you know."
        $ u_tears_pic = "characters/hermione/face/e_her_tears_03d.png"
        call her_main("I can't.","open_wide_tongue","ahegao_mad",cheeks="blush")
        her "{size=-2}(If I do, I will lose what little dignity I have left){/size}"
        call her_main("{size=-2}(But tonight...){/size}","open_wide_tongue","ahegao_mad",cheeks="blush")
        m "I'll handle it then."
        call nar(">You finger both her butthole and her pussy.")
        call her_main("Nooo it's too much {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        g9 "Faster? No problem!"
        hide screen groping_05
        show screen groping_05b
        call her_main("Aaah, you're killing me {image=textheart}.","angry","dead",cheeks="blush",tears="crying")
        call her_main("{size=-2}(And I love it){/size}","silly","worried",cheeks="blush",tears="soft")
        m "More fingers?"
        call her_main("No more pleassse.","open","concerned",cheeks="blush",tears="mascara")
        m "Actually, it wasn't a question."
        call her_main("If you keep this pace I will...","angry","dead",cheeks="blush",tears="crying")
        call nar(">You feel her muscles tighten on your fingers.")
        call her_main("Come!!","open_wide_tongue","ahegao_mad",cheeks="blush")
        g9 "Good girl."
        her "Keep it up, I..."
        call her_main("Yessss {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        m "I can keep this up as long as you please."
        call her_main("Yesss {image=textheart}, nooo I will die!","open_wide_tongue","ahegao_mad",cheeks="blush")
        g9 "In ecstasy."
        call her_main("Aahh not again {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        hide screen groping_05b
        show screen no_groping_05
        m "I think you've had enough for one night."
        call her_main("Yes I... I better go.","open_tongue","ahegao_raised",cheeks="blush")
        m "You forgot your gift."
        call nar(">You promptly insert the butt plug.")
        with hpunch
        call her_main("Aaaaaaah.","open_wide_tongue","ahegao_mad",cheeks="blush")

        hide screen hermione_main
        call blkfade

        hide screen no_groping_05
        show screen no_groping_05_desk

        ">She collapses panting on the desk."
        g9 "Best view in the world."

        ">After a while, she puts her shirt back on."

        call set_her_action("none","update") #Resets clothes.

        hide screen no_groping_05_desk
        show screen genie
        call her_chibi("stand","desk","base")
        call hide_blkfade
        pause.5

        call her_main("Thank you for everything, professor.",tears="mascara",xpos="right",ypos="base")
        call her_main("It was very...{w=0.5} enlightening.","grin","concerned",cheeks="blush",tears="mascara")
        call her_main("But please, try to go easy on me next time.","grin","closed",cheeks="blush",tears="mascara")
        g9 "I have absolutely no idea what you mean by that."
        call her_main("Good night professor.","grin","glance",cheeks="blush",tears="mascara")
        m "Good night, my dear anal whore."
        call her_main("Professor...","open","concerned",cheeks="blush",tears="mascara")

        call nar("You dismiss Hermione.")

        call her_walk(xpos="door", ypos="base", speed=2.5)

        call her_main("{size=-4}(Finally tonight I'll just go to bed){/size}","base","worriedCl",cheeks="blush",ypos="head")
        call her_main("{size=-4}(That was a little too intense){/size}","angry","worriedCl",cheeks="blush",ypos="head")
        call her_main("{size=-4}(Not that I'm complaining...){/size}","silly","glance",cheeks="blush",ypos="head")

        call her_chibi(action="leave")

        $ her_tutoring = 11
        $ aftercum = False
        jump day_start

    elif her_tutoring == 11:
        m "[hermione_name], I have something for you."
        call her_main("Another gift for me?","base","ahegao_raised",cheeks="blush")
        call her_main("Please, please.","open","worriedCl",cheeks="blush")
        m "You weren't this excited last time when I gave you a present..."
        call her_main("Oh don't worry, it was just a moment of weakness.","smile","angry",cheeks="blush")
        her "I'm ready now!"
        call her_main("{size=-2}(My body perhaps not...){/size}","annoyed","down")
        m "Did you have fun with your anal plug?"
        call her_main("Y-yes... I wear it sometimes...","base","ahegao_raised",cheeks="blush")
        call her_main("But I cut the tail!","annoyed","angryL",cheeks="blush")
        her "{size=-2}(No way I could walk around like that...){/size}"
        m "And you like it?"
        call her_main("It's very...{w=0.5} stimulating. It helps me whenever I cast a spell.","base","concerned",cheeks="blush",tears="soft")
        m "Tell me the truth Miss Granger, you wear it all the time, don't you?"
        call her_main("Nooo...","annoyed","angryL",cheeks="blush")
        call her_main("Maybe...","open_tongue","ahegao_raised",cheeks="blush")
        her "........"
        m "Don't be ashamed, it's alright my little whore."
        call her_main("I wear it all the time and...{w=0.3} I love it!","smile","happyCl",cheeks="blush",emote="06")
        g9 "{size=-2}(Marvelous){/size}"
        m "I've taught you good."
        call her_main("To be a slut? Yes you have...","open","closed")
        call her_main("And now I want more so where is my gift?!","annoyed","suspicious")
        m "There, there."

        call give_gift(">You give the anal beads to Hermione",anal_beads_ITEM)

        call her_main("Oh! That's even better than a butt plug.","shock","wide",cheeks="blush")
        g9 "And they can be useful for your pussy too."
        call her_main("So many possibilities...","smile","angry",cheeks="blush")
        her "...so little time."
        call her_main("I suppose you want me to try them out?","smile","happyCl")
        her "Or would you rather try them out on me yourself?"
        g9 "Oh yes."
        call her_main("I don't even know why I'm asking...","annoyed","ahegao")
        her "{size=-2}(Old pervert...){/size}"
        call her_main("{size=-2}({b}My{/b} old pervert){/size}","open","worriedCl",cheeks="blush")

        call set_her_action("lift_top")
        pause.5

        $ hermione_wear_robe = False
        $ hermione_wear_top = False
        $ hermione_wear_bra = False
        call set_her_action("None")
        pause.5

        call her_main("My tits are the best in all of Hogwarts!","silly","ahegao_raised",cheeks="blush")
        m "Have you been with many girls to say that?"
        call her_main("I wish...","grin","ahegao_mad",cheeks="blush")
        g9 "I can tutor you on that too."
        call her_main("Maybe we should finish this lesson first.","base","ahegao_raised",cheeks="blush")
        m "Oh, we have time."
        call her_main("Speaking of that...","base","concerned",cheeks="blush",tears="soft")

        call her_walk_desk_blkfade

        hide screen genie
        show screen no_groping_05
        with d1
        call hide_blkfade
        call ctc

        call bld
        g9 "As always, it's a delightful view."
        call blktone
        call her_main("I'm glad you love it.","angry","worriedCl",cheeks="blush",xpos="mid",ypos="base")

        call set_her_action("lift_skirt")
        pause.5

        $ hermione_wear_bottom = False
        $ hermione_wear_panties = False
        call set_her_action("None")
        pause.5

        call her_main("Can we start now?","grin","angry",cheeks="blush")
        g9 "I suppose you want them in your ass?"
        call her_main("Naturally.","base","ahegao_raised",cheeks="blush")
        call her_main("{size=-2}(I'll try them in my pussy later tonight){/size}","base","closed")
        hide screen no_groping_05
        show screen groping_05
        call nar(">You push the first bead in with ease.")
        her "Hmmm {image=textheart}"
        m "How many do you think you can take, my dear?"
        call her_main("How many have you got?","base","ahegao_raised",cheeks="blush")
        g9 "That's the spirit!"
        call nar(">You push another one inside with little resistance.")
        call her_main("Yess {image=textheart}, one more please.","open","ahegao_raised",cheeks="blush")
        call nar(">You feel the beads sink deeper when you push the third one inside.")
        call her_main("Ohhh, they're... they're moving {image=textheart}.","grin","ahegao_mad",cheeks="blush")
        call nar(">The fourth takes some work before it pops in.")
        call her_main("Ah {image=textheart} ah {image=textheart}.","silly","ahegao_raised",cheeks="blush")
        call nar(">You push the last one forcefully inside.")
        call her_main("Ahhhhh {image=textheart}, delightful.","open_tongue","ahegao_raised",cheeks="blush")
        her "They're so deep in my ass... almost like your cock."
        g9 "I can..."
        call her_main("No you can't! My butthole is too tight for both.","annoyed","closed",cheeks="blush")
        call her_main("{size=-2}(But it's such a good idea){/size}","grin","ahegao_mad",cheeks="blush")
        m "I'm sure there's still room for at least one finger."
        call nar(">You finger her butthole gently.")
        call her_main("Ahh... {image=textheart}{w=0.5} aah...{image=textheart}","silly","ahegao_raised",cheeks="blush")
        call her_main("W-What did I say...","grin","ahegao_mad",cheeks="blush")
        call nar(">You wiggle the finger inside.")
        call her_main("You never listen, old pervert.","grin","ahegao_mad",cheeks="blush")
        m "What can I say, I just know what's best for you, my little witch."
        call nar(">You pick up the pace.")
        call her_main("Yesss {image=textheart}.","grin","ahegao_mad",cheeks="blush")
        m "I thought you didn't want the finger?"
        g9 "In that case, one more finger."
        call nar(">She shivers when you insert a second finger.")
        call her_main("Ahh noo... no more please.","grin","angry",cheeks="blush")
        call her_main("My butthole is stretched so wide!","open","ahegao_raised",cheeks="blush")
        g9 "Your butthole is doing great."
        call nar(">You finger her butthole fiercely.")
        hide screen groping_05
        show screen groping_05b
        call her_main("Nooo... aahh {image=textheart}.","open","concerned",cheeks="blush",tears="mascara")
        m "Your pussy is getting neglected. We need to fix that!"
        call nar(">You start fingering her pussy with your other hand. She is panting heavily.")
        call her_main("Ah... ah... like that yesss {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        call nar(">You suddenly pull out all the beads.")
        call her_main("Ahhhhhh!!","grin","dead",cheeks="blush",tears="messy")
        call nar(">And insert four fingers in her ass.")
        call her_main("I'm cumming old bastard, I cumming!","silly","ahegao_raised",cheeks="blush")
        m "If you must..."
        call nar(">You continue to work her ass while you finger her pussy.")
        her "No don't I..."
        call her_main("Cummm {image=textheart}{image=textheart}.","silly","worried",cheeks="blush",tears="soft")
        call her_main("Agaaain aaah {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        g11 "Sorry my little anal whore but I'm starting to get tired."
        call her_main("Don't you dare stop now!","scream","angry",cheeks="blush",tears="messy")
        call her_main("Just a little more pleassse {image=textheart}.","grin","dead",cheeks="blush",tears="messy")
        call her_main("Because I will...","grin","dead",cheeks="blush",tears="messy")
        call her_main("Come again!!","open_wide_tongue","ahegao_mad",cheeks="blush")
        hide screen hermione_main
        call blkfade

        ">There's a small puddle on your desk from her juices. You slowly remove your fingers."

        hide screen groping_05b
        show screen no_groping_05_desk
        call hide_blkfade
        pause.5

        call her_main("*Pant* *pant*","open","concerned",cheeks="blush",tears="mascara")
        call her_main("I feel completely ravaged but happy.","grin","glance",cheeks="blush",tears="mascara")
        call her_main("Thank you professor, for letting me discover such great sensations.","grin","glance",cheeks="blush",tears="mascara")
        call her_main("But I'm exhausted so good night.","grin","closed",cheeks="blush",tears="mascara")
        hide screen hermione_main
        call blkfade

        ">She puts her shirt back on and rushes to the door."

        call set_her_action("none","update") #Resets clothes.

        hide screen no_groping_05_desk
        call her_chibi("stand","door","base",flip=True)
        show screen genie
        call hide_blkfade

        m "Come back here, girl."
        g11 "I need your mouth, I can't hold it anymore."
        pause.5

        call her_chibi("stand","door","base")
        pause.5

        call her_main("Professor!","open","squint",cheeks="blush")
        call her_main(".........","base","ahegao_raised",cheeks="blush")
        call her_main("Can I have points for this?","mad","wide",cheeks="blush")
        g11 "Now!"
        hide screen hermione_main
        call blkfade

        ">She comes back and does not seem particularly upset."

        call her_chibi("hide")
        hide screen genie
        $ gen_chibi_xpos = -10
        $ gen_chibi_ypos = 10
        $ g_c_u_pic = "blowjob_ani"
        show screen chair_left
        show screen g_c_u
        call hide_blkfade
        call ctc

        her "*Slurp!* *Slurp!* *Gulp!*"
        g9 "Yes, like that..."
        call nar(">Hermione eagerly sucks your dick.")
        m "You seem to be in a hurry. Is it because you're not getting points for this?"
        m "Consider it a payment for your private lessons."
        her "Mmmh..."
        m "Next time, come with your robe and your robe only."
        call nar(">She briefly nods.")
        her "*Slurp!* *Gulp!* *Slurp!*"
        g9 "You're doing great my little whore, I will..."
        g11 "Yes!"

        call cum_block
        $ g_c_u_pic = "cum_in_mouth_ani"
        show screen g_c_u
        hide screen bld1
        with d3

        her "*Gobble!* *Gobble!* *Gobble!*"
        call ctc

        g9 "Good girl, you swallowed it all!"
        call blkfade

        ">She wipes her mouth."
        hide screen g_c_u
        hide screen chair_left
        show screen genie
        call her_chibi("stand","desk","base")
        call hide_blkfade
        call ctc

        call her_main("Sir, I still think I deserve some...","annoyed","angryL",cheeks="blush")
        m "Good night, my dear child."
        call her_main(".........","annoyed","ahegao_raised",cheeks="blush")
        call her_main("Good night, professor.","annoyed","closed",cheeks="blush")
        call nar("You dismiss Hermione.")

        call her_walk(xpos="door", ypos="base", speed=2.5)

        call her_main("{size=-4}(Sucking his cock without getting any points!){/size}","annoyed","angryL",cheeks="blush",ypos="head")
        call her_main("{size=-4}(If he hadn't made me come so hard...){/size}","base","ahegao_raised",cheeks="blush",ypos="head")
        call her_main("{size=-4}(*sigh* Although I guess it's not that high a price...){/size}","base","down_raised",cheeks="blush",ypos="head")

        call her_chibi(action="leave")

        $ her_tutoring = 12
        $ aftercum = False
        jump day_start

    elif her_tutoring == 12:
        call her_main("Oh! I can't believe I forgot! Stay where you are, I'll be right back!","mad","wide",cheeks="blush")
        hide screen hermione_main
        play sound sd_door
        call blkfade

        play sound sd_door
        pause.3

        ###MAKE HER WEAR JUST A ROBE
        if h_robe in gryffindor_robe_list:
            $ hermione_robe = "characters/hermione/clothes/robe/robe_2_g.png"
        elif h_robe in slytherin_robe_list:
            $ hermione_robe = "characters/hermione/clothes/robe/robe_2_s.png"
        call set_her_action("naked") #Removes all clothes.
        $ hermione_wear_robe = True
        call update_chibi_uniform

        call her_chibi("stand","door","base")
        call hide_blkfade

        call her_walk(xpos="mid", ypos="base", speed=2.5)

        call her_main("{size=-4}*panting*{/size} Oh good, you're still here.","open","base",cheeks="blush",xpos="right",ypos="base")
        m "Is it safe to assume you have honoured my request this time?"
        call her_main("I thought it was obvious.","open","squint",cheeks="blush")
        call her_main("I even had to hide in an alcove to avoid getting noticed on my way here!","open","base",cheeks="blush")
        call her_main("It was so embarrassing!","open","worriedCl",cheeks="blush")
        call her_main("{size=-2}(And exciting!){/size}","open","worriedCl",cheeks="blush")
        m "Are you sure you're not wearing anything underneath?"
        call nar(">Hermione opens up her cloak a little.")
        pause.2

        hide screen hermione_main
        if h_robe in gryffindor_robe_list:
            $ hermione_robe = "characters/hermione/clothes/robe/robe_3_g.png"
        elif h_robe in slytherin_robe_list:
            $ hermione_robe = "characters/hermione/clothes/robe/robe_3_s.png"
        call her_main("","open","squint",cheeks="blush")
        call ctc

        call her_main("Does this answer your question?","open","squint",cheeks="blush")
        m "Not really. It's hard to tell from this distance. I mean, it's so dark..."
        call her_main("...","annoyed","ahegao_raised")
        pause.2

        hide screen hermione_main
        if h_robe in gryffindor_robe_list:
            $ hermione_robe = "characters/hermione/clothes/robe/robe_open_g.png"
        elif h_robe in slytherin_robe_list:
            $ hermione_robe = "characters/hermione/clothes/robe/robe_open_s.png"
        call her_main("","base","closed",cheeks="blush",trans="d5")
        call ctc

        call her_main("Is that better?","base","glance",cheeks="blush")
        g9 "Oh yes, definitely. Well done, my girl."

        hide screen hermione_main
        if h_robe in gryffindor_robe_list:
            $ hermione_robe = "characters/hermione/clothes/robe/robe_3_g.png"
        elif h_robe in slytherin_robe_list:
            $ hermione_robe = "characters/hermione/clothes/robe/robe_3_s.png"

        call her_main("Alright then, can we start the lesson now?","smile","angry",cheeks="blush")
        m "Maybe, I don't know... do you like butterbeer?"
        call her_main("You know I do. What's that got to do with...","soft","baseL",cheeks="blush")
        g9 "......."
        call her_main("Do you mean...{w=0.3} no, no way professor!","scream","wide",cheeks="blush")
        m "Oh, rest assured, we won't start with the bottom end."
        call her_main("Still, professor, this is so dirty...","silly","ahegao_raised",cheeks="blush")
        call her_main("{size=-2}(And exciting){/size}","silly","ahegao_raised",cheeks="blush")
        call her_main("Moreover, my butthole isn't stretched enough.","annoyed","closed",cheeks="blush")
        g4 "Are you kidding me, with all your training!"
        call her_main("And what a training!","annoyed","ahegao_raised",cheeks="blush")
        call her_main("{size=-2}(Good thing I practised by myself, otherwise...){/size}","angry","worriedCl",cheeks="blush")
        g4 "Now stop making up excuses!"
        m "I can see you rubbing your thighs from excitement!"
        call her_main("I thought it was so dark in here...","open","squint",cheeks="blush")
        call her_main("Humm, okay, but you better start out easy on me.","annoyed","suspicious")
        g9 "I'm always gentle with you my dear child."
        call her_main("Yeah, obviously...","annoyed","ahegao")
        m "{size=-2}(It's not as if you don't like it rough){/size}"
        m "Alright, my desk, you, naked, now!"

        call her_walk_desk_blkfade

        $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking.
        pause.5

        ">Hermione slowly slides down her robe and climbs up your desk."

        $ hermione_wear_robe = False

        call her_chibi("dance","on_desk","on_desk")

        call hide_blkfade
        pause 1

        call blktone
        call her_main("You're crazy for my body, aren't you?",xpos="mid",ypos="base")
        m "Why do you ask..."
        call her_main("Because a girl likes to be complimented, professor!","annoyed","suspicious")
        call her_main("Especially when she's about to do these kinds of things!","annoyed","ahegao")
        m "I meant, of course you have a amazing body! That's not up to question."
        call her_main("Best in the school?","base","ahegao_raised",cheeks="blush")
        m "......{w=0.3} Yeah, yeah, best in the school."
        call her_main("I can tell you're lying!","mad","angry",cheeks="blush")
        m "Miss Granger, I've lived for a very long time and believe me, I have seen few women with a body like yours."
        m "And definitely none in this school."
        m "{size=-2}(Severus still hasn't sent those Slytherin whores up){/size}"
        m "{size=-2}(I wonder if I can fire him for that...){/size}"
        call her_main("Thank you, professor.","open","worriedCl",cheeks="blush")
        call her_main("Feel free to do use my body as you please.","angry","worriedCl",cheeks="blush")
        m "{size=-2}(*sigh* women...){/size}"
        m "Bend over the desk my dear little witch."
        call her_main("{size=-2}(It starts with my dear little witch and ends up with my dear anal whore...){/size}","annoyed","ahegao_raised",cheeks="blush")
        call her_main("{size=-2}(*sigh* men...){/size}","annoyed","ahegao_raised",cheeks="blush")
        call her_main("As you wish my dear {b}old{/b} headmaster.","open","squint",cheeks="blush")
        m "{size=-2}(If you knew how old I actually am...){/size}"
        hide screen hermione_main
        call blkfade

        ">Hermione languorously climbs down your desk and bends over it."

        call her_chibi("hide")
        hide screen genie

        show screen no_groping_laying_02

        call her_main("I'm ready, [genie_name].",ypos="head")
        ">You take an empty butterbeer bottle, spit on the neck and push it inside her butthole."

        hide screen no_groping_laying_02
        show screen scr_her_fingering_naked("slow")
        hide screen bld1
        hide screen blktone
        call hide_blkfade
        call ctc

        call her_main("Hmmm, yes like that.","base","ahegao_raised",cheeks="blush")
        call her_main("My pussy feels lonely without your care.","grin","wink",cheeks="blush")
        call nar(">You start to finger her pussy too.")
        m "Poor little thing."
        call her_main("What's better in life than this professor?","open","ahegao_raised",cheeks="blush")
        m "Oh, I don't know."
        call her_main("Thank you for letting me discover such pleasures.","open","worriedCl",cheeks="blush")
        g9 "{b}My{/b} pleasure."
        call her_main("It's even better when it's mutual, isn't it?","open","squint",cheeks="blush")
        m "Hmm, yes you're right. I'm glad you feel that way."
        call her_main("Now a little deeper please.","soft","baseL",cheeks="blush")
        call nar(">You push the whole bottle neck up inside her asshole.")
        call her_main("Ohhh, yesss! {image=textheart}","open","ahegao_raised",cheeks="blush")
        call her_main("More, faster!","open","ahegao_raised",cheeks="blush")
        show screen scr_her_fingering_naked()
        call nar(">You rotate the bottle while going back and forth deeper and deeper.")
        call her_main("Yessss, don't forget my pussy {image=textheart}.","grin","ahegao_mad",cheeks="blush")
        g9 "Oh, your pussy better be ready for what's coming!"
        call nar(">You insert all four fingers in her sopping wet pussy.")
        call her_main("Sweet Circe, aah, aah, that's too much! {image=textheart}","open","concerned",cheeks="blush",tears="mascara")
        m "Nothing is too much for my little whore."
        call nar(">You increase the pace of both hands.")
        call her_main("No, no, yes, yessss! {image=textheart}","grin","dead",cheeks="blush",tears="messy")
        call nar(">Most of the bottle is inside her now, leaving just enough to get a good grip.")
        m "Push the bottle, push it!"
        call nar(">Whenever she pushes it back you do the same in the other direction.")
        call her_main("This is, this is, aaaah!!! {image=textheart}{image=textheart}","open_wide_tongue","ahegao_mad",cheeks="blush")
        call nar(">Her whole body convulses as she comes hard.")
        hide screen hermione_main
        call blkfade

        hide screen scr_her_fingering_naked
        show screen no_groping_laying_02
        pause.3
        call hide_blkfade
        call ctc

        call her_main("*Panting* *panting*","grin","dead",cheeks="blush",tears="messy",ypos="head")
        call her_main("P-professor...{w=0.3} I'm so happy right now.","base","concerned",cheeks="blush",tears="soft")
        g9 "Glad to hear it."
        hide screen hermione_main
        call blkfade

        ">After a while, she makes herself somewhat presentable."

        $ hermione_wear_robe = True

        hide screen no_groping_laying_02
        show screen genie
        call her_chibi("stand","desk","base")
        call hide_blkfade

        call bld
        m "Sweet dreams my little princess."
        call her_main("You too, professor.","open","base",cheeks="blush",xpos="right",ypos="base")
        g9 "They are always sweet with you around."
        call her_main("Thank you.","base","ahegao_raised",cheeks="blush")
        m "And next time bring your books, I'll help you with your revisions."
        call nar("You dismiss Hermione.")

        call her_walk(xpos="door", ypos="base", speed=2.5)

        call her_main("{size=-4}(Yes, sweet dreams...){/size}","base","worriedCl",cheeks="blush",ypos="head")
        call her_main("{size=-4}(Sweet and wet!){/size}","silly","glance",cheeks="blush",ypos="head")

        call her_chibi(action="leave")

        $ her_tutoring = 13

        call set_her_action("none","update") #Resets clothes.

        $ aftercum = False
        jump day_start

    elif her_tutoring == 13:
        call her_main("I'll go get my books right away, sir!","soft","baseL")
        hide screen hermione_main
        play sound sd_door
        call blkfade
        pause 1

        #call set_her_action("hold_book")

        play sound sd_door
        pause.3

        call hide_blkfade
        call ctc

        call her_main("Revisions are a serious matter, [genie_name]!","open","worried")
        m "{size=-2}(My cock in your ass is a serious matter...){/size}"
        m "In this regard, I kinda lied, it's more of a mock exam than revisions."
        call her_main("What a surprise!","annoyed","ahegao_raised",cheeks="blush")
        m "I need to make sure you've been working out your butthole."
        call her_main("........","annoyed","ahegao_raised",cheeks="blush")
        g9 "With my cock."
        call her_main("I see...","annoyed","baseL")
        call her_main("I'm not against that but I bet I'll gain no points for this?","annoyed","angryL",cheeks="blush")
        m "I'm helping you with your revisions, why should you be getting points for that?"
        call her_main("And what revisions...","annoyed","closed",cheeks="blush")
        call her_main("Alright, since you have helped me a lot, I'm in.","base","baseL",cheeks="blush")
        call her_main("{size=-2}(I give myself away for free now, what a bad whore I make){/size}","base","concerned",cheeks="blush",tears="soft")
        m "Come here and strip."

        call her_walk_desk_blkfade

        hide screen hermione_main
        with d3

        call set_her_action("naked")
        call set_her_action("hold_book")

        call blktone
        hide screen blkfade
        call her_main(xpos="mid",ypos="base")
        call ctc

        m "Ok now, put your books down and bend over the desk, my little whore."
        pause.5

        call set_her_action("None")
        pause.5

        hide screen hermione_main
        call blkfade

        call her_chibi("hide")
        hide screen genie
        show screen no_groping_laying_02
        hide screen bld1
        hide screen blktone
        call hide_blkfade
        call ctc

        call bld
        g9 "You can open a book if you want."

        call her_main("I should read about this spell called \"the Clap\"!","annoyed","closed",cheeks="blush")

        hide screen hermione_main
        call nar(">You take advantage of her moment of distraction to force you cock into her butthole.")

        hide screen no_groping_laying_02
        show screen chair_left
        show screen scr_her_sex("slow")
        hide screen bld1
        with d1
        with hpunch
        pause.8

        call her_main("Ah, you brute {image=textheart}.","grin","ahegao_mad",cheeks="blush")
        m "Your butthole is the perfect fit, not too tight and not too stretched!"
        call her_main("You've trained me well...","silly","ahegao_raised",cheeks="blush")
        call nar(">You caress her clit while fucking her.")
        call her_main("Mmmh, yes {image=textheart}.","open","ahegao_raised",cheeks="blush")
        g9 "You love it don't you?"
        call her_main("Your cock in my ass, oh yes.","base","ahegao_raised",cheeks="blush")
        m "Even without points?"
        call her_main("Don't make me regret agreeing to this.","upset","worriedCl",cheeks="blush")
        m "Say you love it even without points."
        show screen scr_her_sex()
        call nar(">You increase the pace.")
        call her_main("Ahh yesss {image=textheart}.","open_tongue","ahegao_raised",cheeks="blush")
        call her_main("I'm such a whore, I love sex even for free.","mad","wide",cheeks="blush")
        g9 "You know it!"
        call her_main("Don't make it a habit.","open","squint",cheeks="blush")
        m "......"
        call nar(">You pull out your cock and roughly shove it back inside.")
        with hpunch
        call her_main("Aaaaah {image=textheart}.","open","ahegao",cheeks="blush")
        call her_main("I love being sodomized savagely by my headmaster.","silly","ahegao_raised",cheeks="blush")
        call nar(">And again.")
        with hpunch
        her "Yessss {image=textheart}."
        call her_main("I love his big cock in my ass.","silly","worried",cheeks="blush",tears="soft")
        call nar(">You slap her buttcheek.")
        play sound sd_slap
        with hpunch
        call her_main("And being punished for my sluttiness.","open","concerned",cheeks="blush",tears="mascara")
        play sound sd_slap
        with hpunch
        call her_main("Aah, like this, punish me more master {image=textheart}.","silly","worried",cheeks="blush",tears="soft")
        play sound sd_slap
        with hpunch
        call her_main("Yess!","open_wide_tongue","ahegao_mad",cheeks="blush")
        play sound sd_slap
        with hpunch
        call her_main("Mooore!","open_wide_tongue","ahegao_mad",cheeks="blush")
        play sound sd_slap
        with hpunch
        call her_main("I'm about to...","angry","dead",cheeks="blush",tears="crying")
        play sound sd_slap
        with hpunch
        pause.1
        play sound sd_slap
        with hpunch
        pause.1
        call her_main("Cuuuum {image=textheart}{image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        show screen scr_her_sex("fast")
        call nar(">You fuck her butthole fiercely.")
        call her_main("Yes, yes, again, aaaah {image=textheart}.","open_wide_tongue","ahegao_mad",cheeks="blush")
        g11 "Yes, my little whore, yes!"
        hide screen scr_her_sex
        show screen scr_her_sex_cum_outside()
        call her_main("*Panting* *panting*","open","concerned",cheeks="blush",tears="mascara")
        show screen scr_her_sex_cum_outside(1)
        g11 "*Panting* *panting*"

        hide screen hermione_main
        call blkfade

        hide screen chair_left
        hide screen hermione_main
        hide screen scr_her_sex_cum_outside
        pause 1
        show screen no_groping_laying_02
        hide screen bld1
        hide screen blktone
        call hide_blkfade
        pause.8

        call bld
        m "*sigh* that was, that was..."
        call her_main("Marvellous {image=textheart}.","smile","baseL")
        call her_main("I'm so glad you agreed to tutor me, professor...","silly","ahegao_raised",cheeks="blush")
        call her_main("Your lessons have changed my life so much!","smile","angry",cheeks="blush")
        g9 "{size=-2}(Victory!){/size}"
        call her_main("But if you think you can fuck me all the time without giving me points...","annoyed","angryL",cheeks="blush")
        call her_main("You're dreaming!","annoyed","ahegao_raised",cheeks="blush")
        m "{size=-2}(Ohhh...){/size}"
        m "Even occasionally?"
        her "......."
        call her_main("Only if you are well-behaved...","soft","baseL",cheeks="blush")
        g9 "I'm the most well-behaved professor in the whole school!"
        call her_main("Sure.","annoyed","angryL",cheeks="blush")
        call her_main("{size=-2}(At least, you're not the worst...){/size}","annoyed","ahegao_raised",cheeks="blush")
        m "Good night my, [hermione_name]."
        call her_main("Good night my, [genie_name].","base","baseL",cheeks="blush")

        hide screen hermione_main
        call blkfade

        ">You dismiss Hermione."
        ">She puts her clothes back on without haste."

        call set_her_action("none","update") #Resets clothes.

        hide screen no_groping_laying_02
        pause 1

        show screen genie
        call her_chibi("stand","desk","base")
        call hide_blkfade

        call her_walk(xpos="door", ypos="base", speed=2.5)

        call her_main("{size=-4}(\"my beloved prince\"...){/size}","base","down_raised",cheeks="blush",ypos="head")
        call her_main("{size=-4}(He's hardly Prince Charming but...){/size}","base","glance",cheeks="blush",ypos="head")
        call her_main("{size=-4}(I doubt Prince Charming could fuck me half as well as he can!){/size}","grin","ahegao_raised",cheeks="blush",ypos="head")

        call her_chibi(action="leave")

        $ her_tutoring = 14
        $ aftercum = False
        jump day_start




###UE CUSTOM THINGS
# Music
define ms_arabian_nights = "music/Arabian_Nights.mp3"
define ms_bushwick = "music/Bushwick_Tarantella_Loop.mp3"
define ms_croft_manor = "music/Croft_Manor.mp3"
define ms_dice_game = "music/Dice_Game.mp3"
define ms_gtkm = "music/Going_to_Kill_Me.mp3"
define ms_gorilla = "music/Gorilla_Theme.mp3"
define ms_india = "music/India's_Different.mp3"
define ms_jafar = "music/Jafar's_Hour.mp3"
define ms_kabul = "music/Kabul_Flight_Jumpstart.mp3"
define ms_manatees = "music/Music for Manatees.mp3"
define ms_marketplace = "music/Marketplace.mp3"
define ms_outlaw_star = "music/Outlaw_Star_Freedom.mp3"
define ms_ozone = "music/Ozone.ogg"
define ms_sleep_walking = "music/Sleep_Walking.mp3"
define ms_tension = "music/Tension.mp3"
define ms_the_calm_before = "music/The_Calm_Before.mp3"
define ms_the_eastern_wind = "music/The_Eastern_Wind.mp3"
define ms_the_kiss = "music/The_Kiss.mp3"
define ms_the_xfiles = "music/The_X-Files.mp3"
define ms_vision = "music/Vision.mp3"
# Sounds
define sd_boing1 = "sounds/boing.mp3"
define sd_boing2 = "sounds/boing02.mp3"
define sd_boing3 = "sounds/boing03.mp3"
define sd_burp = "sounds/burp.mp3"
define sd_door = "sounds/door.mp3"
define sd_door2 = "sounds/door2.mp3"
define sd_door3 = "sounds/door3.mp3"
define sd_fall = "sounds/fall.wav"
define sd_glitch = "sounds/gltch.mp3"
define sd_iris_run = "sounds/iris_run.mp3"
define sd_kungfupunch = "sounds/kung-fu-punch.mp3"
define sd_magic4 = "sounds/magic4.ogg"
define sd_monster = "sounds/mon.wav"
define sd_monster_dead = "sounds/mondead.wav"
define sd_pistol2 = "sounds/pistol2.mp3"
define sd_pop1 = "sounds/pop01.mp3"
define sd_pop2 = "sounds/pop02.mp3"
define sd_pop3 = "sounds/pop03.mp3"
define sd_punch1 = "sounds/punch01.mp3"
define sd_punch2 = "sounds/punch02.mp3"
define sd_rustling = "sounds/rustling.mp3"
define sd_scratch = "sounds/scratch.wav"
define sd_slap = "sounds/slap.mp3"
define sd_spit = "sounds/spit.mp3"
define sd_win2 = "sounds/win2.mp3"
# Screens
screen genie_and_hermione(): #Genie sitting, Hermione stands right in front of him (behind the desk even).
    tag favor
    add "images/rooms/main_room/genie_and_hermione_01.png" at Position(xpos = -84, ypos = 10)

screen groping_05():
    tag favor
    add "groping_05" at Position(xpos = -84, ypos = 10)
    add "groping_05_blinking" at Position(xpos = -84, ypos = 10)

screen groping_05b():
    tag favor
    add "groping_05b" at Position(xpos = -84, ypos = 10)
    add "groping_05_blinking" at Position(xpos = -84, ypos = 10)

screen no_groping_05():
    tag favor
    add "characters/hermione/chibis/grope_ass/back_d_05.png" at Position(xpos = -84, ypos = 10)
    add "groping_05_blinking" at Position(xpos = -84, ypos = 10)

screen no_groping_05_desk():
    tag favor
    add "characters/hermione/chibis/fingering/02.png" at Position(xpos = -84, ypos = 10)

screen no_groping_06(): #Facing Genie.
    tag favor
    add "characters/hermione/chibis/grope_ass/front_e_05.png" at Position(xpos = -84, ypos = 10)
    add "groping_06_blinking" at Position(xpos = -84, ypos = 10)

screen groping_06():
    tag favor
    add "groping_06" at Position(xpos = -84, ypos = 10)
    add "groping_06_blinking" at Position(xpos = -84, ypos = 10)

screen groping_06b():
    tag favor
    add "groping_06b" at Position(xpos = -84, ypos = 10)
    add "groping_06_blinking" at Position(xpos = -84, ypos = 10)

screen no_groping_laying_01():
    tag favor
    add "characters/hermione/chibis/fingering/01.png" at Position(xpos = -84, ypos = 10)

screen no_groping_laying_02():
    tag favor
    add "characters/hermione/chibis/fingering/b_01.png" at Position(xpos = -84, ypos = 10)

screen scr_her_fingering_naked(speed="normal"):
    tag favor
    if speed == "slow":
        add "ani_her_fingering_slow_naked" at Position(xpos = -84, ypos = 10)
    else:
        add "ani_her_fingering_naked" at Position(xpos = -84, ypos = 10)
    add "ani_her_fingering_blinking" at Position(xpos = -84, ypos = 10)

screen scr_her_sex(speed="normal"):
    tag favor
    if speed == "slow":
        add "ani_her_sex_slow_naked" at Position(xpos = -84, ypos = 10)
    elif speed == "normal":
        add "ani_her_sex_naked" at Position(xpos = -84, ypos = 10)
    elif speed == "fast":
        add "ani_her_sex_fast_naked" at Position(xpos = -84, ypos = 10)

screen scr_her_sex_cum_outside(blink=0):
    tag favor
    add "ani_her_sex_cum_outside_naked" at Position(xpos = -84, ypos = 10)

image groping_06: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "characters/hermione/chibis/grope_ass/front_e_01.png"
    pause.2
    "characters/hermione/chibis/grope_ass/front_e_02.png"
    pause.2
    "characters/hermione/chibis/grope_ass/front_e_03.png"
    pause.5
    "characters/hermione/chibis/grope_ass/front_e_02.png"
    pause.2
    "characters/hermione/chibis/grope_ass/front_e_01.png"
    pause.2
    repeat

image groping_06b: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "characters/hermione/chibis/grope_ass/front_e_01.png"
    pause.1
    "characters/hermione/chibis/grope_ass/front_e_02.png"
    pause.1
    "characters/hermione/chibis/grope_ass/front_e_03.png"
    pause.2
    "characters/hermione/chibis/grope_ass/front_e_02.png"
    pause.1
    "characters/hermione/chibis/grope_ass/front_e_01.png"
    pause.1
    repeat

image groping_06_blinking: #Animation of Hermione blinking her eyes.
    "images/animation/00.png"
    pause.1
    "characters/hermione/chibis/grope_ass/front_e_04.png"
    pause.1
    "images/animation/00.png"
    pause 3
    "characters/hermione/chibis/grope_ass/front_e_04.png"
    pause.1
    "images/animation/00.png"
    pause.1
    "characters/hermione/chibis/grope_ass/front_e_04.png"
    pause.1
    "images/animation/00.png"
    pause 3
    repeat

image groping_05: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "characters/hermione/chibis/grope_ass/back_d_01.png"
    pause.2
    "characters/hermione/chibis/grope_ass/back_d_02.png"
    pause.2
    "characters/hermione/chibis/grope_ass/back_d_03.png"
    pause.5
    "characters/hermione/chibis/grope_ass/back_d_02.png"
    pause.2
    "characters/hermione/chibis/grope_ass/back_d_01.png"
    pause.2
    repeat

image groping_05b: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "characters/hermione/chibis/grope_ass/back_d_01.png"
    pause.1
    "characters/hermione/chibis/grope_ass/back_d_02.png"
    pause.1
    "characters/hermione/chibis/grope_ass/back_d_03.png"
    pause.2
    "characters/hermione/chibis/grope_ass/back_d_02.png"
    pause.1
    "characters/hermione/chibis/grope_ass/back_d_01.png"
    pause.1
    repeat

image groping_05_blinking: #Animation of Hermione blinking her eyes.
    "images/animation/00.png"
    pause.1
    "characters/hermione/chibis/grope_ass/back_d_04.png"
    pause.1
    "images/animation/00.png"
    pause 3
    "characters/hermione/chibis/grope_ass/back_d_04.png"
    pause.1
    "images/animation/00.png"
    pause.1
    "characters/hermione/chibis/grope_ass/back_d_04.png"
    pause.1
    "images/animation/00.png"
    pause 3
    repeat

image ani_her_fingering_blinking: #Animation of Hermione blinking her eyes.
    "images/animation/00.png"
    pause.1
    "characters/hermione/chibis/fingering/blink.png"
    pause.1
    "images/animation/00.png"
    pause 3
    "characters/hermione/chibis/fingering/blink.png"
    pause.1
    "images/animation/00.png"
    pause.1
    "characters/hermione/chibis/fingering/blink.png"
    pause.1
    "images/animation/00.png"
    pause 3
    repeat

image ani_her_fingering_slow_naked:
    "characters/hermione/chibis/fingering/n_01.png"
    pause.3
    "characters/hermione/chibis/fingering/n_02.png"
    pause.3
    "characters/hermione/chibis/fingering/n_03.png"
    pause.3
    "characters/hermione/chibis/fingering/n_04.png"
    pause.3
    repeat

image ani_her_fingering_naked:
    "characters/hermione/chibis/fingering/n_01.png"
    pause.2
    "characters/hermione/chibis/fingering/n_02.png"
    pause.2
    "characters/hermione/chibis/fingering/n_03.png"
    pause.2
    "characters/hermione/chibis/fingering/n_04.png"
    pause.2
    repeat

image ani_her_sex_slow_naked:
    "characters/hermione/chibis/sex/n_01.png"
    pause.15
    "characters/hermione/chibis/sex/n_02.png"
    pause.15
    "characters/hermione/chibis/sex/n_03.png"
    pause.15
    "characters/hermione/chibis/sex/n_04.png"
    pause.15
    "characters/hermione/chibis/sex/n_05.png"
    pause.15
    "characters/hermione/chibis/sex/n_06.png"
    pause.15
    "characters/hermione/chibis/sex/n_07.png"
    pause.15
    repeat

image ani_her_sex_naked:
    "characters/hermione/chibis/sex/n_01.png"
    pause.1
    "characters/hermione/chibis/sex/n_02.png"
    pause.1
    "characters/hermione/chibis/sex/n_03.png"
    pause.1
    "characters/hermione/chibis/sex/n_04.png"
    pause.1
    "characters/hermione/chibis/sex/n_05.png"
    pause.1
    "characters/hermione/chibis/sex/n_06.png"
    pause.1
    "characters/hermione/chibis/sex/n_07.png"
    pause.1
    repeat

image ani_her_sex_fast_naked:
    "characters/hermione/chibis/sex/n_01.png"
    pause.05
    "characters/hermione/chibis/sex/n_02.png"
    pause.05
    "characters/hermione/chibis/sex/n_03.png"
    pause.05
    "characters/hermione/chibis/sex/n_04.png"
    pause.05
    "characters/hermione/chibis/sex/n_05.png"
    pause.05
    "characters/hermione/chibis/sex/n_06.png"
    pause.05
    "characters/hermione/chibis/sex/n_07.png"
    pause.05
    repeat

image ani_her_sex_cum_outside_naked:
    "characters/hermione/chibis/sex/sperm_n_01.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_02.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_03.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_04.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_05.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_06.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_07.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_08.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_09.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_10.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_11.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_12.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_13.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_14.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_15.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_16.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_17.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_18.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_19.png"
    pause 2
    "characters/hermione/chibis/sex/sperm_n_20.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_21.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_22.png"
    pause.1
    "characters/hermione/chibis/sex/sperm_n_23.png"
    pause.1
    repeat
