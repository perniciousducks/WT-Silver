
label cho_quidd_intro: #have cho come in and talk about wanting help to win more quidditch games against slytherin and gryffindor
    #genie suggest for her to play dirty
    $ cho_quidd = True
    $ cho_busy = True

    call update_cho_quidditch_outfit
    call cho_outfit(cc_outfit_quidditch_OBJ)

    call play_sound("door")
    call cho_main("","annoyed","angry","angry","R",xpos="close",ypos="base")
    pause.1
    call play_sound("bump")
    pause.5
    call cho_main("","annoyed","angry","angry","mid",xpos="mid",ypos="base",trans="fade")
    pause.3
    call cho_main("[cho_genie_name]! It's not fair!","scream","angry","sad","mid",trans="hpunch")
    call cho_main("Malfoy's pompous old man just bought the whole \'Slytherin\'' team brand new Nimbus 2018s!","scream","closed","angry","mid")
    call cho_main("\'Ravenclaw\'' can't be expected to win against that!","angry","angry","angry","downR")
    call cho_main("I demand you level the playing field, [cho_genie_name]!","scream","angry","angry","mid")
    m "Why? Is that crooked as well?"
    call cho_main("This isn't funny, [cho_genie_name]! With \'Slytherin\' playing dirty there's no way we can win!","open","angry","sad","R")
    call cho_main("Ugh! I knew you wouldn't do anything...","annoyed","angry","angry","mid")
    m "So you don't want to hear my solution then?"
    call cho_main("Wait... You are going to help?!","smile","shocked","sad","mid")
    call cho_main("Thank you, thank you, thank you!","smile","closed","base","mid")
    call cho_main("I take a small size broom and I'd like gold trim with a dark-","open","base","base","R")
    m "I'm not buying you a broom..."
    m "(Is quidditch like curling then?)"
    call cho_main("Oh...","annoyed","shocked","sad","downR")
    call cho_main("Then what's your solution?","open","suspicious","angry","mid")
    m "You said that the \'Slytherin\'s were playing dirty..."
    m "How about you fight fire with fire then?"
    call cho_main("So you think we should fight dirty too?","horny","suspicious","base","mid")
    call cho_main("But how? The rules forbid almost all foul play.","pout","angry","sad","downR")
    m "Hmmmm..."
    m "What do they say about uniform?"
    call cho_main("Ugh... I don't think there's anything about the uniform in the rule book, [cho_genie_name].","open","base","base","R")
    m "So if you intended to wear a skirt while you played-"
    call cho_main("I couldn't do that!","scream","wide","angry","mid")
    call cho_main("Everyone would be able to see straight up it!","quiver","wide","angry","downR")
    call cho_main("Not to mention all the other player-","horny","suspicious","sad","R")
    call cho_main("Oh...","pout","suspicious","angry","mid")
    call cho_main("So that's your plan then? For me to distract \'Slytherin\' with some upskirt?","pout","angry","angry","mid")
    m "If you don't think it would work-"
    call cho_main("Of course it would work! Those \'Slytherin\'s are all a bunch of perverts...","open","suspicious","angry","R")
    call cho_main("But I can't go and play a game with a skirt on!","horny","shocked","sad","down")
    call cho_main("All my friends would see!","annoyed","shocked","sad","mid")
    m "They'll forget all about it after you defeat \'Slytherin\'!"
    call cho_main("I really don't think they will...","upset","suspicious","sad","downR")
    m "Then just tell them it was the only way to win. I'm sure they'll understand."
    call cho_main("You... might be right...","open","base","sad","downR")
    call cho_main("But still... I can't do that... can I?","quiver","shocked","sad","mid")
    m "Miss Granger would..."
    call cho_main("{size=-5}She would?{/size}","horny","shocked","sad","R")
    call cho_main("Alright! I'll do it!","smile","base","base","mid")
    call cho_main("Go Go \'Raveclaw\'!","scream","closed","sad","mid")
    m "So when's your next game?"
    call cho_main("I'm actually about to head over for a practice game against \'hufflepuff\'...","open","base","base","mid")
    m "Sounds like the perfect time to test out your new uniform..."
    call cho_main("Already?","open","shocked","sad","mid")
    call cho_main("Can't we wait a bit longer, [cho_genie_name]...","annoyed","base","sad","downR")
    m "Hmmm... if you don't feel up for it, Miss Granger could prob-"
    call cho_main("Fine...","annoyed","suspicious","angry","mid")
    m "Fantastic! Just come back here after the game to tell me how it went!"
    call cho_main("What? Can't I just run back to my dorm?","pout","shocked","sad","R")
    m "Not unless you want the rules to change again..."
    call cho_main("Ugh... Whatever old man...","quiver","suspicious","angry","mid")
    call nar(">With that Cho turns to leave your office.")
    call play_sound("door")
    hide screen cho_chang
    with d3
    pause.5

    m "..."
    m "(I still have no idea what quidditch is...)"

    jump end_cho_event




