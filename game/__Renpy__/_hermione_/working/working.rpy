init python:
    class hermione_job(object):
        inProgress = False
        responses = ""

        def checkProgress(self):
            if self.inProgress:
                renpy.jump(self.responses)


# Maid Job
label job_1:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    if her_whoring <= 6:
        her "*Humph!*..."
    elif her_whoring >=7 and her_whoring <= 15:
        her "Yes [genie_name]..."
    else:
        her "As you wish [genie_name]."

    show screen blkfade
    with d5
    call play_sound("equip_inventory")
    pause 2.5
    call h_equip_temp_outfit(hg_outfit_maid_ITEM)
    hide screen blkfade
    with d5

    call her_main("","base","base",xpos="right",ypos="base",trans="fade")
    pause.8

    m "Off you go then..."

    call her_walk(action="leave", speed=2)

    call h_unequip_temp_outfit()

    $ hermione_busy = True
    $ current_job = 1

    jump main_room

label maid_responses:
    $ payment = renpy.random.randint(10, 25)

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call h_equip_temp_outfit(hg_outfit_maid_ITEM)

    call her_main("","base","base",xpos="right",ypos="base")
    pause.5

    menu:
        "-Ask her how her day was-":
            if day_random <= 4:
                m "How was your day?"
                her "It was as normal a day of cleaning rooms could be."
                her "Although considering that I'm supposed to be in class during the day I guess it's not that normal."
                m "Don't worry [hermione_name], you'll get your points."
                m "Just think of how happy your friends will be when they win the house cup this year."
                her "I suppose..."
                m "10 points to Gryffindor"
            elif day_random <= 8:
                call her_main("Do I really have to keep doing this?","normal","glanceL")
                m "What do you mean, [hermione_name]?"
                call her_main("It's so degrading... I have to clean other students rooms!","open","down")
                m "You can stop anytime."
                call her_main("I can?","soft","concerned")
                g9 "Certainly, I'll just get one of those Slytherin floosies that you are always on about."
                m "I'm sure that they'd jump at the chance to make some points for their house."
                m "They'd probably even do it for next to nothing, if not free."
                call her_main("Fine, I get your point. It's just, surely there are other ways for you to earn money [genie_name]?","upset","closed")
                call her_main("I mean you're the school headmaster, can't you just file some reports and get paid by the ministry?","base","baseL")
                m "I can, it's just not as enjoyable."
                call her_main("Hmmph. Can I at least get my points now?","angry","angryCl")
                m "Certainly, 10 points to Gryffindor."
            else:
                call her_main("I think you need to start enforcing harsher punishment for sexual harassment.","mad","angry")
                call her_main("Hmmph... Can I at least get my points now?","angry","angryCl")
                m "Certainly, 10 points to Gryffindor."
        "-Dismiss her-":
            call her_main("Here's your payment.","base","base")
            ">You receive [payment] gold coins."
            m "Well done [hermione_name], 20 points to Gryffindor."

    call her_main("Thank you, [genie_name].","base","base")
    ">You receive [payment] gold coins."
    $ gryffindor+= 20
    $ gold += payment

    call her_walk(action="leave", speed=2)

    call h_unequip_temp_outfit()

    $ hermione_busy = True
    $ current_job = 0

    jump night_main_menu



# Barmaid Job
label job_2:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    if her_whoring <= 6:
        her "*Humph!*..."
    elif her_whoring >=7 and her_whoring <= 15:
        her "Yes [genie_name]..."
    else:
        her "As you wish [genie_name]."

    show screen blkfade
    with d5
    call play_sound("equip_inventory")
    pause 2.5
    call h_equip_temp_outfit(hg_outfit_maid_ITEM)
    hide screen blkfade
    with d5

    call her_main("","base","base",xpos="right",ypos="base",trans="fade")
    pause.8

    m "Off you go then..."

    call her_walk(action="leave", speed=2)

    call h_unequip_temp_outfit()

    $ hermione_busy = True
    $ current_job = 2

    jump main_room

