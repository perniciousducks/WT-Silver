label cho_quidd_events:
    $ days_since_quidd = 0
    if cho_quidd_points == 0:
        jump cho_quidd_1_1
    elif cho_quidd_points == 1:
        jump cho_quidd_1_2
    elif cho_quidd_points == 2:
        jump cho_quidd_1_3
    jump day_main_menu



label cho_quidd_intro: #have cho come in and talk about wanting help to win more quidditch games against slytherin and gryffindor
    #genie suggest for her to play dirty
    $ cho_quidd = True
    #Temporary way of doing outfits for Cho for now 
    $ cc_vest                = "characters/cho/clothes/quidditch/jacket.png" 
    $ cc_top                 = "characters/cho/clothes/quidditch/sweater.png" 
    $ cc_acc                 = "characters/cho/base/blank.png"
    $ cc_skirt               = "characters/cho/clothes/quidditch/pants.png" 
    $ cc_stock               = "characters/cho/base/blank.png" 
    $ cc_bra                 = "characters/cho/clothes/workout/bra.png" 
    $ cc_panties             = "characters/cho/clothes/workout/panties.png" 
    $ cc_gloves              = "characters/cho/clothes/quidditch/gloves.png" 
    ">With a loud bang, your door is flung open as a disgruntled girl marches in."
    call cho_main("It's not fair!", "angry", "angry", "right", "pout")
    call cho_main("Malfoy's pompous old man just bought the whole \'Slytherin\'' team brand new Nimbus 2018s!", "closed", "angry", "closed", "yell")
    call cho_main("\'Ravenclaw\'' can't be expected to win against that!", "angry", "angry", "right_down", "angry")
    call cho_main("I demand you level the playing field sir!", "angry", "angry", "default", "yell")
    m "Why? Is that crooked as well?"
    call cho_main("This isn't funny sir! With \'Slytherin\' playing dirty there's no way we can win!", "angry", "sad", "right", "frown")
    call cho_main("Ugh! I knew you wouldn't do anything...", "angry", "angry", "default", "frown")
    m "So you don't want to hear my solution then?"
    call cho_main("Wait... You are going to help?!", "shocked", "sad", "default", "smile")
    call cho_main("Thank you, thank you, thank you!", "closed", "default", "closed", "smile")
    call cho_main("I take a small size broom and I'd like gold trim with a dark-", "default", "default", "right", "open")
    m "I'm not buying you a broom..."
    m "(Is quidditch like curling then?)"
    call cho_main("Oh...", "shocked", "sad", "right_down", "frown")
    call cho_main("Then what's your solution?", "suspicious", "angry", "default", "open")
    m "You said that the \'Slytherin\'s were playing dirty..."
    m "How about you fight fire with fire then?"
    call cho_main("So you think we should fight dirty too?", "suspicious", "default", "default", "lip_bite")
    call cho_main("But how? The rules forbid almost all foul play.", "angry", "sad", "right_down", "pout")
    m "Hmmmm..."
    m "What do they say about uniform?"
    call cho_main("Ugh... I don't think there's anything about the uniform in the rule book sir.", "default", "default", "right", "default")
    m "So if you intended to wear a skirt while you played-"
    call cho_main("I couldn't do that!", "wide", "angry", "default", "yell")
    call cho_main("Everyone would be able to see straight up it!", "wide", "angry", "right_down", "quiver")
    call cho_main("Not to mention all the other player-", "suspicious", "sad", "right", "lip_bite")
    call cho_main("Oh...", "suspicious", "angry", "default", "pout")
    call cho_main("So that's your plan then? For me to distract \'Slytherin\' with some upskirt?", "angry", "angry", "default", "pout")
    m "If you don't think it would work-"
    call cho_main("Of course it would work! Those \'Slytherin\'s are all a bunch of perverts...", "suspicious", "angry", "right", "open")
    call cho_main("But I can't go and play a game with a skirt on!", "shocked", "sad", "down", "lip_bite")
    call cho_main("All my friends would see!", "shocked", "sad", "default", "frown")
    m "They'll forget all about it after you defeat \'Slytherin\'!"
    call cho_main("I really don't think they will...", "suspicious", "sad", "right_down", "upset")
    m "Then just tell them it was the only way to win. I'm sure they'll understand."
    call cho_main("You... might be right...", "default", "sad", "right_down", "open")
    call cho_main("But still... I can't do that... can I?", "shocked", "sad", "default", "quiver")
    m "Miss Granger would..."
    call cho_main("{size=-5}She would?{/size}", "shocked", "sad", "right", "lip_bite")
    call cho_main("Alright! I'll do it!", "default", "default", "default", "smile")
    call cho_main("Go Go \'Raveclaw\'!", "closed", "sad", "closed", "yell")
    m "So when's your next game?"
    call cho_main("I'm actually about to head over for a practice game against \'hufflepuff\' now...", "default", "default", "default", "open")
    m "Sounds like the perfect time to test out your new uniform..."
    call cho_main("Already!", "shocked", "sad", "default", "open")
    call cho_main("Can't we wait a bit longer sir...", "default", "sad", "right_down", "frown")
    m "Hmmm... if you don't feel up for it, Miss Granger could prob-"
    call cho_main("Fine...", "suspicious", "angry", "default", "frown")
    m "Fantastic! Just come back here after the game to tell me how it went!"
    call cho_main("What? Can't I just run back to my dorm?", "shocked", "sad", "right", "pout")
    m "Not unless you want the rules to change again..."
    call cho_main("Ugh... Whatever old man...", "suspicious", "angry", "default", "quiver")
    ">With that Cho turns to leave your office."
    hide screen cho_chang
    with d3
    m "..."
    m "(I still have no idea what quidditch is...)"
    $ cc_vest                = "characters/cho/clothes/uniform/vest.png" 
    $ cc_top                 = "characters/cho/clothes/uniform/top.png" 
    $ cc_acc                 = "characters/cho/clothes/uniform/tie.png" 
    $ cc_skirt               = "characters/cho/clothes/uniform/skirt.png" 
    $ cc_stock               = "characters/cho/clothes/uniform/stockings.png" 
    $ cc_bra                 = "characters/cho/clothes/workout/bra.png" 
    $ cc_panties             = "characters/cho/clothes/workout/panties.png" 
    $ cc_gloves              = "characters/cho/base/blank.png" 
    
    jump day_main_menu