label cho_quidd_1_1: #come back and describe playing with a skirt on (embarrassed)
    $ cho_quidd_points = 1
    $ cho_busy = True

    call update_cho_quidditch_outfit
    call cho_outfit(cc_outfit_quidditch_OBJ)

    call play_sound("knocking")
    ">*knock* *knock* *knock*"

    menu:
        "\"Come in!\"":
            cho "Yes, [cho_genie_name]..."
        "\"Who is it?\"":
            cho "Cho Chang, [cho_genie_name]."
            m "Ah miss Chong... Come on in!"
            cho "..."

    call play_sound("door")
    call cho_main("...","annoyed","suspicious","angry","R",xpos="mid",ypos="base")
    m "You seem a little on edge today..."
    call cho_main("On edge?","scream","shocked","angry","mid")
    call cho_main("Of course I'm on edge! I've never felt so humiliated in my life!","angry","wide","angry","mid")
    call cho_main("You had to have me do this on the day half of \"hufflepuff\" shows up to watch the practice didn't you!","pout","suspicious","angry","R")
    call cho_main("I bet you were probably in on it...","upset","suspicious","angry","mid")
    m "Now now, you know I'd never resort to any sort of foul play like that..."
    m "More importantly, how did the game go?"
    m "Score many... points?"
    m "(I hope this stupid game has points...)"
    call cho_main("As a matter of fact I did!","open","closed","base","mid")
    call cho_main("{size=+10}150 of them!!!{/size}","scream","base","base","mid")
    m "Wow... That seems like a lot!"
    call cho_main("Of course it is, I caught the snitch!","smile","closed","base","mid")
    m "(The snitch? Is this prison rules?)"
    call cho_main("Today, I was racing after the snitch along with that blockhead Cedric Diggory...","open","base","sad","R")
    call cho_main("I'm normally never fast enough to beat him with my crummy old nimbus 2010...","pout","angry","angry","downR")
    call cho_main("But today I just flew above him as we were both after the snitch!","smile","base","base","mid")
    call cho_main("Ah!!! I can't believe I was able to finally catch it!","smile","closed","base","mid")
    m "Is this the first time you've caught the... snitch?"
    call cho_main("Of course! This is the first game of quidditch \"Ravenclaw\" has won in over six years!","smile","base","base","mid")
    m "Wasn't this just a practice game?"
    call cho_main("I was including the practices, [cho_genie_name]...","annoyed","suspicious","sad","downR")
    m "oh..."
    call cho_main("\"Ravenclaw\"... isn't very good...","pout","suspicious","sad","down")
    call cho_main("But I have a feeling that's going to change this year!","smile","closed","base","mid")
    call cho_main("We're a boot in to win the quidditch school cup!","smile","base","angry","mid")
    m "Wizarding School Cup?"
    call cho_main("Stop being an idiot, Dumbledore!","smile","suspicious","angry","R")
    call cho_main("You know what the \"Q.S.C.\" is! You've only hosted it for the last 30 years!","open","suspicious","base","mid")
    m "O-of course..."
    call cho_main("Speaking of which you better start getting prepared, it starts in under a month.","open","closed","base","mid")
    m "I'd be more worried about your team..."
    m "I don't think everyone is going to go down as easily as Cedric Digidy."
    m "Speaking of... What happened to him?"
    call cho_main("Oh... he um... crashed... into some... banisters...","quiver","suspicious","sad","downR")
    m "(Crashed? Is this game a racetrack now?)"
    call cho_main("The nurses said he'll be able to walk again by the end of the week!","horny","base","base","R")
    call cho_main("{size=-1}They're {size=-1}not {size=-1}so {size=-1}sure {size=-1}whether {size=-1}or {size=-1}not {size=-1}he'll {size=-1}wake {size=-1}up {size=-1}though...{/size}","smile","suspicious","sad","R")
    m "Anyway, my point is I don't think you'll be able to get away with just a skirt from now on."
    call cho_main("I don't?","pout","shocked","sad","mid")
    m "If you want to have any chance of winning this years cup I think you'll need me as a coach."
    call cho_main("Coach?","quiver","suspicious","base","mid")
    call cho_main("Are you sure you're able to do this, [cho_genie_name]?","pout","suspicious","sad","mid")
    m "Look, I gave you one bit of advice and you won your first game in six years."
    m "Imagine what having me coach you for a season could do!"
    call cho_main("OK...","horny","suspicious","base","R")
    call cho_main("But if you want me to keep doing these sorts of things...","open","base","angry","mid")
    call cho_main("I want some points!","smile","base","base","R")
    m "Ugh... really?"
    m "(I was hoping she'd forgotten about that...)"
    call cho_main("Yep! If you expect me to come back here and tell you how I've humiliated myself, then \"Ravenclaw\" should at least reap the benefits.","smile","closed","base","mid")
    m "Fine..."
    m "How many do you want then?"
    call cho_main("How much would Hermione do this for?","pout","suspicious","base","mid")

    menu:
        "-20 points-":
            call cho_main("Pffft, she really is a slut...","smile","shocked","base","mid")
            call cho_main("I want 100!","open","base","base","mid")
            m "I don't think so..."
            call cho_main("75!","smile","suspicious","angry","mid")
            m "25."
            call cho_main("70!","quiver","suspicious","angry","mid")
            m "30."
            call cho_main("60!","open","suspicious","angry","mid")
            m "40, final offer."
            call cho_main("(...)","annoyed","angry","angry","R")
            call cho_main("Ok, 40...","soft","angry","angry","mid")
            $ current_payout = 40
        "-40 points-":
            call cho_main("(...)","annoyed","angry","angry","R")
            call cho_main("Ok, [cho_genie_name]. I will do it for 40...","horny","base","base","mid")
            g9 "Great!"
            $ current_payout = 40
        "-100 points-":
            call cho_main("100? Really?","open","shocked","sad","mid")
            call cho_main("Done!","smile","closed","base","mid")
            m "Wait, would you have done it for less?"
            call cho_main("Too late!","smile","base","base","mid")
            m "(I'm too generous with those points...)"
            m "Just this once, [cho_name]."
            m "You'll only get 40 next time."
            call cho_main("But you said 100!","angry","base","raised","mid")
            m "Which is a very generous sum for such an easy task. You should thank me..."
            call cho_main("(...)","annoyed","angry","angry","mid")
            $ current_payout = 100

    m "[current_payout] points to \"Gryff-I mean \"Ravenclaw\"!"
    $ ravenclaw += current_payout
    call cho_main("Thank you, [cho_genie_name].","smile","closed","base","mid")
    m "So are you ready for my next bit of coaching advice?"
    call cho_main("Already? Can't I just keep wearing the skirt for now?","open","shocked","sad","R")
    m "And keep using the same old tactics?"
    m "What sort of coach do you take me for?"
    call cho_main("Well what did you have in mind?","pout","suspicious","base","mid")
    m "Seeing as how the skirt was such a success, how about we up the ante then?"
    call cho_main("How do you mean?","open","suspicious","raised","mid")
    m "Well that skirt seems a little long to me..."
    m "if you took a few inches off of it the other players probably wouldn't be able to keep their eyes off of you."
    call cho_main("They already can't keep their eyes off of me...","smile","closed","base","mid")
    m "For now... They'll probably get bored of that skirt after a while..."
    call cho_main("They will not!","scream","shocked","angry","mid")
    m "Are you going to let me coach you or not?"
    call cho_main("...","pout","suspicious","angry","R")
    call cho_main("How much shorter?","horny","suspicious","sad","mid")
    m "Just a few inches..."
    call cho_main("Alright... I'll get madmam mafkin to make some adjustments...","base","suspicious","sad","down")
    m "Very good. Now when is your next game?"
    call cho_main("In two days. Another practice match, this time against \"Gryffindor\".","open","base","sad","R")
    m "Do you think they'll be distracted by your new skirt?"
    call cho_main("Ha ha ha... if Those \"Gryffindor\" boys lose it over Hermione, just imagine what they do when they see me!","smile","suspicious","base","mid")
    m "I'm sure you'll win then..."
    call cho_main("So am I. And I'm sure you'll be happy to reward me with a hefty amount of points after the game...","smile","suspicious","angry","mid")
    m "I look forward to it..."
    call nar(">With that, cho turns and leaves to leave your office.")
    call play_sound("door")
    hide screen cho_chang
    with d3
    pause.5

    m "(I've really gotta learn what this game is about...)"

    jump end_cho_event



