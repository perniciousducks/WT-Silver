

### Old Writing ###

label cho_favor_3: # Not in use.

        m "Miss Chang, do you know what a blowjob is?"
        call cho_main("?","smile","base","base","mid")
        call cho_main("you want me to put my mouth on your...","smile","base","base","mid")
        call cho_main("you want me to put my mouth on your...penis?","smile","base","base","mid")
        m "I just thought you'd like the chance to keep up with Miss Granger."
        call cho_main("you don't mean she's been-","smile","base","base","mid")
        menu:
            "-Absolutely-":
                m "I suppose Miss Granger is just more competitive than you."
                call cho_main("...","smile","base","base","mid")
                call cho_main("(i can't believe it.)","smile","base","base","mid")
                call cho_main("(What a...)","smile","base","base","mid")
                call cho_main("(what a...stupid whore.)","smile","base","base","mid")
                call cho_main("i can do it too!","smile","base","base","mid")
                call cho_main("i'll only charge you 60 points.","smile","base","base","mid")
                menu:
                    "-I'll give you 70 points-":
                        m "I'll give you 80."
                        call cho_main("Really?","smile","base","base","mid")
                        call cho_main("Really? 70 points?","smile","base","base","mid")
                        call cho_main("Okay.","smile","base","base","mid")
                        $ cho_mood -= 1
                        $ current_payout = 70
                        jump cho_favor_3_1

                    "-Okay, 60-":
                        m "60, sounds good."
                        call cho_main("Okay.","smile","base","base","mid")
                        $ current_payout = 60
                        jump cho_favor_3_1

                    "-Mrs. Granger only charges 55...-":
                        m "Ms. Granger only charges 55..."
                        call cho_main("55?...","smile","base","base","mid")
                        call cho_main("55?...why would she-","smile","base","base","mid")
                        call cho_main("I'll do it for 50!","smile","base","base","mid")
                        $ current_payout = 50
                        jump cho_favor_3_1

            "-Of course not-":
                m "Don't be crazy. Of course, not."
                m "Ms. Granger has standards."
                call cho_main("...","smile","base","base","mid")
                m "She's just been earning a lot of points lately."
                call cho_main("She is?","smile","base","base","mid")
                m "Well, she is the school's top student..."
                call cho_main("I'll do it for 60 points.","smile","base","base","mid")

                menu:
                    "-I'll give you 70 points-":
                        m "I'll give you 80."
                        call cho_main("Really?","smile","base","base","mid")
                        call cho_main("Really? 70 points?","smile","base","base","mid")
                        call cho_main("Okay.","smile","base","base","mid")
                        $ cho_mood -= 1
                        $ current_payout = 70
                        jump cho_favor_3_1

                    "-Okay, 60-":
                        m "60, sounds good."
                        call cho_main("Okay.","smile","base","base","mid")
                        $ current_payout = 60
                        jump cho_favor_3_1

                    "-You'll get 40-":
                        m "I'll give you 40 points."
                        call cho_main("40! I get more than that for...well, the other things you make me do.","smile","base","base","mid")
                        call cho_main("I'll do it for 50.","smile","base","base","mid")

                        menu:
                            "-Okay-":
                                m "Deal."
                                $ current_payout = 50
                                jump cho_favor_3_1

                            "-No way-":
                                m "No way, girl. You're not worth more than 40."
                                call cho_main("Fine!","smile","base","base","mid")
                                $ cho_mood += 10
                                m "And try not to look so miserable about it."
                                $ cho_mood += 10
                                call cho_main("(Asshole.)","smile","base","base","mid")
                                call cho_main("(how am i even supposed to do this?)","smile","base","base","mid")
                                $ current_payout = 40
                                jump cho_favor_3_1

        m "I assume you're familar with the ancient Chinese art of 'SukiSuki'."
        call cho_main("What?","smile","base","base","mid")
        m "I want a blowjob."
        if cho_mood >= 6:
            jump cho_mood_blowjob
        call cho_main("Okay. but i'm only doing this to help my House.","smile","base","base","mid")
        call cho_main("And i want [current_payout] points.","smile","base","base","mid")
        m "Yes, yes. Now get sucking."
        jump cho_favor_3_1