label cho_quidd_1_1: #come back and describe playing with a skirt on (embarrassed)
    $ cho_quidd_points = 1
    ">*knock* *knock* *knock*"
    $ cc_vest                = "characters/cho/clothes/quidditch/jacket.png" 
    $ cc_top                 = "characters/cho/clothes/quidditch/sweater.png" 
    $ cc_acc                 = "characters/cho/base/blank.png"
    $ cc_skirt               = "characters/cho/clothes/uniform/skirt.png" 
    $ cc_stock               = "characters/cho/base/blank.png" 
    $ cc_bra                 = "characters/cho/clothes/workout/bra.png" 
    $ cc_panties             = "characters/cho/clothes/workout/panties.png" 
    $ cc_gloves              = "characters/cho/clothes/quidditch/gloves.png" 
    menu:
        "\"Come in!\"":
            cho "Yes sir..."
        "\"Who is it?\"":
            cho "Cho Chang sir."
            m "Ah miss Chong... Come on in!"
            cho "..."
    ">Cho quickly enters your office, quickly turning her head to make sure she's alone."
    call cho_main("...", "suspicious", "angry", "right", "frown")
    m "You seem a little on edge today..."
    call cho_main("On edge?", "shocked", "angry", "default", "yell")
    call cho_main("Of course I'm on edge! I've never felt so humiliated in my life!", "wide", "angry", "default", "angry")
    call cho_main("You had to have me do this on the day half of \"hufflepuff\" shows up to watch the practice didn't you!", "suspicious", "angry", "right", "pout")
    call cho_main("I bet you were probably in on it...", "suspicious", "angry", "default", "upset")
    m "Now now, you know I'd never resort to any sort of foul play like that..."
    m "More importantly, how did the game go?"
    m "Score many... points?"
    m "(I hope this stupid game has points...)"
    call cho_main("As a matter of fact I did!", "closed", "default", "closed", "open")
    call cho_main("{size=+10}150 of them!!!{/size}", "default", "default", "default", "yell")
    m "Wow... That seems like a lot!"
    call cho_main("Of course it is, I caught the snitch!", "closed", "default", "closed", "smile")
    m "(The snitch? Is this prison rules?)"
    call cho_main("Today, I was racing after the snitch along with that blockhead Cedric Diggory...", "default", "sad", "right", "open")
    call cho_main("I'm normally never fast enough to beat him with my crummy old nimbus 2010...", "angry", "angry", "right_down", "pout")
    call cho_main("But today I just flew above him as we were both after the snitch!", "default", "default", "default", "smile")
    call cho_main("Ah!!! I can't believe I was able to finally catch it!", "closed", "default", "closed", "smile")
    m "Is this the first time you've caught the... snitch?"
    call cho_main("Of course! This is the first game of quidditch \"Ravenclaw\" has won in over six years!", "default", "default", "default", "smile")
    m "Wasn't this just a practice game?"
    call cho_main("I was including the practices sir...", "suspicious", "sad", "right_down", "frown")
    m "oh..."
    call cho_main("\"Ravenclaw\"... isn't very good...", "suspicious", "sad", "down", "pout")
    call cho_main("But I have a feeling that's going to change this year!", "closed", "default", "closed", "smile")
    call cho_main("We're a boot in to win the quidditch school cup!", "default", "angry", "default", "smile")
    m "Wizarding School Cup?"
    call cho_main("Stop being an idiot, Dumbledore!", "suspicious", "angry", "right", "smile")
    call cho_main("You know what the \"Q.S.C.\" is! You've only hosted it for the last 30 years!", "suspicious", "default", "default", "open")
    m "O-of course..."
    call cho_main("Speaking of which you better start getting prepared, it starts in under a month.", "closed", "default", "closed", "open")
    m "I'd be more worried about your team..."
    m "I don't think everyone is going to go down as easily as Cedric Digidy."
    m "Speaking of... What happened to him?"
    call cho_main("Oh... he um... crashed... into some... banisters...", "suspicious", "sad", "right_down", "quiver")
    m "(Crashed? Is this game a racetrack now?)"
    call cho_main("The nurses said he'll be able to walk again by the end of the week!", "default", "default", "right", "lip_bite")
    call cho_main("{size=-1}They're {size=-1}not {size=-1}so {size=-1}sure {size=-1}whether {size=-1}or {size=-1}not {size=-1}he'll {size=-1}wake {size=-1}up {size=-1}though...{/size}", "suspicious", "sad", "right", "smile")
    m "Anyway, my point is I don't think you'll be able to get away with just a skirt from now on."
    call cho_main("You don't?", "shocked", "sad", "default", "pout")
    m "If you want to have any chance of winning this years cup I think you'll need me as a coach."
    call cho_main("Coach?", "suspicious", "default", "default", "quiver")
    call cho_main("Are you sure you're able to do this sir?", "suspicious", "sad", "default", "pout")
    m "Look, I gave you one bit of advice and you won your first game in six years."
    m "Imagine what having me coach you for a season could do!"
    call cho_main("OK...", "suspicious", "default", "right", "lip_bite")
    call cho_main("But if you want me to keep doing these sorts of things...", "default", "angry", "default", "open")
    call cho_main("I want some points!", "default", "default", "right", "smile")
    m "Ugh... really?"
    m "(I was hoping she'd forgotten about that...)"
    call cho_main("Yep! If you expect me to come back here and tell you how I've humiliated myself, then \"Ravenclaw\" should at least reap the benefits.", "closed", "default", "closed", "smile")
    m "Fine..."
    m "How many do you want then?"
    call cho_main("How much would Hermione do this for?", "suspicious", "default", "default", "pout")
    menu:
        "-20 points-":
            call cho_main("Pffft, she really is a slut...", "shocked", "default", "default", "smile")
            call cho_main("I want 100!", "default", "default", "default", "open")
            m "I don't think so..."
            call cho_main("75!", "suspicious", "angry", "default", "smile")
            m "30."
            call cho_main("70!", "suspicious", "angry", "default", "quiver")
            m "40."
            call cho_main("60!", "suspicious", "angry", "default", "open")
            m "50, final offer."
            call cho_main("Done!", "closed", "default", "closed", "smile")
            $ current_payout = 50
        "-50 points-":
            call cho_main("Done!", "closed", "default", "closed", "smile")
            $ current_payout = 50
        "-100 points-":
            call cho_main("100? Really?", "shocked", "sad", "default", "open")
            call cho_main("Done!", "closed", "default", "closed", "smile")
            m "Wait, would you have done it for less?"
            call cho_main("Too late!", "default", "default", "right", "smile")
            $ current_payout = 100
    m "[current_payout] points to \"Gryff-I mean \"Ravenclaw\"!"
    $ ravenclaw += current_payout
    call cho_main("Thank you sir.", "closed", "default", "closed", "smile")
    m "So are you ready for my next bit of coaching advice?"
    call cho_main("Already? Can't I just keep wearing the skirt for now?", "shocked", "sad", "right", "open")
    m "And keep using the same old tactics?"
    m "What sort of coach do you take me for?"
    call cho_main("Well what did you have in mind?", "suspicious", "default", "default", "pout")
    m "Seeing as how the skirt was such a success, how about we up the ante then?"
    call cho_main("How do you mean?", "suspicious", "raised", "default", "open")
    m "Well that skirt seems a little long to me..."
    m "if you took a few inches off of it the other players probably wouldn't be able to keep their eyes off of you."
    call cho_main("They already can't keep their eyes off of me...", "closed", "default", "closed", "smile")
    m "For now... They'll probably get bored of that skirt after a while..."
    call cho_main("They will not!", "shocked", "angry", "default", "yell")
    m "Are you going to let me coach you or not?"
    call cho_main("...", "suspicious", "angry", "right", "pout")
    call cho_main("How much shorter?", "suspicious", "sad", "default", "lip_bite")
    m "Just a few inches..."
    call cho_main("Alright... I'll get madmam mafkin to make some adjustments...", "suspicious", "sad", "down", "default")
    m "Very good. Now when is your next game?"
    call cho_main("In two days. Another practice match, this time against \"Gryffindor\".", "default", "sad", "right", "open")
    m "Do you think they'll be distracted by your new skirt?"
    call cho_main("Ha ha ha... if Those \"Gryffindor\" boys lose it over hermione, just imagine what they do when they see me!", "suspicious", "default", "default", "smile")
    m "I'm sure you'll win then..."
    call cho_main("So am I. And I'm sure you'll be happy to reward me with a hefty amount of points after the game...", "suspicious", "angry", "default", "smile")
    m "I look forward to it..."
    ">With that, cho turns and leaves to leave your office."
    hide screen cho_chang
    with d3
    m "(I've really gotta learn what this quitit game is...)"
    $ cc_vest                = "characters/cho/clothes/uniform/vest.png" 
    $ cc_top                 = "characters/cho/clothes/uniform/top.png" 
    $ cc_acc                 = "characters/cho/clothes/uniform/tie.png" 
    $ cc_stock               = "characters/cho/clothes/uniform/stockings.png" 
    $ cc_bra                 = "characters/cho/clothes/workout/bra.png" 
    $ cc_panties             = "characters/cho/clothes/workout/panties.png" 
    $ cc_gloves              = "characters/cho/base/blank.png" 
    jump day_main_menu