label cho_quidd_1_2: #come back and describe playing with a shorter skirt on (happy they won)
    $ cho_quidd_points = 2
    $ cho_busy = True

    call update_cho_quidditch_outfit
    call cho_outfit(cc_outfit_quidditch_OBJ)

    call play_sound("knocking")
    ">*knock* *knock* *knock*"

    m "Come in..."
    call play_sound("door")
    call cho_main("...","base","closed","base","mid",xpos="mid",ypos="base")
    m "How did your game go?"
    call cho_main("We won again!","scream","shocked","base","mid",trans="hpunch")
    call cho_main("I can't believe that we've broken our 6 year dry streak with two back-to-back wins!","smile","base","base","mid")
    call cho_main("We could actually win the cup!","open","shocked","angry","L")
    m "And you weren't embarrassed?"
    call cho_main("I was a little at the start of the game...","quiver","suspicious","sad","downR")
    call cho_main("But once I realized how much it was affecting those slack-jawed \"gryffindor\"s...","smile","angry","angry","R")
    call cho_main("It was like having my own personal weapon of mass distraction!","smile","shocked","angry","mid")
    call cho_main("I don't think Harry even knew where the snitch was most of the time!","horny","base","base","downR")
    call cho_main("All he seemed to do was follow me around...","horny","suspicious","sad","down")
    call cho_main("{size=-2}Him {size=-2}and {size=-2}half {size=-2}the {size=-2}team...{/size}","quiver","suspicious","sad","downR")
    m "So you're prepared to continue our coaching?"
    call cho_main("As long as we keep winning games, I think it's only reasonable...","open","closed","base","mid")
    call cho_main("Speaking of which... did you have any more coaching tips?","smile","wink","raised","mid")
    m "As a matter of fact I do..."
    call cho_main("Good... You can tell me all about them after you pay me my points!","smile","base","angry","mid")
    m "How does fifty sound?"
    call cho_main("Pfft... Only fifty when my skirt is this short?","pout","angry","raised","R")
    call cho_main("I want at least sixty...","smile","angry","angry","mid")
    m "Ugh fine..."
    call cho_main("(yes!)","smile","closed","base","mid")
    m "60 points to \"Ravenclaw\"!"
    $ ravenclaw += 60
    call cho_main("Thank you, [cho_genie_name].","base","closed","base","mid")
    call cho_main("Now about that tip...","smile","suspicious","base","mid")
    m "I've got a tip for you alright... and a bit more-"
    call cho_main("Professor!","open","shocked","angry","mid")
    m "alright, alright... for now, why don't you try shortening that skirt of your again."
    call cho_main("Again? Isn't this short enough?","pout","wink","sad","mid")
    m "Not if you want to win the grand prix or whatever..."
    call cho_main("The quidditch school cup, [cho_genie_name]...","pout","suspicious","base","mid")
    m "Sure..."
    call cho_main("Well I suppose I could take another inch or two off...","quiver","suspicious","sad","downR")
    call cho_main("But we better win the next practice against \"Slytherin\"!","scream","suspicious","angry","mid")
    m "Hey, the games up to you... All I can give is pointers."
    call cho_main("Hmph... That's not what a coach is supposed to say!","pout","suspicious","angry","mid")
    call cho_main("You're supposed to believe in me!","open","closed","angry","mid")
    m "You've gotta show some commitment to the game first."
    call cho_main("commitment...","angry","shocked","angry","mid")
    call cho_main("Isn't wearing a skirt enough?","pout","suspicious","angry","R")
    m "For now..."
    call cho_main("What's that supposed to mean?","upset","suspicious","angry","mid")
    m "It means stop being such a prude and shorten that skirt!"
    call cho_main("...","pout","base","sad","R")
    call cho_main("fine...","annoyed","suspicious","sad","down")
    $ cho_genie_name = "Coach"

    call cho_main("Is that all then, [cho_genie_name]?","soft","base","base","L")
    m "Unless you wanna fool around a little?"
    call cho_main("Not after a game...","quiver","suspicious","base","R")
    m "Then that will be all. "
    call cho_main("Alright then, [cho_genie_name]...","open","closed","base","mid")
    call nar(">With that Cho, turns and leaves your office.")

    jump end_cho_event



