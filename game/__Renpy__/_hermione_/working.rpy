init python:
    class hermione_job(object):
        inProgress = False
        responses = ""
        
        def checkProgress(self):
            if self.inProgress:
                renpy.jump(self.responses)



label maid_responses:
    $ payment = renpy.random.randint(10, 25)

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    pause.2
    
    call h_outfit_OBJ(hg_maid_OBJ)
    
    show screen bld1
    call her_main("","base","base",xpos="right",ypos="base")
    pause.5
    
    menu:
        "-Ask her how her day was-":
            if day_random <= 2:
                m "How was your day?"
                her "It was as normal a day of cleaning rooms could be."
                her "Although considering that I'm supposed to be in class during the day I guess it's not that normal."
                m "Don't worry [hermione_name], you'll get your points."
                m "Just think of how happy your friends will be when they win the house cup this year."
                her "I suppose..."
                m "10 points to Gryffindor"
                her "Thank you [genie_name]"
                $ gryffindor+= 10
                $ gold += payment
            elif day_random >= 3 and day_random <= 5:
                her "Do I really have to keep doing this?"
                m "What do you mean [hermione_name]?"
                her "It's so degrading. I have to clean other students rooms!"
                m "You can stop anytime."
                her "I can?"
                m "Certainly, I'll just get one of those Slytherin floosies that you are always on about."
                m "I'm sure that they'd jump at the chance to make some points for their house."
                m "They'd probably even do it for next to nothing, if not free."
                her "Fine, I get your point. It's just, surely there are other ways for you to earn money [genie_name]?"
                her "I mean you're the school headmaster, can't you just file some reports and get paid by the ministry?"
                m "I can, it's just not as enjoyable."
                her "Hmmph. Can I at least get my points now?"
                m "Certainly, 10 points to Gryffindor."
                her "Thank you [genie_name]."
                $ gryffindor+= 10
                $ gold += payment
            elif day_random >= 6 and day_random <= 8:
                if whoring >= 15:
                    her " "
                else:
                    "bla bla bla"
            elif day_random >=9:
                if whoring >= 15:
                    "bla bla bla"
                else:
                    her "I think you need to start enforcing harsher punishment for sexual harrasment."
                    her "Hmmph. Can I at least get my points now?"
                    m "Certainly, 10 points to Gryffindor."
                    her "Thank you [genie_name]."
                    $ gryffindor+= 10
                    $ gold += payment
        "-Dismiss her-":
            her "Here's your payment."
            ">You receive [payment] gold coins."
            m "Well done [hermione_name], 20 points to Gryffindor."
            her "Thank you [genie_name]."
            $ gryffindor+= 20
            $ gold += payment

    call her_walk("mid","leave",2)
    
    $ hermione_sleeping = True
    $ current_job = 0
    jump night_main_menu

label barmaid_responses:
    $ payment = renpy.random.randint(20, 50)
    
    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    pause.2
    
    call h_outfit_OBJ(hg_maid_OBJ)
    
    show screen bld1
    call her_main("","base","base",xpos="right",ypos="base")
    pause.5
    
    menu:
        "-Ask her how her day was-":
            if day_random <= 2:
                her "Fine."
                m "Anything unusual happen?"
                her "Not really, I just served people drinks."
                m "Well in that case 10 points to Gryffindor."
                her "Thank you [genie_name], here's your payment."
                ">You receive [payment] gold coins."
                her "Good night [genie_name]."
                $ gryffindor+= 10
                $ gold += payment
            elif day_random >= 3 and day_random <= 5:
                "bla bla bla"
                jump day_time_requests
            elif day_random >= 6 and day_random <= 8:
                "bla bla bla"
                jump day_time_requests
            elif day_random >=9:
                "bla bla bla"
                jump day_time_requests
        "-Dismiss her-":
            her "Here's your payment."
            ">You receive [payment] gold coins."
            m "Well done [hermione_name], 20 points to Gryffindor."
            her "Thank you [genie_name]."
            $ gryffindor+= 20
            $ gold += payment
    
    call her_walk("mid","leave",2)
    
    $ hermione_sleeping = True
    $ current_job = 0
    jump night_main_menu