label cho_quidd_1_2: #come back and describe playing with a shorter skirt on (happy they won)
    $ cho_quidd_points = 2

    $ cc_vest                = "characters/cho/clothes/quidditch/jacket.png" 
    $ cc_top                 = "characters/cho/clothes/quidditch/sweater.png" 
    $ cc_acc                 = "characters/cho/base/blank.png"
    $ cc_skirt               = "characters/cho/clothes/uniform/skirt_2.png" 
    $ cc_stock               = "characters/cho/base/blank.png" 
    $ cc_bra                 = "characters/cho/clothes/workout/bra.png" 
    $ cc_panties             = "characters/cho/clothes/workout/panties.png" 
    $ cc_gloves              = "characters/cho/clothes/quidditch/gloves.png" 
    ">*knock* *knock* *knock*"
    m "Come in..."
    ">Cho Chang quickly enters your office, a spring in her step."
    m "How did your game go?"
    call cho_main("We won again!", "shocked", "default", "default", "yell")
    call cho_main("I can't believe that we've broken our 6 year dry streak with two back-to-back wins!", "default", "default", "default", "smile")
    call cho_main("We could actually win the cup!", "shocked", "angry", "left", "open")
    m "And you weren't embarrassed?"
    call cho_main("I was a little at the start of the game...", "suspicious", "sad", "right_down", "quiver")
    call cho_main("But once I realized how much it was affecting those slack-jawed \"gryffindor\"s...", "angry", "angry", "right", "smile")
    call cho_main("It was like having my own personal weapon of mass distraction!", "shocked", "angry", "default", "smile")
    call cho_main("I don't think Harry even knew where the snitch was most of the time!", "default", "default", "right_down", "lip_bite")
    call cho_main("All he seemed to do was follow me around...", "suspicious", "sad", "down", "lip_bite")
    call cho_main("{size=-2}Him {size=-2}and {size=-2}half {size=-2}the {size=-2}team...{/size}", "suspicious", "sad", "right_down", "quiver")
    m "So you're prepared to continue our coaching?"
    call cho_main("As long as we keep winning games, I think it's only reasonable...", "closed", "default", "closed", "open")
    call cho_main("Speaking of which... did you have any more coaching tips?", "wink", "raised", "default", "smile")
    m "As a matter of fact I do..."
    call cho_main("Good... You can tell me all about them after you pay me my points!", "default", "angry", "default", "smile")
    m "How does fifty sound?"
    call cho_main("Pfft... Only fifty when my skirt is this short?", "angry", "raised", "right", "pout")
    call cho_main("I want at least sixty...", "angry", "angry", "default", "smile")
    m "Ugh fine..."
    call cho_main("(yes!)", "closed", "default", "closed", "smile")
    m "60 points to \"Ravenclaw\"!"
    $ ravenclaw += 60
    call cho_main("Thank you sir.", "closed", "default", "closed", "default")
    call cho_main("Now about that tip...", "suspicious", "default", "default", "smile")
    m "I've got a tip for you alright... and a bit more-"
    call cho_main("Professor!", "shocked", "angry", "default", "open")
    m "alright, alright... for now, why don't you try shortening that skirt of your again."
    call cho_main("Again? Isn't this short enough?", "wink", "sad", "default", "pout")
    m "Not if you want to win the grand prix or whatever..."
    call cho_main("The quidditch school cup sir...", "suspicious", "default", "default", "pout")
    m "Sure..."
    call cho_main("Well I suppose I could take another inch or two off...", "suspicious", "sad", "right_down", "quiver")
    call cho_main("But we better win the next practice against \"Slytherin\"!", "suspicious", "angry", "default", "yell")
    m "Hey, the games up to you... All I can give is pointers."
    call cho_main("Hmph... That's not what a coach is supposed to say!", "suspicious", "angry", "default", "pout")
    call cho_main("You're supposed to believe in me!", "closed", "angry", "closed", "open")
    m "You've gotta show some commitment to the game first."
    call cho_main("commitment...", "shocked", "angry", "default", "default")
    call cho_main("Isn't wearing a skirt enough?", "suspicious", "angry", "right", "pout")
    m "For now..."
    call cho_main("What's that supposed to mean?", "suspicious", "angry", "default", "upset")
    m "It means stop being such a prude and shorten that skirt!"
    call cho_main("...", "default", "sad", "right", "pout")
    call cho_main("fine...", "suspicious", "sad", "down", "default")
    call cho_main("Is that all then coach?", "default", "default", "left", "default")
    m "Unless you wanna fool around a little?"
    call cho_main("Not after a game...", "suspicious", "default", "right", "quiver")
    m "Then that will be all. "
    call cho_main("Alright then coach...", "closed", "default", "closed", "open")
    hide screen cho_chang
    with d3
    ">With that Cho, turns and leaves your office."
    jump day_main_menu