label cho_quidd_1_3: #come back and describe playing without a skirt on (aroused)
    $ cho_quidd_points = 3
    $ cho_busy = True

    call update_cho_quidditch_outfit
    call cho_outfit(cc_outfit_quidditch_OBJ)

    call play_sound("knocking")
    ">*knock* *knock* *knock*"

    m "You can just come in from now on Cho..."
    cho "Ok, [cho_genie_name]."
    pause.5

    call play_sound("door")
    call cho_main("But [cho_genie_name], what if you're in here with that floozy Hermione?","pout","suspicious","angry","mid",xpos="mid",ypos="base")
    call cho_main("I don't want to have to see that!","upset","suspicious","angry","R")
    m "Fair enough..."
    m "Now did you manage to win todays game?"
    call cho_main("...","pout","suspicious","sad","downR")
    call cho_main("No...","open","suspicious","sad","down")
    m "You didn't? Why not?"
    m "Wasn't your skirt distracting enough?"
    call cho_main("It wasn't that...","pout","suspicious","sad","downR")
    call cho_main("If anything went wrong it's that my skirt was too distracting!","annoyed","angry","angry","R")
    m "How's that? Don't you want the other players distracted?"
    call cho_main("I do...","quiver","suspicious","sad","R")
    call cho_main("But this was too much!","scream","closed","angry","mid")
    call cho_main("I couldn't get them off of me!","open","angry","angry","R")
    call cho_main("Half the \"slytherin\" team spent the whole game following me around, trying to get a peak from underneath!","scream","angry","angry","mid")
    m "Hmmm, I was worried this might happen...."
    call cho_main("Well how are you going to fix it then, [cho_genie_name]?","pout","suspicious","angry","mid")
    m "I think we'll need to change our angle of attack..."
    call cho_main("Our angle?","annoyed","wink","raised","mid")
    m "At the moment panty shot that all the boys are hoping for can only be seen from underneath-"
    m "-so as a result, most of the boys are hounding you to get a look."
    m "But if we widen our angle of attack, they won't be forced to chase you to get a look..."
    call cho_main("Widen our angle? What do you mean?","pout","wink","raised","mid")
    m "You're gonna have to loose the jacket..."
    m "Probably the sweater as well if we're being honest..."
    call cho_main("You want me to take my jacket off?","upset","shocked","angry","mid")
    call cho_main("I'll freeze!","scream","wide","angry","mid")
    call cho_main("Not to mention the other players and the spectators will be able to see everything!","horny","angry","sad","R")
    call cho_main("My skirt was at least a little hidden before...","pout","suspicious","angry","R")
    m "If you want to win this is the only way..."
    call cho_main("Can't I just go back to the longer skirt? That was working!","open","shocked","sad","mid")
    m "I don't think these \"slytherin\" boys are going to be interested in that after what they saw today..."
    m "I know I wouldn't..."
    call cho_main("[cho_genie_name]!","scream","angry","angry","mid")
    m "Just trust me... If you lose the next game you can put it back on..."
    call cho_main("OK... but I want some points!","pout","suspicious","sad","mid")
    call cho_main("Seventy five to be precise...","smile","closed","base","mid")
    m "...fine..."
    call cho_main("(awesome!)","smile","wink","base","R")
    m "75 points to \"Ravenclaw\"!"
    $ ravenclaw += 75
    call cho_main("Alright... well I'll come and see you after the next game...","open","suspicious","sad","mid")
    call cho_main("When I'm not wearing a jacket...","open","suspicious","sad","R")
    m "And wearing a mini-skirt..."
    call cho_main("And wearing... a mini-skirt...","pout","suspicious","sad","downR")
    m "Good. With tactics like this we can't lose."
    call cho_main("We better not!","upset","suspicious","angry","mid")
    call cho_main("This might be the first real chance \"Ravenclaw\" has ever had to win the cup.","open","closed","sad","mid")
    m "I'm sure this must mean a lot to you..."
    call cho_main("It does... I might even get picked up by a pro team!","smile","base","base","R")
    m "..."
    call cho_main("Agh, I can't wait!","scream","closed","base","mid")
    call cho_main("I better go talk to the team!","open","base","base","R")
    m "Well, off you go then."
    call cho_main("Thank you Professor...","smile","wink","base","mid")
    hide screen cho_chang
    with d3
    call nar(">Cho cheerily leaves your office.")

    jump end_cho_event