label gryffindor_cheer_responses:
    $ payment = renpy.random.randint(40, 80)

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    pause.2
    
    call h_outfit_OBJ(hg_gryffCheer_OBJ)
    
    show screen bld1
    call her_main("","base","base",xpos="right",ypos="base")
    pause.5
    
    menu:
        "-Ask her how her day was-":
            if day_random <= 2:
                m "Hello, [hermione_name], how was your day?"
                call her_main("It was good [genie_name], I think that the team is really starting to liven up.","base","base")
                m "How so?"
                call her_main("Well since I've started they seem to have improved their game.","open","base")
                call her_main("They also seem much happier. Harry is always looking at me with a smile on his face.","base","base")
                m "And does he look at you a lot?"
                call her_main("Of course he does, we're good friends.","open","base")
                m "I'm sure that must be the reason."
                call her_main("Well here's the money, [genie_name].","base","base")
                ">You receive [payment] gold coins."
                m "Well done, [hermione_name], 20 points to Gryffindor."
                call her_main("Thank you [genie_name].","base","happyCl")
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >= 3 and day_random <= 5:
                m "Hello, [hermione_name], how was your day?"
                call her_main("Tiring. This cheering really is quite exhausting.","open","worried")
                m "Anything interesting happen?"
                call her_main("Not unless you count me almost dropping my pom pom.","normal","base")
                m "I don't. Well did they pay you?"
                call her_main("Of course, here you are [genie_name]","open","base")
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                call her_main("Thank you [genie_name].","base","happyCl")
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >= 6 and day_random <= 8:
                m "Welcome back [hermione_name]."
                call her_main("Hello [genie_name].","open","base")
                m "How did you go today?"
                call her_main("Very well, all the boys said that I helped keep their spirits up.","open","base")
                m "{size=-5}I'm sure that wasn't the only thing you kept up...{/size}"
                call her_main("What was that [genie_name]?","open","suspicious")
                m "I was just saying that I'm sure you kept them entertained."
                call her_main("I think so.","open","worriedL")
                m "Well did they pay you for raising their \"spirits\"?"
                call her_main("Of course they did.","open","closed")
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                call her_main("Thank you [genie_name].","base","happyCl")
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >=9 and lock_public_favors == True or whoring <= 15:
                m "You seem very chipper today."
                call her_main("Of course I am, we won!","base","base")
                m "Won?"
                call her_main("We won! We beat Slytherin in a practice match.","smile","happyCl")
                m "You seem a little over-excited for a practice match."
                call her_main("Well it was such a game. Not to mention that we got to rub it in those Slytherin faces afterwards.","smile","baseL")
                m "Well I'm glad that you are enjoying your work."
                call her_main("I am [genie_name]. Given that most of the \"work\" I do to help the house has to be kept private, it feels good to do something public for my house.","open","base")
                m "Not to mention you get paid for it..."
                call her_main("Oh, right. Here you are.","soft","baseL")
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                call her_main("Thank you [genie_name].","base","happyCl")
            else:
                m "Welcome back [hermione_name], how was your day?"
                call her_main("We won! We managed to beat Slytherin.","base","base")
                m "That must have been very exhilarating. I'm sure your cheering gave the motivation to win."
                call her_main("I think it did [genie_name]. They were all very excited to receive their reward for winning the game.","base","happyCl")
                menu:
                    "-Reward?-":
                        m "What reward did you promise them?"
                        call her_main("Well I was so keen for us to beat Slytherin that I may have promised them that I would give them all blowjobs if they won.","grin","baseL")
                        m "You gave every team member a blowjob after the game?"
                        call her_main("And the water boy...","smile","glance")
                        m "How did that even work? Did you just crawl around the room on your knees?"
                        call her_main("Of course not, they all lined up and waited their turn.","scream","angryCl")
                        m "They lined up? And then what?"
                        call her_main("Well I sucked their cocks until they came and then I swallowed. Surely you of all people know how a blowjob works.","annoyed","worriedL")
                        m "That's not quite what I meant."
                        call her_main("Well I'm glad I did. I can't wait to rub it in Astoria's face tomorrow.","smile","baseL")
                        m "Well I'm glad you think it was worth it. Did they pay you?"

                        her "Of course they did [genie_name], here you are."
                    "-Okay-":
                        m "I'm sure they were. Did they pay you?"
                        her "Of course they did [genie_name], here you are."
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                her "Thank you [genie_name]."
        "-Dismiss her-":
            call her_main("Here's your payment [genie_name].","soft","baseL")
            ">You receive [payment] gold coins."
            m "Well done [hermione_name], 20 points to Gryffindor."
            call her_main("Thank you [genie_name].","base","happyCl")
            $ gryffindor+= 20
            $ gold += payment

    call her_walk("mid","leave",2)
    
    $ hermione_sleeping = True
    $ current_job = 0
    jump night_main_menu