label barmaid_responses:
    $ payment = renpy.random.randint(20, 50)

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    call h_equip_temp_outfit(hg_outfit_maid_ITEM)

    call her_main("","base","base",xpos="right",ypos="base")
    pause.5

    menu:
        "-Ask her how her day was-":
            her "Fine..."
            m "Anything unusual happen?"
            her "Not really, I just served people drinks."
            m "Well in that case 10 points to Gryffindor."
            her "Thank you, [genie_name], here's your payment."
        "-Dismiss her-":
            her "Here's your payment."
            ">You receive [payment] gold coins."
            m "Well done [hermione_name], 20 points to Gryffindor."

    her "Thank you, [genie_name]."
    ">You receive [payment] gold coins."
    $ gryffindor+= 20
    $ gold += payment

    call her_walk(action="leave", speed=2)

    call h_unequip_temp_outfit()

    $ hermione_busy = True
    $ current_job = 0
    jump night_main_menu



# Gryffindor Cheerleader Job
label job_3:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    if her_whoring <= 6:
        her "*Humph!*..."
    elif her_whoring <= 15:
        call her_main("Yes, [genie_name]...","normal","baseL")
    else:
        call her_main("As you wish, [genie_name].","open","base")

    show screen blkfade
    with d5
    call play_sound("equip_inventory")
    pause 2.5
    if hg_cheer_g_sexy_ITEM.unlocked and her_whoring >= 11: #Sexy
        call h_equip_temp_outfit(hg_cheer_g_sexy_ITEM)
    else: #Normal
        call h_equip_temp_outfit(hg_cheer_g_ITEM)
    hide screen blkfade
    with d5

    call her_main("","base","base",xpos="right",ypos="base",trans="fade")
    pause.8

    g9 "You look great!"
    call her_main("Thank you...","base","happyCl")
    m "Off you go then..."

    call her_walk(action="leave", speed=2)

    call h_unequip_temp_outfit()

    $ hermione_busy = True
    $ current_job = 3

    jump main_room