label cho_quidd_2_1: #Comes back after playing without a robe on
    $ cho_quidd_points = 4
    $ cho_busy = True

    call update_cho_quidditch_outfit
    call cho_outfit(cc_outfit_quidditch_OBJ)

    call play_sound("door")
    call cho_main("There's been a disaster!","scream","closed","angry","mid",xpos="mid",ypos="base")
    m "What? Did something happen during your game?"
    call cho_main("The game is {b}tomorrow{/b} sir...","open","angry","angry","mid")
    call cho_main("I'm talking about what happened to Lee Jordan, our commentator!","quiver","angry","angry","R")
    m "You have a commentator for practice games?"
    call cho_main("The commentators need to practice too!","open","angry","raised","mid")
    m "So what happened to him?"
    call cho_main("he was hit in the throat by a bludger during yesterdays game between gryffindor and slytherin.","quiver","base","raised","down")
    m "Ouch..."
    call cho_main("Madam Pomfrey says he'll be able to talk in a few days, but yelling is out of the picture for the rest of the season.","soft","closed","sad","mid")
    call cho_main("What are we going to do! We can't have a \"W.S.C.\" without a commentator!","soft","base","sad","mid")
    m "Well I do know someone..."

    label who_shall_commentate:
    menu:
        ">Chose somebody to commentate Cho's quidditch match."
        "-Hermione-":
            call cho_main("Hermione Granger?","scream","shocked","raised","mid")
            pass
        "-Astoria-" if astoria_unlocked:
            call cho_main("That brat?","scream","shocked","raised","mid")
            call cho_main("Not a chance!","open","closed","angry","mid")
            call cho_main("Besides, [cho_genie_name], did you forget that she's a slytherin?","open","angry","angry","mid")
            m "Right. No slytherins. Got it."
            m "How about..."
            jump who_shall_commentate
        "-Luna-" if luna_unlocked:
            call cho_main("Luna? Luna Lovegood, [cho_genie_name]?","open","suspicious","raised","mid")
            call cho_main("Knowing her she'd probably commentate the grass as it's growing...","open","closed","raised","mid")
            call cho_main("Trust me, [cho_genie_name], Luna would be a terrible choice!","soft","angry","angry","mid")
            m "Fine. How about..."
            jump who_shall_commentate

    call cho_main("She wouldn't know the first thing about quidditch!","open","angry","angry","mid")
    call cho_main("You can't pick her!","upset","closed","raised","mid")
    m "Now, now... Don't underestimate Miss Granger..."
    m "Why don't we just ask her first?"
    call cho_main("What? N-","scream","shocked","base","mid")
    call nar(">Before Cho has a chance to protest, you magically summon hermione up to your office...")
    call cho_main("","upset","angry","angry","R")
    pause.5

    #Hermione shouldn't be naked while sbd. else is presemt.
    $ hermione_wear_top = True
    $ hermione_wear_bottom = True
    $ hermione_wear_bra = True

    call play_sound("door")
    call her_main("You wanted to see me, sir?","base","base",xpos="base",ypos="base")
    call her_main("Oh... Hello cho...","soft","baseL")
    call cho_main("Granger...","pout","angry","angry","L")
    call her_main("So what is it you two need, Sir?","soft","base")
    call cho_main("Do you mind settling an argument for us by telling this oaf you don't know anything about quidditch...","open","closed","angry","mid")
    call her_main("What?","scream","wide",trans="hpunch")
    hide screen hermione_main
    with d3
    call her_main("Sir, I know {b}EVERYTHING{/b} about quidditch!","open","angry",xpos="close",ypos="base") #Don't use {\b}, it's {/b}.
    call cho_main("...","pout","angry","angry","L")
    call her_main("Do you really think that I, Hermione Granger, would be lacking in a subject so basic as quidditch?","open","closed")
    call her_main("Not to mention I've been dragged along to every single one of Harry and Ron's games...","open","angry")
    m "So you'd know enough to commentate then?"
    call her_main("Wait... Sir, you want me to commentate this years wizarding school cup?","open","wide_stare")
    call cho_main("That's not what-","pout","angry","angry","R")
    call her_main("I'd be honoured, sir!","scream","closed",trans="hpunch")
    call her_main("Quidditch has always been one of my passions, to be able to commentate it...","open","angry")
    call her_main("Not to mention getting to make all the announcements...","smile","baseL")
    call her_main("The speeches...","grin","squint")
    call her_main("the paper...","soft","ahegao")
    call her_main("The {image=textheart}{i}preparation{/i}{image=textheart}...","open_tongue","ahegao_raised")
    call her_main("I accept!","scream","angryCl",trans="hpunch")
    m "Congratulations miss granger! you can start tomorrow..."
    call her_main("Yay!","smile","happy")
    call cho_main("What? But I'll be...","open","base","sad","mid")
    call her_main("Oh, Will you be playing tomorrow, cho?","open","wide")
    call her_main("I can't wait! I'll make sure that I keep an eye on you!","grin","angry")
    call cho_main("Please don't...","quiver","base","sad","down")
    call her_main("Ah!!! I better start preparing my opening announcements in front of the mirror!!!","open","wide_stare",trans="hpunch")

    call play_sound("door")
    hide screen hermione_main
    with d3
    pause.8

    call cho_main("Argh! You're the worst coach ever!","scream","angry","angry","mid",trans="hpunch")

    call play_sound("door")
    hide screen cho_chang
    with d3
    pause.5

    m "Maybe it's about time I go see one of these games..."

    jump end_cho_event