label slytherin_cheer_responses:
    $ payment = renpy.random.randint(50, 100)

    call play_sound("door") #Sound of a door opening.
    call her_walk("door","mid",2)
    pause.2
    
    call h_outfit_OBJ(hg_slythCheer_OBJ)
    
    show screen bld1
    if day_random >=9 and lock_public_favors == False:
        $ uni_sperm = True 
        call her_main("","base","ahegao_raised",xpos="right",ypos="base")
    else:
        call her_main("","base","base",xpos="right",ypos="base")
    pause.5
        
    menu:
        "-Ask her how her day was-":
            if day_random <= 2:
                m "How was your day today [hermione_name]?"
                call her_main("Exhausting. Those Slytherin pigs insisted that I cheer for their entire practice session.","open","angryCl")
                her "They were hardly playing the game by the end. They were just standing there watching me."
                m "Well what was your routine?"
                call her_main("Mostly star jumps while I cheered \"Go Slytherin!\".","annoyed","frown")
                m "So you were just jumping up and down? That doesn't seem like a very intricate cheer."
                call her_main("It isn't but it's what they insisted I do.","annoyed","angryL")
                m "Well it definitely sounds like you earned your points."
                m "30 points to Gryffindor."
                call her_main("Thank you [genie_name], here's your payment.","open","closed")
                ">You receive [payment] gold coins."
                $ gold += payment
                $ gryffindor+= 30
            elif day_random >= 3 and day_random <= 5:
                m "How was your day today [hermione_name]?"
                call her_main("Uneventful. I completed my routine and then went back to my room.","open","suspicious")
                m "You didn't talk to anyone?"
                call her_main("I make a point of trying to avoid Slytherin student as best I can. ","annoyed","angryL")
                m "Are they really that unbearable."
                call her_main("Yes.","open","angryCl")
                m "Well, you earned your points."
                m "30 points to Gryffindor."
                call her_main("Thank you [genie_name], here's your payment.","open","closed")
                ">You receive [payment] gold coins."
                $ gold += payment
                $ gryffindor+= 30
            elif day_random >= 6 and day_random <= 8:
                m "Hello [hermione_name]."
                call her_main("Hello [genie_name].","normal","base")
                m "How did you go today?"
                call her_main("Very well. In fact I think I might be doing too well.","annoyed","worriedL")
                m "How so?"
                call her_main("I think that my cheering is having too positive an effect.","open","worried")
                call her_main("I'm not sure that I want the Slytherin team to improve, let alone because of me.","open","worriedL")
                m "Just think about how your helping your house in other ways."
                call her_main("I suppose your right [genie_name].","open","base")
                m "Of course I am, now did they pay you?"
                call her_main("Yes [genie_name].","base","base")
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                call her_main("Thank you [genie_name].","base","happyCl")
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >=9 and lock_public_favors == True:
                call her_main("[genie_name], something must be done about these Slytherin boys.","open","angryCl")
                call her_main("It's bad enough that I have to cheer for them but they are starting to become a little touchy.","annoyed","angryL")
                m "Touchy?"
                call her_main("Yes, they keep groping me. It's highly inappropriate and it interrupts my routine.","scream","angryCl")
                m "You keep dancing while they grope you?"
                call her_main("Of course, I'm there to complete a job. I won't fail at this just because of a few boys.","open","angryCl")
                m "Well what would you have me do?"
                call her_main("Speak to Professor Snape, tell him to chastise them. They'll listen to him.","angry","angry")
                m "Very well, I'll speak to him. I'm not sure it will have the effect your hoping for."
                call her_main("It better, otherwise I wont put my full effort into the routine.","normal","frown")
                m "{size=-5}I'm sure that'll show them.{/size}"
                call her_main("What was that [genie_name]?","open","suspicious")
                m "Nothing [hermione_name], I was just saying I'll speak to Professor Snape tonight."
                call her_main("Thank you [genie_name], here's your payment.","annoyed","angryL")
                ">You receive [payment] gold coins."
                $ gold += payment
                m "Well done [hermione_name], 30 points to Gryffindor."
                call her_main("Thank you [genie_name].","open","closed")
                $ gryffindor+= 30
            else:#Comes back with cum on her
                m "What the hell happened to you?"
                call her_main("I did my job [genie_name].","angry","down_raised")
                m "What are you talking about? You were supposed to be a cheerleader."
                call her_main("I am [genie_name]. I just performed a different type of cheer today.","soft","ahegao")
                m "And that cheer included jerking off the entire Slytherin team?"
                call her_main("Well that's not how it started. I was initially just giving them a bit of a dance in the locker room.","angry","down_raised")
                her "And one thing led to another..."
                m "Fine, I don't want to hear it. How much did they pay you for this \"cheering\"?"
                call her_main("Pay me?","silly","dead")
                m "You are supposed to be paid for this [hermione_name]."
                call her_main("Oh... I must have forgotten. Sorry [genie_name]","base","baseL",cheeks="blush")
                m "Fine, but you aren't getting any points."
                call her_main("Of course not [genie_name]. Will that be all?","base","base")
                m "Yes, you can go now."
                call her_main("Thank you [genie_name].","base","glance")
        "-Dismiss her-":
            call her_main("Here's your payment.","open","base")
            ">You receive [payment] gold coins."
            m "Well done [hermione_name], 30 points to Gryffindor."
            call her_main("Thank you [genie_name].","base","glance")
            $ gryffindor+= 30
            $ gold += payment

    call her_walk("mid","leave",2)
    
    $ hermione_sleeping = True
    $ current_job = 0
    $ uni_sperm = False 
    jump night_main_menu