label gryffindor_cheer_responses:
    $ payment = renpy.random.randint(40, 80)

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    if hg_cheer_g_sexy_ITEM.unlocked and her_whoring >= 11: #Sexy
        call h_equip_temp_outfit(hg_cheer_g_sexy_ITEM)
    else: #Normal
        call h_equip_temp_outfit(hg_cheer_g_ITEM)

    call her_main("","base","base",xpos="right",ypos="base")
    pause.5

    menu:
        "-Ask her how her day was-":
            if day_random <= 2:
                m "Hello, [hermione_name], how was your day?"
                call her_main("It was good [genie_name], I think that the team morale has really started to go up.","base","base")
                m "How so?"
                call her_main("Well, since I've started they seem to have improved their tactics.","open","base")
                call her_main("They also seem much happier. Harry is always looking at me with a smile on his face.","base","base")
                m "And does he look at you a lot?"
                call her_main("Of course he does, we're good friends.","open","base")
                m "\"I'm sure that must be the reason...\""
                call her_main("Well here's the money, [genie_name].","base","base")
                ">You receive [payment] gold coins."
                m "Well done, [hermione_name], 20 points to Gryffindor."
            elif day_random >= 3 and day_random <= 5:
                m "Hello, [hermione_name], how was your day?"
                call her_main("Tiring. This cheering thing really is quite exhausting.","open","worried")
                m "Anything interesting happen?"
                call her_main("Not unless you count me almost dropping my pom pom.","normal","base")
                m "I don't... Well, did they pay you?"
                call her_main("Of course, here you are [genie_name].","open","base")
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
            elif day_random >= 6 and day_random <= 8:
                m "Welcome back [hermione_name]."
                call her_main("Hello [genie_name].","open","base")
                m "How did everything go today?"
                call her_main("Very well thank you, all the boys said that I helped keep their spirits up.","open","base")
                m "{size=-5}I'm sure that wasn't the only thing you've helped stay up...{/size}"
                call her_main("What was that [genie_name]?","open","suspicious")
                m "I was just saying that I'm sure you did a stand up job."
                call her_main("I think so...","base","happyCl")
                m "Well, did they pay you for raising their \"spirits\"?"
                call her_main("Of course they did.","open","base")
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
            elif day_random >=9 and her_reputation <= 15:
                m "You seem very chipper today."
                call her_main("Of course I am, we won!","base","base")
                m "Won?"
                call her_main("We won! We beat Slytherin in a practice match.","smile","happyCl")
                m "You seem a little bit over-excited for just a practice match."
                call her_main("Well it was such a great game. Not to mention that we got to rub it in those Slytherin students faces afterwards.","smile","baseL")
                g9 "Well I'm glad that you are enjoying your work."
                call her_main("I am [genie_name]. Given that most of the \"work\" I've done to help my house is kept private, it feels good to be able to do something public once.","open","base")
                m "Not to mention you get paid for it..."
                call her_main("Oh, right, Here you are...","soft","baseL")
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
            else:
                m "Welcome back [hermione_name], how was your day?"
                call her_main("We won! We managed to beat Slytherin.","base","base")
                m "That must have been very exhilarating. I'm sure your cheering gave the extra motivation needed to win."
                call her_main("I think it did [genie_name]. They were all very excited to receive their reward for winning the game.","base","happyCl")

                menu:
                    "-Reward?-":
                        m "What reward did you promise them?"
                        call her_main("Well I was quite keen to ensure our victory against Slytherin that I may have promised that I would give each of them a blowjob if they won.","grin","baseL")
                        m "You gave every team member a blowjob after the game?"
                        call her_main("And the water boy...","smile","glance")
                        m "How did you even manage that? Did have to crawl around the locker room on your knees?"
                        call her_main("Of course not, they all patiently waited on their turn...","scream","angryCl")
                        m "Who doesn't love a queue..."
                        m "So they queued up... And then?"
                        call her_main("Well I did what I said I would, I'm not the kind of person to lie am I?","annoyed","worriedL")
                        call her_main("So, I gave them the reward I promised... And surely you of all people would know how a blowjob works.","annoyed","squintL")
                        m "That's not quite what I meant."
                        m "You just look rather..."
                        m "Clean, that's all."
                        call her_main("Oh, well...","base","down",cheeks="blush")
                        call her_main("I didn't want to make a mess","soft","down_raised",cheeks="blush")
                        call her_main("Anyhow, I'm glad I did it. I can't wait to rub it in Astoria's face tomorrow...","smile","base")
                        m "I'm glad you think it was worth it. Did they pay you?"
                    "-Okay-":
                        m "I'm sure it was worth it. Did they pay you?"

                her "Of course they did [genie_name], here you are."
                m "Well done [hermione_name], 20 points to Gryffindor."

        "-Dismiss her-":
            call her_main("Here's your payment [genie_name].","soft","baseL")
            m "Well done [hermione_name], 20 points to Gryffindor."

    call her_main("Thank you, [genie_name].","base","happyCl")
    ">You receive [payment] gold coins."
    $ gryffindor+= 20
    $ gold += payment

    call her_walk(action="leave", speed=2)

    call h_unequip_temp_outfit()

    $ hermione_busy = True
    $ current_job = 0
    jump night_main_menu



# Slytherin Cheerleader Job
label job_4:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    if her_whoring <= 6:
        her "*Humph!*..."
    elif her_whoring >=7 and her_whoring <= 15:
        her "Yes, [genie_name]..."
    else:
        her "As you wish, [genie_name]."

    show screen blkfade
    with d5
    call play_sound("equip_inventory")
    pause 2.5
    if hg_cheer_s_sexy_ITEM.unlocked and her_whoring >= 11: #Sexy
        call h_equip_temp_outfit(hg_cheer_s_sexy_ITEM)
    else: #Normal
        call h_equip_temp_outfit(hg_cheer_s_ITEM)
    hide screen blkfade
    with d5


    call her_main("","base","base",xpos="right",ypos="base",trans="fade")
    pause.8

    g4 "You look incredible!"
    call her_main("Thank you...","base","happyCl")
    m "Off you go then..."

    call her_walk(action="leave", speed=2)

    call h_unequip_temp_outfit()

    $ hermione_busy = True
    $ current_job = 4

    jump main_room