label cho_quidd_2_2: #Comes back after playing with the robe still on
    $ cho_quidd_points = 5
    $ cho_busy = True

    call update_cho_quidditch_outfit
    call cho_outfit(cc_outfit_quidditch_OBJ)

    call play_sound("door")
    call cho_main("","annoyed","angry","angry","R",xpos="close",ypos="base")
    pause.1
    call play_sound("bump")
    pause.5
    call cho_main("","annoyed","angry","angry","mid",xpos="mid",ypos="base",trans="fade")
    pause.3

    call cho_main("I hate you, I hate you, I HATE YOU!","scream","closed","angry","mid",trans="hpunch")
    m "Good hustle. Nice work catching that gold thing..."
    call cho_main("This isn't the time for your stupid jokes!","open","angry","angry","mid")
    call cho_main("I've never felt so humiliated in my entire life!","open","angry","angry","R")
    m "It wasn't that bad, was it? At least you won."
    call cho_main("At the expense of my dignity!","quiver","base","raised","down")
    call cho_main("Lee Jordan only used to say that I had a nice butt!","soft","base","sad","down")
    call cho_main("Hermione spent five minutes talking about my thighs!","open","base","raised","R")
    g9 "That was the highlight of the match for me!"
    call cho_main("Well this can't go on! I insist you fire Hermione!","open","closed","base","mid")
    call cho_main("Otherwise I'm going to stop listening to your ridiculous coaching!","open","angry","angry","mid")
    m "Ugh... fine..."
    call cho_main("Good...","pout","angry","angry","mid")
    m "Should we talk strategy for the next game?"
    m "I can't help but notice your robe stayed on this game..."
    call cho_main("I'm lucky I kept it on! Can you imagine what Hermione would have said otherwise?","open","closed","raised","mid")
    g9 "Mmmm, I'm picturing it now..."
    call cho_main("Professor!","quiver","shocked","raised","mid")
    call cho_main("I think it's time I left...","open","suspicious","raised","down")
    m "So no strategy talk?"
    call cho_main("maybe later...","soft","suspicious","sad","R")

    call play_sound("door")
    hide screen cho_chang
    with d3
    pause.5

    m "..."

    jump end_cho_event