label cho_favor_3_1:

    call cho_main("Um...","smile","base","base","mid")
    call cho_main("um...What do I...","smile","base","base","mid")

    menu:
        "-Are you serious?-":
            m "Are you serious?"
            call cho_main("Of course I'm serious! I'm not a whore like Hermione.","smile","base","base","mid")
            m "You just suck my cock in your mouth like a lollipop."
            call cho_main("(Like candy? ew... No way, that's nasty. Old...worm tasting like candy...)","smile","base","base","mid")
            call cho_main("([current_payout]! [current_payout]!)","smile","base","base","mid")
            "Cho awkwardly drops to her knees and opens her mouth, thrusting her tongue out."
            call cho_main("hoh's hhisss hHohessor?(How's this professor?)","smile","base","base","mid")
            "You feel your cock twitch under your robes at the sight of your student crouched down on her knees like a whore."
            m "Yes...that will do nicely."
            "You pull your throbbing cock out of your wizard's robes and stand over Cho."
            "The erotic sight causes pre-cum to ooze from the tip of your meaty wand."
            "Cho flinches as your cock bobs past her nose."
            call cho_main("ee! 'e 'arehul!(Be careful!)","smile","base","base","mid")
            "The head of your cock briefly touches the very tip of Cho's pointed nose, leaving a line of pre-cum stretching between you."
            call cho_main("huhhhh...","smile","base","base","mid")
            call cho_main("'uT ith at?(what is that?)","smile","base","base","mid")
            "Cho's mouth drips with with saliva."
            "You arch your cock toward her tongue and guide it into her mouth."
            call cho_main("(eww. it tastes weird...)","smile","base","base","mid")
            m "Yessss....That's better."
            "You let you cock rest there for a moment. Basking in the warmth of Cho's mouth."
            call cho_main("Hmmm.","smile","base","base","mid")
            m "Hold on."
            "You slowly push your cock further into the young girls mouth."
            call cho_main("Hmmmm!","smile","base","base","mid")
            "The sensations are incredible, and your head is wrapped in warm, slippery wetness."
            "Suddenly your cock bottoms out at the back of Cho's throat."
            call cho_main("*cough* *ack!*","smile","base","base","mid")
            "You pull your cock back just as a thick stream of slime spills out of Cho's mouth."
            call cho_main("Bleh!","smile","base","base","mid")
            call cho_main("Bleh!...","smile","base","base","mid")
            call cho_main("Oh my god!","smile","base","base","mid")
            call cho_main("I'm sorry, Professor!","smile","base","base","mid")

            menu:
                "-15 points-":
                    m "Fine! Just do it!"
                    call cho_main("Okay.","smile","base","base","mid")
                    "Cho leans forward and begins to quickly bob her head over your cock."
                    "Her inexperienced mouth only manages to cover your bulbous head, but the constant stimulation quickly drives you over the edge."
                    m "You fucking whore!"
                    "Your cock twitches in Cho's mouth, dumping your cum across her tongue."
                    "Her cheeks begin to bulge with the heavy load."
                    "When it's over your cock pops out of the poor girls lips, leaving her struggling with the massive mouthful."
                    call cho_main("Hmmm!","smile","base","base","mid")
                    "Cho looks around for a place to spit it out."

                "-5 points-":
                    m "I'll give you 5 points."
                    call cho_main("...deal.","smile","base","base","mid")
                    "Cho leans forward and begins to quickly bob her head over your cock."
                    "Her inexperienced mouth fumbles around your head, but the constant stimulation quickly drives you over the edge."
                    m "Yes, take it!"
                    "Your cock twitches in Cho's mouth, dumping your cum in her mouth."
                    "Her cheeks begin to bulge with the heavy load."
                    "When it's over your cock slips out of the Cho's lips, leaving her struggling with the massive mouthful."
                    call cho_main("Hmmm!","smile","base","base","mid")
                    "Cho looks around for a place to spit it out."

                    menu:
                        "-Give her an empty wine glass-":
                            "The only object in your office is a wine glass left over from your nightly chats with Snape."
                            "You pass Ms. Chang the glass just as a little stream of cum dribbles over her lip."
                            call cho_main("Blehgff...","smile","base","base","mid")
                            "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                            "After a few moments it's completely full."
                            call cho_main("Thank you, sir.","smile","base","base","mid")
                            "#gain item [Cum Goblet]"
                            m "Yes...well, [current_payout] to Ravenclaw."
                            jump end_cho_event

                        "-Make her swallow it.-":
                            m "Hey, I'm paying extra so you'd better swallow it."
                            call cho_main("fmMmhm mt?!(Swallow it?!)","smile","base","base","mid")
                            m "You want your points, don't you?"
                            call cho_main("(no way, you gross, old pervert!)","smile","base","base","mid")
                            call cho_main("(I'm gonna throw up!)","smile","base","base","mid")
                            "Cho's eyes are turning red, and her overstuffed cheeks flush."
                            $ renpy.play('sounds/gulp.mp3')
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("Blahg...","smile","base","base","mid")
                            call cho_main("Is...","smile","base","base","mid")
                            call cho_main("is...is that okay?","smile","base","base","mid")
                            m "Very good. [current_payout] to Ravenclaw."
                            call cho_main("Thank you, Profe-","smile","base","base","mid")
                            $ renpy.play('sounds/burp.mp3')
                            call cho_main("...","smile","base","base","mid")
                            jump end_cho_event
                "-Fuck you!-":
                    m "(What a bitch!)"
                    m "You greedy whore!"
                    "You grab your cock and quickly stroke it."
                    "After a few fast pumps your cock explodes, coating Cho in your smelly cum."
                    call cho_main("W-what?...","smile","base","base","mid")
                    m "[current_payout] to Ravenclaw. Now, get out of my office."
                    call cho_main("But I can't go out like this!","smile","base","base","mid")
                    m "Get out."
                    call cho_main("...","smile","base","base","mid")
                    call cho_main("...Fine!","smile","base","base","mid")
                    $ cho_mood += 10
                    #Cho storms out.
                    m "Bitches..."
                    jump end_cho_event

        "-Put my cock in your mouth.-":
            m "You just have to put my cock in your mouth."
            call cho_main("I know that!","smile","base","base","mid")
            call cho_main("I know that! But after that...","smile","base","base","mid")
            m "Just suck on it and tease it with your tongue."
            call cho_main("(Tease it with my tongue? ew. that sounds gross...)","smile","base","base","mid")
            call cho_main("([current_payout]! [current_payout]!)","smile","base","base","mid")
            "Cho awkwardly drops to her knees and opens her mouth, thrusting her tongue out."
            call cho_main("'oo cahn puh i' In 'ow...(you can put it in now...)","smile","base","base","mid")
            "You feel your cock thicken under your robes."
            m "Don't mind if I do..."
            "You pull your throbbing cock out of your robes and stand over Cho."
            "pre-cum oozes from the tip of your thick cock."
            "Cho flinches as your head bobs past her nose."
            call cho_main("ee! 'e 'arehul!(Be careful!)","smile","base","base","mid")
            "You slimy pre-cum touches the very tip of Cho's pointed nose, leaving a dangling line of slime stretching between you."
            call cho_main("huhhhh...","smile","base","base","mid")
            call cho_main("'uT ith at?(what is that?)","smile","base","base","mid")
            "Cho's mouth drips with with saliva."
            "You arch your cock toward her tongue and guide your cock into her mouth."
            call cho_main("(eww. it tastes weird...)","smile","base","base","mid")
            m "Yessss....That's better."
            "You let you cock rest there for a moment. Basking in the warmth of Cho's mouth."
            call cho_main("Hmmm.","smile","base","base","mid")
            m "Hold on."
            "You slowly push your cock further into the young girls mouth."
            call cho_main("Hmmmm!","smile","base","base","mid")
            "The sensations are incredible, and your head is wrapped in warm, slippery wetness."
            "Suddenly your cock bottoms out at the back of Cho's throat."
            call cho_main("*cough* *ack!*","smile","base","base","mid")
            "You pull your cock back just as a thick stream of slime spills out of Cho's mouth."
            call cho_main("Bleh!","smile","base","base","mid")
            call cho_main("Bleh!...","smile","base","base","mid")
            call cho_main("Oh my god!","smile","base","base","mid")
            call cho_main("I'm sorry, Professor!","smile","base","base","mid")

            menu:
                "-That's probably enough-":
                    m "Maybe, I went a little too far."
                    jump end_cho_event

                "-Keep going-":
                    m "You don't get your points if you didn't finish."
                    call cho_main("I'm sorry, Professor!","smile","base","base","mid")
                    m "That's quite all right, girl."
                    "You shove your cock back in her mouth, this time careful not to go too deep."
                    "Cho's tongue rolls around your cock with amateurish effort, getting in the way more than helping."
                    "To your surprise the thought of her inexperience brings you to the edge."

                    menu:
                        "-Cum-":
                            "#Genie cums in Cho's mouth."
                            call cho_main("Hmmmmm!","smile","base","base","mid")
                            m "By the profits of Disney..."
                            call cho_main("Hmmmm!...","smile","base","base","mid")
                            call cho_main("hmmmm!...Mmmmm!","smile","base","base","mid")
                            "In a panic Cho tries to swallow your cum, but it catches at the back of her throat"
                            call cho_main("Blehg!","smile","base","base","mid")
                            "Your cum spews out of Cho's mouth and drips down her chin in a thick torrent of slime."
                            call cho_main("(oh god...that was so nasty..)","smile","base","base","mid")
                            call cho_main("Gross! You owe me extra for that!","smile","base","base","mid")

                            menu:
                                "-Fine 5 extra points-":
                                    m "Very well, Ms. Chang. [current_payout] to Ravenclaw."
                                    call cho_main("Thank you, sir.","smile","base","base","mid")
                                    $ current_payout += 5
                                    jump end_cho_event

                                "-What? Absolutely not.-":
                                    m "What? Absolutely not."
                                    call cho_main("That's not fair!","smile","base","base","mid")
                                    m "Take it or leave it, Ms. Chong."
                                    call cho_main("MY name is Chang, you old jerk!","smile","base","base","mid")
                                    m "Do you want your points or not?"
                                    call cho_main("yes, please.","smile","base","base","mid")
                                    m "[current_payout] to Ravenclaw."
                                    jump end_cho_event
                        "-Warn Her-":
                            m "I'm going to cum!"
                            call cho_main("Hm!","smile","base","base","mid")
                            call cho_main("hm!...Blehrg!","smile","base","base","mid")
                            "Cho spits your slippery cock out of her mouth."
                            "You wait for her to finish you off, but instead she crosses her arms."
                            call cho_main("i want 15 more points.","smile","base","base","mid")
                            m "What?!"
                            call cho_main("You only said I had to suck your cock. If you wanted to cum, I'd like another 15 points.","smile","base","base","mid")

                            menu:
                                "-15 points-":
                                    m "Fine! Just do it!"
                                    call cho_main("Okay.","smile","base","base","mid")
                                    "Cho leans forward and begins to quickly bob her head over your cock."
                                    "Her inexperienced mouth only manages to cover your bulbous head, but the constant stimulation quickly drives you over the edge."
                                    m "You fucking whore!"
                                    "Your cock twitches in Cho's mouth, dumping your cum across her tongue."
                                    "Her cheeks begin to bulge with the heavy load."
                                    "When it's over, your cock pops out of the poor girls lips, leaving her struggling with the massive mouthful."
                                    call cho_main("Hmmm!","smile","base","base","mid")
                                    "Cho looks around for a place to spit it out."

                                "-5 points-":
                                    m "I'll give you 5 points."
                                    call cho_main("...deal.","smile","base","base","mid")
                                    "Cho leans forward and begins to quickly bobs her head over your cock."
                                    "Her inexperienced mouth fumbles around your head, but the constant stimulation quickly drives you over the edge."
                                    m "Yes, take it!"
                                    "Your cock twitches in Cho's mouth, dumping your cum in her mouth."
                                    "Her cheeks begin to bulge with the heavy load."
                                    "When it's over your cock slips out of the Cho's lips, leaving her struggling with the massive mouthful."
                                    call cho_main("Hmmm!","smile","base","base","mid")
                                    "Cho looks around for a place to spit it out."

                                    menu:
                                        "-Give her an empty wine glass-":
                                            "The only object in your office is a wine glass, left over from your nightly chats with Snape."
                                            "You pass Ms. Chang the glass just she dribbles a little stream of cum over her lip."
                                            call cho_main("Blehgff...","smile","base","base","mid")
                                            "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                            "After a few moments it's completely full."
                                            call cho_main("Thank you, sir.","smile","base","base","mid")
                                            "#gain item [Cum Goblet]"
                                            m "Yes...well, [current_payout] to Ravenclaw."
                                            jump end_cho_event
                                        "-Make her swallow it.-":
                                            m "Hey, I'm paying extra so you'd better swallow it."
                                            call cho_main("fmMmhm mt?!(Swallow it?!)","smile","base","base","mid")
                                            m "You want your points, don't you?"
                                            call cho_main("(No way, you gross, old pervert!)","smile","base","base","mid")
                                            call cho_main("(I'm gonna throw up!)","smile","base","base","mid")
                                            "Cho's eyes are turning red, and her overstuffed cheeks flush."
                                            $ renpy.play('sounds/gulp.mp3')
                                            $ renpy.play('sounds/gulp.mp3')
                                            call cho_main("Blahg...","smile","base","base","mid")
                                            call cho_main("Is...","smile","base","base","mid")
                                            call cho_main("is...is that okay?","smile","base","base","mid")
                                            m "Very good. [current_payout] to Ravenclaw."
                                            call cho_main("THank you, Profe-","smile","base","base","mid")
                                            $ renpy.play('sounds/burp.mp3')
                                            call cho_main("...","smile","base","base","mid")
                                            jump end_cho_event
                                "-Fuck you!-":
                                    m "(What a bitch!)"
                                    m "You greedy whore!"
                                    "You grab your cock and quickly stroke it."
                                    "After a few fast pumps your cock explodes, coating Cho in your smelly cum."
                                    call cho_main("W-what?...","smile","base","base","mid")
                                    m "[current_payout] to Ravenclaw. Now, get out of my office."
                                    call cho_main("But I can't go out like this!","smile","base","base","mid")
                                    m "Get out."
                                    call cho_main("...","smile","base","base","mid")
                                    call cho_main("...Fine!","smile","base","base","mid")
                                    $ cho_mood += 10
                                    #Cho storms out.
                                    m "Bitches..."
                                    jump end_cho_event
        "-Let's go slow-":
            m "Let's just go slow."
            call cho_main("Thank you, Professor Dumbledore.","smile","base","base","mid")
            call cho_main("Do i just...you know, suck on it?","smile","base","base","mid")
            m "Yes. Think of it like a lollipop."
            call cho_main("(Like a lollipop? That might be okay...)","smile","base","base","mid")
            call cho_main("(Just ignore the fact that that the wrinkly, old cock in my mouth belongs to a crusty, old wizard...)","smile","base","base","mid")
            call cho_main("([current_payout]! current_payout]!)","smile","base","base","mid")
            "Cho awkwardly drops to her knees and opens her mouth, thrusting her tongue out."
            call cho_main("I' I' 'ood 'o'esser?(is this good, professor?)","smile","base","base","mid")
            "You gently carress Cho's warm cheek with the back of your hand."
            call cho_main("(Wow...that was nice.)","smile","base","base","mid")
            $ cho_mood -= 1
            m "Yes, girl...that will do nicely."
            "You pull your throbbing cock out of your robes and stand over Cho."
            "The erotic sight causes pre-cum to ooze from the tip of your cock."
            "Cho's eyes flinch as your cock bobs above her face."
            "Her long Asian lashes blink fast as she fight the reflex to pull away."
            "A slimy stream of pre-cum drips down onto her face."
            call cho_main("ee! 'e 'arehul!(Be careful!)","smile","base","base","mid")
            "The tip of your cock briefly touches Cho's tongue, leaving a line of pre-cum stretching between you."
            call cho_main("huhhhh...","smile","base","base","mid")
            call cho_main("'uT ith at?(what is that?)","smile","base","base","mid")
            "Cho's mouth drips with with saliva."
            "You arch your cock toward her tongue and slowly rub your cock across it."
            call cho_main("(it tastes weird...)","smile","base","base","mid")
            m "Yessss....That's good."
            "You let you cock rest there for a moment. Basking in the warmth of Cho's breath and the soft, slipperiness of her tongue."
            call cho_main("Hmmm.","smile","base","base","mid")
            m "Shhh. It's okay, girl."
            "You slowly slide your cock into the young girls mouth."
            call cho_main("Hmmmm....","smile","base","base","mid")
            "The sensations are incredible, and soon your head is wrapped in warm, slippery wetness."
            "You leave it there for a moment."
            call cho_main("(This isn't bad...)","smile","base","base","mid")
            "You pull your cock back, out of Cho's mouth."
            call cho_main("Mmm.","smile","base","base","mid")
            call cho_main("Mmm....","smile","base","base","mid")
            "Cho opens her mouth wide, letting spit drip from her tongue."

            menu:
                "-That's probably enough-":
                    m "That's probably enough for now."
                    m "[current_payout] to Ravenclaw."
                    jump end_cho_event

                "-Keep going-":
                    m "We're almost done, girl."
                    call cho_main("(this is definitely worth [current_payout]...)","smile","base","base","mid")
                    "You gently guide your cock back into her mouth, careful not to go too deep."
                    "Cho's tongue rolls around your cock with sweet effort, slipping around your head."
                    "To your surprise her tongue finds your hole, and the assault brings you to the edge."

                    menu:
                        "-Cum-":
                            #Genie cums in Cho's mouth.
                            call cho_main("Hmmmmm!","smile","base","base","mid")
                            m "G-good...girl..."
                            call cho_main("Hmmmm!...","smile","base","base","mid")
                            call cho_main("hmmmm!...Mmmmm!","smile","base","base","mid")
                            "In a panic Cho tries to swallow your cum, but it catches at the back of her throat"
                            call cho_main("Blehg!","smile","base","base","mid")
                            "Your cum spews out of Cho's mouth and drips down her chin in a thick torrent of slime."
                            call cho_main("(oh god...there was so much..)","smile","base","base","mid")
                            call cho_main("Gross!","smile","base","base","mid")
                            call cho_main("gross! warn me next time, okay?","smile","base","base","mid")
                            m "That was great. [current_payout] to Ravenclaw."
                            jump end_cho_event

                        "-Warn Her-":
                            m "I'm getting close!"
                            call cho_main("Hm?","smile","base","base","mid")
                            call cho_main("hm?...Blehrg!","smile","base","base","mid")
                            "Cho spits your slippery cock out of her mouth."
                            "You wait for her to finish you off, but instead she looks up at you with a smile."
                            call cho_main("if you give me 5 extRa points i'll eat it.","smile","base","base","mid")
                            m "You'll eat it?"
                            call cho_main("Well, yeah. I mean, it's gross, but I need the points...","smile","base","base","mid")

                            menu:
                                "-15 points-":
                                    m "I'll give you 15 points."
                                    call cho_main("what? Really?","smile","base","base","mid")
                                    call cho_main("Okay.","smile","base","base","mid")
                                    "Cho dives forward and guides your cock into her mouth."
                                    "Her tongue wraps around your bulbous head, and twists back and forth."
                                    call cho_main("(Mmm. It is like candy!)","smile","base","base","mid")
                                    m "By the power of GreySkull!"
                                    #Genie cums in Cho's mouth.
                                    "Your balls pull tight against your body and your cock begins to twitch."
                                    "Suddenly, you grab Cho's head and drive deeper between her soft lips, dumping your cum at the back of her mouth."
                                    "You feel her trying to swallow, but her cheeks start to bulge from the heavy load."
                                    "When it's over, your cock pops out of the smiling girl's lips, leaving her struggling with the massive mouthful."
                                    call cho_main("Hmmm!","smile","base","base","mid")
                                    "Cho looks around for a place to spit it out."

                                    menu:
                                        "-Give her an empty wine glass-":
                                            "The only object in your office is a wine glass left over from your nightly chats with Snape."
                                            "You pass Ms. Chang the glass just as she dribbles a little stream of cum over her lip."
                                            call cho_main("Blehgff...","smile","base","base","mid")
                                            "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                            "After a few moments it's completely full."
                                            call cho_main("Thank you, sir.","smile","base","base","mid")
                                            #gain item [Cum Goblet]
                                            m "Yes...well, [current_payout] to Ravenclaw."
                                            jump end_cho_event
                                        "-Make her swallow it.-":
                                            m "Hey, I'm paying extra so you'd better swallow it all."
                                            call cho_main("fmMmhm mt?!(Swallow it all?!)","smile","base","base","mid")
                                            m "You want your points, don't you?"
                                            call cho_main("(I'm seriously going to throw up...)","smile","base","base","mid")
                                            call cho_main("Mm hhmm!","smile","base","base","mid")
                                            "Cho's eyes are turning red, and her overstuffed cheeks flush."
                                            $ renpy.play('sounds/gulp.mp3')
                                            $ renpy.play('sounds/gulp.mp3')
                                            call cho_main("Blahg...","smile","base","base","mid")
                                            call cho_main("...","smile","base","base","mid")
                                            call cho_main("...All gone.","smile","base","base","mid")
                                            m "Very good. [current_payout] to Ravenclaw."
                                            call cho_main("THank you, Profe-","smile","base","base","mid")
                                            $ renpy.play('sounds/burp.mp3')
                                            call cho_main("...","smile","base","base","mid")
                                            jump end_cho_event
                                "-5 points-":
                                    m "Sure, I'll give you 5 points."
                                    call cho_main("You will?","smile","base","base","mid")
                                    "Cho leans forward and begins to quickly bob her head over your cock."
                                    "Her inexperienced mouth enthusiastically work your shaft."
                                    "Before long, you can feel the cum churning in your enchanted nut sack."
                                    m "It's magically delicious!"
                                    #Genie cums in Cho's mouth.
                                    #Cho_WideEyes"!..."
                                    #Cho_WideEyes"(What?)"
                                    "Cho's cheeks begin to bulge with the heavy load, causing her to forget your mad outburst."
                                    "When it's over, your cock slips out from between Cho's lips, leaving her struggling with the massive mouthful."
                                    call cho_main("Hmmm!","smile","base","base","mid")
                                    "Cho looks around for a place to spit it out."

                                    menu:
                                        "-Give her an empty wine glass-":
                                            "The only object in your office is a wine glass left over from your nightly chats with Snape."
                                            "You pass Ms. Chang the glass just she dribbles a little stream of cum over her lip."
                                            call cho_main("Blehgff...","smile","base","base","mid")
                                            "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                            "After a few moments it's completely full."
                                            call cho_main("Thank you, sir.","smile","base","base","mid")
                                            #gain item [Cum Goblet]
                                            m "Yes...well, [current_payout] to Ravenclaw."
                                            jump end_cho_event
                                        "-Make her swallow it.-":
                                            m "Hey, I'm paying extra so you'd better swallow it."
                                            call cho_main("fmMmhm mt?!(Swallow it?!)","smile","base","base","mid")
                                            m "You want your points, don't you?"
                                            call cho_main("(No way, you gross, old pervert!)","smile","base","base","mid")
                                            call cho_main("(I'm gonna throw up!)","smile","base","base","mid")
                                            "Cho's eyes are turning red, and her overstuffed cheeks flush."
                                            $ renpy.play('sounds/gulp.mp3')
                                            $ renpy.play('sounds/gulp.mp3')
                                            call cho_main("Blahg...","smile","base","base","mid")
                                            call cho_main("Is...","smile","base","base","mid")
                                            call cho_main("is...is that okay?","smile","base","base","mid")
                                            m "Very good. [current_payout] to Ravenclaw."
                                            call cho_main("THank you, Profe-","smile","base","base","mid")
                                            $ renpy.play('sounds/burp.mp3')
                                            call cho_main("...","smile","base","base","mid")
                                            jump end_cho_event
                                "-Fuck you!-":
                                    m "(I didn't know Chong was a Jewish name?!)"
                                    m "You greedy whore!"
                                    "You grab your cock and pound it like Anne Frank."
                                    m "After a few fast pumps your cock explodes."
                                    #Genie cums.
                                    "After a few fast pumps your cock explodes, coating Cho in your non-kosher cum."
                                    call cho_main("W-what?...","smile","base","base","mid")
                                    m "[current_payout] to Ravenclaw. Now, get out of my office."
                                    call cho_main("but I can't go out like this!","smile","base","base","mid")
                                    m "Get out."
                                    call cho_main("...","smile","base","base","mid")
                                    call cho_main("...Fine!","smile","base","base","mid")
                                    $ cho_mood += 10
                                    #Cho storms out.
                                    m "Bitches..."
                                    jump end_cho_event