label job_1:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    $ hermione_takes_classes = True
    if whoring <= 6:
        her "*Humph!*..."
    elif whoring >=7 and whoring <= 15:
        her "Yes [genie_name]..."
    else:
        her "As you wish [genie_name]."

    call her_walk("mid","leave",2)
    
    $ current_job = 1
    jump day_main_menu

label job_2:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    $ hermione_takes_classes = True
    if whoring <= 6:
        her "*Humph!*..."
    elif whoring >=7 and whoring <= 15:
        her "Yes [genie_name]..."
    else:
        her "As you wish [genie_name]."

    call her_walk("mid","leave",2)
    
    $ current_job = 2
    jump day_main_menu
    
label job_3:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    $ hermione_takes_classes = True
    if whoring <= 6:
        her "*Humph!*..."
    elif whoring >=7 and whoring <= 15:
        her "Yes [genie_name]..."
    else:
        her "As you wish [genie_name]."

    call her_walk("mid","leave",2)
    
    $ current_job = 3
    jump day_main_menu
    
label job_4:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    $ hermione_takes_classes = True
    if whoring <= 6:
        her "*Humph!*..."
    elif whoring >=7 and whoring <= 15:
        her "Yes [genie_name]..."
    else:
        her "As you wish [genie_name]."

    call her_walk("mid","leave",2)
    
    $ current_job = 4
    jump day_main_menu























        