label cho_quidd_2_3: #Cho comes in telling you not to fire Hermione
    $ cho_quidd_points = 6
    $ cho_busy = True

    call update_cho_quidditch_outfit
    call cho_outfit(cc_outfit_quidditch_OBJ)

    call play_sound("door")
    call cho_main("...","pout","suspicious","sad","R",xpos="mid",ypos="base")
    m "Miss Chang... In case you were wondering, I haven't gotten around to firing miss granger yet..."
    call cho_main("Oh... Um... About that...","soft","suspicious","raised","R")
    call cho_main("Could you please... not... do that...","open","base","sad","down")
    g4 "What? You want Hermione to keep commentating your games?"
    g4 "What about our strategies?"
    call cho_main("We can still do that...","soft","base","raised","down")
    call cho_main("...","pout","base","raised","R")
    m "[cho_name], is there something you're not telling me?"
    call cho_main("Well...","soft","suspicious","raised","R")
    call cho_main("It's just that...","open","suspicious","sad","mid")
    call cho_main("People are being a lot nicer to me since that game!","quiver","suspicious","sad","mid")
    call cho_main("All the gryffindors are inviting me to parties...","soft","base","raised","down")
    call cho_main("Most of the Slytherins have stopped being racist...","open","closed","angry","mid")
    call cho_main("And the hufflepuff team weren't even upset that i beat them!","open","base","raised","L")
    m "So you want to keep on with my coaching?"
    call cho_main("Of course! It's the only chance Ravenclaw has to win the W.S.C.!","pout","suspicious","raised","down")
    m "Good, because It's about time you lost that robe of yours while you play."
    call cho_main("Fine...","quiver","base","raised","mid")
    m "And the jumper as well."
    call cho_main("What? I'll freeze!","open","shocked","raised","mid")
    m "You're a witch aren't you? (Is she?)"
    call cho_main("I suppose I can use a warmth charm...","pout","base","raised","R")
    call cho_main("But everyone will see my butt!","quiver","base","raised","down")
    g4 "That's the point."
    call cho_main("But, but, but!","open","closed","sad","mid")
    g9 "That's probably what the crowd will be chanting..."
    call cho_main("Ugh...","quiver","angry","angry","mid")
    call cho_main("Fine...","pout","angry","angry","R")
    call cho_main("But- I better win!","soft","angry","raised","mid")

    call play_sound("door")
    hide screen cho_chang
    with d3
    pause.5

    jump end_cho_event