label cho_favor_3_2:

        m "Ms. Chang, I'd like you to give me another blowjob."
        if cho_mood > 10:
            jump cho_mood_blowjob

        call cho_main("[current_payout] points.","smile","base","base","mid")
        m "Of course."
        "Cho drops to her knees and waits patiently."
        call cho_main("whenever you're ready.","smile","base","base","mid")
        m "Open your mouth."
        "Cho obeys, opening her mouth and thusting her tongue out."
        call cho_main("On 'ea'y...(I'm ready...)","smile","base","base","mid")
        "Your cock throbs under your robes."
        m "This is why I got into teaching..."
        "You pull your throbbing cock out of your robes and stand over Cho."
        "Cho's mouth drips with with saliva."
        "You slap your cock against her tongue a few times before guiding it into her mouth."
        call cho_main("(What's he doing...)","smile","base","base","mid")
        m "Yessss....that's better."
        "You let your cock rest there for a moment. Basking in the warmth of Cho's mouth."
        call cho_main("Hmmm.","smile","base","base","mid")
        m "Hold on."
        "You slowly push your cock deeper into the young girls mouth."
        call cho_main("Hmmmm!","smile","base","base","mid")
        "The sensations are incredible, and your head is wrapped in warm, slippery wetness."
        "Suddenly your cock bottoms out at the back of Cho's throat."
        call cho_main("*cough* *ack!*","smile","base","base","mid")
        "You pull your cock back just as a thick stream of slime spills out of Cho's mouth."
        call cho_main("Bleh!","smile","base","base","mid")
        call cho_main("Bleh!...","smile","base","base","mid")
        call cho_main("Oh my god!","smile","base","base","mid")
        call cho_main("I'm sorry, Professor!","smile","base","base","mid")
        menu:
                    "-Be Nice-":
                        m "That's perfectly alright, Ms. Chang."
                        m "We'll just consider this part of your education."
                        call cho_main("Thank you, sir.","smile","base","base","mid")
                        "Cho gently wraps her mouth around your cock."
                        "Then, flattening her tongue, she guides your cock to the back of her mouth."
                        "You can feel the entrance to her throat tickle the tip of your head."
                        m "Very good. Now, just relax."
                        call cho_main("Mmhm.","smile","base","base","mid")
                        "Cho's tongue twitches under your cock as she tries her best to relax her throat."
                        m "Mmm. Good. Now, try to swallow."
                        call cho_main("*GuL* *Gul* *Glug*","smile","base","base","mid")
                        "Finally, you feel the head of your cock pop into her throat."
                        "The sensation of her tight flesh squeezing around your length is incredible."
                        call cho_main("...","smile","base","base","mid")
                        call cho_main("......","smile","base","base","mid")
                        call cho_main("..........","smile","base","base","mid")
                        call cho_main("*cough* *splutter* ack! i almost had it.","smile","base","base","mid")
                        call cho_main("Let me try again.","smile","base","base","mid")
                        "Cho takes you back into her mouth."
                        "There's a determined look in her eyes."
                        call cho_main("*Gul* *gulp* *Gluck*","smile","base","base","mid")
                        "Your cock pop's back into her throat."
                        "You can feel Cho struggling to hold herself down."
                        "Her throat is fighting around you, squeezing in violent pulses."
                        "The sensations are too much."

                        menu:

                            "-Cum-":
                                #Genie cums in Cho's mouth.
                                call cho_main("*Gluuuuuuh!*","smile","base","base","mid")
                                m "Yessss..."
                                call cho_main("*Glurck!*...","smile","base","base","mid")
                                call cho_main("*GlUrck!*...*gluglugulgh...*","smile","base","base","mid")
                                "Cho struggles to swallow as your cum pumps down her throat, but she gags, vomiting your slimy cum."
                                call cho_main("Blehg!","smile","base","base","mid")
                                "A torrent of slime spews out of Cho's mouth and drips down her chin splattering her uniform."
                                call cho_main("(oh god...that was so nasty..)","smile","base","base","mid")
                                call cho_main("gross! My uniform! You owe me extra, you jerk!","smile","base","base","mid")

                                menu:

                                    "-Fine 5 extra points-":
                                        m "Fine, Ms. Chang. [current_payout] to Ravenclaw."
                                        call cho_main("Thank you, sir.","smile","base","base","mid")
                                        jump end_cho_event

                                    "-What? Absolutely not.-":
                                        m "Absolutely not."
                                        call cho_main("but! That's not fair!","smile","base","base","mid")
                                        m "Take it or leave it, Ms. Chong."
                                        call cho_main("MY name is Chang, you old jerk!","smile","base","base","mid")
                                        #Cho_Sad"It's not even a hard name..."
                                        m "DO you want your points or not?"
                                        call cho_main("yes, please.","smile","base","base","mid")
                                        m "[current_payout] to Ravenclaw."
                                        jump end_cho_event

                            "-Warn Her-":
                                m "I'm going to cum!"
                                call cho_main("Hm!","smile","base","base","mid")
                                call cho_main("hm!...Blehrg!","smile","base","base","mid")
                                "Cho pulls back, dragging your slippery cock out of her throat."
                                "You catch your breath and wait patiently for her to finish you off."
                                "But instead she crosses her arms. and smirks cleverly."
                                call cho_main("15 points.","smile","base","base","mid")
                                m "What?!"
                                call cho_main("The original deal was just for a blowjob. if you want to cum, I want another 15 points.","smile","base","base","mid")

                                menu:

                                    "-15 points-":
                                        m "Whatever, girl! Just do it!"
                                        call cho_main("Okay.","smile","base","base","mid")
                                        "Cho leans forward and guides your cock back into her mouth."
                                        "Unexpectedly, she drives forward, roughly shoving your cock back down her throat."
                                        "The sudden stimulation coupled with her slutty expression drives you over the edge."
                                        m "Take it your plebeian whore!"
                                        #Genie cums in Cho's mouth.
                                        "Your cock twitches and your balls pull tight as you begin to dump your cum down Cho's throat."
                                        "The poor girl tries to swallow, but can't take it all. She pulls back collecting the rest in her mouth."
                                        "Her cheeks bulge with the heavy load."
                                        "When it's over your cock pops out from between the poor girls lips, leaving her struggling with the massive mouthful."
                                        call cho_main("Hmmm!","smile","base","base","mid")
                                        "Cho looks around for a place to spit it out."

                                        menu:

                                            "-Give her an empty wine glass-":
                                                "The only object in your office is a wine glass left over from your nightly chats with Snape."
                                                "You pass Ms. Chang the glass just as she dribbles a little stream of cum over her lip."
                                                call cho_main("Blehgff...","smile","base","base","mid")
                                                "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                                "After a few moments it's completely full."
                                                call cho_main("Thank you, sir.","smile","base","base","mid")
                                                #gain item [Cum Goblet]
                                                m "Yes...well, [current_payout] to Ravenclaw."
                                                jump end_cho_event

                                            "-Make her swallow it.-":
                                                m "Hey, I'm paying extra so you'd better swallow it all."
                                                call cho_main("fMmmhm mt?(Swallow it?)","smile","base","base","mid")
                                                m "You want your points, don't you?"
                                                call cho_main("(Of course, I do.)","smile","base","base","mid")
                                                call cho_main("(just pretend it's pudding.)","smile","base","base","mid")
                                                "Cho's eyes are turning red, and her overstuffed cheeks flush."
                                                call cho_main("(salty, slimy pudding....)","smile","base","base","mid")
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Blahg...","smile","base","base","mid")
                                                call cho_main("Was...","smile","base","base","mid")
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Was...that what you wanted?","smile","base","base","mid")
                                                m "Yes. [current_payout] to Ravenclaw."
                                                call cho_main("THank you, Profe-","smile","base","base","mid")
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...","smile","base","base","mid")
                                                jump end_cho_event
                                    "-5 points-":
                                        m "I'll give you 5 points."
                                        call cho_main("...deal.","smile","base","base","mid")
                                        "Cho leans forward and begins to quickly bobs her head over your cock."
                                        "Her mouth fumbles quickly around your head."
                                        "Suddenly, she wraps her hands around your balls and tugs down gently."
                                        "The sensation is suprisingly pleasant."
                                        m "Yes, take it!"
                                        #Genie cums in Cho's mouth.
                                        "Your cock twitches in Cho's mouth, dumping your cum in her mouth."
                                        "Her cheeks begin to bulge with the heavy load."
                                        "When it's over, your cock slips out of the Cho's lips, leaving her struggling with the massive mouthful."
                                        call cho_main("Hmmm!","smile","base","base","mid")
                                        "Cho looks around for a place to spit it out"

                                        menu:

                                            "-Give her an empty wine glass-":
                                                "The only object in your office is a wine glass left over from your nightly chats with Professor Snape."
                                                "You pass Ms. Chang the glass just as she dribbles a little stream of cum over her lip."
                                                call cho_main("Blehgff...","smile","base","base","mid")
                                                "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                                "After a few moments it's completely full."
                                                call cho_main("Thank you, sir.","smile","base","base","mid")
                                                #gain item [Cum Goblet]
                                                m "Yes...well, [current_payout] to Ravenclaw."
                                                jump end_cho_event
                                            "-Make her swallow it.-":
                                                m "Hey, I'm paying extra so you'd better swallow it."
                                                call cho_main("fmMmhm mt?!(Swallow it?!)","smile","base","base","mid")
                                                m "You want your points, don't you?"
                                                call cho_main("(No way, you gross, old pervert!)","smile","base","base","mid")
                                                call cho_main("(I'm gonna throw up!)","smile","base","base","mid")
                                                "Cho's eyes are turning red, and her overstuffed cheeks flush."
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Blahg...","smile","base","base","mid")
                                                call cho_main("Is...","smile","base","base","mid")
                                                call cho_main("Is...is that okay?","smile","base","base","mid")
                                                m "Very good. [current_payout] to Ravenclaw."
                                                call cho_main("THank you, Profe-","smile","base","base","mid")
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...","smile","base","base","mid")
                                                jump end_cho_event
                                    "-Fuck you!-":
                                        m "(What a bitch!)"
                                        m "You greedy whore!"
                                        "You grab your cock and quickly stroke it."
                                        "After a few fast pumps your cock explodes."
                                        #Genie cums.
                                        "After a few fast pumps your cock explodes, coating Cho in your smelly cum."
                                        call cho_main("W-what?...","smile","base","base","mid")
                                        m "[current_payout] to Ravenclaw. Now, get out of my office."
                                        call cho_main("but I can't go out like this!","smile","base","base","mid")
                                        m "Get out."
                                        call cho_main("...","smile","base","base","mid")
                                        call cho_main("...Fine!","smile","base","base","mid")
                                        $ cho_mood += 10
                                        #Cho storms out.
                                        m "Bitches..."
                                        jump end_cho_event


                        jump end_cho_event

                    "-Be mean-":
                        m "You talk too much."
                        call cho_main("I'm sor-MMPH","smile","base","base","mid")
                        "You shove your cock back in her mouth, enjoying the sputtering tightness."
                        m "That's quite all right, girl."
                        "Cho's tongue thrashes violently around your cock, getting in the way more than helping."
                        "You hold Cho's head and forcefully push your cock towards the back of her throat."
                        call cho_main("mmmph! Mmmm!","smile","base","base","mid")
                        "To your surprise the frantic writhing of her tongue feels incredible."
                        "Your cock finally pops into her tight oesophagus, and you hold it there, enjoying the warm tightness."
                        m "That's the spot..."
                        "You feel Cho pushing you back, but you're close to cumming."

                        menu:

                            "-Cum-":
                                #Genie cums in Cho's mouth.
                                call cho_main("*Glllll!* *Glp!*","smile","base","base","mid")
                                m "By the profits of Disney..."
                                call cho_main("*glp!* *Gack!*","smile","base","base","mid")
                                call cho_main("Hmmmm!","smile","base","base","mid")
                                "Cho's hands pull tight on your robes as she tries desperately to swallow your load, but your thick cum catches at the back of her throat"
                                call cho_main("Blehg!","smile","base","base","mid")
                                "Your cum spews out of Cho's mouth."
                                "The thick slime drips down her chin, soaking her uniform."
                                call cho_main("(oh god...he almost killed me...)","smile","base","base","mid")
                                call cho_main("You-you...asshole! You almost made Me drown! You better pay extra!","smile","base","base","mid")

                                menu:

                                    "-I was pretty rough. 10 extra points.-":
                                        m "Alright, Ms. Chang. [current_payout] to Ravenclaw."
                                        call cho_main("That's all? I want more next time.","smile","base","base","mid")
                                        jump end_cho_event

                                    "-What? Absolutely not.-":
                                        m "What? Absolutely not."
                                        call cho_main("But you almost killed me!","smile","base","base","mid")
                                        call cho_main("I couldn't breathe!","smile","base","base","mid")
                                        m "Take it or leave it, Ms. Chong."
                                        call cho_main("MY name is Chang, you old jerk!","smile","base","base","mid")
                                        m "DO you want your points or not?"
                                        call cho_main("yes, please.","smile","base","base","mid")
                                        m "[current_payout] to Ravenclaw."
                                        jump end_cho_event

                            "-Warn Her-":
                                m "I'm going to cum!"
                                call cho_main("Hm!","smile","base","base","mid")
                                call cho_main("Hm!...Blehrg!","smile","base","base","mid")
                                "Cho wrestles free of your grasp and spits your slippery cock out of her mouth."
                                "Your slimy cock slaps against her face, leaving a line of spit and cockslime across her nose."
                                call cho_main("i want 15 more points.","smile","base","base","mid")
                                m "What?!"
                                call cho_main("I only agreed to a blowjob. Cumming Is extra. I want another 15 points.","smile","base","base","mid")

                                menu:

                                    "-15 points-":
                                        m "It's a deal, now finish it!"
                                        call cho_main("Okay.","smile","base","base","mid")
                                        "Cho leans forward and gives your cock a few quick strokes before guiding the head into her mouth."
                                        "She continues to pump your cock while her tongue swirls around your head."
                                        "Soon, the constant stimulation drives you over the edge."
                                        m "You whore!"
                                        #Genie cums in Cho's mouth.
                                        "Your cock twitches in Cho's mouth, dumping your cum across her tongue."
                                        "Her cheeks begin to bulge with the heavy load."
                                        "When it's over, your cock pops out between the poor girls lips, leaving her struggling with the massive mouthful."
                                        call cho_main("Hmmm!","smile","base","base","mid")
                                        "Cho looks around for a place to spit it out."

                                        menu:

                                            "-Give her an empty wine glass-":
                                                "The only object in your office is a wine glass left over from your nightly chats with Snape."
                                                "You pass Ms. Chang the glass just as she dribbles a little stream of cum over her lip."
                                                call cho_main("Blehgff...","smile","base","base","mid")
                                                "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                                "After a few moments it's completely full."
                                                call cho_main("Thank you, sir.","smile","base","base","mid")
                                                #gain item [Cum Goblet]
                                                m "Yes...well, [current_payout] to Ravenclaw."
                                                jump end_cho_event

                                            "-Make her swallow it.-":
                                                m "Hey, I'm paying extra so you'd better swallow it."
                                                call cho_main("fmMmhm mt?!(Swallow it?!)","smile","base","base","mid")
                                                m "You want your points, don't you?"
                                                call cho_main("(No way, you gross, old pervert!)","smile","base","base","mid")
                                                call cho_main("(I'm gonna throw up!)","smile","base","base","mid")
                                                "Cho's eyes are turning red, and her overstuffed cheeks flush."
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Blahg...","smile","base","base","mid")
                                                call cho_main("Is...","smile","base","base","mid")
                                                call cho_main("is...is that okay?","smile","base","base","mid")
                                                m "Very good. [current_payout] to Ravenclaw."
                                                call cho_main("Thank you, Profe-","smile","base","base","mid")
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...","smile","base","base","mid")
                                                jump end_cho_event
                                    "-5 points-":
                                        m "I'll give you 5 points."
                                        call cho_main("...deal.","smile","base","base","mid")
                                        "Cho leans forward and begins to stroke your cock."
                                        "Then, pumping your cock with her fist, she leans forwards and plants a sloppy kiss on your head."
                                        "Her lips linger on your slit and she teases it with her tongue."
                                        "The intense stimulation finally pushes you over the edge."
                                        m "Yes, take it!"
                                        #Genie cums in Cho's mouth.
                                        "Your cock twitches in Cho's hand, and you begin to cum."
                                        "Cho purses her lips, letting your load fill her mouth."
                                        "Her cheeks begin to bulge with the heavy load."
                                        "When it's over, your cock slips away from Cho's lips, leaving her struggling with the massive mouthful."
                                        call cho_main("Hmmm!","smile","base","base","mid")
                                        "Cho looks around for a place to spit it out."

                                        menu:

                                            "-Give her an empty wine glass-":
                                                "The only object in your office is a wine glass left over from your nightly chats with Snape."
                                                "You pass Ms. Chang the glass just as she dribbles a little stream of cum over her lip."
                                                call cho_main("Blehgff...","smile","base","base","mid")
                                                "Your cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                                "After a few moments it's completely full."
                                                call cho_main("Thank you, sir.","smile","base","base","mid")
                                                #gain item [Cum Goblet]
                                                m "Yes...well, [current_payout] to Ravenclaw."
                                                jump end_cho_event
                                            "-Make her swallow it.-":
                                                m "Hey, I'm paying extra so you'd better swallow it."
                                                call cho_main("fMmmhm mt?(Swallow it?)","smile","base","base","mid")
                                                m "You want your points, don't you?"
                                                call cho_main("(Yes.)","smile","base","base","mid")
                                                call cho_main("(This is so gross...)","smile","base","base","mid")
                                                "Cho's eyes are turning red, and her overstuffed cheeks flush."
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Blahg...","smile","base","base","mid")
                                                call cho_main("Is...","smile","base","base","mid")
                                                call cho_main("is...is that okay?","smile","base","base","mid")
                                                m "Very good. [current_payout] to Ravenclaw."
                                                call cho_main("Thank you, Profe-","smile","base","base","mid")
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...","smile","base","base","mid")
                                                jump end_cho_event
                                    "-Fuck you!-":
                                        m "(Just who's in charge here?!)"
                                        m "You greedy bitch!"
                                        "You grab your cock and force it into Cho's mouth."
                                        call cho_main("Hmm!*Gluck!*","smile","base","base","mid")
                                        "You drive cruelly deep, bursting into her throat, and being to pump hard."
                                        call cho_main("*gack* *gack* *gack* *Gack!*","smile","base","base","mid")
                                        "After a few fast pumps you feel your balls pull tight."
                                        m "You fucking whore!"
                                        "With a cruel smile, you pull your cock out of Cho's abused throat."
                                        #Genie cums.
                                        "Your cock explodes, coating the defiant girl in your smelly cum."
                                        call cho_main("...","smile","base","base","mid")
                                        m "[current_payout] to Ravenclaw. Now, get out of my office."
                                        call cho_main("......","smile","base","base","mid")
                                        m "Get out."
                                        call cho_main("...","smile","base","base","mid")
                                        call cho_main("...O-okay...","smile","base","base","mid")
                                        $ cho_mood += 10
                                        #Cho shuffles out.
                                        m "Bitches..."
                                        jump end_cho_event