label slytherin_cheer_responses:
    $ payment = renpy.random.randint(50, 100)

    call her_walk(action="enter", xpos="mid", ypos="base", speed=2)

    if hg_cheer_s_sexy_ITEM.unlocked and her_whoring >= 11: #Sexy
        call h_equip_temp_outfit(hg_cheer_s_sexy_ITEM)
    else: #Normal
        call h_equip_temp_outfit(hg_cheer_s_ITEM)

    if day_random >=9 and her_reputation > 15:
        $ uni_sperm = True
        call her_main("","base","ahegao_raised",xpos="right",ypos="base")
    else:
        call her_main("","base","base",xpos="right",ypos="base")
    pause.5

    menu:
        "-Ask her how her day was-":
            if day_random <= 2:
                m "How was your day today [hermione_name]?"
                call her_main("Exhausting... Those Slytherin pigs insisted that I cheer for their entire practice session.","open","angryCl")
                her "They were hardly playing the game by the end. They were just standing there watching me."
                m "Well what was your routine?"
                call her_main("Mostly star jumps while I cheered \"Go Slytherin!\".","annoyed","frown")
                m "So you were just jumping up and down? That doesn't seem like a very intricate cheer."
                call her_main("It isn't but it's what they insisted I do.","annoyed","angryL")
                m "Well it definitely sounds like you earned your points."
                m "30 points to Gryffindor."
            elif day_random >= 3 and day_random <= 5:
                m "How was your day today [hermione_name]?"
                call her_main("Uneventful. I completed my routine and then went back to my room...","open","suspicious")
                m "You didn't talk to anyone?"
                call her_main("I make a point of trying to avoid Slytherin student as best I can. ","annoyed","angryL")
                m "Are they really that unbearable?"
                call her_main("Yes...","open","angryCl")
                m "Well, you earned your points."
                m "30 points to Gryffindor."
            elif day_random >= 6 and day_random <= 8:
                m "Hello [hermione_name]."
                call her_main("Hello [genie_name].","normal","base")
                m "How did everything go today?"
                call her_main("Very well. In fact I think I might be doing too well.","annoyed","worriedL")
                m "How so?"
                call her_main("I think that my cheering is having too much of an positive effect.","open","worried")
                call her_main("I'm not sure that I want the Slytherin team to improve, let alone because of me...","open","worriedL")
                m "Just think about how you're helping your house in other ways."
                call her_main("I suppose you're right [genie_name].","open","base")
                m "Of course I am... Now, did they pay you?"
                call her_main("Yes [genie_name].","base","base")
                m "Well done [hermione_name], 20 points to Gryffindor."
            elif day_random >=9 and her_reputation > 15:
                call her_main("[genie_name], something must be done about those Slytherin boys...","open","angryCl")
                call her_main("It's bad enough that I have to cheer for them but they are being a little bit touchy.","annoyed","angryL")
                m "Touchy?"
                call her_main("Yes, they keep groping me. It's highly inappropriate and it interrupts my routine.","scream","angryCl")
                m "You kept dancing while they groped you?"
                call her_main("Of course, I'm there to complete a job. I'm not getting distracted just because of a few boys.","open","angryCl")
                m "Well what would you have me do?"
                call her_main("Speak to Professor Snape, tell him to chastise them. They'll listen to him...","angry","angry")
                m "Very well, I'll speak to him. Although I'm not sure it will have the effect you're hoping for."
                call her_main("It better, otherwise I wont put my full effort into this...","normal","frown")
                m "{size=-5}I'm sure that'll show them.{/size}"
                call her_main("What was that [genie_name]?","open","suspicious")
                m "Nothing [hermione_name], I'll speak to Professor Snape tonight..."
            else:#Comes back with cum on her
                m "What the hell happened to you?"
                call her_main("I did my job [genie_name].","angry","down_raised")
                m "What are you talking about? You were supposed to be a cheerleader."
                m "You know, cheering..."
                m "And all that."
                call her_main("I am [genie_name]. I just performed a different type of cheer today.","soft","ahegao")
                m "And by that you mean jerking off the entire Slytherin team?"
                call her_main("Well that's not how it started. I was initially just giving them a bit of a dance in the locker room...","angry","down_raised")
                her "And one thing led to another."
                m "Fine, I don't want to hear it. How much did they pay you for this \"cheering\"?"
                call her_main("Pay me?","silly","dead")
                m "You are supposed to be paid for this [hermione_name]."
                call her_main("Oh... I must have forgotten. Sorry [genie_name]","base","baseL",cheeks="blush")
                m "Fine, but you aren't getting any points."
                call her_main("Of course [genie_name]. Will that be all?","base","base")
                m "Yes, you're free to go now."
                call her_main("Thank you, [genie_name].","base","glance")
                jump end_her_working_no_payment
        "-Dismiss her-":
            call her_main("Here's your payment.","open","base")
            ">You receive [payment] gold coins."
            m "Well done [hermione_name], 30 points to Gryffindor."

    call her_main("Thank you, [genie_name].","base","glance")
    ">You receive [payment] gold coins."
    $ gryffindor+= 30
    $ gold += payment

    label end_her_working_no_payment:

    call her_walk(action="leave", speed=2)

    call h_unequip_temp_outfit()

    $ hermione_busy = True
    $ current_job = 0
    $ uni_sperm = False
    jump night_main_menu