label cho_quidd_3_1:



label quidditch_game_1:
    show screen blkfade
    with d3
    pause
    $ ccg_folder = "herm_quidditch"
    $ ccg("e6","b3","m1")
    show screen ccg
    hide screen blkfade
    with d3
    her "{size+=5}-AND IT'S ANOTHER 10 POINTs FOR RAVENCLAW!{/size}"
    her "{size+=5}I DON'T THINK ANY OF US EXPECTED THIS FROM THEM AFTER LAST YEARS PERFORMANCE!{/size}"
    ">You get rather caught up in the spectacle of brooms flying around at a blinding pace, hurling deadly balls at each other... "
    her "{size+=5}AND IT ALL SEEMS TO BE THANKS TO THEIR STAR SEEKER, CHO CHANG!{/size}"
    #FADE TO CHO
    show screen blkfade
    with d3
    pause 1
    $ ccg_folder = "astoria_sit"
    $ ccg("e6","b3","m1")
    show screen ccg
    hide screen blkfade
    with d3
    ">Cho stops chasing the tiny golden snitch to turn towards hermione in the grandstand."
    her "Her ingenious outfit seems to have made those hufflepuff boys lives a lot {b}harder{/b}."
    ">Cho's face turns a deep red before she turns away and chases after the snitch once more."
    show screen blkfade
    with d3
    pause 1
    $ ccg_folder = "herm_quidditch"
    $ ccg("e6","b3","m1")
    show screen ccg
    hide screen blkfade
    with d3
    her "{size+=5}And I can't say that I blame them, she's certainly giving us all something nice to look at...{/size}"
    her "{size+=5}But wait... Yes I think...{/size}"
    her "{size+=5}She's caught it! SHe's caught the {size+=5}SNITCH!{/size}"
    her "{size+=10}RAVENCLAW WIN! RAVENCLAW WIN!{/size}"
    show screen blkfade
    with d3
    jump day_main_menu