label cho_quidd_1_3: #come back and describe playing without a skirt on (aroused)
    $ cho_quidd_points = 1

    $ cc_vest                = "characters/cho/clothes/quidditch/jacket.png" 
    $ cc_top                 = "characters/cho/clothes/quidditch/sweater.png" 
    $ cc_acc                 = "characters/cho/base/blank.png"
    $ cc_skirt               = "characters/cho/clothes/uniform/skirt_3.png" 
    $ cc_stock               = "characters/cho/base/blank.png" 
    $ cc_bra                 = "characters/cho/clothes/workout/bra.png" 
    $ cc_panties             = "characters/cho/clothes/workout/panties.png" 
    $ cc_gloves              = "characters/cho/clothes/quidditch/gloves.png" 
    ">*knock* *knock* *knock*"
    m "You can just come in from now on Cho..."
    ">With that, your door slowly opens as Cho enters."
    call cho_main("What if you're in here with that floozy Hermione?", "suspicious", "angry", "default", "pout")
    call cho_main("I don't want to have to see that!", "suspicious", "angry", "right", "upset")
    m "Fair enough..."
    m "Now did you manage to win todays game?"
    call cho_main("...", "suspicious", "sad", "right_down", "pout")
    call cho_main("No...", "suspicious", "sad", "down", "open")
    m "You didn't? Why not?"
    m "Wasn't your skirt distracting enough?"
    call cho_main("It wasn't that...", "suspicious", "sad", "right_down", "pout")
    call cho_main("If anything went wrong it's that my skirt was too distracting!", "angry", "angry", "right", "frown")
    m "How's that? Don't you want the other players distracted?"
    call cho_main("I do...", "suspicious", "sad", "right", "quiver")
    call cho_main("But this was too much!", "closed", "angry", "closed", "yell")
    call cho_main("I couldn't get them off of me!", "angry", "angry", "right", "open")
    call cho_main("Half the \"slytherin\" team spent the whole game following me around, trying to get a peak from underneath!", "angry", "angry", "default", "yell")    
    m "Hmmm, I was worried this might happen...."
    call cho_main("Well how are you going to fix it then coach?", "suspicious", "angry", "default", "pout")
    m "I think we'll need to change our angle of attack..."
    call cho_main("Our angle?", "wink", "raised", "default", "frown")
    m "At the moment panty shot that all the boys are hoping for can only be seen from underneath-"
    m "-so as a result, most of the boys are hounding you to get a look."
    m "But if we widen our angle of attack, they won't be forced to chase you to get a look..."
    call cho_main("Widen our angle? What do you mean?", "wink", "raised", "default", "pout")
    m "You're gonna have to loose the jacket..."
    m "Probably the sweater as well if we're being honest..."
    call cho_main("You want me to take my jacket off?", "shocked", "angry", "default", "upset")
    call cho_main("I'll freeze!", "wide", "angry", "default", "yell")
    call cho_main("Not to mention the other players and the spectators will be able to see everything!", "angry", "sad", "right", "lip_bite")
    call cho_main("My skirt was at least a little hidden before...", "suspicious", "angry", "right", "pout")
    m "If you want to win this is the only way..."
    call cho_main("Can't I just go back to the longer skirt? That was working!", "shocked", "sad", "default", "open")
    m "I don't think these \"slytherin\" boys are going to be interested in that after what they saw today..."
    m "I know I wouldn't..."
    call cho_main("Coach!", "angry", "angry", "default", "yell")
    m "Just trust me... If you lose the next game you can put it back on..."
    call cho_main("OK... but I want some points!", "suspicious", "sad", "default", "pout")
    call cho_main("Seventy five to be precise...", "closed", "default", "closed", "smile")
    m "...fine..."
    call cho_main("(awesome!)", "wink", "default", "right", "smile")
    m "75 points to \"Ravenclaw\"!"
    $ ravenclaw += 75
    call cho_main("Alright... well I'll come and see you after the next game...", "suspicious", "sad", "default", "default")
    call cho_main("When I'm not wearing a jacket...", "suspicious", "sad", "right", "open")
    m "And wearing a mini-skirt..."
    call cho_main("And wearing... a mini-skirt...", "suspicious", "sad", "right_down", "pout")
    m "Good. With tactics like this we can't lose."
    call cho_main("We better not!", "suspicious", "angry", "default", "upset")
    call cho_main("This might be the first real chance \"Ravenclaw\" has ever had to win the cup.", "closed", "sad", "closed", "open")
    m "I'm sure this must mean a lot to you..."
    call cho_main("It does... I might even get picked up by a pro team!", "default", "default", "right", "smile")
    m "..."
    call cho_main("Agh, I can't wait!", "closed", "default", "closed", "yell")
    call cho_main("I better go talk to the team!", "default", "default", "right", "default")
    m "Well, off you go then."
    call cho_main("Thank you Professor...", "wink", "default", "default", "smile")
    ">Cho cheerily leaves your office."
    hide screen cho_chang
    with d3

    jump day_main_menu

label cho_quidd_2_1: #Comes back after playing without a robe on

label cho_quidd_2_2: #Comes back after playing without a jumper on

label cho_quidd_3_1: 



