#Send Hermione to work, promoting the card game.

label job_5:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    $random_choice = renpy.random.randint(0,3)
    if random_choice == 0:
        call her_main("Why are the cards placed like that?","mad","down")
        call her_main("...","normal","worriedCl", cheeks="blush")
        call her_main("Fine...","open","down_raised", cheeks="blush")
    elif random_choice == 1:
        call her_main("...","normal","worried", cheeks="blush")
        call her_main("Well, if it stops you from deducting those points.","open","worriedCl", cheeks="blush")
        call her_main("I'll do it.","base","wink")
    elif random_choice == 2:
        call her_main("It's a bit revealing... but I'll do it.","smile","happy", cheeks="blush")
        call her_main("For Gryffindor house obviously!","open","happyCl", cheeks="blush")
    else:
        call her_main("That doesn't leave a lot to the imagination...","smile","squint")
        call her_main("At least the straps should cover my nipples...","open","wink")
        call her_main("I'll do it...","normal","happy", cheeks="blush")

    if first_time_cardgame_work:
        $ first_time_cardgame_work = False
        call her_main("But... why do you want me to help them promote their shop?","annoyed","closed")
        g9 "That is my business."
        call her_main("What do you want me to tell them then?","open","concerned")
        m "Just ask them if they have a need for any help promoting their card game."
        g9 "If they're as business minded as I assume then there's no way they'd say no."
        g9 "And make sure you ask them for payment."
        call her_main("Fine...","base","closed")
        call her_main("I'll see you tonight.","open","base")
        m "Forgetting something?"
        call her_main("... Just hand it over.","disgust","down", cheeks="blush")

    show screen blkfade
    with d5
    call play_sound("equip_inventory")
    pause 2.5
    call h_equip_temp_outfit(hg_gamble_slut_ITEM)
    hide screen blkfade
    with d5
    g9 "Looking great!"
    call her_main("Thank you...","open","happy", cheeks="blush")
    m "Off you go then..."


    hide screen hermione_main
    call h_unequip_temp_outfit()
    $ hermione_busy = True
    $ current_job = 5

    jump main_room