label cho_favor_3_3:
    m "Suck my cock."

    if cho_mood > 10:
        jump cho_mood_blowjob

    call cho_main("Okay!","smile","base","base","mid")
    m "Don't you want some points or something?"
    call cho_main("What?","smile","base","base","mid")
    call cho_main("Oh, yeah.","smile","base","base","mid")
    call cho_main("That'll be [current_payout] points.","smile","base","base","mid")

    menu:

        "-Let's do this-":

            m "Get on your knees and open your mouth."
            "Cho slides down to her knees and opens her mouth, sticking out her tongue."
            "The sigh of your student on her knees with her young mouth open, her soft tongue drooling over her chin is enough to drive you wild."
            "Your cock strains against your robes, leaking pre-cum all over the inside."
            call cho_main("RIke 'ish?(Like this?)","smile","base","base","mid")
            m "Very good, Ms. Chang."
            call cho_main("Honk 'ou.(Thank you.)","smile","base","base","mid")
            "You pull your rigid cock out of your robes, letting it bob just centimetres from Cho's mouth."
            "You rock your hips back and forth, teasing her."
            call cho_main("...","smile","base","base","mid")
            call cho_main("......","smile","base","base","mid")
            call cho_main("......'ey! 'Ut it in!(hey! Put it in!)","smile","base","base","mid")
            m "Beg."
            call cho_main("What?","smile","base","base","mid")
            m "Beg me for it."
            call cho_main("OkAy. um... g-give it to me.","smile","base","base","mid")
            call cho_main("please. put your cock in my...mouth?","smile","base","base","mid")

            menu:

                "-You call that begging?-":
                    m "You call that begging?"
                    call cho_main("...","smile","base","base","mid")
                    m "Come on. You can do better than that."
                    call cho_main("please. let me suck your cock.","smile","base","base","mid")
                    "You lean forward, letting your slit touch her nose."
                    "Your pre-cum leaves a slimy strand tangling between you."
                    m "You can do better than that."
                    call cho_main("...","smile","base","base","mid")
                    call cho_main("......","smile","base","base","mid")
                    call cho_main(".........","smile","base","base","mid")
                    call cho_main("............please, fuck my mouth!","smile","base","base","mid")
                    call cho_main("treat my slutty little mouth like a pussy.","smile","base","base","mid")
                    call cho_main("please, please, please let me suck your perfect, old man cock!","smile","base","base","mid")
                    call cho_main("i'll lick your balls and slurp up every drop of your slimy stuff.","smile","base","base","mid")
                    call cho_main("please, let me be your little cock sucking whore.","smile","base","base","mid")
                    m "That was...good."
                    pass

                "-Very good.-":
                    m "Very good, girl."
                    call cho_main("Thank you.","smile","base","base","mid")
                    pass

            "You finally lean forward, letting Cho take your cock in her mouth."
            call cho_main("*chomp* *ommph* *Sluuurp*","smile","base","base","mid")
            "Cho begins to worship your throbbing flesh wand, bobbing her head savagely."
            "You can feel her uvula tickling your head as she pushes herself down your cock."
            call cho_main("*oomph* *Gluck*","smile","base","base","mid")
            "Your cock prods the back of her throat, and Cho's movements suddenly stop as she fights her gag reflex."
            call cho_main("*gack!* *Cough*","smile","base","base","mid")
            "A mouthful of slime and spit spills out around your cock."
            call cho_main("Oh my god...i almost had it that time.","smile","base","base","mid")
            "Cho's mouth drips with with saliva."
            "You slap your cock against her tongue a few times before guiding it back into her slippery fuck hole."
            call cho_main("(Cheeky old man...)","smile","base","base","mid")
            m "Practice makes perfect."
            "Cho sinks down, pushing your cock deeper into her mouth."
            call cho_main("Hmmm.","smile","base","base","mid")
            m "Hold on."
            "Cho ignores you. Pushing herself down. Your cock presses against her throat."
            call cho_main("hmmmm!*Gluck!*","smile","base","base","mid")
            "Suddenly, your cock pops into her throat."
            call cho_main("Mmmm!","smile","base","base","mid")
            "The sensations are incredible. Tightness squeezes all around your cock. It's almost too much."
            "Cho begins to bob quickly up and down, dragging your sensative head through her throat."
            call cho_main("*UgG* *Gug* *Gug!*","smile","base","base","mid")
            "The girl's efforts begin to pay off and you feel yourself getting close."

            menu:

                "-Cum-":
                    ##Genie cums in Cho's mouth.
                    call cho_main("*uugg!* *Glp!*","smile","base","base","mid")
                    $ renpy.play('sounds/gulp.mp3')
                    m "I AM THE CHOSEN ONE!"
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("*glp!* *Gack!*","smile","base","base","mid")
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("Hmmmm!","smile","base","base","mid")
                    "Cho takes a finger and gently pushes the last of your cum into her mouth, smacking her lips"
                    call cho_main("You know, Professor Dumbledore, sir, your cum's not that bad.","smile","base","base","mid")
                    call cho_main("well, for A geezer, I mean.","smile","base","base","mid")
                    m "Thank you?"
                    call cho_main("i'll take my points now.","smile","base","base","mid")
                    m "..."
                    m "...Yes, of course. [current_payout] to Ravenclaw."
                    jump end_cho_event


                "-Warn Her-":
                    m "I'm going to cum!"
                    call cho_main("Hm?","smile","base","base","mid")
                    call cho_main("hm!...Blehrg!","smile","base","base","mid")
                    "Cho pushes against your legs and drags your slimy cock out of her tight throat."
                    "Your nasty cock pops out of her lips and bops her nose, leaving a dangling line of spit and pre-cum connecting you."
                    call cho_main("do you want me to eat it?","smile","base","base","mid")
                    m "What?"
                    "Cho leans forward and presses her lips against your cock."
                    call cho_main("i'll swallow all of that tasty cum if you want.","smile","base","base","mid")
                    call cho_main("and i won't even charge extra...","smile","base","base","mid")

                    menu:

                        "-Cum in her mouth.-":
                            m "I want to cum in your mouth."
                            call cho_main("Okay.","smile","base","base","mid")
                            "Cho leans forward and gives your cock a few quick strokes before sucking the head into her wet mouth."
                            "She continues to pump your cock while her tongue swirls around your head, playing with your slit."
                            "Soon the constant stimulation drives you over the edge."
                            m "You slut!"
                            #Genie cums in Cho's mouth.
                            "Your balls pull tight and your cum begins to pump into her mouth.."
                            call cho_main("Hmmmmmm....","smile","base","base","mid")
                            call cho_main("(Holy shit!)","smile","base","base","mid")
                            "Cho struggles to hold your load in her mouth."
                            "A small stream of cum is already trickling down her lips."
                            "Cho looks up into your eyes, pleadingly."

                            menu:

                                "-Give her an empty wine glass-":
                                    "The only object in your office is a wine glass left over from your nightly chats with Snape."
                                    "You pass Ms. Chang the glass just as she dribbles another little stream of cum over her lip."
                                    call cho_main("Blehgff...","smile","base","base","mid")
                                    "Your cum slowly pours out of the little witch's mouth, oozing into the wine glass."
                                    "After a few moments it's completely full."
                                    call cho_main("Thank you, sir.","smile","base","base","mid")
                                    "Cho licks around the rim of the goblet cleaning it for you."
                                    #gain item [Cum Goblet]
                                    m "[current_payout] to Ravenclaw."
                                    jump end_cho_event

                                "-Make her swallow it.-":
                                    m "Swallow it all."
                                    call cho_main("fMmmhm mt?(Swallow it?)","smile","base","base","mid")
                                    m "Yes. Swallow it like a whore."
                                    call cho_main("(Yes, sir!)","smile","base","base","mid")
                                    call cho_main("(mmmm...it's so thick and slimy.)","smile","base","base","mid")
                                    $ renpy.play('sounds/gulp.mp3')
                                    $ renpy.play('sounds/gulp.mp3')
                                    call cho_main("Muh...","smile","base","base","mid")
                                    call cho_main("...","smile","base","base","mid")
                                    call cho_main("...Yummy.","smile","base","base","mid")
                                    m "You whore. [current_payout] to Ravenclaw."
                                    call cho_main("THank you, Profe-","smile","base","base","mid")
                                    $ renpy.play('sounds/burp.mp3')
                                    call cho_main("...","smile","base","base","mid")
                                    jump end_cho_event

                        "-Cum in her throat-":
                            m "I want to cum down your throat."
                            call cho_main("Yeah?","smile","base","base","mid")
                            "Cho leans forward swallowing your cock."
                            "She rest for a moment, getting used to your size."
                            "Then, she begins to violently fuck her throat with your cock."
                            call cho_main("*gluck* *gluck* *gluck* *Gluck*","smile","base","base","mid")
                            m "By Gandalf's gay balls..."
                            call cho_main("*Hnnnng!*","smile","base","base","mid")
                            "Cho goes deep and it's suddenly too much."
                            "Your cock twitches and you being to cum."
                            #Genie cums in Cho's mouth.
                            call cho_main("!","smile","base","base","mid")
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("!...","smile","base","base","mid")
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(god, this old man...)","smile","base","base","mid")
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(So much...)","smile","base","base","mid")
                            "When it's over your cock slips away from Cho's lips, leaving her dazed."
                            call cho_main("THank you, Dumblesir...","smile","base","base","mid")
                            m "[current_payout] to Ravenclaw."
                            jump end_cho_event

                        "-Cum on her face.-":

                                m "I want to cum on your face."
                                call cho_main("you want to cover my stupid face in your cum?","smile","base","base","mid")
                                call cho_main("Okay.","smile","base","base","mid")
                                "Cho grabs your cock and forces it into her mouth."
                                call cho_main("Mmm!*Gluck!*","smile","base","base","mid")
                                "Cho pumps your cock in her mouth fiercely, ravaging her own throat."
                                call cho_main("*gack* *gack* *gack* *Gack!*","smile","base","base","mid")
                                "Finally, you feel your balls begin to tighten."
                                m "I'm almost-"
                                "Cho spits your cock out of her mouth and begins to stroke it."
                                call cho_main("Cum for me, Professor!","smile","base","base","mid")
                                ##Genie cums.
                                "Your cock explodes, coating the proud, young witch in your old wizard jizz."
                                call cho_main("Yes...","smile","base","base","mid")
                                call cho_main("Oh my god...","smile","base","base","mid")
                                call cho_main("that was amazing.","smile","base","base","mid")
                                m "[current_payout] to Ravenclaw."
                                call cho_main("...","smile","base","base","mid")
                                call cho_main("...i'm completely covered, aren't I?","smile","base","base","mid")
                                m "Get out."
                                call cho_main("...","smile","base","base","mid")
                                call cho_main("okay, Professor.","smile","base","base","mid")
                                jump end_cho_event


        "-I want to fuck your face.-":
            m "I want to fuck your face."
            call cho_main("What?...","smile","base","base","mid")
            m "I want to use your mouth like a pussy."
            call cho_main("Professor!","smile","base","base","mid")
            call cho_main("Professor! that sounds so dirty.","smile","base","base","mid")
            m "Get on your knees and open your mouth."
            call cho_main("Well...","smile","base","base","mid")
            call cho_main("Well...I am getting [current_payout] house Points...","smile","base","base","mid")
            "Cho slides down to her knees and opens her mouth, sticking her tounge out."
            call cho_main("ah Oo 'ea'y?(are you Ready?)","smile","base","base","mid")
            "Your cock throbs against your heavy robes."
            m "That's good, girl."
            "You pull out your thick wizard dick and slap it threateningly against your palm."
            call cho_main("(So scary...)","smile","base","base","mid")
            "You carefully guide your cock into Cho's soft, wet mouth."
            call cho_main("Hmmm...","smile","base","base","mid")
            call cho_main("Hmmm...(it's so thick!)","smile","base","base","mid")
            "The young witch's mouth is warm and surprisingly accommodating."
            "You push your cock deeper into her mouth."
            "You stop when you feel your thick head rest against the entrance to her throat."
            call cho_main("*Hrk!*","smile","base","base","mid")
            call cho_main("*Hrk!* *Ack!*","smile","base","base","mid")
            call cho_main("*Hrk!* *Ack!* *Glg*...","smile","base","base","mid")
            m "By the sands!"
            "To your surprise Cho forces her head forward, choking herself on your wizard dick."
            "It takes you a moment to catch your breath."
            "Then you grab Cho's head in your hands and hold tightly."
            m "There's a good witch..."
            "You drag your cock back, out of the slippery tightness of Cho's throat, stopping at the entrance."
            "Then you thrust deep, driving your it all the way to the hilt."
            call cho_main("AALG! HHHGGGGG!","smile","base","base","mid")
            call cho_main("AALG! HHhgGggG! (god he's choking me!)","smile","base","base","mid")
            "The young witch's throat feels too good, and you begin to fuck it in earnest."
            call cho_main("*glug* *GluG* *glg* *Gluck*","smile","base","base","mid")
            call cho_main("(Oh my god....)","smile","base","base","mid")
            call cho_main("*GlG* *Glg* *Glg*","smile","base","base","mid")
            call cho_main("(My throat...)","smile","base","base","mid")
            call cho_main("(My throat...feels...so good...)","smile","base","base","mid")

            menu:

                "-Cum-":
                    #Genie cums in Cho's mouth.
                    call cho_main("*uugg!* *Glp!*","smile","base","base","mid")
                    $ renpy.play('sounds/gulp.mp3')
                    m "I AM THE CHOSEN ONE!"
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("*glp!* *Gack!*","smile","base","base","mid")
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("Hmmmm!","smile","base","base","mid")
                    "Cho takes a finger and gently pushes the last of your cum into her mouth, licking her lips"
                    call cho_main("You know, Professor Dumbledore, sir, your cum's not that bad.","smile","base","base","mid")
                    call cho_main("Well, for a geezer, I mean.","smile","base","base","mid")
                    m "Thank you?"
                    call cho_main("I'll take my points now.","smile","base","base","mid")
                    m "..."
                    m "...Yes, of course. [current_payout] to Ravenclaw."
                    jump end_cho_event


                "-Warn Her-":
                    m "I'm going to cum!"
                    call cho_main("Hm?","smile","base","base","mid")
                    call cho_main("Hm!...Blehrg!","smile","base","base","mid")
                    "Cho pushes against your legs and drags your slimy cock out of her tight throat."
                    "Your nasty cock pops out between her lips and bops her nose, leaving a dangling line of spit and pre-cum connecting you."
                    call cho_main("Do you want me to drink it?","smile","base","base","mid")
                    m "What?"
                    "Cho leans forward and presses her lips against your cock."
                    call cho_main("I'll swallow all of that tasty cum if you want.","smile","base","base","mid")
                    call cho_main("And i won't even charge extra...","smile","base","base","mid")

                    menu:

                        "-Cum in her mouth.-":
                            m "I want to cum in your mouth."
                            call cho_main("Okay.","smile","base","base","mid")
                            "Cho leans forward and gives your cock a few quick strokes before guiding the head into her wet mouth."
                            "She continues to pump your cock while her tongue swirls around your head, playing with your slit."
                            "Rapidly, the constant stimulation drives you over the edge."
                            m "You slut!"
                            #Genie cums in Cho's mouth.
                            "Your balls pull tight and your cum begins to pump into her mouth.."
                            call cho_main("Hmmmmmm....","smile","base","base","mid")
                            call cho_main("(Holy shit!)","smile","base","base","mid")
                            "Cho struggles to hold your load in her mouth."
                            "A small stream of cum is already trickling down her lip."
                            "Cho looks up into your eyes, pleadingly."

                            menu:

                                "-Give her an empty wine glass-":
                                    "The only object in your office is a wine glass left over from your nightly chats with Snape."
                                    "You pass Ms. Chang the glass just as she dribbles another little stream of cum over her lip."
                                    call cho_main("Blehgff...","smile","base","base","mid")
                                    "Your cum slowly pours out of the little witch's mouth, oozing into the wine glass."
                                    "After a few moments it's completely full."
                                    call cho_main("Thank you, sir.","smile","base","base","mid")
                                    "Cho licks around the rim of the goblet cleaning it for you."
                                    #gain item [Cum Goblet]
                                    m "[current_payout] to Ravenclaw."
                                    jump end_cho_event

                                "-Make her swallow it.-":
                                    m "Swallow it all."
                                    call cho_main("fMmmhm mt?(Swallow it?)","smile","base","base","mid")
                                    m "Yes. Swallow it like a whore."
                                    call cho_main("(Yes, sir!)","smile","base","base","mid")
                                    call cho_main("(mmmm...it's so thick and slimy.)","smile","base","base","mid")
                                    $ renpy.play('sounds/gulp.mp3')
                                    $ renpy.play('sounds/gulp.mp3')
                                    call cho_main("Muh...","smile","base","base","mid")
                                    call cho_main("...","smile","base","base","mid")
                                    call cho_main("...Yummy.","smile","base","base","mid")
                                    m "You whore. [current_payout] to Ravenclaw."
                                    call cho_main("Thank you, Profe-","smile","base","base","mid")
                                    $ renpy.play('sounds/burp.mp3')
                                    call cho_main("...","smile","base","base","mid")
                                    jump end_cho_event

                        "-Cum in her throat-":
                            m "I want to cum down your throat."
                            call cho_main("Yeah?","smile","base","base","mid")
                            "Cho leans forward swallowing your cock to the hilt."
                            "She rest for a moment, getting used to your size."
                            "Then, she begins to volently fuck her throat with your cock."
                            call cho_main("*gluck* *gluck* *gluck* *Gluck*","smile","base","base","mid")
                            m "By Gandalf's gay balls..."
                            call cho_main("*Hnnnng!*","smile","base","base","mid")
                            "Cho goes deep and it's suddenly too much."
                            "Your cock twitches and you being to cum."
                            #Genie cums in Cho's mouth.
                            call cho_main("!","smile","base","base","mid")
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("!...","smile","base","base","mid")
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(god, this old man...)","smile","base","base","mid")
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(So much...)","smile","base","base","mid")
                            "When it's over, your cock slips away from Cho's lips, leaving her dazed."
                            call cho_main("Thank","smile","base","base","mid")
                            call cho_main("Thank you","smile","base","base","mid")
                            call cho_main("Thank you, Dumbledore sir...","smile","base","base","mid")
                            m "[current_payout] to Ravenclaw."
                            jump end_cho_event

                        "-Cum on her face.-":

                                m "I want to cum on your face."
                                call cho_main("you want to cover my stupid face in your cum?","smile","base","base","mid")
                                call cho_main("Okay.","smile","base","base","mid")
                                "Cho grabs your cock and forces it into her mouth."
                                call cho_main("Mmm!*Gluck!*","smile","base","base","mid")
                                "Cho pumps your cock in her mouth fiercely, ravaging her own throat."
                                call cho_main("*gack* *gack* *gack* *Gack!*","smile","base","base","mid")
                                "Finally, you feel your balls begin to tighten."
                                m "I'm almost-"
                                "Cho spits your cock out of her mouth and begins to stroke it."
                                call cho_main("Cum for me, Professor!","smile","base","base","mid")
                                ##Genie cums.
                                "Your cock explodes, coating the proud, young witch in your old wizard jizz."
                                call cho_main("Yes...","smile","base","base","mid")
                                call cho_main("Oh my god...","smile","base","base","mid")
                                call cho_main("That was amazing.","smile","base","base","mid")
                                m "[current_payout] to Ravenclaw."
                                call cho_main("...","smile","base","base","mid")
                                call cho_main("...I'm completely covered, aren't I?","smile","base","base","mid")
                                m "Get out."
                                call cho_main("...","smile","base","base","mid")
                                call cho_main("okay, Professor.","smile","base","base","mid")
                                jump end_cho_event


        "-Ms. Chong, do you eat ass?-":
            m "Ms. Chong, do you eat ass?"
            call cho_main("Are you asking or telling?","smile","base","base","mid")
            m "Get over here."
            "Cho playfully hops over to you, stopping just in front of your desk."
            call cho_main("Well?","smile","base","base","mid")
            m "(What's she doing?)"
            m "(Maybe she's trying to tell me something...)"

            menu:

                "-Treat her like a slut.-":
                    "Words are for Socialists and pussies."
                    "You suddenly grab Cho by the hair and drag her down to her knees."
                    call cho_main("!","smile","base","base","mid")
                    call cho_main("Profes-","smile","base","base","mid")
                    "Before she can say another word you pull your wizard robes open and jam your cock in her mouth."
                    call cho_main("(Yessss...)","smile","base","base","mid")
                    call cho_main("*Hrk!*","smile","base","base","mid")
                    call cho_main("*Hrk!* *Ack!*","smile","base","base","mid")
                    call cho_main("*Hrk!* *Ack!* *Glg*...","smile","base","base","mid")
                    "You can feel Cho's tongue thrashing violently around your head as she fights your hands."
                    call cho_main("*oomph* *Gluck*","smile","base","base","mid")
                    "Your cock prods the back of her throat, and Cho's movements suddenly stop as she focuses on fighting her gag reflex."
                    call cho_main("*gack!* *Cough*","smile","base","base","mid")
                    "A mouthful of slime and spit shoots out around your cock as she chokes on it."
                    call cho_main("(I'm going to die...)","smile","base","base","mid")
                    call cho_main("(You nasty, old man...)","smile","base","base","mid")
                    "Cho's chin drips with tangled cords of slime."
                    "Your balls slap against her face as you pound her slippery fuck hole."
                    call cho_main("(I'm such a whore...)","smile","base","base","mid")
                    m "That's good, you fucking whore."
                    call cho_main("(Yes!)","smile","base","base","mid")
                    "Suddenly, you feel Cho's hands tightly grip your ass, and you realise that you haven't had to hold her down."
                    "The crazed young witch desperately fucks her face against your cock."
                    "Your cock feels amazing, but you have other plans."
                    "You grab Cho's hands and push her down."
                    $ renpy.play('sounds/pop.mp3')
                    "Your cock pops out of her throat, and she falls back on her haunches."
                    m "Get over here and lick my ass."
                    call cho_main("yes, Professor!","smile","base","base","mid")
                    "Cho crawls under your robes and leans back."
                    "Suddenly, you feel a slimy, wet sensation as Cho tongue probes your hairy asshole."
                    m "That's it."
                    m "That's it. That's it..."
                    "While Cho's tongue twists and tickles your asshole you pump your thick meat wand."
                    "Cho's hands push your own away and she begins to pound your cock while tongueing your ass."
                    "Cho's hands work in concert with her tongue and it's not long before you find yourself on the edge."
                    #Genie Cums.
                    "Your cock explodes in Cho's soft, slippery hands as her tongue presses deep into your ass."
                    "Thick, heavy ropes of your cum shoot across the room, coating the floor at your feet."
                    call cho_main("Wow!","smile","base","base","mid")
                    call cho_main("Wow! that was intense...","smile","base","base","mid")
                    m "Good work, Ms. Chang. [current_payout] to Ravenclaw..."
                    call cho_main("Thank you, Professor Dumbledore.","smile","base","base","mid")
                    jump end_cho_event