label hermione_helping_selling_cards:
    $ current_job = 0
    $ random_choice = renpy.random.randint(1,4)

    call h_equip_temp_outfit(hg_gamble_slut_ITEM)

    if her_shop_help_first:
        $ her_shop_help_first = False
        call her_main("")
        m "Hello, [hermione_name], how was your day?"
        call her_main("Good...","normal","squint")
        call her_main("Still not that comfortable wearing the outfit you provided though so I just stood behind the shop counter today.","open","closed")
        call her_main("Apparently we sold a lot more items than usual though.","base","happy", cheeks="blush")
        g9 "Great news, I bet the twins are ecstatic."
        call her_main("Indeed, It was nice seeing them in such high spirits.","open","happyCl", cheeks="blush")
        call her_main("Whilst I might not agree with all their business methods I think they might become great salesmen some day.","base","squint")
        g9 "Seems to me like they are already..."
        m "So, how come you had such a surge in new customers?"
        call her_main("No idea, maybe the card game got more people interested in browsing the rest of their stock.","annoyed","squintL")
        call her_main("They actually had some problems with people stealing things before I started working there though.","open","closed")
        m "And this stopped after you started working there?"
        call her_main("Well, probably not because of it. They put in some anti thieving measures.","base","base")
        m "Patent pending?"
        call her_main("It's pretty clever actually, they put up a mirror behind the counter so that when I have to turn around and grab something I'll be able to see if anyone takes anything.","smile","wink")
        g9 "\"Yeah, I'm sure that's why they put the mirror there...\""
        m "Sounds like you're doing a great job."
        call her_main("Thanks!","open","happy", cheeks="blush")
        call her_main("Here's your payment.","open","base")
        call give_reward("You have received 20 gold", "interface/icons/gold.png")
        $ gold += 20
        m "Well done [hermione_name], 15 points to Gryffindor."
        $ gryffindor += 15
        call h_unequip_temp_outfit()
        jump night_main_menu

    if random_choice == 1:
        call her_main("")
        m "Hello, [hermione_name], how was your day?"
        call her_main("It was fine, the outfit is a bit chilly though.","normal","happy")
        m "So, no other complications?"
        call her_main("Well...","soft","down", cheeks="blush")
        call her_main("The twins asked me to give out some free promotional starter packs.","open","squint", cheeks="blush")
        m "Yes?"
        m "Sounds like a great way to get people into playing..."
        call her_main("Well, I didn't have anywhere to store the packs as you could imagine.","base","down", cheeks="blush")
        call her_main("So I had to resort to putting them behind my suspenders and the top of my stockings...","open","closed", cheeks="blush")
        call her_main("And one customer got a bit...","normal","closed", cheeks="blush")
        call her_main("Touchy.","base","ahegao", cheeks="blush")
        m "I see..."
        call her_main("I did get a bit agitated at one point actually...","open","closed", cheeks="blush")
        g4 "They didn't fire you did they?"
        call her_main("No!","mad","wide_stare")
        call her_main("The customer was quite apologetic actually and bought a bunch of things.","smile","angryCl")
        call her_main("The twins obviously took the credit for getting such a big sale and seemed rather pleased with themselves.","crooked_smile","annoyed")
        call her_main("I'm fine with them believing they had anything to do with it though.","smile","closed")
        m "How noble of you..."
        call her_main("Here's your payment.","open","base")
        call give_reward("You have received 20 gold", "interface/icons/gold.png")
        $ gold += 20
        m "Well done [hermione_name], 20 points to Gryffindor."
        $ gryffindor += 20
    elif random_choice == 2:
        call her_main("")
        m "Hello, [hermione_name], how was your day?"
        call her_main("Awful...","normal","down")
        m "Really, why is that?"
        call her_main("Well, I'm not actually angry...","open","base")
        call her_main("Just a bit annoyed, that's all.","annoyed","closed")
        m "With?"
        call her_main("Myself...","open","worriedL", cheeks="blush")
        call her_main("We've set up a practice day where you get to borrow a deck of cards to get more people into the game.","normal","squint")
        g9 "Sounds like a good idea, get people invested."
        call her_main("Well, that was fine and all until the amount of new people interested started to slow down.","open","down")
        m "I see, so I expect the responsibility fell on you as you're the one meant to promote the game?"
        call her_main("Yes... I thought it was a great idea so if it ended up not working out then it would look very bad on my part.","normal","closed")
        m "So, you had to stop the practice sessions?"
        call her_main("No, that's not why I'm annoyed...","annoyed","squintL")
        call her_main("In my haste to find a solution I thought it would be a great idea to play a few rounds of strip cards to get more people interested.","open","down_raised", cheeks="blush")
        call her_main("...","angry","angryCL", cheeks="blush")
        call her_main("I've played enough not to be beaten by a new player I thought.","mad","angryL", cheeks="blush")
        g9 "Of course, you've played against me after all..."
        call her_main("...","base","angry")
        m "Sorry, go on."
        call her_main("Well, I managed to get a bunch of people into the card game so practice day is still on the schedule.","annoyed","angryCl")
        g9 "That's good!"
        call her_main("Though I might reconsider the whole strip card idea...","angry","down", cheeks="blush")
        call her_main("I lost pretty quickly...","normal","closed", cheeks="blush")
        call her_main("It turned out they had been cheating the whole time...","normal","base", cheeks="blush")
        g9 "Well, cheaters never prosper..."
        call her_main("That's not true in this case... they prospered alright.","open","squintL", cheeks="blush")
        call her_main("In any case, they seemed... happy, they bought a bunch of things so that makes me...","normal","base")
        call her_main("Happy as well...","angry","closed", cheeks="blush")
        g9 "A job well done then, I bet the twins are very grateful for your contribution."
        call her_main("Thank you.","annoyed","happyCl", cheeks="blush")
        call her_main("Anyway...","base","base")
        call her_main("Here's your payment.","open","base")
        call give_reward("You have received 20 gold", "interface/icons/gold.png")
        $ gold += 20
        m "Well done [hermione_name], 25 points to Gryffindor."
        $ gryffindor += 25
    elif random_choice == 3:
        call her_main("")
        m "Hello, [hermione_name], how was your day?"
        call her_main("Great, they held a card game tournament today.","base","base")
        g4 "Wait, a tournament? How come I wasn't invited?"
        call her_main("It was students only obviously...","open","squintL")
        m "Oh... of course."
        call her_main("There were way more participants than I expected seeing that there was an entry fee.","base","closed", cheeks="blush")
        m "Must've been a great prize pool then..."
        call her_main("That's the weird thing. The prize pool only amounted do about half of the total entry fee amount.","open","base")
        call her_main("Apparently... someone had gone around spreading the rumour that the winner would...","normal","down")
        call her_main("Get a go with me if they won the tournament...","annoyed","down_raised", cheeks="blush")
        g9 "And did they?"
        call her_main("Of course that was never on the table...","base","angry", cheeks="blush")
        g9 "On a desk then?"
        call her_main("Well...","annoyed","base", cheeks="blush")
        call her_main("The winner did end up standing there with such an expectant look on his face after everyone had left...","open","down", cheeks="blush")
        m "..."
        call her_main("So I told him that whatever he was expecting it wasn't happening.","angry","angryL", cheeks="blush")
        call her_main("He seemed so disheartened so I felt a bit bad about the whole thing...","open","angryCl")
        call her_main("So, since I didn't want to bring his feeling of victory down I figured since some students had spread the rumour they'd assume the worst anyway...","open","angry", cheeks="blush")
        call her_main("So I put my hand down his pants and fiddled around a bit whilst letting the guy get a peek behind my suspenders.","grin","angry", cheeks="blush")
        g9 "Good on you!"
        call her_main("You don't think that was a bit much?","annoyed","base", cheeks="blush")
        g9 "No! That was the right thing to do in that situation."
        m "There wasn't a lot you could do about the rumours even if nothing had happened he'd probably lie about it anyway."
        g9 "You most likely ended up making that guys night."
        call her_main("More like month... seeing how much he...","open","down", cheeks="blush")
        call her_main("Anyway...","normal","base")
        call her_main("glad you agree.","base","happy")
        call her_main("Here's your payment.","open","base")
        call give_reward("You have received 20 gold", "interface/icons/gold.png")
        $ gold += 20
        m "Well done [hermione_name], 25 points to Gryffindor."
        $ gryffindor += 25
    else:
        $ uni_sperm = True
        call her_main("","cum","dead")
        m "What happened to you?"
        call her_main("What do you mean...","open","concerned")
        call her_main("Oh, that...","base","down", cheeks="blush")
        m "Yes, that..."
        call her_main("There's a good explanation for this.","normal","down_raised", cheeks="blush")
        m "..."
        m "Go on."
        call her_main("Oh, sorry... Well, I was trying out a new sales tactic...","open","squintL", cheeks="blush")
        m "Something the twins came up with I assume?"
        call her_main("No, I read about it in one of their books actually.","grin","happy")
        call her_main("Much like how you should always put the most lucrative cheap items at the counter to make the customer....","open","base")
        g4 "Get on with it."
        call her_main("Fine...","annoyed","glanceL", cheeks="blush")
        call her_main("I read that by putting the customer in a state of peace and happiness it would make them more susceptible to making hasty decisions.","smile","happyCl", cheeks="blush")
        g9 "Didn't think you'd be interested in such... unorthodox sales tactics..."
        call her_main("I was curious to see if it would work more than anything else.","base","closed", cheeks="blush")
        call her_main("I tried it out to test the legitimacy of the claims in that book of theirs...","open","base")
        m "of course..."
        m "And how many times did you test this... theory of yours."
        call her_main("There's no conclusion to be made by just testing a theory once [genie_name].","normal","angryCl")
        call her_main("Anyway...","open","base")
        call her_main("Here's your payment.","open","base")
        call give_reward("You have received 20 gold", "interface/icons/gold.png")
        $ gold += 20
        m "Well done [hermione_name], 30 points to Gryffindor."
        $ gryffindor += 30

    call h_unequip_temp_outfit()
    jump night_main_menu