label cho_mood_blowjob:
    call cho_main("I can't believe you, you old pervert.","smile","base","base","mid")
    call cho_main("Fine.","smile","base","base","mid")
    call cho_main("Fine. I'll do it.","smile","base","base","mid")
    "Cho drops to her knees and reaches into your robes grabbing your semi-hard cock."
    call cho_main("You're not even hard yet.","smile","base","base","mid")
    "Cho leans forward and after gathering saliva in her mouth she spits a messy dollop across your cockhead."
    "The angry young witch begins to roughly pump your hardening cock."
    m "Take it easy."
    call cho_main("Take it easy?","smile","base","base","mid")
    "Cho leans forward and guides your cock into her mouth."
    "Her tongue assaults your sensitive head, writhing against your glans."
    "Then she begins to bob her head back and forth, sucking hard."
    m "That's good."
    "Cho spits your cock out and pumps it with fast, rough strokes."
    call cho_main("Are you going to cum yet, you old jerk?","smile","base","base","mid")
    m "I'm almost there."
    "Cho takes your cock back into her mouth, sucking and bobbing."
    "Soon, you reach your limit, but before you can cum Cho feels your shaft twitch and pulls back."
    call cho_main("Cumming so soon?","smile","base","base","mid")
    "Cho squeezes your cock uncomfortably hard and pumps your shaft so fast that your mind reals from the twin sensations of pleasure and pain."
    ##Genie cums
    "Suddenly, your cock throbs and just as you begin to cum Cho bends your twitching cock down, forcing you to cum on the floow at your feet."
    m "Ah! Cho, you Teenage Bitch!"
    "As the last few drops of your cum splatter against the floor of your office, Cho releases your abused cock."
    "She shakes the spit and pre-cum off her hand before glaring daggers at you."
    call cho_main("well? my house Points?","smile","base","base","mid")
    m "Fine. But you're only getting [points-5], you little bitch..."
    $ cho_mood += 5
    m "[points-5] to Ravenclaw."
    call cho_main("Jerk.","smile","base","base","mid")
    jump end_cho_event