label inn_menu:

    if inn_intro:
        jump inn_intro
    abe "Welcome to the Hog's Head Inn"
    menu:
        "-Present Hermione to Aberforth-":
            m "I present you you're new barmaid."
            $ hermione_wear_robe = True
            call set_hermione_outfit(hg_outfit_maid_OBJ)
            call her_main("","normal","frown")
            call ctc

            abe "Well go on then girl, take the robe off."
            her "Fine..."

            hide screen hermione_main
            $ hermione_wear_robe = False
            call her_main("","normal","worriedCl")
            pause

            hide screen hermione_main
            jump inn_menu
        "-Talk to Aberforth-":
            jump inn_talk
        "-Play Dice with Aberforth-":
            "Not added yet (will be soon)."
            jump inn_menu
        "-Leave-":
            jump return_office


label inn_intro:
    m "Hello."
    abe "Hello Professor..."
    ">There is a sour tone in the mans voice."
    m "So what do you sell here?"
    abe "What do you want Albus?"
    m "(Albus? He must know the Professor.)"
    m "Just a drink."
    abe "You, drinking? I never thought that I'd see the day."
    m "Why's that?"
    abe "I never expected my little brother to lift his head out of the books long enough to come have a drink."
    m "(Brother?)"
    m "Well there's a first time for everything."
    abe "Hmmmph. Well we'll start you with a Butterbeer then. Anything stronger and you'll probably pass out."
    ">Aberforth pours you a large stein of a golden, frothy beer."
    ">You take a sip. It has a sweet almost sugary taste and a creamy consistency."
    m "That's not half bad, so how much do I owe you?"
    abe "Just tell me who you are."
    m "(Shit)"
    m "What do you mean."
    abe "I've never seen my brother drink Butterbeer in his life. Either you're not Albus or I'm a bowtruckle."
    m "Fine, you got me, I'm not Albus."
    abe "Then what are you doing in his skin?"
    m "I'm an all powerful genie from a magical world that accidentally made a potion that swapped the minds of me and your brother."
    abe "...."
    abe "That sounds convoluted."
    m "You're telling me."
    abe "So how long will it last?"
    m "No idea."
    abe "Well as far as I'm concerned this is nothing but an improvement."
    m "You don't like your brother that much?"
    abe "It's a long story."
    abe "Now how about a proper drink instead of that buttery crap."
    m "Sure."
    ">You drink well into the night, eventually staggering back to the castle"
    $ inn_intro = False
    jump day_start

label inn_talk: #Responses to Genie asking Aberforth how he's doing
if day_random <= 2:
    "bla bla bla"
    jump inn_menu
elif day_random >= 3 and day_random <= 5:
    "bla bla bla"
    jump inn_menu
elif day_random >= 6 and day_random <= 8:
    "bla bla bla"
    jump inn_menu
elif day_random >=9:
    "bla bla bla"
    jump inn_menu
